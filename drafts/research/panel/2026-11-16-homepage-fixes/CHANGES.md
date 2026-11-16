# issue11.app homepage fixes: Nov 16, 2026

Megan approved fixes 1–8 from the Customer Panel report ("1. Yes", Nov 16). The work was done in Framer on branch `chalky-spark`, merged into main and published to production as version `3374d6b3f`. Only 2 changes were pending: the Home page and the "Primary Feature - Section 03" component.
Source: `drafts/research/panel/2026-11-16-issue11-homepage-and-concept.md`.

## Copy edits (before → after)

All copy edits apply to Desktop, Tablet and Phone. Tablet and Phone had their own text overrides for the Section 03 heading and description, and those were edited too.

| # | Where | Before | After |
|---|---|---|---|
| 5, 6 | Hero description | "…then live it one small move a week. Built on behavior-change psychology, so you finally manifest it for real." | "…then live it one small move a week." (last sentence removed) |
| 3, 4 | Trust line under the button | "Private beta opens Dec 11. Founding members pay $39.99 for the first year (then $69.99/yr). Invite-only." | "Private beta opens Dec 11, with invites for the waitlist. Founding members pay $39.99 for the first year (then $69.99/yr). Invite-only." + new line: "The yearly plan includes a 7-day free trial. Skip any week, no streaks. iPhone only." |
| 6, 7 | "Why nothing's changed" point 01 | "Built on behavior-change psychology" | "One small move a week, never a to-do list" |
| 7 | Point 02 | "One small move a week, never a to-do list" | "Your Issue fills up with things you actually did" |
| 7 | Point 03 | "A magazine about the life you want" | "Your Editor never rewrites your words" |
| 5 | "Here's the plan" heading | "Manifesting, the way that actually works." | "Manifesting, focused on what you can control." |
| 5 | "Here's the plan" description, sentence 1 | "Wishing and lying still with your eyes closed don't change a life." | "Wishing alone doesn't change a life." |
| 6 | "Here's the plan" description, sentence 3 | "…then practice it in small steps until it's simply how you live." | "…then practice it in small steps (the morning, the workout, the hard email) until it's simply how you live." |

Kept exactly as they were: the headline, "Manifestation doesn't work.", the kicker, the FAQ and the meditation card.

Where the new wording comes from:
- "with invites for the waitlist" is from the FAQ ("When can I get ISSUE11?").
- The 7-day trial on the yearly plan is in lessons.md CURRENT FACTS (Megan, Nov 7 and Nov 12).
- "Skip any week, no streaks" comes from "Skip it, shrink it" on the site and "no streaks" in the report/concept.
- "iPhone only" is from the FAQ.
- "Your Issue fills up with things you actually did" is from step 03.
- "Your Editor never rewrites your words" is from the FAQ ("Is there AI in ISSUE11?").
- "focused on what you can control" is from the FAQ ("Does manifestation actually work?").
- "the morning, the workout, the hard email" is from the meditation card.

After the edits, "behavior-change psychology" appears once on the page (in the "Here's the plan" section, with the example).

## Layout changes

- **Fix 1 (Phone):** turned on wrap for the steps row in the 3 Mobile variants of "Primary Feature - Section 03". On a phone, Choose it / Make it / Live it now stack vertically, and step 03 is visible without scrolling sideways. Tablet uses the same variants, but all 3 cards still fit in one row there (minimum width 220px each), so it looks as it did before. Desktop variants were not changed.
- **Fix 2 (Phone only):**
  - Hero top padding changed from 80px to 48px.
  - The hero description and the form are 60% wide.
  - The "The Freedom Issue" phone mockup (the same one desktop uses) now sits beside the description and the form: scale 0.6 → 0.3, pinned top-right at 274px, with the transform origin at the top right.
  - The mockup is fully inside the first 390x844 screen, and nothing on its screen is cropped. The second mockup ("the cool girl" page) stays below, as before.
- **Fix 8 (Phone only):**
  - The founder quote no longer uses the H2 style on phone. It is now 28px with 1.1em line height, in the same font (Inter Tight 500) and the same colour token.
  - Section padding changed from 88px to 56px, inner padding from 64/40 to 24/24, and gaps from 56/48 to 32/28.
  - The quote block went from about 600px to 277px. No photo was added.
- Desktop and Tablet layouts were not changed. Brand fonts, colours, logo, onboarding and the app were not touched.

## Checks

- Visual QA (design/VISUAL-QA.md) was done in the Framer preview (phone, desktop, tablet steps) and again on the live site with Playwright at 390x844 and 1440x900. I looked at every screenshot:
  - The logo is fully visible.
  - Nothing is cropped and no faces are cut.
  - There's no horizontal scroll at 390px.
  - Text is readable.
  - The design is on-brand.
- One problem came up and was fixed before publishing: on phone, the founder quote briefly rendered in the wrong colour (invisible on the dark section) after its text style was detached. I restored the original colour token.
- Live text check at 390px. Each phrase's count:
  - "behavior-change psychology": 1
  - "actually works": 0
  - "manifest it for real": 0
  - "eyes closed": 0
  - Each new line: 1
- Screenshots in this folder:
  - Before: `before-390-fold.png`, `before-390-full.png`, `before-1440-fold.png`, `before-1440-full.png`
  - After: `after-390-fold.png`, `after-390-full.png`, `after-390-steps.png`, `after-390-founder.png`, `after-1440-fold.png`, `after-1440-full.png`
- The form was not submitted, to keep test rows out of the real waitlist.

## Left for Megan

1. **What "approved" means.** The FAQ still says "Approved guests lock in their founding rate". I didn't define it, because she hasn't decided.
2. **Does the 7-day trial apply to the $39.99 founding year?** The new line only says the yearly plan has the trial.
3. **Cancel line.** I didn't add one, because the site never says billing goes through the App Store. If she confirms it does, add "Cancel anytime in your iPhone settings."
