---
name: issue11-pinterest
description: >-
  ISSUE11's own Pinterest rules, built from Megan's decisions and Pinterest's public guidance. Load it
  before making, captioning, scheduling or judging any ISSUE11 pin: orbit motion pins (3D, text behind
  the subject), on-pin hooks, titles and descriptions, boards, seasonal timing, Metricool scheduling,
  and reading analytics (outbound clicks over impressions). Holds what Megan approved and rejected,
  word for word, so no agent repeats a rejected idea. Organic now; paid ads only once organic proves
  which pins get clicks. Pairs with pinterest-growth, pinterest-seo and pinterest-pin-design (generic),
  which this overrides where they differ.
---

# ISSUE11 Pinterest

Megan, Nov 26: "Just save everything as a skill." This is ISSUE11-specific and **wins over the generic
Pinterest skills** where they disagree. Before using it, also read the Pinterest RULE/DECISION lines in
`.pipeline/lessons.md` (newest decisions land there first) and `design/VISUAL-QA.md`.

Full sourced guidance: `references/pinterest-playbook.md` (Part 1 organic, Part 2 paid, gaps, sources).

## 1. Hard rules (never break)
- Never schedule, post or upload unless Megan said go **for those pins**. The scheduled 4h Pinterest
  agent never posts. Only a session Megan is talking to, after her go, may use Metricool.
- No paid tools. No made-up numbers: every number on a pin or in copy comes from the linked article
  or a real source.
- Quotes only from `drafts/pinterest/affirmations/BANK.md`, word for word.
- ISSUE11 logo fully visible, **never bottom-right**. Our spot: logo above `issue11.app`, bottom-left.
- Never "becoming her" (Megan: "becoming her should not be a thing"). Never copy Megan's personal details.
- Audience: Gen Z **and** millennial women. Captions and on-pin text are lowercase (Megan: "No capital letters").
- Never place text over a face. Never cut off a face. Run Visual QA (phone 390px + 236px feed) before showing anything.

## 2. What wins (approved)
- **Phone-notes pins** are the winning static format. The first pin ("personal rebrand 🩷", a notes
  screenshot) got 10x the impressions of others.
