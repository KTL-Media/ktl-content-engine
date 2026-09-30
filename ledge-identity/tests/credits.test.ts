import { readFileSync } from "node:fs";
import { beforeAll, describe, expect, it } from "vitest";
import { PGlite } from "@electric-sql/pglite";
import { jobCost } from "../src/lib/credits/costs";

// Minimal Supabase shims so the real migration runs unmodified.
const SHIM = `
create schema auth;
create table auth.users (id uuid primary key default gen_random_uuid(), email text);
create function auth.uid() returns uuid language sql as $$ select null::uuid $$;
create role anon; create role authenticated; create role service_role;
`;

let db: PGlite;
beforeAll(async () => {
  db = new PGlite();
  await db.exec(SHIM);
  await db.exec(readFileSync("supabase/migrations/0001_foundations.sql", "utf8"));
});

async function newUser(email: string) {
  const r = await db.query<{ id: string }>("insert into auth.users(email) values ($1) returning id", [email]);
  return r.rows[0].id;
}
async function newJob(user: string, cost: number) {
  const i = await db.query<{ id: string }>("insert into identity_profiles(user_id,name,status) values ($1,'x','approved') returning id", [user]);
  const j = await db.query<{ id: string }>(
    "insert into generation_jobs(user_id,identity_id,type,credit_cost) values ($1,$2,'image',$3) returning id", [user, i.rows[0].id, cost]);
  return j.rows[0].id;
}
const wallet = async (u: string) => (await db.query<{ available: number; reserved: number }>("select available,reserved from credit_wallets where user_id=$1", [u])).rows[0];

describe("credit costs", () => {
  it("applies the 4-variation bundle discount", () => {
    expect(jobCost("image", 1)).toBe(5);
    expect(jobCost("image", 4)).toBe(16);
  });
});

describe("wallet + ledger", () => {
  it("grants 50 starter credits on signup", async () => {
    const u = await newUser("a@x.com");
    expect(await wallet(u)).toEqual({ available: 50, reserved: 0 });
  });

  it("reserve -> settle keeps the charge", async () => {
    const u = await newUser("b@x.com");
    const j = await newJob(u, 30);
    await db.query("select reserve_credits($1)", [j]);
    expect(await wallet(u)).toEqual({ available: 20, reserved: 30 });
    await db.query("select resolve_credits($1,true)", [j]);
    expect(await wallet(u)).toEqual({ available: 20, reserved: 0 });
  });

  it("reserve -> refund restores the balance", async () => {
    const u = await newUser("c@x.com");
    const j = await newJob(u, 30);
    await db.query("select reserve_credits($1)", [j]);
    await db.query("select resolve_credits($1,false)", [j]);
    expect(await wallet(u)).toEqual({ available: 50, reserved: 0 });
  });

  it("rejects insufficient balance", async () => {
    const u = await newUser("d@x.com");
    const j = await newJob(u, 60);
    await expect(db.query("select reserve_credits($1)", [j])).rejects.toThrow(/insufficient/);
  });

  it("cannot double-reserve or double-resolve a job", async () => {
    const u = await newUser("e@x.com");
    const j = await newJob(u, 10);
    await db.query("select reserve_credits($1)", [j]);
    await expect(db.query("select reserve_credits($1)", [j])).rejects.toThrow();
    await db.query("select resolve_credits($1,false)", [j]);
    await expect(db.query("select resolve_credits($1,false)", [j])).rejects.toThrow();
    expect(await wallet(u)).toEqual({ available: 50, reserved: 0 });
  });

  it("ledger is append-only", async () => {
    await expect(db.query("update credit_ledger set amount = 999")).rejects.toThrow(/append-only/);
    await expect(db.query("delete from credit_ledger")).rejects.toThrow(/append-only/);
  });

  it("allows only one active identity per user", async () => {
    const u = await newUser("f@x.com");
    await db.query("insert into identity_profiles(user_id,name) values ($1,'one')", [u]);
    await expect(db.query("insert into identity_profiles(user_id,name) values ($1,'two')", [u])).rejects.toThrow();
  });
});
