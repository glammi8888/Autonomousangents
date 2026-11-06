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

## Scanned 2026-10-20 (🩷 EXTERNAL AEO agent; npm tarball read, not yet installed)
| Package | Verdict | What it does | Sends online | Watch-outs |
|---|---|---|---|---|
| framer-api 5.1.0 (official Framer, maintainers @framer.com; deps devalue 6 by Rich Harris, std-env 4 by pi0) | **SAFE TO USE** | Library for Framer's Server API (open beta): read/write CMS, publish, deploy. No install/postinstall scripts (framer-api, devalue, std-env). No child_process, eval or hidden code. Reads only the `FRAMER_API_KEY` env var. Writes a file only when you ask for a debug archive (zip in the current folder). Turns TLS checks off only for Framer's internal dev host `api.framerlocal.com`, never for the real API. | Yes: one WebSocket to `wss://api.framer.com/channel/headless-plugin`, carrying the API key and whatever CMS content we send | The key acts as the person who made it (full edit + publish on that one Framer project): environment secret only, never in chat or the repo. Purpose: auto-post Glammi Studio blog articles. Publishing needs Megan's written OK (requested Oct 20). Re-scan if the version changes. |

## Reviewed 2026-10-21 (🩶 Manager; hosted connector, no files to read)
| Connector | Verdict | What it does | Sends online | Watch-outs |
|---|---|---|---|---|
| Replit MCP (official, by Replit; `https://replit-mcp.com/server/mcp`, beta) | **OK TO CONNECT with limits** (Megan asked Oct 21: "I also want to connect to replit too") | Hosted by Replit, OAuth sign-in (no API key in chat or repo). Tools per Replit docs: create_app_from_prompt, update_app_using_prompt, ask_question (read-only); third-party listings also show more tools incl. a publish/deploy one (not confirmed). | Yes: prompts and app questions go to Replit (and its Agent); Replit already holds the app code | Every create/update runs Replit Agent = **uses Replit credits**, applied straight to the app with no diff to review → Megan sets a Replit budget limit first. Agents never use any publish/deploy/App Store tool (Production Safety Rule); turn that tool off in the connector settings if listed. Sign-in, payments, user-data and delete-account changes still need Megan's spec approval before any update_app call. Beta: tools may change, re-check the list on first use. Sources: docs.replit.com/platforms/mcp-server; agentman.ai review. |

## Scanned 2026-10-21 (🎨 BRAND, Landing Room) · read, not installed
| Skill | Source | Result | Status |
|---|---|---|---|
| frontend-design (Anthropic) | Anthropic Directory, `anthropics/claude-plugins-official` → `plugins/frontend-design` (Apache-2.0) | **SAFE.** 5 files, all read: plugin.json, README, 2 licenses, SKILL.md (design guidance text only). No scripts, hooks, MCP servers or network calls; no reading of keys/.env; no hidden instructions (only non-ASCII = em dashes). Sends nothing online. | Not installed. Its guidance was read and applied to design/landing/ (Megan, Oct 21: "Look for any skill that would make this landing page look incredible"). Install needs Megan's OK. Other directory hits not scanned: UXKIN "Website Design" (uses a remote MCP server → would send data online), "audit-suite" (community, 16 skills). |

