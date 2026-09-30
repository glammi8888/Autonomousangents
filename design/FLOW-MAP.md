# ISSUE11 flow map + gaps (Design Room, step 1, Sep 30, 2026)
🩵 PRODUCT + 🎨 BRAND. Source: design/wireframes-v0.webp + WIREFRAMES.md, checked against Notion "App Concept + Onboarding Flow", Roadmap Goal 3, .pipeline/app-store-checklist.md.
Status: waiting on Megan's 3 answers before step 2 (branded prototype).

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
