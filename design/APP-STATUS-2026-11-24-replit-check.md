# ISSUE11 Final · read-only Replit check · Nov 24, 2026
By 🩵 PRODUCT (Build Room). App: "ISSUE11 Final", replId 5ab9cbce-8aa9-40b5-ad7e-4bf21b96cafc. Read-only (list_app_files / read_app_file). Nothing in Replit was changed, sent, published or deployed. No secrets read.
Compared to: `drafts/replit/2026-11-21-final-signin-paywall-prompt.md` (sent Nov 21 02:33 UTC), `design/V1-LOGIC-SPEC.md`, `design/APP-STATUS-2026-11-19.md`, 1:1 design rule.
Files read: replit.md, artifacts/issue11/{package.json, app.json, app/_layout.tsx, app/(tabs)/index.tsx, issue.tsx, you.tsx, components/Editor.tsx}, artifacts/api-server/{package.json, src/routes/}. Not visually checked (no screenshots taken), so 1:1 match is not verified.

## Headline
**The Nov 21 update did not land.** None of sign-in, paywall, delete account, Download my issue or Your pace exists in the code. `replit.md` Scope still says "No onboarding flow, sign-in, paywall/payments, cloud database". Why is unknown (Replit may have stopped to ask for secrets, or the run was rolled back): Megan can see it in the Replit chat.

## Done
- 5 tabs + Focus, Maker, Reader, Write, Close-up screens (app/, app/(tabs)/).
- Inter Tight only (_layout.tsx), "The Editor" name, floating 11 with pulse (Editor.tsx).
- Local-only data, first name gate (_layout.tsx `FirstName`).
- AI consent before first use + on/off + Read my journal (Editor.tsx, you.tsx).
- 988 crisis stop on app side (Editor.tsx `CrisisPanel`, lib/safety.ts).
- Bundle id com.issue11.app (app.json). Notifications asked when a reminder is turned on, not at launch (you.tsx `setReminder`).
- Print at 40: "Order my print · $29.99" opens issue11.app, "I've ordered it" archives (issue.tsx).

## Partly done / wrong
- AI copy names **Anthropic Claude and Replit** to users (Editor.tsx consent + "How we use your data" + links to anthropic.com/replit.com privacy; label "Your Editor · Claude"; issue.tsx title consent; you.tsx AI + Privacy). Breaks Megan's Nov 21 rule ("an AI provider").
- Privacy / Terms are in-app "Provisional summary · not the final legal policy" text, not links to issue11.app/privacy and /terms (Apple 5.1.1 + 2.1 risk). Privacy text says "There is no account" and "Order your print to keep your issue".
- Membership row is display-only: "For display only. Nothing is charged in the app." (you.tsx).
- App icon row: "Placeholder only" (Apple 2.1 risk).
- "Weeks showing up" still on Home and You (spec: "Actions done").
- Photo purpose string is "Choose photos for your issue and journal." (spec wording differs; fine for Apple, align anyway).

## Missing
- Sign in with Apple + email code (no Supabase / expo-apple-authentication packages; no CP1 screen).
- Paywall + 7-day trial, Restore, Manage membership (no RevenueCat package; no CP2).
- Delete account + Sign out (CP3/CP4; api-server has only editor.ts + health.ts routes).
- Download my issue (PDF) (no print/share packages).
- Your pace (Daily/Weekly/Monthly): Home, Focus, You, reminders all fixed to weekly.
- UIBackgroundModes audio (sessions stop when the phone locks).
- Unused **expo-location** package is installed (permission risk; app never uses location).

## Not checked
- Visual 1:1 vs Megan's references (needs screenshots per design/VISUAL-QA.md).
- Whether the Nov 20 Home masthead (design/site-screens/15-home-v2-full.png) matches: Home uses a supplied cover image + "01–04" sections; looks close in code, unverified on screen.
- Onboarding V3 is not in Final (out of scope since Nov 20; launch order is Sign in → Paywall → name → Home as approved).

## Next
Draft: `drafts/replit/2026-11-24-next-update-DRAFT.md` (re-send of the approved Nov 21 prompt + 10 fixes). Waits on Megan's "send" and her keys in Replit Secrets.
