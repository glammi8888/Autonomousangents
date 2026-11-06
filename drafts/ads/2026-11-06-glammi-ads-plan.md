# Glammi Studio paid ads plan (DRAFT, Nov 6, 2026)
💚 GROWTH, Media Buyer. **Draft only, no commitment.** Nothing is live, nothing is spent, no accounts, keys or images. Megan clicks every button herself.

> ⚠️ **Provisional.** The claude-ads policy reference (`compliance.md`) hit its refresh date today (Nov 6) and the benchmarks reference is past its quarterly check (last verified Jul 11). Anything resting on platform rules, menus or character limits is marked *(provisional)*. wordstream.com is blocked in this environment, so every benchmark below comes from search snippets and is **unverified**.
> ⚠️ **No confirmed Glammi price exists in the repo.** The $499/mo figure is the *proposal* in `drafts/glammi/PRICING-EVALUATION-2026-10.md` (Oct 26), still waiting on Megan. It's a placeholder for the math only. Never put it in an ad.

---

> ✅ Update Nov 5 (Megan): the booking page is already live on glammi.ai (Calendly). Item (b) below is done.

## 1. Recommendation (3 lines)
1. **Not yet. Cold email + daily articles first.** Cold email costs no extra cash per booked call, while Google charges an estimated $16 to $31 per click on our terms. At a $499 price, one paid client would cost more than the first 3 months bring in (math in section 3).
2. **Must exist before $1 is spent:** (a) a confirmed offer and price, (b) the booking page live on glammi.ai with the calendar embedded, (c) tracking that counts a booked call, plus a privacy policy that mentions it, (d) payments working (bank → Stripe), so a "yes" on the call can actually pay.
3. **When those are done and cold email has produced ~10 booked calls (that gives us your real close rate):** start with **Meta retargeting** at ~$5/day. Add **Google Search** only if the numbers say it can pay back.

## 2. Best channels (and why)
| Channel | Verdict | Why |
|---|---|---|
| **Meta retargeting** (people who already visited glammi.ai) | **First** | Cheapest and lowest risk. It reminds people who read an article or clicked a cold email. It works alongside cold email instead of replacing it. Needs the Pixel on glammi.ai. |
| **Google Search** on "agency" terms | **Second** | Highest intent: the person is already looking for help. But the volume is tiny (about 870 US searches a month across our 4 known terms) and clicks are pricey, so it naturally caps around ~$1,000/mo. |
| Meta cold (owners, by interest) | Later | Cold owners need the VSL and a strong booking page first. Interest targeting for "med spa owners" is loose, so we'd pay to reach staff and patients. |
| LinkedIn | Skip for now | Aggregators put US clicks at ~$6 to $12 *(unverified)*. Most med spa owners live on Instagram, not LinkedIn. Maybe revisit later for jewelers. |

