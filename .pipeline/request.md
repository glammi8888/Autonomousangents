# Request

**Date:** 2026-10-06
**Requested by:** Megan
**Branch:** planning on `claude/fervent-volta-fibmd4` (the session's working branch; the app lives in `issue11/`). The Builder creates `feature/core-loop-1` on Friday Oct 9.

## Request (Megan, Oct 6: "ok so start the planner")
Plan the first build slice of the ISSUE11 iPhone app (Expo, in `issue11/`), so the Builder can start on Friday Oct 9:

1. **App foundation:** replace the Expo starter with ISSUE11's navigation (the 4 functions: Your World · Audio · Scribe · Publish, plus the 11 sticker entry point for Lucky Star as a placeholder only) and one shared design system (colors, fonts, spacing) so the visual look can be refined later in one place.
2. **Sign-up / sign-in only** (account creation and login, needed to save content). **Onboarding is NOT in this slice: Megan, Oct 6: "but onboarding isn't finalized yet though".** Leave a single placeholder entry point where onboarding will plug in later.
3. **Your World: mechanics only.** Add her own photos (photo picker, permissions, saving, a simple grid). **Megan, Oct 6: "the 'your world' images aren't finalized either"**, so no curated/suggested image library, categories or final layout: use plain placeholders that the final images and look can replace without code changes.
4. **Scribe = writing, and she chooses what goes in her magazine.** Megan, Oct 6, word for word: "scribe should be writing and it appears on your magazine if you want to". So: write and save entries, plus a per-entry choice (off by default) to include it in her Issue, stored so Publish can read only the chosen entries later. Writing prompts and gratitude prompts are a later slice.

## Context and limits
- Product rules: `design/PRODUCT-ARCHITECTURE.md`, `design/NORTH-STAR.md`. Keep the magazine as the hero, the AI invisible until useful. No productivity/task/goal features.
- **Publish (AI magazine) and Lucky Star are NOT in this slice.** They wait for Megan's 3 Lucky Star yes/no answers. Design data so Publish can later read World + Scribe content.
- **Audio and paywall are NOT in this slice** (weeks 3–4).
- Timeline: core loop (incl. Publish) on Megan's phone via internal TestFlight by ~Oct 23 · beta Nov 11 · App Store launch Dec 11 (submit ~Nov 28).
- Visual look is still being refined in Claude Design: the flow is locked, the look is not. Build on design tokens, not hard-coded styles.
- Expo SDK 57: follow `issue11/AGENTS.md` (check current Expo docs, never memory).
- If the slice is too big for one spec, propose the smallest first slice and list the rest in order.
- Sign-in and user data are sensitive areas: flag them clearly, they need Megan's approval of the spec before building (target: approval by Wed Oct 8).
