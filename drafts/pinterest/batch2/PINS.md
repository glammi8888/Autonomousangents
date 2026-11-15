# Pin batch 2 (Nov 15, 2026): vision boards + text pins, for Megan's review
Drafts only. Nothing is scheduled. Canvas: https://claude.ai/artifact/MZr3GzSS5YdENf5x4D3DrT (rows at y 8380 and 10000, note "Pinterest batch 2 · vision boards + text pins").
All pins link to **https://issue11.app/rebrand-kit** (free 2027 Life Glow Up Kit: "My 2027" list page, 6 chapters, 30 ChatGPT prompts, 30-day challenge, future self letter). Truth rule: the vision board pins promise the **list page**, not a printable vision board (that kit isn't built yet).
Source: `generator-b2.py <scratch dir>` writes `project/Pin19..28.dc.html` (copy them next to this file). The Notes template is copied from batch1/generator.py `notes()`, incl. the white "Get it free at issue11.app →" bar. PNGs + phone contact sheets: `png/` (`sheet-390.png`, `sheet-236.png`). Local render: `node render.js <dir with Pin*.dc.html> png`.

## Keyword data (real numbers only)
Pinterest autocomplete (Apify `lergassy~pinterest-search-scraper`, searchType keywords, Nov 15; raw: `../2026-11-15-visionboard-keywords.json`):
- "2027 vision board ideas" → #1 "2027 vision board ideas aesthetic", #2 "…travel", #3 "vision board ideas wallpaper 2027"; refinement "vision board 2027 ideas collage"
- "vision board 2027" → #1 "vision board 2027 ideas", #2 "…aesthetic", #3 "…ideas collage", #4 "…wallpaper", #5 "…photos"
- "vision board aesthetic" → #1 "vision board aesthetic pictures", #2 "…ideas", #3 "…wallpaper"; refinements "money vision board aesthetic", "self care vision board aesthetic"
- "2027 manifestation board" → #1 "manifestation board ideas 2027", "2027 vision board manifestation", "vision board manifestation dream life 2027"
- "journal prompts 2027" → #1 "journal prompts for 2027", #2 "2027 journal prompts"

Google US monthly (Mangools, Nov 14, DEMAND-CHECK): vision board ideas 43,400 · journal prompts 38,200 · manifestation journal 3,100 · lifemaxxing 1,200 · 2027 vision board 50 (12-month avg, spikes Dec–Jan).
**Missing:** Google volume for "vision board aesthetic", "manifestation board", "things to manifest" (not pulled this run). Pinterest volumes aren't public (see lessons, Nov 15).

