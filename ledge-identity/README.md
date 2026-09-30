# Ledge Identity

Persistent, consent-based AI visual identity platform. Spec: [`../docs/prds/ledge-identity-prd.md`](../docs/prds/ledge-identity-prd.md).

Stack: Next.js (App Router, TypeScript) + Supabase (auth, Postgres, storage).

## Status: Phase 0 foundations

| Built | PRD ref |
|---|---|
| Email auth, route protection (`src/proxy.ts`) | §9.1 |
| Explicit consent flow: age, ownership, processing, optional training opt-in (default off); versioned consent records | §10 |
| One active identity per account (DB-enforced) | §9.2 |
| Credit wallet + append-only ledger; reserve / settle / refund as atomic SQL functions; replay-safe | §9.9, §13 |
| Job runner (`queued → generating → completed/failed`) with credit settlement, idempotency keys | §12 |
| Provider interface + stub provider | §12 |
| RLS: users read only their own rows; all writes to wallet/jobs/assets go through the service role | §11 |

**Stubbed / not built yet:** photo upload + quality validation, real identity creation, image/video providers, moderation, Stripe, World Explorer UI, sharing, referrals, admin console, account/identity deletion. The dashboard has a dev-only "mark identity approved" button standing in for the identity pipeline.

## Run

```bash
cp .env.example .env.local   # fill in Supabase project values
# apply supabase/migrations/0001_foundations.sql in the Supabase SQL editor (or supabase db push)
npm install --legacy-peer-deps
npm run dev
npm test      # runs the real migration in PGlite and tests wallet/ledger invariants
```

Generate via API: `POST /api/jobs` `{identityId, type, prompt, variations, idempotencyKey}` (prompt containing `[fail]` exercises the refund path).

## Next (Phase 1)
1. Photo upload to private storage + validation; `identity_sources` rows
2. Pick an identity-consistency + image provider; replace `stubProvider`; move job execution to a queue worker
3. Moderation before/after generation; reporting + takedown
4. Stripe subscriptions and credit packs; World Explorer UI
5. Identity + account deletion flow; retention policy; legal review before any alpha (biometric privacy)
