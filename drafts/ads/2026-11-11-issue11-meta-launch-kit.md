# ISSUE11 Meta ads: ready-to-launch kit (DRAFT, Nov 11, 2026)

💚 GROWTH, Media Buyer. **Draft only.** Nothing has been created in Meta and nothing has been spent. Megan presses every button.
Skills used: ads-meta, ads-create, ads-creative, ads-test, copywriting. Builds on `drafts/ads/2026-11-06-issue11-launch-plan.md` (budget, break-even math, stop rules). The voice now follows the live landing page (`drafts/landing/landing-copy-v3-full-page.md`).

**Status:** Pixel 2228324218041215 is live on issue11.app (PageView, loads once). Thank-you page is /thank-you. Automatic Advanced Matching stays OFF (the privacy page promises it). Facebook Page "Issue11" exists and Instagram is linked. The ad account has no card yet, and the Meta Ads connector can't read it yet.
**Cold start:** the ad account, the Pixel's conversion history and the sign-up event are all new. That means no outside benchmark applies and no forecast. Our own test is the only number that counts.
**Provisional:** Meta's menus and names (Advantage+ audience, A/B test, creative enhancements) change often and weren't re-checked live today. If a button below has a different name, take a screenshot and I'll match it.

---

## 1. Megan's clicks before launch (about 20 minutes)

1. **Check the ad account basics first.** Ads Manager → Account settings. Time zone should be Los Angeles (or your local time) and currency USD. You can't change these later, so check them before adding the card.
2. **Add your card.** Ads Manager → Billing & payments → Payment methods → Add payment method.
3. **Set a $300 spending limit.** Billing & payments → Payment settings → Account spending limit → Set limit → **$300**. Meta stops all ads when it's reached, so it's your hard cap. (It counts total spend until you reset it. It does not reset by itself every month.)
4. **Connect the Pixel to the ad account.** Business settings → Data sources → Datasets (or Pixels) → pick **2228324218041215** → Connected assets → Add assets → choose the ISSUE11 ad account → Save.
5. **Give the ad account your Instagram.** Business settings → Accounts → Instagram accounts → Issue11 → Connected assets → add the ISSUE11 ad account. Without this, the ad can't post as @issue11.
6. **Create the sign-up conversion.** Events Manager → Custom conversions → Create custom conversion:
   - Name: **Waitlist Sign Ups**
   - Data source: Pixel 2228324218041215 · Action source: Website
   - Event: All URL traffic · Rule: **URL contains** `thank-you`
   - Category: **Lead** · Value: leave empty
7. **Test it once.** Sign up on issue11.app with a test email, land on /thank-you, then check that "Waitlist Sign Ups" shows **Active** in Events Manager (it can take up to a day). Mark that test row in the Google Sheet as "test" so we don't count it.
8. **Verify the domain if it isn't done yet.** Business settings → Brand safety → Domains → Add issue11.app → use the meta-tag option and paste it in Framer → Site Settings → Custom Code (head). Then press Verify.
9. **Send me one screenshot** of the custom conversion page showing Active. Then you're ready to build the campaign below.

## 2. Exact campaign settings

Changes from Nov 6: new hooks in the live voice, the price is now decided (kept out of round 1 on purpose, see section 4), and creative "enhancements" must be OFF so Meta doesn't add AI images or text.

**Campaign**
| Setting | Enter this |
|---|---|
| Name | ISSUE11 · Waitlist · US · Hook test Nov |
| Objective | **Leads** |
| Special ad category | None |
| Campaign budget (Advantage+ campaign budget) | **Off** (the budget sits on each ad set for the A/B test) |

**Ad set** (set up one, then make the A/B test from it, see section 4)
| Setting | Enter this |
|---|---|
| Name | Hook A · Manifestation doesn't work |
| Conversion location | **Website** |
| Performance goal | Maximize number of conversions |
| Dataset / conversion event | Pixel 2228324218041215 → custom conversion **Waitlist Sign Ups** |
| Budget | **$5/day per ad set** (2 ad sets = $10/day total) |
| Schedule | Start the day after step 9 is done. End date exactly **14 days later** |
| Location | United States only |
| Audience | Click **"Switch to original audience options"** so these are firm limits instead of suggestions: **Women, 18 to 40**. No interests, no lookalikes, no uploaded lists |
| Placements | **Manual placements** → Instagram only: Feed, Explore, Explore home, Stories, Reels. Untick Facebook, Messenger, Audience Network and Threads |
| Attribution | Leave Meta's default (7-day click, 1-day view) and write down what it says |

