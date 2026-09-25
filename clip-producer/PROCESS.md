# PROCESS — clip-producer

Job: turn a word-level transcript into 3–5 finished 1080×1920 vertical clips
with karaoke captions, ready for Phillip's review.

Trigger: `content-intake` hands off `work/<slug>/transcript.json`, or Phillip
names timestamps himself.

## Steps

1. **Generate candidates.**
   `.venv/bin/python scripts/03_find_moments.py --out work/<slug>/ --top 20`
   Produces `moments.json` — heuristic 20–45s windows. These are suggestions,
   not picks.
2. **Read like an editor.** Read the candidates AND the transcript around them.
   Hunt for: cold-open hooks, hot takes, stories with a payoff, hard numbers,
   quotable one-liners, anything that makes a stranger stop scrolling.
3. **Make the pick sheet.** 3–5 clips. Each entry: name (clip01…), start/end
   timestamps, the hook line verbatim, one-line why-it-works. Aim 20–45s per clip.
   If Phillip gave timestamps, use his — his call overrides the heuristics.
4. **Render each clip.**
   `.venv/bin/python scripts/04_render.py --out work/<slug>/ --start <s> --end <e> --name clip01`
   Face-tracked 9:16 crop (center crop fallback), karaoke word-highlight captions.
   Produces `clips/clip01.mp4`.
5. **Watch every render.** Eyes on the actual video: framing holds the face,
   captions are readable and in sync, no glitch frames, audio is clean.
6. **Hand off.** Pick sheet + `clips/*.mp4` go to the `publisher` playbook.
   Flag your #1 clip and why.

## Decisions the agent makes

- Final picks (Phillip can always override with his own timestamps).
- Clip boundaries: start on the hook, end on the payoff — never mid-sentence.
- Which clip leads the batch.

## "Done right"

3–5 clips, each 20–45s, each opening with a hook in the first 3 seconds,
karaoke captions readable on a phone, agent watched every render end to end.
Nothing posted — clips go to `publisher` for captioning and Phillip's approval.
