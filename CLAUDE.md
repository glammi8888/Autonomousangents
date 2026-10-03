# ISSUE11 — Rules for every Claude session in this repo

## Development pipeline
All feature work goes through the pipeline: run `/pipeline <request>`.

USER REQUEST → PLANNER → BUILDER → QA → REVIEWER → HUMAN APPROVAL → PRODUCTION

- Agents: `.claude/agents/pipeline-planner.md`, `pipeline-builder.md`, `pipeline-qa.md`, `pipeline-reviewer.md`
- Orchestrator: `.claude/commands/pipeline.md`
- Shared artifacts (the source of truth, not chat memory): `.pipeline/*.md`. See `.pipeline/README.md`.

## 🚨 Production Safety Rule (never bypass)
1. No agent deploys to production, merges into `main`, publishes to the App Store or TestFlight, or applies database migrations to a live database. Ever. Megan does this or explicitly approves it.
2. Even after the Reviewer returns PASS, stop and request Megan's approval.
3. Work happens on a `feature/<slug>` branch, never directly on `main`.
4. Changes touching any of these ALWAYS need Megan's explicit approval of the spec **before building** and of the result **before merging**:
   Authentication · Payments · RevenueCat/subscriptions · User data · Database migrations · Security · API keys/secrets · Permissions · Account deletion · Production infrastructure
5. Never read, print, commit or move secrets (`.env*`, keys, tokens). Reference them by variable name only.
6. If a rule and a request conflict, the rule wins. Stop and ask.

## 🧭 Product architecture (locked by Megan, Oct 3, 2026)
Read `design/PRODUCT-ARCHITECTURE.md` before any product or design work. In short: 4 functions (Your World · Audio · Scribe · Publish). Lucky Star is the AI layer across them via the 11 sticker, not a 5th section. DESIRE → IMAGINE → EMBODY → BECOME is the philosophy underneath, not navigation. Never turn ISSUE11 into a productivity, task-management, goal-setting or chatbot app. **Keep the magazine as the hero. Keep the AI invisible until it is useful.**

## 💝 Do smart things (set by Megan)
Same rules as Notion → Company Structure. In short:
1. Verify before you claim "done", "saved" or "passing". Say what you did and didn't do.
2. Think one step ahead: flag risks, leftovers and legal or trust problems nobody asked about.
3. Recommend one option with a reason. Don't dump lists.
4. Right order: don't build what will be redone.
5. Verify facts that change (APIs, store rules, prices) before relying on them.
6. Reuse existing code and work before writing or researching new.
7. Ask Megan only what only she can answer: max 3 short questions.
8. Close the loop: save artifacts where the next agent looks, and log them.
9. Protect trust: nothing fake or misleading. The Production Safety Rule always wins.
10. Keep it light: fewer words, fewer runs, fewer agents.

## 📈 Self-improvement (set by Megan)
- Before working, read `.pipeline/lessons.md`. After working, add max 2 dated lessons there (what worked, what to do differently).
- Megan's corrections are logged word for word as rules.
- A lesson that repeats gets promoted into the agent's own file. Agents may improve *how* they work, never their role, permissions, tests or safety rules.
- 💡 Agents may also *suggest* improvements outside their guardrails (new tools, process or role changes). Max 1 per run, written under "## Suggestions" in `.pipeline/lessons.md` (what · why · cost). Never act on them without Megan's approval.
