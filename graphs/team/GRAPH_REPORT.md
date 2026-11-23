# Graph Report - Autonomousangents  (2026-11-23)

## Corpus Check
- 20 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 224 nodes · 340 edges · 13 communities (10 shown, 3 thin omitted)
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 69 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Third-party skills install & scan log
- Pipeline Planner / Architect
- Pipeline lessons learned (lessons.md)
- ISSUE11 repo rules (CLAUDE.md)
- Spec: Core loop 1
- CURRENT FACTS box (read first)
- New Way of Manifestation positioning
- App Store readiness checklist
- Framer (issue11.app + glammi.ai)
- GROWTH Reddit Specialist
- Anti-slop checklist doc
- Public name Megan Scott Manolova

## God Nodes (most connected - your core abstractions)
1. `Third-party skills install & scan log` - 29 edges
2. `ISSUE11 repo rules (CLAUDE.md)` - 20 edges
3. `Pipeline Planner / Architect` - 18 edges
4. `Pipeline Reviewer / Gatekeeper` - 17 edges
5. `Production Safety Rule` - 16 edges
6. `Pipeline Builder` - 16 edges
7. `Pipeline QA / Tester` - 15 edges
8. `Spec: Core loop 1` - 14 edges
9. `Pipeline lessons learned (lessons.md)` - 12 edges
10. `Pipeline orchestrator (acts for OPS Manager)` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Production Safety Rule` --conceptually_related_to--> `Stop for Megan's approval (approval-request.md)`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `Work on feature/<slug> branches, never main` --semantically_similar_to--> `Recommended GitHub branch protection on main`  [INFERRED] [semantically similar]
  CLAUDE.md → .pipeline/README.md
- `Graphify note: load skill and read map piece first (pinned 0.9.111)` --references--> `Knowledge maps in graphs/ (team, product, marketing, app)`  [INFERRED]
  .claude/agents/growth-reddit-specialist.md → CLAUDE.md
- `How OPS runs a task (plan-execute-verify loop, limits)` --conceptually_related_to--> `Loop limits: 2 re-plans, 3 build/QA rounds, 2 review fails`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `Core loop 1 spec (reference only since Oct 20; Replit wins)` --references--> `Pipeline Planner / Architect`  [INFERRED]
  .pipeline/spec.md → .claude/agents/pipeline-planner.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core loop 1 data layer (repos + migration + RLS)** — _pipeline_spec_scribe_repo, _pipeline_spec_world_repo, _pipeline_spec_prompt_repo, _pipeline_spec_core_loop_1_migration, _pipeline_spec_rls_policies [EXTRACTED 1.00]
- **Dev pipeline flow (Planner → Builder → QA → Reviewer → Megan approval)** — _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, claude_development_pipeline [EXTRACTED 1.00]
- **ISSUE11 dev pipeline: orchestrator, planner, builder, QA, reviewer, approval gate** — _claude_commands_pipeline_pipeline_orchestrator, _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, _claude_commands_pipeline_megan_approval_gate [EXTRACTED 1.00]
- **Copy voice rules** — _pipeline_lessons_brand_voice_lexicon, _pipeline_lessons_agents_never_invent_lines, _pipeline_lessons_anti_slop, _pipeline_lessons_no_becoming_her [INFERRED 0.85]
- **Dec 11 launch build path** — _pipeline_lessons_dec11_public_launch, _pipeline_lessons_boards_26_28, _pipeline_lessons_replit_final, _pipeline_lessons_signin_payments_spec, _pipeline_lessons_issue11_pricing [INFERRED 0.85]
- **Pinterest traffic engine** — _pipeline_lessons_pinterest_seo_agent, _pipeline_lessons_pin_templates, _pipeline_lessons_pin_posting_ramp, _pipeline_lessons_metricool, _pipeline_lessons_apify [INFERRED 0.85]
- **Growth agents that draft only and leave posting/spend to Megan** — _claude_agents_growth_media_buyer_media_buyer_agent, _claude_agents_growth_pinterest_seo_pinterest_seo_agent, _claude_agents_growth_reddit_specialist_reddit_specialist_agent, _claude_agents_customer_panel_customer_panel_agent [INFERRED 0.85]

## Communities (13 total, 3 thin omitted)

### Community 0 - "Third-party skills install & scan log"
Cohesion: 0.07
Nodes (37): Customer Panel (synthetic customer tester) (agent file), Customer Panel (synthetic customer tester), synthetic-crowd panel test (same seed, A vs B), GROWTH Media Buyer (agent file), Monday competitor ad watch (Meta Ad Library), GROWTH Media Buyer, GROWTH Pinterest SEO agent (agent file), Apify lergassy~pinterest-search-scraper research (+29 more)

### Community 1 - "Pipeline Planner / Architect"
Cohesion: 0.10
Nodes (27): Pipeline Builder (agent file), Pipeline Builder, Graphify note: load skill and read map piece first (pinned 0.9.111), Writes .pipeline/implementation-log.md (append rounds: files, decisions, checks, fixes), Pipeline Planner / Architect (agent file), Writes .pipeline/acceptance-criteria.md (numbered AC-n, PASS/FAIL testable), Graphify note: load skill and read map piece first (pinned 0.9.111), Spec section: Loop stage (DESIRE→IMAGINE→EMBODY→BECOME test) (+19 more)