## SEO rows
| # | Format | Title (keyword first) | Description | Board | Alt text | AI flag |
|---|---|---|---|---|---|---|
| 19 | Collage 3×3 | 2027 vision board ideas: closet, money, love, style | 2027 vision board ideas for a whole-life glow up: dream closet, money, date nights, city nights, your own desk. Pin the pics, then write your 2027 list on the free page in the 2027 Life Glow Up Kit. | 2027 Visionboard Ideas | Nine colour photos in a black grid labelled dream closet, money, date nights, city nights, my own desk, shopping day, love, savings and the walk-in, under the words 2027 vision board ideas | yes (AI people) |
| 20 | Collage 2×3, black | Vision board 2027 ideas: it's on my vision board | Vision board 2027 ideas collage: a glass closet, city nights, love, money, a calm desk. It's on my vision board, now it's on my list. Write your 2027 list free with the 2027 Life Glow Up Kit. | 2027 Visionboard Ideas | Six colour editorial photos on black under the words vision board 2027 | yes (AI people) |
| 21 | Magazine grid | Vision board aesthetic pictures for 2027 (moodboard) | Vision board aesthetic for 2027: big closets, cash, city nights, slow love. Save the moodboard, then write your 2027 list free in the 2027 Life Glow Up Kit, with a ChatGPT prompt for every chapter. | 2027 Visionboard Ideas | Magazine-style moodboard with a large walk-in closet photo and five colour fashion photos, titled vision board aesthetic | yes (AI people) |
| 22 | Collage + type tiles | 2027 manifestation board ideas: i claim it all | 2027 manifestation board ideas: money, love, the closet, shopping day, plus "i claim it all" and "same girl, bigger dreams". Board done? The free kit has the My 2027 list page and 30 prompts. | 2027 Visionboard Ideas | Grid of seven colour photos with two text tiles reading i claim it all and same girl, bigger dreams, titled 2027 manifestation board | yes (AI people) |
| 23 | Text list | 2027 vision board ideas (that aren't a beach) | 2027 vision board ideas that aren't a beach: a closet where you can see the floor, a savings number written down, a solo trip, asleep before 12. Write your own on the free 2027 list page. | 2027 Visionboard Ideas | Black and white list titled 2027 vision board ideas (that aren't a beach) with seven numbered ideas | no |
| 24 | Text checklist | Things i'm manifesting for 2027 (manifestation list) | Things i'm manifesting for 2027: a raise (asking this time), friends who clap when i win, money i don't panic about, a trip i pay for myself. Claim yours on the free My 2027 list page. | 2027 Visionboard Ideas | White checklist on black titled things i'm manifesting for 2027 | no |
| 25 | Text numbered | Journal prompts for 2027: 6 questions for january | Journal prompts for 2027: what am i done apologizing for? what money number scares me to say out loud? New year journal prompts for a personal rebrand, plus 30 more ChatGPT-ready prompts in the free kit. | Journal Prompts | Six numbered journal prompts for 2027 in black type on white | no |
| 26 | Text brief | Lifemaxxing 2027: the list (body, money, love, style) | Lifemaxxing 2027, one chapter at a time: walk daily, one money date a month, spf every day. A lifemaxxing guide with a ChatGPT prompt for each chapter, free in the 2027 Life Glow Up Kit. | Lifemaxxing | White text list on black titled lifemaxxing 2027: the list, with body, money, love, style, beauty and home | no |
| 27 | Notes | Vision board ideas 2027: my notes app list | Vision board ideas for 2027, notes app version: the closet i'm saving for, $300 a month into savings, pilates 3x a week. Write your 2027 list free at issue11.app. | 2027 Visionboard Ideas | Dark-mode phone note titled vision board 2027 with four list items and a link to issue11.app | no |
| 28 | Notes | Journal prompts for jan 1 (new year journal prompts 2027) | Journal prompts for jan 1: what did 2026 teach me, what am i done saying yes to, who do i want to see more of? 30 more prompts in the free 2027 Life Glow Up Kit. | Journal Prompts | Dark-mode phone note titled journal prompts for jan 1 with four prompts and a link to issue11.app | no |

Link for all: https://issue11.app/rebrand-kit. Metricool (only after Megan's "go"): pins 19–22 `isAiGenerated: true, isAiGeneratedPerson: true`; pins 23–28 no AI flag (Megan: "no need to mention that the pins without images are AI"). Board ids: batch1/SCHEDULE-NOTES.md. Suggested pacing: vision board pins first (Nov 16–25), ahead of the Dec–Jan spike.

## Visual QA (design/VISUAL-QA.md), Nov 15
Rendered all 10 with Playwright at 1000×1500 and checked 390px and 236px contact sheets. Fixed before publishing:
- Pin22 title overflowed into the grid ("board" hidden) → re-set to 2 lines at 96px.
- Pin22 beauty tile (e28) cut at the hairline → focal point moved to the top.
- Pin20: the bag in n17 could show a brand plate, and the visor in e34 has printing → swapped for n16 and e31.
- Pin19 "my own desk" tile (e29) showed a person with something at her mouth → swapped for e27 (desk + book), which matches the caption.
- Text pins 23–26 had empty space and small list text at 390px → list text 42 → 48–52px; one-word orphans reworded.
Re-checked after publishing: live Pin19, Pin28 and canvas.json match local; the 33 existing boards and notes are untouched.
