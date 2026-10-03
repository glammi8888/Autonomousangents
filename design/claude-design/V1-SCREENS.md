# ISSUE11 V1 — Megan's Claude Design screens, adapted (Oct 3, 2026)
Prototype: https://claude.ai/artifact/3T2jdNK2ZT1J5gzKjwhyTM (source: design/claude-design/v1-prototype/, rebuilt by build.py from the exports in this folder)

## Flow
Launch (V3) → Welcome (V5 01) → Q02 "Who are you becoming?" (V3 Onboarding) → Q07 "One year from now, she…" (V5) → "Lucky Star is building your first Issue" (V5) → Sign in, "save your issue" (V2) → Home (V4)
Home → Audio player (V4 Immersive) → Eyes closed (V4) · Scribe = Notes to self (V4) · Your World = In frame (V2) · Issue = My Issue (V4) · 11 → Lucky Star aura (V1: speaks, chat in V2)

## Adaptations made (look unchanged)
- Home tiles renamed to the locked functions: Audio · Scribe · Your world · Publish. "Notes to self" chip → Scribe; "In frame" chip → Your world.
- "4 to print" → "4 to go"; "Finish 4 pages to print" → "Finish my issue" (printing not confirmed for V1).
- Launch: removed the "Curating your issue" bar (the app opens; the issue is built after onboarding by V5 "Building").
- Sign in moved after onboarding as "save your issue"; terms line now names Terms & Privacy Policy (Apple needs a privacy policy link).
- Q02 label "Step 2 of 4" → "Question 02" to match V5's 9-question numbering.
- V2 Launch ("Curating your issue", dark) not used: V5 "Building your first Issue" does the same job better.

## Gaps for V1 (not designed yet)
Onboarding Q01, Q03–06, Q08–09 · Meet Lucky Star + AI consent · paywall · Scribe writing screen · Publish (edit issue by prompting) + issue reader · Add-proof flow · Explore · You/settings/delete account · notification permission.

## Vibes batch (Oct 3, 2026), added to the prototype
- 12 Streak calendar ← tap "12 day streak" on Home; "Write one line" → Scribe.
- 14 Vision board "Collect · Your vision" (alternative Your World; Design Room suggests it replaces In frame).
- 07 App icon picker ← avatar/You (iOS supports alternate app icons).
- 11 Launch variants: red full-bleed, noir, white over photo (Megan to pick one).
- Megan: "they don't all need to be added but they can be added on screens that haven't been established yet." Vibes = a mood library for the gap screens:
  - Red full-bleed 11 → "Proof added" celebration moment
  - Noir small 11 → Meet Lucky Star + AI consent background
  - White 11 over photo → paywall hero
  - Streak calendar → You screen (your ritual history)
  - App icon picker → Settings, inside You
  - Vision board → Your World (stronger than In frame)

## Full V1 flow (Oct 3, 2026): new design + original onboarding and app logic (Megan: "yes exactly")
Onboarding: Launch → Welcome → How it works → Q01 name → Q02 who are you becoming (life areas) → Q03 what you want most → Q04 pick what feels like her (Your World) → Q05 how you want to practice (Audio) → Q06 how you want to feel → Q07 one year from now → Q08 past proof → Q09 one small step → Meet Lucky Star + AI consent → Lucky Star builds your first Issue → Cover reveal → Notifications → Paywall → Save your issue (sign in) → Home.
App: Home · Audio (player, eyes closed) · Scribe (notes, write) · Your World (vision board → in frame) · Issue (pages → page with "change this page" prompt) · Add proof → "It's real" · You (stats, app icon, ritual, notifications, Lucky Star & AI, membership, privacy, sign out, delete account) · 11 → Lucky Star.
Design Room-made screens (V4 style, Megan to refine in Claude Design): how, q01, q03–q06, q08, q09, meet, reveal, notif, paywall, write, proof, proofdone, page, you, delete. Source: v1-prototype/gaps.py.
⚠️ Paywall shows "PRICE TBD": prices, trial and final wording are a Revenue + Megan decision. Payments + user data screens need Megan's spec approval before building.
Still open: Explore tab.

## Batch 2 (Oct 3, 2026, Megan: "Add it all please")
Added to the prototype: Hold to log your win (Home) · Lucky Star weekly move card (Home carousel) · Explore + Collection (session library) · After-session "How do you feel now?" → Scribe (player ⏭ ends the session in the prototype) · Issue reader (swipe pages) · Page editor (layout, page color with auto text color, emoji + 11 stickers you can drag, patterns waves/zebra/cheetah/hearts, edit text, undo) · Night mode (You → Night mode; preview) · Past proof archive (You → Proofs) · Offline state · Scribe empty state.
