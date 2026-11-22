# Magazine templates + Editor training · the logic behind it · DRAFT for Megan
Megan, Nov 22, 2026, word for word: "I will just send examples of magazine layouts and those will become "templates" available in the app" · "And also the editor's training (different templates)" · "We need to build the logic behind all of it".
Status: logic only (CLAUDE.md rule 12). Megan OKs this → templates get made → ONE Replit update. Builds on design/magazine-ai-spec.md (APPROVED Oct 9: "AI fills, it never designs"), design/magazine/MISE-EN-PAGE.md and design/magazine/EDITOR-TRAINING-KIT.md.

## A. How an example becomes a template (behind the scenes)
1. **Megan sends an example**: a photo, screenshot or PDF of a magazine page or spread she loves (chat or the shared Drive folder).
2. **The Editor agent (🎨 DESIGN — The Editor) remakes it in ISSUE11 style**: same structure and feel, our type (Inter Tight), our colours, sample photos only. Never another magazine's photos, text or logo ("Inspiration, not copying").
3. **Slot sheet**: id · name · best for (action / journal / save / opener / cover) · photo slots (how many, crop) · text slots (headline / quote / caption / body + max characters) · allowed accent colours · phone + print (US Letter) versions.
4. **Megan approves** ✅ (or ✏️ fix / ❌ drop). Only ✅ templates enter the library.
5. **Tags** so the Editor can match: number of photos (1 · 2–4 · 5+), words (few · medium · lots), mood (calm · bold · playful), use (page · opener · breather · cover).
6. **Batch to Replit**: approved templates go in ONE update at a time (not one by one), with a reference image each so it's built 1:1.

## B. What she sees and does in the app
**New page (Issue tab):** content (from an action, journal entry, save or upload) → **Layout** step → Keep.
- Layout step: **"Editor decides"** (default) · **4 suggested templates** that fit her content · **"More layouts"** (filters: 1 photo · a few photos · many photos · words first). (Megan, Oct 23.)

**Edit a page:** swap template (her photos and words move over; if the new one has fewer photo slots, the extra photos wait in a "not used" tray) · page colour (theme list) · edit her words · stickers / patterns · undo · "Remake this page".

**Cover:** a cover template per issue (her name, issue number, cover lines from her own words, her best photo). She can swap the cover template.

**The whole issue:** the Editor keeps the rhythm (never the same template twice in a row, a breather page every 3–4 pages, opener at the start of a new topic).

**Download / print:** every template has a print version, so the PDF and the printed issue look the same as the app.

## C. How the Editor picks a template (matching rules)
1. Content type: action → "proof" templates · journal → words-first · save → photo-first · first page of a topic → opener.
2. Fits: number of photos and length of text must fit the slots (no tiny text crammed in, no empty photo slots).
3. Mood: matches the photo and topic (no money photo on a beauty page).
4. Variety: not the same as the last page; spread templates across the issue.
5. Best match = "Editor decides"; the next 4 = suggestions.

## D. Training the Editor (different templates)
- Per template: a slot sheet + 1–2 ✅ example pages (few-shot) + "never do" notes from Megan's ✏️/❌.
- 3 sample issues (money/career, glow up/beauty, love/self), 10 pages each, using the approved templates → Megan grades every page → fixes become rules → round 2 → done at ≥ 8/10 ✅.
- Automatic check before a page shows: approved template id, text fits, words come from her content, no banned words, accent from the theme list, no text on a face. Fail → retry once → safe default page.
- Each new batch of templates gets 1 round of sample pages before it goes live.

## E. Underneath (data, stays on the phone)
- Template = id, name, tags, slots, version, phone + print layout. Shipped inside the app; new templates arrive with app updates.
- Page = template id + version + her content (photos, words, colour, stickers). Updating a template never breaks old pages (they keep their version).
- AI only with consent (CP5). Without consent or offline: "Editor decides" uses the matching rules in C (no AI), so it still works.

## F. Launch scope (Dec 4 submission)
- v1: the templates Megan approves by ~Nov 28 (aim 8–12 pages + 2–3 covers). More templates in updates after launch.

## Questions for Megan (max 3)
1. Freedom: A. templates + small edits (recommended) or B. also a free drag-and-drop page later?
2. Reorder pages in the issue overview (hold and move a page)? Recommended: yes (it doesn't change any design).
3. Where to send examples: one shared Google Drive folder "ISSUE11 templates" (recommended, easy from the phone) or chat?
