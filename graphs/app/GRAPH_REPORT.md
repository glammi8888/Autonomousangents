# Graph Report - Autonomousangents  (2026-11-20)

## Corpus Check
- 40 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 162 nodes · 299 edges · 14 communities (11 shown, 3 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- ref_framer_api
- animated-icon.tsx
- graphs.py
- theme.ts
- app-tabs.web.tsx
- reset-project.js
- explore.tsx
- index.tsx
- Framer scripts README
- ISSUE11 Expo app AGENTS.md
- hint-row.tsx
- web-badge.tsx
- ISSUE11 Expo starter README
- glammi-cover.sh

## God Nodes (most connected - your core abstractions)
1. `ThemedText()` - 16 edges
2. `ThemedView()` - 15 edges
3. `useTheme()` - 9 edges
4. `Framer scripts README` - 8 edges
5. `TabTwoScreen()` - 7 edges
6. `HomeScreen()` - 7 edges
7. `WebBadge()` - 7 edges
8. `Spacing` - 7 edges
9. `diff()` - 7 edges
10. `Collapsible()` - 6 edges

## Surprising Connections (you probably didn't know these)
- `TabTwoScreen()` --calls--> `ExternalLink()`  [EXTRACTED]
  issue11/src/app/explore.tsx → issue11/src/components/external-link.tsx
- `TabTwoScreen()` --calls--> `ThemedText()`  [EXTRACTED]
  issue11/src/app/explore.tsx → issue11/src/components/themed-text.tsx
- `TabTwoScreen()` --calls--> `WebBadge()`  [EXTRACTED]
  issue11/src/app/explore.tsx → issue11/src/components/web-badge.tsx
- `HomeScreen()` --calls--> `ThemedView()`  [EXTRACTED]
  issue11/src/app/index.tsx → issue11/src/components/themed-view.tsx
- `TabButton()` --calls--> `ThemedText()`  [EXTRACTED]
  issue11/src/components/app-tabs.web.tsx → issue11/src/components/themed-text.tsx

## Import Cycles
- None detected.

## Communities (14 total, 3 thin omitted)

### Community 0 - "ref_framer_api"
Cohesion: 0.07
Nodes (17): body, faq, [html, slug, date], seoTitle, src, title, map, [slug, file, alt] (+9 more)

### Community 1 - "animated-icon.tsx"
Cohesion: 0.11
Nodes (11): TabLayout(), AnimatedSplashOverlay(), glowKeyframe, keyframe, logoKeyframe, styles, glowKeyframe, keyframe (+3 more)

### Community 2 - "graphs.py"
Cohesion: 0.15
Nodes (9): fp(), build(), diff(), files(), manifest(), rel(), sha(), status() (+1 more)

### Community 3 - "theme.ts"
Cohesion: 0.20
Nodes (8): styles, ThemedTextProps, ThemedViewProps, BottomTabInset, Colors, Fonts, MaxContentWidth, ThemeColor

### Community 4 - "app-tabs.web.tsx"
Cohesion: 0.23
Nodes (6): AppTabs(), CustomTabList(), styles, TabButton(), ExternalLink(), Props

### Community 5 - "reset-project.js"
Cohesion: 0.18
Nodes (7): exampleDirPath, fs, oldDirs, path, readline, rl, root

### Community 6 - "explore.tsx"
Cohesion: 0.42
Nodes (6): styles, TabTwoScreen(), ThemedView(), Collapsible(), styles, useTheme()

### Community 7 - "index.tsx"
Cohesion: 0.44
Nodes (7): getDevMenuHint(), HomeScreen(), styles, AnimatedIcon(), HintRow(), ThemedText(), WebBadge()

### Community 8 - "Framer scripts README"
Cohesion: 0.28
Nodes (9): Framer scripts README, Keys from env only: FRAMER_API_KEY_ISSUE11landing, FRAMER_API_KEY_GLAMMI, glammi-add-post.mjs (draft, refuses live), glammi-list.mjs (read only), glammi-publish-one.mjs (one item live + deploy), glammi-set-cover.mjs (WebP 1600x1067), i11-add-post.mjs (always draft), i11-list.mjs (read only) (+1 more)

### Community 9 - "ISSUE11 Expo app AGENTS.md"
Cohesion: 0.29
Nodes (6): ISSUE11 Expo app AGENTS.md, Continuous Native Generation (never edit ios/ android/), EAS build/submit/update, expo install / lint / tsc --noEmit before done, Expo Router file-based routes in src/app/, ISSUE11 app CLAUDE.md

### Community 10 - "hint-row.tsx"
Cohesion: 0.50
Nodes (3): HintRowProps, styles, Spacing

## Knowledge Gaps
- **11 isolated node(s):** `Expo Router file-based routes in src/app/`, `EAS build/submit/update`, `expo install / lint / tsc --noEmit before done`, `Continuous Native Generation (never edit ios/ android/)`, `ISSUE11 app CLAUDE.md` (+6 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 82 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ThemedText()` connect `index.tsx` to `theme.ts`, `app-tabs.web.tsx`, `explore.tsx`, `hint-row.tsx`, `web-badge.tsx`?**
  _High betweenness centrality (0.010) - this node is a cross-community bridge._
- **What connects `Expo Router file-based routes in src/app/`, `EAS build/submit/update`, `expo install / lint / tsc --noEmit before done` to the rest of the system?**
  _11 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `ref_framer_api` be split into smaller, more focused modules?**
  _Cohesion score 0.07258064516129033 - nodes in this community are weakly interconnected._
- **Why does `ThemedView()` connect `explore.tsx` to `theme.ts`, `app-tabs.web.tsx`, `index.tsx`, `hint-row.tsx`, `web-badge.tsx`?**
  _High betweenness centrality (0.008) - this node is a cross-community bridge._
- **Should `animated-icon.tsx` be split into smaller, more focused modules?**
  _Cohesion score 0.11462450592885376 - nodes in this community are weakly interconnected._