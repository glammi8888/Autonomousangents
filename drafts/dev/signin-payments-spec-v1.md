# ISSUE11 · Sign-in + payments spec v1 · DRAFT for Megan's approval
Planner · 2026-10-30 · Nothing built, nothing installed, no keys read. Replaces nothing; `.pipeline/spec.md` stays a reference checklist.
**Why this needs your OK before building:** it touches Authentication · Payments · RevenueCat/subscriptions · User data · Account deletion · API keys/secrets · Database changes (CLAUDE.md Production Safety Rule 4).
**Sources read:** CLAUDE.md, .pipeline/lessons.md, design/PRODUCT-ARCHITECTURE.md, design/V1-SIMPLIFIED.md, design/ONBOARDING-V3.md (locked), design/PRINT-PURCHASE.md, research/paywall-notes.md, drafts/dev/replit-backend-recommendation.md, drafts/dev/replit-build-audit-2026-10-21.md, .pipeline/app-store-checklist.md, .pipeline/spec.md + acceptance-criteria.md (sections B and E reused).
**Not verified live this session:** Apple, RevenueCat, Stripe, Supabase, Lulu and Replit docs. Every "(verify)" below is a fact that changes and must be checked at build start.

**Loop stage:** none directly. This is the trust layer that lets her keep her Issue (EMBODY → BECOME over a quarter) and hold the printed magazine at the end. It passes Megan's test only because without it there is no paid app and no print.

---

## 0. Scope in one look
| In this spec | Not in this spec (own spec later) |
|---|---|
| Sign in with Apple + email code, sign-in placement, sign-out | Syncing journal pages, wall and photos to the cloud (old spec sections C/D) |
| Subscription paywall (screen 37), downsell (37b), restore, manage, lapsed paywall | AI calls (design/magazine-ai-spec.md) |
| Print order checkout + payment + order status | Making the print-ready PDF of the 40 pages (**biggest open launch risk, see section 7**) |
| In-app account deletion | Onboarding copy or order (locked, untouched) |

---

## 1. Logic per flow (what she sees · what she can do · where it goes · underneath)

### 1.1 Opening the app (the router)
- **Sees:** the right screen for where she is. Nothing new to look at.
- **Underneath, checked in this order every launch:**
  1. Signed in + active membership → Home.
  2. Signed in + no active membership → the paywall again (V1 screen 14, "same locked paywall").
  3. Not signed in + active membership (she paid but closed the app before screen 38) → screen 38 "Save your Issue".
  4. Not signed in + finished onboarding before → paywall 37 with her cover (her answers stay on the phone, she never redoes onboarding).
  5. Otherwise → onboarding screen 1 (current build behavior unchanged).
- **Offline at launch:** use the last known state stored on the phone; never lock her out of an active membership because of no signal.

### 1.2 Where sign-in sits relative to the locked onboarding
- **Already in the locked flow:** screen 38 "Save your Issue · Sign in with Apple / email, after purchase so nothing she made is lost". This spec only wires it. Order stays 36 → 37 paywall → (37b) → 38 sign-in → first-open cover reveal → Home.
- **Sign-in is required on screen 38** (no skip). Reason: her Issue, print orders and deletion are account-based. (verify: App Review 5.1.1(v) allows required login when the app has significant account-based features; we argue journal + print orders + Issue history qualify.)
- **⚠️ Touches locked onboarding (Question 1):** returning users (new phone, reinstall, after sign-out) have no way in except redoing 36 screens. Proposed: one small text link on screen 1, "Already have an Issue? Sign in", opening the same sign-in screen with the title "Welcome back". Nothing else in onboarding changes.
- **Truth check on screen 38's promise "nothing she made is lost":** with this spec her profile and onboarding answers go to the cloud; her pages and photos stay on the phone until the content-sync spec ships. Same phone = nothing lost. New phone = only true after content sync. Content sync must ship before the App Store build.

