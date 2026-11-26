# I11-ASO-001 · ISSUE11 ASO launch strategy (prelaunch + first 30 days)
Nov 26, 2026 · 💚 GROWTH — ASO & Opportunity Scout, coordinated by 🩶 OPS · Handoff: Notion "🤝 AI Collaboration Room", I11-ASO-001 · Independent evaluators: 🩶 OPS (internal), then ChatGPT.
Skills loaded: `aso` (audit method), `aso-specialist` (limits, copy blocks), `graphify` (graphs/marketing has no ASO node, so I read drafts/aso directly). Framework: App Masters "5 big + 20 small" (Notion Source Log; summary only).
**Budget used: $0 incremental.** Applyra: 3 new inspections + 3 autocompletes inside the existing Unlimited plan (126 of 10,000 requests this month). ASOMobile: 0 tokens spent (1 left). No Apify. Nothing submitted, no App Store Connect access, no live metadata change.

**Goal (Megan):** $10,000 MRR, not vanity rankings. So every keyword below is judged on four things: demand, winnability, product fit, and whether the searcher is likely to **pay and stay**.

---
## 0. Summary and the 3 decisions only Megan can make
**Recommendation:** keep the name and subtitle. Submit the **v16 keyword field** below on Dec 4 (v15.1 + `2027`, `journaling` out, **no `free`**). Run 3 custom product pages from launch week. Measure everything against the $10K MRR model in §8, not against rank alone.

1. **Drop `free` from the keyword field.** Recommended: yes. Apple guideline 2.3.7 (re-read Nov 26) says not to pack metadata with "pricing information", and Applyra's checker flags `free` as a price term. The Nov 26 "add free" decision risks a rejection or Apple silently editing keywords right before a fixed Dec 11 date. Keep "7 days free" in the description and paywall only, and retest `free` in an update after launch.
2. **Approve the v15.1/v16 keyword swap** (`scripting` out → `maker`, `personal`, `2027` in). Recommended: yes. Your approval of v15.1 isn't recorded in the repo, so the baseline is ambiguous (v15 approved Nov 19; v15.1 proposed Nov 21–22; on Nov 26 you referred to the field as "96/100", which is v15.1).
3. **Angel numbers and subliminal sessions: in the Dec 11 build or not?** These are in the es-MX keyword field. The Oct 5 plan put them in the beta, but the Nov 22 launch feature list doesn't include them. If they don't ship, swap those 3 words before Dec 4 (Apple 2.3.7: keywords must describe the app accurately).

---
## 1. Baseline (facts, Nov 26)
| Item | State | Source |
|---|---|---|
| App on the App Store | **Not live.** iTunes Search for "issue11" returns only newsstand apps. | Live check Nov 26 |
| Rankings, impressions, conversion, revenue | **None yet** (nothing to measure until Dec 11) | — |
| Approved metadata | v15: US `ISSUE11: Manifestation Journal` (30) / `Manifest with a Vision Board` (28) / keywords v15 (91). es-MX `ISSUE11: Law of Attraction` / `Manifesting Digital Scrapbook` / keywords (96) | drafts/aso/2026-11-18-listing-v15.md |
| Proposed, approval not recorded | v15.1 keyword field: `scripting` → `maker`, `personal` (96) + new description opening + promo text + caption 3 "move" → "action" | drafts/aso/2026-11-22-keyword-optimization.md |
| Decision Nov 26 | Add `free` at the Dec 1 recheck | .pipeline/lessons.md |
| Prices | $9.99/mo (no trial) · $69.99/yr with 7-day trial · founding $39.99 first year until Jan 11, 2027 | lessons Nov 24, signin-payments spec |
| Dates | Submission Fri Dec 4 · public launch Dec 11 | OPS Nov 20 |
| Paid acquisition | Meta waitlist test ~$10/day started Nov 26 | lessons Nov 26 |
| Data sources | Applyra (Unlimited, 0–100 estimates) · ASOMobile Nov 18 export (traffic = estimated searches/day; 1 token left) · iTunes Search API (free, close to but not identical to iPhone search) | drafts/aso/exports/2026-11-18/ |

