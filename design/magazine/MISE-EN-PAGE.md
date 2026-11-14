# ISSUE11 mise en page guidelines v1 (strict)

Owner: 🖋 The Editor (agent, `.claude/agents/the-editor.md`). Set up by Megan on Nov 14, 2026, word for word: "I think we need to create « the editor » agent with Claude design and follow some strict mise en page guidelines" and "And we can use those same guidelines for magazine layouts for the app".
Scope: every ISSUE11 magazine page. That covers PDFs, lead magnets (Rebrand Kit, Vision Board Kit, Journaling Prompts; Megan: "that will help us with all the lead magnets"), wallpapers and pins with magazine pages, and the app's magazine page templates.
This file replaces the type and colour parts of `design/MAGAZINE-STYLE-GUIDE.md` (Archivo, hot-pink blocks, collage). That guide's logic still holds: a fixed template library where the AI picks and the user never moves things around.
"Must" means no exceptions without Megan's OK.

## 1. Source of the look
- Must copy the mise en page of Megan's inspo spreads closely (`design/magazine/inspo/`, Megan Nov 14: "You can legit copy the layouts of the examples I sent you and remake it for issue11"). Then swap in ISSUE11 fonts, colours, our photos and our copy.
- Must never copy their photos, text, mastheads or logos.
- Printed indie magazine, not glossy and not a Canva template. It should look like paper: grain, spine shadow, page numbers, real margins.

## 2. Format and grid
- Page: **US Letter** portrait, 8.5×11 in = 816×1056 px (1:1.294). A spread is 1632×1056. Megan, Nov 14: "Ok so everything gotta be US letter then". This is the printed issue's format (Lulu, `design/PRINT-PURCHASE.md`). Never A4.
- Print files (Lulu): add 0.125 in bleed on each side (12 px; 840×1080 per page) and keep text 0.5 in (48 px) inside the trim. Check Lulu's current spec page before the first real print file.
- App: the same US Letter proportion, scaled to the screen width. A page is a printed page, not a web card.
- Margins: top 64, bottom 56, outer 72, inner/spine 88. Full-bleed photos may ignore the margins. Text never does.
- Grid: 6 columns, 24 px gutter, 8 px baseline steps. Text runs in 1–3 columns. Body columns are 220–330 px wide.
- Spine shadow on every spread (a 100 px soft gradient centred on the fold). Paper grain on every page (feTurbulence, multiply, opacity 0.12–0.22).

## 3. Type (must: Inter Tight only, the same as issue11.app and the app)
| Role | Size (px, A4) | Weight | Tracking | Line height |
|---|---|---|---|---|
| Display / chapter word | 110–330 | 500–600 | -0.06em | 0.80–0.88 |
| Headline | 56–96 | 500 | -0.06em | 0.86–0.95 |
| Pull quote | 44–84 | 500 | -0.06em | 0.88–0.98 |
| Deck / subline | 22–30 | 500 | -0.03em | 1.1 |
| Body | 11.5–13 | 400 | 0 | 1.45–1.5, justified + hyphens in columns |
| Prompt title | 12.5–14 | 600 | -0.02em | 1.3 |
| Label / kicker / running head | 9–10 | 500 | 0.18em, UPPERCASE | 1 |
| Page number | 11 (or 40 vertical as a display element) | 500 | 0 | 1 |
- Headlines are in sentence case. Never all-caps headlines. The one exception is giant single letters (layout K).
- No serif, no Archivo, no mono and no script fonts. No emoji in layouts.
- Max 3 sizes per page, plus labels.

## 4. Colour (must: flat Electric Soft, no ombré, no gradients)
- Paper: White #FFFFFF or Paper #F6F3EE. Ink: #0D0D0D.
- Flat accents: Lilac #D9B3FF · Ice #EAF6FF · Peach #FF9A7A · Mint #7DE3C7 · Rose #E84C7A.
- Pink #C2207E only for small text (numbers, sublines, scattered words). Never flat hot pink (#FF4DB8) as a background (Megan is "allergic").
- Max 1 accent colour per page and 2 per spread.
- Contrast: body text 4.5:1 minimum. White text only on dark photo areas.

## 5. Images (Megan: "use a lot of aspirational images", "And lots of images", "no collage-like pictures")
- Every spread has photos: at least 1, and 2–6 is the norm. Text-only spreads are allowed only for layout K, and K still carries one photo.
- Photos are placed cleanly: full-bleed, framed (1.5 px white inset frame), equal grids (contact sheet), or stacks. Never overlapping, torn, cut-out, stickered or rotated collage.
- One treatment for all photos: contrast 1.04, saturation 0.9. Aspirational and on-brand: closets, cars, money, friends, glow, travel, faces.
- Never put text on a face. Text over a photo only sits on a calm area, with a soft shadow.
- Star cut-outs (layout J) are the only shaped photo crop allowed.
- Photo sources: Megan's library and uploaded assets only. Never stock that looks fake, and never a fake app screenshot.

