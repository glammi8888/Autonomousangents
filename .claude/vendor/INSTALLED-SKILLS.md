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
| security-watchdog (Entelligentsia) 0.1.0 · MIT | Anthropic Directory, community tier (repo Entelligentsia/skillforge) | Megan's local Claude Code (terminal) | **Scanned Oct 15 by the Design Room from Megan's zip: SAFE TO USE.** 9 files, all read. Hook = Node built-ins only (fs/path/os): reads ~/.claude/plugins/installed_plugins.json, saves a list of plugin names to its own data folder, prints one alert line. No network, no keys/.env, no installs, no persistence, no hidden comments; PNG has no appended data. Only fullwidth Unicode is the labeled "ignore previous instructions" example in SKILL.md. Notes: first session after install flags EVERY installed plugin as new (one-time scan of all); its alert says "before responding to any user request" (expected); scan-plugin allows Bash (used for `du`). Next: `/security-watchdog:scan-plugin <id>` on appstore-screenshots and Sonar ASO after the Replit build. |

## Waiting for scan (Megan approved Oct 15; not installed until scanned, Safety Rule 7)
| Plugin | Why | Sends data online? | Needs |
|---|---|---|---|
| appfoyer (AppFoyer) | Privacy policy, terms, support + account-deletion pages | Yes: AppFoyer hosts the pages | Megan's zip; needs the app code |
| Mobile Release Check (Stefan Petrovici) | App Store readiness check of the code | Listing says no | Megan's zip; needs the app code |

## Scanned 2026-10-15 (Design Room, from Megan's zips; every file read)
| Plugin | Verdict | What it does on her machine | Sends online | Watch-outs |
|---|---|---|---|---|
| appstore-screenshots 1.0.0 · MIT (Nicolas Torres, github ntgussoni/app-store-play-store-screenshots-skill) | **SAFE TO USE** | 1 skill + 2 scripts (compose.py = Pillow image maker; launch_simulators.sh = boots iPhone/Android simulators). No hooks, no auto-run, no keys read. | Nothing from its own scripts | Mac + Xcode + Expo apps only. Its setup step tells Claude to install tools (Maestro via `curl … \| bash`, fastlane, ImageMagick, Pillow): ask Megan before installing any of them. Docs mention options compose.py doesn't have (glow, particles, background image), so those will error. Outputs 1290×2796; check Apple's current sizes before uploading. |
| Sonar ASO 1.1.0 · MIT (Edge Analytics s.r.o., github trysonar/skills) | **SAFE TO USE** (data goes to Sonar) | 11 Markdown skills + a link to Sonar's hosted MCP server. No hooks, scripts or installs; may save `app-marketing-context.md` when asked. Never asks for API keys. | Yes: every sonar_ tool sends its inputs (app ids, keywords, country, saved captions/screenshot URLs) to https://trysonar.app/mcp; free tier is keyed by IP | Free tier: ~30 calls/day. Screenshot Studio, rank tracking and reviews need a paid Sonar plan (ask Megan before signing up). Never send private user data; public listing info and keywords only. |
Installing from GitHub may pull a newer version than the zip scanned; security-watchdog flags it next session, so run `/security-watchdog:scan-plugin` then.
