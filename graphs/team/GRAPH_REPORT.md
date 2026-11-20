# Graph Report - Autonomousangents  (2026-11-20)

## Corpus Check
- 20 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 191 nodes · 302 edges · 10 communities (9 shown, 1 thin omitted)
- Extraction: 74% EXTRACTED · 26% INFERRED · 0% AMBIGUOUS · INFERRED: 78 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Pipeline Planner / Architect
- Third-party skills install & scan log
- Spec: Core loop 1
- Glammi audience: med spas, derm, aesthet
- ISSUE11 repo rules (CLAUDE.md)
- App Store readiness checklist
- CURRENT FACTS box
- 2027 Life Glow Up Kit lead magnet
- GROWTH Reddit Specialist
- Anti-slop checklist doc

## God Nodes (most connected - your core abstractions)
1. `Third-party skills install & scan log` - 29 edges
2. `ISSUE11 repo rules (CLAUDE.md)` - 20 edges
3. `Pipeline Planner / Architect` - 18 edges
4. `Pipeline Reviewer / Gatekeeper` - 17 edges
5. `Production Safety Rule` - 16 edges
6. `Pipeline Builder` - 16 edges
7. `Pipeline QA / Tester` - 15 edges
8. `Spec: Core loop 1` - 14 edges
9. `Pipeline orchestrator (acts for OPS Manager)` - 11 edges
10. `Development pipeline (Planner→Builder→QA→Reviewer→Approval)` - 9 edges

## Surprising Connections (you probably didn't know these)
- `Work on feature/<slug> branches, never main` --semantically_similar_to--> `Recommended GitHub branch protection on main`  [INFERRED] [semantically similar]
  CLAUDE.md → .pipeline/README.md
- `Production Safety Rule` --conceptually_related_to--> `Stop for Megan's approval (approval-request.md)`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `How OPS runs a task (plan-execute-verify loop, limits)` --conceptually_related_to--> `Loop limits: 2 re-plans, 3 build/QA rounds, 2 review fails`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `Core loop 1 spec (reference only since Oct 20; Replit wins)` --references--> `Pipeline Planner / Architect`  [INFERRED]
  .pipeline/spec.md → .claude/agents/pipeline-planner.md
- `Pipeline QA / Tester` --references--> `Core loop 1 acceptance criteria`  [INFERRED]
  .claude/agents/pipeline-qa.md → .pipeline/acceptance-criteria.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core loop 1 data layer (repos + migration + RLS)** — _pipeline_spec_scribe_repo, _pipeline_spec_world_repo, _pipeline_spec_prompt_repo, _pipeline_spec_core_loop_1_migration, _pipeline_spec_rls_policies [EXTRACTED 1.00]
- **Dev pipeline flow (Planner → Builder → QA → Reviewer → Megan approval)** — _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, claude_development_pipeline [EXTRACTED 1.00]
- **ISSUE11 dev pipeline: orchestrator, planner, builder, QA, reviewer, approval gate** — _claude_commands_pipeline_pipeline_orchestrator, _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, _claude_commands_pipeline_megan_approval_gate [EXTRACTED 1.00]
- **Lead magnet flow (kit, gate, email)** — _pipeline_lessons_life_glow_up_kit, _pipeline_lessons_email_gated_magnets, _pipeline_lessons_resend_newsletter, _pipeline_lessons_the_editor_agent [INFERRED 0.75]
- **Copy quality guardrails (lexicon, anti-slop, no invented lines)** — _pipeline_lessons_brand_voice_lexicon, _pipeline_lessons_anti_slop_checklist, _pipeline_lessons_agents_never_invent_lines, _pipeline_lessons_no_becoming_her [INFERRED 0.85]
- **Growth agents that draft only and leave posting/spend to Megan** — _claude_agents_growth_media_buyer_media_buyer_agent, _claude_agents_growth_pinterest_seo_pinterest_seo_agent, _claude_agents_growth_reddit_specialist_reddit_specialist_agent, _claude_agents_customer_panel_customer_panel_agent [INFERRED 0.85]
- **Pinterest pin production system** — _pipeline_lessons_pinterest_favourite_formats, _pipeline_lessons_pinterest_posting_ramp, _pipeline_lessons_pinterest_kw_pin_strategy, _pipeline_lessons_metricool_scheduling [INFERRED 0.85]

## Communities (10 total, 1 thin omitted)

### Community 0 - "Pipeline Planner / Architect"
Cohesion: 0.09
Nodes (29): Graphify note: load skill and read map piece first (pinned 0.9.111), Pipeline Builder (agent file), Pipeline Builder, Graphify note: load skill and read map piece first (pinned 0.9.111), Writes .pipeline/implementation-log.md (append rounds: files, decisions, checks, fixes), Pipeline Planner / Architect (agent file), Writes .pipeline/acceptance-criteria.md (numbered AC-n, PASS/FAIL testable), Graphify note: load skill and read map piece first (pinned 0.9.111) (+21 more)

### Community 1 - "Third-party skills install & scan log"
Cohesion: 0.07
Nodes (36): Customer Panel (synthetic customer tester) (agent file), Customer Panel (synthetic customer tester), synthetic-crowd panel test (same seed, A vs B), GROWTH Media Buyer (agent file), Monday competitor ad watch (Meta Ad Library), GROWTH Media Buyer, GROWTH Pinterest SEO agent (agent file), Apify lergassy~pinterest-search-scraper research (+28 more)

