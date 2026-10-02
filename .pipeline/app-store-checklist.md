# 🍎 App Store readiness checklist (ISSUE11)

Megan's rule: ISSUE11 must qualify for the Apple App Store. The Planner checks new features against this list, and the Reviewer treats a likely rejection as a blocker.
**Last checked:** Oct 2, 2026 (sources: developer.apple.com/news, /news/upcoming-requirements). Apple changes these rules often, so re-verify against the official App Review Guidelines at build start (Nov) and before submission (Jan).

## Build & tooling
- [ ] Built with **Xcode 26 / iOS 26 SDK or later** (required for uploads since Apr 28, 2026). Check that the Despia or Capacitor output meets this. Current release is iOS 27: build and test with the latest Xcode 27.x.
- [ ] Deployment target iOS 13 or later (required since Sep 9, 2026; any modern build meets this).

## Not "just a website" (4.2 minimum functionality + June 2026 "adds value" rule)
- [ ] Feels like a real app, not a wrapped website: native navigation, push notifications, offline basics, haptics/share sheet where natural.
- [ ] Clear reason to exist in a crowded category (journaling): the magazine-cover experience is the differentiator. Say it in the review notes.

## Make Apple happy (featuring)
- [ ] Design follows the current Apple Human Interface Guidelines and the latest iOS design language (iOS 26/27). Checked during app design in October.
- [ ] **iPhone Duo (foldable, on sale Oct 23, 2026, runs iOS 27.1):** layouts adapt to its new screen sizes, poses and orientations (no fixed phone-width layouts). Test in the Xcode 27.1 simulator. Apple is promoting apps "purpose-built" for it: a spread-style magazine view on the open fold is a featuring opportunity. (Apple news, Sep 16 + 18, 2026)
- [ ] Use recent iOS features where they fit naturally (widgets later, notifications, App Intents/Shortcuts). Apple features apps that adopt what's new.
- [ ] Re-checked monthly by the Manager's Friday retro (first Friday).

## Privacy (5.1)
- [ ] Privacy policy link inside the app and in App Store Connect.
- [ ] Accurate App Privacy "nutrition label" (what data is collected and why).
- [ ] Every permission prompt (notifications, photos, etc.) has a clear purpose text and is asked only when needed.
- [ ] **AI:** explicit user permission before sending personal data (journal entries, photos) to any third-party AI service (2026 rule).
- [ ] Privacy manifests present for third-party SDKs.
- [ ] If there are accounts: **account deletion inside the app** (5.1.1(v)).
- [ ] App Tracking Transparency prompt only if we track users across apps or websites.

## Login (4.8)
- [ ] If offering Google/social login, also offer an equivalent privacy-focused option (Sign in with Apple).
- [ ] Demo account + instructions in the review notes if login is required.

## Payments (3.1)
- [ ] Digital subscriptions use Apple in-app purchase (RevenueCat is fine).
- [ ] Before paying, the user sees the price, renewal period, trial terms and how to cancel.
- [ ] "Restore purchases" button. Links to Terms (EULA) and Privacy on the paywall.

## Completeness & honesty (2.1, 2.3)
- [ ] No placeholders, "coming soon", lorem ipsum, broken links or crashes. Note: the beta safety valve (audio/video shown as "coming soon" in TestFlight) is beta only; the Jan App Store build must ship them complete or hide them.
- [ ] Screenshots and description show the real app. No fake reviews or ratings.
- [ ] Wellness wording only: no medical or therapy claims.
- [ ] If users can share content publicly: report, block and moderation (1.2).
- [ ] Age rating questionnaire answered honestly.

## Sources
- https://developer.apple.com/news/upcoming-requirements/
- https://developer.apple.com/app-store/review/guidelines/
- https://9to5mac.com/2026/06/09/apple-tightens-app-review-guidelines-against-apps-that-do-not-add-value-to-the-app-store/

## Desktop / web version (added Oct 1, 2026) — DROPPED from V1 by Megan, Oct 1. Keep for later reference.
- [ ] 3.1.3(b): anything sold on the website (subscription) is ALSO available as in-app purchase in the iOS app; web purchases may then unlock the app.
- [ ] 4.2: the iOS app is not just the web editor in a wrapper (native navigation, push, offline, haptics, photo picker, share sheet).

## AI-made magazine (added Oct 1, 2026, spec: design/magazine-ai-spec.md)
- Consent screen before journal text is sent to the AI service; can be turned off in Settings.
- Privacy labels and AI data disclosure updated; the provider must not train on or keep user data (verify its terms).
- Account deletion also deletes generated issues.
- Re-check current App Store guidelines on AI and user data at build start and before submission.
- Lucky Star (AI helper, spec: design/lucky-star-spec.md): "AI can make mistakes" label, crisis-word message with resources, no health/medical/financial advice, app still works with AI turned off.
