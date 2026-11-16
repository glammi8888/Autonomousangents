# Customer Panel: issue11.app homepage + full concept (Nov 16, 2026)

Asked by: OPS for Megan ("Just show the website http://issue11.app and explain the concept thoroughly and see what they say and what feedback they have" · "Explain who our ICP is too"). Homepage only; the Rebrand Kit landing page was not used.
Skills: synthetic-user-feedback (4 browsing personas), synthetic-crowd (12 personas, haiku, seed 11), customer-research (personas grounded in the real Reddit / App Store lines in design/editorial/LEXICON.md and design/research/REDDIT-ICP-2026-11.md).

> **Read this first.** These are AI personas, not real customers. This is a screening signal for confusion and objections, not a forecast. Never quote these answers publicly as reviews, testimonials or "users said". Confirm anything with money at stake against real data (waitlist sources, the Nov 17 Instagram test, beta interviews).

Raw files (same panel for future before/after runs): `drafts/research/panel/2026-11-16-issue11-homepage-and-concept/` (crowd/ = dims, personas, both assets, results, tally · browse/ = persona briefs, screen-by-screen walkthroughs, full narrations · screens/ = Visual QA captures).

---

## 1. ICP summary (from the repo docs only)

1. **Who:** a woman in a "next chapter" (new city, new job, post-breakup, post-baby, turning a new decade). She's ambitious and has taste ("Soho House x Pinterest x fashion magazine"). Sources: design/ICP.md, LEXICON.
2. **Age:** Megan's current frame is millennial, **30–38** (LEXICON: "You're building for us. 36. Millennial. 30s."). GAP: design/ICP.md still says 24–38, core 26–34. The two docs disagree, and neither is validated.
3. **Primary segment (Megan, Nov 9):** the disappointed manifester, "people that tried manifestation and think it doesn't work", plus believers who still believe but say it doesn't work for them. Never mock her belief; the passive method is what failed her.
4. **What she wants:** to know what she actually wants, a practice she can stick to, to see her dreams made beautiful and tangible, to know what to do next, to focus on the process instead of anxiously waiting, and to notice proof she is changing (POSITIONING, 10 outcomes).
5. **Pain points, in her words (Reddit):** "I'm tired of being in a loop of planning goals, starting and leaving after a few days" · "I keep waking up in terror, with the how's" · "sick of getting all my info from short form content" · vision boards "inspire for 5 minutes" · affirmations "feel fake" · journals feel like homework.
6. **Skepticism (real lines in LEXICON):** "I notice all these Manifesting influencers want you to pay for shit." · "I hate all these annoying coaches and grifters..." · "how the heck do I cancel this subscription" · "a $7/week price after a free trial" (Stella complaint).
7. **Her vocabulary:** dream life, future self, next chapter, self-concept, living in the end, inspired action, the loop, the hows, delulu, "soft life, but I have a mortgage".
8. **Where she hangs out:** Pinterest (vision boards: "anything I claim on my Pinterest comes true"), long-form YouTube, and audiobooks (Neville, Dispenza). She uses TikTok but doesn't trust it. Instagram is assumed, not proven.
9. **Money:** has disposable income for apps, beauty and wellness, and probably pays for 1–3 subscriptions already. Both lines are [Megan]/[Assumed]. GAP: willingness to pay for this subscription is unproven (ICP section 13).
10. **What she'd pay for (Reddit):** personalized affirmations, audio loops, a rhythm that sticks, and "a free tier to try first".
11. **Not her:** working creators who could make this themselves in Canva.
12. **Unproven (ICP section 13):** that she'll pay, that she wants an AI-built magazine, that she prefers process audio, and that the age/income range is right.

## 2. The concept explanation the personas received

Written only from POSITIONING, PRODUCT-ARCHITECTURE, EDITORIAL-BIBLE, the lessons.md CURRENT FACTS box, and the live FAQ. Full text: `crowd/concept.md`. In short:
- **What it is:** a process-focused manifestation app that turns the life you want into your own magazine and helps you take small real steps. It has 4 parts:
  - **My saves:** your images and Pinterest saves.
  - **Audio:** curated musical meditations, 5–10 minutes, rehearsing the steps rather than the outcome, and playing with the phone locked.
  - **Scribe:** a private journal; you pick which lines go in your Issue; no streaks.
  - **Publish:** a 40-page evolving Issue that fills up over about 3 months from what you do. Default is one Issue every 3 months. Print is optional at $29.99.
  - **The Editor:** the AI layer. It sorts, lays out and helps you think, never rewrites your words, can be switched off, and suggests one optional "next move" a week. It is not a to-do list.
