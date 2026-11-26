# ISSUE11 US keyword optimization: most traffic, least competition (v15 → v15.1 draft)
Nov 22, 2026 · 💚 GROWTH (ASO & Opportunity Scout) · skills loaded with the Skill tool: **aso**, **aso-specialist**, **graphify** (graphs/marketing has no ASO keyword node, so I read drafts/aso directly).
Megan, word for word: "Check with ASO agent and optimize for the most traffic with the least competition" · "We can also put in the description that you can make a personal magazine".
Draft only. App Store Connect not touched. v15 (approved Nov 19) stays live in the plan until Megan OKs this.

**Data:** Applyra `inspect_keyword` (US, iPhone, en-US). Traffic and difficulty are 0–100 tool estimates, not Apple numbers. **8 = Applyra's floor**, meaning almost no measurable demand. Today: **15 new inspections** + 76 reused from Nov 18/21 (`list_keyword_inspections`, free). ASOMobile column = Megan's Nov 18 Sheet (drafts/aso/exports/2026-11-18/). **0 ASOMobile tokens spent** (1 left, saved).
**Method (aso skill, Challenger tier, so strict textbook ASO):** score = traffic ÷ difficulty, then three filters: (1) the app really does it (Apple 2.3.7), (2) the top 3 apps have the same intent as our user, (3) a new app with 0 ratings can reach the top 10 (difficulty under ~55, or a combo of a head term).

