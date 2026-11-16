# Colour + variety test · 10 pins · Nov 16, 2026 · waiting for Megan's pick

Megan (Nov 16, word for word): "I also want to see more variety and colors on the pins and making them a bit more irresistible, Can I see some examples with Claude Design?" · then live: "can we do pins where images are full bleed and with text on top ?" · "and make sure the images correlate with the text" · "less black and white, please inspire yourself from viral pins too".

Canvas: https://claude.ai/artifact/MZr3GzSS5YdENf5x4D3DrT, section "Color + variety examples · Nov 16" (y 45300, boards CT01–CT10, 5 per row). Source: `python3 gen.py` writes CT01–CT10.dc.html; `node render.js` renders png/ + sheet-390/236. This test overrides the black-and-white rule for these 10 only; the palettes Megan picks become the new rule. Nothing is scheduled.

Viral inspiration (`../2026-11-15-viral-quote-pins.json`, 151 top quote pins): the most-saved use blush pinks (#FCECEF, #FCD4DA), one short line of big type, and photos with words on top. So: 6 full-bleed photo pins, a blush one-line type card (10), and coloured inks instead of black on the text pins (8, 9). Quotes are BANK.md lines word for word; article facts are copied from the live articles. Photos are AI-generated library images, each picked to match its line. Logo bottom-left on all 10.

| # | Palette | Layout | Hook (first words) | Type · link | Keyword title | Photo ↔ text | Why it should get saved |
|---|---|---|---|---|---|---|---|
| 01 | Emerald #0B5D45 + mint #9DF2C8 | Full-bleed photo, gradient fade, text on top | "I'm making money in my sleep" | Quote (BANK) | Money affirmation quotes | m28: a woman asleep on a bed of cash | Money manifestation lines are a top saved topic; the photo literally shows the line |
| 02 | Butter yellow #FFE36E on dark photo | Full-bleed photo, giant uppercase type | "My dream life wants me" | Quote (BANK) | Affirmation quotes aesthetic | e20: a dream walk-in closet with chandeliers | Aspirational "dream life" image people pin to vision boards |
| 03 | Hot pink #FF3EA5 + red #E8112D | Full-bleed magazine cover | "Self love affirmations" | Article · https://issue11.app/blog/self-love-affirmations?utm_source=pinterest&utm_medium=organic&utm_campaign=self-love-affirmations | Self love affirmation quotes for women | n17: a confident woman in a fur coat | Cover look + "60 that feel true" promises a full list |
| 04 | Cherry red #D7092B highlight bars | Full-bleed photo, highlighted text | "I'm the girl who always makes it work" | Quote (BANK) | That girl quotes red | e29: a woman working at her desk | "That girl" quotes are a top search; the photo shows her making it work |
| 05 | Chocolate #3B2218 + baby blue #A9D4FF | Torn paper note | "How to stop overthinking at night" | Article · https://issue11.app/blog/how-to-stop-overthinking?utm_source=pinterest&utm_medium=organic&utm_campaign=how-to-stop-overthinking | How to stop overthinking at night | – (text pin) | 4 steps you can use tonight, all from the article |
| 06 | Cobalt #1F3FFF + white | Notes-app screenshot | "My nervous system is calm" | Quote (BANK) | Affirmation quotes short | – | Notes screenshots are a top viral format; "save for a hard day" gives the reason |
| 07 | Plum tint #4A0F3E + pink #FFC2E6 | Full-bleed tinted photo, carousel-style cover (1/6) | "Your vision board isn't broken. It's unfinished." | Article · https://issue11.app/blog/vision-board-for-manifestation?utm_source=pinterest&utm_medium=organic&utm_campaign=vision-board-for-manifestation | Vision board for manifestation | e21: a dream dressing room (a vision-board image) | Curiosity hook, from the article's own words, plus "5 steps to finish it" |
| 08 | Tangerine #FF7A1A + burnt orange #5A1E00 | "Save this" card | "Word of the year 2027" | Article · https://issue11.app/blog/word-of-the-year-ideas?utm_source=pinterest&utm_medium=organic&utm_campaign=word-of-the-year-ideas | Word of the year ideas 2027 | – | A reference card people come back to in December |
| 09 | Lilac #CDB4FF + deep purple #3B0F7A | Numbered list | "Answer before 2027" | Article · https://issue11.app/blog/new-year-journal-prompts?utm_source=pinterest&utm_medium=organic&utm_campaign=new-year-journal-prompts | New year journal prompts | – | 5 prompts from the article, a ready-made NYE ritual |
| 10 | Blush #FCD4DA + raspberry #C2185B | One-line type card (viral 2027 style) | "2027 is the year I lifemaxx" | Quote (BANK) | 2027 vision board quotes | – | Same format as the most-saved 2027 pins: one line, big type, pink |

Visual QA (390 + 236, Nov 16): passed after fixes. Pin 3's title broke as "AFFIRM-ATIONS" and covered its tags (set on two lines). Pin 10 ran off the edge (smaller type, centred). Pins 5 and 6 had empty space (bigger type, tighter card). The first pin 10 was a black-and-white control; Megan asked for less black and white, so it became the blush card, and pins 8 and 9 lost their black text. No faces cut off, no stray logos or readable signs, ISSUE11 logo fully visible bottom-left.

## Round 2 · CT11–CT20 (Megan: "show me more")

Source: `python3 gen2.py` (reuses gen.py's template). Canvas: section "More color examples · round 2", boards CT11–CT20 below round 1. Same rules: BANK.md lines word for word, article facts from the live articles, AI library photos matched to each line, logo bottom-left.

| # | Palette | Layout | Hook | Type · link | Keyword title | Photo ↔ text | Why it should get saved |
|---|---|---|---|---|---|---|---|
| 11 | Lavender #D9C8FF on deep violet | Full-bleed photo + checklist chips | "Glow up checklist" | Article · https://issue11.app/blog/how-to-glow-up?utm_source=pinterest&utm_medium=organic&utm_campaign=how-to-glow-up | Glow up checklist 30 day | e36: a glam editorial look | A tickable list people save to follow |
| 12 | Fire red #FF2D3F | Full-bleed portrait, giant type | "My face card is absolutely lethal" | Quote (BANK) | That girl quotes red | e24: a sharp beauty portrait | Beauty line on a beauty face; bold red type |
| 13 | Rose #FF9EC0 on wine | Full-bleed photo, roman + italic mix | "The love of my life is coming to me" | Quote (BANK) | Love manifestation quotes | l23: a couple kissing | Love manifestation is a top search; the photo shows it |
| 14 | Champagne gold #F2C14E | Full-bleed photo + tilted sticker | "I'm the luckiest girl on the planet" | Quote (BANK) | Lucky girl syndrome affirmations | n16: a glam night-out portrait | Lucky-girl lines are widely saved; sticker pops in the feed |
| 15 | Baby blue + cream | Full-bleed photo, text on top | "I only attract the best of the best" | Quote (BANK) | Affirmation quotes aesthetic | e22: a dream dressing room | "The best" shown as a dream room |
| 16 | Sage #DDF2C9 on forest | Full-bleed photo, fade | "I have all the time in the world" | Quote (BANK) | Calm affirmations | e27: a woman sitting calmly | Slow, calm line on a calm photo |
| 17 | Bubblegum #FF7EB6 + money green | Photo top, colour band, giant type | "I wake up to money" | Quote (BANK) | Money affirmation quotes | m24: a woman lying on a bed of cash | One short money line, huge type |
| 18 | Teal #06403F + gold #FFD23F | Full-bleed article cover, big number | "40 money affirmations" | Article · https://issue11.app/blog/money-affirmations?utm_source=pinterest&utm_medium=organic&utm_campaign=money-affirmations | Money affirmations that feel true | m26: a woman lying in cash | Number + promise ("that actually feel true") |
| 19 | Peach → pink gradient | Type card, italic + roman | "I am my own dream girl" | Quote (BANK) | Dream girl quotes | – | Viral "dream girl" line in the soft pinks the top pins use |
| 20 | Sky blue gradient + sparkles | Type card | "Thank you universe for all the blessings" | Quote (BANK) | Gratitude affirmations | – | Gratitude lines are saved daily; airy sky palette |

Visual QA (390 + 236): passed after fixes. 12's last word sat on the logo (smaller type, moved up). 15's white logo vanished on the white rug (switched to the black logo). 19 and 20 had empty lower halves (text centred). 13's type was enlarged.

## Round 3 · CT21–CT30 (Megan: "more magazine-like, art studio-like and I want some innovative aspects to it")

Source: `python3 gen3.py`. Canvas: section "Magazine + art studio examples · round 3", boards CT21–CT30 under round 2 (y 52480). Same rules: BANK.md lines word for word, article facts from the live articles, AI library photos matched to each line, logo bottom-left. Studio furniture (cover date, page folio, swatch names, "Specimen 11", "Room 11", riso stamp) is decoration, not a claim.

| # | Format (the innovative bit) | Palette | Line / article | Photo ↔ text | Keyword title |
|---|---|---|---|---|---|
| 21 | Magazine cover: masthead, cover story, cover lines = real ISSUE11 articles, barcode | Blush + hot pink | "I am my own dream girl" (BANK) | n17: a confident portrait | Dream girl quotes |
| 22 | Editorial spread: full-page photo, gutter shadow, pull quote, body copy as bars, folio | Sage + cream | "I have all the time in the world" (BANK) | e27: a woman reading calmly | Calm affirmations |
| 23 | Contact sheet with a grease-pencil circle and note | Light table + red marker | "My face card is absolutely lethal" (BANK) | e24: six crops of a beauty portrait | That girl quotes |
| 24 | Paint swatch card (colour chips + punch hole) | Pinks | "Dream life is on its way" (BANK) | e20: a dream closet as the third chip | Dream life aesthetic quotes |
| 25 | Riso 2-colour print: duotone photo, halftone grain, misregistered type | Pink + teal on cream | "I make way more money than what I'm able to spend" (BANK) | m26: a woman lying in cash | Money affirmation quotes |
| 26 | Taped collage with polaroids and highlighted steps | Kraft + rust | how-to-make-a-vision-board, its 5 steps | Closet, home, weekend photos = what goes on a board | How to make a vision board |
| 27 | Gallery wall: framed photo + museum label | Oxblood + gold frame | "The love of my life is coming to me" (BANK) | l23: a couple kissing | Love manifestation quotes |
| 28 | Type specimen poster: grid, crop marks, baseline rule, "Aa" | Tomato + cream | "I'm the art director of my life. I create it page by page. I make my own opportunities." (BANK) | – (type is the art) | I'm the art director of my life |
| 29 | Contents page: the 8 checklist items as a table of contents | Chartreuse + violet | how-to-glow-up checklist | e36: a glam editorial look | Glow up checklist |
| 30 | Polaroid board, each polaroid captioned with a word of the line | Sky blue + pink pins | "The right people, places, and moments find me" (BANK) | n18 = people, e21 = places, e35 = moments | Manifestation quotes aesthetic |

Links: 26 → https://issue11.app/blog/how-to-make-a-vision-board?utm_source=pinterest&utm_medium=organic&utm_campaign=how-to-make-a-vision-board · 29 → https://issue11.app/blog/how-to-glow-up?utm_source=pinterest&utm_medium=organic&utm_campaign=how-to-glow-up · 21 → https://issue11.app/blog/self-love-affirmations?utm_source=pinterest&utm_medium=organic&utm_campaign=self-love-affirmations

Visual QA (390 + 236): passed after fixes. 21's masthead covered the face (now one line above the head). 26 and 30 had polaroids hiding each other's captions (re-laid out). 24's name and 28's specimen text were enlarged.
