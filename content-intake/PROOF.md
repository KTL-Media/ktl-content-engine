# PROOF — content-intake

Run this checklist before handing off to `clip-producer`. Fix failures in the
playbook, not the chat.

- [ ] `source.mp4` exists in `work/<slug>/` and plays (spot-check 10s)
- [ ] `audio.wav` exists, 16 kHz mono
- [ ] `transcript.json` exists, word-level timestamps present
- [ ] Transcript duration ≈ audio duration (±1%)
- [ ] 3 segments spot-checked against audio — clean, no gibberish
- [ ] Names / numbers / brand terms spelled right
- [ ] Log line written in the work dir
- [ ] **Approval gate:** nothing was emailed, sent, posted, shared, or published
      during intake. If anything left the machine, Phillip approved the exact
      content first — otherwise stop and report.

Checklist version: content-intake v1. Only hand off work that passes 100%.
