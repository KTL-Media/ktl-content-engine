# TOOLBOX — content-intake

Approved tools and commands. Reach for these every run; add corrections here,
not in the chat.

## Commands

```bash
cd ~/workspace/skills/clip-farm
# ingest (YouTube or file)
.venv/bin/python scripts/01_ingest.py --url <url> --out work/<slug>/
.venv/bin/python scripts/01_ingest.py --file <local.mp4> --out work/<slug>/
# trim dead air
.venv/bin/python scripts/01_ingest.py --url <url> --out work/<slug>/ --sections "00:05:00-02:30:00"
# transcribe
.venv/bin/python scripts/02_transcribe.py --out work/<slug>/ --model base
```

## Known quirks (fixed in-script, keep them fixed)

- Bracketed IPv6 entries in `no_proxy` crash the transcription HTTP client —
  `02_transcribe.py` sanitizes them. Don't "clean up" that code.
- Some TTS WAVs carry an ID3-prefixed RIFF header ffmpeg can't read — strip
  bytes before the `RIFF` marker first.
- YouTube bot-checks the default yt-dlp client: use `--extractor-args
  "youtube:player_client=android"`. The egress proxy's self-signed cert must be
  appended to the venv's certifi bundle before the android client works.

## Transcript QC rubric

- [ ] Duration of transcript ≈ duration of audio (±1%)
- [ ] 3 random segments checked against audio — no gibberish runs
- [ ] Proper nouns / brand terms ("GIT BUILT", "Imaginarium", speaker names) spelled right
- [ ] No 30+ second gaps with no words unless it's genuinely silent

## Log line format

`<date> | <slug> | <source-url> | <duration> | <segments> segs / <words> words | model=<base|small> | notes`
