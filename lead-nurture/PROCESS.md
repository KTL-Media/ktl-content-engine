# PROCESS — lead-nurture

Job: turn captured leads into clients with a short, value-first follow-up
sequence. No spam, no pressure — earn the reply.

Trigger: `lead-capture` hands off a lead record (name, handle, email, source post).

## The sequence (email + IG DM, Phillip approves every message before activation)

- **Day 0 — welcome.** Deliver value immediately: the kit + the one thing to do
  first. One ask max: reply with their #1 bottleneck.
- **Day 2 — proof.** A real result or teardown: what the delegation loop did for
  a business like theirs. Keep it concrete, no hype.
- **Day 5 — the offer.** Soft: "GIT BUILT builds this for operators — want me to
  map it for your business? Reply MAP." No hard close.
- **Day 9 — last touch.** One line: the door's open. Then stop. Silence is an answer.

## Reply handling

- Any reply → stop the sequence for that lead, flag to Phillip same day.
- `replied-setup` / hot intent → Phillip handles personally, agent drafts the
  reply for his approval.
- Unsubscribe / "stop" → remove immediately, log it, never contact again.

## Segmentation

- `email-captured` → full sequence.
- Kit-only (no email) → DM-only touches, Day 0 and Day 5.

## "Done right"

Every lead gets the right sequence for their segment, every message sent
matches approved copy, every reply stops the automation and reaches Phillip,
and unsubscribes are honored same day. Leads become conversations;
conversations become clients.
