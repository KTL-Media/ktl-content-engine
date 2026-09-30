import { NextResponse } from "next/server";
import { z } from "zod";
import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";
import { jobCost } from "@/lib/credits/costs";
import { runJob } from "@/lib/jobs/run";
import { stubProvider } from "@/lib/providers/stub";

const Body = z.object({
  identityId: z.uuid(),
  worldId: z.uuid().optional(),
  type: z.enum(["image", "image_hq", "upscale", "animation_5s", "animation_10s"]),
  prompt: z.string().max(1000).default(""),
  variations: z.union([z.literal(1), z.literal(2), z.literal(4)]).default(1),
  idempotencyKey: z.string().min(8).max(100),
});

export async function POST(req: Request) {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) return NextResponse.json({ error: "unauthorized" }, { status: 401 });

  const parsed = Body.safeParse(await req.json().catch(() => null));
  if (!parsed.success) return NextResponse.json({ error: "invalid request" }, { status: 400 });
  const b = parsed.data;

  // RLS-scoped read: only the caller's own approved identity is visible
  const { data: identity } = await supabase
    .from("identity_profiles").select("id,status").eq("id", b.identityId).maybeSingle();
  if (!identity || identity.status !== "approved")
    return NextResponse.json({ error: "identity not approved" }, { status: 403 });

  const db = createAdminClient();
  const { data: existing } = await db.from("generation_jobs").select("id,status")
    .eq("user_id", user.id).eq("idempotency_key", b.idempotencyKey).maybeSingle();
  if (existing) return NextResponse.json(existing);

  const cost = jobCost(b.type, b.variations);
  const { data: job, error } = await db.from("generation_jobs").insert({
    user_id: user.id, identity_id: b.identityId, world_id: b.worldId, type: b.type,
    prompt: b.prompt, settings: { variations: b.variations }, credit_cost: cost,
    idempotency_key: b.idempotencyKey,
  }).select("id,status").single();
  if (error || !job) return NextResponse.json({ error: "could not create job" }, { status: 500 });

  const { error: reserveErr } = await db.rpc("reserve_credits", { p_job: job.id });
  if (reserveErr) {
    await db.from("generation_jobs").update({ status: "failed", error: "insufficient credits" }).eq("id", job.id);
    return NextResponse.json({ error: "insufficient credits", cost }, { status: 402 });
  }

  await db.from("audit_events").insert({ user_id: user.id, action: "generation_started", target_id: job.id });
  // Foundations: run inline with the stub provider. Replace with a queue worker in Phase 1.
  const result = await runJob(db, stubProvider, job.id);
  return NextResponse.json({ id: job.id, cost, ...result });
}
