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

## Quick start

```bash
# 1. Intake — download + transcribe a source
python3 clip-farm/scripts/01_ingest.py <youtube-url> work/<slug>/
python3 clip-farm/scripts/02_transcribe.py work/<slug>/

# 2. Find moments, 3. render, 4. ship (on approval)
python3 clip-farm/scripts/03_find_moments.py work/<slug>/
python3 clip-farm/scripts/04_render.py work/<slug>/moments.json
# 05_ship.py publishes only what was explicitly approved
```

See each module's `SKILL.md` for the full operating contract.
