# TOOLBOX — publisher

## Caption template

```
<HOOK — the clip's strongest line, verbatim>
<1–2 lines context in Phillip's voice>

<CTA>
<3–5 hashtags>
```

## CTA blocks

- Lead magnet: `Comment PLAYBOOK and I'll DM you the free starter kit.`
- No magnet: `Follow @phil_moreland — new playbooks drop weekly.`

## Hashtag bank (pick 3–5 per post)

`#AI #AIAgents #BuildInPublic #Systems #Automation #ContentEngine #GITBUILT #Imaginarium`

## Hook-variant format

Give Phillip 2, each ≤ 12 words, each usable as the caption's first line:

1. …
2. …

## Schedule

- 1 clip/day max to start. Windows: 7–9am ET, 12–1pm ET.
- Alternate formats across the week: talking-head clip → carousel reel →
  talking-head clip (variety holds attention).

## Posting

```bash
cd ~/workspace/skills/clip-farm
.venv/bin/python scripts/05_ship.py --clip work/<slug>/clips/clip01.mp4 \
  --account imaginarium2026 --caption "<EXACT approved caption>"
```

Accounts: `@phil_moreland` (personal), `imaginarium2026` (brand). Confirm which
account per post at approval time.

## Approval log format

`<date> | clip01 | account=@phil_moreland | approved_by=Phillip | caption_hash | post_url`
