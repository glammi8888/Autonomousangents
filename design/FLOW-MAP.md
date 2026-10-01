# ISSUE11 flow map + gaps (Design Room, step 1, Sep 30, 2026)
🩵 PRODUCT + 🎨 BRAND. Source: design/wireframes-v0.webp + WIREFRAMES.md, checked against Notion "App Concept + Onboarding Flow", Roadmap Goal 3, .pipeline/app-store-checklist.md.
Status: step 2 done. Prototype v1: https://claude.ai/artifact/LrFfSmECZknsurnx2LKKVf (source: design/prototype/index.html)

## Flow map
```
01 Splash ─ENTER→ 02 Hook → 03 Dream outcome → 04 Ideal life (text)
  → 05 Life areas (3+) → 06 Visuals (3+) → 07 Audio → 08 Paywall ─→ 09 HOME
  (SKIP on 02–04 jumps ahead; ⚠️ skip target undefined)

Tabs: Home · Explore · (+) · Journal · You
09 Home ─today's experience→ 12 Player ─end→ 13 Journal ─save quote/image→ 14 My Issue
09 Home ─continue your world→ 11 Visual World
10 Explore ─collection→ 12 Player
16 You → Goals · 11 My World · 14 My Issue · 13 Journal · 15 Past Proof · Audio Library · Settings · Privacy
15 Past Proof ← reached only from You (⚠️ or a push notification?)
(+) ─→ ⚠️ undefined
```

## Gaps
**Already listed in WIREFRAMES.md:** sign up/in (+ Sign in with Apple), in-app account deletion, paywall Restore/Terms/Privacy/renewal text, pricing (💛 Revenue + Megan), notification permission, empty/error/offline states, AI consent if any AI, no health claims.

**New ones found:**
1. **No cover reveal.** The magazine is the differentiator and the "aha" (Notion concept), but onboarding never shows it. The user pays at 08 before seeing their issue.
2. **Scope clash with the roadmap.** MVP = journal + magazine cover; immersive sessions come later. 5 of 16 screens are audio (07, 10, 12, plus the Home hero + Audio Library). Also: who records the audio content? Nothing is planned.
3. **My Issue isn't a tab.** The core feature sits 2 taps deep. The brand mockup had tabs Home · Collect · Journal · Issue.
4. **Name is never asked** but Home says "Good morning, Megan" and the cover needs a name.
5. **(+) has no destination.** Recommend: new journal entry.
6. **Permissions not designed:** Photos (11 add image), Microphone + Speech (13 voice). Each needs a purpose screen, asked only when used.
7. **Past Proof needs history** ("8 months ago"). Day 1 has none, so it needs an empty state. Where do the proofs come from (journal wins)?
8. **Stale/placeholder copy:** "Spring 2025" cover date; onboarding 3 is labelled "Explainer" but is a text field; "Subliminals" wording needs the no-claims check.
9. **Skip logic:** where SKIP on 02–04 lands, and what happens to the personalization if skipped.
10. **Paywall close (X):** Apple requires a way out or a clear free path. Is there a free tier or is it hard-gated?

## Questions for Megan (max 3)
1. **Scope:** do the audio screens (07, 10, 12) ship on Jan 11, or v1.1? *Recommend: design them now, build journal + cover first (the roadmap MVP), unless the audio content has a maker.*
2. **Cover reveal before the paywall?** *Recommend: yes, add Name → "Printing your issue…" → Reveal between 07 and 08. It's the aha, and research says value before price.*
3. **Tabs:** *Recommend Home · Explore · (+ new entry) · Issue · You.* Journal lives under (+) and You.

Not decided here: pricing (💛 Revenue + Megan).

## Megan's decisions (Sep 30, 2026, her words summarized)
- Add a magazine sneak peek (cover reveal) before she pays: Name → "Printing your issue…" → Reveal → Paywall.
- ~~No audio in v1~~ → **Megan, Sep 30 (later): "I want the video/audio experiences with V1, not later."** Immersive audio + video sessions ship Jan 11: onboarding sessions question, Home "Today's experience", Explore library, full-screen Player → Journal.
  ✅ Megan, Oct 1: she makes the sessions herself with AI tools; launch with 10–20 sessions. Checks: commercial license of each AI tool (voice, music, video), no cloned real voices/likenesses, no health claims. (was: ⚠️ Open: who makes the sessions (audio + video content) and by when; this is the biggest scope/time risk for TestFlight Dec 15. Wording: no health claims ("Subliminals").)
- Ask her name. Onboarding is not set in stone yet.
- Tabs: Home · Explore · (+ new entry) · Issue · You (agreed).

## Product Lead suggestions for the open parts (in the prototype, Megan to confirm)
- (+) opens a "New entry" sheet: write, voice, add image, log a win.
- SKIP → jumps to the name screen; skipped answers use gentle defaults, editable in You → Goals.
- Logo: Megan's real wordmark files in brand/logo/ (used in the prototype).
- Photos: use the iOS photo picker (no permission prompt needed). Mic: ask on first mic tap, with a reason.
- Notifications: primed screen right after the reveal ("Get your issue every morning?"), system prompt only on "Yes".
- Past Proof day 1: seeded by a new onboarding question "Name one thing you already made happen" (from the Notion concept).
- Cover date: the real current season, set automatically (no "Spring 2025").
- Paywall: visible close (X) + Restore + Terms/Privacy. Free vs hard-gated after closing = 💛 Revenue + Megan.

