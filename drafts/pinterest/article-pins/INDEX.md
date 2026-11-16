# Article pins: one 2:3 "save this" image per live article

Made by the hourly Pinterest agent. These are images to drop into the matching Framer blog article (so readers can save the article to Pinterest), not scheduled pins. The Manager places them in Framer after Megan's go. Nothing here is uploaded anywhere yet.
Source boards: Claude Design Lead Magnets canvas (https://claude.ai/artifact/MZr3GzSS5YdENf5x4D3DrT), row "Hourly 2026-11-16 · Pinterest agent". PNGs: `png/`. Re-render: `node render.js`. Photos are AI-generated library images (AI label applies if any is ever posted as a pin).

| Pin | Article (live) | PNG | Pin title (keyword first) | Alt text | Visual QA | Status |
|---|---|---|---|---|---|---|
| ArticlePinNYVB | issue11.app/blog/new-year-vision-board | png/ArticlePinNYVB.png | New Year Vision Board Ideas 2027: What to Put on It | Four colour editorial photos above the title "New year vision board ideas 2027" and a five-point list of what to put on your board | Pass 390 + 236 (Nov 16) | ready for Framer |
| ArticlePinNYVB2 | issue11.app/blog/new-year-vision-board | png/ArticlePinNYVB2.png | New Year Vision Board 2027 Ideas + a Vision Board Party Plan | Collage of glow up, love and money photos under "New Year Vision Board", with the line "My life can do a 180 in just 1 year" | Pass 390 + 236 (Nov 16) | ready for Framer |
| ArticlePinVBI | issue11.app/blog/vision-board-ideas | png/ArticlePinVBI.png | Vision Board Ideas 2027: One Image for Each Area of Your Life | Four photo cards for money, home, love and the version of you, each with one vision board idea | Pass 390 + 236 (Nov 16) | ready for Framer |
| ArticlePinVBE | issue11.app/blog/vision-board-examples | png/ArticlePinVBE.png | Vision Board Examples: 10 Boards to Copy in 2027 | "Vision board examples" with career, home and personal rebrand photos and a list of 10 board types, from one word to digital | Pass 390 + 236 (Nov 16) | ready for Framer |
| ArticlePinWOTY | issue11.app/blog/word-of-the-year-ideas | png/ArticlePinWOTY.png | Word of the Year Ideas 2027: 120 Words + How to Choose Yours | Text-only pin: "Word of the year ideas" over eight boxes of word ideas grouped by what you want more of, from confidence to boundaries | Pass 390 + 236 (Nov 16) | ready for Framer |
| ArticlePinNYA | issue11.app/blog/new-year-affirmations | png/ArticlePinNYA.png | New Year Affirmations 2027: 50 Short Affirmations for Money, Love + a Fresh Start | A crystal walk-in closet (no people) with the line "Dream life is on its way", the title "New year affirmations" and five topic tags: fresh start, confidence, money + work, love, calm | Pass 390 + 236 (Nov 16) | ready for Framer |
| ArticlePinNYJ | issue11.app/blog/new-year-journal-prompts | png/ArticlePinNYJ.png | New Year Journal Prompts 2027: 40 Reflection + Goal Setting Questions for One Evening | Text-only pin: "New year journal prompts" in a black band over two columns, "Look back" and "Look ahead", each with five prompts from the article | Pass 390 + 236 (Nov 16) | ready for Framer |

Keyword check for ArticlePinVBE: Pinterest autocomplete (Apify, Nov 16) suggests "vision board examples" with "inspiration", "aesthetic", "life", "career" and "manifestation" variants. Raw: `../2026-11-16-vision-board-examples-keywords.json`. No volume figure from Pinterest; Google US 11,000/mo per QUEUE.md.

Keyword check for ArticlePinWOTY: Pinterest autocomplete (Apify, Nov 16) top suggestion is "word of the year ideas", then "word of the year vision board", "word of the year journal". Raw: `../2026-11-16-word-of-the-year-keywords.json`. No volume figure. Text-only, no photos, so no AI label needed. Words are copied from the article's list.

Keyword check for ArticlePinNYA: Pinterest autocomplete (Apify, Nov 16) suggests "new year affirmations" with "short", "money", "love", "quotes" and "wallpaper" variants. Raw: `../2026-11-16-new-year-affirmations-keywords.json`. The quote is Megan's line from BANK.md ("Dream life is on its way"). The article's own 50 affirmations are not in BANK.md, so the pin shows only their 5 category names and quotes none of them. Photo is an AI-generated library image (AI label applies if ever posted as a pin).

Keyword check for ArticlePinNYJ: Pinterest autocomplete (Apify, Nov 16) suggests "new year journal prompts" with "goal settings", "reflection", "simple" and "short" variants. Raw: `../2026-11-16-new-year-journal-prompts-keywords.json`. The 10 prompts on the pin are copied word for word from the article. Text-only, so no AI label needed.

Next articles without a pin (New Year first): december-january-journal-prompts · how-to-make-a-vision-board · journaling-prompts.