- **Orbit motion pins** (Megan: "This is excellent!", "looks really freakin cool"): one person cut
  out and still, a big editorial word locked behind her, only the background swinging left and right.
  - Look: tall stretched condensed type (Anton) behind the head; a pink italic lead-in (Instrument
    Serif, #F7A0CC-ish) on top; tiny lowercase mono captions; a thin outline of the letters the person
    hides (Megan: "make sure the writing behind is visible"); slight red/blue colour split; grain.
  - Motion: `TEXT_SWING=0` (text locked), `CYCLES=2` (2 swings per 6s loop; Megan: "a bit more rapid").
  - Photos: **one person, clean outline, head not touching the top edge**. Rejected or broken: two
    people (smears), lying on a cash bed (tears), the long red hair back shot, the visor/vision board
    shot, the manifestation journal shot.
  - Words: the full search phrase in the big type ("winter arc", not "arc"). Short words get
    hidden by the head.
- Text behind the subject, editorial "2000s experimental" mood (Megan: "think dazed & confused").
  This is the genre, never another magazine's logo or layout.

## 3. Rejected (don't bring back without asking)
- **Black-box hook text on the pin** (Megan: "i don't think i like the captions unfortunately").
  Curiosity goes in the **Pinterest title and description**, unless she approves a new on-pin hook look.
- Phone-notes **article** pins (Megan: "the pins are so bad"). Article pins stay on hold until she
  picks a style.
- Notes text composited onto a photo of a phone screen ("it's not working out").
- Moving text (approved but second choice): locked text reads faster and looks like a magazine.

## 4. Hooks and titles
Megan's path: "too AI" → "not really a hook" → "outcome driven" → "pattern interrupt" → "more
polarizing" → "ok this is much better". A good hook =
- **polarizing + pattern interrupt + a gap the article actually closes**, in a human voice
- lowercase, attacks a habit, never a person
- no AI formulas ("unpopular opinion:", "hot take:", "it's not X, it's Y")
- passes the hook test (x-and-threads-posts skill): would you stop, is it specific, is the promise
  clear, does it open a gap, is it bold but believable?

Examples Megan approved: "skincare isn't a glow up. it's a hobby. here's the real one" · "that girl
is a myth. this 30-day plan isn't" · "your affirmations are lies. say these instead".

Titles: keyword first (from real Pinterest searches, Apify `lergassy~pinterest-search-scraper`),
max 100 characters, **keyword + hook inside the first 40**. Pinterest's own advice for click
goals is "clarity over cleverness", so if the hook is spicy, the next line says plainly what she gets.

## 5. Links, boards, timing
- Every pin links to its article with a UTM: `?utm_source=pinterest&utm_medium=organic&utm_campaign=<slug>`
  (see `drafts/marketing/UTM-MAP.md`). Articles live at `issue11.app/blog/<slug>`. Check the page is
  live first (it sometimes serves the homepage, so retry).
- Never the same article URL twice within 72h (check the Metricool calendar first).
- Boards in use (Metricool ids): 253327616479086940 glow up / self care · …941 self love ·
  …942 money / manifestation / new year · …943 manifestation / journal. Board kit still to do: one
  clearly named board per topic (e.g. "Winter Arc").
- Launch about 2 months before a peak: New Year / vision board → now; self love / Valentine's →
  early December; spring reset / glow up → January. Dec 26–31 still converts (app / early-access pins).
- Ramp: 3 → 5 → 7 → 10 pins a day. Metricool is on a paid plan (no 20-post cap).

## 6. Judging results
- The number that matters is **outbound clicks** and the outbound click rate (clicks ÷ times on
  screen), not impressions. Sort Top Pins by outbound clicks; ignore the first 48h (estimates).
- Each week: the top 3 articles by outbound clicks get new pins first, and those pins go on more boards.
- Paid ads only after organic proves the winners (Megan: "If our organic content is growing").
  Before any ad spend: Pinterest Tag + Conversions API (needs Megan's approval, Production Safety Rule).

## 7. How to make an orbit pin (tools in the repo)
- Script: `drafts/pinterest/motion/spatial_orbit.py`. Batch example: `drafts/pinterest/motion/orbit/batch.sh`.
- Free models (ONNX, downloaded to the scratchpad, not committed):
  Depth Anything V2 Small `onnx-community/depth-anything-v2-small` (onnx/model.onnx) and MODNet
  `Xenova/modnet` (onnx/model.onnx, Apache-2.0). Needs `pip install onnxruntime opencv-python-headless`.
- Run: `OUTLINE=1 TEXT_SWING=0 CYCLES=2 python3 spatial_orbit.py <photo> <depth.onnx> <modnet.onnx> <out.mp4> "<big phrase>" "<italic>" "<top caption>" "<bottom caption>" </dev/null`.
  Always `</dev/null` in loops (ffmpeg otherwise eats the list). Run batches in the background.
- Photos come from `drafts/issue11-gift/rebrand-kit/img/`. Fonts: `drafts/pinterest/motion/fonts/` (OFL).
- QA every pin: a contact sheet of frames 45 and 135; crops of the hair edges; a check that no text
  sits over a face and the logo is fully visible.
- To schedule (after Megan's go): media = the public raw GitHub URL of the committed mp4 (the repo is public), via
  Metricool `createScheduledPost` (brand 7995906, timezone America/Los_Angeles, `pinterestData.boardId`).
  Log the Metricool ids in `drafts/pinterest/motion/orbit/PINS.md`.

## 8. Still unknown (needs the real Academy courses, behind Megan's login)
The "4Cs of creative effectiveness", Pinterest's video specs and first-seconds guidance, official
keyword/SEO guidance, and 14 of the 21 Predicts 2026 trends. See the playbook's Gaps section.
