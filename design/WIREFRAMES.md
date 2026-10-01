# ISSUE11 wireframes v0 (Megan, Sep 30, 2026): wireframes-v0.webp
Functionality only; the look comes from brand/BRAND-GUIDE.md. 16 screens. Bottom tabs: Home · Explore · (+) · Journal · You.

01 Splash: wavy ISSUE11, "Your world. A higher you.", ENTER
02 Onboarding 1 (hook): "Tired of scrolling other people's lives?"
03 Onboarding 2 (dream outcome): "A more aligned you."
04 Onboarding 3: "What does your ideal life feel like?" free text
05 Onboarding 4: life areas, multi-select (Wealth, Career, Love, Body, Style, Travel), select 3+
06 Onboarding 5: visual preferences, pick 3+ images
07 Onboarding 6: audio preferences (Affirmations, Subliminals, Guided visualizations, Meditations, Breathwork)
08 Paywall (before personalization): "Create a more aligned you." $4.99/week (7 days free) or $19.99/month, Start free trial
09 Home: "Good morning, Megan", today's experience (e.g. "Become Her", Self Concept, 12 min), continue your world
10 Explore: library by goal (All, Self Concept, Career, Body...), collections (Confidence, Travel, Style & Beauty)
11 Visual World: save and curate imagery (+ add, hearts)
12 Player: immersive audio/visual session with playback controls
13 Journal (after experience): "How are you feeling now?", text + voice mic, save quote / save image to My Issue
14 My Issue: the virtual magazine (Issue 01 cover, "A Higher You", Spring 2025), Enter Issue, templates (Fashion & Beauty, Travel, Art, Business & Lifestyle)
15 Past Proof: "From the archive", 8 months ago: "Is this part of your life now?" Yes, it happened / Not yet
16 Profile: goals, My World (saved), My Issue, Journal, Past Proof, Audio Library, Settings, Privacy

## Gaps to add (Manager, for the Design Room; Apple + trust)
- Sign up / sign in (and Sign in with Apple if Google login is offered)
- Account deletion inside the app (Profile → Settings)
- Paywall: Restore purchases, Terms + Privacy links, clear renewal/cancel text (competitors' #1 review complaint is billing)
- Pricing is a 💛 Revenue + Megan decision (sensitive area): weekly plans draw billing complaints; earlier research suggested yearly $99.99 / monthly $19.99
- Notification permission screen (with a reason), empty states (first day: no issue yet), error/offline states
- AI consent screen IF any AI touches journal entries or images
- Wording check: "subliminals" and wellness audio must not make health claims

## ✅ Approved by Megan, Sep 30, 2026: add these screens
A. **Sign up / Sign in**, placed AFTER onboarding + paywall: "Save your issue" (no sign-in wall at the start; users invest first, then create an account).
   - Sign in with Apple (primary, one tap) + email. If Google is ever added, Apple stays (App Store 4.8).
   - Returning users: a small "Already have an account? Sign in" link on the Splash screen.
B. **Account deletion inside the app:** You → Settings → Delete account → confirm screen (what gets deleted, and that any subscription must be cancelled in Apple settings, with a link) → done. (App Store 5.1.1(v))
⚠️ Authentication and account deletion are sensitive areas: when these are BUILT, the spec needs Megan's explicit approval before building (CLAUDE.md safety rule). Designing them now is fine.

## ✅ Megan, Sep 30: "Add all the things that are missing"
Approved to design (see design/FLOW-MAP.md for details):
1. Sign up / sign in (A above) + in-app account deletion (B above)
2. Paywall: Restore purchases, Terms + Privacy links, clear renewal/cancel text, a close (X) or clear path
3. Notification permission, Photos permission (before adding images), Microphone/Speech permission (before voice journaling): each with a short "why" screen, asked only when used
4. Empty states (day 1: no issue, no Past Proof yet), error and offline states
5. AI consent screen IF any AI ever touches journal entries or images
6. No-health-claims wording (incl. "Subliminals")
7. Cover reveal before the paywall: Name → "Printing your issue…" → Reveal, between 07 and 08
8. Ask the user's name (for Home greeting + cover)
9. (+) button = new journal entry
10. Skip logic on 02–04 defined (skip lands on the next question; defaults used for personalization)
11. Fix placeholder copy: cover date = current season, onboarding 3 label, etc.
Still Megan's decision (not approved yet): audio scope for Jan 11 (Q1), tab layout (Q3), pricing (💛 Revenue + Megan).

## ✅ Megan, Oct 1: scope + launch plan
- ALL features ship by Jan 11 (journal, own photos, magazine, immersive audio, immersive video).
- **ONE beta on Nov 11 with ALL features** (Megan's final call, Oct 1). Official App Store launch Jan 11, 2027.
- Design priority: finish ALL screens by ~Oct 14 so the build can start Oct 15.
- Safety valve: if audio/video aren't solid by Nov 4, show them as "coming soon" in the beta and ship them in a TestFlight update.