### 1.3 Sign in with Apple (main button)
- **Sees:** Apple's black "Sign in with Apple" button (Apple's official style), then Apple's own sheet (Face ID).
- **Can do:** sign in, or share/hide her email (Apple's "Hide my email").
- **Goes to:** the first-open cover reveal → Home. Cancelling the Apple sheet returns to screen 38 with no error.
- **Underneath:** native Apple sign-in on the phone → Apple's identity token goes to Supabase → Supabase account created or found. Her app account id is then linked to her RevenueCat purchase (so the membership she just bought belongs to her account). Her name from screen 2 and her onboarding answers are saved to her profile.

### 1.4 Email code (second option) · recommended, reason
- **Why keep it:** screen 38 is locked and already shows "Apple / email"; it also gives her a way in from a non-Apple device later and is a familiar fallback. Cost $0.
- **Sees:** "Continue with email" → type email → "We sent a 6-digit code" → type code.
- **Can do:** resend code after 60 s, change email.
- **Goes to:** same as Apple. Wrong code: "That code didn't work. Try again." stays on screen.
- **Underneath:** Supabase email one-time code (no password, nothing to forget). Needs a real email sender (Resend free tier, set up inside Supabase) because Supabase's built-in sender is for testing only and heavily rate-limited (verify limits).

### 1.5 Subscription paywall (screen 37) + downsell (37b) + restore
- **Sees (locked design, one screen, no scroll):** her cover, the plan(s) with price, renewal period and trial terms in plain words, START MY ISSUE, and under the button "Cancel anytime · Restore · Terms · Privacy".
- **Can do:** buy, close (→ 37b pop-up), restore, open Terms / Privacy.
- **Goes to:** purchase success → screen 38. Close → 37b "WAIT · A BETTER OFFER, JUST FOR YOU" → claim → Apple sheet → 38; "No thanks" → back to the paywall without the pop-up (hard paywall: the app opens only with a membership, matching V1 screen 14). Her answers stay on the phone.
- **Restore:** "Restoring…" then either → 38 (or Home if signed in) or "We couldn't find a membership for this Apple ID." Never an error code.
- **Underneath:** prices and plans come live from the App Store through RevenueCat (never typed into the app), so Megan can change price in App Store Connect without an app update. One entitlement named `member` unlocks the app. Buying uses Apple in-app purchase (App Store rule 3.1.1).
- **Plans:** see Question 2. Known: Monthly $9.99. The locked paywall direction (Oct 8) was Yearly with a free trial pre-selected + Monthly without a trial; yearly price, trial length and 37b offer are still open.

### 1.6 Membership in You (manage, restore, lapsed)
- **Sees:** You → Membership: plan name, "Renews on <date>" or "Ends on <date>", Manage or cancel, Restore purchases, My print orders.
- **Manage or cancel:** opens Apple's own subscription page (cancellation always happens at Apple).
- **Lapsed:** next launch shows the paywall again with a small line under it: "Signed in as <email> · Sign out · Delete account" so she can always leave or delete (Apple requires deletion to be reachable).

### 1.7 Print order purchase (Issue tab, at 40 of 40)
- **Sees (existing design, design/PRINT-PURCHASE.md):** Ready to print → review 40 pages → "I love it · Approve my Issue" → Order screen: Issue 01 · 40 pages $29.99 · shipping choices · US address form · "$29.99 + tax" · estimate notes → **Apple Pay** button (and "Pay with card").
- **Can do:** pick shipping (Standard free, Expedited +$16, Express +$32; PO box/APO/FPO shows Standard + Priority +$10 only), enter address, pay.
- **Goes to:** order confirmation ("Placed · Printing takes 3–5 business days before shipping. Estimates, not guaranteed.") → Issue 01 moves to her shelf, Issue 02 starts (Megan, Oct 15). Order status lives in You → Membership → My print orders: Placed → Printing → Shipped → On its way.
- **Underneath:**
  - App Store rule: physical goods must NOT use Apple in-app purchase; they use Apple Pay or card (guideline 3.1.3(e) as I know it; verify; it's not yet on our checklist).
  - Payment by **Stripe inside the app** (native payment sheet with Apple Pay + card, no web page, as Megan asked). Card numbers never touch our servers or database.
  - **The server sets the price,** never the phone: it recalculates $29.99 + chosen shipping + sales tax, creates the order as "awaiting payment", then asks Stripe for the payment. Stripe tells the server when the payment succeeded (webhook) → order "paid". Only then does the app show "Placed".
  - Sales tax: Stripe Tax calculates it (adds a small per-order fee, verify). Who must collect tax where is an accountant question (section 5).
  - Fulfilment at launch: see Question 3 (manual Lulu order by Megan vs automatic Lulu API).
  - Double taps / retries never create two orders or two charges (one open order per Issue).

### 1.8 Sign-out
- **Sees:** You → Sign out → "Sign out of ISSUE11?" → Sign out.
- **Goes to:** the "Welcome back" sign-in screen with a small "New here? Start your Issue" link to screen 1.
- **Underneath:** ends the Supabase session, unlinks RevenueCat from her account on this phone, hides her local pages (kept on the phone under her account id, shown again when the same person signs back in on this phone; wiped only by deletion). Her subscription is not affected.

### 1.9 Account deletion (Apple requires it in the app, 5.1.1(v))
- **Sees (existing design, V1 screen 11):** You → Delete account → what gets deleted (her Issue, pages, photos, journal, generated Issues, profile) + "Deleting your account doesn't cancel your membership. Cancel it in your Apple subscriptions first." with a "Manage subscription" button → "Delete my account" (red) → for Apple users, Apple's sheet once more to confirm → "Deleting…" → "Your account is deleted." → screen 1.
- **Open print order:** the confirm screen says "Your print order already placed will still ship. We keep only the shipping address until it ships, then erase it."
- **Underneath (one server job, safe to retry if it stops halfway):**
  1. Check she is who she says (her login token).
  2. Apple users: tell Apple to revoke ISSUE11's access to her Apple ID (Apple requires this for Sign in with Apple apps on deletion; verify current wording).
  3. Delete her files in every storage folder `<her id>/`.
  4. Print orders: remove her account link and email; erase the address on finished orders now, and on open orders automatically when they ship. Amount, date and status stay, anonymous, for tax records (verify retention period with the accountant).
  5. Delete her RevenueCat customer record.
  6. Delete her login → every table row tied to her disappears (database cascade).
  7. Phone: wipe her local data, sign out, back to screen 1.
- She can't be half-deleted: if any step fails she sees "We couldn't finish. Try again." and retrying finishes the job.

---

## 2. Recommended stack (easiest first, then cheapest)
| Job | Pick | Why | Cost (verify) |
|---|---|---|---|
| Accounts + database | **Supabase** (already recommended Oct 20) | Native Apple sign-in for Expo, email code, per-user row security, admin delete. Replit Auth is web-redirect and I couldn't confirm in-app deletion. | Free to build; Pro ~$25/mo before outside testers (free projects pause) |
| Subscriptions | **RevenueCat** + Apple in-app purchase | Easiest correct way to Apple IAP in Expo; handles restore, receipts, renewals, sandbox. | Free until ~$2.5k monthly revenue, then ~1% |
| Print payment | **Stripe** native payment sheet (Apple Pay + card) + Stripe Tax | Apple Pay inside the app as Megan wants; no card data on our side. | ~2.9% + 30¢ per US card order; Stripe Tax ~0.5% |
| Server jobs (delete account, print checkout, Stripe webhook) | **Replit's existing `artifacts/api-server`** | Already in her Replit workspace; Replit Agent builds and deploys it; secrets in Replit Secrets. Supabase Edge Functions are cheaper but need a CLI deploy step Megan would have to run. | Replit deployment usage (check her plan) |
| Email codes + order emails | **Resend** connected to Supabase | Free tier covers launch. | Free to ~3k emails/mo |
| Print | **Lulu** (already chosen) | — | $16.75/issue incl. standard shipping (Megan, Oct 15) |
| Apple commission | **Apple Small Business Program** | 15% instead of 30% on subscriptions. Apply right after the Paid Apps Agreement. | Free |
**Don't use:** Replit Auth, Replit's own Postgres (`DATABASE_URL`) for user data, Stripe Checkout web pages, or Apple IAP for prints.

---

## 3. Build now (before the bank) vs waits for the bank
| Can be built and tested now (sandbox/test) | Waits for business bank → Apple Paid Apps Agreement / Stripe live |
|---|---|
| Bundle id `com.issue11.app`, App ID with Sign in with Apple | Real subscription products loading in sandbox/TestFlight (I believe StoreKit returns no products until the Paid Apps Agreement is active; verify) |
| Supabase project, tables, row security, Apple + email sign-in | Apple Small Business Program enrollment |
| Sign-out, account deletion incl. Apple revoke | Stripe live mode (payouts need the bank) |
| Paywall wired to RevenueCat (RevenueCat's Test Store / preview mode if available; verify) | Real Lulu orders (needs a payment card on Lulu) |
| Stripe test mode end to end (test cards, Apple Pay test) | App Store submission with paid products |
| Lulu sandbox order (if fulfilment is automatic) | |
**Deadline math:** submission ~Nov 28 needs ~2 weeks of real sandbox subscription testing → **bank open + Paid Apps Agreement active by ~Nov 14**. Apple can take a few days to activate it. This is the critical path.
**Testing note:** Apple sign-in, RevenueCat and Apple Pay need a real iPhone build (development build or TestFlight), not Replit's Expo Go preview. Apple sign-in inside Expo Go signs in as Expo's app, not ISSUE11, so Supabase will reject it. Plan the first TestFlight build early.

---

## 4. Acceptance criteria (PASS/FAIL, checked on a TestFlight/dev build on an iPhone unless marked)
**Router**
- AC-1 Fresh install → onboarding screen 1. Onboarding screens 1–37b keep the locked order and copy (diff check against design/ONBOARDING-V3.md); only the Question 1 link is new, and only if Megan approves it.
- AC-2 Paid but not signed in, kill + reopen → screen 38 (not onboarding, not paywall).
- AC-3 Signed in, membership expired (sandbox) → paywall with "Signed in as … · Sign out · Delete account".
- AC-4 Signed in + member, airplane mode, reopen → Home (no lock-out).
**Sign in with Apple**
- AC-5 Screen 38 → Apple → Face ID → cover reveal → Home. A `profiles` row exists with her id, cover name and onboarding answers.
- AC-6 Cancelling the Apple sheet returns to 38 with no error text.
- AC-7 "Hide my email" works (account created with the relay address).
- AC-8 Same Apple ID on reinstall signs into the same account (same profile row, no duplicate).
**Email code**
- AC-9 Invalid email shows an inline error and sends nothing; valid email sends a 6-digit code that arrives within 2 minutes from the ISSUE11 sender.
- AC-10 Correct code signs in; wrong code shows "That code didn't work" and stays; Resend is disabled for 60 s.
- AC-11 No network: friendly "No connection" message within 20 s, typed email kept.
**Paywall + restore**
- AC-12 Paywall shows the live App Store price, renewal period and trial terms (if any) before the button; "Cancel anytime · Restore · Terms · Privacy" visible without scrolling on a 375 pt-wide screen; Terms and Privacy links open real pages.
- AC-13 Sandbox purchase → screen 38; after sign-in, RevenueCat shows the purchase on her Supabase user id.
- AC-14 Close → 37b pop-up; "No thanks" → paywall without pop-up; app tabs not reachable without membership.
- AC-15 Restore on a fresh install with a sandbox subscription unlocks; restore with none shows the "couldn't find" message.
- AC-16 Grep: no price strings like "$9.99" hard-coded in paywall code; prices come from RevenueCat.
- AC-17 You → Membership shows plan + renew/end date; "Manage or cancel" opens Apple's subscription page.
**Print order**
- AC-18 Order button only active at 40 of 40 and after "Approve my Issue".
- AC-19 PO box / APO / FPO address hides Expedited and Express and shows Standard + Priority +$10; non-US address can't be submitted (US only at launch).
- AC-20 Total shown = server-calculated $29.99 + shipping + tax. Tampering with the request price (QA sends a modified amount to the API) does not change the charge.
- AC-21 Stripe test card / Apple Pay test succeeds → order "Placed" only after Stripe's webhook marks it paid; declined card shows a friendly error and no order is placed.
- AC-22 Double-tapping Pay or retrying after a dropped connection gives one order and one charge.
- AC-23 Confirmation shows the estimate wording from PRINT-PURCHASE.md (no promised date); Issue 01 moves to the shelf, Issue 02 starts.
- AC-24 Purchase never uses Apple in-app purchase; no card number is stored in Supabase (column check).
**Sign-out**
- AC-25 Sign out → "Welcome back" screen; reopening the app does not show her Home; signing back in on the same phone shows her pages again.
- AC-26 Sign-out does not cancel or change the subscription (RevenueCat check).
**Account deletion**
- AC-27 Delete screen states what is deleted and that the membership must be cancelled at Apple, with a working "Manage subscription" button.
- AC-28 Apple user: confirm → Apple sheet → deleted → screen 1. Afterwards: no `auth.users` row, no `profiles` row, no files under `<id>/`, RevenueCat customer gone, and the app no longer appears in her iPhone Settings → Apple ID → Sign in with Apple list (verify name of that list).
- AC-29 Email user: same result without the Apple step.
- AC-30 Cancel on the Apple sheet or the confirm screen deletes nothing.
- AC-31 Kill the network mid-delete → "We couldn't finish. Try again." → retry completes; no half-deleted state is reachable.
- AC-32 Open print order at deletion: order row keeps the address until marked shipped, then the address is erased automatically; finished orders lose name/address/email immediately; amounts stay.
- AC-33 Deleting and signing up again with the same Apple ID creates a fresh, empty account.
**Data security (reused from old spec section E)**
- AC-34 Row security on every table: with 2 test accounts, A cannot read or change B's profile or orders (API test with A's token).
- AC-35 The phone cannot insert or update `print_orders` directly (only the server can).
- AC-36 Grep of the app code and repo finds no secret key values; only the `EXPO_PUBLIC_*` names in section 5 are in the app. `SUPABASE_SERVICE_ROLE_KEY`, `STRIPE_SECRET_KEY`, `REVENUECAT_SECRET_API_KEY`, `APPLE_SIGNIN_PRIVATE_KEY` exist only in the api-server's Replit Secrets.
- AC-37 Every server route rejects calls without a valid Supabase login token (401), except the Stripe webhook, which rejects bad signatures (400).

---

## 5. Data stored + privacy
| What | Where | Why | On deletion |
|---|---|---|---|
| Apple user id, email (may be Apple relay), name if Apple shares it | Supabase Auth | Login | Deleted |
| `profiles`: cover name, age range, onboarding answers | Supabase table (row security: own row only) | Her Issue | Deleted (cascade) |
| Pages, wall, photos | On her phone (cloud sync = next spec) | Her Issue | Wiped from phone; cloud copies covered by the same `<id>/` + cascade rule |
| Subscription status, Apple receipts | RevenueCat (linked to her id) | Membership | Customer deleted (Apple keeps its own purchase records) |
| `print_orders`: name, US address, phone (verify Lulu requires it), email, shipping choice, amounts, tax, status, Stripe payment id, Lulu job id, tracking | Supabase table (she reads own; only the server writes) | Shipping + tax records | Address/email/link erased (open orders: when shipped); anonymous amounts kept for tax |
| Card / Apple Pay data | Stripe only | Payment | Stripe keeps payment records as required by law |
| Shipping address | Also Lulu | Printing | Lulu keeps its order records (check their privacy terms) |

**Tables (Megan runs the SQL in the Supabase SQL editor herself; no agent applies it):** `profiles` (id = login id, cascade delete), `print_orders` (user_id nullable, set null on account deletion; trigger erases address when status becomes shipped and user_id is empty; unique Stripe payment id; one open order per Issue). Row security on both. No subscription table (RevenueCat is the source of truth).
**Secrets, by name only (never in the app, chat or repo):**
- App (public by design): `EXPO_PUBLIC_SUPABASE_URL`, `EXPO_PUBLIC_SUPABASE_ANON_KEY`, `EXPO_PUBLIC_REVENUECAT_IOS_KEY`, `EXPO_PUBLIC_STRIPE_PUBLISHABLE_KEY`, `EXPO_PUBLIC_API_URL`.
- api-server only (Replit Secrets): `SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `REVENUECAT_SECRET_API_KEY`, `APPLE_TEAM_ID`, `APPLE_KEY_ID`, `APPLE_SIGNIN_PRIVATE_KEY`, `RESEND_API_KEY`, (`LULU_CLIENT_KEY`, `LULU_CLIENT_SECRET` only if fulfilment is automatic).
- In dashboards, not Replit: Resend SMTP login (inside Supabase), Apple In-App Purchase key (inside RevenueCat), Apple Pay certificate (inside Stripe).
**App Store privacy label (to declare):** Contact info (email, name, physical address, phone), User content, Purchases, Identifiers (user id), Other data (age range). All linked to her, none used for tracking → no tracking prompt.
**Privacy policy must name:** Supabase, RevenueCat, Stripe, Lulu, Resend, Apple; what each gets; deletion behavior above.

---

## 6. What Megan decides (3 questions) and sets up (in order)
**Q1. Returning users: add one small link "Already have an Issue? Sign in" on onboarding screen 1?** (touches locked onboarding)
Recommend **yes**: without it someone on a new phone redoes 36 screens before she can sign in; that's the most likely 1-star review.
**Q2. Plans at launch?** Known: Monthly $9.99. Open since Oct 8: yearly price, trial, 37b offer.
Recommend **Monthly $9.99 (no trial) + Yearly $59.99 with a 7-day free trial, pre-selected** (≈$5/mo, same as I am; Calm is $79.99) and **37b = Yearly $39.99 for the first year**. Your price call; 💛 Revenue can check it.
**Q3. Print fulfilment at launch: you place each paid order on Lulu yourself, or fully automatic through Lulu's API?**
Recommend **manual for launch**: you get a "New paid order" email with the address and print file; about 5 minutes per order on Lulu's site, then you mark it shipped. Fewer keys, fewer things to break before Nov 28. Automate in V1.1 once orders are steady.
*(Defaults I picked, tell me if wrong: hard paywall, i.e. the app needs a membership, per V1 screen 14 · sign-in required on screen 38 · email code kept because locked screen 38 shows it · US-only print.)*

**Megan sets up, in this order (never paste keys into chat; Replit Secrets or the provider's dashboard only):**
1. **Business bank account** → then immediately **App Store Connect → Agreements, Tax and Banking → Paid Apps Agreement** (critical path, target Nov 14) → Apple Small Business Program.
2. **Apple Developer** (if not done: enrollment; organization needs a D-U-N-S number): App ID `com.issue11.app` with Sign in with Apple; a Sign in with Apple key (gives `APPLE_KEY_ID` + private key); Merchant ID `merchant.com.issue11.app` for Apple Pay.
3. **App Store Connect:** create the app "ISSUE11: Manifestation Journal" with `com.issue11.app`; one subscription group; products per Q2.
4. **Supabase** project → turn on Apple (client id = `com.issue11.app`) and Email providers; run the SQL; upgrade to Pro before outside testers.
5. **Resend** account → verify the sending domain → connect as SMTP in Supabase.
6. **RevenueCat** project → connect App Store (upload the In-App Purchase key) → entitlement `member` → offering with the Q2 products.
7. **Stripe** account (test mode works now; live needs the bank) → Apple Pay certificate for the Merchant ID → Stripe Tax on → webhook to the api-server.
8. **Lulu** account (+ Lulu API sandbox only if Q3 = automatic); order your proof copy.
9. **Privacy policy + Terms** pages live on the landing site (Apple's standard EULA is fine for Terms).
10. Paste the Replit prompt (section 8) only after you approve this spec.

---

## 7. Risks (read these)
1. **Print file not specced.** Lulu needs a print-ready PDF (interior + cover, 8.5×11, bleed). Nothing in the build makes it yet. Without it, paid orders can't be printed. Needs its own spec this week, or print launches on Dec 11 with manual PDF export by us.
2. **Bank → Paid Apps Agreement is the critical path.** If not active by ~Nov 14, subscription testing squeezes into days before Nov 28.
3. **Content sync not built.** Screen 38 promises "nothing she made is lost". True on the same phone, not on a new phone until the content-sync spec ships. Must ship before the App Store build (trust + 2.1 completeness).
4. **Sales tax.** We sell prints at retail, so we may owe sales tax. Stripe Tax calculates it, but where you must register is an accountant question. Ask before live orders.
5. **Expo Go can't test any of this.** Apple sign-in, IAP and Apple Pay need a real iPhone build. Check Replit's iOS build path passes the `EXPO_PUBLIC_*` values into the build (verify).
6. **Replit Agent shortcuts.** It may turn off row security, put a secret key in the app or set prices on the phone "to make it work". QA runs AC-34 to AC-37 on every build.
7. **App Review on required login + hard paywall.** Usually accepted for account-based subscription apps; write review notes saying reviewers can sign in with their own Apple ID, and how to reach deletion. (verify 5.1.1(v) and 3.1.2 at build start.)
8. **Checklist gap:** `.pipeline/app-store-checklist.md` has no line for physical goods (3.1.3(e)) or Sign in with Apple token revocation. Manager should add both.

---

## 8. DRAFT Replit prompt
> ### ⛔ DO NOT SEND until Megan approves this spec (and answers Q1–Q3).

```
ISSUE11 · Sign-in, membership, print checkout, sign-out, delete account (ONE update)

Context: Expo app in artifacts/issue11 + Express server in artifacts/api-server.
Do NOT change onboarding screens 1–37b (order, copy, look) [exception: if Megan said yes to Q1, add ONE small text link on screen 1: "Already have an Issue? Sign in"].
Do NOT restyle any existing screen; reuse the existing paywall, screen 38, Membership, Order, Order status and Delete account designs. Do NOT publish or deploy.
Do NOT use Replit Auth or Replit's Postgres (DATABASE_URL) for user data. Use Supabase.

1. App setup
- app.json: ios.bundleIdentifier "com.issue11.app", ios.usesAppleSignIn true, Stripe plugin with merchantIdentifier "merchant.com.issue11.app". Remove expo-location if unused.
- Add: @supabase/supabase-js, expo-apple-authentication, expo-crypto, react-native-purchases, @stripe/stripe-react-native. Supabase session stored with AsyncStorage.
- App reads ONLY these env names: EXPO_PUBLIC_SUPABASE_URL, EXPO_PUBLIC_SUPABASE_ANON_KEY, EXPO_PUBLIC_REVENUECAT_IOS_KEY, EXPO_PUBLIC_STRIPE_PUBLISHABLE_KEY, EXPO_PUBLIC_API_URL. If one is missing, show a calm "not configured" screen, never crash, never print values.

2. Launch router (in this order): signed in + member → Home · signed in + not member → paywall with "Signed in as <email> · Sign out · Delete account" · not signed in + member → screen 38 · finished onboarding, not member → paywall 37 · else onboarding. Offline: use last known state.

3. Sign-in (screen 38 + a "Welcome back" version of it)
- Sign in with Apple: native button, nonce via expo-crypto, supabase.auth.signInWithIdToken({ provider: 'apple', token, nonce }). Cancel = back, no error.
- Email: supabase.auth.signInWithOtp({ email }) then verifyOtp 6-digit code. Inline invalid-email error, "That code didn't work", Resend locked 60 s, "No connection" after 20 s.
- After sign-in: Purchases.logIn(supabaseUserId); upsert profiles row (cover name, age range, onboarding answers) → first-open cover reveal → Home.

4. Membership (RevenueCat)
- Purchases.configure with EXPO_PUBLIC_REVENUECAT_IOS_KEY at launch (anonymous until sign-in). Entitlement id "member".
- Paywall 37 and 37b read packages from the current offering (37b uses offering "offer"). Show price, period and trial text from the package; no hard-coded prices.
- Restore button: Purchases.restorePurchases(); success → continue; none → "We couldn't find a membership for this Apple ID."
- You → Membership: plan, renews/ends date, "Manage or cancel" (Apple subscription page), Restore, My print orders.

5. Database (write a SQL file supabase/sql/001_signin_payments.sql; Megan runs it herself, do not run it)
- profiles(id uuid pk references auth.users on delete cascade, display_name text, age_range text, onboarding jsonb, created_at, updated_at). RLS: user selects/inserts/updates own row only.
- print_orders(id uuid pk, user_id uuid null references auth.users on delete set null, issue_number int, ship_name, line1, line2, city, state, postal_code, country default 'US', phone, email, shipping_option text, item_cents int, shipping_cents int, tax_cents int, total_cents int, status text check in (awaiting_payment, paid, sent_to_print, shipped, delivered, canceled, refunded), stripe_payment_intent_id text unique, lulu_job_id text, tracking_url text, created_at, updated_at). Unique open order per (user_id, issue_number). RLS: user selects own rows; NO insert/update/delete policy for users (server only).
- Trigger: when status becomes shipped/delivered/canceled/refunded and user_id is null → null ship_name, line1, line2, phone, email.

6. Server (artifacts/api-server). Every route except the webhook requires "Authorization: Bearer <supabase access token>", verified with supabase.auth.getUser; else 401. Secrets from Replit Secrets by name: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET, REVENUECAT_SECRET_API_KEY, APPLE_TEAM_ID, APPLE_KEY_ID, APPLE_SIGNIN_PRIVATE_KEY, RESEND_API_KEY.
- POST /print/checkout {issueNumber, address, shippingOption}: validate US address; PO box/APO/FPO only Standard or Priority. Server sets prices (item 2999; Standard 0, Priority 1000, Expedited 1600, Express 3200 cents), tax via Stripe Tax calculation, creates or reuses the open order, creates/reuses a PaymentIntent (idempotency key = order id), returns client secret + totals. App shows totals, then Stripe PaymentSheet with Apple Pay + card.
- POST /stripe/webhook: verify signature; payment_intent.succeeded → status paid + email Megan "New paid order" (order id, address, issue) via Resend; payment_failed → stays awaiting_payment.
- POST /account/delete {appleAuthorizationCode?}: (1) if Apple user: exchange code and revoke the token with Apple's REST API (client secret JWT from APPLE_TEAM_ID, APPLE_KEY_ID, APPLE_SIGNIN_PRIVATE_KEY, client id com.issue11.app) (2) delete storage objects under "<userId>/" in every bucket (3) print_orders: set user_id null, email null; null address on non-open orders (4) delete RevenueCat customer (5) supabase.auth.admin.deleteUser. Safe to call twice.

7. Sign-out and delete in the app
- Sign out: confirm → supabase.auth.signOut(), Purchases.logOut(), hide local pages (keep them keyed by user id) → "Welcome back".
- Delete account: existing screen + "Deleting your account doesn't cancel your membership" + Manage subscription button + note about open print orders. Apple users re-confirm with the Apple sheet to get a fresh authorization code. Success → wipe all local data, logOut, screen 1. Failure → "We couldn't finish. Try again."

8. Rules: never put a secret key value in app code or chat · never turn RLS off · never compute charge amounts on the phone · never use Apple in-app purchase for prints · keep "Cancel anytime · Restore · Terms · Privacy" visible on the paywall without scrolling.

When done, list: files changed, packages added, the env names used, and anything you could not test in the preview (Apple sign-in, purchases and Apple Pay need a real iPhone build).
```
