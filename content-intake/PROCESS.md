# PROCESS — content-intake

Job: get Phillip's long-form content in and transcribed, ready for clip-picking.

Trigger: Phillip names a source (YouTube URL, Zoom replay, local file) or points
at a new recording that needs clipping.

## Steps

1. **Name the run.** Slug it: `work/<slug>/` under `~/workspace/skills/clip-farm/`
   (e.g. `phase2`, `livestream-09-24`). One folder per source, always.
2. **Ingest.**
   `.venv/bin/python scripts/01_ingest.py --url <youtube-url> --out work/<slug>/`
   or `--file <local.mp4>`. Add `--sections "00:10:00-00:40:00"` to trim dead air.
   Produces `source.mp4` + `audio.wav` (16 kHz mono).
3. **Transcribe.**
   `.venv/bin/python scripts/02_transcribe.py --out work/<slug>/ [--model small]`
   Default `base` for speed; `small` when time allows and accuracy matters.
   Produces `transcript.json` (word-level timestamps).
4. **QC the transcript.** Spot-check 3 segments against the audio: names,
   numbers, and brand terms spelled right. Re-run with `small` if base is sloppy.
5. **Log it.** Note in the work dir: source URL, duration, segment count,
   word count, date. Then hand `transcript.json` to the `clip-producer` playbook.

## Decisions the agent makes

- Which model (base vs small): base for speed, small for noisy/multi-speaker audio.
- Section trimming: cut intros/outros/waiting-room dead air before transcribing.

## "Done right"

`source.mp4` + `audio.wav` + `transcript.json` in `work/<slug>/`, transcript
spot-checked, log line written. Nothing posted, sent, or shared — this stage is
internal; no external gate needed, but the standing approval rule still applies
to anything leaving the machine.