- **Philosophy:** DESIRE → IMAGINE → EMBODY → BECOME. "The new way of manifestation: You don't have to see it to believe it. But you have to participate to create it." No promised results.
- **Who it's for:** women in their late 20s and 30s in a next chapter who save lots of vision-board content.
- **Price:** $9.99/month or $69.99/year (7-day trial on yearly). Approved waitlist guests get $39.99 for the first year, then $69.99. The waitlist is free.
- **When:** private beta Dec 11, 2026. App Store launch comes after the beta. iPhone only.

---

## 3. Browsing panel (synthetic-user-feedback, 4 personas)

**Method.** I browsed https://issue11.app live with Playwright at 390x844 (phone) and 1440x900 (desktop). I expanded the FAQ and stepped through all 8 gallery screens. I did **not** submit the form, because that would add a fake row to Megan's real waitlist sheet. I then wrote a screen-by-screen capture of what is actually visible (`browse/walk-phone.md`, `walk-desktop.md`). Each persona ran as its own isolated `claude -p --safe-mode` call (sonnet, no tools, no shared context) in three parts: browse with running commentary, hear the full concept, give a verdict. Three personas were on phone, one on desktop.

| Persona (ICP stage) | Device / arrival | After site | After concept | Pays $39.99 → $69.99? | 1st impression |
|---|---|---|---|---|---|
| Jess, 31, curious newcomer, new city, 900-pin board | Phone, Pinterest pin, 10pm | maybe later | **join now** | maybe ($39.99 yes) | 6/10 |
| Dana, 34, daily paper journaler, believer, post-breakup | Phone, Instagram ad | maybe later | **join now** | maybe | 5/10 |
| Rachel, 37, burned by a $7/week app, mom of a toddler | Desktop, friend's link | maybe later | **join now** (for the weekly move only) | maybe, only if cancelling is obvious | 6/10 |
| Mia, 29, glow-up / rebrand Pinterest girl, tight budget | Phone, Pinterest pin, bus | maybe later | **join now** (not paying) | maybe | 6/10 |

**The pattern:** all 4 went from "maybe later" after the site to "join now" after hearing the concept explained. The site under-explains the product. The concept is not what's failing.

### Jess (curious newcomer, phone)
- **First 5 seconds:** "The headline 'Your vision board is a museum of a life you're not living' stung a little... I'd screenshot that line. But I still don't know what the product looks like."
- **Scroll:** she understood the product only at the "Send the pitch you've been sitting on [I did it] [Not yet]" mockup, "a screen later than it should be". She missed step 3 because the cards scroll sideways. The printed magazine was "the nicest thing on the page". She got bored at the founder quote.
- **Form:** "'Request access' makes me wonder what happens next. Will I get an email? Am I approved? What if I'm not?"
- **What clicked in the concept:** "process, not outcome", saves becoming pages, one move a week, no streaks, the AI off switch, and the 40-page Issue filling up from what she does.
- **Objection:** "I've dropped every practice I've ever started, and nothing on the page shows me why this time would be different."
- **Quote:** "I only understood what this actually is after someone explained it to me, and a lot of people at 10pm in bed won't scroll that far."

### Dana (daily journaler, believer, phone)
- **First 5 seconds:** hooked by the headline, then put off by "invite-only", "request access" and "behavior-change psychology", which "sounds like a pitch deck, not my language".
- **Scroll:** "Manifestation doesn't work... At least not the way you've been doing it" read to her as "the exact guru move I hate, 'my way is the real way'". "Wishing and lying still with your eyes closed don't change a life" read as "dismissing meditation and visualization, which is half of what I do. **This is the point where I almost leave.**" Print stopped her scroll: "the closest this gets to my paper-journal brain." The founder line about phones pulling us away was "the best sentence on the page".
- **Form:** "approved by who? ... What if I'm rejected? Do I get the $39.99?"
- **Concept:** "The site made it sound like it was against manifesting. Explained this way, it's not." She would keep paper and copy some lines into Scribe.
- **Quote:** "The printed magazine is the only thing that made me stop scrolling, and the rest felt like a manifestation guru in a pink gradient telling me my notebook doesn't work."