---
## 2. Audit of the current strategy and metadata (aso skill, Challenger tier, prelaunch)
Only the dimensions that exist before launch can be scored. Ratings, reviews and freshness score at launch.
| Dimension (aso skill weight) | Prelaunch read | Score |
|---|---|---|
| Title & subtitle (20%) | 58/60 characters used. Big terms placed (manifestation journal, manifest, vision board). Brand + keyword balance good. | 9/10 |
| Keyword field | Valid, no repeats, but v15 still spends 10 bytes on `scripting` (coding-app intent) and 11 on `journaling` (difficulty 70, giants). v16 fixes both. | 6/10 → 8/10 with v16 |
| Description (15%) | Written by Megan, not in the repo, so can't be audited. Apple doesn't index it (conversion only). | n/a |
| Visual assets (25%) | 6 mockups with sample content. **Real captures don't exist yet** (needs the build). Caption 3 in v15 still uses the banned word "move". | 3/10 (blocker) |
| Ratings (20%) | 0 (prelaunch). | n/a |
| Metadata & freshness (10%) | Category Health & Fitness + Lifestyle never checked against live charts. Privacy/support/terms URLs not live (drafts/aso/2026-11-20-asc-submission-checklist.md). | 4/10 |
| Conversion signals (10%) | Trial on yearly, clear prices, founding offer with a real end date. | 7/10 |
**Biggest risks are not keywords:** (1) no real screenshots until a build exists, and (2) privacy/support URLs and the App Privacy answers are still open. Either can move the Dec 11 date.

---
## 3. Validating "5 big + 20 small" (App Masters)
**Verdict: keep the structure, but change what counts as "small".**
- ✅ **Big 5 in the name/subtitles** is right and already done: manifest (subtitle), vision board (subtitle), manifestation (name), scrapbook and law of attraction (es-MX subtitle and name; es-MX indexing in the US is **unverified**).
- ⚠️ **The 20 small list (Nov 18) is half empty.** 14 of 20 sit at Applyra's floor (traffic 8), which means near-zero searches. Winning them gives rank screenshots, not revenue. For a $10K MRR goal, "small" should mean **low difficulty AND measurable demand AND buyer intent**.
- ⚠️ **Missing training:** the App Masters video was never transcribed (Notion Source Log: "Full video not yet transcribed: link pending"). Everything here uses the 1-line summary. **Ask: share the video link** so the framework can be checked against the source.
- **Revised small list (revenue-weighted)**, all buildable from US fields:
  manifestation journal · journal prompts · daily journal prompts · moodboard · mood board · dream board · manifesting · vision board maker · zine maker · mood board maker · magazine maker · scrapbook journal · manifestation journal prompts · manifesting journal · manifestation magazine · personal magazine · vision board magazine · vision board scrapbook · vision board 2027 · manifest vision board
  The first 11 have measured demand. The last 9 are kept as cheap, near-empty niches (no extra bytes) and **not counted toward targets**.

