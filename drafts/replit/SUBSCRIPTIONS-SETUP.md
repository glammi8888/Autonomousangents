# ISSUE11 subscriptions setup (Megan, Nov 27, 2026) · checklist
Pricing A (approved): Yearly $39.99 founding + 1 week free · Monthly $9.99 · Jan 11, 2027: Yearly → $69.99 for new members only · Giveaway: code ISSUE100, 100 uses, 3 months free (launch week).

## A · App Store Connect: subscriptions
1. Apps → ISSUE11 → Monetization → Subscriptions → Subscription Groups → + → "ISSUE11 Membership".
2. Create: Reference name "Yearly", Product ID `issue11_yearly`, Duration 1 year, Price $39.99 (US; let Apple fill other countries).
3. In Yearly → Subscription Prices → Introductory Offers → + → all countries → Free → 1 week.
4. Create: Reference name "Monthly", Product ID `issue11_monthly`, Duration 1 month, Price $9.99. No offer.
5. Each: App Store localization (display name + description) + review screenshot + review notes. Group localization: display name "ISSUE11 Membership".
## B · Link RevenueCat to Apple
6. App Store Connect → Users and Access → Integrations → In-App Purchase → Generate API key ("RevenueCat") → download .p8 once + note Key ID and Issuer ID.
7. RevenueCat → project → Apps → ISSUE11 (App Store) → In-app purchase key configuration → upload .p8, Key ID, Issuer ID. Also App Store Connect API key if RevenueCat asks (for importing products).
## C · RevenueCat configuration
8. Products → Import from App Store (or + New: issue11_yearly, issue11_monthly).
9. Entitlements → + → identifier `member` → attach both products.
10. Offerings → `default` (current) → packages: Annual = issue11_yearly, Monthly = issue11_monthly.
## D · Test (Nov 30 TestFlight)
11. App Store Connect → Users and Access → Sandbox → Testers → + a test Apple ID. Buy, cancel, Restore in the TestFlight build.
## E · Launch week (Dec 10–11)
12. Subscriptions → Yearly → Offer Codes → Create → Custom code `ISSUE100`, 100 redemptions, Free, 3 months, eligibility: new subscribers. Announce Dec 11.
## F · Jan 11, 2027
13. Yearly → Subscription Prices → + Change price → $69.99 → "Keep current price for existing subscribers". Update the landing + paywall copy.
