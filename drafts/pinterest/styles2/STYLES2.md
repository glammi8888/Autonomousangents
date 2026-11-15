# Quote pin styles · 20 options · Pin103–Pin122 (Nov 15, 2026) · drafts, not scheduled

Megan: "Now work with Claude design and give me 20 different pin styles just for the quotes". Megan picks by number.
Canvas: https://claude.ai/artifact/MZr3GzSS5YdENf5x4D3DrT, title note "Quote pin styles · 20 options" (y 34220), boards at y 34460–39320, 5 per row. Board titles start with the number.
Source: `python3 generator-styles2.py <dir>` writes `<dir>/project/Pin103..Pin122.dc.html` and reuses `../styles/generator-styles.py` (st.doc, st.logo, st.ph, st.url). Render: `node ../styles/render.js <abs dir> <abs dir>/png` (the styles render.js loads the local Inter Tight italic that style 17 needs). Contact sheets: `png/sheet-390.png`, `png/sheet-236.png`.

Copy: every line is from `../affirmations/BANK.md`, word for word. The only changes are curly apostrophes, line breaks, CSS uppercase on 5 formats (receipt, magazine cover, tabloid, label tape, letter board) and splitting Pin104 into two bubbles at its full stop. No invented titles, kickers or taglines. UI furniture only: a timestamp (103, 106), a lock-screen date and time (108), the January 2027 month grid (115), bars standing in for book text (107).
Formats: taken from the viral quote pins (`../2026-11-15-viral-quote-pins.json`; the top "that girl quotes" pin, 5,518 reactions, is the roman + italic stack, style 17) plus Megan's brief. All generic: no app logos, usernames or trademarks.
Accent: lilac #D9B3FF, the colour actually on Pin82. The brief said #C8A2F0, but Pin82's file has #D9B3FF.

| # | Pin | Style | Line (BANK.md) | Imitates | Photo |
|---|---|---|---|---|---|
| 1 | 103 | Text-post screenshot | I cannot wait to prove to the people doubting me that they were wrong | a text post screenshot (avatar = our logo, no name or handle) | – |
| 2 | 104 | Message bubbles | I am no longer proving my worth to someone. You either value me or you're OUT! | a dark-mode chat, two sent bubbles in lilac | – |
| 3 | 105 | Sticky note | Get up girl, you got people to prove wrong | a taped paper note on black | – |
| 4 | 106 | Receipt | I glowed up so hard now my ex is crying | a till receipt with barcode | – |
| 5 | 107 | Highlighted book page | Imagine what your bullies will feel when they see you succeed | a book page with one passage highlighted (lilac) | – |
| 6 | 108 | Lock screen with clock | I wake up to money | a phone lock screen with a notification | m24 (money, AI) |
| 7 | 109 | Magazine cover line | My face card is absolutely lethal | a cover with our logo as the masthead | e35 (beauty, AI) |
| 8 | 110 | Tabloid front page | I glowed up so hard now my enemies are crying | a tabloid headline in black/white blocks + framed photo | e36 (editorial, AI) |
| 9 | 111 | Ransom cut-out letters | I am the prize, always | cut-out words and letters | – |
| 10 | 112 | Film still subtitles | I only date a guy if he can afford me | a letterboxed film still with subtitles | l23 (love, AI) |
| 11 | 113 | Label-maker tape | I'm the girl who always makes it work | embossed label tape | – |
| 12 | 114 | Giant number (Swiss) | My life can do a 180 in just 1 year | a Swiss poster, 180 running vertically | – |
| 13 | 115 | Calendar page | 2027 is the year I lifemaxx | a January 2027 month page, 1 Jan circled | – |
| 14 | 116 | Search bar + results | Dream life is on its way | a search bar over an image results grid | e21, m26, e22, e20 (AI) |
| 15 | 117 | Lyric card on photo | I'm the art director of my life. I create it page by page. I make my own opportunities. | a song-lyric share card (no music-app branding) | e27 (desk, AI) |
| 16 | 118 | Polaroid caption | I am my own dream girl | an instant photo with a caption | n16 (portrait, AI) |
| 17 | 119 | Roman + italic stack | I love my hot bod | the top viral "She can. She will." format, in Inter Tight | – |
| 18 | 120 | Felt letter board | I only attract the best of the best | a felt letter board | – |
| 19 | 121 | Fortune slip | I'm the luckiest girl on the planet | a fortune-cookie slip | – |
| 20 | 122 | RULE-BREAKER typewriter | My business is bringing sooooo much money | a typed page, in Courier Prime (monospace, not Inter Tight). Megan decides | – |

Other rule notes for Megan: Pin109's logo is masthead-sized (150px tall), larger than our fixed 40px logo, because a cover needs a masthead. The lilac fills on 104 and 111 are the only accent use.

**Visual QA (design/VISUAL-QA.md):** every PNG checked at 1000×1500, plus sheet-390 and sheet-236. Fixed before publishing: Pin108 clock sat on the woman's face (the photo now starts under the clock); Pin103, 106, 122 had too much empty space and small type (bigger, centred); Pin104 and 121 type enlarged for the 236px feed; Pin108 url moved off the busy money area. Faces checked whole on 108, 109, 110, 112, 117, 118. Re-checked after publishing: live Pin108 and Pin122 match the local files byte for byte; all 11 asset ids exist on the canvas. Local render uses a fallback monospace for Pin122; the canvas loads Courier Prime.
**If scheduled:** pins 108, 109, 110, 112, 116, 117, 118 need isAiGenerated: true and isAiGeneratedPerson: true (116 shows a person in m26). Text-only pins get no AI label. SEO rows get written once Megan picks styles.