---
## 4. Keyword matrix (US, iPhone)
Columns: **Applyra** traffic/difficulty (0–100, date) · **ASOM** = ASOMobile estimated searches/day (Nov 18 export) · **Top competitors live** (rating counts, iTunes Search Nov 20/26) · **Intent**: M = manifestation, MAG = magazine-making, R = self-reinvention, G = generic · **Fit** = product does it (Apple 2.3.7) · **$** = likely to pay for a subscription (judgment, labeled) · **Field** = v16 coverage (N name, S subtitle, K keywords, MX es-MX listing, CPP custom product page).
| Keyword | Applyra T/D (date) | ASOM /day | Top competitors live | Intent | Fit | $ | Field |
|---|---|---|---|---|---|---|---|
| manifest | 74/70 (Nov 18) | 1,066 | ⁢Manifest 2,859 · Stella 5,686 · Soul 3,804 | M | ✅ | High | S |
| vision board | 52/67 (Nov 18) | 923 | Vision Board & Goal Tracker 3,760 · 2027 VB Maker 613 · VB++ 3,097 | M | ✅ | High | S |
| mood board | 41/45 (Nov 18) | 781 | Moodboard 1,825 · Milanote 4,144 · Morpholio 3,760 | G (design) | ✅ | Low–Med | K+S |
| scrapbook | 52/64 (Nov 18) | 780 | Planly 74 · Nooka 60 · Dotie 24 | MAG | ✅ | Med | K+MX |
| journaling | 61/70 (Nov 18) | 624 | Journal 327K · Day One 118K | G | ✅ | Med | out in v16 |
| magazine | 77/74 (Nov 18) | 567 | newsstands | G | partial | Low | K |
| digital scrapbook | 22/45 (Nov 18) | 431 | Planly 74 · Tomobook 56 · Nooka 52 | MAG | ✅ | Med | MX+K |
| moodboard | 59/54 (Nov 18) | 393 | Moodboard 1,825 · Milanote 4,144 | G | ✅ | Low–Med | K |
| manifestation | 41/62 (Nov 18) | 301 | Stella 5,686 · I am 739,813 · Aya 3,219 | M | ✅ | High | N |
| journal prompts | 45/47 (Nov 18) | 288 | solo. 6 · Ink 17 · Prompted 6,906 | M/G | ✅ | Med | N+K |
| law of attraction | 48/58 (Nov 18) | 276 | LoA Toolbox 3,012 · LoA Affirmations 2,194 · LoA Space 13 | M | ✅ | High | MX |
| manifestation journal | 43/40 (Nov 18) | 246 | Myla 750 · Manifestation Journal 34 · Soul 3,817 | M | ✅ | **High** | N (exact) |
| daily journal prompts | 25/53 (Nov 18) | 213 | Ink 17 · Quill 2 · Day One 119K | G | ✅ | Med | K+N |
| manifesting | 25/30 (Nov 18) | 162 | Stella 5,686 · Myla 749 · Soul 3,804 | M | ✅ | High | K+MX |
| dream board | 25/35 (Nov 18) | 155 | VB & Goal Tracker 3,760 · Dreamboard 322 · VB 4 | M | ✅ | Med–High | K+S |
| **zine maker** | **48/13** (Nov 26) | not measured | Artino 3 · EZZINE 12 · AnyPiece 0 | MAG | ✅ | Low–Med | K (`zine`+`maker`) |
| mood board maker | 45/38 (Nov 22) | not measured | Moodboard 1,826 · LiveCollage 180K · Morpholio 3,761 | G | ✅ | Low–Med | K+S |
| magazine maker | 37/32 (Nov 21) | Search Ads 23 | Magazine Cover Maker 3,144 · Canva 3.6M · Cover Me 41 | MAG (fake cover) | partial | Low | K |
| **vision board maker** | 25/54 (Nov 18) | "…free" 413 | **VB Maker: Manifest 2** · 2027 VB Maker 610 · VB++ 3,109 | M | ✅ | Med–High | S+K |
| vision board free | 23/23 (Nov 22) | autocomplete #5 | VB Maker 337 · VB++ 3,109 · VB & Goal 3,761 | M (price-seeking) | ✅ | **Low** | not in v16 (2.3.7 risk) |
| vision board 2027 | 8/33 (**Nov 26**, still floor) | n/a | Vision Board 2027 (4.6★) + many new tiny apps | M (seasonal) | ✅ | Med–High | K (`2027`) + MX |
| personal magazine | 8/22 (**Nov 26**, still floor) | C 6.9 | ZINIO · Personal Care Magazine · Cosmopolitan (newsstands) | MAG | ✅ | Med | K |
| self love | 52/59 (Nov 18) | 276 (C 7.0) | affirmation / self-care apps | R | partial | Med | MX |
| glow up | 50/67 (Nov 18) | 1,313 | looksmaxxing / beauty | R (wrong) | ❌ | — | no |
| personal rebrand | 9/31 (Nov 18) | n/a | — | R | partial | — | no |
| future self | 36/49 (Nov 18) | 3 | face-aging apps | R (wrong) | ❌ | — | no |
| affirmations | 25/88 (Nov 18) | 1,615 | I am (#1) | M | partial | High | **out** (Megan Nov 18) |
| gratitude journal | 52/87 (Nov 18) | 898 | Gratitude 45K | G | partial | Med | MX |
| angel numbers / subliminal | 54/31 · 58/54 (Nov 18) | not measured | small apps | M | ❓ not in the launch list | Med | MX (decision 3) |
Autocomplete (Apple suggestions via Applyra, Nov 26): "vision board" → **vision board maker free, free vision board app, vision board free**, vision board widget, vision board maker · "magazine" → magazine cover maker, magazine maker · "manifest" → manifestation journal, manifest free, manifest love.
**Missing data:** ASOMobile searches/day for zine maker, mood board maker, journal prompts combos; Apple Search Ads popularity (needs an Apple Ads account, after launch); any real ISSUE11 rank or conversion.

---
## 5. Realistic #1 opportunities (evidence + uncertainty, no guarantees)
| # | Keyword | Why #1 is credible | Revenue value | Main uncertainty |
|---|---|---|---|---|
| 1 | **manifestation journal** | Exact phrase in the name. #2 has 34 ratings; #1 (Myla) has 750. 246 searches/day, difficulty 40. | **Highest:** manifestation is a proven subscription category (Stella, I am). | Passing Myla needs ratings + installs; #2–3 likely first. |
| 2 | **vision board maker** | #1 today has **2 ratings**. Top Apple autocomplete for "vision board" is "vision board maker free". `maker` + subtitle "Vision Board" cover it. | High: vision board is our entry point (My saves). | Difficulty 54 (Applyra) despite tiny #1; many new seasonal apps launch in December. |
| 3 | **zine maker** | Best traffic/difficulty in the set (48/13). Top 3 have **0–12 ratings**. | Low–medium: creative-tool searchers; ISSUE11 is a paid habit + magazine, not a free zine tool. | Applyra only (ASOMobile not measured); "zine" traffic was inflated by "Zain" telecom apps before. |
| 4 | **journal prompts** (+ daily journal prompts) | Leaders have **6 and 17** ratings. 288 + 213 searches/day. Prompts ship in Journal. | Medium: journaling users pay, but many want free prompts. | Prompted Journal (6.9K) and Day One sit right behind. |
| 5 | **scrapbook / digital scrapbook** | Top apps 24–74 ratings. 780 + 431 searches/day. | Medium: fits "your saves become pages". | Applyra difficulty 64 conflicts with the tiny rivals; es-MX dependence for "digital". |
Not #1 candidates in year 1: manifest, vision board, manifestation (3,000–740K-rating incumbents). Aim for top 10.

---
## 6. Magazine-making vs manifestation vs self-reinvention (evaluated separately)
| | Manifestation | Magazine-making | Self-reinvention |
|---|---|---|---|
| App Store demand | **Largest and proven**: manifest 1,066/day, vision board 923, manifestation journal 246 | Small in the store: magazine maker 37 (Applyra), zine maker 48, personal magazine **floor (8), still flat Nov 26** | Big words are the wrong intent (glow up = beauty, future self = face-aging); right-intent terms are at the floor (personal rebrand 9) |
| Demand outside the store | Steady | **Rising on TikTok** ("pinterest magazines" +1000% in 7 days, "personalized magazine gift" 80–108K; ICP-DETAILED Nov 21). Not in App Store search yet. | Strong in content (Pinterest pillar "personal rebrand + glow up") |
| Competition | Strong incumbents (Stella, I am, Soul) | Weak, and a different product (fake covers, zine tools, newsstands) | n/a |
| Payer intent (judgment) | **High:** the category already pays subscriptions | Mixed: one-off creative tools and gift searches; some want a free cover | Medium, but not through App Store search |
| Product fit | ✅ core loop (vision board → journal → action) | ✅ the differentiator (your Issue) | ✅ positioning, not a search term |
| **Role in ASO** | **Lead:** name, subtitle, main CPP | **Hidden field + 1 CPP + social.** Lets us be indexed early if the TikTok trend reaches the store | **Content and Pinterest, not metadata** |
This matches I11-001's hypothesis (magazine intent may convert better on social). ASO should not wait for that test, but CPP #2 (below) can measure the store side of it.

---
## 7. Final metadata recommendation (v16, for Megan's OK; not submitted)
```
[TRACKING DATA-FIELD: US · App Name (30/30)]      ISSUE11: Manifestation Journal                       (unchanged)
[TRACKING DATA-FIELD: US · Subtitle (28/30)]      Manifest with a Vision Board                         (unchanged)
[TRACKING DATA-FIELD: US · Keywords (90/100)]     magazine,moodboard,mood,scrapbook,prompts,dream,manifesting,zine,daily,maker,personal,2027
[TRACKING DATA-FIELD: es-MX · App Name (26/30)]   ISSUE11: Law of Attraction                           (unchanged)
[TRACKING DATA-FIELD: es-MX · Subtitle (29/30)]   Manifesting Digital Scrapbook                        (unchanged)
[TRACKING DATA-FIELD: es-MX · Keywords (96/100)]  loa,inspiration,self,love,mindset,visualization,gratitude,subliminal,angel,numbers,2027,new,year   (decision 3)
```
Checked with Applyra `check_metadata` (Nov 26): **valid, 0 duplicates, 0 wasted bytes.** The variant with `free` (95/100) returned a **2.3.7 "price" warning**, so `free` is left out.
| Change vs v15 | Why |
|---|---|
| − `scripting` | Coding-app intent; its combos sit at the floor (8). |
| − `journaling` | Difficulty 70, owned by Journal (327K) and Day One (118K). "journal prompts" is still covered by name + `prompts`. |
| + `maker` | Unlocks vision board maker (#1 has 2 ratings), zine maker (48/13), mood board maker (45/38), magazine maker (37/32). |
| + `personal` | Early index on "personal magazine" before the TikTok trend reaches the store (still floor Nov 26). Weakest word in v16; first to swap if a measured term appears. |
| + `2027` | US-only coverage of "vision board 2027" in peak season (es-MX indexing unverified). Swap in the early-February update. |
| 10 bytes left | Reserved for the **Dec 1 recheck** (seasonal and new-year terms). Fill only with a measured term, otherwise submit at 90. |
Also carry over from the Nov 22 draft (pending Megan): promo text (161), description opening ("Make your own personal magazine…"), **caption 3 "move" → "action"** (banned word in the approved v15).

### Custom product pages (Apple: up to 70; keywords can be assigned, and each keyword combination may sit on one page only. Apple docs, checked Oct 4)
| CPP | Assigned keywords (must be eligible in App Store Connect: verify there) | First 3 screenshots |
|---|---|---|
| 1 · Manifestation journal (default page) | manifestation journal, journal prompts, manifesting journal | Journal wall with today's prompt → Write → the line becoming a page |
| 2 · Make your own magazine | zine maker, personal magazine, scrapbook, magazine maker | Saves → 40-page Issue → cover with you on it (*printed copy sold separately*) |
| 3 · Vision board 2027 (Dec 11–Jan 31) | vision board maker, vision board 2027, dream board | My saves board → "The New Year Issue" cover → one small action |
Each needs real-app screenshots (Apple). Whether CPPs can go live without a new app version: **verify in App Store Connect** (not confirmed).

---
## 8. Reverse-engineering $10K MRR (assumptions labeled)
| Assumption | Value | Basis |
|---|---|---|
| A1 Plan mix | 70% yearly / 30% monthly | **Assumption**: trial pre-selected on yearly |
| A2 Gross per subscriber per month | yearly $69.99/12 = $5.83 · monthly $9.99 → blended **$7.08** | Prices (Nov 7/24 decisions) |
| A3 Founding period | until Jan 11, yearly is $39.99 → blended **$5.33** | Decision Nov 24 |
| A4 Apple fee | 15% (Small Business Program) → net blended **$6.02** | Apple program; enrolment unverified |
| A5 Download → paid (35 days) | 1.5% / **2.9%** / 5% | RevenueCat 2026 benchmark via search summaries (H&F median 2.9%); 1.5% and 5% are our scenarios |
| A6 Monthly-plan churn | 15%/month | **Assumption** |
| A7 Yearly churn in year 1 | 0% (renewals start Dec 2027) | Plan mechanics |
**Target math:** $10K gross MRR = ~**1,412** active subscribers at the full price (1,662 for $10K net; ~1,876 if everyone were on the founding price).
**Model** (A1, A2, A6, A7; gross MRR, full price):
| New paying subs / month | Month 3 | Month 6 | Month 12 |
|---|---|---|---|
| 150 | $3.0K | $5.5K | **$9.9K** |
| 250 | $5.0K | **$9.2K** | $16.5K |
| 350 | $7.0K | $12.9K | $23.1K |
**What that needs:** ~250 new paying subs a month reaches $10K MRR around **month 6–7 (June–July 2027)**. That takes **8,600 downloads/month at 2.9%**, 5,000 at 5%, or 16,700 at 1.5%.
**Can ASO alone deliver it?** In season, the Nov 20 model gives ~330 search downloads/day (~9,900/month) at realistic ranks. After January, search demand is expected to roughly halve (October numbers were ~½ of November's), so ~3–5K/month from ASO. **ASO alone reaches $10K MRR only if conversion is ≥5%**. Otherwise Pinterest, SEO and Meta have to fill the gap. This is why conversion (cover reveal before the paywall) matters as much as rank.

---
## 9. Prelaunch + first 30 days execution plan
| Date | Action | Owner | Done when |
|---|---|---|---|
| Nov 26–27 | Megan: decisions 1–3 (§0); featuring nomination submitted | Megan | Answers logged in lessons |
| **Mon Dec 1** | Seasonal + `personal magazine` recheck (Applyra; ASOMobile last token only if one term decides the 10 bytes). Freeze v16. | ASO Scout | v16 final + check_metadata valid |
| Dec 1–2 | Real screenshots from the build (6 + 3 CPP sets), captions per v15 with the "action" fix | Design + build | 1320 × 2868 real captures |
| Dec 2–3 | All App Store Connect fields (checklist Nov 20): privacy/support/terms URLs live, App Privacy, age rating 16+, subscription names | Megan | Checklist all ✅ |
| **Fri Dec 4** | Megan submits (agents never do) | Megan | "Waiting for Review" |
| Dec 5–10 | If approved early: pre-order or scheduled release (verify availability in ASC); New Year Issue In-App Event drafted (Apple: promoted up to 14 days before start, max 31 days) | Megan + ASO Scout | Event approved |
| **Dec 11–14** | Launch burst: waitlist email + Pinterest + Instagram + Meta point to the App Store on the same days; ask beta testers to rate honestly | Growth Lead | Installs concentrated in 72 h |
| Dec 11+ | Rating prompt right after the first cover reveal (Apple: max 3 prompts per year); reply to every review | Product + Megan | ≥20 ratings by Dec 25 |
| Dec 12 | Start tracking all v16 + small-list keywords in Applyra (adds them to Megan's Applyra account, not the store) | ASO Scout | Daily rank file |
| Dec 15–Jan 10 | Daily scorecard (§10); weekly review on Mondays | ASO Scout → OPS | Scorecard filled 7/7 days |
| ~Jan 5 | First metadata update (v17) using real ranks: App Masters rules (keep 1–3, add weight to climbing 4–20, swap stuck past 20) | ASO Scout → Megan | Megan approves before submission |
| Early Feb | Swap `2027` / `new,year`; retest `free` (if Megan still wants it) in its own update, so any rejection is isolated | ASO Scout → Megan | — |

---
## 10. Daily monitoring, success criteria, feedback loops
**Data access (genuine blocker to solve before Dec 11):** agents can't open App Store Connect. Daily impressions, product page views, conversion and source split need **one read path**: Megan pastes the App Store Connect Analytics numbers daily (5 min), or RevenueCat dashboard access for trials/paid. Rankings come from Applyra tracking.
**Daily scorecard (from Dec 12):**
| Metric | Source | Day 7 target | Day 30 target | Stop / fix trigger |
|---|---|---|---|---|
| Rank: manifestation journal | Applyra | top 10 | top 3 | not top 20 by day 14 → check indexing, conversion |
| Rank: vision board maker, zine maker, journal prompts, scrapbook | Applyra | top 20 each | ≥2 in top 3 | stuck past 20 at day 21 → swap word in v17 |
| Search impressions → page views → installs | ASC Analytics (Megan) | baseline | conversion ≥ category norm (to set from week 1) | page-view → install < 20% → screenshots before keywords |
| Downloads/day (search vs other) | ASC | ≥100/day launch week | ≥150/day search | <50/day search by day 14 → push CPPs + In-App Event |
| Trial starts / installs | RevenueCat | ≥8% | ≥10% | <5% → paywall/cover reveal, not ASO |
| Trial → paid (yearly) | RevenueCat | (trials end day 7+) | ≥35% (H&F benchmark) | <25% → onboarding |
| Ratings count / average | ASC | ≥10 / ≥4.5 | ≥40 / ≥4.5 | any "not free" or billing complaint → fix copy that week |
| New paying subs / month | RevenueCat | — | ≥150 (on path to §8) | <80 by day 30 → escalate channel mix to Megan |
**Loop:** daily scorecard → Monday review (ASO Scout drafts, OPS checks the evidence) → one change per update (keywords OR screenshots, never both) → Megan approves → next update. Retries: max 3 corrective attempts per keyword before it's swapped for good.

---
## 11. Advanced, Apple-compliant techniques we haven't used yet
| Technique | Apple status | Cost | When |
|---|---|---|---|
| Custom product pages with assigned keywords (§7) | Apple docs, verified Oct 4 | $0 | Launch week |
| Product page optimization (A/B up to 3 treatments of icon/screenshots) | Apple feature | $0 | After ~2 weeks of traffic |
| In-App Events ("The New Year Issue", then monthly "the 11th") | Apple docs: up to 31 days, promoted 14 days ahead; search card shows only to existing users | $0 | Dec 11 |
| App preview video (15–30 s, real app, autoplays muted) | Apple feature | Megan's time | v17 |
| Promotional text rotation (no app update needed, doesn't rank) | Apple | $0 | Weekly in season |
| English (UK/AU/CA) localizations: separate keyword fields for those stores | Industry practice; how Apple falls back between English listings is unverified | $0 | v17 test |
| Offer codes for the waitlist / founding rate; win-back offers for lapsed subscribers | Apple subscription offers (win-back availability: verify in ASC) | $0 | Launch / month 2 |
| Apple Ads on brand + exact terms (gives Apple popularity data) | Paid | **needs Megan's budget OK** | After organic baseline |
| Featuring nomination (spread layout on the foldable iPhone) | Apple | $0 | Drafted; Megan submits |
**Not allowed (and not proposed):** paid or incentivized reviews, download farms, competitor names or prices in metadata, fake-cover "magazine cover maker" wording in visible fields.

---
## 12. Skill instructions used (for ChatGPT's review)
- `aso-specialist` (Lacey, MIT, `.claude/skills/aso-specialist/SKILL.md`): limits (title/subtitle 30, keywords 100, comma, no spaces); copy-paste blocks labeled `[TRACKING DATA-FIELD: …]` with counts; localization by storefront. Its "percentage lift projections" step is **not** followed: there's no data to base them on (trust rule).
- `aso` (`.claude/skills/aso/SKILL.md`): Phase 1.5 brand tier (ISSUE11 = Challenger, so strict textbook ASO); 6 weighted dimensions; Apple facts (don't repeat words across fields; first 3 screenshots show in search; CPPs in organic search; In-App Events indexed; rating prompt max 3/year). ISSUE11 overrides: agents draft, Megan acts; no paid tools without OK; real proof only.
- App Masters "5 big + 20 small" (Notion Source Log, summary only; **video not transcribed**).
- Team rules applied: never pick a keyword one tool alone loves; Applyra floor = 8 means near-zero demand; the hidden field is where off-store trends wait; never touch App Store Connect.

## 13. What I did NOT do
No App Store Connect access, no submission, no Applyra app or keyword tracking added (the app isn't live), no ASOMobile tokens, no Apify, no edits to the approved v15 file's fields, and no edits to skills.
