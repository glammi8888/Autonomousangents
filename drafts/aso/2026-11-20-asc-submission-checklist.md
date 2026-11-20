# App Store Connect: what's ready vs missing for the Dec 4 submission
Nov 20, 2026 · 💚 GROWTH — ASO & Opportunity Scout · skills: aso-specialist, graphify (graphs/marketing; no node for App Store Connect fields yet, so I read the files listed below).
**Date change (Megan, Nov 20, word for word): "No I want it to be on App Store on dec 11".** Public launch **Dec 11**, submission due **Fri Dec 4**. Agents never submit and never connect App Store Connect to Applyra. Megan enters everything herself.

## ✅ Ready (copy from the source file)
| Field | Status | Source |
|---|---|---|
| Name, subtitle, keywords (US + es-MX) | Approved Nov 19, Applyra check_metadata valid | drafts/aso/2026-11-18-listing-v15.md |
| Promotional text (167/170) | Drafted in v15 (approved with v15) | same file |
| Description (US) | Written and decided by Megan (Nov 12) | Megan's copy, not in the repo |
| Price points | Monthly $9.99 (no trial) · Yearly $69.99 with 7-day free trial · founding $39.99 first year | drafts/dev/signin-payments-spec-v1.md (Nov 7 update) |

## ❌ Missing (owner · needed by)
1. **Screenshots (real app).** The 6 files in design/app-store/screenshots/ (1320 × 2868) are mockups with sample content. Apple requires real app captures. Re-shoot from the build with the **v15 captions** (screen 5 = mood board). · Design + build · **build by ~Nov 30**, screenshots by Dec 2
2. **App privacy policy URL.** Only the website/waitlist policy exists (drafts/legal/issue11-website-privacy-policy.md). The app needs its own: journal entries, photos, AI Editor consent, subscriptions, account deletion. It must be live at a public URL. · Megan (lawyer review recommended) · user data = Megan approves (CLAUDE.md rule 4) · Dec 1
3. **App Privacy "nutrition label"** (the data-collection answers in App Store Connect). Not started. Must match the privacy policy and the SDKs in the build (RevenueCat, the AI provider). · Megan + build · Dec 3
4. **Support URL.** support@issue11.app exists, but Apple asks for a **web page**. Not found in the repo. Suggest issue11.app/support (contact + FAQ). · Megan (Framer) · Dec 1
5. **Terms of Use (EULA).** App terms aren't written (the Nov 7 terms cover the website only). Option: use Apple's standard EULA and link to it. The paywall still needs Terms + Privacy links (3.1). · Megan · Dec 1
6. **Age rating questionnaire,** including the new "Shared Location" and "Dating and Relationships" questions (required from Nov 16). ISSUE11 has neither → No. Answer honestly about the AI Editor and user-written text. · Megan in App Store Connect · Dec 3
7. **Subscriptions:** group, product IDs, display names, descriptions, review screenshot, introductory offer (7-day trial on yearly) and the founding offer ($39.99 first year as a promotional/offer code). DRAFT for Megan's OK (description limit 45 characters per Apple's help page; display-name limit not confirmed, check in App Store Connect):
   | Item | Draft | Length |
   |---|---|---|
   | Group name | ISSUE11 Membership | 18 |
   | Monthly display name | ISSUE11 Monthly | 15 |
   | Monthly description | Your own magazine, month by month. | 34 |
   | Yearly display name | ISSUE11 Yearly | 14 |
   | Yearly description | A full year of Issues. Try it free. | 35 |
   No prices in these texts (Apple shows prices). "Try it free" only on yearly, because only yearly has the trial. · Megan + Revenue · Dec 2
8. **App Review notes + demo account** (if sign-in is required). Explain the magazine/cover reveal, the AI Editor, "printed Issue sold separately", and anything behind a remote flag (guideline 2.5.19). · Product + Megan · Dec 3
9. **es-MX localization text:** a description (and optional promo text) for the es-MX listing. Same English approach as the name/subtitle. Screenshots can reuse the US set. · ASO Scout drafts on request · Dec 2
10. **Category:** Health & Fitness (primary) + Lifestyle (secondary) is the standing plan, but it's never been checked against live charts. Confirm before Dec 4. · ASO Scout · Dec 2
11. **Small fields:** copyright ("2026 ISSUE11"), contact details for App Review, marketing URL (issue11.app, optional), app icon 1024 px inside the build. · Megan · Dec 3

## 📅 Moved
- **Seasonal keyword recheck: moved from ~Dec 10 to Mon Dec 1** (vision board 2027, new year vision board, and the Big 5 traffic). Applyra, plus ASOMobile if tokens are back. Only change v15 if a word's numbers collapse. Any change needs Megan's OK before Dec 4.
- The New Year In-App Event can be submitted on its own, without a new app version (Apple's In-App Events page, checked Oct 4), so it doesn't block Dec 4. Custom product pages: check in App Store Connect whether they can go in without a new version (not verified).