## Printed issues (Megan, Oct 1, 2026)
- Megan wants printed magazines and has found a print partner (name to come). V1 vs right after launch: not decided yet.
- How: issue rendered as print-size pages → print-ready PDF (300 dpi, bleed) on a server → partner API prints + ships.
- Payment: physical goods go outside Apple in-app purchase, e.g. Stripe with Apple Pay. ⚠️ Payments + shipping addresses = sensitive areas: Megan approves the spec before building (CLAUDE.md).
- Image rights: app images need licenses that allow printing.

## Figma (Oct 1, 2026)
- File: https://www.figma.com/design/vKzbnR5ffDv0Zuf0A3Sp2e (Megan's team, Starter plan: max 3 pages, 1 variable mode)
- 01 · Foundations: colors (variables), 9 text styles, vector logo component, components (liquid-glass button, cover capsule, hold to log your win, band label, Future You splash, tab bar)
- 02 · Screens · Night and 03 · Screens · Light: Splash, Cover reveal, Paywall, Home, Explore, Immersive session, Journal, Past Proof
- Images are placeholders named "IMAGE · pX": the image upload host (mcp.figma.com) is blocked by this environment's network policy.
- Oct 1: added onboarding 02–07 (Hook, Dream, Ideal life, Life areas, Visuals, Sessions) on the Night page (row 2). Then hit the Figma Starter plan's MCP tool-call limit. Still to build: 08 Past proof Q, 09 Name, 10 Printing, 12 Notifications, 14 Save your issue, Issue tab, Reader, My World, Collection, You, Settings, Delete account, Offline, (+) sheet, Mic sheet; plus Light copies of the new screens. Leftover to delete by hand: red "Wording check…" note on 07 · Sessions.

## Figma v1 — rebuilt on Megan's paid account (Oct 1, 2026)
- **File: https://www.figma.com/design/vmhEozmeuxjFV8OhtKLU0r** (glammiagency@gmail.com · "Megan Scott's team" · Pro). This is the main file.
- 01 · Foundations: theme variables with **Night + Light modes**, 9 text styles, vector logo (follows theme), components: Button / Liquid glass (Primary · Secondary · On photo), Cover capsule, Hold to log your win, Band label, Cover splash · Future you, Tab bar.
- 02 · Onboarding: 01–14 (Night row + Light row). 03 · App: 15–29 (Night row + Light row). Light rows = same screens with the frame's theme mode set to Light.
- Images: named placeholders "IMAGE · pX · …" (upload host mcp.figma.com blocked by this environment). Originals in brand/imagery/ (mj-00…mj-09 = p0…p9).
- Old partial file on the free account (meganscottmanolova@gmail.com, vKzbnR5ffDv0Zuf0A3Sp2e) is superseded.

## Desktop magazine editor (Megan, Oct 1, 2026 — idea, scope not decided)
- Megan: let people build their magazine on desktop too ("it's not easy on the phone").
- Proposal: a web version of the Issue editor (same account, same Supabase data, syncs both ways). Lovable builds web apps natively, so this reuses the same code; the iOS app stays the main product.
- Login on web: Sign in with Apple + email (works on web).
- ⚠️ Payments: subscription bought on web vs in the app must follow Apple's multiplatform rules (3.1.3) — verify current rules before building. Payments = Megan approves the spec.
- ~~Decided by Megan (Oct 1, 2026): desktop editor ships in V1 (Jan 11).~~ → **Megan, Oct 1 (later): desktop editor DROPPED from V1.** The magazine is made by AI on her approved layouts, with small edits on the phone. Spec: design/magazine-ai-spec.md (waiting for approval).
- ⚠️ Scope risk: V1 now = iOS app + immersive audio/video sessions + magazine editor (layouts, colors, stickers, patterns, text editing) + desktop web editor. Roadmap's build window is Nov 2 – Dec 11; flag to the Manager for re-planning.
- Apple check (Oct 1, 2026, Megan: "as long as it fits Apple rules"):
  - 3.1.3(b) Multiplatform: a subscription bought on the website may unlock the iOS app, IF the same subscription is also sold as in-app purchase in the app. → Sell in both places (RevenueCat supports web + Apple), same account.
  - 4.2 Minimum functionality: a plain web wrapper gets rejected. → The iOS app must be clearly native: push, haptics, offline reading, photo picker, mic dictation, share sheet, widget later. The shared editor is one screen inside a native app, not the whole app.
  - Re-verify the guidelines at build start (Nov) and before submission (Jan).
- Oct 1: placeholder images added to Figma through the code channel (small, soft 300px versions): p0–p6 are in, on pages 02 and 03 (Night + Light). p7–p9 and the cover-capsule thumbnails are not done yet. Paused because Megan is redesigning the visual language in Claude Design, Megan, Oct 1: "our flow is perfect" — the flow, screens and order stay as they are; only the visual language changes, applied across all screens and the Figma file.
