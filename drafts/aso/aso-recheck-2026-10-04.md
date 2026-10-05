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
[TRACKING DATA-FIELD: US · Keywords (94/100)]      scripting,magazine,photo,diary,intention,reflection,lucky,dream,life,audio,aesthetic,moodboard
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
