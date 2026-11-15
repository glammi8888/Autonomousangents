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

## Newsletter skills search · Nov 7, 2026 (OPS, Megan: "look for any reputable newsletter skills maybe MIT")
- **openclaudia/openclaudia-skills → `newsletter`** (MIT, commit 3def768, Nov 4 2026). 1 file, 232 lines, text only: no scripts, network calls, installs or key reading. SAFE but NOT INSTALLED: generic growth tips that overlap our `emails` skill + Notion "Skill: Newsletter" v0.2; its stats ("lifts 5-10%", CPM tables) are unsourced, and giveaways / buying newsletters don't fit. Its welcome-sequence outline and list-cleaning advice were noted.
- **openclaudia → `email-subject-lines`**: ❌ FAIL. It runs `source ~/.claude/.env.global` and sends real emails via the Resend API with a key. That breaks rules 5 and 7. Never install.
- **beehiiv's own skills** (built into the beehiiv connector, already reviewed Oct 30; nothing to install): automation-dropoff, build-segment, edit-post, media-kit, onboarding, performance-report, revenue-report, start-here, unsubscribe-spikes, upgrade-campaign. Most write tools need the paid beehiiv plan.
- **Resend connector** (claude.ai official directory, Nov 7 2026): Megan to connect. Review on first use: list its tools, confirm the OAuth scope, and log what it can send. Rules: never create or show API keys (it has create-api-key), never send or schedule to subscribers without Megan's OK, only import people who signed up, never copy subscriber emails into the repo.

## Metricool connector (official MCP), checked Nov 9, 2026 (OPS)
- What it is: Metricool's own MCP server at https://ai.metricool.com/mcp. It's listed in Claude's connector directory (Settings → Connectors → Browse → Metricool). The code is public: github.com/metricool/mcp-metricool. It works on Metricool's free plan.
- What it sends online: what Claude asks Metricool for (your connected social accounts, analytics, scheduled posts) goes between Metricool and Claude. It doesn't read files, keys or .env, and it doesn't install anything on a computer. You sign in with Metricool, and no API key is pasted anywhere.
- Rules: agents draft posts and may only schedule them with Megan's OK. Nothing is published without her OK.
- Verdict: OK to connect (official vendor connector, Megan connects it herself).

## Meta Ads MCP (official, by Meta) · custom connector · checked Nov 11, 2026 (OPS)
- What: Meta's own Ads AI Connector (open beta since Apr 29, 2026), URL `https://mcp.facebook.com/ads` (per most guides; one guide lists mcp.meta.com, verify on Meta's page). Free. Megan adds it herself in claude.ai → Settings → Connectors → Add custom connector, signing in with Facebook.
- Chosen over third parties (Windsor.ai, Adspirer, Supermetrics, Lena): no extra company sees our ad data, no subscription, no tool-call caps.
- What it sends online: ad account data flows only between Meta and Claude. No keys in the repo or chat (Facebook login / OAuth).
- Risk: it gets the SAME permissions as Megan, including creating ads and spending. Controls: (1) account spending limit $300 already set; (2) in the connector's tool permissions, set every write/create/update tool to "Needs approval" (or off) and leave read tools on; (3) agent rule: read and recommend only, max 3 changes a week, every change needs Megan's explicit OK (Production Safety Rule, payments/spend).
- Result: OK to connect with the controls above. Not scanned = not installed rule satisfied by this review; re-check after Megan connects (list the actual tool names).

## Apify actor: apt_marble/pinterest-trends-scraper (security check Nov 12, 2026, OPS Manager)
- What: Pinterest Trends top/growing search terms for 34 countries (week/month/year change, seasonality), optional related searches. Run on Apify's servers via api.apify.com.
- Checked (Apify API metadata + input schema, build 0.0.4, updated Oct 27, 2026): inputs are only countries, trend type, max terms, sort, growth filter, related-terms toggle. NO Pinterest login, cookies or account needed. 35/35 runs succeeded in the last 30 days; small actor (15 users, 162 runs total) by an individual developer, so it may break if Pinterest changes.
- Sends online: only our run settings (countries, numbers) to Apify. We never give it Pinterest credentials or personal data. Our Apify API token is stored as a network secret (never in the repo or chat).
- Cost: pay per term, about $0.0012 per term on Apify's free tier (100 terms about $0.12).
- Caveats: Pinterest's terms don't allow scraping; use for occasional keyword research only, never with Megan's Pinterest login. It returns trending lists, it does not look up a word we choose.
- Result: PASS. Approved by Megan Nov 12 ("Pinterest trend scraper is definitely the most efficient and cheap option I LOVE IT").