## Installed 2026-10-27 (🎨 BRAND, handoff from 🩶 OPS — Knowledge & Training; Megan approved: "THISSS", "let's grab that skill too please")
Scanned first by OPS, then re-scanned by BRAND before install (every file read or pattern-checked; nothing run).
| Skill | Source · license · pinned commit | Installed as | Scan result | Changes made |
|---|---|---|---|---|
| waitlist-page | nexu-io/open-design · Apache-2.0 (LICENSE copied) · 26d60298f8129e229a1c10aab4df7ca25b1e9ad3 · plugins/_official/examples/waitlist-page/ | `.claude/skills/waitlist-page` | SAFE. 5 files (SKILL.md, template.html, example.html, checklist.md, open-design.json). Only network use: Google Fonts in the HTML. Form script only hides the form: **saves nothing**. No hidden Unicode, no install steps. | Marked "ISSUE11 overrides" block: never publish unwired; use the locked brand; no fake counts. |
| copywriting | coreyhaines31/marketingskills · MIT (LICENSE copied) · 17772c7a80b7b8c7a47af30f648374cd8bd8adc5 · skills/copywriting/ | `.claude/skills/copywriting` | SAFE. Text only (SKILL.md, references incl. ai-tells.md, evals.json). Links are citations only. | Marked "ISSUE11 overrides" block (Megan's copy rules win). |
| marketing-psychology | same repo/commit · MIT · skills/marketing-psychology/ | `.claude/skills/marketing-psychology` | SAFE. Text only (SKILL.md, evals.json). | Marked "ISSUE11 overrides" block: ethical use only, real scarcity only. |
Not installed: the rest of marketingskills, anything via npx or a plugin marketplace.

## Oct 28, 2026: 4 skills from the OPS handoff (approval relayed by OPS: Megan "Ok let's do that")
Re-scanned by 🩷 EXTERNAL — AEO before install: every file read in full at the pinned commit; automated checks for code, network calls, secrets, install steps, hidden/control Unicode and HTML comments: none found. Nothing was run.
| Skill | Source · license · pinned commit | Installed as | Scan result | Changes made |
|---|---|---|---|---|
| schema-markup | sickn33/antigravity-awesome-skills · MIT code + CC BY 4.0 content (LICENSE + LICENSE-CONTENT copied) · e8d346bcb691225fb6ae51a49c353bcedb2ef61d · skills/schema-markup/ | `.claude/skills/schema-markup` | SAFE. 1 file (SKILL.md). Links are Google citations only. Its "risk: critical" frontmatter is the library's own label, not a finding. Bans self-serving reviews. | Added "ISSUE11 / Glammi overrides" block (no fake ratings; FAQ text must match visible FAQ). |
| customer-psychographic-profiler | same repo/commit · MIT + CC BY 4.0 · skills/customer-psychographic-profiler/ | `.claude/skills/customer-psychographic-profiler` | SAFE. 1 file (SKILL.md). Evidence-only, bans inferring sensitive traits. | Added overrides block (never infer health, body image, finances etc.). |
| emails | coreyhaines31/marketingskills · MIT (LICENSE copied) · 0cd9b3a0ef4c411a1d690419ce843f2a1da32cce · skills/emails/ | `.claude/skills/emails` | SAFE. 5 files (SKILL.md, 3 references, evals.json = sample prompts). Reads only a local product-marketing.md if present. Tool links are references, nothing installed. | Added overrides block (drafts only, Megan's copy rules). |
| cold-email | same repo/commit · MIT · skills/cold-email/ | `.claude/skills/cold-email` | SAFE. 13 files (SKILL.md, 10 references incl. deliverability.md, evals.json). Text only. Mentions LinkedIn automation tools with their terms-of-service risk. | Added overrides block (drafts only, Megan sends; no LinkedIn automation; CAN-SPAM opt-out + address). |
Not installed: the rest of either library, linked skills/tools, anything via npx or a plugin marketplace.
| sales-enablement | coreyhaines31/marketingskills · MIT (LICENSE copied) · 0cd9b3a0ef4c411a1d690419ce843f2a1da32cce · skills/sales-enablement/ (original repo, not the mcpmarket copy) | `.claude/skills/sales-enablement` | SAFE. 8 files (SKILL.md, 6 references: cold-call scripts, objection library, demo scripts, deck frameworks, one-pagers, win-loss; evals.json = sample prompts). Text only, every file read, no hidden Unicode, links are references. Approval relayed by OPS handoff 2 (Megan: "this too"). | Added overrides block: real proof only (no invented clients/metrics), TCPA/DNC check, all-party consent before recording (CA), drafts only. |
| beehiiv connector (claude.ai, official directory) | Connected by Megan via claude.ai connectors, Oct 30 2026 (not a repo install) | n/a (remote MCP) | REVIEWED. Official beehiiv connector, OAuth (no API key in repo or chat). ~200 tools: read/write posts, pages, subscribe forms, automations, segments, subscriber lists, community, products; some tools can schedule/send posts and test emails. Data it touches: Megan's beehiiv workspace "The Radar" incl. subscriber emails (user data). Rules: read-only by default; never send, schedule or email subscribers, change pricing/products, or delete anything without Megan's explicit OK; drafts only; never copy subscriber emails out of beehiiv. What it sends online: only calls to beehiiv's own service. |
| prospecting | coreyhaines31/marketingskills · MIT (LICENSE copied) · 0cd9b3a0ef4c411a1d690419ce843f2a1da32cce · skills/prospecting/ | `.claude/skills/prospecting` | SAFE. 12 files (SKILL.md, 10 references incl. local-prospecting.md + compliance.md, evals.json). Text only, 0 hidden Unicode, no commands/scripts, no key or .env reads, no hidden instructions. URLs = GitHub tool-registry docs + Clay docs (references only, nothing fetched). Compliance: no bulk scraping (LinkedIn/Google Maps), no reselling data. Sends nothing online. Approved by Megan via OPS handoff Nov 1; re-scanned by AEO agent before install. |
| offers | same repo/commit · MIT · skills/offers/ | `.claude/skills/offers` | SAFE. 10 files (SKILL.md, 8 references, evals.json). Text only, 0 hidden Unicode, no URLs/commands. Bans fake scarcity/countdowns. Sends nothing online. |
| competitor-profiling | same repo/commit · MIT · skills/competitor-profiling/ | `.claude/skills/competitor-profiling` | SAFE. 4 files (SKILL.md, tool-reference.md, templates.md, evals.json). Text only, 0 hidden Unicode, no commands; URLs are placeholders (competitor1.com) and registry docs. Sends nothing online. |
Not installed: the rest of the library.

## newsletter-writer (naveedharri/benai-skills) · scanned Nov 5, 2026 · NOT INSTALLED (method borrowed)
- Source: https://github.com/naveedharri/benai-skills/tree/main/shared-skills/newsletter-writer (MIT), listed on mcpmarket.com. Install cmd would be `npx skillfish add naveedharri/benai-skills newsletter-writer` (not run).
- Files: SKILL.md + references 01–05 read in full; 08 (example newsletters, 649 lines) scanned for instructions/network/install/key patterns. No hidden instructions, no scripts, no installs, no key or .env reading. References hold another person's private business details (team, revenue), so nothing from them is copied.
- Network: optional Apify scraper tools (paid, not connected here). No key reading.
- ⚠️ Self-modifying: its "PROGRESSIVE SELF-UPDATE RULE" edits its own SKILL.md without asking. Against our rules (agents may not change skills without Megan's approval).
- ⚠️ Written entirely for another creator (Ben Van Sprundel): his voice, offers, prices, story. Unusable as-is.
- Decision: not installed. Its step-by-step method (5 angles → 3 outlines → write → 10 subject lines) was adapted into our Notion "Skill: Newsletter (ISSUE11 + Glammi Studio)" v0.2 in our own voice.

## Nov 5, 2026: claude-ads (AgriciDaniel/claude-ads) — INSTALLED Nov 5 (Megan: "Sure !")
Requested by Megan ("Yes Claude ads", "I want the whole thing"). Source: github.com/AgriciDaniel/claude-ads · MIT · pinned commit fc3908e786c318776df89a3a098333da377364be · 434 files (12 ad platforms, 33 sub-skills, 25 agents, Python core + scripts, optional Cockpit mod). Scanned by OPS + 3 read-only scan agents; nothing from the repo was run.
- Every installed file read in full (skills, ads/ refs, agents, docs, claude_ads_core, 14 installed scripts incl. release.py, 29 control-plane runtime files). Non-installed dev files (CI, dev inventories, verify_managed_install.py) grep-checked. Hidden/zero-width Unicode across all files: 0. Prompt injection: none.
- Network: nothing automatic, no telemetry. Only on explicit run: user-given landing-page URLs (SSRF-guarded; browser screenshots off unless a signed attestation is set up), paid image APIs (Gemini, OpenAI, Stability, Replicate; up to 50 calls per batch; reference images get uploaded), WebSearch/WebFetch of official platform pages, public ad libraries, ad-platform MCPs only if connected. Maintainer-only: GitHub/gh API and pip-audit. Install: github.com + PyPI (hash-pinned lock).
- Secrets: reads only named image-API keys / GITHUB_TOKEN from env; never .env, ~/.ssh, cookies; errors scrubbed; refuses to store token values.
- Ad accounts: read-only. capability-manifest: all 12 "live-write" operations disabled; every adapter's apply/rollback raises MutationDisabledError. Skill-level gate: draft by default, exact-plan owner approval + spend ceilings; permanent deletion always refused.
- Persistence: none (no settings.json hooks, rc files, cron, self-update). Optional Cockpit mod (mods/) registers Claude Code event handlers but is only active if enabled separately — do NOT install.
- Low notes: agents/release-verifier.md has Bash (release QA only); very broad trigger description; generated PDF reports carry "Powered by claude-ads" + GitHub link (remove before sending to a Glammi client); several reference claims hit their refresh date Nov 6 2026 → results marked provisional until refreshed.
Verdict: SAFE. Installed into `.claude/skills/ads` + 33 `.claude/skills/ads-*` + 24 `.claude/agents` (upstream installer layout, copied by hand; installer not run, no venv). Excluded: mods/ (Cockpit), scripts/release.py, agents/release-verifier.md. Overrides block added to ads/SKILL.md. New agent: `.claude/agents/growth-media-buyer.md` (💚 GROWTH — Media Buyer).

## Nov 5, 2026: 9 more skills from coreyhaines31/marketingskills — INSTALLED (Megan: "all 9", "making sure they're safe")
Source: github.com/coreyhaines31/marketingskills · MIT (LICENSE copied into each) · commit 88c79f6528a9347420e57ceb1fff9a60de651768. Installed as `.claude/skills/<name>`: launch, paywalls, onboarding, referrals, social, pricing, lead-magnets, public-relations, cro. 60 files, all read in full by 2 read-only scan agents (29 + 31); automated checks for hidden Unicode, HTML comments, install commands: none. Nothing run.
- Text only (markdown + eval JSON). No scripts, hooks, auto-install, secret reading or spending. Reads only a local product-marketing.md if present.
- What it sends online: only if asked for social listening / newsjacking — read-only public GETs to reddit.com, hn.algolia.com, public.api.bsky.app, youtube.com/feeds, news.google.com with a search keyword. Everything else is reference links.
- Concerns fixed with overrides blocks: social (browser-driving logged-in LinkedIn/X, Apify/PhantomBuster scraping, scheduler publishing, a manufactured-vulnerability example) → banned; Typefully drafts only. public-relations: guessed emails + scraping banned; "Re: [their real headline]" allowed by Megan Nov 5 ("PR: allw the \"Re\""), never a fake past thread. launch (partner/affiliate mentions) → stripped. cro/lead-magnets example social-proof numbers → real counts only.
Common override on all 9: agents draft, Megan acts; real proof only; Megan's copy rules; no paid tools without her OK.
Not installed: the rest of the library (conversion-tracking has website JS snippets; skipped).
