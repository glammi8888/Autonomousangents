# Graph Report - Autonomousangents  (2026-11-22)

## Corpus Check
- 41 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 165 nodes · 323 edges · 19 communities (15 shown, 4 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- graphs.py
- theme.ts
- animated-icon.tsx
- app-tabs.web.tsx
- reset-project.js
- explore.tsx
- Framer scripts README
- index.tsx
- animated-icon.web.tsx
- ref_fs
- ISSUE11 Expo app AGENTS.md
- glammi-add-faq.mjs
- glammi-add-post.mjs
- i11-add-post.mjs
- hint-row.tsx
- web-badge.tsx
- ref_framer_api
- ISSUE11 Expo starter README
- glammi-cover.sh

## God Nodes (most connected - your core abstractions)
1. `ThemedText()` - 16 edges
2. `ThemedView()` - 15 edges
3. `Framer scripts README` - 11 edges
4. `useTheme()` - 9 edges
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

## Hyperedges (group relationships)
- **Framer draft-then-publish-one flow** — tools_framer_glammi_add_post, tools_framer_glammi_set_cover, tools_framer_glammi_add_faq, tools_framer_glammi_publish_one [EXTRACTED 1.00]

## Communities (19 total, 4 thin omitted)

### Community 0 - "graphs.py"
Cohesion: 0.15
Nodes (9): fp(), build(), diff(), files(), manifest(), rel(), sha(), status() (+1 more)

### Community 1 - "theme.ts"
Cohesion: 0.20
Nodes (8): styles, ThemedTextProps, ThemedViewProps, BottomTabInset, Colors, Fonts, MaxContentWidth, ThemeColor

### Community 2 - "animated-icon.tsx"
Cohesion: 0.23
Nodes (7): TabLayout(), AnimatedSplashOverlay(), glowKeyframe, keyframe, logoKeyframe, styles, AppTabs()

### Community 3 - "app-tabs.web.tsx"
Cohesion: 0.23
Nodes (6): AppTabs(), CustomTabList(), styles, TabButton(), ExternalLink(), Props

### Community 4 - "reset-project.js"
Cohesion: 0.18
Nodes (7): exampleDirPath, fs, oldDirs, path, readline, rl, root

### Community 5 - "explore.tsx"
Cohesion: 0.42
Nodes (6): styles, TabTwoScreen(), ThemedView(), Collapsible(), styles, useTheme()

### Community 6 - "Framer scripts README"
Cohesion: 0.31
Nodes (5): framer-api@5.1.0 (scanned, --ignore-scripts), Framer API keys from env (FRAMER_API_KEY_ISSUE11landing, FRAMER_API_KEY_GLAMMI), Framer scripts README, Glammi blog collection, ISSUE11 Blog Posts collection

### Community 7 - "index.tsx"
Cohesion: 0.44
Nodes (7): getDevMenuHint(), HomeScreen(), styles, AnimatedIcon(), HintRow(), ThemedText(), WebBadge()

### Community 8 - "animated-icon.web.tsx"
Cohesion: 0.22
Nodes (4): glowKeyframe, keyframe, logoKeyframe, styles

### Community 9 - "ref_fs"
Cohesion: 0.25
Nodes (4): map, [slug, file, alt], webp, [slug,file,alt]

### Community 10 - "ISSUE11 Expo app AGENTS.md"
Cohesion: 0.29
Nodes (6): ISSUE11 Expo app AGENTS.md, Continuous Native Generation (never edit ios/ android/), EAS build/submit/update, expo install / lint / tsc --noEmit before done, Expo Router file-based routes in src/app/, ISSUE11 app CLAUDE.md

### Community 11 - "glammi-add-faq.mjs"
Cohesion: 0.29
Nodes (4): qa, [slug, qaFile], FAQ Schema field (Blog Posts), IndexNow

### Community 12 - "glammi-add-post.mjs"
Cohesion: 0.29
Nodes (6): body, faq, [html, slug, date], seoTitle, src, title

### Community 13 - "i11-add-post.mjs"
Cohesion: 0.29
Nodes (6): body, faq, [html,slug,date,img,alt], seoTitle, src, title

### Community 14 - "hint-row.tsx"
Cohesion: 0.50
Nodes (3): HintRowProps, styles, Spacing

## Knowledge Gaps
- **10 isolated node(s):** `Expo Router file-based routes in src/app/`, `EAS build/submit/update`, `expo install / lint / tsc --noEmit before done`, `Continuous Native Generation (never edit ios/ android/)`, `ISSUE11 app CLAUDE.md` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 79 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Framer scripts README` connect `Framer scripts README` to `ref_fs`, `glammi-add-faq.mjs`, `glammi-add-post.mjs`, `i11-add-post.mjs`?**
  _High betweenness centrality (0.018) - this node is a cross-community bridge._
- **What connects `Expo Router file-based routes in src/app/`, `EAS build/submit/update`, `expo install / lint / tsc --noEmit before done` to the rest of the system?**
  _10 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Why does `ThemedText()` connect `index.tsx` to `theme.ts`, `app-tabs.web.tsx`, `explore.tsx`, `hint-row.tsx`, `web-badge.tsx`?**
  _High betweenness centrality (0.010) - this node is a cross-community bridge._
- **Why does `ThemedView()` connect `explore.tsx` to `theme.ts`, `app-tabs.web.tsx`, `index.tsx`, `hint-row.tsx`, `web-badge.tsx`?**
  _High betweenness centrality (0.007) - this node is a cross-community bridge._