### Community 2 - "Pipeline lessons learned (lessons.md)"
Cohesion: 0.09
Nodes (17): Apify (Pinterest scrapers), App Masters ASO framework, Applyra Unlimited (ASO tracker), GROWTH ASO & Opportunity Scout, ASOMobile, Glammi chrome cover theme, graphify knowledge maps (graphs/), App Store listing v15 (+9 more)

### Community 3 - "ISSUE11 repo rules (CLAUDE.md)"
Cohesion: 0.12
Nodes (15): Spec section: Sensitive areas touched, Review checks: missing reqs, bugs, security, unintended changes, complexity, test honesty, The Editor (art direction + mise en page) (agent file), MISE-EN-PAGE.md magazine rules (US Letter, Inter Tight), The Editor (art direction + mise en page), openclaudia email-subject-lines (FAIL: sources .env, sends via Resend), muapi-skills (NOT installed; sources .env), Replit MCP connector review (OK with limits; uses credits) (+7 more)

### Community 4 - "Spec: Core loop 1"
Cohesion: 0.13
Nodes (22): Writes .pipeline/spec.md (summary, files, architecture, DB, deps, edge cases, security), Acceptance criteria: Core loop 1 (AC-1..AC-68), Auth criteria AC-13..AC-24, Process criteria AC-67..AC-68 (feature branch, no live migration), Scribe criteria AC-25..AC-43, Database/security criteria AC-55..AC-63 (RLS isolation, no secrets), Your World criteria AC-44..AC-54, AI consent before sending personal data to AI (+14 more)

### Community 5 - "CURRENT FACTS box (read first)"
Cohesion: 0.09
Nodes (20): Design boards 26-28 (approved Dec 11 design), CURRENT FACTS box (read first), Dec 11 2026 public App Store launch, Download my issue (PDF), ISSUE11 Fictitious Business Name filing, Floating draggable 11 mark, Gift / occasion magazines idea, iPostal1 mailing address (+12 more)

### Community 6 - "New Way of Manifestation positioning"
Cohesion: 0.17
Nodes (10): Anti-slop checklist (.pipeline/ANTI-SLOP.md), Audience: Gen Z and millennial women, Brand Voice Guide + LEXICON.md, Educational carousels (CAR5 language), Copy direction: THE NEW WAY OF MANIFESTATION, Full-bleed hero video, ICP: tried manifestation, thinks it doesn't work, issue11.app landing page frozen (+2 more)

### Community 7 - "App Store readiness checklist"
Cohesion: 0.18
Nodes (11): Spec section: App Store compliance check, Core loop 1 acceptance criteria, App Store readiness checklist, 5.1.1(v) in-app account deletion, 3.1 Apple in-app purchase subscriptions (RevenueCat ok), Guideline 2.5.19: no hidden features behind remote flags, iPhone Duo foldable layouts, Core loop 1 request (Oct 6) (+3 more)

### Community 8 - "Framer (issue11.app + glammi.ai)"
Cohesion: 0.20
Nodes (5): Framer (issue11.app + glammi.ai), Glammi audience: aesthetic medicine, jewelers, beauty brands, Glammi blog up to 2 articles/day, Glammi services = AEO + websites, IndexNow pings

### Community 9 - "GROWTH Reddit Specialist"
Cohesion: 0.22
Nodes (7): GROWTH Reddit Specialist (agent file), Graphify note: load skill and read map piece first (pinned 0.9.111), Reddit loop: monitor → pick 5 → draft disclosed replies → report → track UTM, drafts/growth/reddit-playbook.md (keyword lists), GROWTH Reddit Specialist, Reddit UTM format (utm_source=reddit, organic, thread slug), Weekly report drafts/growth/reddit/<date>.md

## Knowledge Gaps
- **52 isolated node(s):** `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)`, `GROWTH Pinterest SEO agent (agent file)`, `The Editor (art direction + mise en page) (agent file)` (+47 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 78 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Third-party skills install & scan log` connect `Third-party skills install & scan log` to `ISSUE11 repo rules (CLAUDE.md)`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Pipeline Planner / Architect` (e.g. with `Pipeline Builder` and `Core loop 1 spec (reference only since Oct 20; Replit wins)`) actually correct?**
  _`Pipeline Planner / Architect` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)` to the rest of the system?**
  _52 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Third-party skills install & scan log` be split into smaller, more focused modules?**
  _Cohesion score 0.07051282051282051 - nodes in this community are weakly interconnected._
- **Why does `ISSUE11 repo rules (CLAUDE.md)` connect `ISSUE11 repo rules (CLAUDE.md)` to `Third-party skills install & scan log`, `Pipeline Planner / Architect`, `Spec: Core loop 1`, `App Store readiness checklist`?**
  _High betweenness centrality (0.111) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Production Safety Rule` (e.g. with `Builder commits on feature branch only; no push, deploy, merge or live migrations` and `Stop for Megan's approval (approval-request.md)`) actually correct?**
  _`Production Safety Rule` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Pipeline Planner / Architect` be split into smaller, more focused modules?**
  _Cohesion score 0.09915966386554621 - nodes in this community are weakly interconnected._