**Search terms we have real data for** (our keyword tool, US, Oct 28 to Nov 5, 2026; CPC = the tool's estimated top-of-page bid, not an auction result):
- "ai search agency": 330/mo, est. CPC **$22.44** (broad, so it draws non-beauty businesses too)
- "med spa marketing agency": 290/mo, CPC not recorded
- "med spa website design": 180/mo, est. CPC **$31.50**
- "jewelry store advertising": 70/mo, est. CPC **$16.19**
- "dermatology marketing": 210/mo, CPC not recorded

## 3. Three budget options + the math

| | A · $0 (recommended now) | B · ~$150/mo (recommended once section 1 is done) | C · ~$900/mo |
|---|---|---|---|
| What runs | Cold email (~100/day once warm), 1 article a day, free directory listings | Meta retargeting, $5/day, glammi.ai visitors only | B + Google Search $25/day on the terms above |
| What it buys | Your real close rate, for free | A second touch for people who already know you. Booked calls: **unknown** until we know glammi.ai traffic | Google part: ~30 clicks → about **1 to 2 booked calls/mo** (at 3% to 8% booking rate, $25 click) |
| Risk | Slowest | Tiny, capped by a spending limit | Real money for few calls. Probably doesn't pay back at $499 unless clients stay 6+ months |

### What a client is worth (all assumptions labeled)
- **Price:** $499/mo *(placeholder: Oct 26 proposal, not confirmed)*
- **Gross margin:** ~60% *(estimate from the same doc)* → **~$299 profit per client per month**
- **Months a client stays:** 3 (the proposed minimum term) or 6 *(my guess, no data)*
- **Profit per client:** **$898** (3 months) · **$1,796** (6 months)
- Not counted: Megan's call time, refunds, taxes, Stripe fees beyond the margin estimate.

**Most you can pay per booked call and still break even** (formula: profit per client × close rate):
| Close rate *(unknown, cold email will tell us)* | If client stays 3 mo | If client stays 6 mo |
|---|---|---|
| 10% | $90 | $180 |
| 20% | $180 | $359 |
| 30% | $269 | $539 |

**What Google might actually cost per booked call** (formula: CPC ÷ share of clicks that book; $25 CPC assumed):
| Booking rate *(assumption)* | Per booked call | Per client at 20% close |
|---|---|---|
| 3% | $833 | $4,167 |
| 5% | $500 | $2,500 |
| 8% | $313 | $1,563 |

**Plain reading:** Google only breaks even if the booking page converts ~8%+ of clicks, you close 20%+ of calls and clients stay ~6 months. That's why it waits. Meta retargeting clicks are usually far cheaper, but we have no Glammi data, so its cost per booked call is **unknown** until we test. **One rule to remember:** at the placeholder price, a paid client must cost less than **~$900** to pay back in 3 months.

**Benchmarks (vendor or practitioner, from search snippets Nov 6, 2026, unverified, not ours):**
| Number | Source (type, date) | Fit / caveat |
|---|---|---|
| Google Ads Business Services avg cost per lead **$103.54**; all-industry CPC $5.26, conv. rate 7.52%, CPL $70.11 | WordStream / LocaliQ 2025 Google Ads benchmarks (vendor), via Search Engine Land | A "lead" there is any form fill, not a booked sales call. Our niche CPCs are 3 to 6x higher. **Poor fit** |
| Google Ads Business Services avg CPC **$5.87** (2026 report) | adwave.com quoting WordStream 2026 (secondhand) | Sources disagree on the 2026 figures. **Uncertain** |
| Meta all-industry CPL **$27.66**, CPC $0.70, CTR 1.71% | WordStream *Facebook Ads Benchmarks 2025* (vendor) | Local consumer businesses, not B2B. Don't use as a target |
| LinkedIn US Sponsored Content CPC **~$6 to $12**; CPL ~$75 to $200 | zenabm (211 B2B companies, 2026), stackmatix (practitioner) | LinkedIn publishes no official averages. **Uncertain** |

## 4. Campaign structure (Option B, then C) + tracking

**Tracking first (nothing runs without it):**
1. **Booking page** at glammi.ai/book with the calendar embedded (logic waiting on your OK in Notion). An embedded calendar lets one small code snippet count a "Booked call" without a paid calendar plan. We draft the snippet, you paste it in Framer → Site Settings → Custom Code.
2. **Meta Pixel + Google tag** on glammi.ai (same place). One conversion only: **Booked call**.
3. **Privacy policy on glammi.ai** that honestly mentions the Pixel and Google tag (we draft it, you OK it). Check that one exists at all.
4. **UTM links** on every ad (`?utm_source=meta&utm_medium=paid&utm_campaign=retarget&utm_content=<concept>`) and one booking question: "How did you hear about Glammi?"
5. **Source of truth = real bookings on your calendar**, not the ad platform's count. Each week we compare them. If they differ by more than ~20%, fix tracking before spending more.
6. Don't upload cold email lists to Meta or Google (that's personal data and needs a privacy decision).

**B · Meta retargeting**
- Ad account "Glammi Studio", USD, Los Angeles time zone, own spending limit (separate from ISSUE11).
- Campaign "Glammi · Retarget · US". Objective **Leads**, optimize for **Booked call**. If it fires fewer than a few times a week, switch the goal to **landing page views** of /book *(provisional, Meta menus change)*.
- Audience: glammi.ai visitors, last 180 days, excluding people who already booked. US only.
- 1 ad set, $5/day, 2 ads (concepts 2 and 3 below). Link to /book.
- ⚠️ **Health-category risk *(unverified)*:** since 2025 Meta has reportedly limited conversion tracking for advertisers it classifies as health and wellness. glammi.ai publishes many treatment articles, so Meta could misclassify Glammi. If Events Manager shows a restriction, we fall back to landing page views.

