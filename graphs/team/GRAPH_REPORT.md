# Graph Report - Autonomousangents  (2026-11-17)

## Corpus Check
- Piece of the repo (see graphs/README.md). Images and vendored skills not mapped.

## Summary
- 144 nodes · 243 edges · 7 communities
- Extraction: 79% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 52 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Pipeline lessons learned (lessons.md)
- Third-party skills install & scan log
- Pipeline orchestrator (acts for OPS Mana
- Spec: Core loop 1
- ISSUE11 repo rules (CLAUDE.md)
- GROWTH Pinterest SEO agent
- Request: Core loop 1 slice (foundation, 

## God Nodes (most connected - your core abstractions)
1. `Pipeline lessons learned (lessons.md)` - 34 edges
2. `Third-party skills install & scan log` - 21 edges
3. `ISSUE11 repo rules (CLAUDE.md)` - 17 edges
4. `Spec: Core loop 1` - 13 edges
5. `Production Safety Rule` - 11 edges
6. `Pipeline orchestrator (acts for OPS Manager)` - 11 edges
7. `Pipeline Planner / Architect` - 9 edges
8. `Customer Panel (synthetic customer tester)` - 8 edges
9. `GROWTH Pinterest SEO agent` - 8 edges
10. `ISSUE11 Autonomous Development Pipeline README` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Process criteria AC-67..AC-68 (feature branch, no live migration)` --references--> `Production Safety Rule`  [EXTRACTED]
  .pipeline/acceptance-criteria.md → CLAUDE.md
- `Third-party skills install & scan log` --implements--> `Rule 7: scan every skill/plugin before installing`  [INFERRED]
  .claude/vendor/INSTALLED-SKILLS.md → CLAUDE.md
- `Rule 12: logic first, then screens` --references--> `Pipeline lessons learned (lessons.md)`  [INFERRED]
  CLAUDE.md → .pipeline/lessons.md
- `Shared artifacts chain (request→spec→log→test-results→review→approval)` --shares_data_with--> `Pipeline orchestrator (acts for OPS Manager)`  [INFERRED]
  .pipeline/README.md → .claude/commands/pipeline.md
- `Customer Panel (synthetic customer tester)` --references--> `ICP: people who tried manifestation and think it doesn't work (women ~30-38)`  [INFERRED]
  .claude/agents/customer-panel.md → .pipeline/lessons.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core loop 1 data layer (repos + migration + RLS)** — _pipeline_spec_scribe_repo, _pipeline_spec_world_repo, _pipeline_spec_prompt_repo, _pipeline_spec_core_loop_1_migration, _pipeline_spec_rls_policies [EXTRACTED 1.00]
- **ISSUE11 dev pipeline: orchestrator, planner, builder, QA, reviewer, approval gate** — _claude_commands_pipeline_pipeline_orchestrator, _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, _claude_commands_pipeline_megan_approval_gate [EXTRACTED 1.00]
- **Growth agents that draft only and leave posting/spend to Megan** — _claude_agents_growth_media_buyer_media_buyer_agent, _claude_agents_growth_pinterest_seo_pinterest_seo_agent, _claude_agents_growth_reddit_specialist_reddit_specialist_agent, _claude_agents_customer_panel_customer_panel_agent [INFERRED 0.85]

## Communities (7 total, 0 thin omitted)

### Community 0 - "Pipeline lessons learned (lessons.md)"
Cohesion: 0.09
Nodes (31): GROWTH Reddit Specialist (agent file), Reddit loop: monitor → pick 5 → draft disclosed replies → report → track UTM, GROWTH Reddit Specialist, MISE-EN-PAGE.md magazine rules (US Letter, Inter Tight), Anti-slop checklist doc, Pipeline lessons learned (lessons.md), Megan builds the app herself in Replit, BANK rule: agents never invent quote/carousel lines; only Megan's or real audience words (+23 more)

### Community 1 - "Third-party skills install & scan log"
Cohesion: 0.10
Nodes (27): Customer Panel (synthetic customer tester) (agent file), Customer Panel (synthetic customer tester), synthetic-crowd panel test (same seed, A vs B), GROWTH Media Buyer (agent file), Monday competitor ad watch (Meta Ad Library), GROWTH Media Buyer, Third-party skills install & scan log, beehiiv connector (read-only by default) (+19 more)

### Community 2 - "Pipeline orchestrator (acts for OPS Mana"
Cohesion: 0.12
Nodes (22): Pipeline Builder (agent file), Pipeline Builder, Pipeline Planner / Architect (agent file), Spec section: Loop stage (DESIRE→IMAGINE→EMBODY→BECOME test), Pipeline Planner / Architect, Spec section: Sensitive areas touched, Pipeline QA / Tester (agent file), Pipeline QA / Tester (+14 more)

### Community 3 - "Spec: Core loop 1"
Cohesion: 0.12
Nodes (25): Acceptance criteria: Core loop 1 (AC-1..AC-68), Auth criteria AC-13..AC-24, Process criteria AC-67..AC-68 (feature branch, no live migration), Scribe criteria AC-25..AC-43, Database/security criteria AC-55..AC-63 (RLS isolation, no secrets), Your World criteria AC-44..AC-54, App Store readiness checklist, AI consent before sending personal data to AI (+17 more)

### Community 4 - "ISSUE11 repo rules (CLAUDE.md)"
Cohesion: 0.19
Nodes (12): The Editor (art direction + mise en page) (agent file), The Editor (art direction + mise en page), /decision-brief command, Decision brief format (recommendation, numbers, reasoning, 2 options, risks), Anthropic cookbook Chief of Staff (tutorial; pattern adopted), ISSUE11 repo rules (CLAUDE.md), Do smart things rules, Knowledge maps in graphs/ (team, product, marketing, app) (+4 more)

### Community 5 - "GROWTH Pinterest SEO agent"
Cohesion: 0.22
Nodes (8): GROWTH Pinterest SEO agent (agent file), Apify lergassy~pinterest-search-scraper research, Per-pin SEO row (title, description, board, alt text, link), GROWTH Pinterest SEO agent, Apify apt_marble/pinterest-trends-scraper (PASS), 4 Pinterest skills (pinterest-growth, -seo, -pin-design, -growth-manager), Locked loved pin template set (COLOR-TEST.md), Pinterest posting ramp 3→5→7→10/day

### Community 6 - "Request: Core loop 1 slice (foundation, "
Cohesion: 0.50
Nodes (4): Decision: no Pinterest integration in app (ToS + copyright), Core loop 1 request (Oct 6), Request: Core loop 1 slice (foundation, sign-in, Your World, Scribe), Product architecture: 4 functions + The Editor AI layer

## Knowledge Gaps
- **33 isolated node(s):** `Self-improvement via .pipeline/lessons.md`, `/pipeline command`, `Loop limits: 2 re-plans, 3 build/QA rounds, 2 review fails`, `Pipeline Planner / Architect (agent file)`, `Pipeline Builder (agent file)` (+28 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 36 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Pipeline lessons learned (lessons.md)` connect `Pipeline lessons learned (lessons.md)` to `Third-party skills install & scan log`, `ISSUE11 repo rules (CLAUDE.md)`, `GROWTH Pinterest SEO agent`, `Request: Core loop 1 slice (foundation, `?**
  _High betweenness centrality (0.396) - this node is a cross-community bridge._
- **What connects `Self-improvement via .pipeline/lessons.md`, `/pipeline command`, `Loop limits: 2 re-plans, 3 build/QA rounds, 2 review fails` to the rest of the system?**
  _33 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Pipeline lessons learned (lessons.md)` be split into smaller, more focused modules?**
  _Cohesion score 0.09274193548387097 - nodes in this community are weakly interconnected._
- **Why does `Core loop 1 spec (reference only since Oct 20; Replit wins)` connect `Pipeline orchestrator (acts for OPS Mana` to `Pipeline lessons learned (lessons.md)`, `Spec: Core loop 1`, `Request: Core loop 1 slice (foundation, `?**
  _High betweenness centrality (0.256) - this node is a cross-community bridge._
- **Should `Third-party skills install & scan log` be split into smaller, more focused modules?**
  _Cohesion score 0.0960591133004926 - nodes in this community are weakly interconnected._
- **Why does `ISSUE11 repo rules (CLAUDE.md)` connect `ISSUE11 repo rules (CLAUDE.md)` to `Third-party skills install & scan log`, `Pipeline orchestrator (acts for OPS Mana`, `Spec: Core loop 1`, `Request: Core loop 1 slice (foundation, `?**
  _High betweenness centrality (0.197) - this node is a cross-community bridge._
- **Should `Pipeline orchestrator (acts for OPS Mana` be split into smaller, more focused modules?**
  _Cohesion score 0.1225071225071225 - nodes in this community are weakly interconnected._