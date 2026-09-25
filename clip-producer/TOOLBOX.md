# TOOLBOX — clip-producer

## Commands

```bash
cd ~/workspace/skills/clip-farm
.venv/bin/python scripts/03_find_moments.py --out work/<slug>/ --top 20
.venv/bin/python scripts/04_render.py --out work/<slug>/ --start 372.5 --end 405.0 --name clip01
```

## Moment-pick rubric (score each candidate 1–5)

- **Hook:** does the first line make a stranger stop? ("Stop building 15 half-broken agents.")
- **Self-contained:** makes sense with zero context from the long-form.
- **Payoff:** ends on a takeaway, punchline, or number — not trailing off.
- **Clip-ability:** 20–45s of dense speech, no long pauses or filler.

Pick the top scorers; ties go to the stronger hook.

## Render spec

- 1080×1920, 9:16, H.264 mp4.
- Face-tracked crop via YuNet (`models/face_yunet.onnx`); center-crop fallback
  when no face (slides, screen-share).
- Karaoke captions: word-level highlight, big bold font, safe margins top/bottom.

## Pick-sheet format

```
clip01 | 00:06:12–00:06:47 | "Stop building 15 half-broken agents..."
       | why: cold-open hook + the whole thesis in 35s. LEAD CLIP.
```

## Corrections log

- 2026-09-24: smoke test — synthetic source had no face, center crop correct.
  Old Haar cascades missing from installed OpenCV; renderer now uses YuNet.
