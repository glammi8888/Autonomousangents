# Graph Report - Autonomousangents  (2026-11-17)

## Corpus Check
- 20 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 295 nodes · 537 edges · 28 communities (15 shown, 13 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 95 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Pipeline lessons learned (lessons.md)
- Third-party skills install & scan log
- ISSUE11 repo rules (CLAUDE.md)
- Spec: Core loop 1
- CURRENT FACTS box (read first; OPS updat
- GROWTH Pinterest SEO agent
- Logic map per tab (board 26) as source f
- BANK rule: agents never invent quote/car
- Daily article publish always allowed; re
- The Editor (art direction + mise en page
- ISSUE11 newsletter moved from beehiiv to
- Locked loved pin template set (COLOR-TES
- Carousels: funny/delulu hook + education
- Every lead magnet is email-gated with re
- Framer: always pass draft:true on addIte
- AI-generated images = editorial mood onl
- Megan's 11 framework diagrams = content 
- $300/mo Instagram ads test, launches Nov
- Public name: Megan Scott Manolova
- Core positioning: manifestation done rig
- Glammi positioning: Discoverability x De
- Framer images via raw.githubusercontent 
- Glammi covers: chrome theme, Megan's vis
- Glammi sitewide black footer (industries
- Manifestation pins evergreen; vision boa
- "The New Way of Manifestation" positioni

## God Nodes (most connected - your core abstractions)
1. `Pipeline lessons learned (lessons.md)` - 183 edges
2. `Third-party skills install & scan log` - 21 edges
3. `ISSUE11 repo rules (CLAUDE.md)` - 21 edges
4. `Production Safety Rule` - 17 edges
5. `CURRENT FACTS box (read first; OPS updates Fridays)` - 17 edges
6. `Spec: Core loop 1` - 13 edges
7. `Pipeline orchestrator (acts for OPS Manager)` - 11 edges
8. `Pipeline Planner / Architect` - 10 edges
9. `GROWTH Pinterest SEO agent` - 9 edges
10. `Development pipeline (Planner→Builder→QA→Reviewer→Approval)` - 9 edges

## Surprising Connections (you probably didn't know these)
- `Locked loved pin template set (COLOR-TEST.md)` --conceptually_related_to--> `Pin rules (Notes pins, photo-led, logo, Inter Tight, 1000x1500)`  [INFERRED]
  .pipeline/lessons.md → .claude/agents/growth-pinterest-seo.md
- `Work on feature/<slug> branches, never main` --semantically_similar_to--> `Recommended GitHub branch protection on main`  [INFERRED] [semantically similar]
  CLAUDE.md → .pipeline/README.md
- `Production Safety Rule` --conceptually_related_to--> `Stop for Megan's approval (approval-request.md)`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `How OPS runs a task (plan-execute-verify loop, limits)` --conceptually_related_to--> `Loop limits: 2 re-plans, 3 build/QA rounds, 2 review fails`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `Customer Panel (synthetic customer tester)` --references--> `ICP: people who tried manifestation and think it doesn't work (women ~30-38)`  [INFERRED]
  .claude/agents/customer-panel.md → .pipeline/lessons.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core loop 1 data layer (repos + migration + RLS)** — _pipeline_spec_scribe_repo, _pipeline_spec_world_repo, _pipeline_spec_prompt_repo, _pipeline_spec_core_loop_1_migration, _pipeline_spec_rls_policies [EXTRACTED 1.00]
- **ISSUE11 dev pipeline: orchestrator, planner, builder, QA, reviewer, approval gate** — _claude_commands_pipeline_pipeline_orchestrator, _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, _claude_commands_pipeline_megan_approval_gate [EXTRACTED 1.00]
- **Growth agents that draft only and leave posting/spend to Megan** — _claude_agents_growth_media_buyer_media_buyer_agent, _claude_agents_growth_pinterest_seo_pinterest_seo_agent, _claude_agents_growth_reddit_specialist_reddit_specialist_agent, _claude_agents_customer_panel_customer_panel_agent [INFERRED 0.85]
- **Daily blog publish flow (Framer draft → gate → publish → IndexNow → inbound links)** — _pipeline_lessons_framer_draft_true, _pipeline_lessons_fake_review_gate, _pipeline_lessons_daily_publish_always_allowed, _pipeline_lessons_indexnow, _pipeline_lessons_inbound_links_daily, _pipeline_lessons_one_article_per_day [INFERRED 0.85]
- **ISSUE11 copy authenticity rules (no invented lines, Lexicon, anti-slop, ask don't invent)** — _pipeline_lessons_bank_rule, _pipeline_lessons_lexicon_brand_voice, _pipeline_lessons_anti_slop_rule, _pipeline_lessons_dont_make_things_up, _pipeline_lessons_first_person_affirmations [INFERRED 0.85]
- **Pinterest traffic engine toward 100k visitors/month** — _pipeline_lessons_goal_100k_visitors, _pipeline_lessons_pinterest_seo_agent, _pipeline_lessons_loved_pin_formats, _pipeline_lessons_pinterest_posting_ramp, _pipeline_lessons_metricool_scheduling, _pipeline_lessons_pin_website_utm [INFERRED 0.85]

## Communities (28 total, 13 thin omitted)

### Community 0 - "Pipeline lessons learned (lessons.md)"
Cohesion: 0.06
Nodes (24): Pipeline lessons learned (lessons.md), 17MedSpa article recipe (volume-led topics, layer paragraph, PMC/AAD/FDA), 17MedSpa articles paused (site has no blog); no coordination with their agency, Angle idea: "How to use AI to manifest your dream life", Plan: ISSUE11 launch + marketing → content for both → Glammi sprint to 10k, Claude Design canvas max 512 files per version, Glammi cold outreach paused (owned by separate agent), Self-improvement loop with an independent UI/UX critic (+16 more)

### Community 1 - "Third-party skills install & scan log"
Cohesion: 0.08
Nodes (30): Customer Panel (synthetic customer tester) (agent file), Customer Panel (synthetic customer tester), synthetic-crowd panel test (same seed, A vs B), GROWTH Media Buyer (agent file), Monday competitor ad watch (Meta Ad Library), GROWTH Media Buyer, Third-party skills install & scan log, claude-ads (AgriciDaniel) installed Nov 5: 34 ads skills + 24 agents (+22 more)

### Community 2 - "ISSUE11 repo rules (CLAUDE.md)"
Cohesion: 0.11
Nodes (25): Pipeline Builder (agent file), Pipeline Builder, Pipeline Planner / Architect (agent file), Spec section: Loop stage (DESIRE→IMAGINE→EMBODY→BECOME test), Pipeline Planner / Architect, Spec section: Sensitive areas touched, Pipeline QA / Tester (agent file), Pipeline QA / Tester (+17 more)

### Community 3 - "Spec: Core loop 1"
Cohesion: 0.09
Nodes (29): Acceptance criteria: Core loop 1 (AC-1..AC-68), Auth criteria AC-13..AC-24, Process criteria AC-67..AC-68 (feature branch, no live migration), Scribe criteria AC-25..AC-43, Database/security criteria AC-55..AC-63 (RLS isolation, no secrets), Your World criteria AC-44..AC-54, App Store readiness checklist, 5.1.1(v) in-app account deletion (+21 more)

### Community 4 - "CURRENT FACTS box (read first; OPS updat"
Cohesion: 0.09
Nodes (18): GROWTH Reddit Specialist (agent file), Reddit loop: monitor → pick 5 → draft disclosed replies → report → track UTM, GROWTH Reddit Specialist, /decision-brief command, Decision brief format (recommendation, numbers, reasoning, 2 options, risks), Anthropic cookbook Chief of Staff (tutorial; pattern adopted), Megan builds the app herself in Replit, Brand guide palette (Blush, Pink, Cream, Grey, Black) (+10 more)

### Community 5 - "GROWTH Pinterest SEO agent"
Cohesion: 0.12
Nodes (14): GROWTH Pinterest SEO agent (agent file), Apify lergassy~pinterest-search-scraper research, Per-pin SEO row (title, description, board, alt text, link), GROWTH Pinterest SEO agent, Apify apt_marble/pinterest-trends-scraper (PASS), Apify pinterest-search-scraper takes `keywords` array, Goal: 100k visitors/month to issue11.app, Goal: 500 paying app subscribers/month over time (+6 more)

### Community 6 - "Logic map per tab (board 26) as source f"
Cohesion: 0.13
Nodes (12): Retention: weeks-showing-up streak (never resets), unlocks every 5 pages, endless Explore, Lucky Star renamed "The Editor", In-app feedback: "What are we missing?" + "Help us improve", Layout picker: "Let the Editor decide" + 4 layouts + More layouts, Logic map per tab (board 26) as source for Replit update, The Editor (Lucky Star) architecture: GUIDE on Home, ASSIST per screen, KNOWN→RETRIEVE→ASK→GENERATE→KEEP, Lulu print/shipping rules and margin (design/PRINT-PURCHASE.md), "My World" renamed "My saves" (+4 more)

### Community 8 - "Daily article publish always allowed; re"
Cohesion: 0.22
Nodes (6): i11-publish-one fake-review safety gate, NexApp template traces cleanup (alt text, controls, screenshots), Glammi: 2 articles a day, Add 2 inbound "Keep reading" links to each new article, IndexNow ping on every publish (both sites), Use Search Console, not site:, for index counts

### Community 9 - "The Editor (art direction + mise en page"
Cohesion: 0.32
Nodes (4): The Editor (art direction + mise en page) (agent file), MISE-EN-PAGE.md magazine rules (US Letter, Inter Tight), The Editor (art direction + mise en page), New agent: The Editor (magazine layouts, MISE-EN-PAGE.md)

### Community 10 - "ISSUE11 newsletter moved from beehiiv to"
Cohesion: 0.40
Nodes (3): beehiiv connector (read-only by default), beehiiv plan blocks agent writes to forms/automations, ISSUE11 newsletter moved from beehiiv to Resend

### Community 11 - "Locked loved pin template set (COLOR-TES"
Cohesion: 0.40
Nodes (4): CAR5 carousel design language (vary layouts, same family), Locked loved pin template set (COLOR-TEST.md), Phone-notes pin format (lowercase, issue11.app line, no footer), Pinterest agent makes 10–20 variations of favourites for nightly pick

### Community 13 - "Every lead magnet is email-gated with re"
Cohesion: 0.40
Nodes (3): 2027 Life Glow Up Kit (formerly Personal Rebrand Kit), Privacy pages updated (issue11.app, new glammi.ai/privacy), Free manifestation wallpaper maker (issue11.app/wallpapers)

### Community 15 - "AI-generated images = editorial mood onl"
Cohesion: 0.50
Nodes (3): Check image twins across brands (32x32 RMSE<500) before use, Pins with AI people go out without AI label (Megan's call), Megan photo library canvas (design/photo-library/)

### Community 16 - "Megan's 11 framework diagrams = content "
Cohesion: 0.50
Nodes (4): CAR14–CAR15 rejected; new carousels paused except diagram direction, Carousels mix playbook frameworks via DESIRE→IMAGINE→ACT→EVOLVE, one diagram, Megan's 11 framework diagrams = content redrawn in ISSUE11 style, Pin graph style: #100 hand arrows, LG9/LG10, brand pastel palette, no words in shapes

### Community 18 - "Public name: Megan Scott Manolova"
Cohesion: 0.50
Nodes (3): Public name: Megan Scott Manolova, Queen of AEO experiment (thequeenofaeo.com), Taste Engine Optimization (TEO) term

## Knowledge Gaps
- **35 isolated node(s):** `/pipeline command`, `Pipeline Planner / Architect (agent file)`, `Pipeline Builder (agent file)`, `Pipeline QA / Tester (agent file)`, `Pipeline Reviewer / Gatekeeper (agent file)` (+30 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 49 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Pipeline lessons learned (lessons.md)` connect `Pipeline lessons learned (lessons.md)` to `Third-party skills install & scan log`, `ISSUE11 repo rules (CLAUDE.md)`, `Spec: Core loop 1`, `CURRENT FACTS box (read first; OPS updat`, `GROWTH Pinterest SEO agent`, `Logic map per tab (board 26) as source f`, `BANK rule: agents never invent quote/car`, `Daily article publish always allowed; re`, `The Editor (art direction + mise en page`, `ISSUE11 newsletter moved from beehiiv to`, `Locked loved pin template set (COLOR-TES`, `Carousels: funny/delulu hook + education`, `Every lead magnet is email-gated with re`, `Framer: always pass draft:true on addIte`, `AI-generated images = editorial mood onl`, `Megan's 11 framework diagrams = content `, `$300/mo Instagram ads test, launches Nov`, `Public name: Megan Scott Manolova`, `Core positioning: manifestation done rig`, `Glammi positioning: Discoverability x De`, `Borrow functionality from other builds, `, `ISSUE11 owns "Become your own dream girl`, `Framer images via raw.githubusercontent `, `Glammi covers: chrome theme, Megan's vis`, `Glammi sitewide black footer (industries`, `Manifestation pins evergreen; vision boa`, `"The New Way of Manifestation" positioni`?**
  _High betweenness centrality (0.844) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Production Safety Rule` (e.g. with `Install skills as original upstream files; report risks` and `Standing permission: always publish glammi.ai and issue11.app`) actually correct?**
  _`Production Safety Rule` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `/pipeline command`, `Pipeline Planner / Architect (agent file)`, `Pipeline Builder (agent file)` to the rest of the system?**
  _35 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Pipeline lessons learned (lessons.md)` be split into smaller, more focused modules?**
  _Cohesion score 0.05609756097560976 - nodes in this community are weakly interconnected._
- **Why does `ISSUE11 repo rules (CLAUDE.md)` connect `ISSUE11 repo rules (CLAUDE.md)` to `Pipeline lessons learned (lessons.md)`, `Third-party skills install & scan log`, `Spec: Core loop 1`, `CURRENT FACTS box (read first; OPS updat`, `GROWTH Pinterest SEO agent`, `Logic map per tab (board 26) as source f`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Should `Third-party skills install & scan log` be split into smaller, more focused modules?**
  _Cohesion score 0.07823613086770982 - nodes in this community are weakly interconnected._
- **Why does `Core loop 1 spec (reference only since Oct 20; Replit wins)` connect `ISSUE11 repo rules (CLAUDE.md)` to `Spec: Core loop 1`, `CURRENT FACTS box (read first; OPS updat`, `Logic map per tab (board 26) as source f`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._