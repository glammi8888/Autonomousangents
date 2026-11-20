# ISSUE11

An iPhone app (Expo / React Native) where your ambitions become your own personal magazine: a weekly action, a private journal, saved images and audio sessions, and an AI Editor that turns them into a 40-page issue you can print.

## Current source of truth (read this first)
- **Design v1 (Nov 20, 2026) is the ONLY current design.** Older designs, boards and earlier prompts are outdated. If code disagrees with this file, this file wins.
- Tabs: **Home · Explore · Issue · Journal · You.** Listen and Vision are NOT tabs (sessions live in Explore + player; vision lives in Explore → Saved).
- **"The Editor"** is the AI (the floating 11 button). The old name "Lucky Star" is retired everywhere.
- **"Saved"** (inside Explore) replaced "My saves" / "Her world". Never "her world".
- Removed for good: session detail page, eyes-closed, how-do-you-feel, ritual, progress, streak page, old Listen tab, any "BECOME HER" sample.
- Out of scope unless the owner says so: onboarding + first-open cover reveal (locked, being reworked separately), sign-in, payments/paywall logic, the api-server database, widgets.

## Product rules (never break)
- Never call the user "she"/"her"; use "you" / "future you". Say "action", never "move".
- The user's own words are never rewritten or changed by the app or the AI.
- One action a week (week starts Monday). Numbers shown: pages toward print ("15 of 40") and weeks showing up. No streaks, no guilt, no fake urgency.
- Everyday screens off-white and photo-led. Pale pink #F4E4E4 → #F0D0D8 only on first open and the paywall. Bright pink only in the Editor halo.
- One font: **Inter Tight**. (Archivo Black, Archivo Narrow, IBM Plex Mono are retired.) No barbie imagery.
- Keep the crisis-word safety stop (988).

## Design tokens
ink #0D0D0D · paper #F3F3F1 (background, sheets, tab bar) · paper-warm #FBFAF7 (journal) · white #FFFFFF · grey text #5E5E5E · inactive tab #8A8A8A · line rgba(13,13,13,0.12) · halo pink #F2B8CB → #F7D3DF, glow #F6AAC6 → #FFD6E4 · destructive #B42318.
Display 44–64/600 tracking −0.055em · H1 32–40/600 · H2 24–30/600 · pull quote 20–38/300 italic · body 15–16/400 · label 11/600 uppercase +0.1em. 24px side margins. Photos full-bleed with sharp corners; only buttons (54px pills) and sheets (22px top radius) are rounded. Tab bar 84px.

## Data
All user data stays on the phone for now (IssueProvider / local storage): current issue (max 40 pages), pages, weekly action, journal entries (always private), saves, player position, settings. No cloud database yet.

## Where things live
- App: `artifacts/issue11/` (expo-router). Tabs in `app/(tabs)/`: index = Home, world = Explore, create = Issue, scribe = Journal, profile = You.
- Strings: `constants/strings.ts`, `constants/explore-strings.ts`. Colors: `constants/colors.ts` (put every color here, no hard-coded hex in screens).
- State: `state/IssueProvider`, `state/SessionPlaybackProvider`.
- `artifacts/api-server` and `artifacts/mockup-sandbox` are not used by the app.

## User preferences (owner: non-developer founder, pays per credit)
- Keep every change lean: reuse existing components, no new packages unless asked, no long self-testing loops.
- When done, stop and give a short plain list: what changed, what was skipped, anything that needs the owner's decision.
- Never touch onboarding, sign-in, payments or account deletion without the owner saying so in that request.
- Don't delete user data or change storage formats without saying so first.

## Gotchas
- Sending a request through the Claude connector opens its own Agent thread.
- Bundle id must be `com.issue11.app` (App Store).
