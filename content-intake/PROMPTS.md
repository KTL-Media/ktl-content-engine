# PROMPTS — content-intake

Four setup prompts. Each is a complete spec — paste into the agent to build or
rebuild this playbook's layer.

## 1. Process prompt

> Act as a world-class operations consultant. I want to document my process for
> CONTENT INTAKE — getting my long-form videos (YouTube, Zoom replays, local
> files) downloaded and transcribed with word-level timestamps — so an AI agent
> can execute it exactly the way I do. The agent has scripts: `01_ingest.py`
> (downloads/trims to source.mp4 + audio.wav) and `02_transcribe.py`
> (faster-whisper, base or small model, outputs transcript.json). Interview me
> ONE question at a time. Ask about: what triggers an intake run; how I name
> work folders; when I trim sections vs transcribe everything; how I pick base
> vs small model; how I QC a transcript (spot checks, names, numbers); what
> "done right" looks like; the mistakes a beginner always makes (wrong folders,
> skipping QC, transcribing dead air). Keep asking until you can write the full
> process back as a numbered SOP. Ask your first question now.

## 2. Toolbox prompt

> Build the TOOLBOX for my content-intake playbook. It must contain: the exact
> shell commands for ingest (URL, file, section-trim) and transcribe (base,
> small) using the venv at ~/workspace/skills/clip-farm/.venv; the three known
> environment quirks and their fixes (bracketed IPv6 in no_proxy crashes the
> transcription client — sanitize it; ID3-prefixed RIFF headers in TTS WAVs —
> strip to RIFF; YouTube bot-checks default yt-dlp — use the android player
> client with the egress CA appended to the venv certifi bundle); a transcript
> QC rubric (duration match, 3 spot-checks, proper nouns, no long gaps); and the
> log-line format for recording each run. Keep it tight, no fluff — commands the
> agent can copy-paste.

## 3. Proof prompt

> Build the PROOF checklist for my content-intake playbook. Every item must be
> verifiable by inspecting files: source.mp4 exists and plays; audio.wav is 16
> kHz mono; transcript.json exists with word-level timestamps; transcript
> duration matches audio ±1%; 3 segments spot-checked clean; names/numbers/brand
> terms spelled right; log line written. Final item is the approval gate:
> nothing was emailed, sent, posted, shared, or published during intake — if
> anything left the machine, I approved the exact content first. The checklist
> must end with a version label, and the rule: only hand off work that passes
> 100%.

## 4. Correction prompt

> My content-intake playbook got something wrong. Don't re-prompt me in the
> chat — fix the playbook files instead. Diagnose first: was PROCESS.md unclear
> (wrong step or missing decision)? Was TOOLBOX.md missing a command, quirk, or
> example? Was PROOF.md too weak to catch the failure? Then edit the right file,
> bump nothing else, and tell me in one line what you changed and which future
> runs it fixes. If the failure is a judgment call I need to make, ask me one
> direct question instead of guessing.