## 1. Final keywords (US)
| # | Keyword | Applyra T / D | T÷D | ASOMobile (Nov 18) | Field | Why |
|---|---|---|---|---|---|---|
| 1 | **zine maker** 🆕 | 48 / 13 | **3.69** | not measured | K `zine`+`maker` | Best ratio we have that fits the product. Top apps are real photo-zine makers (EZZINE, Artino, Zinely), the same thing ISSUE11 does with your saves. |
| 2 | **mood board maker** 🆕 | 45 / 38 | 1.18 | mood board 781 · C 3.0 | K `mood`+`maker` + S `Board` | Real traffic, mid difficulty. My saves is a mood board. |
| 3 | **magazine maker** 🆕 | 37 / 32 | 1.16 | Search Ads 23 | K `magazine`+`maker` | Hidden field only (Oct 2 rule bans visible wording). Fake-cover intent in the top 3, so expect weaker conversion here. |
| 4 | manifestation journal | 43 / 40 | 1.07 | 246 · C 2.2 | N (exact) | Best core term in both tools. Unchanged. |
| 5 | moodboard | 59 / 54 | 1.09 | 393 · C 1.1 | K | Strongest agreement between the tools. Unchanged. |
| 6 | manifest | 74 / 70 | 1.06 | 1066 · C 3.9 | S | Biggest relevant head term. A long game, kept in the subtitle. |
| 7 | journal prompts | 45 / 47 | 0.96 | 288 · C 1.6 | N + K | The daily prompt ships. |
| 8 | mood board | 41 / 45 | 0.91 | 781 · C 3.0 | K + S | |
| 9 | manifesting | 25 / 30 | 0.83 | 162 · C 3.0 | K | |
| 10 | scrapbook | 52 / 64 | 0.81 | 780 · C 3.6 | K | Big volume. The 40 pages are a scrapbook you can hold. |
| 11 | vision board | 52 / 67 | 0.78 | 923 · C 4.0 | S | Head term, kept for combos. |
| 12 | dream board | 25 / 35 | 0.71 | 155 · C 1.3 | K + S | |
| 13 | daily journal prompts | 25 / 53 | 0.47 | 213 · C 1.5 | K + N | ASOMobile rates it easy. |
| 14 | vision board maker 🆕 | 25 / 54 | 0.46 | "…free" 413 · C 3.4 | S + K `maker` | Was parked in v15 for lack of `maker`. |
| 15 | personal journal 🆕 | 27 / 64 | 0.42 | not measured | K `personal` + N | Moderate; mostly a side effect of `personal`. |
| 16 | personal magazine 🆕 | 8 / 22 | 0.36 | C 6.9 · Search Ads 5 | K `personal`+`magazine` | Floor today. We're indexed early, before the TikTok trend reaches store search, and it matches the new description line. |
| — | journaling · magazine · zine | 61/70 · 77/74 · 84/58 | — | 624 · 567 · 116 | K | Kept as connector words for combos (zine's traffic is inflated by "Zain" telecom apps). |

## 2. Exact fields
```
[TRACKING DATA-FIELD: US · App Name (30/30)]   ISSUE11: Manifestation Journal      (unchanged)
[TRACKING DATA-FIELD: US · Subtitle (28/30)]   Manifest with a Vision Board        (unchanged)
[TRACKING DATA-FIELD: US · Keywords (96/100)]  magazine,moodboard,mood,scrapbook,prompts,journaling,dream,manifesting,zine,daily,maker,personal
```
**Verified twice:** a local script (96 bytes, no spaces, no repeated words, no word from the name or subtitle) and Applyra `check_metadata`: valid, 96/100, 0 duplicates, 0 phrases, 0 wasted characters.
v15 vs v15.1 keyword field: **out `scripting`** (−10 incl. comma) · **in `maker`, `personal`** (+15). Same swap as the Nov 21 draft. Today's data makes the case stronger: `maker` now unlocks 4 measured terms (zine maker 48/13, mood board maker 45/38, magazine maker 37/32, vision board maker 25/54), not 1.

## 3. Subtitle: keep it
| | Current (approved) | Strongest alternative tested |
|---|---|---|
| Subtitle | Manifest with a Vision Board (28) | Vision Board & Mood Board Maker (31, over the limit) → "Mood Board & Vision Board" (25) |
| Gains | manifest 74/70 (ASOMobile 1066, our biggest relevant term) + vision board | mood board moves into a stronger field |
| Loses | n/a | `manifest` leaves every field. "Manifestation" in the name is a different word, and Apple's stemming is undocumented. |
**Verdict:** no change. Mood board is already covered by `mood` + "Board", so the alternative only shifts weight and loses our top head term. The data is not close to overwhelming, and the name stays too.

## 4. Dropped or not added, and why
| Keyword | Applyra T / D | Why it's out |
|---|---|---|
| scripting | 25 / 31 | Top apps are coding tools. Its useful combos (manifestation scripting, scripting journal) sit at the floor (8). |
| habit tracker 🆕 | 72 / 91 | Giants (HabitKit, Streaks, Finch). It also pulls toward a productivity app, which the locked architecture forbids. The approved one-liner stays for copy, not keywords. |
| habit journal 🆕 | 25 / 69 | Low KEI, habit-tracker apps. |
| collage maker 🆕 | 63 / 96 | Near-impossible (PicCollage, Canva). |
| photo book 🆕 | 25 / 81 | Print giants (Shutterfly, Mixbook, Chatbooks). |
| self care / self care journal 🆕 | 56 / 83 · 25 / 60 | Hard, and the intent is mental-health or pet apps. |
| vision board free 🆕 | 23 / 23 (KEI 1.0) | Good numbers, but ISSUE11 is a paid subscription behind a trial. "free" searchers who hit a paywall leave bad reviews (trust rule). **Parked for Megan.** |
| affirmation journal 🆕 · affirmations | 11 / 44 · 25 / 88 | Low traffic, or owned by I am (Megan, Nov 18: "affirmations is too hard to rank"). |
| scrapbook maker 🆕 · journal for women 🆕 · manifestation planner 🆕 · aesthetic vision board 🆕 | 11/46 · 12/47 · 8/22 · 8/22 | Low traffic. |
| magazine cover | 48 / 15 | Still out: fake-cover intent, 5.2 risk, Oct 2 decision. |
| lifemaxxing · law of assumption · mirror work | 25/5 · 25/22 · 44/33 | ASOMobile shows ~0 traffic (tools disagree). Mirror work isn't a feature. |
| angel numbers · subliminal | 54/31 · 58/54 | Only if that content ships (2.3.7). It isn't in the launch feature list. |

## 5. Description: "make your own personal magazine" (Megan, Nov 22)
Apple doesn't index the description, so this is for conversion. Only the first ~3 lines show before "more" (aso skill).
⚠️ **Megan's published description isn't in the repo** (checklist: "Megan's copy, not in the repo"). So "old" below is the v15 promo text and caption, plus the opening of the Nov 12 draft, the closest copy we have. Megan should paste her live first lines over the "old" column before swapping.

**New opening (first 3 lines):**
```
Make your own personal magazine from the life you want.                                  (55)
Save images to your vision board, write a few lines in your journal, and they become your 40-page Issue, with you on the cover.   (127)
Then pick one small action a day, week or month, at your own pace. There are no streaks to break.   (97)
```
| Spot | Old | New |
|---|---|---|
| Description, lines 1–3 | "If your camera roll is half screenshots of a life you want, hi. / ISSUE11 gathers all of it into your Issue: a personal 40-page magazine…" (Nov 12 draft; live text may differ) | The 3 lines above. "make your own personal magazine" is in line 1. |
| Description, YOUR ISSUE section (add 1 line at its end) | (none) | "It's your personal magazine: download it, or order it printed (sold separately)." (80) |
| Promotional text (170) | "Turn your vision board, saved photos and journal lines into your own 40-page magazine, with you on the cover. Then take one small step a week toward the life you want." (167) | "Make your own personal magazine from your vision board, saved photos and journal lines: 40 pages, with you on the cover. Then one small action a week, your pace." (161) |
| Screenshot caption 3 (v15) ⚠️ | "Your manifestation journal, one small **move** a week." | "Your manifestation journal, one small **action** a week." (52) **This fixes a banned word already in approved v15.** |
Everything else in v15 stays as approved (name, subtitle, captions 1, 2, 4, 5, 6, es-MX).
Copy check (script): no "becoming her", no "move", no visible "magazine maker", no promised outcome, print sold separately, no prices. "Pinterest meets a habit tracker" is left out of the store copy on purpose: Pinterest is a brand and we have no integration (Oct 23 decision).

## 6. Expected ranking timeline (estimate, not a promise)
Apple usually indexes new metadata within 1–3 days of the Dec 11 release. Rough ranks for a new app with 0 ratings, assuming a normal launch week (waitlist downloads, first ratings):
| When | Terms | Likely rank |
|---|---|---|
| Week 1–2 (Dec 11–25) | floor niches: personal magazine, manifestation magazine, vision board magazine, manifesting journal | top 1–5 (little volume) |
| Weeks 2–6 (late Dec–Jan) | zine maker, manifestation journal, manifesting, dream board, magazine maker | top 10, if launch-week downloads come in |
| Months 2–3 | mood board maker, journal prompts, moodboard, daily journal prompts, vision board maker | top 10–20 → top 10 with ratings |
| Months 3–6+ | manifest, vision board, scrapbook, journaling, magazine | top 20–50; top 10 needs ratings volume |
New Year matters: vision board searches peak Dec 26–Jan 15. Recheck `vision board 2027` and `personal magazine` on **Mon Dec 1** (already scheduled) before the Dec 4 submission.

## 7. Uncertain
- **zine maker** and **mood board maker** are Applyra-only numbers (ASOMobile has 1 token left, unspent). Applyra has inflated short `zine` terms before. If Megan wants a second tool's view, spend the last ASOMobile token on `zine maker`.
- `maker` changes the Oct 2 decision in spirit (the field is hidden, nothing visible says "magazine maker"), so it needs Megan's explicit OK. If she says no: drop only `scripting`, add `personal` → 90/100.
- Apple's cross-field matching of multi-word searches is standard ASO understanding, not something Apple documents.

## For Megan (2 questions, recommended answer first)
1. Keyword field: swap `scripting` → `maker` + `personal`? **Yes.** It adds 4 measured "maker" terms with real traffic and low or mid difficulty, and loses only floor terms.
2. Description: use the new 3-line opening + the YOUR ISSUE line + the promo text + the caption 3 fix? **Yes.** It says "make your own personal magazine" up top, and caption 3 currently breaks the "action" rule.


## Update Nov 26 (Megan said yes)
Add `free` to the keyword field at the Dec 1 recheck (swap out the weakest word, stay ≤100). Target: vision board free (23/23). Visible copy: "7 days free, then $39.99 for your first year" only. Watch reviews 2 weeks; drop it if "not free" complaints appear. Also recheck `personal magazine` + `personalized magazine`.
