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

## Rounds 4–6 · CT31–CT67 (Megan, Nov 16: "Can you use more images that are in the file ?" · "It's in google drive" · "Make the pins look like an Indie magazine" · "But I want more options with photos in it" · "I like when the images are full bleed" · "keep generating I want to see different styles" · "ohhh the magazine covers are amazing")

Photos: 14 from Megan's Google Drive folder "ISSUE11 Images" (AI-generated beauty + money editorials), saved as JPGs in `drive/` and uploaded to the canvas assets. Skipped one with a car-maker logo on the seat (Visual QA rule 3). Every line is from BANK.md word for word (approved section only); cover lines are real ISSUE11 articles with their real counts.

Megan's likes so far (her screenshots, Nov 16): the existing type cards (black + lilac uppercase, lavender italic, "me 🤝 2027", white roman + italic "I love my hot bod"), CT03 (magazine cover with photo), CT21 (DREAM GIRL cover), CT42 (lavender + inset photo + italic line), CT45 (full-bleed red + I AM THE PRIZE, ALWAYS), and the covers CT51–CT53. Common thread: one line, huge clean type (roman + italic), small logo on top, issue11.app at the bottom, full-bleed photos, magazine covers.

- Round 4 (CT31–CT40, `gen4.py`): indie-magazine pages: paper stocks, running header, folio, figure captions, photo inset.
- Round 5 (CT41–CT53, `gen5.py`): Megan's liked style with photos, mostly full bleed; CT51–CT53 = magazine covers (THE PRIZE, GLOW UP, MONEY).
- Round 6 (CT54–CT63, `gen6.py`): split screen, triptych, circular text around a round photo, photo-filled knockout type (DREAM GIRL, $10,000), four-photo grid, price-tag sticker, blurred backdrop + polaroid, quiet corner caption, arch window.
- More covers (CT64–CT67, `gen7.py`): SELF LOVE, SLEEP, BUSINESS, WORTHY.

Visual QA (390 + 236): passed after fixes: type moved off mouths and chins (31, 40, 45, 46, 49), full-bleed versions of 41/44/46/47/48, readable mastheads, overlapping circle text, cut-off knockout words, vertical cover date moved off faces (64, 66), lilac label contrast (67).

## Round 7 · CT68–CT77 + Megan's loves (Nov 16)

Megan, word for word: "Keep up Indie magazine style pins please I want to see more options !" · "these I absolutely love" (CT61 quiet full-bleed + corner caption; covers CT64 SELF LOVE, CT65 SLEEP, CT66 BUSINESS, CT67 WORTHY) · "This one is pretty cool too" (CT55 triptych) · "You can do the ISSUE11 logo a bit bigger on each but it's excellent" / "and the issue11 logo can be a bit bigger too".

Done: the logo is bigger on all 77 CT pins (bottom logo 66 → 92px, top logo 52 → 76px). Round 7 (`gen8.py`, Drive photos): band masthead + full bleed (68), spread with type stack (69), "Money, an index" page listing Megan's money lines (70), giant $ + tall photo (71), two looks with credits (72), framed full bleed (73), square portrait + two-column credits (74), letter page + polaroid (75), three-panel gatefold (76), broadsheet front page (77).

LOVED so far (template candidates): magazine covers CT21, CT51–CT53, CT64–CT67 · CT61 quiet full-bleed · CT55 triptych · CT42 lavender inset + italic · CT45 full-bleed huge type · CT03 · the type cards (black + lilac, lavender italic, "me 🤝 2027", white roman + italic).

## Round 8 · CT78–CT87 (Megan: "Can you create some more pins with different images too ?? And different layouts" · "I also want the text on the pins to correlate to the images")

8 new Drive photos (`gen9.py`), each paired with the BANK line it literally shows:
| # | Photo | Line | Layout |
|---|---|---|---|
| 78 | in bed on a pile of cash | I wake up to money | full bleed + hotel door-hanger tag |
| 79 | lounging on cash in a blue suit | I make way more money than what I'm able to spend | full bleed + outline type |
| 80 | glowing skin, pink coat, wall of pink money | A healthy mind, a fit body, and lots of money $$$ | photo + three colour bands, one phrase each |
| 81 | money raining down | My business is bringing sooooo much money | full bleed + words on falling bill tags |
| 82 | red liner close-up | My face card is absolutely lethal | photo + zoom loupe on the eye |
| 83 | blue liner, direct stare | I am the prize, always | huge cropped type THE PRIZE |
| 84 | pink liner, gloss | I am my own dream girl | split seam, type across the edge |
| 85 | big hair, cream knit | I glowed up so hard now my enemies are crying | indie cover B: vertical title + issue number |
| 86 | pink money wall | A healthy mind, a fit body, and lots of money $$$ | magazine cover (HEALTHY) |
| 87 | bed of cash | I wake up to money | magazine cover (WAKE UP) |

