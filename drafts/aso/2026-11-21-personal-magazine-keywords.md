# Should "personal magazine" / "magazine maker" go into listing v15? (US App Store)
Nov 21, 2026 · 💚 GROWTH (ASO & Opportunity Scout) · skills: aso, aso-specialist, graphify (graphs/marketing has no ASO node, so I read drafts/aso directly).
Draft only. App Store Connect not touched. v15 (approved Nov 19) stays the baseline; this is a proposed change for Megan.

**Short answer:** yes, as a small keyword-field change only. App Store search demand for "personal magazine" is still at the tools' floor (the TikTok spike hasn't reached App Store search yet), so it doesn't earn a place in the name or subtitle. Adding two cheap words (`personal`, `maker`) to the hidden keyword field costs one weak word (`scripting`) and positions us before the trend arrives.

## The data (US, iPhone, Nov 21)
Applyra `inspect_keyword` (traffic / difficulty, 0–100; **8 = Applyra's floor, meaning almost no measurable demand**). ASOMobile: only **1 API token left** (plan "FREE to MAX"), so no new ASOMobile checks were run; the column shows Megan's Nov 18 Sheet where it exists.

| Keyword | Applyra T / D / KEI | ASOMobile (Nov 18) | Who ranks top 3 now | Read |
|---|---|---|---|---|
| **magazine maker** | **37 / 32 / 1.16 excellent** | Search Ads 23 | Magazine Cover Maker & PIP Cam · Cover Me (fake cover) · Canva | The only candidate with real traffic. Intent = cover/collage makers. |
| personal magazine | 8 / 22 / 0.36 low | popularity n/a · C 6.9 · Search Ads 5 | ZINIO · Personal Care Magazine · Cosmopolitan | Same as Nov 18. Nobody owns it; newsstand apps only. |
| personalized magazine | 8 / 18 / 0.44 | not measured | Cosmopolitan · ZINIO · Personal Care Magazine | Floor. Newsstand apps. |
| custom magazine | 8 / 19 / 0.42 | not measured | Custom Car Magazine · Build Home Magazine · Mosaic | Floor. Wrong intent (car/home titles). |
| magazine creator | 8 / 14 / 0.57 | not measured | Magazine Cover Maker · Magazine Maker (1.3★) · MagLoft | Floor. Covered free by `magazine` + `maker`. |
| digital magazine maker | 8 / 16 / 0.50 | not measured | Magazine Maker (1.3★) · MagLoft · Magazine Cover Maker | Floor. Would need `digital` (es-MX only). |
| scrapbook magazine | 8 / 16 / 0.50 | not measured | Creative Scrapbooker Magazine · Scrapbooking Memories · Scrapbook | Floor. **Already covered by v15** (`scrapbook` + `magazine`). |
| make a magazine | 8 / 26 / 0.31 | not measured | Make: Magazine (2.0★) · Money Hacks · Craft & Home | Floor. Make: is a DIY title, not intent. |

Off-store demand (design/ICP-DETAILED.md, Megan's Nov 21 screenshots): TikTok "pinterest magazines" 277K (+1000% in 7 days), "personalized magazine gift(s)" 80.9K–108K, "how to make a personalized magazine" 35.7K; Google Trends "personal magazine" +160% year on year but low right now. **Read:** real interest, but it lives on TikTok, not App Store search yet. Store demand usually lags social; the hidden keyword field is the cheap place to wait for it.

## Weakest words in v15 today
Keyword field (91/100): `magazine,moodboard,mood,scrapbook,prompts,journaling,dream,manifesting,zine,scripting,daily`
| Word | Why it's weak | Keep? |
|---|---|---|
| **scripting** | 141/day on ASOMobile but top apps are coding tools; its two useful combos (manifestation scripting, scripting journal) are both at Applyra's floor 8 | **Out** |
| zine | 116 · C 4.2; Applyra inflated by "Zain" telecom apps | Keep: with `maker` it unlocks "zine maker" (Zinely, Artino rank for magazine terms), and it fits the magazine |
| daily | Only a connector, but it unlocks "daily journal prompts" (213/day, C 1.5) | Keep |
Name and subtitle: untouched. "manifestation journal" (246/day, D 40) and "manifest"/"vision board" are far stronger than any magazine term. The data is not close to overwhelming.

## ✅ Recommended swap (keyword field only)
Out: `scripting` (−10 incl. comma). In: `maker` (+6), `personal` (+9).
```
[TRACKING DATA-FIELD: US · App Name (30/30)]   ISSUE11: Manifestation Journal      (unchanged)
[TRACKING DATA-FIELD: US · Subtitle (28/30)]   Manifest with a Vision Board        (unchanged)
[TRACKING DATA-FIELD: US · Keywords (96/100)]  magazine,moodboard,mood,scrapbook,prompts,journaling,dream,manifesting,zine,daily,maker,personal
```
Checked by script: 96 bytes, no spaces, no repeated words, no word repeated from name or subtitle.

What the two new words unlock (Apple combines words across name + subtitle + keyword field):
- `maker` → **magazine maker** (37 / 32, KEI 1.16, the best number here), **vision board maker** (25 / 54; ASOMobile "vision board maker free" 413/day; parked in v15 for lack of `maker`), magazine creator-style searches, zine maker, scrapbook maker, journal maker.
- `personal` → **personal magazine** (8 / 22, empty of real rivals: if the TikTok trend reaches the store, we're already indexed), personal journal.
- Lost with `scripting`: manifestation scripting and scripting journal (both 8 = floor). "manifestation scripting" searches still partly match via the name.

Net: we give up two floor-level phrases and gain one real-traffic term (magazine maker 37), one parked term with ASOMobile demand (vision board maker), and an early position on personal magazine.

**Honest risk on `maker`:** most "magazine maker" searchers want a one-off fake cover (Cover Me, Canva). Some will bounce, which may dent conversion for that query. It's a hidden-field word with no visible claim and no trademark, so the Oct 2 concern (fake-cover wording, 5.2) doesn't apply to the field itself, but it is a change to that decision and needs Megan's OK. **If she says no to `maker`:** drop only `scripting`, add `personal` → `...zine,daily,personal` (90/100).

## Description opening lines (conversion only: Apple doesn't index the description)
Option A (161 chars):
> ISSUE11 is a personal magazine maker for your vision board. Your saves, journal lines and weekly actions become your own 40-page magazine, with you on the cover.

Option B (uses the approved one-liner):
> A personal magazine maker for the life you want. It's like Pinterest meets a habit tracker, except your progress becomes a personalized magazine you can print. *(Printed Issue sold separately.)*

The description is currently exactly as Megan published it, so either line would replace or sit above her first line only with her OK. Recommended: **A** (says what it is in the first 2 lines, which is what shows before "more").

## Uncertain
- ASOMobile numbers for the 6 new phrases are missing (1 token left). Applyra alone puts 7 of 8 at the floor; a second tool would only matter for `magazine maker`, which ASOMobile already rated Search Ads 23 on Nov 18.
- Whether TikTok demand reaches App Store search, and when, is unknown. Recheck `personal magazine` and `personalized magazine` on **Mon Dec 1** with the seasonal check, before the Dec 4 submission.
- Apple's cross-field matching of multi-word searches is standard ASO understanding, not something Apple documents.

## For Megan (2 questions)
1. Swap `scripting` → `maker` + `personal` in the keyword field? Recommended: yes.
2. Description: add Option A as the first line? Recommended: yes.