### Community 2 - "Spec: Core loop 1"
Cohesion: 0.13
Nodes (22): Writes .pipeline/spec.md (summary, files, architecture, DB, deps, edge cases, security), Acceptance criteria: Core loop 1 (AC-1..AC-68), Auth criteria AC-13..AC-24, Process criteria AC-67..AC-68 (feature branch, no live migration), Scribe criteria AC-25..AC-43, Database/security criteria AC-55..AC-63 (RLS isolation, no secrets), Your World criteria AC-44..AC-54, AI consent before sending personal data to AI (+14 more)

### Community 3 - "Glammi audience: med spas, derm, aesthet"
Cohesion: 0.10
Nodes (15): Content angle: How to use AI to manifest your dream life, Anti-slop checklist (.pipeline/ANTI-SLOP.md), Lexicon + Brand Voice Guide for all copy, Carousel 5 = design language template, Framer stale-publish fix: make a small real edit, Glammi audience: med spas, derm, aesthetic medicine, jewelers, luxury, creative and beauty e-commerce, Glammi chrome cover theme, Landing hero full-bleed video (+7 more)

### Community 4 - "ISSUE11 repo rules (CLAUDE.md)"
Cohesion: 0.18
Nodes (12): The Editor (art direction + mise en page) (agent file), MISE-EN-PAGE.md magazine rules (US Letter, Inter Tight), The Editor (art direction + mise en page), /decision-brief command, Decision brief format (recommendation, numbers, reasoning, 2 options, risks), Anthropic cookbook Chief of Staff (tutorial; pattern adopted), ISSUE11 repo rules (CLAUDE.md), Do smart things rules (+4 more)

### Community 5 - "App Store readiness checklist"
Cohesion: 0.14
Nodes (14): Spec section: App Store compliance check, Spec section: Sensitive areas touched, Review checks: missing reqs, bugs, security, unintended changes, complexity, test honesty, Core loop 1 acceptance criteria, App Store readiness checklist, 5.1.1(v) in-app account deletion, 3.1 Apple in-app purchase subscriptions (RevenueCat ok), Guideline 2.5.19: no hidden features behind remote flags (+6 more)

### Community 6 - "CURRENT FACTS box"
Cohesion: 0.22
Nodes (8): ASO tooling: Applyra connector + ASOMobile accuracy check, CURRENT FACTS box, Dec 11, 2026 = private beta (not App Store launch), Graphify knowledge maps in graphs/, ISSUE11 prices: $9.99 monthly, $69.99 yearly, $39.99 founding year, North-star goal: 660 paying subscribers per month, ISSUE11 publishes 1 article per day, Pipeline lessons learned (lessons.md)

### Community 7 - "2027 Life Glow Up Kit lead magnet"
Cohesion: 0.20
Nodes (8): The Editor (renamed from Lucky Star), Floating draggable 11 mark never hidden, 2027 Life Glow Up Kit lead magnet, Issue = 40 pages to print, quarterly rhythm, marketing-psychology skill for freebie work, One freebie, many keyword pins strategy, Newsletter moved from beehiiv to Resend, The Editor agent for magazine layouts

### Community 8 - "GROWTH Reddit Specialist"
Cohesion: 0.25
Nodes (6): GROWTH Reddit Specialist (agent file), Reddit loop: monitor → pick 5 → draft disclosed replies → report → track UTM, drafts/growth/reddit-playbook.md (keyword lists), GROWTH Reddit Specialist, Reddit UTM format (utm_source=reddit, organic, thread slug), Weekly report drafts/growth/reddit/<date>.md

## Knowledge Gaps
- **42 isolated node(s):** `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)`, `GROWTH Pinterest SEO agent (agent file)`, `The Editor (art direction + mise en page) (agent file)` (+37 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 61 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Third-party skills install & scan log` connect `Third-party skills install & scan log` to `Pipeline Planner / Architect`, `ISSUE11 repo rules (CLAUDE.md)`?**
  _High betweenness centrality (0.185) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Pipeline Planner / Architect` (e.g. with `Pipeline Builder` and `Core loop 1 spec (reference only since Oct 20; Replit wins)`) actually correct?**
  _`Pipeline Planner / Architect` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)` to the rest of the system?**
  _42 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Pipeline Planner / Architect` be split into smaller, more focused modules?**
  _Cohesion score 0.08902439024390243 - nodes in this community are weakly interconnected._
- **Why does `ISSUE11 repo rules (CLAUDE.md)` connect `ISSUE11 repo rules (CLAUDE.md)` to `Pipeline Planner / Architect`, `Third-party skills install & scan log`, `Spec: Core loop 1`, `App Store readiness checklist`?**
  _High betweenness centrality (0.154) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Production Safety Rule` (e.g. with `Builder commits on feature branch only; no push, deploy, merge or live migrations` and `Stop for Megan's approval (approval-request.md)`) actually correct?**
  _`Production Safety Rule` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `Third-party skills install & scan log` be split into smaller, more focused modules?**
  _Cohesion score 0.07051282051282051 - nodes in this community are weakly interconnected._