**Ad**
| Setting | Enter this |
|---|---|
| Identity | Facebook Page: Issue11 · Instagram: @issue11 |
| Format | Single video, 9:16, 10 to 15 seconds, sound-off friendly (text on screen) |
| Creative enhancements / Advantage+ creative | **Turn every option OFF** (no auto music, no generated backgrounds, no text variations, no image "touch-ups"). Our rule: nothing AI-made or fake in ads |
| Multi-advertiser ads | Off |
| Primary text / headline | From section 3 (variant 1 of each hook for round 1) |
| Call to action | **Sign Up** |
| Website URL | see UTM links below |
| Tracking | Website events: Pixel 2228324218041215 ticked |

**UTM links** (paste exactly, one per ad)
- Hook A: `https://issue11.app/?utm_source=meta&utm_medium=paid&utm_campaign=waitlist-hooktest-nov&utm_content=a-manifestation-doesnt-work`
- Hook B: `https://issue11.app/?utm_source=meta&utm_medium=paid&utm_campaign=waitlist-hooktest-nov&utm_content=b-vision-board-museum`

**Missing data (flagging, not guessing):** I don't know whether the waitlist form saves the UTM into the Google Sheet. If it doesn't, the Sheet can't tell ad sign-ups from Instagram organic ones (organic posting started Nov 9). Then we compare Sheet totals per day with Meta's count and read it as a range, not an exact number.

## 3. Two Reel concepts (new voice)

Both use only (a) the interim screens in `design/site-screens/` (the `-fit` versions crop best) and (b) Megan's own phone footage. Rules applied: magazine stays the hero, the AI isn't sold, no promised results, no health words (meditation, healing, anxiety, body), no dates, no em dashes, belief is never mocked (the passive method is what failed).
Small text on the last frame of both Reels: **"Early design preview."** The screens are interim mockups, not the final app, so this keeps it honest.
Screen 2 (My saves) is left out on purpose: its "03 Body" board label could pull the ad into Meta's health review.

### Hook A · "Manifestation doesn't work." (the follow-through angle)
**On-screen hook (0 to 2 s):** **Manifestation doesn't work.**

| Time | Shot | Text on screen |
|---|---|---|
| 0 to 2 s | Megan's footage: a still shot of a sticky-note affirmation on a mirror or a vision board on a wall. No face needed | Manifestation doesn't work. |
| 2 to 4 s | Same shot, slow push in | At least not the passive kind. |
| 4 to 7 s | Screen `1-home-fit.jpg`, slow zoom to "This week's move: Send the pitch you've been sitting on." | One small move a week. |
| 7 to 10 s | Screen `6-scribe-write-fit.jpg` (the typed line "Send the pitch. Not reread it nine times.") | Write the day you want. |
| 10 to 13 s | Screen `11-i-did-it-fit.jpg` (the page lands: "The pitch.") | Do it. It becomes a page in your magazine. |
| 13 to 15 s | End card: blush background, wavy 11 icon (`icon-wavy-11-black.png`) | Get your invite · issue11.app · Early design preview. |

**Caption** (only if the same Reel is also posted organically; ads use the primary text): Manifestation doesn't work when it's all wishing and waiting. ISSUE11 is built on behavior-change psychology: you make your own magazine about the life you want, then live it one small move a week. Invite link in bio.

**Primary text** (about 125 characters before "more")
1. Wishing and waiting don't change a life. What you do each week does. Make your own magazine, then live it one move at a time. *(round 1)*
2. Affirmations, vision boards, scripting. Then December looks like January. ISSUE11 swaps wishing for one small move a week.
3. Done with wishful thinking? Make your own magazine, live it weekly. Approved guests: $39.99 for year one, then $69.99/yr.

**Headline (about 40 characters):** Less wishing. One small move a week.
**CTA:** Sign Up

**Policy self-check, Hook A:** no health or healing words ✓ · no promised result (no "you will manifest", no "actually works") ✓ · no date, no "launches Dec 11" ✓ · doesn't say or imply the viewer's beliefs ("you manifest", "you believe"), which Meta's personal-attributes rule covers ✓ · price shown with the real renewal price ✓ · no fake reviews, AI faces or founder story ✓.

### Hook B · "Your vision board is a museum of a life you're not living." (the magazine angle)
**On-screen hook (0 to 2 s):** **Your vision board is a museum of a life you're not living.** (Megan's locked hero line. Two lines of big text.)

