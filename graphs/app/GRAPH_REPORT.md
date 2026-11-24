# Graph Report - Autonomousangents  (2026-11-24)

## Corpus Check
- 42 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 166 nodes · 318 edges · 19 communities (14 shown, 5 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 5 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- graphs.py
- animated-icon.tsx
- theme.ts
- app-tabs.web.tsx
- reset-project.js
- explore.tsx
- index.tsx
- glammi-set-cover.mjs
- ref_framer_api
- ISSUE11 Expo app AGENTS.md
- glammi-add-faq.mjs
- glammi-add-post.mjs
- i11-add-post.mjs
- hint-row.tsx
- web-badge.tsx
- Framer scripts (tools/framer)
- ISSUE11 Expo starter README
- glammi-cover.sh

## God Nodes (most connected - your core abstractions)
1. `ThemedText()` - 16 edges
2. `ThemedView()` - 15 edges
3. `useTheme()` - 9 edges
4. `TabTwoScreen()` - 7 edges
5. `HomeScreen()` - 7 edges
6. `WebBadge()` - 7 edges
7. `Spacing` - 7 edges
8. `diff()` - 7 edges
9. `Collapsible()` - 6 edges
10. `ISSUE11 Expo app AGENTS.md` - 6 edges

## Surprising Connections (you probably didn't know these)
- `TabTwoScreen()` --calls--> `ExternalLink()`  [EXTRACTED]
  issue11/src/app/explore.tsx → issue11/src/components/external-link.tsx
- `TabTwoScreen()` --calls--> `ThemedText()`  [EXTRACTED]
  issue11/src/app/explore.tsx → issue11/src/components/themed-text.tsx
- `HomeScreen()` --calls--> `ThemedView()`  [EXTRACTED]
  issue11/src/app/index.tsx → issue11/src/components/themed-view.tsx
- `HomeScreen()` --calls--> `WebBadge()`  [EXTRACTED]
  issue11/src/app/index.tsx → issue11/src/components/web-badge.tsx
- `TabButton()` --calls--> `ThemedText()`  [EXTRACTED]
  issue11/src/components/app-tabs.web.tsx → issue11/src/components/themed-text.tsx

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Guarded publish-one scripts (one item live, abort on unsafe state)** — tools_framer_glammi_publish_one, tools_framer_i11_publish_one, tools_framer_readme_draft_first_publishing [EXTRACTED 1.00]
- **Glammi article draft pipeline (add post, cover, FAQ, link, publish)** — tools_framer_glammi_add_post, tools_framer_glammi_set_cover, tools_framer_glammi_add_faq, tools_framer_glammi_link_before_faq, tools_framer_glammi_publish_one [INFERRED 0.85]

## Communities (19 total, 5 thin omitted)

### Community 0 - "graphs.py"
Cohesion: 0.15
Nodes (9): fp(), build(), diff(), files(), manifest(), rel(), sha(), status() (+1 more)

### Community 1 - "animated-icon.tsx"
Cohesion: 0.12
Nodes (11): TabLayout(), AnimatedSplashOverlay(), glowKeyframe, keyframe, logoKeyframe, styles, glowKeyframe, keyframe (+3 more)

### Community 2 - "theme.ts"
Cohesion: 0.22
Nodes (7): styles, ThemedTextProps, ThemedViewProps, BottomTabInset, Colors, Fonts, ThemeColor

### Community 3 - "app-tabs.web.tsx"
Cohesion: 0.20
Nodes (7): AppTabs(), CustomTabList(), styles, TabButton(), ExternalLink(), Props, MaxContentWidth

### Community 4 - "reset-project.js"
Cohesion: 0.18
Nodes (7): exampleDirPath, fs, oldDirs, path, readline, rl, root

### Community 5 - "explore.tsx"
Cohesion: 0.47
Nodes (7): styles, TabTwoScreen(), ThemedView(), Collapsible(), styles, WebBadge(), useTheme()

### Community 6 - "index.tsx"
Cohesion: 0.39
Nodes (6): getDevMenuHint(), HomeScreen(), styles, AnimatedIcon(), HintRow(), ThemedText()

### Community 7 - "glammi-set-cover.mjs"
Cohesion: 0.25
Nodes (4): map, [slug, file, alt], webp, [slug,file,alt]

### Community 8 - "ref_framer_api"
Cohesion: 0.28
Nodes (3): [slug, para], Glammi Framer site, [site]

### Community 9 - "ISSUE11 Expo app AGENTS.md"
Cohesion: 0.29
Nodes (6): ISSUE11 Expo app AGENTS.md, Continuous Native Generation (never edit ios/ android/), EAS build/submit/update, expo install / lint / tsc --noEmit before done, Expo Router file-based routes in src/app/, ISSUE11 app CLAUDE.md

### Community 10 - "glammi-add-faq.mjs"
Cohesion: 0.29
Nodes (4): qa, [slug, qaFile], FAQ Schema field on blog posts, ISSUE11 Framer site (issue11.app)

### Community 11 - "glammi-add-post.mjs"
Cohesion: 0.29
Nodes (6): body, faq, [html, slug, date], seoTitle, src, title

### Community 12 - "i11-add-post.mjs"
Cohesion: 0.29
Nodes (6): body, faq, [html,slug,date,img,alt], seoTitle, src, title

### Community 13 - "hint-row.tsx"
Cohesion: 0.50
Nodes (3): HintRowProps, styles, Spacing

## Knowledge Gaps
- **8 isolated node(s):** `Expo Router file-based routes in src/app/`, `EAS build/submit/update`, `expo install / lint / tsc --noEmit before done`, `Continuous Native Generation (never edit ios/ android/)`, `ISSUE11 app CLAUDE.md` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 79 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ThemedText()` connect `index.tsx` to `theme.ts`, `app-tabs.web.tsx`, `explore.tsx`, `hint-row.tsx`, `web-badge.tsx`?**
  _High betweenness centrality (0.010) - this node is a cross-community bridge._
- **What connects `Expo Router file-based routes in src/app/`, `EAS build/submit/update`, `expo install / lint / tsc --noEmit before done` to the rest of the system?**
  _8 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `animated-icon.tsx` be split into smaller, more focused modules?**
  _Cohesion score 0.11904761904761904 - nodes in this community are weakly interconnected._
- **Why does `ThemedView()` connect `explore.tsx` to `theme.ts`, `app-tabs.web.tsx`, `index.tsx`, `hint-row.tsx`, `web-badge.tsx`?**
  _High betweenness centrality (0.007) - this node is a cross-community bridge._
- **Why does `Glammi Framer site` connect `ref_framer_api` to `glammi-add-faq.mjs`, `glammi-add-post.mjs`, `glammi-set-cover.mjs`, `glammi-publish-one.mjs`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._