Visual QA (390 + 236): passed after fixes: top logo moved off faces (79, 81, 83, 84), zoom loupe re-aimed at the eye (82), cropped type made readable (83), title moved off the chin (84).

## Round 9 · CT88–CT97 (Megan: "can you look at the indie magazine layouts and copy them ?" · "this follows the magazine cover layout we already approved… there is no point of giving me layouts we already approved")

APPROVED TEMPLATE (Megan, Nov 16): the magazine cover (CT21, CT51–CT53, CT64–CT67, CT86, CT87). Never send it again as a "new option"; it's a reusable template now. Other loves so far: CT61 quiet full-bleed, CT55 triptych, CT42, CT45, CT03, the type cards.

Round 9 copies her inspo spreads (`design/magazine/inspo/`, library in `design/magazine/MISE-EN-PAGE.md`), `gen10.py`:
88 overprint type on cash photo (editorial-25 "Happy Victims") · 89 star windows (editorial-12 "trust the process") · 90 repeated name + ID list (editorial-30) · 91 outline type + mint bubble note (editorial-15) · 92 vertical stacked words + columns (editorial-21 "Not the icing on the cake") · 93 giant translucent word, off the face (editorial-22 "BAD") · 94 bleed word + text column (editorial-27 "CO2MO") · 95 giant lowercase word + 4 photo specimens (editorial-33 "gaijin") · 96 giant letters over columns (editorial-20 "WASHINGTON") · 97 headline over photo + repeated vertical word + bar (editorial-08). Each photo matches its BANK line.

Megan on round 9 (Nov 16, word for word): "Okayyy those are really cool to test out !" → CT88–CT97 join the test set (status: approved to test, not scheduled; the Manager schedules after Megan's go).

Megan's picks from round 9 (Nov 16, word for word): "91, 90, 89, 95, 93 except the image is more hair focused so we can say "I love my long hair"". LOVED TEMPLATES added: CT89 star windows · CT90 repeated name + ID list · CT91 outline type + bubble note · CT93 giant translucent word (now "LONG HAIR" / "I love my long hair", line added to BANK.md as Megan's) · CT95 giant lowercase word + specimens. Not picked: 88, 92, 94, 96, 97.