### Rachel (burned skeptic, desktop)
- **First 5 seconds:** she understood the product immediately because the desktop hero shows the mockups. "Invite-only... feel like fake scarcity." She spotted the price and went looking for the catch.
- **Scroll:** "behavior-change psychology... a phrase I've now seen twice with zero proof. ... Say which study or which method, or stop saying it." Choose it / Make it / Live it was "the first part that feels like it was made for a real person with a real schedule." The magazine builder: "homework with nice fonts."
- **FAQ:** "No app can promise results is an honest answer and I respect it more than the hero copy." She noticed the yearly trial and that "nothing here says how to cancel."
- **Quote:** "I like the idea of one small thing a week that doesn't make me feel guilty, but I'm not paying for another pretty app until someone tells me how to cancel it."

### Mia (glow-up Pinterest girl, phone)
- **First 5 seconds:** "I see '$39.99' and think, wait, it costs money?? I just cancelled three subscriptions." There is no product picture on the first phone screen.
- **Scroll:** "Behavior-change psychology is the third time they've said it. Sounds like homework." She saw only one and a half of the 3 steps. Print was the thing she'd screenshot. The Pinterest FAQ answer "upload as images" "sounds like work, not a link-paste".
- **Quote:** "I love the idea of my vision board becoming a real magazine, but the site made me read a lot of words before it showed me the one thing I wanted to see."

---

## 4. Crowd panel (synthetic-crowd, 12 personas, haiku, seed 11)

- **Panel (dims.json):** age 28–31 / 32–35 / 36–40 · 6 manifestation stages (curious newcomer, daily journaler, disappointed manifester, burned skeptic, glow-up/rebrand, still believes but stuck in the loop) · 3 budgets · 4 life moments · 4 arrival contexts · millennial woman in the US.
- **Assets:** A = the homepage text as visitors see it, plus a description of the visuals (`crowd/homepage.md`). B = the concept explanation (`crowd/concept.md`).
- **Question:** "Would you join the waitlist / pay for this? Why or why not?" 24 calls, 0 failed.

