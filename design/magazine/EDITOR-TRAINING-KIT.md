# The Editor (in-app AI) · magazine training kit v0 · DRAFT for Megan
Megan, Nov 22, 2026, word for word: "Yes but we need to work on that part and train the AI and also what kind of designs can they do?" + "And train the AI too".
Status: draft. Nothing goes to Replit until Megan OKs the magazine logic and picks her layouts (CLAUDE.md rule 12). Assumes option A (layouts + small edits, the approved Oct 9 spec) until Megan answers.

"Training" here = what the Editor is given every time it builds a page: a rulebook, Megan's layouts, her approved examples, and an automatic check. No custom model is trained; the AI provider is only allowed to choose and fill.

## Built on (already approved, reuse, don't rewrite)
- design/magazine-ai-spec.md (APPROVED Oct 9): "AI fills, it never designs".
- design/magazine/MISE-EN-PAGE.md: type, colour, grid, rhythm, checklist.
- design/LUCKY-STAR-VOICE.md (locked voice) + Megan's context rule: "KNOWN → RETRIEVE → ASK → GENERATE", "A clarifying question is ALWAYS preferable to a fabricated personalized answer."
- design/V1-LOGIC-SPEC.md: page maker (3 steps), "Editor decides" + 4 layouts + "More layouts" (Megan, Oct 23), her words never changed.

## Part 1 · The rulebook (sent with every request)
1. You are the Editor of ISSUE11, a personal magazine. You only choose and fill. You never invent layouts, fonts, colours or images.
2. Use only the layouts in LAYOUT_LIBRARY (ids + slot sheets). Never repeat the previous page's layout.
3. Text: use her own words first (journal, action, save caption). Headlines may be shortened from her words; never invent facts, people, numbers or quotes. Every slot has a max length; stay under it.
4. Photos: only her saves/uploads. Never put text over a face. Pick the photo that fits the page's topic (no money photo on a beauty page).
5. Colour: one accent from THEME_COLOURS per page.
6. Voice: calm, editorial, "you" (never "she/her"), "action" (never "move"), never "becoming her", no outcome promises, no health/medical claims, no faith words.
7. Missing info: return a question for her ("Which photo is from the trip?") instead of guessing.
8. Output = a page plan in JSON only (layout id, photo per slot, text per slot, accent colour). The app draws it.

## Part 2 · Layout library (waiting on Megan's picks)
- Megan picks 8–12 page layouts + 2–3 covers from A–Z (Rebrand Kit canvas https://claude.ai/artifact/8zZ5hj9UH6FjFAGCFsCasC).
- For each pick, the Editor agent (🎨 DESIGN — The Editor) writes a slot sheet: id · best for (action / journal / save / cover) · photo slots (count, crop) · text slots (role + max characters) · allowed accents · a reference PNG for Replit 1:1.

## Part 3 · Examples (the "training")
- The Editor agent builds 3 sample issues (10 pages each) from realistic sample content (no real users): 1 money/career, 1 glow up/beauty, 1 love/self.
- Megan marks each page: ✅ keep · ✏️ fix (one line why) · ❌ never.
- Every ❌/✏️ becomes a rule in Part 1 or a slot limit in Part 2. The ✅ pages become "good examples" sent with requests (few-shot).
- Repeat once (round 2) with the new rules; stop when ≥ 8 of 10 pages per issue are ✅.

## Part 4 · Automatic check (before a page shows)
Layout id approved · not same as previous page · every text slot under its limit · words come from her content (quote match) · no banned words (move, becoming her, guaranteed, cure…) · accent from the theme list · no text slot over a face area. Fail → retry once → safe default layout (a simple photo + her words page).

## Part 5 · How we measure it after launch
- "Remake this page" taps and layout swaps per page (high = the Editor guessed wrong).
- Pages kept vs deleted. Megan reviews 10 random anonymised plans a week? Only with users' consent (privacy: content stays on the phone), so default = no; use the counts only.

## Questions for Megan (max 3)
1. Freedom: A. layouts + small edits (recommended, approved Oct 9) or B. also a free drag-and-drop page later?
2. Pick your 8–12 layouts + 2–3 covers on the canvas (15 min).
3. Sample issue topics: money/career, glow up/beauty, love/self (recommended), or others?
