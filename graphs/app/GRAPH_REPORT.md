# Graph Report - Autonomousangents  (2026-11-17)

## Corpus Check
- Piece of the repo (see graphs/README.md). Images and vendored skills not mapped.

## Summary
- 229 nodes · 387 edges · 13 communities (11 shown, 2 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- package.json
- explore.tsx
- ref_framer_api
- expo
- animated-icon.tsx
- reset-project.js
- animated-icon.web.tsx
- Framer scripts README
- tsconfig.json
- ISSUE11 Expo app AGENTS.md
- scripts
- ISSUE11 Expo starter README
- glammi-cover.sh

## God Nodes (most connected - your core abstractions)
1. `react-native` - 17 edges
2. `ThemedText()` - 16 edges
3. `ThemedView()` - 15 edges
4. `expo` - 14 edges
5. `useTheme()` - 9 edges
6. `Framer scripts README` - 8 edges
7. `react` - 7 edges
8. `scripts` - 7 edges
9. `TabTwoScreen()` - 7 edges
10. `HomeScreen()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `HomeScreen()` --calls--> `AnimatedIcon()`  [EXTRACTED]
  issue11/src/app/index.tsx → issue11/src/components/animated-icon.tsx
- `ISSUE11 app CLAUDE.md` --references--> `ISSUE11 Expo app AGENTS.md`  [EXTRACTED]
  issue11/CLAUDE.md → issue11/AGENTS.md
- `TabLayout()` --calls--> `AnimatedSplashOverlay()`  [EXTRACTED]
  issue11/src/app/_layout.tsx → issue11/src/components/animated-icon.tsx
- `TabLayout()` --calls--> `AppTabs()`  [EXTRACTED]
  issue11/src/app/_layout.tsx → issue11/src/components/app-tabs.tsx
- `TabTwoScreen()` --calls--> `ExternalLink()`  [EXTRACTED]
  issue11/src/app/explore.tsx → issue11/src/components/external-link.tsx

## Import Cycles
- None detected.

## Communities (13 total, 2 thin omitted)

### Community 0 - "package.json"
Cohesion: 0.06
Nodes (46): dependencies, expo@~57.0.26, expo-constants@~57.0.20, expo-device@~57.0.2, expo-font@~57.0.4, expo-glass-effect@~57.0.4, expo-linking@~57.0.11, expo-status-bar@~57.0.1 (+38 more)

### Community 1 - "explore.tsx"
Cohesion: 0.15
Nodes (31): styles, TabTwoScreen(), getDevMenuHint(), HomeScreen(), styles, AppTabs(), CustomTabList(), styles (+23 more)

### Community 2 - "ref_framer_api"
Cohesion: 0.07
Nodes (17): body, faq, [html, slug, date], seoTitle, src, title, map, [slug, file, alt] (+9 more)

### Community 3 - "expo"
Cohesion: 0.07
Nodes (28): backgroundColor, backgroundImage, foregroundImage, monochromeImage, adaptiveIcon, predictiveBackGestureEnabled, projectId, reactCompiler (+20 more)

### Community 4 - "animated-icon.tsx"
Cohesion: 0.13
Nodes (15): expo-router@~57.0.24, expo-splash-screen@~57.0.9, react@19.2.3, TabLayout(), AnimatedIcon(), AnimatedSplashOverlay(), glowKeyframe, keyframe (+7 more)

### Community 5 - "reset-project.js"
Cohesion: 0.18
Nodes (7): exampleDirPath, fs, oldDirs, path, readline, rl, root

### Community 6 - "animated-icon.web.tsx"
Cohesion: 0.20
Nodes (6): expo-image@~57.0.5, glowKeyframe, keyframe, logoKeyframe, styles, expo-image

### Community 7 - "Framer scripts README"
Cohesion: 0.28
Nodes (9): Framer scripts README, Keys from env only: FRAMER_API_KEY_ISSUE11landing, FRAMER_API_KEY_GLAMMI, glammi-add-post.mjs (draft, refuses live), glammi-list.mjs (read only), glammi-publish-one.mjs (one item live + deploy), glammi-set-cover.mjs (WebP 1600x1067), i11-add-post.mjs (always draft), i11-list.mjs (read only) (+1 more)

### Community 8 - "tsconfig.json"
Cohesion: 0.25
Nodes (7): compilerOptions, paths, strict, extends, include, @/assets/*, expo/tsconfig.base

### Community 9 - "ISSUE11 Expo app AGENTS.md"
Cohesion: 0.29
Nodes (6): ISSUE11 Expo app AGENTS.md, Continuous Native Generation (never edit ios/ android/), EAS build/submit/update, expo install / lint / tsc --noEmit before done, Expo Router file-based routes in src/app/, ISSUE11 app CLAUDE.md

### Community 10 - "scripts"
Cohesion: 0.29
Nodes (7): scripts, android, ios, lint, reset-project, start, web

## Knowledge Gaps
- **12 isolated node(s):** `expo/tsconfig.base`, `Expo Router file-based routes in src/app/`, `EAS build/submit/update`, `expo install / lint / tsc --noEmit before done`, `Continuous Native Generation (never edit ios/ android/)` (+7 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 108 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `react-native` connect `explore.tsx` to `package.json`, `animated-icon.tsx`, `animated-icon.web.tsx`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **What connects `expo/tsconfig.base`, `Expo Router file-based routes in src/app/`, `EAS build/submit/update` to the rest of the system?**
  _12 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `package.json` be split into smaller, more focused modules?**
  _Cohesion score 0.060129509713228495 - nodes in this community are weakly interconnected._
- **Why does `dependencies` connect `package.json` to `animated-icon.tsx`, `animated-icon.web.tsx`?**
  _High betweenness centrality (0.053) - this node is a cross-community bridge._
- **Should `explore.tsx` be split into smaller, more focused modules?**
  _Cohesion score 0.14693446088794926 - nodes in this community are weakly interconnected._
- **Why does `scripts` connect `scripts` to `package.json`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Should `ref_framer_api` be split into smaller, more focused modules?**
  _Cohesion score 0.07258064516129033 - nodes in this community are weakly interconnected._