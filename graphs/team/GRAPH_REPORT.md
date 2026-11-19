# Graph Report - Autonomousangents  (2026-11-19)

## Corpus Check
- 20 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 400 nodes · 744 edges · 33 communities (25 shown, 8 thin omitted)
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 175 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Pipeline lessons learned (lessons.md)
- Pipeline Planner / Architect
- Spec: Core loop 1
- CURRENT FACTS box (read first; OPS updat
- ISSUE11 repo rules (CLAUDE.md)
- Rule: graphify for every agent, split in
- Locked loved pin template set (COLOR-TES
- BANK rule: agents never invent quote/car
- Third-party skills install & scan log
- Rule 7: scan every skill/plugin before i
- Brand guide palette (Blush, Pink, Cream,
- $300/mo Instagram ads test, launches Nov
- Logic map per tab (board 26) as source f
- Daily article publish always allowed; re
- Customer Panel (synthetic customer teste
- Glammi audience: med spas, derm, cosmeti
- GROWTH Media Buyer
- GROWTH Pinterest SEO agent
- Apify apt_marble/pinterest-trends-scrape
- Pinterest Trends searchVolume is a 0-100
- AI-generated images = editorial mood onl
- Framer: always pass draft:true on addIte
- Metricool schedules pins (createSchedule
- Core positioning: manifestation done rig
- Customer Panel synthetic tests (390px ca
- Public name: Megan Scott Manolova
- Every pin shows issue11.app and links wi
- Self-improvement loop with an independen
- Routine frequency cut to ~30 runs/day (u
- Stale Framer page fix: make a real edit 
- "The New Way of Manifestation" positioni
- Luxury brand logos on bags may stay in p
- Megan to-do status Nov 18: waitlist test

## God Nodes (most connected - your core abstractions)
1. `Pipeline lessons learned (lessons.md)` - 236 edges
2. `Third-party skills install & scan log` - 29 edges
3. `ISSUE11 repo rules (CLAUDE.md)` - 21 edges
4. `CURRENT FACTS box (read first; OPS updates Fridays)` - 19 edges
5. `Production Safety Rule` - 18 edges
6. `Pipeline Planner / Architect` - 18 edges
7. `Pipeline Reviewer / Gatekeeper` - 17 edges
8. `Pipeline Builder` - 16 edges
9. `Pipeline QA / Tester` - 15 edges
10. `Spec: Core loop 1` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Verify, don't trust: re-run checks independently; untestable = NOT VERIFIED` --semantically_similar_to--> `Verify by re-fetching, not by an agent's report`  [INFERRED] [semantically similar]
  .claude/agents/pipeline-qa.md → .pipeline/lessons.md
- `Work on feature/<slug> branches, never main` --semantically_similar_to--> `Recommended GitHub branch protection on main`  [INFERRED] [semantically similar]
  CLAUDE.md → .pipeline/README.md
- `OPS never does specialist work itself; brief the owning agent, verify, commit` --conceptually_related_to--> `How OPS runs a task (plan-execute-verify loop, limits)`  [INFERRED]
  .pipeline/lessons.md → CLAUDE.md
- `Production Safety Rule` --conceptually_related_to--> `Stop for Megan's approval (approval-request.md)`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `How OPS runs a task (plan-execute-verify loop, limits)` --conceptually_related_to--> `Loop limits: 2 re-plans, 3 build/QA rounds, 2 review fails`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core loop 1 data layer (repos + migration + RLS)** — _pipeline_spec_scribe_repo, _pipeline_spec_world_repo, _pipeline_spec_prompt_repo, _pipeline_spec_core_loop_1_migration, _pipeline_spec_rls_policies [EXTRACTED 1.00]
- **Dev pipeline flow (Planner → Builder → QA → Reviewer → Megan approval)** — _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, claude_development_pipeline [EXTRACTED 1.00]
- **ISSUE11 dev pipeline: orchestrator, planner, builder, QA, reviewer, approval gate** — _claude_commands_pipeline_pipeline_orchestrator, _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, _claude_commands_pipeline_megan_approval_gate [EXTRACTED 1.00]
- **ASO tool stack Nov 18 (Applyra + ASOMobile + listing v15)** — _claude_vendor_installed_skills_applyra_connector, _claude_vendor_installed_skills_asomobile_connector, _pipeline_lessons_aso_listing_v15, _pipeline_lessons_two_tool_keyword_rule [INFERRED 0.85]
- **Growth agents that draft only and leave posting/spend to Megan** — _claude_agents_growth_media_buyer_media_buyer_agent, _claude_agents_growth_pinterest_seo_pinterest_seo_agent, _claude_agents_growth_reddit_specialist_reddit_specialist_agent, _claude_agents_customer_panel_customer_panel_agent [INFERRED 0.85]
- **ISSUE11 copy authenticity rules (no invented lines, Lexicon, anti-slop, ask don't invent)** — _pipeline_lessons_bank_rule, _pipeline_lessons_lexicon_brand_voice, _pipeline_lessons_anti_slop_rule, _pipeline_lessons_dont_make_things_up, _pipeline_lessons_first_person_affirmations, _pipeline_lessons_carousel_bank_rule, _pipeline_lessons_voice_guide_first [INFERRED 0.85]
- **Pinterest traffic engine toward 100k visitors/month** — _pipeline_lessons_goal_100k_visitors, _pipeline_lessons_pinterest_seo_agent, _pipeline_lessons_loved_pin_formats, _pipeline_lessons_pinterest_posting_ramp, _pipeline_lessons_metricool_scheduling, _pipeline_lessons_pin_website_utm [INFERRED 0.85]

## Communities (33 total, 8 thin omitted)

### Community 0 - "Pipeline lessons learned (lessons.md)"
Cohesion: 0.05
Nodes (28): Pipeline lessons learned (lessons.md), 17MedSpa article recipe (volume-led topics, layer paragraph, PMC/AAD/FDA), 17MedSpa articles paused (site has no blog); no coordination with their agency, Angle idea: "How to use AI to manifest your dream life", Plan: ISSUE11 launch + marketing → content for both → Glammi sprint to 10k, Claude Design canvas max 512 files per version, Glammi cold outreach paused (owned by separate agent), ISSUE11 editorial source of truth = design/editorial/ (+20 more)

### Community 1 - "Pipeline Planner / Architect"
Cohesion: 0.08
Nodes (31): Pipeline Builder (agent file), Pipeline Builder, Writes .pipeline/implementation-log.md (append rounds: files, decisions, checks, fixes), Pipeline Planner / Architect (agent file), Writes .pipeline/acceptance-criteria.md (numbered AC-n, PASS/FAIL testable), Spec section: App Store compliance check, Spec section: Loop stage (DESIRE→IMAGINE→EMBODY→BECOME test), Pipeline Planner / Architect (+23 more)

### Community 2 - "Spec: Core loop 1"
Cohesion: 0.09
Nodes (31): Writes .pipeline/spec.md (summary, files, architecture, DB, deps, edge cases, security), Acceptance criteria: Core loop 1 (AC-1..AC-68), Auth criteria AC-13..AC-24, Core loop 1 acceptance criteria, Process criteria AC-67..AC-68 (feature branch, no live migration), Scribe criteria AC-25..AC-43, Database/security criteria AC-55..AC-63 (RLS isolation, no secrets), Your World criteria AC-44..AC-54 (+23 more)

### Community 3 - "CURRENT FACTS box (read first; OPS updat"
Cohesion: 0.08
Nodes (17): beehiiv connector (read-only by default), Megan builds the app herself in Replit, App status checklist (design/APP-STATUS-2026-11-19.md): ~70% design; Replit has old tabs, beehiiv plan blocks agent writes to forms/automations, Before any Replit prompt, sweep boards against CURRENT FACTS + recent lessons, CURRENT FACTS box (read first; OPS updates Fridays), Glammi prices not confirmed (two-option retainer draft), iPostal1 notary done Nov 18; address unlocks privacy, email footers, citations (+9 more)

### Community 4 - "ISSUE11 repo rules (CLAUDE.md)"
Cohesion: 0.10
Nodes (16): The Editor (art direction + mise en page) (agent file), MISE-EN-PAGE.md magazine rules (US Letter, Inter Tight), The Editor (art direction + mise en page), /decision-brief command, Decision brief format (recommendation, numbers, reasoning, 2 options, risks), Anthropic cookbook Chief of Staff (tutorial; pattern adopted), /decision-brief command (executive brief pattern), Lucky Star renamed "The Editor" (+8 more)

### Community 5 - "Rule: graphify for every agent, split in"
Cohesion: 0.11
Nodes (19): GROWTH Reddit Specialist (agent file), Graphify note: load skill and read map piece first (pinned 0.9.111), Reddit loop: monitor → pick 5 → draft disclosed replies → report → track UTM, drafts/growth/reddit-playbook.md (keyword lists), GROWTH Reddit Specialist, Reddit UTM format (utm_source=reddit, organic, thread slug), Weekly report drafts/growth/reddit/<date>.md, Graphify note: load skill and read map piece first (pinned 0.9.111) (+11 more)

### Community 6 - "Locked loved pin template set (COLOR-TES"
Cohesion: 0.11
Nodes (10): Article pins only from approved favourites; phone-notes article pins rejected, CAR5 carousel design language (vary layouts, same family), Pinterest carousels max 5 slides; plan 7-slide IG/TikTok with cut marks, "ISSUE11 Editorial Hooks & Visual Philosophy" source; hooks reframed to lexicon, Carousel hooks from real viral hooks (HOOKS.md), Locked loved pin template set (COLOR-TEST.md), Bold gestures that ARE the message are on-brand for ISSUE11 covers, Phone-notes pin format (lowercase, issue11.app line, no footer) (+2 more)

### Community 7 - "BANK rule: agents never invent quote/car"
Cohesion: 0.14
Nodes (4): Anti-slop checklist doc, Carousel and post copy built from LEXICON.md terms word for word, source noted, Mermaid mini carousel credits Paris Hilton (Megan's call), Read the ISSUE11 Brand Voice Guide first and run its AI-giveaways table

### Community 8 - "Third-party skills install & scan log"
Cohesion: 0.17
Nodes (12): Third-party skills install & scan log, claude-persona skill (installed as persona), Nov 17 skills: content-writing-thought-leadership, social-content-ar, content-strategist-ar, openclaudia email-subject-lines (FAIL: sources .env, sends via Resend), frontend-design (Anthropic) scanned Oct 21: SAFE, not installed, coreyhaines31/marketingskills (installed in full Nov 15, upstream text + overrides block), muapi-skills (NOT installed; sources .env), newsletter-writer (NOT installed: self-modifying, another creator's voice; method borrowed) (+4 more)

### Community 9 - "Rule 7: scan every skill/plugin before i"
Cohesion: 0.15
Nodes (13): Applyra connector (claude.ai remote MCP, Nov 18): scan PASSED with notes; Unlimited $9.99/mo, ASOMobile connector (claude.ai remote MCP, Nov 18): scan PASSED with rules; free week has no API tokens, ECC chief-of-staff agent (NOT installed: auto-archive, git-push personal notes), App Masters: big terms only count in name/subtitle; small list stays at 20, Decision: Applyra Unlimited is the ongoing ASO tool (Astro, GrowASO skipped), ASO listing v15 request: build from week-3 plan + ASOMobile/Astro exports, ASO & Opportunity Scout does all ISSUE11 ASO, following the App Masters framework, ASOMobile free week Nov 16-22, then 50% off window for the paid month (+5 more)

### Community 10 - "Brand guide palette (Blush, Pink, Cream,"
Cohesion: 0.18
Nodes (8): Brand guide palette (Blush, Pink, Cream, Grey, Black), CAR14–CAR15 rejected; new carousels paused except diagram direction, Carousels mix playbook frameworks via DESIRE→IMAGINE→ACT→EVOLVE, one diagram, Electric Soft hero gradient (issue11.app), Megan's 11 framework diagrams = content redrawn in ISSUE11 style, Reference diagrams are content, not style: redraw in ISSUE11's own look, Graph pins keep layout, change colours: brand pinks, cream, red, lilac, Pin graph style: #100 hand arrows, LG9/LG10, brand pastel palette, no words in shapes

### Community 11 - "$300/mo Instagram ads test, launches Nov"
Cohesion: 0.18
Nodes (6): Ad creative direction: I Am-style vertical video, $300/mo Instagram ads test, launches Nov 17 (own photos + text screen only), 2027 Life Glow Up Kit (formerly Personal Rebrand Kit), Do not credit site visits to Pinterest; ask for Framer Analytics Sources, Privacy pages updated (issue11.app, new glammi.ai/privacy), Free manifestation wallpaper maker (issue11.app/wallpapers)

### Community 12 - "Logic map per tab (board 26) as source f"
Cohesion: 0.20
Nodes (8): Retention: weeks-showing-up streak (never resets), unlocks every 5 pages, endless Explore, In-app feedback: "What are we missing?" + "Help us improve", Layout picker: "Let the Editor decide" + 4 layouts + More layouts, Explain app logic as "one week in her life" (day-by-day table), Logic map per tab (board 26) as source for Replit update, The Editor (Lucky Star) architecture: GUIDE on Home, ASSIST per screen, KNOWN→RETRIEVE→ASK→GENERATE→KEEP, Lulu print/shipping rules and margin (design/PRINT-PURCHASE.md), Printed Issue = 40 pages, $29.99 via Lulu

### Community 13 - "Daily article publish always allowed; re"
Cohesion: 0.20
Nodes (7): Verify live pages by <title> (Googlebot UA, re-fetch), not the 200 status, i11-publish-one fake-review safety gate, NexApp template traces cleanup (alt text, controls, screenshots), Glammi: 2 articles a day, Add 2 inbound "Keep reading" links to each new article, IndexNow ping on every publish (both sites), Use Search Console, not site:, for index counts

### Community 14 - "Customer Panel (synthetic customer teste"
Cohesion: 0.28
Nodes (9): Customer Panel (synthetic customer tester) (agent file), Customer Panel (synthetic customer tester), synthetic-crowd panel test (same seed, A vs B), synthetic-crowd skill (claude -p per persona), synthetic-user-feedback skill (Playwright personas), Goal: 100k visitors/month to issue11.app, Goal: 500 paying app subscribers/month over time, Marketing Room shared session (100K-PLAN.md, ROOM.md) (+1 more)

### Community 15 - "Glammi audience: med spas, derm, cosmeti"
Cohesion: 0.25
Nodes (6): Duplicated Framer pages keep per-breakpoint/component text; patch all and grep live HTML, Glammi medical vertical = med spas, derm, plastic surgeons, cosmetic dentists, Glammi audience: med spas, derm, cosmetic dentists, jewelers, beauty e-commerce, Glammi sitewide black footer (industries, legal), Glammi blog verticals add local, creative, beauty e-commerce, perfume, indie fashion, Glammi positioning: Discoverability x Desirability

### Community 16 - "GROWTH Media Buyer"
Cohesion: 0.38
Nodes (7): GROWTH Media Buyer (agent file), Monday competitor ad watch (Meta Ad Library), GROWTH Media Buyer, claude-ads (AgriciDaniel) installed Nov 5: 34 ads skills + 24 agents, Meta Ads MCP review (read tools only; writes need approval), claude-ads installed + GROWTH Media Buyer agent, Media Buyer owns weekly competitor ad watch (no new agent)

### Community 17 - "GROWTH Pinterest SEO agent"
Cohesion: 0.40
Nodes (5): GROWTH Pinterest SEO agent (agent file), Per-pin SEO row (title, description, board, alt text, link), GROWTH Pinterest SEO agent, 4 Pinterest skills (pinterest-growth, -seo, -pin-design, -growth-manager), New agent: GROWTH Pinterest SEO (Claude Design)

### Community 18 - "Apify apt_marble/pinterest-trends-scrape"
Cohesion: 0.33
Nodes (5): Apify lergassy~pinterest-search-scraper research, Apify apt_marble/pinterest-trends-scraper (PASS), Apify actors Nov 17: instagram-hashtag-scraper, tiktok-scraper (no login, capped by maxTotalChargeUsd), Apify pinterest-search-scraper takes `keywords` array, Tools Megan has: Apify, Metricool, Resend, Mangools, Meta Ads (read-only), Astro/ASOMobile

### Community 19 - "Pinterest Trends searchVolume is a 0-100"
Cohesion: 0.33
Nodes (5): Manifestation pins evergreen; vision board peaks Dec–Jan, Pinterest API (ads:read) for keyword volume ranges, Pinterest API set up with ads:read token via request_credential, Pinterest Trends searchVolume is a 0-100 index, not a count, Seasonal Dec/Jan vision board pages live before Dec 20

### Community 20 - "AI-generated images = editorial mood onl"
Cohesion: 0.50
Nodes (3): Check image twins across brands (32x32 RMSE<500) before use, Pins with AI people go out without AI label (Megan's call), Megan photo library canvas (design/photo-library/)

### Community 22 - "Metricool schedules pins (createSchedule"
Cohesion: 0.50
Nodes (3): Metricool connector (OK to connect, schedule only with OK), Metricool schedules pins (createScheduledPost always allowed; only approved batches), Metricool updateScheduledPost needs full resend; each update returns a new id

### Community 24 - "Customer Panel synthetic tests (390px ca"
Cohesion: 0.50
Nodes (4): Customer Panel synthetic tests (390px captures, never submit live form), Text panels can't judge visual fixes; test copy fixes on top of layout fixes, Megan OK to apply waitlist-page review fixes on issue11.app and publish, issue11.app reviewed with waitlist-page skill; Megan OK'd fixes

### Community 25 - "Public name: Megan Scott Manolova"
Cohesion: 0.50
Nodes (3): Public name: Megan Scott Manolova, Queen of AEO experiment (thequeenofaeo.com), Taste Engine Optimization (TEO) term

### Community 29 - "Stale Framer page fix: make a real edit "
Cohesion: 0.67
Nodes (3): Framer edits land on auto-branches: merge, check status, publish, verify live, Framer publish can serve the previous state; re-fetch live and republish, Stale Framer page fix: make a real edit then republish

## Ambiguous Edges - Review These
- `Give facts and options, not opinions, unless Megan asks` → `Rule: every question to Megan comes with recommended answer + reasoning`  [AMBIGUOUS]
  .pipeline/lessons.md · relation: conceptually_related_to

## Knowledge Gaps
- **52 isolated node(s):** `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)`, `GROWTH Pinterest SEO agent (agent file)`, `The Editor (art direction + mise en page) (agent file)` (+47 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 71 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Pipeline lessons learned (lessons.md)` connect `Pipeline lessons learned (lessons.md)` to `Pipeline Planner / Architect`, `Spec: Core loop 1`, `CURRENT FACTS box (read first; OPS updat`, `ISSUE11 repo rules (CLAUDE.md)`, `Rule: graphify for every agent, split in`, `Locked loved pin template set (COLOR-TES`, `BANK rule: agents never invent quote/car`, `Third-party skills install & scan log`, `Rule 7: scan every skill/plugin before i`, `Brand guide palette (Blush, Pink, Cream,`, `$300/mo Instagram ads test, launches Nov`, `Logic map per tab (board 26) as source f`, `Daily article publish always allowed; re`, `Customer Panel (synthetic customer teste`, `Glammi audience: med spas, derm, cosmeti`, `GROWTH Media Buyer`, `GROWTH Pinterest SEO agent`, `Apify apt_marble/pinterest-trends-scrape`, `Pinterest Trends searchVolume is a 0-100`, `AI-generated images = editorial mood onl`, `Framer: always pass draft:true on addIte`, `Metricool schedules pins (createSchedule`, `Core positioning: manifestation done rig`, `Customer Panel synthetic tests (390px ca`, `Public name: Megan Scott Manolova`, `Every pin shows issue11.app and links wi`, `Self-improvement loop with an independen`, `Routine frequency cut to ~30 runs/day (u`, `Stale Framer page fix: make a real edit `, `"The New Way of Manifestation" positioni`, `Luxury brand logos on bags may stay in p`?**
  _High betweenness centrality (0.833) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `Production Safety Rule` (e.g. with `Builder commits on feature branch only; no push, deploy, merge or live migrations` and `Install skills as original upstream files; report risks`) actually correct?**
  _`Production Safety Rule` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)` to the rest of the system?**
  _52 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Pipeline lessons learned (lessons.md)` be split into smaller, more focused modules?**
  _Cohesion score 0.05272895467160037 - nodes in this community are weakly interconnected._
- **Why does `ISSUE11 repo rules (CLAUDE.md)` connect `ISSUE11 repo rules (CLAUDE.md)` to `Pipeline lessons learned (lessons.md)`, `Pipeline Planner / Architect`, `Spec: Core loop 1`, `Rule: graphify for every agent, split in`, `Third-party skills install & scan log`, `Rule 7: scan every skill/plugin before i`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Should `Pipeline Planner / Architect` be split into smaller, more focused modules?**
  _Cohesion score 0.08282828282828283 - nodes in this community are weakly interconnected._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Give facts and options, not opinions, unless Megan asks` and `Rule: every question to Megan comes with recommended answer + reasoning`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._