**C · add Google Search**
- Account in **Expert mode** (skip the Smart campaign Google pushes at sign-up).
- Campaign "Glammi · Search · Agency terms · US". **Search only:** untick Search Partners and Display. Location: US, "presence" only. Hours: Mon to Fri business hours.
- 2 ad groups: **Med spa** ([med spa marketing agency], [med spa website design], [dermatology marketing]) and **AI search** ([ai search agency]). Exact and phrase match only.
- Bidding: Maximize clicks with a max CPC cap *(provisional)*, then switch to conversions only once bookings are counted.
- 1 responsive search ad per group (headlines ≤30 characters, descriptions ≤90 *(provisional)*).
- **Negative keywords:** none invented up front. After week 1 we read the search terms report together and only then propose exclusions.
- **Never put drug names** ("Botox" or other prescription brands) in keywords or ad text. Google and Meta restrict prescription drug terms *(provisional)*.

**Stop rules (you pause, we tell you when):** 0 booked calls after ~$150 on Meta → check the Pixel and page. Google cost per booked call above your break-even (section 3) after ~$500 → pause Google and stay on cold email.

**Competitor check, not done:** ad libraries can't be reached from here. Before launch, a 10-minute look at the Meta Ad Library and Google Ads Transparency Center for the agencies AI names most in our tracking (and nowseen.ai) would show their hooks and offers. You or a browser on your computer can do it.

## 5. Five ad concepts
Rules applied: Glammi voice (witty, sharp, human), no em dashes, no Oxford comma, no banned words, no tool names, no guarantees of AI placement or rankings, no prices, no results we don't have, no client names, no treatment or drug names, no before/after images, no real AI logos (generic chat screen only). Primary text ~125 characters before "more", headline ~40 *(provisional)*. CTA button: **Book Now**.

**1 · The short list**
Hook (on screen): *"Ask AI for the best med spa near you. Count the names."* · Headline: *Is your clinic on the short list?*
- a. Your clients used to get ten blue links. Now they get three names. Glammi helps med spas become one AI can find and trust.
- b. AI answers with a short list. Being great at what you do isn't enough if AI can't find clear information about you.
- c. Somebody asked AI where to book tonight. We check whether your clinic came up, and what to fix if it didn't.

**2 · Ask it yourself** (the call as the offer; wording depends on Question 3)
Hook: *"What does ChatGPT say about your clinic?"* · Headline: *See what AI says about you*
- a. On the call we ask AI the questions your clients ask, live, and show you who comes up. Then the first three things we'd fix.
- b. You check your reviews. When did you last check what AI says about you? Book a call and we'll look together.
- c. No pitch deck. Real AI answers about your business, side by side with the clinics AI picks instead.

**3 · Where AI looks** (real proof: our own tracking, Oct 24 and 27, LA med spa and jeweler questions)
Hook: *"AI didn't read your homepage. It read your Google Maps listing."* · Headline: *Where AI gets its answers*
- a. In our tracking of LA med spa and jeweler questions, Google Maps and Yelp were the sources AI cited most. Is yours ready?
- b. We tracked where AI finds its answers about local beauty businesses. Listings beat websites. Read the full report.
- c. Your website matters. Your listings matter more than you think. See what our tracking found for LA.
*Link: the published article where-ai-gets-answers-la-med-spas-jewelers. Keep "in our tracking" in the line, never "AI always".*

**4 · The ring question** (jewelers)
Hook: *"Someone just asked AI where to buy an engagement ring in your city."* · Headline: *Get your store into the answer*
- a. The ring hunt now starts with a question to AI. Glammi helps jewelers show up with clear and trusted information.
- b. Your window display can't help if the shopper never walks past. Find out what AI tells people about your store.
- c. We check what AI says about your jewelry store, then fix the listings and pages it relies on. You approve everything.

