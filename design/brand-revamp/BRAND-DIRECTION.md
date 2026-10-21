# ISSUE11 brand revamp · direction notes (Design Room, Oct 21, 2026)
Megan, word for word: "i think we might have to revamp the entire design / i have an issue with the branding" · "it's indie. it feels like a creative studio. Right now ISSUE11 feels like a cartoon" · "We can keep our current logo because I like it" · magazines: "Real pictures not a cartoon mockup" · "I want a mix of digital images but also background photos of magazines so it feels real".

## Her references (Oct 21)
NIKO / Noir Form Studio posters · REP.CLUB shop app · museum app (hairline lists) · "Curated (Works) 16–24" gallery app · MOZOO agency site · "The Editorial Drop" Instagram set · Sexto 'Nplugged 2023 posters · Pleo stories · her Pinterest magazine board.

## What they share (the rules)
1. **Type does the design.** Huge grotesk headlines (condensed black caps like Curated/REP.CLUB, or tight Helvetica-style like Pleo/Sexto/Editorial Drop), small mono or small sans labels. No cute shapes.
2. **Flat and sharp.** Square corners, hairline rules, no shadows, no gloss, no bubbles, no stickers with drop shadows.
3. **Real photography, full-bleed.** Fashion/beauty portraits, often cropped tight on a face; type sits on or next to the photo.
4. **Black + white base, pink as the only accent** (refs use many colors; Megan chose pink only).
5. **Lots of white space next to one loud element.**
6. **Playful type moments, not illustrations** (text on a curve, giant word cut off at the edge, numbers 01/02/03).

## Kept
- The wavy ISSUE11 logo (Megan likes it).
- All flows and logic (tabs, saves = vibe, Make a page, templates not tools, Issue grid, print). Only the skin changes.

## Changes
- Cream 11 sticker → flat square "11" mark (black, pink edge), still draggable.
- Glossy pink glass buttons → flat black or pink rectangles.
- Archivo Black everywhere → condensed grotesk display + clean grotesk text + mono labels.
- Magazine shown as real photos: digital pages composited into ~5 real background photos of blank magazines (Megan to make in Midjourney). Prompts in chat Oct 21.

## Decided
- **Color: pink only** (Megan, Oct 21, to "pink + lilac/orange?": "nope"). Black + white base, hot pink is the one accent. No extra color blocks.

## Focus refs (Megan, Oct 21: "ok let's focus on this then")
Museum app (white, lowercase grotesk, hairline lists) · "Curated (Works) 16–24" gallery (giant condensed caps, numbered strip 01/02/03, mono labels) · "The Editorial Drop" (tight bold grotesk on close-up photos). Draft: 03-gallery-museum-editorial.png.

## Rule: real magazines only
Megan, word for word: "I don't want any picture of a magazine that isn't real". Never show a drawn, rendered or fake-3D magazine anywhere (app, landing, App Store, social). Physical magazine = real photos only (her printed proof, or real photographed blank magazines with her page placed on them). Digital pages inside the app are fine because they're shown as screens, not as fake objects. Her Pinterest magazine board (Oct 19 + 21) is the target look for the pages themselves.

## Update (Megan, Oct 21): "I don't mind showing real images of magazines if that makes sense... Like the ones i sent you. You can even use them as placeholders within the app"
- Real magazine photos are welcome: Home hero, Issue cover, Order my print, My shelf. Draft: 04-real-magazine-placeholders.png.
- The placeholders are cropped from her Pinterest saves = other people's work. **Internal mockups / Replit placeholders only. Never ship them in the App Store build, App Store screenshots, landing page or social.** Replace with her own printed proof photos or licensed/her Midjourney photos before launch.

## Favorite so far (Megan, Oct 21)
"my favorite so far has been the very first options you gave me" + she sent back the Home 4-options board (05-home-4-options.png). This board is the style reference: white, hairlines, condensed caps titles, tight bold grotesk, mono labels, wavy logo big, black 11 square, pink only, real magazine photos.

## More vibes (Megan, Oct 21: "some additional vibes for you")
Harry Richards poster-grid site on a phone · MAJI STUDIOS (one giant letter "M", tiny text) · Inner.co (huge wordmark cropped off the screen edge, photos labeled "001001.jpg", small right-aligned text) · Pryatki (full-bleed photo, soft pink backdrop).
Takeaways: one giant cropped word or letter per screen, very small secondary text, file-name style captions, full-bleed photos, generous white. Also: present app screens as real phones in hands / on a table (real photos), not flat mockups.
Also (same day): Apple Music concept (tile wall of covers, square + round crops, giant "Music" word cropped at the bottom, grey "+ Add" tile) · quiet still-life editorial (soft grey photos, one medium headline, small two-column text, a → arrow) · Maison Point Blue (tiny logo top center, small caps paragraph, one small photo in lots of white, logo big at the bottom).

## Fonts · LOCKED (Megan, Oct 21: "ok i like that")
From the Home 4-options board she loves. All free Google Fonts (OFL).
- **Titles:** Archivo Condensed (Archivo, width 62, weight 800), UPPERCASE, line-height ~0.86. e.g. "THE FREEDOM (ISSUE)".
- **Text + bold sentences:** Inter Tight (400 text, 800 tight sentences, letter-spacing about -0.04em).
- **Labels:** IBM Plex Mono 500, UPPERCASE, small (8–10px in mockups).
- **Logo:** the wavy ISSUE11 image, unchanged.
Colors: white/off-white base, black, pink accents (calm: baby pink #F7C6D9 small touches; text-pink #C2207E only for small readable pink text). No hot-pink blocks unless Megan asks.

## Melting titles · LOCKED (Megan, Oct 21: "2. melting")
Big hero titles (FREEDOM, EXPLORE, ISSUE 01, "THAT'S TODAY.") melt like the logo: Archivo Condensed 800 caps, smooth horizontal wave, medium strength (board 17, option 2). Only big titles melt; labels, body text and buttons never do.
How to build (for Replit): render each title as an SVG/canvas with a row-by-row sine shift (amplitude ≈ 2% of the text width, ~2.5 waves over the cap height), or pre-render the fixed titles as images. Must stay readable and fit the screen width.
Reference build: design/brand-revamp/melt-title-generator.html (canvas: Archivo extra-condensed 800, amplitude 1.7% of width, 1.8 waves over the cap height). Applied on screens: 18-screens-with-melting-titles.png.
