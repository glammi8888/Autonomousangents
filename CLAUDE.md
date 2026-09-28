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
