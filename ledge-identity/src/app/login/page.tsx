import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";

async function auth(formData: FormData) {
  "use server";
  const email = String(formData.get("email"));
  const password = String(formData.get("password"));
  const mode = String(formData.get("mode"));
  const supabase = await createClient();
  const { error } =
    mode === "signup"
      ? await supabase.auth.signUp({ email, password })
      : await supabase.auth.signInWithPassword({ email, password });
  if (error) redirect(`/login?error=${encodeURIComponent(error.message)}`);
  redirect("/dashboard");
}

export default async function Login({ searchParams }: { searchParams: Promise<{ error?: string }> }) {
  const { error } = await searchParams;
  return (
    <main style={{ maxWidth: 360, margin: "4rem auto", padding: "0 16px" }}>
      <h1>Ledge Identity</h1>
      <form action={auth} style={{ display: "grid", gap: 12 }}>
        <label>Email<input name="email" type="email" required style={{ width: "100%" }} /></label>
        <label>Password<input name="password" type="password" minLength={8} required style={{ width: "100%" }} /></label>
        {error && <p role="alert">{error}</p>}
        <button name="mode" value="signin">Sign in</button>
        <button name="mode" value="signup">Create account</button>
      </form>
    </main>
  );
}