## Round 10 · CT98–CT109 (Megan: "now give me a few more pins and then we can switch styles")
Pins in her inspiration formats with her inspiration lines (`gen11.py`, `../inspo-megan/README.md`): 98 soft lowercase on photo (richer and prettier) · 99 message bubbles (tea) · 100 loop with arrows (i'm sexy) · 101 loud poster type (prettier and hotter) · 102 subtitle line on photo (I am iconic) · 103 plain lowercase card (lucky girl syndrome) · 104 dictionary card (muse) · 105 huge lowercase white on black (big deal) · 106 pink card + emoji (Spoiled by the Universe) · 107 pink text over photo (never let a loser) · 108 cosy after photo (it all worked out) · 109 big caps three beats (brains, beauty & booty). All Inter Tight. Visual QA 390 + 236 passed after fixes (hidden words on 100/104, contrast on 102/107).

Megan on round 10 (Nov 16, word for word): "Ok those are all winners !!!" → CT98–CT109 all join the LOVED templates.

## Template set (as of Nov 16)
- APPROVED: magazine cover (CT21, CT51–CT53, CT64–CT67, CT86, CT87)
- LOVED: CT03, CT42, CT45, CT55, CT61, CT89, CT90, CT91, CT93, CT95, CT98–CT109, plus the earlier type cards (black + lilac, lavender italic, "me 🤝 2027", white roman + italic)
- To test: CT88, CT92, CT94, CT96, CT97 (not picked)

## Rounds 11–12 · viral copies (Nov 16) · research in ../viral/README.md
- CT110–CT121 (`gen12.py`): letter + "Send this to yourself" · orange + blue italic · photo + small caption · stacked "I am the prize" · pink centred quote · spaced words · money photo + italic · note on the wall · repeated line with one highlighted · olive + italic · black + pink 2027 · dark celestial. Megan: "also the last pins you made were perfection" → LOVED.
- CT122–CT131 (`gen13.py`, manifestation + vision board, "all year long" trend): big pink "manifesting" over photo · TONIGHT save-to-affirm card · repeated blocks · aura gradient · Notes-app manifestation journal prompts (article) · 369 method page · 2027 vision board photo grid · film caption · dreamy photo + italic · torn paper note.

## Round 13 · CT132–CT142 (Nov 16) · more viral manifestation formats + angel numbers
Source: ../viral/2026-11-16-viral-manifest2.json + viral-vb-manifest (364 manifestation pins ranked by saves). Megan: "Ohhh we can do angel numbers too !!!" BANK lines only.
- 132 · 8888 save-to-affirm card (viral 1,532) · 133 · 111 over sky photo · 134 · 777 photo + red band · 135 · angel numbers sheet (111/222/333/777/888)
- 136 · repeated pink line over money photo · 137 · big pink spaced text · 138 · spaced caps on cream · 139 · bold italic over money photo · 140 · sticker over photo · 141 · old paper save card · 142 · pink 369 method
- Angel number pins (132–135): v2 lines after Megan "I am not a fan of what you wrote": viral format (number + KEYWORD + one plain line to "you"), lexicon phrases inside sentences. 135 is now the viral 3×3 chart. See ../affirmations/ANGEL-NUMBERS.md.

## Angel number format test · CT143–CT146 (Nov 16)
Megan: "I think we should do them all but we need to decide on the pin aesthetic format". Same 888 in A aura gradient · B full-bleed photo · C photo + colour band · D minimal cream card. Waiting for her pick.
Megan also noted (Nov 16): "there are also carousels we can repurpose from Instagram to TikTok to Pinterest" → angel numbers can become a carousel (cover + one number per slide).

## ❤️ Megan's loved formats (Nov 16, word for word: "Ok so let me tell you the formats I like")
CT110–116, 118–122, 124–126, 129, 132, 133, 135–139, 142, 143, 144, 146 · plus CT147, the 128 redo (Megan, Nov 17: "yes 147 is cute too! Save it").
Angel numbers: formats A (143 aura), B (144 photo) and D (146 cream card) are all liked. C (145) is not.
Megan, Nov 16: "Ok I think we have enough formats". Stop making new format rounds. Next is pins in these formats, then a Barbie series from her Drive upload.

## Doll series · round 1 · CT149–CT162 (Nov 17)
Megan's AI doll photos (Drive "glammi_barbie_doll…", drive-barbie/b01–b14) + her 18 viral caption picks (BANK). Megan: "Make sure every facial expression matches with the quote". Memes (pink band on top + photo, the top "barbie quotes" format): 149–155, 157. Quotes over a full-bleed photo: 156, 158–162.
Skipped photos: readable Chanel logos, a stock "PNG" watermark, a Google Lens screenshot icon, cigarettes (3).
Keyword (Megan): "funny quotes humor". Pinterest check: the top 5 pins have 1.6k–5k saves, but the median of the top 40 is 76 and 22 of 40 have <100, so it's winnable. Long-tail: funny quotes humor about life / hilarious / short / memes / jokes / work / wallpaper.

## Doll series · round 2 · CT163–CT172 (Nov 17)
❤️ Megan liked 156, 158, 160, 161, 162 (quote over a full-bleed photo). "157 is good for messaging but i don't like that style of pin" → the pink meme band is out. 163–170 redo the meme captions in the liked style, with text moved below the chin on the square photos. 171 "WHY BE MOODY…" and 172 "Are you free tomorrow?…" use the 2 lines Megan sent (BANK).

## ❤️ Favourites section on the canvas (Nov 17)
Megan: "put aside on a different work design board all the numbers I saved and liked ... You can also keep them on the same board but separated from the rest". The boards were moved to a "❤️ Megan's favourites" section at the far right of the canvas (x ≥ 22360):
- Covers (approved): 21, 51–53, 64–67, 86, 87
- Loved templates: 03, 42, 45, 55, 61, 89–91, 93, 95, 98–109
- Viral formats: 110–116, 118–122, 124–126, 129
- Manifestation + angel numbers: 132, 133, 135–139, 142–144, 146
- Vision board grid: 147, 148
- Doll series: 156, 158, 160–162, 165, 166, 169, 170, 172 (Megan, Nov 17: "165 is good 166 / 169 / 170 / 172")

## Variants · CT173–CT184 (Nov 17)
Megan: "Do you think we have a good variety of pins to test now ? You can mix and match images too / Especially with pins similar to 42, 95, 45, 122, 133, 144, 62". There are 2 new photo + line pairs per format. CT62 was added to the favourites section.
Shopping series (Megan, Nov 17): 5 lines in BANK. Waiting for her to show which "slavic girl with fur coat" photo she means.

## Shopping series · CT185–CT190 (Nov 17)
Megan's fur-coat shopping photos (pasted in chat, saved in shop/*-full.jpg) + her 6 lines from BANK. Megan: "the logos don't need to be cropped out", so the full photos are used with the Dior/Chanel bags visible (Megan's call after the trademark flag). The text sits on the coat between the face and the bags.
- Variants: 173, 174, 177–184 · Shopping series: 185–190 (Megan, Nov 17, moved to favourites)

## Magazine covers · batch 2 · CT191–CT200 (Nov 17)
Megan: "I think we should do magazine cover styles like 87, 86, 51, 52m etc 64". Approved cover() template with the shopping, Drive and doll photos + BANK lines. The cover lines use real article counts.
