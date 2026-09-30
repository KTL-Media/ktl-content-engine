-- Ledge Identity — Phase 0 foundations (PRD §9, §10, §12, §13)
-- Identity, consent, credit wallet/ledger, and job tracking.


-- ───────── enums ─────────
create type identity_status as enum ('draft','processing','review_required','approved','suspended','deleted');
create type job_status as enum ('queued','preparing_identity','generating','enhancing','completed','failed','cancelled');
create type job_type as enum ('image','image_hq','upscale','identity_reprocess','animation_5s','animation_10s');
create type ledger_type as enum ('grant','reserve','settle','refund','expire','purchase','adjustment');
create type credit_kind as enum ('starter','subscription','purchased','promo','referral');

-- ───────── users / workspace ─────────
create table profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text,
  age_confirmed_at timestamptz,
  account_status text not null default 'active' check (account_status in ('active','suspended','deleted')),
  created_at timestamptz not null default now()
);

-- ───────── consent (separate from ToS; immutable) ─────────
create table consent_records (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references profiles(id) on delete cascade,
  identity_id uuid,
  policy_version text not null,
  attestation text not null,
  allow_model_training boolean not null default false,
  withdrawn_at timestamptz,
  created_at timestamptz not null default now()
);

-- ───────── identity ─────────
create table identity_profiles (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references profiles(id) on delete cascade,
  name text not null,
  status identity_status not null default 'draft',
  identity_version int not null default 1,
  consent_id uuid references consent_records(id),
  allowed_uses jsonb not null default '{"personal":true,"commercial":false,"public_sharing":false}',
  created_at timestamptz not null default now(),
  deleted_at timestamptz
);
-- MVP: one active (non-deleted) identity per account
create unique index one_active_identity_per_user on identity_profiles(user_id) where status <> 'deleted';

alter table consent_records add constraint consent_identity_fk
  foreign key (identity_id) references identity_profiles(id) on delete set null;

create table identity_sources (
  id uuid primary key default gen_random_uuid(),
  identity_id uuid not null references identity_profiles(id) on delete cascade,
  storage_key text not null,
  quality_score numeric,
  validation_status text not null default 'pending' check (validation_status in ('pending','accepted','rejected')),
  rejection_reason text,
  created_at timestamptz not null default now()
);

-- ───────── worlds / projects / jobs / assets ─────────
create table world_templates (
  id uuid primary key default gen_random_uuid(),
  category text not null,
  title text not null,
  prompt_template text not null,
  settings_schema jsonb not null default '{}',
  safety_policy jsonb not null default '{}',
  active boolean not null default true
);

create table projects (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references profiles(id) on delete cascade,
  name text not null,
  identity_id uuid references identity_profiles(id),
  visibility text not null default 'private' check (visibility in ('private','unlisted','public')),
  created_at timestamptz not null default now()
);

create table generation_jobs (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references profiles(id) on delete cascade,
  project_id uuid references projects(id) on delete set null,
  identity_id uuid not null references identity_profiles(id),
  world_id uuid references world_templates(id),
  type job_type not null,
  status job_status not null default 'queued',
  prompt text,
  settings jsonb not null default '{}',
  provider text,
  model_version text,
  credit_cost int not null check (credit_cost >= 0),
  error text,
  idempotency_key text,
  created_at timestamptz not null default now(),
  completed_at timestamptz,
  unique (user_id, idempotency_key)
);

create table media_assets (
  id uuid primary key default gen_random_uuid(),
  job_id uuid not null references generation_jobs(id) on delete cascade,
  user_id uuid not null references profiles(id) on delete cascade,
  kind text not null check (kind in ('image','video')),
  storage_key text not null,
  visibility text not null default 'private' check (visibility in ('private','unlisted','public')),
  provenance jsonb not null default '{}',
  created_at timestamptz not null default now()
);

-- ───────── credits: wallet + immutable ledger ─────────
create table credit_wallets (
  user_id uuid primary key references profiles(id) on delete cascade,
  available int not null default 0 check (available >= 0),
  reserved int not null default 0 check (reserved >= 0)
);

create table credit_ledger (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references profiles(id) on delete cascade,
  type ledger_type not null,
  kind credit_kind,
  amount int not null,               -- signed change to `available`
  job_id uuid references generation_jobs(id),
  expires_at timestamptz,
  note text,
  created_at timestamptz not null default now()
);
-- exactly one reserve / settle-or-refund per job: replayed calls can't double charge
create unique index ledger_one_reserve_per_job on credit_ledger(job_id) where type = 'reserve';
create unique index ledger_one_resolution_per_job on credit_ledger(job_id) where type in ('settle','refund');

create table audit_events (
  id bigint generated always as identity primary key,
  user_id uuid,
  action text not null,
  target_id uuid,
  meta jsonb not null default '{}',
  created_at timestamptz not null default now()
);

-- ledger + audit + consent are append-only
create function forbid_mutation() returns trigger language plpgsql as $$
begin raise exception '% is append-only', tg_table_name; end $$;
create trigger ledger_append_only before update or delete on credit_ledger
  for each row execute function forbid_mutation();