## 6. Page furniture (every page)
- Running head: section on the left, issue title on the right, as a label.
- A page number on every page. On full-bleed pages it is white.
- An `issue11.app` mark at least once per spread.
- Vertical running text is welcome as a detail (repeated chapter word, credits).

## 7. Layout library (copied from the inspo; Megan picks the final set)
Candidates live in the Rebrand Kit canvas (https://claude.ai/artifact/8zZ5hj9UH6FjFAGCFsCasC). Until Megan picks, treat them all as candidates. Once she picks, the rest are dropped.
| ID | Layout | Inspo | Best for |
|---|---|---|---|
| A | Framed: coloured page, photo in a thin white frame, vertical text | board-01 (pink frame) | Chapter opener |
| B | Scattered type: letters spread over a white page, facing a full-bleed photo | board-04 ("t r u bl e") | Chapter opener |
| C | Contact sheet: 6-photo grid with captions, facing a text page | board-04 (photo grid) | Moodboard, vision board |
| D | Big word: huge word at the bottom, offset small photo, facing stacked photos | board-04 ("klima") | Chapter opener |
| E | Colour block: colour band with a giant number over a photo, side strip | — | Section start |
| F | Headline over photo + repeated vertical word + colour bar | editorial-01 ("Love that if it were…") | Feature, prompts |
| G | Scattered coloured words on a colour page, small photo | editorial-01 ("It's a dirty job") | Prompts, essay |
| H | Quote page facing a full-bleed photo | editorial-01 (Kyoto), editorial-05 | Pull quote, interlude |
| I | Giant vertical word + app-style windows on a photo | editorial-05 ("Renderizarme") | App CTA, prompts |
| J | Star cut-outs: colour page with star windows, photo with colour stars | editorial-12 ("trust the process") | Beauty, glow up |
| K | Giant letters over dense text columns | editorial-20 ("WASHINGTON") | Long read |

## 8. Rhythm (a whole issue)
- Never put the same layout on two spreads in a row.
- Alternate dense and airy spreads.
- Every 3–4 spreads, add a breather: a full-bleed photo or a quote (H, or an interlude page).
- Cover → Editor's letter → How to use → chapters → closing ritual (letter, cover, challenge) → back cover with the CTA.

## 9. Copy (from `design/editorial/` and lessons)
- Use the customer lexicon and her own words for pull quotes ("Get my dream bod", "I'm in my building era", "I keep my circle small").
- "Become YOU", "future you", "your true self". Never "become her". "Become your own dream girl" is ours. Never use "dream girl" alone.
- No promised outcomes or dates. No faith words. No "it's not X, it's Y". No filler or lorem ipsum: missing facts become [PLACEHOLDER].
- One CTA per spread at most, and it's always soft ("Make your own issue", "Want your answers turned into a magazine about YOU?").

## 10. Process (Claude Design)
1. Before working, read this file, `.pipeline/lessons.md` and the inspo folder.
2. Build in Claude Design (Design artifact, `.dc.html` artboards). Pages are US Letter (816×1056) or spreads (1632×1056), with the fonts and colours above.
3. New direction? Show 3–6 sample spreads first and let Megan pick. Then build the whole piece in the picked layouts.
4. Never verify, render or screenshot unless Megan asks. Before republishing, read any file she may have edited.
5. Copy the canvas source into the repo next to the piece and commit after every change.
6. Megan approves before anything goes live (Framer, Pinterest, the app).

## 11. The Editor's checklist (every page, before handing over)
1. Inter Tight only. Sizes come from the table in section 3.
2. Flat colours only, max 1 accent per page. No ombré and no hot pink background.
3. At least 1 photo per spread, cleanly placed, with no collage.
4. Margins and the grid are respected, and text never touches the edge.
5. Running head, page number and the issue11.app mark are present.
6. The layout is one of the picked library IDs, and it's not the same as the previous spread.
7. Copy follows the lexicon rules, with no promised outcomes.
8. No text on faces. Body text contrast is at least 4.5:1.
9. Paper grain and spine shadow are on.
10. The source is saved in the repo, and the pages are logged.

## 12. For the app (the same rules, more steps)
- These layouts become the app's magazine template library. The Editor (the app's AI layer) picks the template, her images and one accent colour. "Another look" means another template. She never drags things around.
- The app's magazine pages are not final (`design/V1-SIMPLIFIED.md`). Before anything goes to Replit, CLAUDE.md rule 12 applies: logic per tab first, Megan's OK, then screens, then ONE consolidated Replit update. Nothing has been sent to Replit for this yet.
