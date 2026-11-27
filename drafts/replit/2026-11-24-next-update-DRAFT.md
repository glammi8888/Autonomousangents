# DRAFT · Replit · ISSUE11 Final · next update (Nov 24, 2026)
Status: **DRAFT. Not sent.** Sending needs Megan's OK (one consolidated update; sign-in, payments, account deletion and user data need her explicit approval under CLAUDE.md rule 4). Her Nov 20 "Yes I approve" covers the Nov 21 spec; the new fixes in Part B are small, but she still says "send" before anyone sends it.
> 🔴 **CHANGE Nov 27 (Megan, word for word: "No just remove sign in because it makes people bounce"): NO sign-in, NO accounts.** Before sending, rewrite PART A without: Sign in with Apple, email code, Supabase auth, account table, Sign out, Delete account. Keep: paywall (RevenueCat, StoreKit) with 7-day trial on yearly, **Restore purchases**, Manage membership, Download my issue, Your pace (+ Every 3 days), Apple checklist fixes. All data stays on the phone. Secrets needed shrink to: EXPO_PUBLIC_REVENUECAT_IOS_KEY (+ REVENUECAT_SECRET_API_KEY only if the server checks entitlements). Privacy text: "no account" is now TRUE, keep it accurate. Apple 5.1.1(v): no account = no account-deletion requirement.

Written by 🩵 PRODUCT (Build Room). Evidence: read-only check of replId 5ab9cbce-8aa9-40b5-ad7e-4bf21b96cafc on Nov 24, gap list in `design/APP-STATUS-2026-11-24-replit-check.md`.

**Why a re-send:** the Nov 21 prompt (`drafts/replit/2026-11-21-final-signin-paywall-prompt.md`, sent 02:33 UTC Nov 21) did not land in the code at all. No auth, payment or PDF packages, no new screens, `replit.md` still says "No sign-in, paywall/payments". So Part A is that same approved prompt, unchanged. Part B adds the fixes found today.

**Before sending (Megan):** put the keys into Replit Secrets first (names below), or Replit may stop and ask again. The prompt tells it not to stop if one is missing.

---

## Prompt to paste (one message)

My Nov 21 request (sign-in, paywall, delete account, Download my issue, Your pace, Apple checklist) is not in the code yet: there are no auth, purchase or PDF packages and no new screens. Please build all of it now, in this order, then stop and give me one short list: what changed, what's left, which secrets are still missing. Keep it lean, no long testing loops. Replicate my screens 1:1 like every other screen; do not redesign anything that already exists.

If a secret is missing, still build the code that reads it from Replit Secrets by name, show a calm "Not set up yet" state instead of crashing, and list the missing name at the end. Never put a key in code or chat.

**PART A · build the Nov 21 request exactly as written.** (Paste the full "Prompt to paste" section of `drafts/replit/2026-11-21-final-signin-paywall-prompt.md` here, unchanged: CP1–CP5 image links, order on first open, ACCOUNTS, PAYWALL, DOWNLOAD MY ISSUE, DELETE ACCOUNT, YOUR PACE, Do not, APPLE COMPLIANCE CHECKLIST, FIXES TO EARLIER WORK.)

Secret names (Megan enters the values in Replit Secrets):
- App: EXPO_PUBLIC_SUPABASE_URL, EXPO_PUBLIC_SUPABASE_ANON_KEY, EXPO_PUBLIC_REVENUECAT_IOS_KEY, EXPO_PUBLIC_API_URL
- api-server only: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, REVENUECAT_SECRET_API_KEY, APPLE_TEAM_ID, APPLE_KEY_ID, APPLE_SIGNIN_PRIVATE_KEY
(Stripe and print-order keys are not needed in this update: prints stay on issue11.app.)

**PART B · fixes found in the current code (do these in the same pass):**
1. Never name the AI service to users. Replace every user-facing "Anthropic", "Claude" and "Replit" in the app with "an AI provider": the consent sheet and "How we use your data" (components/Editor.tsx), the source label "Your Editor · Claude" → "Your Editor", the issue-title consent and "Suggested by your Editor · Claude" (app/(tabs)/issue.tsx), You › The Editor & AI and You › Privacy (app/(tabs)/you.tsx). Remove the "Anthropic privacy" and "Replit privacy" links; link "How we use your data" to https://issue11.app/privacy instead. Backend stays as is.
2. Privacy and Terms in You: remove the "Provisional summary · not the final legal policy/terms" labels and the summary text; each row opens the real page (https://issue11.app/privacy, https://issue11.app/terms). Remove "There is no account and no cloud copy" and "Deleting the app deletes your data. Order your print to keep your issue." (no longer true once accounts and Download my issue exist).
3. Membership row: replace the display-only price list and "For display only. Nothing is charged in the app." with the real membership state from RevenueCat, plus "Manage membership" and "Restore purchases" (as in Part A). The right-hand label shows the real plan, not a fixed "Yearly". Printed copies $29.99 stays as a link to issue11.app.
4. App icon row: it says "Placeholder only". Hide the App icon row for this build (Apple rejects placeholder content).
5. "Weeks showing up" → "Actions done" everywhere it shows: Home Focus done label ("Done this week · Week [n] showing up") and the You header line. With Your pace, the Home label follows the pace ("Done today" / "Done this week" / "Done this month").
6. Home and Focus labels follow Your pace ("Today's action" / "This week's action" / "This month's action", "Pick today's / this week's / this month's action", "Set for tomorrow / next Monday / the 1st"). Help text in You follows the pace too.
7. Notifications: the "Weekly action · Mondays at 9:00" switch follows the pace (Daily 9:00 / Monday 9:00 / the 1st at 9:00). The right-hand label on the Notifications row shows the real time.
8. Remove the unused expo-location package and plugin (the app never asks for location; an unused location permission is an App Store risk).
9. app.json: photo library purpose string exactly "Add your own photos to your pages and journal"; add UIBackgroundModes audio so sessions keep playing when the phone locks.
10. Update replit.md so it matches what's now built (sign-in, paywall, delete account, Your pace, "an AI provider"); remove "No onboarding flow, sign-in, paywall/payments, cloud database" from Scope, keep "No onboarding flow" and "No widgets".

**Do not:** change onboarding, the magazine templates or page layouts, any approved screen design, prices in code, or add in-app payment for prints.

---

## Notes for Megan (not part of the prompt)
- Copy check done: "you" only, "action" only, no "becoming her", "an AI provider", no outcome promises.
- Part A is the prompt you approved Nov 20. Nothing new in auth, payments or deletion was added; Part B only removes wrong text, placeholders and an unused permission.
- Expo Go can't test Sign in with Apple or purchases. The Nov 30 TestFlight build is the first real test of them (sandbox tester account needed in App Store Connect).
- Magazine template logic (design/magazine/TEMPLATE-LOGIC.md) is still waiting on you and is not in this update.
