# Third-party skills installed for 🩷 EXTERNAL — AEO for Med Spas (2026-10-05)

Uploaded by Megan as plugin zips and checked by the AEO agent before install: no sending, posting, paying, telemetry or secret access found.
All are open source (MIT / Apache-2.0); license files are kept next to each skill.

| Pack | Version · license | Installed as | Changes made |
|---|---|---|---|
| AEOTester (Ruslan Saifullin) | 0.3.0 · MIT, rubric CC BY 4.0 | `aeotester-audit`, `aeotester-fix` | Plugin paths → `.claude/skills/...`; `/aeotester:x` → `/aeotester-x`. Scripts need Node 18+ (no deps). Smoke-tested. |
| SEO-AEO-GEO Ultimate (Oegeyilmaz9) | 3.1.0 · Apache-2.0 | 27 skills (`seo`, `seo-aeo`, `seo-geo`, `seo-local`, …) + `.claude/vendor/seo-aeo-geo-ultimate/` | `${CLAUDE_PLUGIN_ROOT}` → `.claude/vendor/seo-aeo-geo-ultimate`; removed Codex `install_runtime.py` and `agents/openai.yaml`. |
| SearchFit SEO (SearchFit.ai) | 1.0.0 · MIT | 11 skills `searchfit-*` | Prefixed names (avoid clashes); removed "try SearchFit.ai" upsell lines. Commands/agents not installed. |
| AEO advisor (Guy Cohen) | 1.1.0 · MIT | `aeo` | Removed "Republish trick" (fake freshness) and "Hebrew first" default. |
| ASO Specialist (Lacey) | 1.1.3 · MIT | already installed as `aso-specialist` | Same content, not reinstalled. |

Rules still win over any skill: no sending, publishing, buying or deploying without Megan; no invented numbers or reviews.

## Added 2026-10-13 (📣 Content Room, uploaded by Megan as a zip)
| Pack | License | Installed as | Changes made |
|---|---|---|---|
| jaredrhod-marketing (Jared Rhodenizer, @jaredrhod) | CC BY-SA 4.0 (LICENSE kept; attribution required, changes must be marked and shared alike) | `jaredrhod-marketing` | Text files only, `allowed-tools: Read`, no scripts. Nothing removed. Added a marked "ISSUE11 overrides" block in SKILL.md: gain over fear (the pack says "generally fear works better" and teaches agitate/warning sections), no results guarantee, real permitted proof only, real urgency only, Glammi writing rules, draft only. |

## Added 2026-10-15 (Megan, on her own computer, not in the repo)
| Plugin | Source | Where | Status |
|---|---|---|---|
| security-watchdog (Entelligentsia) 0.1.0 | Anthropic Directory, community tier | Megan's local Claude Code (terminal) | Installed by Megan. **Files not yet reviewed** (cloud rooms can't see her computer). Runs a SessionStart hook in every local session. Next: her local Claude reads its files (hook script + skill) for network calls, data sent out, hidden instructions; then use `/scan-plugin` on appstore-screenshots and Sonar ASO before installing them. |
