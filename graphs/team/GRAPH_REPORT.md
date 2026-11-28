# Graph Report - Autonomousangents  (2026-11-28)

## Corpus Check
- 20 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 182 nodes · 270 edges · 16 communities (12 shown, 4 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 51 edges (avg confidence: 0.88)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Pipeline Reviewer / Gatekeeper
- Pipeline lessons learned (lessons.md)
- Spec: Core loop 1
- Pipeline Planner / Architect
- ISSUE11 repo rules (CLAUDE.md)
- GROWTH Reddit Specialist
- Installed Skills and Connectors Registry
- Rule: never name our tools or vendors in
- Glammi audience verticals (med spa, derm
- GROWTH Pinterest SEO agent
- 2027 Life Glow Up Kit, email-gated lead 
- OPS manager rules: delegate, keep Megan 
- Customer Panel (synthetic customer teste
- Anti-slop checklist doc
- Banned phrases: becoming her, move (use 
- Rule: floating 11 never hidden or moved

## God Nodes (most connected - your core abstractions)
1. `ISSUE11 repo rules (CLAUDE.md)` - 21 edges
2. `Pipeline Planner / Architect` - 18 edges
3. `Pipeline Reviewer / Gatekeeper` - 17 edges
4. `Pipeline Builder` - 16 edges
5. `Production Safety Rule` - 15 edges
6. `Pipeline QA / Tester` - 15 edges
7. `Spec: Core loop 1` - 14 edges
8. `Installed Skills and Connectors Registry` - 12 edges
9. `Pipeline lessons learned (lessons.md)` - 12 edges
10. `Pipeline orchestrator (acts for OPS Manager)` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Work on feature/<slug> branches, never main` --semantically_similar_to--> `Recommended GitHub branch protection on main`  [INFERRED] [semantically similar]
  CLAUDE.md → .pipeline/README.md
- `Production Safety Rule` --conceptually_related_to--> `Stop for Megan's approval (approval-request.md)`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `How OPS runs a task (plan-execute-verify loop, limits)` --conceptually_related_to--> `Loop limits: 2 re-plans, 3 build/QA rounds, 2 review fails`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `Pipeline QA / Tester` --references--> `Core loop 1 acceptance criteria`  [INFERRED]
  .claude/agents/pipeline-qa.md → .pipeline/acceptance-criteria.md
- `Process criteria AC-67..AC-68 (feature branch, no live migration)` --references--> `Production Safety Rule`  [EXTRACTED]
  .pipeline/acceptance-criteria.md → CLAUDE.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **App v1 launch stack decisions** — _pipeline_lessons_launch_dec11, _pipeline_lessons_pricing_model, _pipeline_lessons_decision_no_signin, _pipeline_lessons_supabase_content, _pipeline_lessons_replit_workflow, _pipeline_lessons_onboarding_locked [EXTRACTED 1.00]
- **Core loop 1 data layer (repos + migration + RLS)** — _pipeline_spec_scribe_repo, _pipeline_spec_world_repo, _pipeline_spec_prompt_repo, _pipeline_spec_core_loop_1_migration, _pipeline_spec_rls_policies [EXTRACTED 1.00]
- **Dev pipeline flow (Planner → Builder → QA → Reviewer → Megan approval)** — _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, claude_development_pipeline [EXTRACTED 1.00]
- **ISSUE11 dev pipeline: orchestrator, planner, builder, QA, reviewer, approval gate** — _claude_commands_pipeline_pipeline_orchestrator, _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, _claude_commands_pipeline_megan_approval_gate [EXTRACTED 1.00]
- **Rules every pin and carousel copy line must satisfy** — _pipeline_lessons_rule_brand_voice_lexicon, _pipeline_lessons_rule_no_ai_sounding_copy, _pipeline_lessons_banned_words, _pipeline_lessons_pin_hook_patterns, _pipeline_lessons_carousel_rules, _pipeline_lessons_positioning_new_way [EXTRACTED 1.00]
- **Growth agents that draft only and leave posting/spend to Megan** — _claude_agents_growth_media_buyer_media_buyer_agent, _claude_agents_growth_pinterest_seo_pinterest_seo_agent, _claude_agents_growth_reddit_specialist_reddit_specialist_agent, _claude_agents_customer_panel_customer_panel_agent [INFERRED 0.85]
- **Skill scan-before-install flow** — claude_vendor_installed_skills_safety_rule_7_scan, claude_vendor_installed_skills_registry, claude_vendor_installed_skills_issue11_overrides_block, claude_vendor_installed_skills_not_installed [INFERRED 0.85]
- **Organic traffic engines toward 100k visits** — _pipeline_lessons_goal_100k_traffic, _pipeline_lessons_pinterest_formats, _pipeline_lessons_aeo_blog_cadence, _pipeline_lessons_lead_magnet_kit, _pipeline_lessons_image_uniqueness [INFERRED 0.85]

## Communities (16 total, 4 thin omitted)

### Community 0 - "Pipeline Reviewer / Gatekeeper"
Cohesion: 0.11
Nodes (20): Pipeline Builder (agent file), Pipeline Builder, Writes .pipeline/implementation-log.md (append rounds: files, decisions, checks, fixes), Writes .pipeline/acceptance-criteria.md (numbered AC-n, PASS/FAIL testable), Pipeline QA / Tester (agent file), Test each AC happy path + failure cases (bad input, empty, network, unauthorized, duplicates), Pipeline QA / Tester, Writes .pipeline/test-results.md (AC table, QA-n failures, regressions, verdict) (+12 more)

### Community 1 - "Pipeline lessons learned (lessons.md)"
Cohesion: 0.10
Nodes (25): Pipeline lessons learned (lessons.md), Blog cadence: ISSUE11 1 per day, Glammi up to 2, Apify actors for research, ASO strategy: Applyra plus ASOMobile merged, listing v15, free keyword Dec 1, Decision: v1 has no sign-in or accounts, Framer publish and variant quirks, Goal: 100k monthly visitors to issue11.app, North-star: 660 paying subscribers/month (+17 more)

### Community 2 - "Spec: Core loop 1"
Cohesion: 0.13
Nodes (22): Writes .pipeline/spec.md (summary, files, architecture, DB, deps, edge cases, security), Acceptance criteria: Core loop 1 (AC-1..AC-68), Auth criteria AC-13..AC-24, Process criteria AC-67..AC-68 (feature branch, no live migration), Scribe criteria AC-25..AC-43, Database/security criteria AC-55..AC-63 (RLS isolation, no secrets), Your World criteria AC-44..AC-54, AI consent before sending personal data to AI (+14 more)

### Community 3 - "Pipeline Planner / Architect"
Cohesion: 0.13
Nodes (17): Pipeline Planner / Architect (agent file), Spec section: App Store compliance check, Spec section: Loop stage (DESIRE→IMAGINE→EMBODY→BECOME test), Pipeline Planner / Architect, Spec section: Sensitive areas touched, Review checks: missing reqs, bugs, security, unintended changes, complexity, test honesty, Core loop 1 acceptance criteria, App Store readiness checklist (+9 more)

### Community 4 - "ISSUE11 repo rules (CLAUDE.md)"
Cohesion: 0.16
Nodes (13): GROWTH Media Buyer (agent file), Monday competitor ad watch (Meta Ad Library), GROWTH Media Buyer, The Editor (art direction + mise en page) (agent file), MISE-EN-PAGE.md magazine rules (US Letter, Inter Tight), The Editor (art direction + mise en page), /decision-brief command, Decision brief format (recommendation, numbers, reasoning, 2 options, risks) (+5 more)

### Community 5 - "GROWTH Reddit Specialist"
Cohesion: 0.14
Nodes (12): GROWTH Reddit Specialist (agent file), Graphify note: load skill and read map piece first (pinned 0.9.111), Reddit loop: monitor → pick 5 → draft disclosed replies → report → track UTM, drafts/growth/reddit-playbook.md (keyword lists), GROWTH Reddit Specialist, Reddit UTM format (utm_source=reddit, organic, thread slug), Weekly report drafts/growth/reddit/<date>.md, Graphify note: load skill and read map piece first (pinned 0.9.111) (+4 more)

### Community 6 - "Installed Skills and Connectors Registry"
Cohesion: 0.15
Nodes (13): AEO/SEO packs (AEOTester, SEO-AEO-GEO Ultimate, SearchFit, aeo advisor), Apify actors security-checked (Pinterest trends, Instagram/TikTok hashtag scrapers), ASO connectors (Applyra, ASOMobile, Astro, Sonar ASO), claude-ads (12 ad platforms, 33 sub-skills, 24 agents), Customer panel skills (synthetic-crowd, synthetic-user-feedback, persona), decision-brief command adopted from Anthropic Chief of Staff cookbook, graphify skill (pinned 0.9.111, GRAPHIFY_BACKEND=none), Hosted connectors reviewed (Replit, beehiiv, Resend, Metricool, Meta Ads, ScreensDesign) (+5 more)

### Community 7 - "Rule: never name our tools or vendors in"
Cohesion: 0.33
Nodes (5): Carousel rules: 5 slides preferred, educational, CTA last slide, CAR5 style, Rule: never name our tools or vendors in public content, Rule: privacy and consent say AI provider, never name services, Pin hook patterns: skeptic callout, comparison, polarizing pattern interrupt, Rule: copy uses Brand Voice Guide and LEXICON word for word

### Community 8 - "Glammi audience verticals (med spa, derm"
Cohesion: 0.33
Nodes (6): Glammi cold outreach paused, Glammi chrome cover theme, Rule: new Glammi industry page max 1 per week, unique content, Glammi audience verticals (med spa, derm, jewelers, creative, beauty ecommerce), Niche correction: ISSUE11 is manifestation, not beauty, Queen of AEO experiment

### Community 9 - "GROWTH Pinterest SEO agent"
Cohesion: 0.40
Nodes (4): GROWTH Pinterest SEO agent (agent file), Apify lergassy~pinterest-search-scraper research, Per-pin SEO row (title, description, board, alt text, link), GROWTH Pinterest SEO agent

### Community 10 - "2027 Life Glow Up Kit, email-gated lead "
Cohesion: 0.40
Nodes (5): FBN filed and iPostal address handling, 2027 Life Glow Up Kit, email-gated lead magnet, Resend as newsletter tool, The Editor agent and MISE-EN-PAGE, US Letter print, Visual QA rule (design/VISUAL-QA.md)

### Community 12 - "Customer Panel (synthetic customer teste"
Cohesion: 0.67
Nodes (3): Customer Panel (synthetic customer tester) (agent file), Customer Panel (synthetic customer tester), synthetic-crowd panel test (same seed, A vs B)

## Knowledge Gaps
- **59 isolated node(s):** `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)`, `GROWTH Pinterest SEO agent (agent file)`, `The Editor (art direction + mise en page) (agent file)` (+54 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 76 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ISSUE11 repo rules (CLAUDE.md)` connect `ISSUE11 repo rules (CLAUDE.md)` to `Pipeline Reviewer / Gatekeeper`, `Pipeline lessons learned (lessons.md)`, `Spec: Core loop 1`, `Pipeline Planner / Architect`, `GROWTH Reddit Specialist`?**
  _High betweenness centrality (0.307) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Pipeline Planner / Architect` (e.g. with `Pipeline Builder` and `Core loop 1 spec (reference only since Oct 20; Replit wins)`) actually correct?**
  _`Pipeline Planner / Architect` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)` to the rest of the system?**
  _59 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Pipeline Reviewer / Gatekeeper` be split into smaller, more focused modules?**
  _Cohesion score 0.11290322580645161 - nodes in this community are weakly interconnected._
- **Why does `Pipeline lessons learned (lessons.md)` connect `Pipeline lessons learned (lessons.md)` to `Pipeline Reviewer / Gatekeeper`, `ISSUE11 repo rules (CLAUDE.md)`?**
  _High betweenness centrality (0.233) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Pipeline Builder` (e.g. with `Writes .pipeline/spec.md (summary, files, architecture, DB, deps, edge cases, security)` and `Pipeline QA / Tester`) actually correct?**
  _`Pipeline Builder` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Should `Pipeline lessons learned (lessons.md)` be split into smaller, more focused modules?**
  _Cohesion score 0.09686609686609686 - nodes in this community are weakly interconnected._