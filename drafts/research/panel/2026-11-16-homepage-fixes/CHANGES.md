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

## Fix 9 · Cancel line (Nov 16, after Megan's "Yes" on App Store billing + trial on founding year)
| Where | Before | After |
|---|---|---|
| Hero trust line, 2nd line (node SQh312SI4, all 3 breakpoints inherit) | "The yearly plan includes a 7-day free trial. Skip any week, no streaks. iPhone only." | "The yearly plan includes a 7-day free trial. Skip any week, no streaks. Cancel anytime in your iPhone settings. iPhone only." |

Status: **LIVE.** Megan OK'd merge + publish ("1. You can do that"). Branch supple-thread merged into main (1 change: Home) and published to production, version `bd56af953`. Live check with Playwright: phrase count 1 at 390x844 and 1440x900, no horizontal scroll, logo fully visible, text readable, nothing cropped. Screenshots: `after-390-cancel.png`, `after-1440-cancel.png`.

## Nov 17 · waitlist-page fixes

Source: `../2026-11-17-waitlist-page-review.md` section 3 (rows 1a–5). Megan approved: "i want it to do all the fixes or tell you thefixes and you do the mods". Standing rule: always publish issue11.app.
Status: **LIVE.** Framer branch `matte-meadow` merged into main (9 changes) and published to production, version **`1f9201075`**. Checked live with Playwright on Nov 17. No form was submitted.

| # | Where | Before | After |
|---|---|---|---|
| 1a | `Early Access Submit` component (the hero form button on Desktop, Tablet and Phone, plus the blog article form) | White fill, black "Request access" | Black fill (`Primary` token), white label (`100` token), **"Request my invite"**, pointer cursor. The Success state is also black/white now. The arrow icon was skipped (optional). |
| 1b | Same button: new Hover gesture variant | No hover state | Opacity 0.85 on hover. Live: opacity goes from 1 to 0.85. |
| 2a | /thank-you paragraph (all breakpoints) | "Your request is in. The first Issue is invite-only, and invitations go out in waves. We're saving you a spot. Future you is already in print." | "Your request is in. The first Issue is invite-only, so our emails go out in waves before the Dec 11 beta. Keep an eye on your inbox (and your spam folder, just in case). Future you is already in print." |
| 2b | /thank-you: new "Share block" under the paragraph | (none) | Thin divider · "KNOW SOMEONE WITH A BOARD FULL OF PLANS?" (Section Label style) · "Send her ISSUE11. She can request her own invite." · black **"Share ISSUE11"** button. This is a new code component, `ShareButton.tsx`. It calls `navigator.share({title:'ISSUE11', url:'https://issue11.app'})` and falls back to copying the link, after which the label shows "Link copied" for 2.5s. It has no tracking, no reward and makes no network calls. Live test in a desktop browser without share support: the fallback copied `https://issue11.app`, the label changed to "Link copied" and 0 requests were sent. |
| 2c | /thank-you "Back to home" | The only action | Unchanged, now under the share button |
| 3 | Hero small print (all breakpoints) | One grey Metadata line: "Private beta opens Dec 11, with invites for the waitlist. Founding members pay $39.99 for the first year (then $69.99/yr). Invite-only." + "The yearly plan includes a 7-day free trial. Skip any week, no streaks. Cancel anytime in your iPhone settings. iPhone only." | New dark line, "Offer Line" (new text style **Body - Medium**: Inter Tight 500, 18/17/16px, Primary colour): **"Free to join, no card needed. Founding rate: $39.99 for your first year (then $69.99/yr). Private beta opens Dec 11."** The grey line SQh312SI4 keeps its style and now reads: **"Invite-only. 7-day free trial on the yearly plan. Skip any week, no streaks. Cancel anytime in your iPhone settings. iPhone only."** Both lines sit in a new "Small print" stack with an 8px gap. Width is 500px on Desktop (keeps the hero from overflowing at 768px tall), 260px on Tablet (keeps it clear of the phone mockup) and 300px on Phone. |
| 4 | Hero, Phone only | Top padding 48px; H1 46px; form bottom at 704px on a 375x667 screen | Hero/Content top padding 48 → 24px. Hero H1 uses a new phone-only style **H1 - Hero Phone** at 40px (−13%); the H1 is unchanged everywhere else. The small mockup moved up from 274 → 213px so it stays beside the description, and the hero is 1100 → 1140px tall so the second mockup stays clear of the small print. The headline words, kicker and "Manifestation doesn't work." were not touched. |
| 5 | CTA labels | Header: "Request access" (Desktop) and "Get early access" (Tablet, Desktop-Scroll, Mobile, Mobile Open; the /thank-you header uses the same component). Closing button: "Request access" (all 3 breakpoints) | All now read **"Request my invite"**. The closing line "Get your invite before the Dec 11 beta and lock in $39.99 for your first year." is unchanged. |

Copy change after the table was approved (row 2a): Megan first answered "Yes they do but not immediately" about the confirmation email, then clarified "Since its invite only they go by waves". So the paragraph doesn't promise a confirmation email. It says emails go out in waves and asks her to watch her inbox and spam folder.

### Live checks (Playwright, deviceScaleFactor 1, Nov 17, after publish)
- **Fix 4 acceptance:** at 375x667 the hero form spans 513–617px, so the bottom is at **617px**, under the 655px target and fully above the fold. At 390x844 the form bottom is at 591px and the small "Freedom Issue" mockup is fully visible and uncropped.
- No horizontal scroll: scrollWidth equals viewport width at 390, 375 and 1440, on both the home page and /thank-you.
- Phrase counts on the live home page: "Request access" 0 and "Get early access" 0 at every width. "Request my invite" appears 4× on phone (header, mobile menu, hero, closing) and 3× on desktop. "Free to join, no card needed" 1 and "Invite-only. 7-day free trial" 1.
- Phrase counts on /thank-you (opened directly, status 200): new paragraph 1, "KNOW SOMEONE…" 1, "Share ISSUE11" 1, "Back to home" 1.
- Hero button: computed background rgb(12, 14, 13) with a white label.
- Visual QA (design/VISUAL-QA.md): I looked at every screenshot below. The logo is fully visible, nothing overlaps or is cut off, the text is readable on phone, and it stays on-brand (existing fonts and tokens). On Tablet (checked in the Framer canvas only), the phone mockup slightly overlaps the right end of the hero form. That overlap was there before this change (form width untouched).

Screenshots (this folder):
- Hero (fixes 1, 3, 4, 5): `after-1-3-4-5-hero-390-fold.png`, `after-4-hero-375x667-fold.png`, `after-1-3-4-5-hero-1440-fold.png`, `after-1-3-4-5-home-390-full.png`, `after-1-3-4-5-home-1440-full.png`
- Hover (1b): `after-1a-hover-1440.png`
- Thank-you (fix 2): `after-2-thankyou-390-fold.png`, `after-2-thankyou-375x667-fold.png`, `after-2-thankyou-1440-fold.png`, `after-2-thankyou-390-full.png`, `after-2-thankyou-1440-full.png`, `after-2b-share-copied-1440.png`

Not changed: the blog article heading "Get early access to ISSUE11" (it's a heading, not a button) and the Rebrand Kit page's "Start your issue" button (it isn't part of the waitlist page).
