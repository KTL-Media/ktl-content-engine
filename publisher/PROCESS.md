# PROCESS — publisher

Job: take finished clips and turn them into posted Reels — with captions,
hooks, hashtags, and a schedule — only after Phillip approves each exact post.

Trigger: `clip-producer` hands off `clips/clipNN.mp4` + pick sheet.

## Steps

1. **Draft the caption.** Hook line (the clip's own hook, verbatim if strong)
   + 1–2 lines of context + CTA + 3–5 hashtags. If a lead magnet sits behind
   the clip, the CTA is always: `Comment PLAYBOOK and I'll DM you the free starter kit.`
2. **Draft 2 hook variants** for the on-screen title / first caption line.
   Phillip picks or rewrites.
3. **Propose the schedule.** 1 clip/day max to start, best windows: 7–9am and
   12–1pm ET. Note the target account per post (`@phil_moreland` vs brand).
4. **Submit for approval.** Show Phillip: the exact clip (he watches it), the
   exact caption text, the exact account, the scheduled time. He approves each
   post individually — one "yes" does not cover the batch.
5. **Post only on explicit approval.** Via `05_ship.py` (`--clip … --account …
   --caption "…"`) or the IG app. Log the post URL back to the work dir.
6. **Hand off.** Published post URL + keyword armed → `lead-capture` playbook.

## Decisions the agent makes

- Caption draft and hook variants. Hashtag picks. Schedule proposal.
- Phillip makes: final caption, account, timing, and the go/no-go per post.

## "Done right"

Every published post has a logged approval (exact clip + exact caption +
account + time), the caption passed PROOF, the post URL is recorded, and
`lead-capture` knows which keyword to listen for. Unapproved clips stay in the
work dir — never posted.
