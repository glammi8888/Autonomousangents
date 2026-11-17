# Graph Report - Autonomousangents  (2026-11-17)

## Corpus Check
- Piece of the repo (see graphs/README.md). Images and vendored skills not mapped.

## Summary
- 202 nodes · 273 edges · 12 communities
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 20 edges (avg confidence: 0.83)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- V1 Simplified
- ISSUE11 Product Architecture (Locked)
- ISSUE11 Positioning
- Lucky Star Architecture (Proposal v1)
- ISSUE11 Brand Guide v1
- Landing Copy + Framer Notes
- Flow Map + Gaps
- Brand Revamp Direction
- Printed Magazine Purchase Flow
- Rank plan (App Store, own pages, lists, 
- UI/UX Laws Audit
- ISSUE11 Vibe Board

## God Nodes (most connected - your core abstractions)
1. `V1 Simplified` - 25 edges
2. `ISSUE11 Product Architecture (Locked)` - 24 edges
3. `ISSUE11 Positioning` - 17 edges
4. `Lucky Star Architecture (Proposal v1)` - 15 edges
5. `Landing Copy + Framer Notes` - 15 edges
6. `Flow Map + Gaps` - 14 edges
7. `Onboarding v3 (Locked)` - 13 edges
8. `Lucky Star Personality & Tone` - 11 edges
9. `AI-Made Magazine Spec` - 11 edges
10. `Mise en Page Guidelines v1` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Landing Copy + Framer Notes` --references--> `ISSUE11 Brand Guide v1`  [EXTRACTED]
  design/landing/COPY-AND-FRAMER-NOTES.md → brand/BRAND-GUIDE.md
- `Wireframes v0` --references--> `ISSUE11 Brand Guide v1`  [EXTRACTED]
  design/WIREFRAMES.md → brand/BRAND-GUIDE.md
- `Colour: flat Electric Soft, no gradients` --references--> `Electric Soft gradient`  [INFERRED]
  design/magazine/MISE-EN-PAGE.md → brand/BRAND-GUIDE.md
- `Printed issues via print partner API` --semantically_similar_to--> `Printed issue: 40 pages, US Letter, $29.99`  [INFERRED] [semantically similar]
  design/FLOW-MAP.md → design/PRINT-PURCHASE.md
- `ISSUE11 Brand Guide v1` --references--> `ISSUE11 North Star`  [EXTRACTED]
  brand/BRAND-GUIDE.md → design/NORTH-STAR.md

## Hyperedges (group relationships)
- **Lucky Star safe action flow (route → propose → KEEP → log)** — design_lucky_star_architecture_contextual_routing, design_lucky_star_architecture_context_integrity, design_lucky_star_architecture_proposals_table, design_lucky_star_architecture_approval_system, design_lucky_star_architecture_agent_log [EXTRACTED 1.00]
- **Onboarding pain → way out → value equation** — design_onboarding_v3_pain_cards, design_positioning_ten_pain_points, design_positioning_ten_desired_outcomes, design_onboarding_v3_value_line, design_positioning_value_equation, design_onboarding_v3_paywall_screen_37 [EXTRACTED 1.00]
- **Fixed template library the AI fills** — design_magazine_ai_spec_ai_fills_never_designs, design_magazine_ai_spec_layout_library, design_magazine_style_guide_layout_library, design_magazine_mise_en_page_layout_library_a_z, design_v1_simplified_lucky_star_makes_magazine [INFERRED 0.85]

## Communities (12 total, 0 thin omitted)

### Community 0 - "V1 Simplified"
Cohesion: 0.08
Nodes (27): AI-Made Magazine Spec, Issue generation: input → plan → check → render → tweak, Layout library from Magazine Lab, Small edits kept in V1, Mise en Page Guidelines v1, The Editor's checklist, Same rules for the app's template library, Image rules (no collage) (+19 more)

### Community 1 - "ISSUE11 Product Architecture (Locked)"
Cohesion: 0.09
Nodes (19): ISSUE11 Aesthetics (8 Worlds), Aspirations per world, 8 aesthetic worlds (onboarding screen 25), Style anchor image prompt, Library of worlds for Your World, App After the Paywall, Bottom bar: Home · Explore · Issue · Journal · You + floating 11, Recommended design order (Home first) (+11 more)

### Community 2 - "ISSUE11 Positioning"
Cohesion: 0.09
Nodes (20): ISSUE11 ICP, Primary ICP: the disappointed manifester (Nov 9), Objections and answers, A/B angles: dream-life experience vs follow-through, ICP: 24-38 ambitious aesthetic woman reinventing herself, Onboarding v3 (Locked), Downsell pop-up (37b), Meet Lucky Star + AI consent (screen 34) (+12 more)

### Community 3 - "Lucky Star Architecture (Proposal v1)"
Cohesion: 0.12
Nodes (17): Lucky Star Architecture (Proposal v1), agent_log table, Approval system: KEEP / EDIT / TRY AGAIN / UNDO, Contextual routing: screen → mode → skill → tools (in code), lucky-star Supabase Edge Function, proposals table (KEEP before write), Structured user state (source + confidence columns), V1 required vs later (+9 more)

### Community 4 - "ISSUE11 Brand Guide v1"
Cohesion: 0.10
Nodes (16): ISSUE11 Brand Guide v1, Brand colors (Blush, Pink, Red, Cream, Green, Black), Electric Soft gradient, Small mono labels (IBM Plex Mono 11px), Tagline: See it. Write it. Become it., Electric Soft Gradient Handoff, App Store screenshots: A · Cover story, Electric Soft official gradient (+8 more)

### Community 5 - "Landing Copy + Framer Notes"
Cohesion: 0.12
Nodes (16): Landing Copy + Framer Notes, Waitlist tool = beehiiv (Slim Embed), Founding offer: first 1,000 get 50% off year one, Decision: landing built in Megan's Framer template, Landing v6 (approved copy), Missing info flagged (privacy, social, beta capacity), Landing FAQ (AEO), 8 FAQ answers (AEO) (+8 more)

### Community 6 - "Flow Map + Gaps"
Cohesion: 0.12
Nodes (13): Flow Map + Gaps, Apple 3.1.3(b) / 4.2 check, Desktop magazine editor (dropped from V1), Figma v1 file (Night + Light modes), Flow gaps (no cover reveal, (+) undefined, etc.), Onboarding v2 (teach the loop), Lucky Star Sheet Design Brief, 5 sheet states (Guide, Next Move, Proof, Listening, Scribe Assist) (+5 more)

### Community 7 - "Brand Revamp Direction"
Cohesion: 0.18
Nodes (9): Brand Revamp Direction, Fonts locked: Archivo Condensed / Inter Tight / IBM Plex Mono, Melting titles (dropped), Color: pink only accent, Claude Design Re-skin Brief, Locked by founder (logo, colors, fonts, words), Make a page flow, Screens & logic to keep (+1 more)

### Community 8 - "Printed Magazine Purchase Flow"
Cohesion: 0.20
Nodes (10): Printed issues via print partner API, US Letter format + 6-col grid, Printed Magazine Purchase Flow, Issue 02 starts after she prints, Lulu print partner, Margin per printed issue (~$12.07), Printed issue: 40 pages, US Letter, $29.99, Shipping add-ons (Standard/Expedited/Express) (+2 more)

### Community 9 - "Rank plan (App Store, own pages, lists, "
Cohesion: 0.18
Nodes (10): Blog Keyword Plan, Blog cover images (Megan's editorial), First 7 blog articles keyword plan, ISSUE11 Profile Copy, App Store listing draft, Core profile line (vision board → magazine, one move a week), LinkedIn / Crunchbase / Product Hunt / Pinterest profiles, ISSUE11 Rank Plan (+2 more)

### Community 10 - "UI/UX Laws Audit"
Cohesion: 0.29
Nodes (5): UI/UX Laws Audit, Contrast fix: text-pink #C2207E, grey #6B6762, Issue reader: swipe + p.15/40 + one Edit, Principles already strong (Goal-Gradient, Peak-End, etc.), Tab bar: 11pt labels, 44pt targets

### Community 11 - "ISSUE11 Vibe Board"
Cohesion: 0.67
Nodes (3): ISSUE11 Vibe Board, Logo system (hero wavy, calm, short 11 mark), Vibe board: pink + black + cream, zebra stripes

## Knowledge Gaps
- **86 isolated node(s):** `Brand colors (Blush, Pink, Red, Cream, Green, Black)`, `Small mono labels (IBM Plex Mono 11px)`, `Tagline: See it. Write it. Become it.`, `Logo system (hero wavy, calm, short 11 mark)`, `Vibe board: pink + black + cream, zebra stripes` (+81 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 110 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `V1 Simplified` connect `V1 Simplified` to `ISSUE11 Product Architecture (Locked)`, `ISSUE11 Positioning`, `Lucky Star Architecture (Proposal v1)`, `Landing Copy + Framer Notes`, `Printed Magazine Purchase Flow`, `UI/UX Laws Audit`?**
  _High betweenness centrality (0.356) - this node is a cross-community bridge._
- **What connects `Brand colors (Blush, Pink, Red, Cream, Green, Black)`, `Small mono labels (IBM Plex Mono 11px)`, `Tagline: See it. Write it. Become it.` to the rest of the system?**
  _86 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `V1 Simplified` be split into smaller, more focused modules?**
  _Cohesion score 0.08387096774193549 - nodes in this community are weakly interconnected._
- **Why does `Landing Copy + Framer Notes` connect `Landing Copy + Framer Notes` to `V1 Simplified`, `ISSUE11 Positioning`, `ISSUE11 Brand Guide v1`, `Brand Revamp Direction`, `Printed Magazine Purchase Flow`, `UI/UX Laws Audit`?**
  _High betweenness centrality (0.353) - this node is a cross-community bridge._
- **Should `ISSUE11 Product Architecture (Locked)` be split into smaller, more focused modules?**
  _Cohesion score 0.09420289855072464 - nodes in this community are weakly interconnected._
- **Why does `ISSUE11 Positioning` connect `ISSUE11 Positioning` to `V1 Simplified`, `ISSUE11 Product Architecture (Locked)`, `Lucky Star Architecture (Proposal v1)`, `ISSUE11 Brand Guide v1`, `Landing Copy + Framer Notes`?**
  _High betweenness centrality (0.239) - this node is a cross-community bridge._
- **Should `ISSUE11 Positioning` be split into smaller, more focused modules?**
  _Cohesion score 0.09420289855072464 - nodes in this community are weakly interconnected._