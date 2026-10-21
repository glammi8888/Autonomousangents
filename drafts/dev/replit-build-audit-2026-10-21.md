# Replit build audit · ISSUE11 iPhone app · Oct 21, 2026
Read-only audit for 🩶 OPS Manager. Only list/read of Replit files was used: no prompts, no publish, no credits. Compared against design/V1-SIMPLIFIED.md (top block), drafts/replit/02b, 01-design-system, V4-TOKENS, ONBOARDING-V3, PRINT-PURCHASE. App: replId 3804b1fa…, `artifacts/issue11`. I skimmed about 20 of the 45 screen files. The rest are judged by file name only.

## 1. Stack and structure
- **App:** Expo SDK 57 / React Native 0.86 with expo-router, in a pnpm workspace. `app/(tabs)/` has 5 tabs (index=Home, world=Explore, create=Issue, scribe=Journal, profile=You) plus a hidden `listen`. 40+ stack screens sit in `app/`. Other folders: `components/` (home, explore, issue, lucky, launch, onboarding), `constants/` (colors, strings, explore-strings, launch-features flags), `data/` (sample sessions, visuals, pages), `state/` (IssueProvider, which saves to AsyncStorage on the phone, plus SessionPlayback), and `tests/` (3 node tests).
- **Not wired yet:** sign-in (onboarding "Save your Issue" shows disabled Apple/email buttons), payments (paywall says "Pricing will be shown when billing is connected"), AI ("LOCAL REPLY PREVIEW · NOT CONNECTED TO CLAUDE"), cloud database, account deletion. No API keys or secrets in the files I read. The dev script only refers to Replit's own env variable by name (`REPLIT_EXPO_SESSION_SECRET`).
- **Wired:** local notifications (expo-notifications), photo picker, demo audio (expo-audio).
- **`artifacts/api-server`:** an Express 5 + Postgres/Drizzle template. Its only route is `health`, and it needs `DATABASE_URL`. The app does not use it yet. `replit.md` is still the unfilled template. There is also `artifacts/mockup-sandbox`.
- **Publish setup:** `.replit` has an autoscale web deployment. There is no EAS/App Store setup, and `app.json` has **no `ios.bundleIdentifier`** (it should be `com.issue11.app`).

## 2. V1 vs build
| V1 screen / feature | Status | Notes |
|---|---|---|
| Onboarding (ONBOARDING-V3) | ✅ | All 38 screens plus the 37b pop-up, in the locked order and copy. Paywall, sign-in and AI are honest "preview" stubs. There is 1 extra screen at the end ("Your first Issue starts here" + START AGAIN) that is not in V3. |
| First-open cover reveal | ✅ | Red sticker peel (FirstOpenGate/Reveal), shown once. |
| Home (long page) | 🟡 | Has the masthead, sticky header, cover with 40 ticks, move card with pink glass "I made room for it", resume capsule, flashback, saves strip, latest pages, and the "That's today" ending. Story rings are switched off by a flag (`homeStories:false`), in line with the Oct 19 launch scope. |
| Explore + player | ✅ | Search, chips (For you · Sessions · My Saves · 5/10 min · topics), Spotify-style shelves, mixed grid, Make a page, add photo. Tapping a session goes **straight to Now Playing** with a mini player. Demo audio only. |
| Issue reader / ready to print / order | 🟡 | Has the Issue tab, a 40-slot grid, reader, ready-to-print (locked under 40 pages), and an order screen with $29.99, 3 shipping options, the PO-box rule and estimate notes (matches PRINT-PURCHASE), plus order status. No Apple Pay, address or payment (correct for now). The main buttons are black ink rectangles, not pink glass. |
| Journal | ✅ | Live pull quote, "You're writing page x of 40", Another look, Keep page, private entries. There is only one fixed prompt, and swiping for another prompt is missing. |
| You + settings | 🟡 | Has the full row list (proof, shelf, membership, notifications, Lucky Star & AI, help, privacy, terms, sign out, delete). Most rows open a generic `account-info` preview page. |
| Lucky Star A–G | 🟡 | A guide ✅ · B hold to talk 🟡 (voice preview, no mic) · C one-card answer 🟡 (**shows a chat thread of the last 6 messages, but the rule is one card, never a thread**) · D curate (ADD ALL 3) ✅ · E picked session ❌ (says "NO SESSIONS ADDED YET" even though Explore has demo sessions) · F kept + UNDO ✅ · G AI off ❌ (no on/off switch found). It is full-screen everywhere, not a half sheet. There is no pink dot, and the labels use old names ("In Scribe", "Listen", "Curate"). Crisis words stop it and show 988 ✅. The full red safety screen exists (`safety.tsx`, not checked). |
| Floating 11 | ✅ | On every screen after onboarding. It can be dragged, remembers its position, opens on tap and starts voice when held. It does not snap to the nearest edge. |
| Delete account | 🟡 | Placeholder only ("not available in this preview"), which is honest. It must be real before submitting to Apple (5.1.1(v)). |
| System states | 🟡 | Loading, offline, a storage error banner and empty states exist. A friendly error screen exists (ErrorFallback, not checked). |
| Design system | 🟡 | Archivo Black, Archivo Narrow and IBM Plex Mono are loaded ✅. Ink, pink, blush and cream colors ✅. The glass tab bar uses a blur on iOS ✅. But red #D40806 and the greys are not in `colors.ts`, screens hard-code many hex values, `destructive` is #B34146 (off-brand), and pink glass capsules appear only on Home. |

