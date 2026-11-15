# Pin batch 3 (Nov 15, 2026): magazine-page pins, for Megan's review
Drafts only. Nothing is scheduled. Megan: "Yes we could do magazine layout style for the pins too".
Canvas: https://claude.ai/artifact/MZr3GzSS5YdENf5x4D3DrT (note "Pinterest batch 3 · magazine pages", rows at y 11900 and 13520).
All pins link to **https://issue11.app/rebrand-kit** (free 2027 Life Glow Up Kit: "My 2027" list page, 6 chapters, 30 ChatGPT prompts, 30-day challenge, future self letter).
Each pin is one layout from `design/magazine/MISE-EN-PAGE.md` §7, adapted to 1000×1500: running head (kicker + "issue11 · 0NN" page number), colour photo, black-and-white type, footer "Free 2027 Life Glow Up Kit → issue11.app" with the ISSUE11 logo. Inter Tight only. No collage overlap.
Source: `generator-b3.py <scratch dir>` writes `project/Pin29..36.dc.html` (it reads asset ids and the doc() shell from `../batch2/generator-b2.py`). Render: `node render.js <dir> png`. PNGs + phone sheets: `png/` (`sheet-390.png`, `sheet-236.png`).

## Keyword data (real numbers only)
Google US monthly (Mangools, Nov 14, DEMAND-CHECK): how to glow up 9,300 · glow up tips 5,000 · vision board ideas 43,400 · lifemaxxing 1,200 · personal rebrand 40 · future self journal 40 · 2027 vision board 50 (12-month avg, spikes Dec–Jan).
Pinterest autocomplete (Apify `lergassy~pinterest-search-scraper`, searchType keywords, Nov 15, 1 call; raw: `../2026-11-15-batch3-autocomplete.json`):
- "glow up 2027" → glow up 2027 wallpaper, 2027 glow up vision board, glow up tips 2027, 2027 glow up plan, my glow up 2027
- "manifesting 2027" → manifesting wallpaper 2027, manifesting board 2027, manifesting vision board 2027, manifesting for 2027
- "that girl aesthetic" → …lifestyle, …routine, …quotes, …vision board, …wallpaper
- "future self" → future self aesthetic, letter, quotes, journal, questions; "letter to future self", "dear future self"
- "lifemaxxing" → lifemaxxing aesthetic, wallpaper, quotes, 101, tips, magazine
**Missing:** Google volume for "glow up 2027", "manifesting 2027", "that girl aesthetic" (no paid Mangools call this run). Pinterest volumes aren't public.

## SEO rows
| # | Layout | Title (keyword first) | Description | Board | Alt text | AI flag |
|---|---|---|---|---|---|---|
| 29 | L · quote across full-bleed photo | How to glow up in 2027: pick one thing, do it for 30 days | How to glow up without changing everything at once: pick one thing, do it for 30 days, then the next one. Glow up tips for 2027 with a 30-day challenge and 30 ChatGPT prompts, free in the 2027 Life Glow Up Kit. | Glow Up Tips | Colour editorial photo of a woman in a silver jacket with the quote how to glow up: pick one thing, do it for 30 days, then the next one | yes (AI person) |
| 30 | M · giant overprint type + info box | Glow up 2027: what's inside the free life glow up kit | Glow up 2027, the whole-life version: a My 2027 list page, 6 chapters (body, money, love, style, beauty, home), 30 ChatGPT prompts, a 30-day challenge and a letter from future you. Your 2027 glow up plan, free. | Glow Up Tips | Magazine cover with a colour photo of a blonde woman in a fur coat and giant black type reading glow up 2027, plus a box listing what is inside the free kit | yes (AI person) |
| 31 | T · stacked letters + portrait | Lifemaxxing 101: body, money, love, style, beauty, home | Lifemaxxing 101 for 2027: one chapter at a time, body, money, love, style, beauty, home, with a ChatGPT prompt for each. A lifemaxxing guide in magazine form, free in the 2027 Life Glow Up Kit. | Lifemaxxing | Giant letters spelling LIFEMAXX down a white column next to a colour photo of a woman with long dark hair at a desk | yes (AI person) |
| 32 | V · repeated name + ID card | Future self ID card: name, future you. year, 2027 | Future self aesthetic, as an ID card: name future you, mornings no phone till 9, $500 a month saved, motto Become YOU. Write a letter from future you on the free page in the 2027 Life Glow Up Kit. | Journal Prompts | The words future you repeated four times in white on black above a colour portrait and an ID card list for future you | yes (AI person) |
| 33 | Z · words in ruled boxes | Manifesting 2027: me 🫱🏻‍🫲🏽 2027, and it's finally my year | Manifesting 2027? Write it down first. Me 🫱🏻‍🫲🏽 2027, and it's finally my year. Make your 2027 manifestation list on the free My 2027 list page, with 30 prompts to fill it. | 2027 Visionboard Ideas | Words stacked in black ruled boxes reading me handshake 2027, and it's finally my year, next to a colour photo of a woman in a white fur coat | yes (AI person) |
| 34 | D · huge word + offset photo | Personal rebrand list: can't talk rn, i'm rebranding | Personal rebrand ideas for 2027: audit my socials, clear out the closet, find a signature scent, one money date a month. Plan your personal rebrand with 6 chapters and 30 ChatGPT prompts, free. | How to rebrand yourself | Huge black word rebrand under a short personal rebrand list and a framed colour photo of a woman in a brown fur coat at night | yes (AI person) |
| 35 | H · pull quote + full photo | That girl aesthetic: i'm the art director of my life | That girl aesthetic, my version: i'm the art director of my life. Plan your 2027 with 30 ChatGPT prompts and a 30-day plan, free in the 2027 Life Glow Up Kit. | Glow Up Tips | Colour photo of two women in cream coats walking at night seen from behind, above the quote i'm the art director of my life | yes (AI people) |
| 36 | P · portrait + itemised list | 2027 vision board ideas: date nights in the rain, $5k saved | 2027 vision board ideas, as a list: date nights in the rain, a closet i actually wear, a $5k emergency fund, learn italian (badly), phone off at 10. Pin the pics, then write your list on the free 2027 page. | 2027 Visionboard Ideas | Tall colour photo of a couple kissing in the rain next to a numbered list titled 2027 vision board ideas | yes (AI people) |

Link for all: https://issue11.app/rebrand-kit. Metricool (only after Megan's "go"): all 8 show AI-generated people → `isAiGenerated: true, isAiGeneratedPerson: true`. Never present them as real customers or results.

## Visual QA (design/VISUAL-QA.md), Nov 15
Rendered all 8 at 1000×1500 with Playwright and checked 390px and 236px sheets plus full size. Photos chosen for whole faces (l19 not used). Fixed before publishing:
- Pin29: the right-edge vertical credit was cut off at the top → both credits re-set with writing-mode inside the frame.
- Pin32: the outlined "future you" lines overlapped their own strokes (tight tracking) → 4 solid lines at 184px, filling the width.
- Pin35: the quote touched the right edge and left a gap → 92px quote, subline moved up and enlarged to 40px.
- Pin36: list too small at 390px → list 32 → 38px, portrait narrowed to 470px.
- Pin34: list 32 → 35px, "in bed by 12 (most nights)" shortened (it wrapped).
Checked: no text on faces, no brand logos or readable signs, the ISSUE11 logo is whole on every pin, colour photos only.
Re-checked after publishing (version 1794717961-0b80): live Pin33, Pin19 and canvas.json are byte-identical to local; the 43 existing boards and 4 notes are untouched.