**5 · Can AI read your website?** (website offer; Megan to camera is the strongest format here)
Hook: *"Your website is beautiful. Can AI read it?"* · Headline: *Websites AI can actually read*
- a. A pretty site that AI can't understand is a brochure in a locked drawer. We build sites that look premium and read clearly.
- b. Clear service pages, clean structure and answers to real questions. Built for your clients and for AI search.
- c. If your clinic only has a booking link and an Instagram, AI has very little to go on. We fix that.
*[Megan approves every word and decides if she's on camera.]*

**Med spa note:** these ads sell a marketing service to business owners, so they're not health ads. They still stay clear of treatment claims, patient photos and drug names, so neither Meta nor Google treats them as health ads *(provisional, check policy at launch)*.

## 6. First test (once B is live)
- **Question:** for people who already visited glammi.ai, does **concept 2 "Ask it yourself"** (the call as the offer) or **concept 3 "Where AI looks"** (proof first) get more visits to /book?
- **Setup:** Meta A/B test, same audience, $2.50/day each, same format, 21 days. Only the hook and message change.
- **Measure:** cost per /book visit (main metric, because bookings will be too few to call). Booked calls reported alongside, but not used to pick a winner.
- **Call a winner only if** Meta shows ≥80% chance of winning **and** one ad has ~2x the other's rate. Otherwise "no clear winner".
- **Free pre-test (optional):** the outreach agent could try the same two openers as cold email first lines. Their room decides; I don't touch outreach.
- **Undo:** pausing either ad stops it right away.

## 7. Megan's click list (only when you say go, max 6)
1. **Approve** the booking page logic in Notion, then publish glammi.ai/book in Framer.
2. **Paste** the Pixel + Google tag + "Booked call" snippet we draft into Framer → Site Settings → Custom Code, and approve the privacy policy update.
3. **business.facebook.com** → add an ad account "Glammi Studio" (USD, Los Angeles time; you can't change these later), add your card, then **Billing → Account spending limit = $150**.
4. **Events Manager → Connect data → Web → Meta Pixel** for glammi.ai. Send us the Pixel ID (it isn't a secret).
5. *(Option C only)* **ads.google.com** → sign up, choose **Switch to Expert Mode**, add your card. Send us the 10-digit customer ID.
6. **Press Publish** on the campaign using our click-by-click sheet.

## 8. Questions for Megan (max 3)
1. **What price should the math use?** Recommend: **AEO Essentials $499/mo with a 3-month minimum** (the Oct 26 proposal) as a planning number, until you confirm the real one. Ads never show the price either way.
2. **Budget?** Recommend: **$0 for now (Option A).** Revisit B when the booking page, tracking and Stripe are live and cold email has brought ~10 booked calls.
3. **What do people book?** The VSL says a **free 15-minute AI visibility check** and the live calendar link is a **30-minute discovery call**. Recommend **one CTA: "Book a discovery call"** (it's already on every article and profile), with the ad saying what happens on it ("we check what AI says about you, live").

**Missing data (not guessed):** glammi.ai monthly visitors (sets the retargeting audience size) · whether glammi.ai has a privacy policy · your close rate (cold email will show it) · how long clients stay.

---
Sources (retrieved Nov 6, 2026, search snippets only, unverified):
- [Search Engine Land: Google Ads costs rising, conversion rates improved in 2025](https://searchengineland.com/google-ads-costs-rising-but-conversion-rates-improved-in-2025-477927)
- [adwave: Google Ads cost benchmarks](https://adwave.com/resources/google-ads-cost-benchmarks)
- [WordStream: Facebook Ads Benchmarks 2025](https://www.wordstream.com/blog/facebook-ads-benchmarks-2025)
- [WordStream: Google Ads industry benchmarks](https://www.wordstream.com/resources/google-ads-industry-benchmarks) (blocked here, not opened)
- [ZenABM: LinkedIn Ads Benchmarks 2026](https://zenabm.com/blog/linkedin-ads-benchmarks-2026.md)
- [Stackmatix: LinkedIn Ads cost 2026](https://www.stackmatix.com/blog/linkedin-ads-cost)
- Internal: keyword data in `.pipeline/lessons.md` (Oct 28, Oct 29, Oct 30) and `drafts/glammi-blog/` article headers (Nov 4 to 5); citation data in `.pipeline/lessons.md` (Oct 29).
