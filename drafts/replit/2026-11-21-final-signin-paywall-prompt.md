# Replit · ISSUE11 Final · sign-in, paywall, delete account (CP1–CP4)
Approved by Megan, Nov 20, 2026 (LA), word for word: "Yes I approve" (to: Supabase + RevenueCat; order Sign in → Paywall → name → Home; journal/photos stay on the phone, the account holds membership + name only). Spec: drafts/dev/signin-payments-spec-v1.md (prices updated Nov 7). Send ONLY after the 1:1 design pass is finished, and after Megan has created the accounts below (keys go into Replit Secrets by Megan, never into chat or code).

## Prompt to paste

Add the App Store requirements from my design (screens CP1–CP4), replicated 1:1 like every other screen. Reference images: Sign in https://framerusercontent.com/images/  (CP1 image: open my canvas export when provided) · use the existing design system. Keep it lean: no long testing loops; stop and list what changed, what's left, and which secrets you still need.

Order on first open: Sign in (CP1) → Paywall (CP2) → "What should we call you?" → Home. Returning signed-in members go straight to Home.

ACCOUNTS (Supabase): Sign in with Apple first (native, Expo), "Continue with email" second (one-time email code), plus a Terms and Privacy line. The account holds only the membership link and first name. Journal entries, pages, photos and saves stay on the phone (local storage) exactly as now. Row-level security on every table. Supabase URL and publishable key come from Replit Secrets; the service-role key only in the api-server, never in the app.

PAYWALL (RevenueCat + Apple in-app purchase): Yearly $69.99 with a 7-day free trial (pre-selected), Monthly $9.99, founding offer $39.99 for the first year as an introductory offer. Prices load live from the App Store via RevenueCat (never hard-coded). Show price, period, trial terms, auto-renew and how to cancel, "Restore purchases", Terms (Apple standard EULA) and Privacy links, Close. One entitlement "member" unlocks the app. Membership row in You: "Manage membership" (Apple subscriptions) and "Restore purchases".

DELETE ACCOUNT (CP3/CP4, from You › Delete account): explain what gets deleted and that it doesn't cancel the membership, with a "Manage subscription" link; "Delete my account" (destructive red) → server deletes the Supabase user and their row, revokes Sign in with Apple, deletes the RevenueCat customer, and the app wipes this account's local data → "Account deleted" → Close → Sign in. If any step fails: "We couldn't finish. Try again." and retry completes it. Add "Sign out" in You (keeps local data on this phone for the same account).

Do not: use Replit Auth or Replit Postgres for user data, put any key in code or chat, add in-app payment for prints (prints stay on issue11.app), or change onboarding.
