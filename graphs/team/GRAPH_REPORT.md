# Graph Report - Autonomousangents  (2026-11-18)

## Corpus Check
- 20 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 374 nodes · 709 edges · 34 communities (20 shown, 14 thin omitted)
- Extraction: 78% EXTRACTED · 21% INFERRED · 0% AMBIGUOUS · INFERRED: 152 edges (avg confidence: 0.84)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- ISSUE11 repo rules (CLAUDE.md)
- Third-party skills install & scan log
- Spec: Core loop 1
- CURRENT FACTS box (read first; OPS updat
- Pipeline lessons learned (lessons.md)
- Rule: graphify for every agent, split in
- BANK rule: agents never invent quote/car
- ASO tools: Astro ongoing + ASOMobile one
- The Editor (art direction + mise en page
- Logic map per tab (board 26) as source f
- Brand guide palette (Blush, Pink, Cream,
- Carousels: funny/delulu hook + education
- Daily article publish always allowed; re
- $300/mo Instagram ads test, launches Nov
- Locked loved pin template set (COLOR-TES
- Glammi audience: med spas, derm, cosmeti
- AI-generated images = editorial mood onl
- Framer: always pass draft:true on addIte
- Core positioning: manifestation done rig
- Public name: Megan Scott Manolova
- Self-improvement loop with an independen
- Routine frequency cut to ~30 runs/day (u
- Stale Framer page fix: make a real edit 
- Framer: duplicate an existing text prese
- Track only keywords with 100+ US searche
- "The New Way of Manifestation" positioni
- 17MedSpa article recipe (volume-led topi
- Glammi covers: chrome theme, Megan's vis
- Glammi worker schedule cut from every 2h
- Log every Megan decision in the repo doc
- Pin logo 92px tall at bottom on 1000x150

## God Nodes (most connected - your core abstractions)
1. `Pipeline lessons learned (lessons.md)` - 236 edges
2. `Third-party skills install & scan log` - 21 edges
3. `ISSUE11 repo rules (CLAUDE.md)` - 21 edges
4. `Production Safety Rule` - 18 edges
5. `CURRENT FACTS box (read first; OPS updates Fridays)` - 18 edges
6. `Pipeline Planner / Architect` - 18 edges
7. `Pipeline Reviewer / Gatekeeper` - 17 edges
8. `Pipeline Builder` - 16 edges
9. `Pipeline QA / Tester` - 15 edges
10. `Spec: Core loop 1` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Verify, don't trust: re-run checks independently; untestable = NOT VERIFIED` --semantically_similar_to--> `Verify by re-fetching, not by an agent's report`  [INFERRED] [semantically similar]
  .claude/agents/pipeline-qa.md → .pipeline/lessons.md
- `Locked loved pin template set (COLOR-TEST.md)` --conceptually_related_to--> `Pin rules (Notes pins, photo-led, logo, Inter Tight, 1000x1500)`  [INFERRED]
  .pipeline/lessons.md → .claude/agents/growth-pinterest-seo.md
- `Work on feature/<slug> branches, never main` --semantically_similar_to--> `Recommended GitHub branch protection on main`  [INFERRED] [semantically similar]
  CLAUDE.md → .pipeline/README.md
- `Production Safety Rule` --conceptually_related_to--> `Stop for Megan's approval (approval-request.md)`  [INFERRED]
  CLAUDE.md → .claude/commands/pipeline.md
- `Customer Panel (synthetic customer tester)` --references--> `ICP: people who tried manifestation and think it doesn't work (women ~30-38)`  [INFERRED]
  .claude/agents/customer-panel.md → .pipeline/lessons.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Core loop 1 data layer (repos + migration + RLS)** — _pipeline_spec_scribe_repo, _pipeline_spec_world_repo, _pipeline_spec_prompt_repo, _pipeline_spec_core_loop_1_migration, _pipeline_spec_rls_policies [EXTRACTED 1.00]
- **Dev pipeline flow (Planner → Builder → QA → Reviewer → Megan approval)** — _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, claude_development_pipeline [EXTRACTED 1.00]
- **ISSUE11 dev pipeline: orchestrator, planner, builder, QA, reviewer, approval gate** — _claude_commands_pipeline_pipeline_orchestrator, _claude_agents_pipeline_planner_planner_agent, _claude_agents_pipeline_builder_builder_agent, _claude_agents_pipeline_qa_qa_agent, _claude_agents_pipeline_reviewer_reviewer_agent, _claude_commands_pipeline_megan_approval_gate [EXTRACTED 1.00]
- **Growth agents that draft only and leave posting/spend to Megan** — _claude_agents_growth_media_buyer_media_buyer_agent, _claude_agents_growth_pinterest_seo_pinterest_seo_agent, _claude_agents_growth_reddit_specialist_reddit_specialist_agent, _claude_agents_customer_panel_customer_panel_agent [INFERRED 0.85]
- **ISSUE11 copy authenticity rules (no invented lines, Lexicon, anti-slop, ask don't invent)** — _pipeline_lessons_bank_rule, _pipeline_lessons_lexicon_brand_voice, _pipeline_lessons_anti_slop_rule, _pipeline_lessons_dont_make_things_up, _pipeline_lessons_first_person_affirmations, _pipeline_lessons_carousel_bank_rule, _pipeline_lessons_voice_guide_first [INFERRED 0.85]
- **Pinterest traffic engine toward 100k visitors/month** — _pipeline_lessons_goal_100k_visitors, _pipeline_lessons_pinterest_seo_agent, _pipeline_lessons_loved_pin_formats, _pipeline_lessons_pinterest_posting_ramp, _pipeline_lessons_metricool_scheduling, _pipeline_lessons_pin_website_utm [INFERRED 0.85]

## Communities (34 total, 14 thin omitted)

### Community 0 - "ISSUE11 repo rules (CLAUDE.md)"
Cohesion: 0.07
Nodes (35): Pipeline Builder (agent file), Pipeline Builder, Writes .pipeline/implementation-log.md (append rounds: files, decisions, checks, fixes), Pipeline Planner / Architect (agent file), Writes .pipeline/acceptance-criteria.md (numbered AC-n, PASS/FAIL testable), Spec section: App Store compliance check, Spec section: Loop stage (DESIRE→IMAGINE→EMBODY→BECOME test), Pipeline Planner / Architect (+27 more)

### Community 1 - "Third-party skills install & scan log"
Cohesion: 0.06
Nodes (38): Customer Panel (synthetic customer tester) (agent file), Customer Panel (synthetic customer tester), synthetic-crowd panel test (same seed, A vs B), GROWTH Media Buyer (agent file), Monday competitor ad watch (Meta Ad Library), GROWTH Media Buyer, GROWTH Pinterest SEO agent (agent file), Per-pin SEO row (title, description, board, alt text, link) (+30 more)

### Community 2 - "Spec: Core loop 1"
Cohesion: 0.11
Nodes (27): Writes .pipeline/spec.md (summary, files, architecture, DB, deps, edge cases, security), Acceptance criteria: Core loop 1 (AC-1..AC-68), Auth criteria AC-13..AC-24, Core loop 1 acceptance criteria, Process criteria AC-67..AC-68 (feature branch, no live migration), Scribe criteria AC-25..AC-43, Database/security criteria AC-55..AC-63 (RLS isolation, no secrets), Your World criteria AC-44..AC-54 (+19 more)

### Community 3 - "CURRENT FACTS box (read first; OPS updat"
Cohesion: 0.08
Nodes (15): beehiiv connector (read-only by default), 3.1 Apple in-app purchase subscriptions (RevenueCat ok), Megan builds the app herself in Replit, beehiiv plan blocks agent writes to forms/automations, CURRENT FACTS box (read first; OPS updates Fridays), 7-day trial also applies to $39.99 founding year; billing via App Store subscriptions, Glammi prices not confirmed (two-option retainer draft), ISSUE11 email: megan@ / support@issue11.app (+7 more)

### Community 4 - "Pipeline lessons learned (lessons.md)"
Cohesion: 0.07
Nodes (17): Pipeline lessons learned (lessons.md), Angle idea: "How to use AI to manifest your dream life", Plan: ISSUE11 launch + marketing → content for both → Glammi sprint to 10k, Claude Design canvas max 512 files per version, Glammi cold outreach paused (owned by separate agent), ISSUE11 editorial source of truth = design/editorial/, Megan's designs are a LOOK reference; agents design the UX states, From Megan: gratitude to every agent (+9 more)

### Community 5 - "Rule: graphify for every agent, split in"
Cohesion: 0.11
Nodes (19): GROWTH Reddit Specialist (agent file), Graphify note: load skill and read map piece first (pinned 0.9.111), Reddit loop: monitor → pick 5 → draft disclosed replies → report → track UTM, drafts/growth/reddit-playbook.md (keyword lists), GROWTH Reddit Specialist, Reddit UTM format (utm_source=reddit, organic, thread slug), Weekly report drafts/growth/reddit/<date>.md, Graphify note: load skill and read map piece first (pinned 0.9.111) (+11 more)

### Community 6 - "BANK rule: agents never invent quote/car"
Cohesion: 0.14
Nodes (4): Anti-slop checklist doc, Carousel and post copy built from LEXICON.md terms word for word, source noted, Mermaid mini carousel credits Paris Hilton (Megan's call), Read the ISSUE11 Brand Voice Guide first and run its AI-giveaways table

### Community 7 - "ASO tools: Astro ongoing + ASOMobile one"
Cohesion: 0.14
Nodes (12): Apify lergassy~pinterest-search-scraper research, Apify apt_marble/pinterest-trends-scraper (PASS), Apify pinterest-search-scraper takes `keywords` array, ASO listing v15 request: build from week-3 plan + ASOMobile/Astro exports, ASOMobile free week Nov 16-22, then 50% off window for the paid month, ASO tools: Astro ongoing + ASOMobile one month around submission, Manifestation pins evergreen; vision board peaks Dec–Jan, Pinterest API (ads:read) for keyword volume ranges (+4 more)

### Community 8 - "The Editor (art direction + mise en page"
Cohesion: 0.19
Nodes (8): The Editor (art direction + mise en page) (agent file), MISE-EN-PAGE.md magazine rules (US Letter, Inter Tight), The Editor (art direction + mise en page), /decision-brief command, Decision brief format (recommendation, numbers, reasoning, 2 options, risks), Anthropic cookbook Chief of Staff (tutorial; pattern adopted), /decision-brief command (executive brief pattern), New agent: The Editor (magazine layouts, MISE-EN-PAGE.md)

### Community 9 - "Logic map per tab (board 26) as source f"
Cohesion: 0.15
Nodes (11): Retention: weeks-showing-up streak (never resets), unlocks every 5 pages, endless Explore, Lucky Star renamed "The Editor", In-app feedback: "What are we missing?" + "Help us improve", Layout picker: "Let the Editor decide" + 4 layouts + More layouts, Explain app logic as "one week in her life" (day-by-day table), Logic map per tab (board 26) as source for Replit update, The Editor (Lucky Star) architecture: GUIDE on Home, ASSIST per screen, KNOWN→RETRIEVE→ASK→GENERATE→KEEP, Lulu print/shipping rules and margin (design/PRINT-PURCHASE.md) (+3 more)

### Community 10 - "Brand guide palette (Blush, Pink, Cream,"
Cohesion: 0.18
Nodes (8): Brand guide palette (Blush, Pink, Cream, Grey, Black), CAR14–CAR15 rejected; new carousels paused except diagram direction, Carousels mix playbook frameworks via DESIRE→IMAGINE→ACT→EVOLVE, one diagram, Electric Soft hero gradient (issue11.app), Megan's 11 framework diagrams = content redrawn in ISSUE11 style, Reference diagrams are content, not style: redraw in ISSUE11's own look, Graph pins keep layout, change colours: brand pinks, cream, red, lilac, Pin graph style: #100 hand arrows, LG9/LG10, brand pastel palette, no words in shapes

### Community 11 - "Carousels: funny/delulu hook + education"
Cohesion: 0.20
Nodes (4): "ISSUE11 Editorial Hooks & Visual Philosophy" source; hooks reframed to lexicon, Carousel hooks from real viral hooks (HOOKS.md), Bold gestures that ARE the message are on-brand for ISSUE11 covers, content-writing-thought-leadership skill for informative carousels

### Community 12 - "Daily article publish always allowed; re"
Cohesion: 0.20
Nodes (7): Verify live pages by <title> (Googlebot UA, re-fetch), not the 200 status, i11-publish-one fake-review safety gate, NexApp template traces cleanup (alt text, controls, screenshots), Glammi: 2 articles a day, Add 2 inbound "Keep reading" links to each new article, IndexNow ping on every publish (both sites), Use Search Console, not site:, for index counts

### Community 13 - "$300/mo Instagram ads test, launches Nov"
Cohesion: 0.20
Nodes (5): Ad creative direction: I Am-style vertical video, $300/mo Instagram ads test, launches Nov 17 (own photos + text screen only), 2027 Life Glow Up Kit (formerly Personal Rebrand Kit), Privacy pages updated (issue11.app, new glammi.ai/privacy), Free manifestation wallpaper maker (issue11.app/wallpapers)

### Community 14 - "Locked loved pin template set (COLOR-TES"
Cohesion: 0.29
Nodes (5): CAR5 carousel design language (vary layouts, same family), Pinterest carousels max 5 slides; plan 7-slide IG/TikTok with cut marks, Locked loved pin template set (COLOR-TEST.md), Phone-notes pin format (lowercase, issue11.app line, no footer), Pinterest agent makes 10–20 variations of favourites for nightly pick

### Community 15 - "Glammi audience: med spas, derm, cosmeti"
Cohesion: 0.25
Nodes (6): Duplicated Framer pages keep per-breakpoint/component text; patch all and grep live HTML, Glammi medical vertical = med spas, derm, plastic surgeons, cosmetic dentists, Glammi audience: med spas, derm, cosmetic dentists, jewelers, beauty e-commerce, Glammi sitewide black footer (industries, legal), Glammi blog verticals add local, creative, beauty e-commerce, perfume, indie fashion, Glammi positioning: Discoverability x Desirability

### Community 16 - "AI-generated images = editorial mood onl"
Cohesion: 0.50
Nodes (3): Check image twins across brands (32x32 RMSE<500) before use, Pins with AI people go out without AI label (Megan's call), Megan photo library canvas (design/photo-library/)

### Community 19 - "Public name: Megan Scott Manolova"
Cohesion: 0.50
Nodes (3): Public name: Megan Scott Manolova, Queen of AEO experiment (thequeenofaeo.com), Taste Engine Optimization (TEO) term

### Community 22 - "Stale Framer page fix: make a real edit "
Cohesion: 0.67
Nodes (3): Framer edits land on auto-branches: merge, check status, publish, verify live, Framer publish can serve the previous state; re-fetch live and republish, Stale Framer page fix: make a real edit then republish

### Community 23 - "Framer: duplicate an existing text prese"
Cohesion: 0.67
Nodes (3): Framer: duplicate an existing text preset instead of changing fontName, Framer hero: extra lines overflow 96vh; set maxWidth per breakpoint, check 3 breakpoints, Detaching a Framer text preset can swap its colour; re-set textColor and screenshot

## Ambiguous Edges - Review These
- `Rule: every question to Megan comes with recommended answer + reasoning` → `Give facts and options, not opinions, unless Megan asks`  [AMBIGUOUS]
  .pipeline/lessons.md · relation: conceptually_related_to

## Knowledge Gaps
- **37 isolated node(s):** `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)`, `GROWTH Pinterest SEO agent (agent file)`, `The Editor (art direction + mise en page) (agent file)` (+32 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 56 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Pipeline lessons learned (lessons.md)` connect `Pipeline lessons learned (lessons.md)` to `ISSUE11 repo rules (CLAUDE.md)`, `Third-party skills install & scan log`, `CURRENT FACTS box (read first; OPS updat`, `Rule: graphify for every agent, split in`, `BANK rule: agents never invent quote/car`, `ASO tools: Astro ongoing + ASOMobile one`, `The Editor (art direction + mise en page`, `Logic map per tab (board 26) as source f`, `Brand guide palette (Blush, Pink, Cream,`, `Carousels: funny/delulu hook + education`, `Daily article publish always allowed; re`, `$300/mo Instagram ads test, launches Nov`, `Locked loved pin template set (COLOR-TES`, `Glammi audience: med spas, derm, cosmeti`, `AI-generated images = editorial mood onl`, `Framer: always pass draft:true on addIte`, `Core positioning: manifestation done rig`, `Public name: Megan Scott Manolova`, `Self-improvement loop with an independen`, `Routine frequency cut to ~30 runs/day (u`, `Stale Framer page fix: make a real edit `, `Framer: duplicate an existing text prese`, `Track only keywords with 100+ US searche`, `"The New Way of Manifestation" positioni`, `17MedSpa article recipe (volume-led topi`, `Borrow functionality from other builds, `, `Photos always in colour; full-bleed, mag`, `Glammi covers: chrome theme, Megan's vis`, `Glammi worker schedule cut from every 2h`, `Log every Megan decision in the repo doc`, `Marketing copy is outcome-focused and po`, `Pin logo 92px tall at bottom on 1000x150`?**
  _High betweenness centrality (0.851) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `Production Safety Rule` (e.g. with `Builder commits on feature branch only; no push, deploy, merge or live migrations` and `Install skills as original upstream files; report risks`) actually correct?**
  _`Production Safety Rule` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `/pipeline command`, `Customer Panel (synthetic customer tester) (agent file)`, `GROWTH Media Buyer (agent file)` to the rest of the system?**
  _37 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `ISSUE11 repo rules (CLAUDE.md)` be split into smaller, more focused modules?**
  _Cohesion score 0.07012987012987013 - nodes in this community are weakly interconnected._
- **Why does `ISSUE11 repo rules (CLAUDE.md)` connect `ISSUE11 repo rules (CLAUDE.md)` to `Third-party skills install & scan log`, `Spec: Core loop 1`, `Pipeline lessons learned (lessons.md)`, `Rule: graphify for every agent, split in`, `Logic map per tab (board 26) as source f`?**
  _High betweenness centrality (0.128) - this node is a cross-community bridge._
- **Should `Third-party skills install & scan log` be split into smaller, more focused modules?**
  _Cohesion score 0.06262626262626263 - nodes in this community are weakly interconnected._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Rule: every question to Megan comes with recommended answer + reasoning` and `Give facts and options, not opinions, unless Megan asks`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._