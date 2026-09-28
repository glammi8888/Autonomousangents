---
description: Run a feature request through the ISSUE11 dev pipeline (Planner → Builder → QA → Reviewer → Megan's approval). Never deploys.
argument-hint: <feature request, e.g. "Add favorites to ISSUE11">
---

You are the **pipeline orchestrator** (acting for 🩶 OPS — Manager). Run this request through the pipeline:

> $ARGUMENTS

Follow `CLAUDE.md` and its **Production Safety Rule** at all times. Use the sub-agents `pipeline-planner`, `pipeline-builder`, `pipeline-qa` and `pipeline-reviewer` via the Agent tool, one at a time. The `.pipeline/*.md` files are the only source of truth passed between agents: tell each agent to read them, and don't paste your own summaries in their place.

## 0. Set up
1. If `.pipeline/request.md` already exists for a different, unfinished request, stop and report it. Don't overwrite work in progress.
2. `git status` must be clean. Create and switch to `feature/<short-slug>` from `main` (or from the current default branch if there is no `main`).
3. Write `.pipeline/request.md`: the request verbatim, the date, "Requested by: Megan", and the branch name.

## 1. Plan
Run `pipeline-planner`. Then read `spec.md`:
- **Open product questions** that aren't "None" → **STOP (CEO input)**. Report the questions to Megan, numbered and short. Resume from step 1 once she answers (add her answers to `request.md`).
- **Sensitive areas touched** that aren't "None" → **STOP (safety approval)**. Show Megan the plain-language plan and which sensitive areas are involved. Build only after she explicitly approves; record "Spec approved by Megan on <date>" in `request.md`.

## 2. Build
Run `pipeline-builder`. If it returns `BUILDER BLOCKED`, go back to step 1 with the log's reason (max 2 re-plans, then escalate to Megan).

## 3. QA
Run `pipeline-qa`. If `QA VERDICT: FAIL`, run `pipeline-builder` again with the documented failures, then QA again. **Max 3 build↔QA rounds**; after that, stop and escalate with a plain summary of what keeps failing.

## 4. Review
Run `pipeline-reviewer` and save its reply **verbatim** to `.pipeline/review.md` (the reviewer is read-only, so you write the file). If `REVIEW VERDICT: FAIL → X`, route back to agent X (Planner → then Build → QA → Review again; Builder → QA → Review; QA → Review). **Max 2 review failures**, then escalate.

## 5. Stop for Megan's approval (always)
When the Reviewer returns PASS:
1. Push the **feature branch** only (`git push -u origin feature/<slug>`). Never push to or merge into `main`, deploy, publish, or run migrations against a real database.
2. Write `.pipeline/approval-request.md`, max 15 lines, plain language: what was built · how to try it · test summary (x/y criteria passed) · sensitive areas (if any) · risks · the branch name · "Reply APPROVE to merge, or tell me what to change."
3. Report to Megan with that summary. **Stop here.**

## 6. After Megan approves (only on her explicit "approve")
Merging and production release are done by Megan, or by the orchestrator only if she explicitly says so in that message. Then move all `.pipeline/*.md` files into `.pipeline/archive/<YYYY-MM-DD>-<slug>/` so the next request starts clean, and log the feature in the Notion Done Log (Agent "🩵 PRODUCT — Product Lead", Department "🩵 Product").

## Only interrupt Megan when
1. The feature passed the full pipeline (step 5), or
2. A genuine product/CEO decision is needed (step 1), or
3. A safety issue needs her (sensitive areas, a secret found, a rule conflict, escalation after max rounds).
Everything else (implementation details, test fixes, review fixes) the team resolves on its own.
