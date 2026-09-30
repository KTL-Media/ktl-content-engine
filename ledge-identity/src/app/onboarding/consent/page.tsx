import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";

const CONSENT_POLICY_VERSION = "2026-09-v1";

async function createIdentity(formData: FormData) {
  "use server";
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect("/login");

  // Every box is required: age, ownership, and purpose-specific consent (PRD §10)
  const required = ["age", "ownership", "processing"];
  if (!required.every((k) => formData.get(k) === "on")) redirect("/onboarding/consent?error=all+confirmations+required");

  await supabase.from("profiles").update({ age_confirmed_at: new Date().toISOString() }).eq("id", user.id);
  const { data: consent, error: cErr } = await supabase.from("consent_records").insert({
    user_id: user.id,
    policy_version: CONSENT_POLICY_VERSION,
    attestation: "I am the person depicted, or have legal authority to use these images, and authorize creation of this identity.",
    allow_model_training: formData.get("training") === "on", // separate opt-in, default off
  }).select("id").single();
  if (cErr || !consent) redirect("/onboarding/consent?error=could+not+record+consent");

  const { data: identity, error: iErr } = await supabase.from("identity_profiles")
    .insert({ user_id: user.id, name: String(formData.get("name") || "My identity"), consent_id: consent.id })
    .select("id").single();
  if (iErr || !identity) redirect("/onboarding/consent?error=you+already+have+an+identity");
  // Link both directions with the service role; users have no UPDATE policy on consent or identity rows.
  const admin = createAdminClient();
  await admin.from("consent_records").update({ identity_id: identity.id }).eq("id", consent.id);
  redirect("/dashboard");
}

export default async function Consent({ searchParams }: { searchParams: Promise<{ error?: string }> }) {
  const { error } = await searchParams;
  return (
    <main style={{ maxWidth: 560, margin: "3rem auto", padding: "0 16px" }}>
      <h1>Create your identity</h1>
      <p>
        Your photos and the identity derived from them are used only to generate content for you. You can
        delete them at any time.
      </p>
      <form action={createIdentity} style={{ display: "grid", gap: 12 }}>
        <label>Identity name<input name="name" defaultValue="My identity" /></label>
        <label><input type="checkbox" name="age" /> I confirm I meet the minimum age requirement.</label>
        <label><input type="checkbox" name="ownership" /> I am the person depicted, or I have legal authority to use these images.</label>
        <label><input type="checkbox" name="processing" /> I consent to my photos being processed to create a reusable identity.</label>
        <label><input type="checkbox" name="training" /> (Optional) Allow my data to help improve general models. Off by default.</label>
        {error && <p role="alert">{error}</p>}
        <button>Continue</button>
      </form>
    </main>
  );
}
