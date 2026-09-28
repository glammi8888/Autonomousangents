# ISSUE11 Autonomous Development Pipeline

```
USER REQUEST → PLANNER → BUILDER → QA → REVIEWER → HUMAN APPROVAL → PRODUCTION
                  ↑_________|________|       |
                  (re-plan)  (fix loop)  (routed back on FAIL)
```

**Start a feature:** in Claude Code, inside the ISSUE11 repo, run
`/pipeline Add favorites to ISSUE11`
(or ask 🩶 OPS — Manager, who starts it for you).

## Agents
| Step | Agent | Can edit code? | Writes |
|---|---|---|---|
| 1 | `pipeline-planner` (Planner / Architect) | No | `spec.md`, `acceptance-criteria.md` |
| 2 | `pipeline-builder` (Builder) | Yes, on `feature/*` only | code, tests, `implementation-log.md` |
| 3 | `pipeline-qa` (QA / Tester) | No (may add failing tests) | `test-results.md` |
| 4 | `pipeline-reviewer` (Reviewer / Gatekeeper) | **Read-only** | verdict → orchestrator saves `review.md` |
| — | `/pipeline` (orchestrator, for the Manager) | No | `request.md`, `approval-request.md` |

## Shared artifacts (source of truth, never chat memory)
`request.md` → `spec.md` + `acceptance-criteria.md` → `implementation-log.md` → `test-results.md` → `review.md` → `approval-request.md`
Finished runs move to `archive/<date>-<slug>/`.

## Loops and limits
- Builder blocked by a bad spec → back to Planner (max 2).
- QA FAIL → back to Builder (max 3 rounds).
- Review FAIL → routed to Planner, Builder or QA (max 2).
- Over a limit → escalate to Megan with a plain summary.

## 🚨 Production Safety Rule
- Nothing reaches production without Megan's explicit approval, even after a PASS.
- Work stays on `feature/*` branches. `.claude/settings.json` blocks pushing to `main`, merging, force-pushing, production deploys (Vercel, Netlify, EAS, fastlane), live database pushes, and reading `.env` files.
- **Always approval first** (spec before build, result before merge): Authentication · Payments · RevenueCat/subscriptions · User data · Database migrations · Security · API keys/secrets · Permissions · Account deletion · Production infrastructure.

## Recommended GitHub setting (Megan, one time)
Repo → Settings → Branches → add a rule for `main`: *Require a pull request before merging* + *Require approvals*. This makes the approval gate impossible to bypass, even by mistake.

## Reusing the pattern
Executor → independent checker → approval gate. The same shape can later serve Product, Creative, Marketing, PR and Revenue work: swap in the right executor and checker agents.
