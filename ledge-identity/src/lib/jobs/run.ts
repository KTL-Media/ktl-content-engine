import type { SupabaseClient } from "@supabase/supabase-js";
import type { GenerationProvider } from "../providers/types";

type JobRow = {
  id: string; user_id: string; identity_id: string; type: string; prompt: string | null;
  settings: Record<string, unknown>;
};

/**
 * Runs a reserved job to completion: queued -> generating -> completed|failed.
 * Credits: success settles the reservation; any failure refunds it. Both paths are
 * idempotent at the DB level (one reserve / one resolution per job).
 */
export async function runJob(db: SupabaseClient, provider: GenerationProvider, jobId: string) {
  const { data: job, error } = await db.from("generation_jobs").select("*").eq("id", jobId).single<JobRow>();
  if (error || !job) throw new Error("job not found");

  await db.from("generation_jobs").update({ status: "generating" }).eq("id", jobId);
  try {
    const out = await provider.generate({
      jobId, identityId: job.identity_id, prompt: job.prompt ?? "",
      type: job.type as never, settings: job.settings,
    });
    await db.from("media_assets").insert(
      out.outputs.map((o) => ({
        job_id: jobId, user_id: job.user_id, kind: o.kind, storage_key: o.storageKey,
        provenance: { generated: true, provider: out.provider, model: out.modelVersion },
      })),
    );
    await db.from("generation_jobs").update({
      status: "completed", provider: out.provider, model_version: out.modelVersion,
      completed_at: new Date().toISOString(),
    }).eq("id", jobId);
    await db.rpc("resolve_credits", { p_job: jobId, p_success: true });
    return { status: "completed" as const };
  } catch (e) {
    await db.from("generation_jobs").update({
      status: "failed", error: e instanceof Error ? e.message : "unknown error",
      completed_at: new Date().toISOString(),
    }).eq("id", jobId);
    await db.rpc("resolve_credits", { p_job: jobId, p_success: false });
    return { status: "failed" as const };
  }
}