| Time | Shot | Text on screen |
|---|---|---|
| 0 to 2 s | Megan's footage: slow pan across a real vision board, or her thumb scrolling a camera roll full of saved screenshots | Your vision board is a museum of a life you're not living. |
| 2 to 5 s | Keep scrolling the camera roll, a bit faster | So make it a magazine instead. |
| 5 to 9 s | Screen `7-your-issue-fit.jpg`, slide left like a page turn ("p.15 of 40") | Your own magazine. Your name on the cover. |
| 9 to 12 s | Screen `1-home-fit.jpg`, zoom from "The Freedom Issue." down to "This week's move" | Then live it, one small move a week. |
| 12 to 15 s | End card: blush background, wavy 11 icon | Get your invite · issue11.app · Early design preview. |

**Caption** (organic version only): If your camera roll is half screenshots of a life you want, hi. ISSUE11 turns them into your own magazine, then helps you live it one small move a week. Invite link in bio.

**Primary text**
1. Your vision board is a museum of a life you're not living. Turn it into your own magazine, then live it one small move a week. *(round 1)*
2. Your camera roll is half screenshots of a life you want. Put them in a magazine you make, with your name on the cover.
3. Most vision boards get forgotten. Make yours a magazine you live, page by page. Approved guests: $39.99 year one, then $69.99/yr.

**Headline:** Make your own manifestation magazine
**CTA:** Sign Up

**Policy self-check, Hook B:** no health or healing words, and the "Body" screen is left out ✓ · no promised result ✓ · no date, no "launches Dec 11" ✓ · "your vision board" names an object, not a belief or a personal trait ✓ (small risk: if Meta rejects it, swap in variant 2 and the hook "Most vision boards get forgotten.") · price with renewal ✓ · nothing fake ✓ · images inside the screens: see Question 1.

## 4. The A/B test and stop rules (reused from Nov 6)

- **Question:** which first line gets cheaper waitlist sign-ups from the women we want: the problem ("Manifestation doesn't work.") or the magazine ("Your vision board is a museum...")? These are the two angles the ICP says to test: follow-through vs the magazine itself.
- **Setup:** build the Hook A ad set, then use Meta's **A/B test** button and pick "Creative" as the variable. Ad set B = Hook B. Same audience, same placements, same $5/day each, same 14 days, same CTA, same length. Primary text variant 1 for both. **No price in round 1**, so the price doesn't muddy which hook won.
- **Main number:** cost per waitlist sign-up, checked against the Google Sheet. Tie-breaker: share of people who watched past 3 seconds.
- **Call a winner only if** there are at least ~30 sign-ups across both ads AND Meta shows one ad with at least 80% chance of winning. Otherwise it's "no clear winner": keep the better-looking one and test a new hook. About $140 can only show big gaps (about 2x). Small differences don't count.
- **Don't peek and switch.** No changes in the first 7 days, except the stop rules below.
- **Stop rules (you pause, I tell you when):**
  1. $70 spent and 0 sign-ups → pause and check the form, /thank-you and the Pixel before spending more.
  2. After 14 days, cost per sign-up still above the break-even you pick (for example **$3.40**, which assumes 10% of sign-ups end up paying the $39.99 offer) → stop paid, stay organic, rethink the hook.
  3. Meta and the Sheet differ by more than ~20% → check tracking before spending more.
  4. The $300 spending limit is the hard ceiling no matter what.
- **Undo:** pausing an ad stops it right away. Nothing is lost and it can be turned back on.
- **Round 2 idea (after a winner):** winner with price (variant 3) vs winner without price. It tells us if "$39.99 for year one" pulls more sign-ups or just more clicks.

## 5. Policy check, all ads (one line each)
- **Hook A:** no health claims ✓ · no outcome guarantees ✓ · no "launches Dec 11" (no date at all) ✓.
- **Hook B:** no health claims ✓ · no outcome guarantees ✓ · no "launches Dec 11" (no date at all) ✓.
- **Landing page note:** the page says "so you finally manifest it for real" and "Manifesting, the way that actually works." Those are fine on the site (Megan's Nov 9 rule) but they stay out of the ads, where Meta and the FTC judge them as result claims.

## 6. Two decisions only Megan can make
1. **Are the photos inside the interim screens ours to use in paid ads?** (For example the "the cool girl." magazine page in screens 1, 7 and 9.) **Recommended:** if you're not sure they're yours or licensed, swap your own photos into those screens before filming, or use only screen 6 (text only) plus your own footage. Reason: paid ads get more eyes than the site, and a rights complaint can get the ad or the account flagged.
2. **When do we press Publish?** **Recommended:** as soon as steps 1 to 9 are done, ideally by Mon Nov 17. Reason: 14 days ends around Dec 1, before holiday ad prices peak and with 10 days left to push the winner before the Dec 11 beta. Filming both Reels is about 30 minutes of phone footage (best on Tue/Wed, not on your solo days).
