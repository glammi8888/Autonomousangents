# Graph Report - Autonomousangents  (2026-11-25)

## Corpus Check
- 20 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 171 nodes · 268 edges · 10 communities (9 shown, 1 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 49 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Pipeline Lessons Learned Log
- Pipeline Reviewer / Gatekeeper
- Pipeline Planner / Architect
- Spec: Core loop 1
- Installed Skills and Connectors Registry
- ISSUE11 repo rules (CLAUDE.md)
- GROWTH Reddit Specialist
- GROWTH Pinterest SEO agent
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
10. `Pipeline Lessons Learned Log` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Work on feature/<slug> branches, never main` --semantically_similar_to--> `Recommended GitHub branch protection on main`  [INFERRED] [semantically similar]
  CLAUDE.md → .pipeline/README.md
- `Production Safety Rule` --conceptually_related_to--> `Stop for Megan's approval (approval-request.md)`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `How OPS runs a task (plan-execute-verify loop, limits)` --conceptually_related_to--> `Loop limits: 2 re-plans, 3 build/QA rounds, 2 review fails`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `Writes .pipeline/spec.md (summary, files, architecture, DB, deps, edge cases, security)` --references--> `Spec: Core loop 1`  [INFERRED]
  .claude/agents/pipeline-planner.md → .pipeline/spec.md
- `Pipeline QA / Tester` --references--> `Core loop 1 acceptance criteria`  [INFERRED]
  .claude/agents/pipeline-qa.md → .pipeline/acceptance-criteria.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core loop 1 data layer (repos + migration + RLS)** — _pipeline_spec_scribe_repo, _pipeline_spec_world_repo, _pipeline_spec_prompt_repo, _pipeline_spec_core_loop_1_migration, _pipeline_spec_rls_policies [EXTRACTED 1.00]
- **Dev pipeline flow (Planner → Builder → QA → Reviewer → Megan approval)** — _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, claude_development_pipeline [EXTRACTED 1.00]
- **ISSUE11 dev pipeline: orchestrator, planner, builder, QA, reviewer, approval gate** — _claude_commands_pipeline_pipeline_orchestrator, _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, _claude_commands_pipeline_megan_approval_gate [EXTRACTED 1.00]
- **Growth agents that draft only and leave posting/spend to Megan** — _claude_agents_growth_media_buyer_media_buyer_agent, _claude_agents_growth_pinterest_seo_pinterest_seo_agent, _claude_agents_growth_reddit_specialist_reddit_specialist_agent, _claude_agents_customer_panel_customer_panel_agent [INFERRED 0.85]
- **Skill scan-before-install flow** — claude_vendor_installed_skills_safety_rule_7_scan, claude_vendor_installed_skills_registry, claude_vendor_installed_skills_issue11_overrides_block, claude_vendor_installed_skills_not_installed [INFERRED 0.85]
- **ISSUE11 content quality rules** — pipeline_lessons_brand_voice_rules, pipeline_lessons_anti_slop_rule, pipeline_lessons_visual_qa_rule, pipeline_lessons_pinterest_hook_rule, pipeline_lessons_unique_cover_images [INFERRED 0.85]
- **Dec 11 launch workstreams** — pipeline_lessons_dec11_launch_date, pipeline_lessons_replit_build, pipeline_lessons_signin_payments_spec, pipeline_lessons_aso_program, pipeline_lessons_design_boards_26_28 [INFERRED 0.85]

## Communities (10 total, 1 thin omitted)

### Community 0 - "Pipeline Lessons Learned Log"
Cohesion: 0.08
Nodes (23): ASO connectors (Applyra, ASOMobile, Astro, Sonar ASO), graphify skill (pinned 0.9.111, GRAPHIFY_BACKEND=none), Hosted connectors reviewed (Replit, beehiiv, Resend, Metricool, Meta Ads, ScreensDesign), ASO program (listing v15, Applyra + ASOMobile, App Masters framework), Brand voice rules (lexicon, no 'becoming her', anti-slop, agents never invent quotes), CURRENT FACTS box (Dec 11 public App Store launch, prices, tools), Dec 11, 2026 public App Store launch (changed from private beta Nov 20), Design boards 26-28 approved as Dec 11 design (+15 more)

### Community 1 - "Pipeline Reviewer / Gatekeeper"
Cohesion: 0.12
Nodes (20): Pipeline Builder (agent file), Pipeline Builder, Writes .pipeline/implementation-log.md (append rounds: files, decisions, checks, fixes), Writes .pipeline/acceptance-criteria.md (numbered AC-n, PASS/FAIL testable), Pipeline QA / Tester (agent file), Test each AC happy path + failure cases (bad input, empty, network, unauthorized, duplicates), Pipeline QA / Tester, Writes .pipeline/test-results.md (AC table, QA-n failures, regressions, verdict) (+12 more)

### Community 2 - "Pipeline Planner / Architect"
Cohesion: 0.11
Nodes (19): Pipeline Planner / Architect (agent file), Spec section: App Store compliance check, Spec section: Loop stage (DESIRE→IMAGINE→EMBODY→BECOME test), Pipeline Planner / Architect, Spec section: Sensitive areas touched, Writes .pipeline/spec.md (summary, files, architecture, DB, deps, edge cases, security), Review checks: missing reqs, bugs, security, unintended changes, complexity, test honesty, Core loop 1 acceptance criteria (+11 more)

### Community 3 - "Spec: Core loop 1"
Cohesion: 0.15
Nodes (20): Acceptance criteria: Core loop 1 (AC-1..AC-68), Auth criteria AC-13..AC-24, Process criteria AC-67..AC-68 (feature branch, no live migration), Scribe criteria AC-25..AC-43, Database/security criteria AC-55..AC-63 (RLS isolation, no secrets), Your World criteria AC-44..AC-54, AI consent before sending personal data to AI, Spec: Core loop 1 (+12 more)

### Community 4 - "Installed Skills and Connectors Registry"
Cohesion: 0.10
Nodes (17): AEO/SEO packs (AEOTester, SEO-AEO-GEO Ultimate, SearchFit, aeo advisor), Apify actors security-checked (Pinterest trends, Instagram/TikTok hashtag scrapers), claude-ads (12 ad platforms, 33 sub-skills, 24 agents), Customer panel skills (synthetic-crowd, synthetic-user-feedback, persona), decision-brief command adopted from Anthropic Chief of Staff cookbook, ISSUE11 overrides block (drafts only, real proof, Megan's copy rules), coreyhaines31 marketingskills library (55 skills, installed unmodified plus overrides block), Scanned but not installed (muapi-skills, openclaudia email-subject-lines, newsletter-writer, synthetic-consumer-research, ECC chief-of-staff) (+9 more)

### Community 5 - "ISSUE11 repo rules (CLAUDE.md)"
Cohesion: 0.14
Nodes (13): GROWTH Media Buyer (agent file), Monday competitor ad watch (Meta Ad Library), GROWTH Media Buyer, The Editor (art direction + mise en page) (agent file), MISE-EN-PAGE.md magazine rules (US Letter, Inter Tight), The Editor (art direction + mise en page), /decision-brief command, Decision brief format (recommendation, numbers, reasoning, 2 options, risks) (+5 more)

### Community 6 - "GROWTH Reddit Specialist"
Cohesion: 0.14
Nodes (12): GROWTH Reddit Specialist (agent file), Graphify note: load skill and read map piece first (pinned 0.9.111), Reddit loop: monitor → pick 5 → draft disclosed replies → report → track UTM, drafts/growth/reddit-playbook.md (keyword lists), GROWTH Reddit Specialist, Reddit UTM format (utm_source=reddit, organic, thread slug), Weekly report drafts/growth/reddit/<date>.md, Graphify note: load skill and read map piece first (pinned 0.9.111) (+4 more)

### Community 7 - "GROWTH Pinterest SEO agent"
Cohesion: 0.40
Nodes (4): GROWTH Pinterest SEO agent (agent file), Apify lergassy~pinterest-search-scraper research, Per-pin SEO row (title, description, board, alt text, link), GROWTH Pinterest SEO agent

### Community 8 - "Customer Panel (synthetic customer teste"
Cohesion: 0.67
Nodes (3): Customer Panel (synthetic customer tester) (agent file), Customer Panel (synthetic customer tester), synthetic-crowd panel test (same seed, A vs B)

## Knowledge Gaps
- **39 isolated node(s):** `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)`, `GROWTH Pinterest SEO agent (agent file)`, `The Editor (art direction + mise en page) (agent file)` (+34 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 57 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `GROWTH Reddit Specialist` connect `GROWTH Reddit Specialist` to `Pipeline Lessons Learned Log`?**
  _High betweenness centrality (0.466) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Pipeline Planner / Architect` (e.g. with `Pipeline Builder` and `Core loop 1 spec (reference only since Oct 20; Replit wins)`) actually correct?**
  _`Pipeline Planner / Architect` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)` to the rest of the system?**
  _39 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Pipeline Lessons Learned Log` be split into smaller, more focused modules?**
  _Cohesion score 0.07741935483870968 - nodes in this community are weakly interconnected._
- **Why does `Knowledge maps in graphs/ (team, product, marketing, app)` connect `GROWTH Reddit Specialist` to `ISSUE11 repo rules (CLAUDE.md)`?**
  _High betweenness centrality (0.452) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Pipeline Builder` (e.g. with `Writes .pipeline/spec.md (summary, files, architecture, DB, deps, edge cases, security)` and `Pipeline QA / Tester`) actually correct?**
  _`Pipeline Builder` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `Pipeline Reviewer / Gatekeeper` be split into smaller, more focused modules?**
  _Cohesion score 0.12413793103448276 - nodes in this community are weakly interconnected._