# ASO re-check: metadata v8 vs the ASO Specialist skill (Oct 4, 2026)

By 💚 GROWTH — ASO & Opportunity Scout. **Method:** `.claude/skills/aso-specialist/SKILL.md` (Lacey's "ASO Specialist" plugin v1.1.3, MIT, added to the repo so cloud agents can use it). Its steps: keyword architecture → iOS title/subtitle/100-char keyword field + categories → validation with exact character counts.
**Inputs:** `drafts/aso/ASO-BRIEF-for-skill.md`, Notion "Scout's opinion … v8 (DRAFT)" and "Listing Plan vs Round 1", `marketing/PRODUCT-ARCHITECTURE.md`, `brand/BRAND-GUIDE.md`, `.pipeline/app-store-checklist.md`. Notion pages were read only, not edited.

## What was verified, and what wasn't
- ✅ **Verified live (Oct 4) on developer.apple.com:**
  - Name and subtitle can be up to 30 characters each. The keyword field holds 100 characters, comma-separated with no spaces.
  - Don't repeat words that are already in the name, subtitle or category in the keyword field. Don't use competitor app names.
  - Ranking uses the title, subtitle, keywords and primary category, plus user behavior. Promo text doesn't rank.
  - The subtitle only changes when you submit a new app version.
  - Custom product pages can be given their own keywords, show up in search, and work for pre-orders.
  - In-App Events: the card shows in search only for people who already downloaded the app. Max 31 days, promoted up to 14 days ahead. Name up to 30 characters.
- ✅ **Verified by script:** all character counts below and duplicate words. Everything fits. No word in a keyword field repeats a word from that listing's name or subtitle.
- ❌ **Not verified live:**
  - The App Store and the iTunes search API are blocked from this environment (timeouts).
  - Popularity numbers (44/40/24…) are from Round 1 (Sep 2026, Keyword Monitor). They were not re-measured.
  - Two beliefs come from the ASO industry, not from Apple, and I couldn't check either: that the Spanish (Mexico) listing is indexed in the US store, and that keyword combos work across the two listings.
- ⚠️ **Where I didn't follow the skill:** it asks for "percentage lift projections". We have no conversion data, so any number would be made up. Skipped (CLAUDE.md rule 9: nothing fake). Its Google Play steps don't apply (iOS only).

## Verdict per item

| Item | Verdict | Why |
|---|---|---|
| Title `ISSUE11: Manifestation Journal` (30/30) | **Keep** | Exactly at the limit. "manifestation journal" is still the easiest #1 in Round 1 (top rival 363 ratings). Locked by Megan. |
| US subtitle `Manifest with a Vision Board` (28/30) | **Keep** | Carries the 2 biggest measured words (manifest 44, vision board 40). It also matches **Your World**. |
| "manifest" (44) realistic at launch? | **Keep, low expectations** | Top result Stella has 5.1K ratings, but Round 1 saw a 3-rating app ranking. Being in the subtitle is cheap. The real launch win is "manifestation journal". Judge in Round 2. |
| US keywords v8 | **Change (1 word + 1 swap)** | `goals` turns ISSUE11 into a goal-setting app (locked architecture says never). It also pulls in goal-tracker searchers. `self` repeats "Self" in the Mexico subtitle. See v9. |
| Mexico listing v8 | **Change** | Its keyword field repeats `manifest, journal, vision, board`, which are already in the US name and subtitle. If the listings combine, that's ~30 wasted characters. `goal` has the same problem as above. See v9. |
| "magazine" in the keyword field only | **Keep** | It matches **Publish** without leading with it in the title. |
| Oct 2 decision: no "magazine maker" | **Keep** | Those searchers want fake Vogue/Forbes covers (wrong intent, risk under guideline 5.2). Test "personal magazine" in Round 2. |
| Category: Health & Fitness + Lifestyle | **Unsure** | No live chart check. Note: keywords must avoid "health", "fitness" and "lifestyle" (✅ none used). Health & Fitness raises the bar on wellness wording (1.4.1). |
| "visualization", "audio", "affirmations" | **Change: now allowed** | Audio ships in V1 (Oct 1). Add `audio` (US) and `affirmations, guided, ritual` (Mexico). "affirmations" is **unsure**: I Am owns it. It's here for combos (manifestation affirmations), not to rank on its own. |
| Unmeasured words (magazine, photo, diary, intention, reflection, aesthetic, moodboard, inspiration, 2027, new year) | **Unsure** | Still hypotheses. Measure before late Dec, as planned. |
| `2027,new,year` | **Keep + plan the swap** | They fit the Jan 11 vision-board season. Keywords only change with a new app version, so **plan a February update** to swap them. |
| Captions 1–3 | **Keep 1 and 3, tweak 2** | They match Scribe, Your World and Publish. Audio has no caption yet. Add caption 4 for it: "Step into your future with audio". All real UI only. |
| Captions help ranking | **Unsure (bonus only)** | Industry reports say yes, Apple doesn't say so. The decision stands: never rely on captions alone. |
| Fit with the locked architecture | **Keep, 1 fix** | No "AI" in the listing, no chatbot words, Lucky Star not named (correct: lead with the magazine). The only conflict is `goals`/`goal`. |
| UK/AU/CA storefronts | **Missing** | The skill flags UK spelling (visualisation, personalise). There's no English (UK) or English (Australia) listing yet. One could add a second keyword field for those stores. Unverified how Apple falls back between English listings. |
| In-App Event + custom product pages | **Missing** | See change 3. |

## Proposed v9 (DRAFT, counts by script)
Copy-paste blocks in the skill's format:
```
[TRACKING DATA-FIELD: US · App Name (30/30)]       ISSUE11: Manifestation Journal
[TRACKING DATA-FIELD: US · Subtitle (28/30)]       Manifest with a Vision Board
[TRACKING DATA-FIELD: US · Keywords (88/100)]      scripting,magazine,photo,diary,intention,reflection,lucky,girl,audio,aesthetic,moodboard
[TRACKING DATA-FIELD: es-MX · App Name (26/30)]    ISSUE11: Law of Attraction
[TRACKING DATA-FIELD: es-MX · Subtitle (28/30)]    Manifesting Your Future Self
[TRACKING DATA-FIELD: es-MX · Keywords (89/100)]   loa,concept,visualization,assumption,affirmations,guided,ritual,inspiration,2027,new,year
[TRACKING DATA-FIELD: In-App Event · Name (18/30)] The New Year Issue
[TRACKING DATA-FIELD: Category]                    Primary: Health & Fitness · Secondary: Lifestyle (unchanged, unsure)
```
Keyword-field rules checked: no spaces, no repeats within a field, no repeats between the US and Mexico fields, no repeats of the name, subtitle or category words, no competitor names.

**🇺🇸 US** · title and subtitle unchanged
- `goals` → `audio`. Audio ships, and it isn't a productivity word.
- `self` → `lucky`. "self" is already in the Mexico subtitle. "lucky" fits the Lucky Star brand and "lucky girl" manifestation searches. **Unmeasured.**

**🇲🇽 Spanish (Mexico)** · title and subtitle unchanged
`loa,concept,visualization,assumption,affirmations,guided,ritual,inspiration,2027,new,year` **(89/100)**
- Removed `manifest, journal, vision, board` (repeats of the US words) and `goal`.
- Added `affirmations, guided, ritual` (Audio). 11 characters left on purpose: fill them after measuring.

## The 3 most important changes
1. **Remove `goals`/`goal` and add Audio words.** These are the only two changes that fix a real mismatch: `goals` contradicts the locked architecture ("never a goal-setting app"), and audio now ships, so it's honest to target it.
2. **Stop repeating US words in the Mexico keyword field.** This gives back ~30 of 100 characters for free, provided the cross-listing indexing holds (industry belief, unverified here). Even if it doesn't hold, removing the repeats costs nothing.
3. **Add two launch tools:**
   - **A "vision board" custom product page.** Assign the keywords vision board / vision board 2027 and use Your World screenshots. This is verified Apple functionality.
   - **A "New Year Issue" In-App Event** (18/30) around Jan 11. Event cards only show in search for existing users, so this helps retention and Today-tab placement, not first downloads.
   - Both cost $0 and fit the New Year season.

## Questions for Megan (max 3)
1. Okay to drop `goals` from the keywords (it pulls in goal-tracker searchers)?
2. Do you want an English (UK/Australia) listing at launch, or US + Mexico only for now?
3. Is Keyword Monitor still free on your account, so I can measure the ~12 unmeasured words before late December?

## 🔴 Live scan, Oct 5 (App Store now reachable)
**Method:** iTunes Search API, US store, top 10 per term, `userRatingCount` = competition. **Limits:** the API's order is close to, but not the same as, iPhone App Store search. It shows competition only; **demand (popularity) still needs Keyword Monitor.**

| Term | #1 result (ratings) | Top-5 median | Read |
|---|---|---|---|
| manifestation journal | My Manifestation Journal (366) | 728 | ✅ still the easy #1 target (title) |
| manifest / manifestation | Stella (5,218) | 3,729 | hard, long-term |
| vision board | Vision Board & Goal Tracker (3,758) | 3,055 | hard; CPP + subtitle |
| vision board 2027 | Vision Board 2027 (2,728) | **17** | 🟢 one strong app, rest tiny → top 3 realistic in Jan |
| manifestation audio | Becoming (36) | 1,613 | 🟢 #1 is weak; Audio ships |
| affirmations audio | Presence (358) | 0 | 🟢 open |
| manifestation scripting | Kazara (10) | 93 | 🟢 open (US `scripting` + title) |
| future self manifestation | Faye (0) | 0 | 🟢 open (MX subtitle) |
| lucky girl manifestation | Lucky Girl (6) | 14 | 🟢 open (new `lucky,girl`) |
| self concept | HerSelfConcept (3) | 134 | 🟢 open (MX `concept` + "Self") |
| law of assumption | Assume (0) | 214 | 🟢 open, but popularity 5 |
| manifestation magazine | Stella; no app owns the phrase | 563 | 🟢 ownable, demand unknown |
| personal magazine / my magazine | ZINIO, Pocketmags (newsstands) | 1,450+ | ❌ wrong intent (people want to read magazines) |
| dream journal / dream life | sleep-dream apps / life-sim games | — | ❌ wrong intent → `dream,life` removed |
| future self journal | Reflectly (81,692) | 5,067 | ❌ generic journal giants |

**Next for accuracy:** popularity numbers for the 🟢 terms (Keyword Monitor). Demand × weak competition = the final v10 list.

## 📊 Demand data, Oct 5 (ASOMobile 7-day trial, US store, from Megan's screenshots)
"Traffic" = ASOMobile's estimate of **people searching this term per day in the US** (help center, Oct 5; shared between organic results and ads). E.g. manifest ≈ 535/day, manifestation journal ≈ 122/day. ASOMobile also offers Complexity (0–10) and KEI columns plus an xls export. **ASOMobile's tooltip (Oct 5):** "The current App Store score for this keyword is 5. After the latest update, many keywords were set to 5, making the score less informative. We show the previous popularity score." So in "5 | 40", 40 is the last real popularity score. **A bare "5" (or traffic 0) means "unknown", not "no demand"**, which affects visualization, guided visualization, self reflection and law of assumption. Treat those as unmeasured, not as dead. "Search Ads" = Apple's popularity score (5 is the lowest value). Where it shows "5 | 40", the right-hand number matches our September value. What the "5" means still needs ASOMobile's ⓘ tooltip (it might be the latest reading at the floor). "–" = not enough data to track.

| Term | Traffic | Search Ads | Verdict |
|---|---|---|---|
| diary | 902 | 52 | ✅ keep (US) |
| affirmations | 808 | 50 | ✅ **move to US** (combos with the title: manifestation affirmations) |
| manifest | 535 | 44 | ✅ subtitle, confirmed |
| vision board | 459 | 5 \| 40 | ✅ subtitle, confirmed |
| aesthetic | 392 | 5 \| 37 | ✅ keep |
| magazine | 286 | 5 \| 31 | ✅ keep (the searcher intent here is mixed with newsstand apps) |
| moodboard | 215 | 5 \| 27 | ✅ keep |
| manifestation journal | 122 | 5 \| 20 | ✅ title, confirmed |
| photo journal | 75 | 5 \| 15 | ✅ keep `photo` |
| law of assumption | 3 | 5 | ⚪ cheap, keep in Mexico only |
| guided visualization, visualization, self concept, self reflection | 0 | 5 / – | ❌ cut `visualization, guided, concept, reflection` |
| vision board 2027, new year vision board, manifestation audio, affirmations audio, manifestation scripting, manifestation magazine, future self manifestation, lucky girl manifestation, intention journal | – | – | ❌ no measurable demand **now**. The weak competitors were real, but almost nobody searches these. Exception to check: **vision board 2027** is seasonal (check last year's "vision board 2026" for Dec–Jan). |

**Lesson:** weak competitors only matter where there's demand. Most of the Oct 5 "opportunities" have no demand. The real wins are the big single words combined with our title and subtitle.

### v10 DRAFT (counts by script, title/subtitle unchanged)
```
[TRACKING DATA-FIELD: US · Keywords (93/100)]    diary,affirmations,aesthetic,magazine,moodboard,photo,audio,scripting,intention,visualization
[TRACKING DATA-FIELD: es-MX · Keywords (40/100)] loa,assumption,inspiration,2027,new,year
```
- Removed: `lucky, girl, reflection, life, guided, ritual, concept` (0 or no data).
- **`visualization` back in (US), per Megan:** Apple scores it 5, the lowest value Apple reports. That means low search volume, not zero. The live check shows the right searchers (guided visualization and manifestation apps; the #1 app has only 894 ratings), it describes the Audio feature, and it combines with the title ("manifestation visualization"). For 14 characters it's worth keeping. Re-check in Round 2.
- `scripting`, `intention`, `audio`, `inspiration`, `2027,new,year` are still unmeasured → measure in batch 3 before locking.
- 67 characters are free across the two fields. Fill them **only with measured words** from batch 3.

## 📥 Batch from Megan's ASOMobile export (Keyword Monitor, Stella selected, US, Oct 4) + live intent check
| Term | Traffic/day | Search Ads | Who ranks (live) | Verdict |
|---|---|---|---|---|
| motivation | 2,779 | 62 | quote apps (Motivation 1.07M ratings) | ❌ wrong intent (quotes not in V1), giants |
| glow up | 654 | 47 | looksmaxxing/beauty apps | ❌ appearance intent |
| journaling | 318 | 33 | Journal (327K), Day One (118K) | ⚪ right intent, giants. Not now |
| self love | 162 | 23 | affirmation/self-care apps (#1 2,025) | ✅ add `love` (combos with "Self" in the Mexico subtitle, same listing) |
| that girl | 162 | 23 | routine/habit planners | ❌ habit-tracker intent (architecture) |
| mindset | 152 | 22 | motivation/affirmation apps | ✅ add (medium competition) |
| audio | 108 | 53 | — | ✅ keep |
| inspiration | 102 | 18 | — | ✅ keep |
| scripting | 101 | 18 | — | ✅ keep (now measured) |
| affirmation | 92 | 28 | — | ⚪ skip, `affirmations` covers it |
| intention | – | 5 | — | ❌ drop (no data) |
| stella, stela, vix… | — | — | competitor brands | ❌ never (Apple keyword rules) |

### v11 DRAFT (counts by script; no repeats within or across listings; no name/subtitle/category words)
```
[TRACKING DATA-FIELD: US · Keywords (83/100)]    diary,affirmations,aesthetic,magazine,moodboard,photo,audio,scripting,visualization
[TRACKING DATA-FIELD: es-MX · Keywords (53/100)] loa,assumption,inspiration,love,mindset,2027,new,year
```
64 characters free. Fill them only with measured words (still to measure: scrapbook, collage, dream board, daily affirmations, positive affirmations, journal app, vision board app, abundance, manifest money, becoming, zine). Swap `2027,new,year` after January (needs an app update).

## 🌟 Final batch (ASOMobile export 2, Oct 4) + live intent check: the real opportunity
| Term | Traffic/day | Search Ads | Top apps live (ratings) | Verdict |
|---|---|---|---|---|
| **scrapbook** | **392** | 37 | Planly 70 · klora 39 · Nooka 9 | 🟢 **demand + weak competition.** Fits Your World + Publish |
| **digital scrapbook** | **230** | 28 | Planly 70 · Tomobook 49 · Nooka 9 | 🟢 same |
| mood board | 311 | 32 | Moodboard 1,748 · Morpholio 3,755 | ✅ add `mood` (combos with "Board" in the US subtitle) |
| collage | 3,493 | 63 | PicCollage 1.8M · LiveCollage 178K | ❌ photo-editor giants |
| daily / positive affirmations | 373 / 288 | 36 / 31 | I am 734K · Mantra 34K | ❌ I am owns it (`affirmations` alone stays) |
| gratitude journal | 436 | 39 | Gratitude 45K | ❓ only if Scribe really offers gratitude writing |
| journal prompts | 162 | 23 | solo. 6 · Ink 11 · Prompted 6.9K | ❓ only if Scribe really has prompts |
| dream board 75 · confidence 62 · journal app 22 · zine 13 | low | | | ⚪ not worth the space |
| abundance, manifest money, manifestation app, affirmation app, affirmations for women, future self, new me | 0–3 | 5 | | ⚪ unknown (Apple floor) / no demand |
| vision board app/2026, inspiration board, personal magazine, becoming, dear future self, aesthetic vision board | – | – | | ⚪ no data |

### v12 DRAFT (counts by script; no repeats within or across listings)
```
[TRACKING DATA-FIELD: US · Keywords (92/100)]    diary,affirmations,aesthetic,magazine,moodboard,mood,photo,audio,scripting,scrapbook,digital
[TRACKING DATA-FIELD: es-MX · Keywords (67/100)] loa,assumption,inspiration,love,mindset,visualization,2027,new,year
```
- `scrapbook` + `digital` sit in the US field so "digital scrapbook" combines within one listing (no reliance on the cross-listing belief).
- `visualization` moved to Mexico to make room. It combines with "Manifesting" there.
- 41 characters free: reserved for `gratitude` / `prompts` if Megan confirms those features.
- Idea for later (needs Megan): the Mexico subtitle's "Future Self" has ~3/day. A subtitle with **scrapbook** would carry more weight than the keyword field. Test in Round 2.

## ✅ Megan's answers (Oct 5) → v13
- Scribe **has writing prompts**: yes. Gratitude writing: yes, "an easy feature" (**must actually ship in the Jan 11 build** before the word goes live).
- Audio/video will include **angel numbers** and **subliminals**. This changes the earlier brief ("no subliminals in V1"). PRODUCT/Design docs should be updated to match.

| Term | Popularity (Round 1, Sep) | Top apps live, Oct 5 (ratings) | Verdict |
|---|---|---|---|
| angel numbers | 16 | Angel Numbers Numerology 1,478 · Angel Number Signs 838 · rest 0–2 | 🟢 weak competition |
| subliminal(s) | 20 | VibeSesh 1,613 · Sound & Soulful 1,748 · Subliminal Manifestation 444 · Hopium 29 | 🟢 medium-weak |
| journal prompts | 23 (ASOMobile, 162/day) | solo. 6 · Ink 11 | 🟢 |
| gratitude journal | 39 (436/day) | Gratitude 45K | ⚪ hard to top, but a real feature now |

### v13 DRAFT (counts by script; no repeats within or across listings, or with name/subtitle/category)
```
[TRACKING DATA-FIELD: US · Keywords (100/100)]   diary,affirmations,aesthetic,magazine,moodboard,mood,photo,audio,scripting,scrapbook,digital,prompts
[TRACKING DATA-FIELD: es-MX · Keywords (91/100)] loa,inspiration,love,mindset,visualization,gratitude,subliminal,angel,numbers,2027,new,year
```
- `prompts` in US combines with "Journal" in the US title (same listing).
- `assumption` dropped (≈3 searches/day) to make room.
- **Trust rules:** only list these if the content is in the Jan 11 build (Apple 2.3.7: keywords must be accurate). Subliminal/angel-number copy must not promise results or health effects (1.4.1). Present them as experiences, not guarantees.

## 🏁 Conclusions: where ISSUE11 can rank (Oct 5, from ASOMobile demand + live competition)
No guarantees. Ranking = text relevance (title > subtitle > keywords) × user behavior (downloads, ratings, conversion). Estimates assume a decent launch week.

| Tier | Keywords | Why |
|---|---|---|
| **A · top 3 realistic in launch month** | manifestation journal (title, 122/day) · scrapbook (392) · digital scrapbook (230) · journal prompts (162) · angel numbers · manifestation scripting · manifestation visualization | demand exists, the current top apps have 6 to 1,500 ratings |
| **B · top 10 within 1–3 months, with ratings** | vision board (459) · manifestation (174) · law of attraction · mood board (311) · subliminal · self love (162) · mindset (152) · manifesting (111) | real demand, top apps have 300 to 5K ratings |
| **C · long game (6–12 months)** | manifest (535, Stella 5.2K) · affirmations (808, I am 734K) · diary (902, Day One/Journal) · gratitude journal (436, 45K) · aesthetic · magazine | giants; we're present for combos, and ranking comes later |

**Recommendation (needs Megan's OK):** put **scrapbook** in a subtitle, the strongest Tier A term. The Mexico subtitle "Manifesting Your Future Self" carries "future self" at ~3/day. Option: `Manifesting Digital Scrapbook` (29/30). That frees 18 US keyword characters, but it breaks the "self love" combo (re-add `self` or drop `love`). Decide before submission.

## ✅ v14: CURRENT DRAFT (Megan approved the scrapbook subtitle swap, Oct 5)
```
[TRACKING DATA-FIELD: US · App Name (30/30)]        ISSUE11: Manifestation Journal
[TRACKING DATA-FIELD: US · Subtitle (28/30)]        Manifest with a Vision Board
[TRACKING DATA-FIELD: US · Keywords (93/100)]       diary,affirmations,aesthetic,magazine,moodboard,mood,photo,audio,scripting,prompts,journaling
[TRACKING DATA-FIELD: es-MX · App Name (26/30)]     ISSUE11: Law of Attraction
[TRACKING DATA-FIELD: es-MX · Subtitle (29/30)]     Manifesting Digital Scrapbook
[TRACKING DATA-FIELD: es-MX · Keywords (96/100)]    loa,inspiration,self,love,mindset,visualization,gratitude,subliminal,angel,numbers,2027,new,year
[TRACKING DATA-FIELD: Category]                     Primary: Health & Fitness · Secondary: Lifestyle
```
Script-checked: all within limits; no spaces; no repeats within a field, across the two fields, or with any name/subtitle/category word; no competitor names.
- Mexico subtitle: "Your Future Self" (~3 searches/day) → **Digital Scrapbook** (392 + 230/day, top apps 9–70 ratings).
- `scrapbook,digital` left the US keywords (now in the subtitle). `self` was added to the Mexico keywords so "self love" still works. `journaling` (318/day) was added to the US keywords.
- Still to do: swap `2027,new,year` in a February update. All features named here must be in the Jan 11 build (2.3.7).
- Screenshot caption idea for scrapbook: "Your vision board, made into a scrapbook magazine". Real UI only.

## 📈 ASO growth plan (Oct 5): App Store levers only
Ranking = relevance (metadata) × behavior (downloads, conversion, ratings, retention). Metadata is done (v14). Growth now comes from:
1. **Keyword iteration every app update (every 2–4 weeks).** Keywords and subtitles only change with a new version (Apple). Each release: keep ranks 1–3, add weight to 4–20 that are climbing, swap anything stuck past 20 or with ~0 traffic. Track ranks weekly.
2. **Custom product pages per keyword cluster** (Apple: up to 70, each can be assigned keywords and appear in search; verified Oct 4): Scrapbook · Vision board · Audio (subliminal, angel numbers, visualization) · Affirmations · Journal prompts. Each gets screenshots that match the search, which lifts conversion.
3. **Conversion tests:** Apple's product page optimization on icon + first 3 screenshots (cover reveal first). Higher tap-through → more downloads → higher rank.
4. **Ratings:** the built-in prompt right after the first cover reveal. Reply to every review in the first months.
5. **In-App Events on "the 11th":** a monthly event on the 11th (11:11 / angel numbers ties to the name), plus the New Year Issue in January. Event cards show on the product page and in browse. In search they show only for existing users (Apple), so they help retention more than first downloads.
6. **Launch-week velocity:** waitlist downloads concentrated around Jan 11 + featuring nomination (drafted, Nov 12–30).
7. **Later:** English (UK/AU/CA) localizations for more keyword space (indexing unverified), then other languages.

## 🎯 "5 big + 20 small" check (framework Megan heard on YouTube, Oct 5)
**5 big (Apple popularity > 20), all already in the strongest fields (title/subtitles):**
manifest 44 (US subtitle) · vision board 40 (US subtitle) · scrapbook 37 (MX subtitle) · digital scrapbook 28 (MX subtitle) · manifestation 24 (US title)

**20 small (winnable long-tails covered by v14):**
manifestation journal · manifest journal · journal prompts · manifestation prompts · scripting journal · manifestation scripting · photo journal · gratitude journal · angel numbers · subliminal · manifestation subliminal · manifestation visualization · manifestation affirmations · manifestation audio · law of attraction · law of attraction journal · self love · mindset · mood board · vision board 2027 (seasonal)
Combos across the US and Mexico listings (e.g. gratitude + Journal) rely on the cross-listing belief (unverified).

## 🔮 Projection: organic App Store **search** downloads, ~3 months after launch (model, not a promise)
**Inputs:** ASOMobile daily traffic (US, Oct 4–5) for 16 terms. Angel numbers (~85/day) and subliminal (~120/day) are estimated from their September popularity scores. **Assumption (industry rule of thumb, not measured):** share of a term's daily searchers who install, by rank: #1 30% · #2 15% · #3 10% · #4–5 6% · #6–10 3% · #11–20 1% · 21+ 0.2%.

| Scenario | Ranks assumed (examples) | Downloads/day | Downloads/month |
|---|---|---|---|
| Conservative | manifestation journal #3, digital scrapbook #5, scrapbook #8, journal prompts #5, vision board #40, manifest #50 | ~57 | ~1,700 |
| Realistic | manifestation journal #1, digital scrapbook #2, scrapbook #3, journal prompts #2, angel numbers #3, vision board #15, manifest #25 | ~176 | ~5,300 |
| Optimistic | manifestation journal, scrapbook, digital scrapbook, journal prompts, angel numbers all #1; manifestation #3, vision board #5, manifest #8 | ~432 | ~13,000 |

Not included: TikTok/Instagram/Pinterest, featuring, word of mouth, the January seasonal spike, other countries. Biggest driver in every scenario: **scrapbook + digital scrapbook + manifestation journal + journal prompts.** Re-run with real Search Analytics data from App Store Connect after launch.

## 💳 Conversion estimate (Oct 5): downloads → paying subscribers
**Benchmarks** (RevenueCat State of Subscription Apps 2026, read via search summaries; revenuecat.com is blocked here): download → paid within 35 days: median app 2.0%, **Health & Fitness 2.9%**. Trial → paid: average 25.6%, Health & Fitness 35%. Trial start ≈ 5–7% of installs (top apps 12–15%+).

| Scenario | Search downloads/month | Download → paid | New paying subs/month | Bookings/month at $99.99/yr after Apple's 15%* |
|---|---|---|---|---|
| Conservative | ~1,700 | 1.5% (new app, below median) | ~26 | ~$2,200 |
| Realistic | ~5,300 | 2.9% (category median) | ~154 | ~$13,100 |
| Optimistic | ~13,000 | 5% (strong onboarding + cover reveal before paywall) | ~650 | ~$55,200 |
*Assumes everyone picks the annual plan at $99.99 (pricing not decided) and the App Store Small Business Program rate (15%). Monthly plans lower these numbers. Search downloads only.
**Year 1 (if the month-3 pace held for 12 months; real months 1–2 will be lower):** Conservative ~312 subs ≈ $26.5K · Realistic ~1,848 subs ≈ $157K · Optimistic ~7,800 subs ≈ $663K (net after Apple's 15%, all on the $99.99 yearly plan, search downloads only). Year 2 adds renewals from these subscribers.
