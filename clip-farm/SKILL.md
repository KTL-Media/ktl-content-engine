# clip-farm

Agentic clip farm: turn Phillip's long-form content (livestreams, Zooms, podcasts)
into vertical short-form clips with word-highlight captions, ready to ship.

## The loop

Skooly is the agent in this pipeline. Stages are scripts; judgment calls are mine.

1. **Ingest** — pull the long-form source:
   `scripts/01_ingest.py --url <youtube-url> --out work/<slug>/ [--sections "00:10:00-00:40:00"]`
   or `--file <local.mp4>`. Produces `source.mp4` + `audio.wav`.
2. **Transcribe** — word-level timestamps:
   `.venv/bin/python scripts/02_transcribe.py --out work/<slug>/ [--model base]`
   Produces `transcript.json`. (`small` is better if time allows.)
3. **Find moments** — heuristic candidates:
   `.venv/bin/python scripts/03_find_moments.py --out work/<slug>/ --top 20`
   Produces `moments.json`. I read the candidates and the transcript, then make
   the final pick — hooks, hot takes, stories, numbers. Aim 20–45s per clip.
4. **Render** — face-tracked 9:16 crop + karaoke captions:
   `.venv/bin/python scripts/04_render.py --out work/<slug>/ --start <s> --end <e> --name clip01`
   Produces `clips/clip01.mp4` (1080x1920). I watch the render before shipping.
5. **Ship** — ONLY with Phillip's explicit approval, per the standing gate:
   `.venv/bin/python scripts/05_ship.py --clip work/<slug>/clips/clip01.mp4 --account imaginarium2026 --caption "..."`

Work dirs live under `~/workspace/skills/clip-farm/work/<slug>/` (gitignored, heavy).
Nothing is posted, published, or sent without Phillip approving the exact clip first.

## Caption style

Captions follow the carousel CTA convention when there's a lead magnet behind the
clip (e.g. "Comment PLAYBOOK and I'll DM it to you"). Otherwise keep it native:
hook line + 3-5 hashtags.

## Notes

- Python deps live in `.venv/` (faster-whisper, opencv, yt-dlp). System pip is
  Debian-managed — never `pip install` outside the venv.
- Haar-cascade face detect; falls back to center crop when no face found.
- Clip picks are the agent's call, but Phillip can always name timestamps himself.