## 3. Possible conflicts with locked rules
- **Streaks:** `app/streak.tsx` exists, but it is turned off by a flag (it redirects) and its copy says "NO STREAK TO PROTECT". The onboarding Day-1 week row is part of locked V3, so it is OK. No to-do lists, stats or invented claims found. Paywall and print copy say "preview/sample" honestly.
- **Session detail screen** (`app/session.tsx`, Spotify album page) still exists. The Explore feed bypasses it, so it is probably unused. Remove it if Megan has cut it.
- **Removed screens still in the code:** `eyes-closed.tsx`, `how-do-you-feel.tsx`, `listen.tsx`/(tabs)/listen, `ritual.tsx`, `progress.tsx` (Megan cut the Listen and "How do you feel" screens on Oct 15). I didn't check whether anything still links to them.
- **Onboarding** matches V3 apart from the extra "end" screen. Keep it or remove it only with Megan's OK.
- **Keys:** none found. **Publishing:** only a Replit web deployment config. Nothing for App Store or TestFlight.
- **App Store risks:** no bundle id. No iOS photo-library permission text in `app.json`, which the picker needs. `expo-location` is installed but looks unused, which would raise a permission flag. Background audio is off (`enableBackgroundPlayback:false`), but V1 says audio keeps playing when the phone is locked.

## 4. Next Replit prompts (this week: 5 tabs + tappable 11)
1. Clean-up: delete the screens Megan cut (session, eyes-closed, how-do-you-feel, listen, ritual, progress, streak) and any links to them, without changing onboarding.
2. Lucky Star: show a single answer card instead of the chat thread, make it a half sheet inside the tabs (full screen on Home), pick a demo session in Explore, add the "Lucky Star & AI" off state, and rename the labels to Journal/Explore/My saves.
3. Design pass: move red, the greys and all hard-coded colors into one theme file, and make the main actions pink glass capsules (Issue tab, Lucky Star, You).
4. Small fill-ins: swipe for another Journal prompt, snap the 11 to the nearest edge, and replace the You rows that open the generic `account-info` page with sample pages for Membership, Notifications and Lucky Star & AI.
⚠️ Oct 21, Megan: the magazine page and Journal page designs are not final ("Also the app design isn't finalized either for the \"magazine page\"" + "and \"journal\" pages"). Changes 2–4 must not restyle magazine pages or the Journal screen; the Journal prompt swipe in change 4 waits for her final Journal design.
5. App setup (next week, before TestFlight): set `ios.bundleIdentifier` to `com.issue11.app`, add the photo-library permission text, remove expo-location, and turn on background audio. Sign-in and RevenueCat need Megan's spec approval first (CLAUDE.md rule 4).