create trigger audit_append_only before update or delete on audit_events
  for each row execute function forbid_mutation();

-- ───────── credit functions (service role only) ─────────
create function grant_credits(p_user uuid, p_amount int, p_kind credit_kind, p_expires timestamptz default null, p_note text default null)
returns void language plpgsql security definer set search_path = public as $$
begin
  if p_amount <= 0 then raise exception 'grant must be positive'; end if;
  insert into credit_wallets(user_id, available) values (p_user, p_amount)
    on conflict (user_id) do update set available = credit_wallets.available + p_amount;
  insert into credit_ledger(user_id, type, kind, amount, expires_at, note)
    values (p_user, 'grant', p_kind, p_amount, p_expires, p_note);
end $$;

-- Moves credits available -> reserved and writes the reserve entry. Fails on insufficient balance.
create function reserve_credits(p_job uuid)
returns void language plpgsql security definer set search_path = public as $$
declare j generation_jobs%rowtype; w credit_wallets%rowtype;
begin
  select * into j from generation_jobs where id = p_job for update;
  if not found then raise exception 'job not found'; end if;
  select * into w from credit_wallets where user_id = j.user_id for update;
  if w.available < j.credit_cost then raise exception 'insufficient credits'; end if;
  update credit_wallets set available = available - j.credit_cost, reserved = reserved + j.credit_cost
    where user_id = j.user_id;
  insert into credit_ledger(user_id, type, amount, job_id) values (j.user_id, 'reserve', -j.credit_cost, p_job);
end $$;

-- Success: release the reservation (charge stays). Failure: return credits to available.
create function resolve_credits(p_job uuid, p_success boolean)
returns void language plpgsql security definer set search_path = public as $$
declare j generation_jobs%rowtype;
begin
  select * into j from generation_jobs where id = p_job for update;
  if not found then raise exception 'job not found'; end if;
  if p_success then
    update credit_wallets set reserved = reserved - j.credit_cost where user_id = j.user_id;
    insert into credit_ledger(user_id, type, amount, job_id) values (j.user_id, 'settle', 0, p_job);
  else
    update credit_wallets set reserved = reserved - j.credit_cost, available = available + j.credit_cost
      where user_id = j.user_id;
    insert into credit_ledger(user_id, type, amount, job_id) values (j.user_id, 'refund', j.credit_cost, p_job);
  end if;
end $$;

revoke all on function grant_credits, reserve_credits, resolve_credits from public, anon, authenticated;
grant execute on function grant_credits, reserve_credits, resolve_credits to service_role;

-- ───────── signup: profile + wallet + starter credits ─────────
create function handle_new_user() returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into profiles(id, display_name) values (new.id, split_part(new.email, '@', 1));
  insert into credit_wallets(user_id) values (new.id);
  perform grant_credits(new.id, 50, 'starter', now() + interval '90 days', 'signup starter grant');
  return new;
end $$;
create trigger on_auth_user_created after insert on auth.users
  for each row execute function handle_new_user();

-- ───────── row level security: users see only their own data ─────────
alter table profiles enable row level security;
alter table consent_records enable row level security;
alter table identity_profiles enable row level security;
alter table identity_sources enable row level security;
alter table world_templates enable row level security;
alter table projects enable row level security;
alter table generation_jobs enable row level security;
alter table media_assets enable row level security;
alter table credit_wallets enable row level security;
alter table credit_ledger enable row level security;
alter table audit_events enable row level security;

create policy own_profile_read on profiles for select using (id = auth.uid());
create policy own_profile_update on profiles for update using (id = auth.uid()) with check (id = auth.uid());
create policy own_consent_read on consent_records for select using (user_id = auth.uid());
create policy own_consent_insert on consent_records for insert with check (user_id = auth.uid());
create policy own_identity_read on identity_profiles for select using (user_id = auth.uid());
create policy own_identity_insert on identity_profiles for insert with check (user_id = auth.uid() and status = 'draft');
create policy own_sources_read on identity_sources for select
  using (exists (select 1 from identity_profiles i where i.id = identity_id and i.user_id = auth.uid()));
create policy worlds_read on world_templates for select using (active);
create policy own_projects_all on projects for all using (user_id = auth.uid()) with check (user_id = auth.uid());
create policy own_jobs_read on generation_jobs for select using (user_id = auth.uid());
create policy own_assets_read on media_assets for select using (user_id = auth.uid());
create policy own_wallet_read on credit_wallets for select using (user_id = auth.uid());
create policy own_ledger_read on credit_ledger for select using (user_id = auth.uid());
-- Writes to jobs, assets, wallet, ledger, sources, and audit go through the service role only (no policies).

-- ───────── seed worlds ─────────
insert into world_templates(category, title, prompt_template) values
  ('professional','Studio headshot','Professional studio headshot of {{identity}}, soft key light, neutral backdrop'),
  ('cinematic','Film still','Cinematic film still of {{identity}}, anamorphic lens, moody practical lighting'),
  ('music','Album cover','Album cover concept featuring {{identity}}, bold typography space, editorial lighting'),
  ('illustrated','Comic avatar','Comic-book avatar of {{identity}}, inked lines, flat color');