**Difference between A and B on the same panel (the only number worth reading):**
- The concept explanation moved **2 personas from ignore to consider** (the tight-budget daily journaler and the tight-budget rebrand). No one moved the other way.
- Price reaction **did not change**: 10 of 12 said "expensive" for both. The explanation fixes understanding, not price resistance. Price resistance is tied to "I can't see it work" (see theme 1), so price is probably not the lever. Real data should confirm this.
- Objections about the **"Manifestation doesn't work" framing went from about 7 of 12 on the homepage to 0** on the concept (which doesn't use that line). The concept-only objections were mostly "a notes app and Pinterest already do this" (about 6 of 12).
- **Segments:** the warmest were "still believes but stuck in the loop", the newcomer, the journaler and the rebrand girl. **Both disappointed manifesters and both burned skeptics ignored both versions.** That is the segment the homepage hook is written for. Treat this as a hypothesis for the Nov 17 ad test, not a conclusion: haiku panels told that "ignoring is normal" skew harsh, and these segments are skeptical by definition.

Keyword-based theme counts (rough; homepage → concept): no proof / can't see it 12 → 12 · wants a free trial, free tier or refund 12 → 12 · price/subscription 10 → 11 · how to cancel / renewal 8 → 7 · invite-only / approval unclear 6 → 1 · time and effort 5 → 6 · quit-before / stickiness 4 → 5 · psychology claim unexplained 4 → 0 · print feels like an upsell 5 → 5.

Per persona (verdict homepage → concept):
| # | Stage · budget · arrival | Homepage | Concept |
|---|---|---|---|
| 0 | journaler · picky 1–3 apps · IG ad | consider | consider |
| 1 | rebrand · tight · Google | ignore | ignore |
| 2 | stuck in loop · spends freely · Pinterest | consider | consider |
| 3 | disappointed · picky · friend | ignore | ignore |
| 4 | burned skeptic · tight · Pinterest | ignore | ignore |
| 5 | newcomer · spends freely · IG ad | ignore | ignore |
| 6 | disappointed · picky · Google | ignore | ignore |
| 7 | stuck in loop · spends freely · friend | consider | consider |
| 8 | journaler · tight · IG ad | ignore | **consider** |
| 9 | burned skeptic · picky · Pinterest | ignore | ignore |
| 10 | newcomer · spends freely · Google | consider | consider |
| 11 | rebrand · tight · friend | ignore | **consider** |

---

## 5. Objection themes (both panels), with the bluntest line for each

1. **"I can't see it work, and nobody has used it."** Every persona raised this. Pre-launch, there are no reviews and the product is shown only as mockups. "Pretty magazine, unproven app, and a $70 renewal for a weekly to-do nudge I can get free from a notes app, so I'm out." (crowd #3)
2. **"Manifestation doesn't work" plus "the way that actually works" reads as a contradiction, or as guru talk.** It hits believers and skeptics from opposite sides. "It's a manifestation app that tells me manifesting doesn't work, and I'm not paying to find out what they mean by that." (crowd #6) · "This is the point where I almost leave." (Dana, on "Wishing and lying still with your eyes closed don't change a life")
3. **Subscription trust: trial, renewal, cancelling.** "I'm not paying for another pretty app until someone tells me how to cancel it." (Rachel) The yearly 7-day trial is real (CURRENT FACTS), but the page never mentions it, and the crowd repeatedly asked for "a free trial".
4. **"Request access / invite-only / approved" with no next step explained.** "'Request access' sounds like I might get rejected. What's 'approved'?" (Mia) "Invite-only... feel like fake scarcity." (Rachel)
5. **"Another practice I'll quit / I have no time."** "I have a toddler and about twenty spare minutes a week, and I'm not paying $69.99 a year to feel behind on a magazine I'll never finish." (crowd)
6. **The "behavior-change psychology" claim is repeated 3 times and never explained.** "Say which study or which method, or stop saying it." (Rachel)
7. **"A notes app and Pinterest already do this" (mostly on the concept).** "It's a Pinterest board with a journal, a weekly reminder, and a $70 annual charge, and I already have the first two for free." (crowd #11)

**What landed (keep it):** the headline ("stung", "I'd screenshot that line") · "December looked exactly like January" · **the printed magazine** (the scroll-stopper for 3 of 4 browsers) · the "Send the pitch you've been sitting on [I did it] [Not yet]" mockup (the moment people "got it") · "never a to-do list / skip it, shrink it" · the honest FAQ answer "No app can promise results" (it raised trust in every persona who opened it) · AI being optional and never rewriting her words.

---

## 6. Visual QA (design/VISUAL-QA.md) on the live homepage

Captures are in `screens/`. Desktop 1440: the hero shows the product, the logo is fully visible, nothing is cropped, there are no stray logos or readable signs, the mockups fit the topic, and it's on-brand. Pass. Phone 390: no horizontal page overflow and the logo is fully visible. Three issues:
- **No product above the fold on phone.** Only the top edge of a phone mockup peeks in under the price line (`screens/phone-fold.png`). Desktop shows the mockups right away. This matches every phone persona saying "I don't know what it looks like yet".
- **The 3 steps are cut off on phone** (`screens/phone-3-steps-cut-off.png`). They sit in a sideways-scrolling row (`overflow-x: auto`, no snap, no dots or arrows). Card 02 is cut mid-sentence and **card 03 "Live it."**, the weekly move and the core mechanism, is fully off-screen. 3 of 3 phone personas missed it.
- **The founder quote is set in display-size type on phone**, about 2 full screens with no photo. All 4 personas skimmed past it.
No viewport fix was needed on my side: captures at 390x844 with `isMobile` were consistent across two runs.

---

## 7. Fixes, ranked by impact (grouped by theme)

All copy suggestions reuse Megan's existing words or facts already on the page. Panel wording must not replace hers. The site has standing publish permission, but these are copy and positioning calls, so Megan picks.

**A. Show the product sooner (theme 1, Visual QA)**
1. **Phone hero: bring the magazine mockup into the first screen.** Desktop already does this. For example, place the "The Freedom Issue" cover beside or above the headline at a smaller size, or move the phone mockup above the email field. This is the highest-impact layout fix.
2. **Stack the 3 steps vertically on phone** (or add snap plus dots), so "03 Live it." is seen. It is the step that explains the product.
3. **Show a real finished Issue:** a short flip-through of Megan's own Issue (founder-led proof, ICP section 12.4). It is the most believable proof available before launch, with no fake testimonials. It answers "I can't see it work" without inventing reviews.

**B. Subscription trust (themes 3, 4)**
4. **Put the trust facts next to the price line under the button:** that the yearly plan has a 7-day free trial (a CURRENT FACTS item that is not on the page yet; confirm it applies to the founding rate), that you can skip any week (no streaks), and that it's iPhone only (FAQ-only today). Add a cancel line, such as "cancel anytime in your iPhone settings", once it is confirmed that billing runs through App Store subscriptions (RevenueCat implies it does). Moving these to where the hesitation happens answers Rachel's "how do I cancel".
5. **Say what happens after "Request access"** in one line (e.g. the confirmation email and when invites go out), and **define "approved"**. Also align the wording: the hero says "Founding members pay $39.99", while the FAQ and the rule say "Approved guests lock in their founding rate". Needs Megan (see the questions below).

**C. Framing (themes 2, 6)**
6. **Keep "Manifestation doesn't work. At least not the way you've been doing it." (Megan's chosen angle) but A/B test it in the Nov 17 Instagram test** against Megan's own line "You can't control the outcome. You are in control of the process." (POSITIONING, Oct 7). The panel flagged the "doesn't work" framing on the homepage but not in the concept, and the hook's target segment (disappointed and skeptic) was the coldest. Real click and sign-up data should decide, not the panel.
7. **Tone down the two "manifest it for real / the way that actually works" claims** and the line "Wishing and lying still with your eyes closed don't change a life", which read as dismissing meditation, a feature ISSUE11 sells. Use the softer, honest FAQ voice ("No app can promise results. ISSUE11 focuses on what you can control: the process."). It raised trust in every persona.
8. **Say "behavior-change psychology" once, and make it concrete**, or use "designed to" wording (OPS trust note in POSITIONING, Oct 22). Example of concrete, from the page itself: meditations that rehearse the morning, the workout, the hard email.

**D. Explain the mechanism (themes 1, 5, 7)**
9. **Surface the 3 things that converted the browsers in the concept but are buried or missing on the site:** (a) the Issue fills up over about 3 months from what you actually do (proof, not a wish list), (b) no streaks and no guilt, and (c) the Editor never rewrites your words and can be switched off. Today (a) is only in the hidden step 3, (b) is implied, and (c) is FAQ-only.
10. **Answer "why not Notes + Pinterest" with the print and the proof mechanic**, not more features. Print was the clearest "I want that" moment.

**E. Smaller page fixes**
11. **Shrink the founder quote on phone** (smaller type, about 1 screen) and consider Megan's photo. Her call; personal details are hers to share.
12. **Pinterest import wording:** "Upload your board or your Pinterest saves as images" read as work. Fine for now; revisit if a link import is ever built (product change, logic first).

**F. Offer/product ideas (Megan decides; logic first, not urgent)**
13. "Try before paying" came up in nearly every answer: one free meditation on the site, or a free first page of your Issue. The Reddit research also lists "a free tier to try first". This is a pricing/paywall change, so it needs Megan's OK under Safety Rule 4 (payments/subscriptions) before anything is built.
14. A time-cost line ("how much time a week this asks") would answer the "no time" moms. I only have "one move a week, skip any week" as a fact. A minutes figure needs Megan.

## 8. Questions only Megan can answer
1. What does "approved" mean for waitlist guests (everyone who signs up, or reviewed)? *Recommended:* say everyone on the waitlist gets an invite. It removes the "will I be rejected" worry and is likely true for a beta.
2. Does the 7-day free trial apply to the $39.99 founding year? *Recommended:* yes, if RevenueCat/App Store allows it. "Free trial" was the most repeated ask.
3. OK to A/B "Manifestation doesn't work" vs "You can't control the outcome. You are in control of the process." in the Nov 17 ad test? *Recommended:* yes. It's cheap and settles it with real data.

## 9. Limits of this test
- AI personas only. They agree with each other more than real people do, and they are sensitive to prompt wording. The haiku crowd is told that ignoring is normal, so expect harshness. Read the **differences**, not the shares.
- Browsing personas worked from my exact screen-by-screen capture, not a live browser of their own. I did the live browsing and Visual QA myself.
- The form was not submitted (to protect the real waitlist sheet), so the post-submit experience is untested.
- Pre-launch, every persona asks for reviews that cannot exist yet. Don't read that as a page flaw beyond "show the product and the proof mechanic".
