# PROMPTS — clip-producer

## 1. Process prompt

> Act as a world-class operations consultant. I want to document my process for
> CLIP PRODUCTION — turning a word-level transcript of my long-form content into
> 3–5 finished vertical clips — so an AI agent can execute it exactly the way I
> do. The agent has scripts: `03_find_moments.py` (heuristic 20–45s candidates
> into moments.json) and `04_render.py` (face-tracked 9:16 crop + karaoke
> captions into clips/clipNN.mp4). Interview me ONE question at a time. Ask
> about: how I spot a clip-worthy moment (hooks, hot takes, stories, numbers);
> how many clips per source; my rules for start/end boundaries; what makes me
> reject a candidate; how I QC a render (framing, captions, audio); when my own
> timestamps override the agent's picks; what "done right" looks like; the
> mistakes a beginner always makes (mid-sentence cuts, weak opens, unreadable
> captions). Keep asking until you can write the full process back as a numbered
> SOP. Ask your first question now.

## 2. Toolbox prompt

> Build the TOOLBOX for my clip-producer playbook. It must contain: the exact
> commands for 03_find_moments and 04_render with the clip-farm venv; a
> moment-pick rubric scoring hook / self-contained / payoff / clip-ability 1–5;
> the render spec (1080×1920, YuNet face-tracked crop with center-crop fallback,
> karaoke word-highlight captions); the pick-sheet format (name, timestamps,
> hook line verbatim, why-it-works); and a corrections log for render fixes.
> Keep it tight, no fluff.

## 3. Proof prompt

> Build the PROOF checklist for my clip-producer playbook. Every item verifiable
> from the files: 3–5 clips in work/<slug>/clips/; each 20–45s; hook in the
> first 3 seconds; ends on a payoff, no mid-sentence cuts; captions readable and
> in sync; face framed or clean center crop; agent watched every render end to
> end; pick sheet written. Final item is the approval gate: nothing posted,
> published, or sent — clips go to the publisher playbook for approval, no
> exceptions. End with a version label and the rule: only hand off work that
> passes 100%.

## 4. Correction prompt

> My clip-producer playbook got something wrong. Don't re-prompt me in the chat
> — fix the playbook files instead. Diagnose first: was PROCESS.md unclear (pick
> criteria, boundaries, QC)? Was TOOLBOX.md missing a rubric line, render
> detail, or correction? Was PROOF.md too weak to catch the failure? Then edit
> the right file and tell me in one line what changed and which future runs it
> fixes. If it's a judgment call I need to make, ask me one direct question
> instead of guessing.