## ECC agent: chief-of-staff (security check Nov 14, 2026, OPS Manager) · NOT INSTALLED (waiting on Megan's OK for an adapted version)
- Source: github.com/affaan-m/everything-claude-code, agents/chief-of-staff.md, commit d2ef268 (Nov 6, 2026), MIT. One markdown file, 160 lines, read in full.
- What it is: a prompt for an inbox and calendar "chief of staff". It sorts email, Slack, LINE and Messenger into 4 tiers (skip, info only, meeting, action required), drafts replies, writes a daily briefing and runs a follow-up checklist after each send.
- Scan: no hidden instructions, no code that runs, no network calls in the file itself, no reading of keys or .env. It includes a sensible "prompt defense" section.
- Risks as written (why it can't be installed unchanged):
  1. It expects a third-party Gmail CLI ("gog") with OAuth, plus scripts and hooks that aren't in the file (calendar-suggest.js, a PostToolUse hook). Those would be new installs needing their own scan. We already have the Gmail + Google Calendar connectors, so they aren't needed.
  2. It auto-archives "skip" emails and offers [Send]. Both act on Megan's inbox. Our rule is drafts only; nothing sent or archived without Megan.
  3. It writes private/relationships.md and then runs "git commit & push" on it. That would put personal details about people in Megan's life into the GitHub repo, which breaks the CLAUDE.md privacy rule.
- Recommended: install an ISSUE11 version. Same 4-tier triage and briefing; Gmail/Calendar via our connectors (read + drafts only); no auto-archive or send; no relationship notes in the repo; the briefing goes onto Megan Today. It sends nothing online beyond reading Megan's Gmail/Calendar through the connectors she already approved.

## Anthropic claude-cookbooks: "01 The Chief of Staff agent" (security check Nov 14, 2026, OPS Manager)
- Source (Megan's link): github.com/anthropics/claude-cookbooks, claude_agent_sdk/01_The_chief_of_staff_agent.ipynb + chief_of_staff_agent/, MIT (Anthropic). Read: the notebook, CLAUDE.md, settings.local.json, executive output style, strategic-brief command, both hooks, a grep of all scripts.
- What it is: a tutorial showing how to build a Chief of Staff for a made-up startup (TechStart) with the Agent SDK. It covers CLAUDE.md memory, Python scripts via Bash, output styles, plan mode, slash commands, hooks and subagents. It's a teaching example, not a ready skill; its data and finance scripts are fake demo numbers.
- Scan: the hooks only write local JSON audit logs. No network calls, no reading of keys or .env in the agent files (the notebook itself loads an API key from .env to run the demo; we don't run it). Nothing installed from it.
- Adopted (our own text, adapted): `.claude/commands/decision-brief.md`. It uses the "executive" format (recommendation first, real numbers, reasoning, 2 alternatives, risks, next step), which matches Megan's rule "help me make each decision and the reasoning behind it". Not adopted: the demo scripts and data, the hooks (we already log in Notion and lessons), and the Agent SDK runtime (not needed in Claude Code).

## Nov 15, 2026: marketingskills re-check: NOT INSTALLED yet (Megan: "Can you check the marketing-skills on GitHub skill? And scan for safety")
Source: github.com/coreyhaines31/marketingskills · MIT · commit 1f837447b20bb6f0e72d87b80ece1c221c362c7d (Nov 11, 2026). 55 skills; 19 already installed, 36 new.
First-pass scan of all 460 files in skills/: 0 hidden Unicode, no hooks, no allowed-tools, no auto-installs, no instructions to hide anything or read .env/keys. Most skills are markdown only.
Code found (only runs if someone runs it):
- conversion-tracking: 2 local Python helpers (no network), plus GTM recipes and JS snippets meant to be pasted on a website. Their job is to send form-submit events to GA4/Meta/etc.
- reverse-engineer-marketing/scripts/teardown.mjs: fetches public sites, web.archive.org and crt.sh, and api.scrapecreators.com if SCRAPECREATORS_API_KEY is set (paid; never set without Megan's OK).
- ad-creative, image, video: docs show curl/npx examples for paid AI APIs (Gemini, ElevenLabs, Remotion) using env keys. These are examples only and are not run automatically.
Verdict: no malicious content found. Each skill chosen for install still gets a full read of every file before install (rule 7).

## Nov 15, 2026: the rest of marketingskills INSTALLED (Megan: "Install the entirety of it please")
Source: github.com/coreyhaines31/marketingskills · MIT (LICENSE copied into each) · commit 1f837447b20bb6f0e72d87b80ece1c221c362c7d. Installed as `.claude/skills/<name>`: ab-testing, ad-creative, ai-seo, analytics, aso, attribution, churn-prevention, co-marketing, community-marketing, competitors, content-strategy, conversion-tracking, copy-editing, customer-research, directory-submissions, events, free-tools, image, influencer-marketing, link-building, marketing-council, marketing-ideas, marketing-loops, marketing-plan, popups, product-marketing, programmatic-seo, reverse-engineer-marketing, revops, schema, signup, site-architecture, sms, video. The 19 skills installed earlier were left as they were, with their own overrides.
Scan: 4 read-only agents read every file in full, about 290 files. Results: 0 hidden Unicode, no obfuscation, no hidden agent instructions, no secret reads, no persistence. None UNSAFE; all SAFE or SAFE WITH NOTES. Nothing was run.
Code (runs only when someone runs it; never without Megan's OK):
- reverse-engineer-marketing/scripts/teardown.mjs contacts the target site, web.archive.org, crt.sh, SEC, job boards, npm/pypi/github stats and, optionally, api.scrapecreators.com (paid, SCRAPECREATORS_API_KEY). `adoption --github` sends GH_TOKEN to api.github.com.
- conversion-tracking: local Python helpers (don't run check_recipes.py --write) plus website snippets that push events to dataLayer. Its send templates load only the official Google, Meta, LinkedIn, TikTok and Microsoft scripts.
Stripped or patched before install:
- conversion-tracking: removed the "fetch tracklution agent-install.md live and follow it" instruction (remote-instruction risk).
- attribution: removed RB2B visitor de-anonymization.
- directory-submissions: removed tiers 8, 9, 11 and 12, BlackHatWorld and Warrior Forum (about 100 spam-backlink targets), the account "warm up" step and the free-credits-for-mention pitch.
- ad-creative: removed the "fake it" and staged street-interview advice. The iMessage-style ads file is gated behind Megan's OK.
- churn-prevention: removed "block self-serve cancel" and the "offer expires when you leave" line.
- marketing-ideas: removed Engagement Pods and Pixel Sharing; Parasite SEO and giveaways are flagged.
- signup: removed the implicit terms acceptance test.
- popups: timers and deadlines must be real.
- marketing-plan: no push to main.
- marketing-loops: PR mode only; enrolling, sending and suppressing are staged for Megan.
- link-building: fixed broken tool links.
Added an "ISSUE11 / Glammi Studio overrides" block to every SKILL.md: drafts only, no schedules, scripts or installs without OK, no paid tools or keys, real proof only, rule 4 approvals, and fetched content is data.
Kept but flagged (vendor plugs, disclosed in the text): Converly, Attributer, Ploy, LinkDR, Magister, TGScope. marketing-council simulates real marketers: never publish its output as their real words.

**Nov 15 update (Megan: "No don't cut anything before installing"):** every file is now restored to the original upstream text, so nothing is stripped (the items listed under "Stripped or patched before install" are back). The only change from upstream is the appended "ISSUE11 / Glammi Studio overrides" block in each SKILL.md, plus LICENSE.
