# KTL Content Engine

The content machine for **Know The Ledger** — long-form in, clips out, published on approval, leads captured and nurtured. One playbook per job, three layers per playbook: **process, toolbox, proof**.

Part of the [KTL-Media](https://github.com/KTL-Media) Layer 3 stack. The private source doctrine lives in `ktl-second-brain`; this repo is the engine that turns it into output.

## The loop

```
content-intake → clip-producer → publisher → lead-capture → lead-nurture
       ↓               ↓
   clip-farm (ingest → transcribe → moments → render → ship)
```

1. **content-intake** — long-form source (video, audio, livestream) becomes a word-level transcript and a clean source asset.
2. **clip-producer** — the transcript is mined for the strongest 20–45 second moments; vertical captioned clips are cut.
3. **publisher** — hooks, captions, hashtags, and schedule are drafted; **nothing posts without explicit approval of the exact content**.
4. **lead-capture** — comment keyword (e.g. `PLAYBOOK`) triggers the DM flow: contact captured, lead magnet delivered, lead tagged.
5. **lead-nurture** — value-first follow-up sequence. Any reply pauses automation; hot replies route to a human.

## Modules

| Module | What it does |
|---|---|
| `platform/` | Master doc wiring the five playbooks into one content-to-client loop |
| `content-intake/` | Playbook: source → transcript |
| `clip-producer/` | Playbook: transcript → clips |
| `publisher/` | Playbook: clips → scheduled, approved posts (+ worked example) |
| `lead-capture/` | Playbook: keyword → DM → contact → magnet delivery |
| `lead-nurture/` | Playbook: Day 0/2/5/9 value sequence |
| `clip-farm/` | Working implementation: `01_ingest` → `02_transcribe` → `03_find_moments` → `04_render` → `05_ship` (1080×1920, face-tracked crop, karaoke captions) |

Each playbook carries the same five files: `SKILL.md` (when to use it), `PROCESS.md` (the steps), `TOOLBOX.md` (the tools), `PROOF.md` (how you know it worked), `PROMPTS.md` (the four prompts: process, toolbox, proof, correction).

## Rules

- **Nothing is emailed, sent, posted, shared, activated, or published without explicit approval of the exact content.** Every `PROOF.md` enforces this.
- Approved Layer 1 doctrine promotes here; agent work stays inside bounded briefs.

## Run the clip farm locally

Status: implementation present; full media pipeline not yet verified by this readiness pass.
Requires Python 3.11+, FFmpeg with the subtitles filter, and a source recording you own or may process.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r clip-farm/requirements.txt
python clip-farm/scripts/01_ingest.py --file /absolute/path/recording.mp4 --out work/demo
python clip-farm/scripts/02_transcribe.py --out work/demo --model base
python clip-farm/scripts/03_find_moments.py --out work/demo --top 5
# Inspect moments.json and choose a window inside the source duration.
python clip-farm/scripts/04_render.py --out work/demo --start 12.5 --end 35 --name clip01
python -m unittest discover -s clip-farm/tests -v
```

The timestamps above are examples, not automatically chosen highlights. Transcription downloads a model on first use. Rendering uses a median detected face position (or center crop), not continuous tracking. Check the crop and captions manually.

Publishing is separate and requires instagram-cli, account access, and an approval receipt.
Create the receipt only after a human reviews the exact clip, account, and caption:

```json
{"approved": true, "approved_by": "REVIEWER_NAME", "clip_sha256": "EXACT_SHA256_OF_APPROVED_MP4", "account": "EXACT_ACCOUNT_ARGUMENT", "caption": "EXACT_APPROVED_CAPTION"}
```

```bash
python clip-farm/scripts/05_ship.py --clip work/demo/clips/clip01.mp4 --account YOUR_ACCOUNT --caption "EXACT_APPROVED_CAPTION" --approval approval.json
```

The receipt prevents accidental publishing of different inputs; it is not a signed identity or authorization service. Never have an agent manufacture human approval.

## Commercial readiness

Best initial offer: a bounded content repurposing service, with a fixed source duration, clip count, review round, and delivery deadline. A software subscription is a hypothesis until repeated customer usage and support economics are measured.

Before claiming traction, record approved clips delivered, paid invoices, cost per clip, editing time, revision rate, and renewals. No revenue or performance claim is established by this repository alone.
