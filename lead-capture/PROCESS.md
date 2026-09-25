# PROCESS — lead-capture

Job: turn post engagement into captured leads. Someone comments the keyword →
they get the starter kit → we get their email → they're tagged for nurture.

Trigger: `publisher` hands off a published post URL + keyword (default: PLAYBOOK).

## The flow (ManyChat — planned, not yet configured)

1. **Keyword trigger.** Comment containing `PLAYBOOK` on the linked post fires
   the flow. (Keywords armed per post — never account-wide without approval.)
2. **Public reply.** Auto-reply under their comment: short, native, points to DMs.
3. **DM #1 — the delivery.** Sends the starter-kit link/PDF + one line on what's
   inside. Exact copy below — Phillip approves every word before activation.
4. **DM #2 — the email ask.** "Where should I send the bonus playbook?" Captures
   email via quick-reply / free text.
5. **Tag + log.** Tag `playbook-lead` + source post slug. Write the lead record:
   name, IG handle, email, date, source post.
6. **Hand off.** Lead record → `lead-nurture` playbook.

## Decisions the agent makes

- None about copy — every word of the flow is Phillip-approved before activation.
- The agent drafts, proposes tags, and reports metrics (comments, DMs, emails).

## "Done right"

Flow fires only on the armed keyword + linked post, every DM matches the
approved copy character-for-character, every email captured is logged with its
source, and nothing was activated before Phillip approved the exact flow.
