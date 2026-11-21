# Replit · ISSUE11 Final · sign-in, paywall, delete account (CP1–CP4)
Approved by Megan, Nov 20, 2026 (LA), word for word: "Yes I approve" (to: Supabase + RevenueCat; order Sign in → Paywall → name → Home; journal/photos stay on the phone, the account holds membership + name only). Spec: drafts/dev/signin-payments-spec-v1.md (prices updated Nov 7). Send ONLY after the 1:1 design pass is finished, and after Megan has created the accounts below (keys go into Replit Secrets by Megan, never into chat or code).

## Prompt to paste

Add the App Store requirements from my design (screens CP1–CP4), replicated 1:1 like every other screen. Reference images (replicate 1:1): CP1 Sign in https://framerusercontent.com/images/DSVlNdWDZRxjBK5W9YcCaVroK4.jpg · CP2 Paywall https://framerusercontent.com/images/T55qjn59CtH6GL8D6fTW3qnktY.jpg · CP3 Delete account https://framerusercontent.com/images/unbGTDaVqgEkRWqR8LAeQCbtI.jpg · CP4 Account deleted https://framerusercontent.com/images/no1LaTADV8a7idLgxytjj2rbnQ4.jpg · CP5 AI consent https://framerusercontent.com/images/qBCRp1c5eVH0jVg6kIpVJpkGeg.jpg Keep it lean: no long testing loops; stop and list what changed, what's left, and which secrets you still need.

Order on first open: Sign in (CP1) → Paywall (CP2) → "What should we call you?" → Home. Returning signed-in members go straight to Home.

ACCOUNTS (Supabase): Sign in with Apple first (native, Expo), "Continue with email" second (one-time email code), plus a Terms and Privacy line. The account holds only the membership link and first name. Journal entries, pages, photos and saves stay on the phone (local storage) exactly as now. Row-level security on every table. Supabase URL and publishable key come from Replit Secrets; the service-role key only in the api-server, never in the app.

PAYWALL (RevenueCat + Apple in-app purchase): Yearly $69.99 with a 7-day free trial (pre-selected), Monthly $9.99, founding offer $39.99 for the first year as an introductory offer. Prices load live from the App Store via RevenueCat (never hard-coded). Show price, period, trial terms, auto-renew and how to cancel, "Restore purchases", Terms (Apple standard EULA) and Privacy links, Close. One entitlement "member" unlocks the app. Membership row in You: "Manage membership" (Apple subscriptions) and "Restore purchases".

DOWNLOAD MY ISSUE: unlocks when an issue reaches 40 of 40 pages, then available anytime for every finished issue. Add "Download my issue (PDF)" on the print screen next to "Order my print", in the Issue reader's Share sheet, in You › My Issues, and on the Delete account screen above "Delete my account". It builds a PDF of the cover and all kept pages in order on the phone (no upload) and opens the iOS share sheet.

DELETE ACCOUNT (CP3/CP4, from You › Delete account): explain what gets deleted and that it doesn't cancel the membership, with a "Manage subscription" link; "Delete my account" (destructive red) → server deletes the Supabase user and their row, revokes Sign in with Apple, deletes the RevenueCat customer, and the app wipes this account's local data → "Account deleted" → Close → Sign in. If any step fails: "We couldn't finish. Try again." and retry completes it. Add "Sign out" in You (keeps local data on this phone for the same account).

YOUR PACE (new logic, approved by the owner): users choose how often they get an action: Daily, Weekly (default) or Monthly. Data stays on the phone.
- Where: the first time Focus opens (before the FC1 pick), a small "Your pace" sheet with three options: Daily · Weekly · Monthly. Build it in the same style as the Focus 3 "Not yet" sheet (https://framerusercontent.com/images/FEHUtOq09cEBJVuvu6rNxXDTDWQ.jpg): same fonts, colors, spacing and buttons. Also add a "Your pace" row in You (above Notifications) that opens the same sheet. A change starts with the next day, week or month. Do not change onboarding.
- One action per period: Daily = a new action each day (can be different every day), Weekly = one action each Monday, Monthly = one action on the 1st.
- Home: the action label follows the pace: "Today's action" · "This week's action" · "This month's action". I did it / Not yet work as now.
- Focus: the FC1 pick opens at the start of each period. "Keep it for next week" reads "Keep it for tomorrow" / "Keep it for next week" / "Keep it for next month". "Make it smaller" unchanged.
- Progress: replace "Weeks showing up" with "Actions done": a total of done actions that never resets. No streaks, no guilt copy, missing a period changes nothing.
- Issue: unchanged; any done action can become a page via "See my page".
- The Editor: with AI consent, fresh action suggestions each period; without consent or offline, a fixed list of about 30 suggestions per topic, never repeating a recent one.
- Reminders follow the pace: Daily 9:00, Weekly Monday 9:00, Monthly the 1st at 9:00; quiet hours 22:00–7:00 still apply; all can be turned off in Notifications.

Do not: use Replit Auth or Replit Postgres for user data, put any key in code or chat, add in-app payment for prints (prints stay on issue11.app), or change onboarding.

APPLE COMPLIANCE CHECKLIST (all must pass; list any that can't and why):
- 4.8 Sign in with Apple offered first whenever email login is offered; Apple's official button style.
- 3.1.1 / 3.1.2 Subscriptions only through Apple in-app purchase. Paywall shows price, length, trial terms, auto-renew + how to cancel, Restore purchases, Terms (EULA) and Privacy links that open real pages, and a visible Close. No pricing typed into the app.
- 5.1.1(v) Account deletion inside the app, reachable from You, deletes the account and its data, revokes Sign in with Apple, and says it doesn't cancel the subscription with a Manage subscription link.
- 5.1.2(i) AI consent before any data goes to the AI (CP5), saved, and changeable in You > The Editor & AI.
- 5.1.1 Privacy policy link in the app (You > Privacy) and on the paywall: https://issue11.app/privacy. Terms: https://issue11.app/terms.
- Permission prompts have clear purpose strings: photo library ("Add your own photos to your pages and journal"), notifications (asked when the user turns a reminder on, not at launch). Remove any permission the app doesn't use.
- 2.1 No placeholder, demo or "coming soon" content in the review build; sample content clearly reads as examples. App must not crash on first launch or with no network.
- Age rating: 16+.
- Bundle id com.issue11.app.
- Background audio on for sessions (UIBackgroundModes audio) so sessions keep playing when the phone locks.
- Crisis safety stop (988) kept.
- Review notes: provide a way for Apple to test the paywall (sandbox) and the Editor.

FIXES TO EARLIER WORK:
- AI consent (CP5) and all app copy: say "an AI provider". Never name Anthropic, Claude or any other service anywhere the user can see (replace "Anthropic Claude" wherever it appears, including replit.md's Editor section wording shown to users). The backend integration stays as is.
- Delete account copy (CP3): "This can't be undone. Download your issue first if you'd like to keep it. Then everything below is permanently deleted from this phone and our servers." On this screen only, the download works even before 40 pages.
