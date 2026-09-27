---
name: tesseract-client-playbook
description: Turn Tesseract (Mirage's local AI video engine) into paid client work — install check, per-deliverable pricing packages, client terms, and a 7-day first-client outreach plan with copy-paste messages. Use when someone asks how to sell video editing with Tesseract, what to charge per edit, how to land first editing clients, wants an Upwork proposal or outreach DM for video work, is building the Git Built → Get Money video-services track, or says "tesseract playbook", "hook pack", "launch video pricing", or "editing retainer". Pairs with tesseract-video and tesseract-motion, which do the actual editing.
---

# Tesseract Client Playbook

The commercial layer over the two Mirage skills. `tesseract-video` and `tesseract-motion`
do the editing; this skill decides **what gets sold, at what price, to whom, and how the
first yes happens**.

Source: *The Tesseract Client Playbook*, The AI Leverage (Sep 23, 2026). Market numbers
below are that article's cited figures — re-check before quoting them to a client.

Ecosystem position: **Triple AI Agency** service line and the **Get Money** stage of the
GitHub → Git Built → Get Money pipeline. Pillars: Wealth & Wisdom (revenue),
AGI-Autonomy (agent does the labor).

## Route the request

| Ask | Go to |
|---|---|
| "Set me up" / "it's not working" | Part 1 — Install |
| "What do I charge?" / quote / proposal pricing | Part 2 — Pricing & terms |
| "How do I get clients?" / DMs / Upwork | Part 3 — 7-day plan + [outreach templates](references/outreach-templates.md) |
| Actual edit of client footage | Hand off to `tesseract-video` (edits) or `tesseract-motion` (graphics) |
| Teaching this to a cohort | Part 4 — Git Built module |

## Part 1 — Install (≈15 min)

**Hard requirements — check before promising anything:**
- Apple Silicon/Intel Mac or 64-bit Windows 10+. The article marks Linux, WSL and cloud
  setups unsupported for this workflow (the CLI does ship a Linux x86_64 build that needs
  Vulkan, but don't build a client offer on it). **Claude Code on the web cannot run it.**
- A *local* agent with file access: Claude Code (desktop/terminal), Codex, Cursor, or
  ChatGPT desktop. A browser chat will not work.
- Node.js LTS + npm (for the skills installer).
- Cost: Tesseract is free, no Mirage account. Only cost is the agent plan.

**Route A — one prompt** (paste into a local agent session pointed at a project folder):

```
Set up Tesseract by Mirage so you can edit videos and create motion graphics locally. Read https://github.com/mirage-hq/Tesseract and check that this computer and agent support local execution on macOS or Windows. If Tesseract is not already installed, install both Tesseract skills for this agent. Follow their installation guide to set up the required CLI version, verify its checksum, and confirm it runs. Then ask me for my footage or the video I want to make.
```

**Route B — one command:** `npx skills add mirage-hq/Tesseract`, select both skills
(Edit Video + Motion Graphics) and the agent, start a **new** session, then ask the agent
to follow the Tesseract runtime installation guide. ChatGPT desktop users: install the
official plugin *instead* — plugin or skills, not both.

**First test — before selling anything:**

```
Use Tesseract to make a 10 second video from the footage in this folder. Start with a strong opening, add a short animated title, and keep the dialogue clear. Show me a preview before the final render. Keep the Tesseract project editable so we can revise the timing, graphics, and sound.
```

Then drill the client loop until it's automatic: **preview → one note → preview → render.**
(Tighter cut, different title, quieter music bed.) This loop *is* the product.

**Troubleshooting:**
- Nothing happens → you're in a browser chat. Switch to a local session.
- Agent can't find Tesseract → start a fresh session; skills load at session start.
- Still stuck → ask the agent to read the repo's setup guide and verify the runtime can
  preview and render.

## Part 2 — Pricing & terms

**Market reference (article's sources):**

| Source | Figure |
|---|---|
| Upwork cost guide | $10–$60/hr, median ≈$35; mid-tier ≈$40/hr; senior ≈$100/hr |
| HireMango 2026 | Short-form: $30–60 entry · $60–120 mid · $120–300+ with motion graphics & hooks |
| Vidico 2026 | TikTok/Reels: $50–400 per video, 1–2 day turnaround |
| Upwork listings | Short-form jobs posted at $750 fixed |

**Rule #1: never bill hourly.** The agent compresses hours into minutes; hourly billing
punishes speed. Price the finished deliverable.

**The four packages:**

| # | Package | Price | Scope | Role in the funnel |
|---|---|---|---|---|
| 1 | Single Edit | $75–100 | ≤60s short-form; captions, music, clean cuts, animated title; 2 revisions; 48h | Land first 3 clients — mid-tier, credible, low-friction |
| 2 | Hook Pack | $200 | One video, **four different openings** | Best upsell — same footage, 4 deliverables, sold as "we test which hook works" |
| 3 | Launch Video | $300–750 | 30–60s product/launch video; motion graphics, kinetic type, logo end card | Easiest sale: launches have a date and a budget. Built for `tesseract-motion` |
| 4 | Monthly Retainer | $900–1,500/mo | 12 short-form/month (3/week), captions + hooks, 1 revision each | Where it becomes a business — recurring revenue |

**Terms that protect the operator:**
- 50% upfront on anything over $100; **100% upfront on the first job** with a new client.
- Two revision rounds included; extra rounds $25 each.
- Turnaround 48h; same-day rush +50%.
- Music: client-supplied or licensed only. Never rip from Spotify.
- **Review every render yourself before sending.** The agent drafts; the human approves.
  The operator's eye is what the client pays for.

**Unit economics check** (run through `formulas-for-moolah` for full modeling): the retainer
at $900/12 videos = $75/video — same as the Single Edit rate, but with guaranteed volume.
At $1,500 it's $125/video. Quote the retainer as the volume discount, not a cut rate.

## Part 3 — First paying client in 7 days

Full copy-paste messages: [references/outreach-templates.md](references/outreach-templates.md).

| Day | Move | Output |
|---|---|---|
| 1 | Build 3 samples: talking-head w/ captions + hook · 15s product promo w/ animated title · Hook Pack (one clip, 4 openings side by side) | Portfolio. Own footage, free stock, or permissioned footage **only** |
| 2 | Upwork: search "short form video editor", filter fixed price. Headline: `Short form video editor \| Reels, TikTok, Shorts \| 48h delivery`. Apply only where samples match (Connects cost money) | Profile + proposals |
| 3 | Local businesses on Instagram posting static photos or uncaptioned video (restaurants, gyms, salons, real estate) | DMs with free first edit |
| 4 | Podcasters/YouTubers with strong content and no Reels/Shorts clips | DMs offering 3 clips, risk-free |
| 5 | Founders announcing launches on X / LinkedIn / Product Hunt (often 1–2 weeks out) | DMs offering 48h first version |
| 6–7 | Follow up at 48h; close happy free-edit clients with a **two-option** offer | First invoice |

**Mechanics that do the work:**
- **The free first edit** removes client risk and costs minutes of agent time.
- **Most yeses come on the second message.** Always follow up once.
- **Always offer two options** — people choose between options instead of deciding yes/no.
- Send podcast sample clips **privately**. Never post someone else's content without permission.

**Week-one target: one paid job.** One paid job proves the offer. Everything after is
volume — more DMs, more proposals, more free edits — and upselling every happy client
into the Hook Pack or a retainer.

## Part 4 — Red Pillar integration

**G.O.D. roles in a delivery pod** (use `god-framework` for full assessment):
- **Generator** — hook concepts; the 4 openings in a Hook Pack; outreach angles.
- **Operator** — the preview → note → render loop; 48h SLA; invoicing and follow-ups.
- **Destroyer** — the human review gate; kills weak hooks and anything that isn't client-ready.

A solo operator carrying all three is the concentration-of-load risk. First hire/pod split:
Operator (delivery loop) separate from outreach.

**CLAW Code — client delivery pipeline** (build in `red-pillar-workflows`):
- **Capture:** client footage + brief intake (deliverable, aspect ratio, duration, must-keep moments, brand assets).
- **Logic:** package selected → scope, revision count, deadline, deposit rule.
- **Action:** `tesseract-video` / `tesseract-motion` edit → preview → note → render → human review.
- **Workflow:** deliver, invoice, log revision count, schedule the retainer upsell at edit #3.

**Git Built module — "Edit for Money" (one Wednesday session + one week of homework):**
1. Install live (Part 1), everyone runs the first-test brief.
2. Build the three Day-1 samples as homework.
3. Pod accountability: each member sends 10 DMs using the templates; track replies.
4. Graduation metric: one paid job. Report it in the community.
Anpu covers the install/troubleshooting; Hitsuyo runs the outreach accountability — keep
those split so neither carries both.

**Voice:** the source copy is plain and direct — keep it. When adapting for Red Pillar
channels, frame it as **liberation tech**: the agent plan someone already pays for becomes
a production studio they own. No hype, no fake urgency.

## Guardrails

- Never claim Tesseract runs in a browser chat, on WSL, or in a cloud session.
- Never quote market numbers as guarantees; they are reference ranges from cited guides.
- Never use footage or music without rights. Permission first, always.
- Never send an unreviewed render.
