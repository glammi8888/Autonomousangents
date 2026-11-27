# Graph Report - Autonomousangents  (2026-11-27)

## Corpus Check
- 20 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 178 nodes · 278 edges · 11 communities (10 shown, 1 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 48 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Pipeline Reviewer / Gatekeeper
- Spec: Core loop 1
- Pipeline lessons learned (lessons.md)
- Pinterest pin pipeline via Metricool and
- Pipeline Planner / Architect
- The Editor (art direction + mise en page
- GROWTH Reddit Specialist
- ISSUE11 repo rules (CLAUDE.md)
- Installed Skills and Connectors Registry
- Customer Panel (synthetic customer teste
- Anti-slop checklist doc

## God Nodes (most connected - your core abstractions)
1. `ISSUE11 repo rules (CLAUDE.md)` - 20 edges
2. `Pipeline Planner / Architect` - 18 edges
3. `Pipeline Reviewer / Gatekeeper` - 17 edges
4. `Pipeline Builder` - 16 edges
5. `Production Safety Rule` - 15 edges
6. `Pipeline QA / Tester` - 15 edges
7. `Spec: Core loop 1` - 14 edges
8. `Installed Skills and Connectors Registry` - 12 edges
9. `Pipeline orchestrator (acts for OPS Manager)` - 11 edges
10. `Pipeline lessons learned (lessons.md)` - 10 edges

## Surprising Connections (you probably didn't know these)
- `Production Safety Rule` --conceptually_related_to--> `Stop for Megan's approval (approval-request.md)`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `Work on feature/<slug> branches, never main` --semantically_similar_to--> `Recommended GitHub branch protection on main`  [INFERRED] [semantically similar]
  CLAUDE.md → .pipeline/README.md
- `How OPS runs a task (plan-execute-verify loop, limits)` --conceptually_related_to--> `Loop limits: 2 re-plans, 3 build/QA rounds, 2 review fails`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `Pipeline QA / Tester` --references--> `Core loop 1 acceptance criteria`  [INFERRED]
  .claude/agents/pipeline-qa.md → .pipeline/acceptance-criteria.md
- `Process criteria AC-67..AC-68 (feature branch, no live migration)` --references--> `Production Safety Rule`  [EXTRACTED]
  .pipeline/acceptance-criteria.md → CLAUDE.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core loop 1 data layer (repos + migration + RLS)** — _pipeline_spec_scribe_repo, _pipeline_spec_world_repo, _pipeline_spec_prompt_repo, _pipeline_spec_core_loop_1_migration, _pipeline_spec_rls_policies [EXTRACTED 1.00]
- **Dev pipeline flow (Planner → Builder → QA → Reviewer → Megan approval)** — _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, claude_development_pipeline [EXTRACTED 1.00]
- **ISSUE11 dev pipeline: orchestrator, planner, builder, QA, reviewer, approval gate** — _claude_commands_pipeline_pipeline_orchestrator, _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, _claude_commands_pipeline_megan_approval_gate [EXTRACTED 1.00]
- **Growth agents that draft only and leave posting/spend to Megan** — _claude_agents_growth_media_buyer_media_buyer_agent, _claude_agents_growth_pinterest_seo_pinterest_seo_agent, _claude_agents_growth_reddit_specialist_reddit_specialist_agent, _claude_agents_customer_panel_customer_panel_agent [INFERRED 0.85]
- **Skill scan-before-install flow** — claude_vendor_installed_skills_safety_rule_7_scan, claude_vendor_installed_skills_registry, claude_vendor_installed_skills_issue11_overrides_block, claude_vendor_installed_skills_not_installed [INFERRED 0.85]
- **Megan standing operating rules** — _pipeline_lessons_do_it_yourself_rule, _pipeline_lessons_check_lessons_first, _pipeline_lessons_logic_first, _pipeline_lessons_production_safety [INFERRED 0.85]
- **v1 no-account architecture** — _pipeline_lessons_no_signin_v1, _pipeline_lessons_supabase_content, _pipeline_lessons_replit_final_app, _pipeline_lessons_prices [INFERRED 0.85]
- **Pin and carousel content rule set** — _pipeline_lessons_pin_hook_rules, _pipeline_lessons_no_invented_lines, _pipeline_lessons_lexicon_voice, _pipeline_lessons_visual_qa [INFERRED 0.85]

## Communities (11 total, 1 thin omitted)

### Community 0 - "Pipeline Reviewer / Gatekeeper"
Cohesion: 0.13
Nodes (19): Pipeline Builder (agent file), Pipeline Builder, Writes .pipeline/implementation-log.md (append rounds: files, decisions, checks, fixes), Writes .pipeline/acceptance-criteria.md (numbered AC-n, PASS/FAIL testable), Pipeline QA / Tester (agent file), Test each AC happy path + failure cases (bad input, empty, network, unauthorized, duplicates), Pipeline QA / Tester, Writes .pipeline/test-results.md (AC table, QA-n failures, regressions, verdict) (+11 more)

### Community 1 - "Spec: Core loop 1"
Cohesion: 0.13
Nodes (22): Writes .pipeline/spec.md (summary, files, architecture, DB, deps, edge cases, security), Acceptance criteria: Core loop 1 (AC-1..AC-68), Auth criteria AC-13..AC-24, Process criteria AC-67..AC-68 (feature branch, no live migration), Scribe criteria AC-25..AC-43, Database/security criteria AC-55..AC-63 (RLS isolation, no secrets), Your World criteria AC-44..AC-54, AI consent before sending personal data to AI (+14 more)

### Community 2 - "Pipeline lessons learned (lessons.md)"
Cohesion: 0.12
Nodes (23): Daily AEO blog publishing (ISSUE11 1/day, Glammi up to 2/day), Apple developer account in Megan's own name, ASO workflow: Applyra Unlimited plus ASOMobile, ASO decision: add free to keyword field at Dec 1 recheck, Approved logic board 26 and screens boards 27-28, Floating draggable 11 (the Editor), Fix for Framer page stale after publish, Framer MCP and server API workflow (+15 more)

### Community 3 - "Pinterest pin pipeline via Metricool and"
Cohesion: 0.11
Nodes (23): Brand direction: calm, white space, Inter Tight, no gradients, pink as small accent, Carousel 5 design language, Rule: check lessons and live source before claiming or asking, Unique cover image rule and cover-dupe-check, Rule: do everything possible yourself, only hand Megan blocked items, Graphify knowledge maps split into 4 pieces, ICP: experienced but disillusioned manifestor, Gen Z and millennial women, 2027 Life Glow Up Kit lead magnet (email-gated) (+15 more)

### Community 4 - "Pipeline Planner / Architect"
Cohesion: 0.13
Nodes (17): Pipeline Planner / Architect (agent file), Spec section: App Store compliance check, Spec section: Loop stage (DESIRE→IMAGINE→EMBODY→BECOME test), Pipeline Planner / Architect, Spec section: Sensitive areas touched, Review checks: missing reqs, bugs, security, unintended changes, complexity, test honesty, Core loop 1 acceptance criteria, App Store readiness checklist (+9 more)

### Community 5 - "The Editor (art direction + mise en page"
Cohesion: 0.13
Nodes (12): GROWTH Media Buyer (agent file), Monday competitor ad watch (Meta Ad Library), GROWTH Media Buyer, GROWTH Pinterest SEO agent (agent file), Apify lergassy~pinterest-search-scraper research, Per-pin SEO row (title, description, board, alt text, link), GROWTH Pinterest SEO agent, The Editor (art direction + mise en page) (agent file) (+4 more)

### Community 6 - "GROWTH Reddit Specialist"
Cohesion: 0.14
Nodes (12): GROWTH Reddit Specialist (agent file), Graphify note: load skill and read map piece first (pinned 0.9.111), Reddit loop: monitor → pick 5 → draft disclosed replies → report → track UTM, drafts/growth/reddit-playbook.md (keyword lists), GROWTH Reddit Specialist, Reddit UTM format (utm_source=reddit, organic, thread slug), Weekly report drafts/growth/reddit/<date>.md, Graphify note: load skill and read map piece first (pinned 0.9.111) (+4 more)

### Community 7 - "ISSUE11 repo rules (CLAUDE.md)"
Cohesion: 0.24
Nodes (6): Recommended GitHub branch protection on main, ISSUE11 repo rules (CLAUDE.md), Do smart things rules, Knowledge & Training Inbox (Notion), Notion Done Log (single task tracker), How OPS runs a task (plan-execute-verify loop, limits)

### Community 8 - "Installed Skills and Connectors Registry"
Cohesion: 0.15
Nodes (13): AEO/SEO packs (AEOTester, SEO-AEO-GEO Ultimate, SearchFit, aeo advisor), Apify actors security-checked (Pinterest trends, Instagram/TikTok hashtag scrapers), ASO connectors (Applyra, ASOMobile, Astro, Sonar ASO), claude-ads (12 ad platforms, 33 sub-skills, 24 agents), Customer panel skills (synthetic-crowd, synthetic-user-feedback, persona), decision-brief command adopted from Anthropic Chief of Staff cookbook, graphify skill (pinned 0.9.111, GRAPHIFY_BACKEND=none), Hosted connectors reviewed (Replit, beehiiv, Resend, Metricool, Meta Ads, ScreensDesign) (+5 more)

### Community 9 - "Customer Panel (synthetic customer teste"
Cohesion: 0.67
Nodes (3): Customer Panel (synthetic customer tester) (agent file), Customer Panel (synthetic customer tester), synthetic-crowd panel test (same seed, A vs B)

## Knowledge Gaps
- **48 isolated node(s):** `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)`, `GROWTH Pinterest SEO agent (agent file)`, `The Editor (art direction + mise en page) (agent file)` (+43 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 61 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ISSUE11 repo rules (CLAUDE.md)` connect `ISSUE11 repo rules (CLAUDE.md)` to `Pipeline Reviewer / Gatekeeper`, `Spec: Core loop 1`, `Pipeline Planner / Architect`, `The Editor (art direction + mise en page`, `GROWTH Reddit Specialist`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Pipeline Planner / Architect` (e.g. with `Pipeline Builder` and `Core loop 1 spec (reference only since Oct 20; Replit wins)`) actually correct?**
  _`Pipeline Planner / Architect` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)` to the rest of the system?**
  _48 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Pipeline Reviewer / Gatekeeper` be split into smaller, more focused modules?**
  _Cohesion score 0.12923076923076923 - nodes in this community are weakly interconnected._
- **Why does `Pipeline Planner / Architect` connect `Pipeline Planner / Architect` to `Pipeline Reviewer / Gatekeeper`, `Spec: Core loop 1`, `GROWTH Reddit Specialist`, `ISSUE11 repo rules (CLAUDE.md)`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Pipeline Builder` (e.g. with `Writes .pipeline/spec.md (summary, files, architecture, DB, deps, edge cases, security)` and `Pipeline QA / Tester`) actually correct?**
  _`Pipeline Builder` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `Spec: Core loop 1` be split into smaller, more focused modules?**
  _Cohesion score 0.13405797101449277 - nodes in this community are weakly interconnected._