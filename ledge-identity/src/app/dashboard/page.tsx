import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";

// Dev-only stand-in for the Phase 1 capture/quality pipeline.
async function devApprove(formData: FormData) {
  "use server";
  if (process.env.NODE_ENV === "production") return;
  const { createAdminClient } = await import("@/lib/supabase/admin");
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) return;
  await createAdminClient().from("identity_profiles").update({ status: "approved" })
    .eq("id", String(formData.get("id"))).eq("user_id", user.id);
  redirect("/dashboard");
}

export default async function Dashboard() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  if (!user) redirect("/login");

  const [{ data: wallet }, { data: identity }, { data: ledger }] = await Promise.all([
    supabase.from("credit_wallets").select("available,reserved").maybeSingle(),
    supabase.from("identity_profiles").select("id,name,status").neq("status", "deleted").maybeSingle(),
    supabase.from("credit_ledger").select("id,type,amount,created_at").order("created_at", { ascending: false }).limit(10),
  ]);
  if (!identity) redirect("/onboarding/consent");

  return (
    <main style={{ maxWidth: 720, margin: "3rem auto", padding: "0 16px" }}>
      <h1>Dashboard</h1>
      <p>Credits: <strong>{wallet?.available ?? 0}</strong> available, {wallet?.reserved ?? 0} reserved</p>
      <p>Identity: {identity.name} — <em>{identity.status}</em></p>
      {identity.status !== "approved" && process.env.NODE_ENV !== "production" && (
        <form action={devApprove}>
          <input type="hidden" name="id" value={identity.id} />
          <button>Dev: mark identity approved</button>
        </form>
      )}
      <h2>Recent credit activity</h2>
      <ul>{ledger?.map((l) => <li key={l.id}>{l.type}: {l.amount}</li>)}</ul>
    </main>
  );
}
