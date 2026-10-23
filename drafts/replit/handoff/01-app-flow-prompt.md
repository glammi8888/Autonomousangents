# ISSUE11 · Replit update prompt (Oct 15, 2026)
Paste everything inside the box into Replit, together with the other files in this folder.

```
You already built a first version of ISSUE11. I've worked with a UI/UX designer and the flow changed. Please UPDATE the app to match the files I'm uploading, everything AFTER onboarding:
- screens/ = 50 PNG images, one per approved screen, numbered in build order. THESE ARE THE DESIGNS: copy the layouts, the order of things and the look exactly. Screens 49-50 (widgets) are for AFTER launch: don't build them now.
- 02-screens-mockup.html = the same screens, live (animations, scrolling). It also shows some design options we did NOT choose: if anything differs, the screens/ images win.
- 03-app-copy.md = all the words in the app. Put them in ONE strings file.
- 04-print-purchase.md = the print order rules.
- 05-design-tokens.md = colors, fonts, sizes. 06-lucky-star/ = my the Editor screens (copy their look).
Keep everything that already matches. Change what doesn't. Do NOT change onboarding (screens before the paywall) or the design system from step 1.
Sample content only for now: no real payments, sign-in, AI or API keys yet.

WHAT ISSUE11 IS
A process-focused manifestation app. She builds her dream life into her own magazine (her "Issue") and takes one small step a week. The magazine is the hero.

FEEL
It must feel instantly familiar: use the gestures people know from TikTok, Instagram, Pinterest and ChatGPT (listed per screen below). Borrow ONLY the gestures, never their look. No likes, followers, comments or public posts. Explore (Images and Sessions) is ENDLESS like Pinterest (Megan, Oct 23); Home still ends with "That's today."

NAVIGATION
Bottom tabs: Home · Explore · Issue · Journal · You. Issue sits in the centre (like TikTok's "+").
A floating "11" sticker button (The Editor) on every screen. It starts bottom right, above the tabs, and she can DRAG it anywhere (like the iPhone AssistiveTouch button): when she lets go it snaps to the nearest left or right edge, never covers the tab bar, and the app remembers where she put it. Tap = opens the Editor. Press and hold WITHOUT moving = voice. Press and move = drag. It is never hidden.

FIRST OPEN (right after the paywall and sign in, once)
- Full red screen (#D40806) with the big cream 11 sticker in the middle and "Peel to open your Issue ↗".
- She drags the corner (or taps): the red layer peels away like a sticker and her cover is underneath.
- Her cover settles, the cover lines appear one by one, the small 11 sticker pops onto the corner, a pink glow blooms.
- "Your Issue has started. 8 of 40 pages · 32 to go" + pink glass button "Open my Issue" -> Home. Soft haptic on the peel.

HOME (one long scrollable page, calm, LOTS of white space · see design/brand-revamp/13-home-calmer.png)
- Top bar: the wavy ISSUE11 logo (left), small mono "VOL. 01 · [date]" and the 11 mark (right).
- Poster: big centered title in Archivo Condensed caps "THE [NAME] (ISSUE) 14–40", then small "open my issue · 26 to print" (baby pink tag), then a numbered strip (01–04) of her Issue shown as real magazine photos. Tap -> Issue tab.
- 01 · This week's move (hairline rule + mono label + "week 06"): her move in bold Inter Tight, black button "I made room for it" -> Add Proof -> "It's real", outline button "Not yet". If no move yet: "Pick this week's move".
- 02 · Tonight: one session row (image, name, "resume · 6 min left"), black play square.
- Ends with "THAT'S TODAY." + "see you tomorrow" (no endless feed).
- NOT on Home anymore (Megan, Oct 21): story bubbles, flashback card, saves strip, latest pages. Flashbacks can come from the Editor (the 11).

HOW PAGES ARE MADE (important logic)
- Saves are her VIBE, not pages. Saving (hearting) an image or session never adds a page by itself. There is NO save counter anywhere ("4 more saves = 1 new page" is removed everywhere).
- The Editor is the designer: whenever a page is made, it picks the images from HER saves and HER own photos (matching her vibe) and lays the page out in one of my layouts. She can tap "↻ Another look" to try other images/layouts. Her words are NEVER changed.
- Pages come from what she DOES, WRITES or CHOOSES. An image alone can be a full-bleed page (Megan, Oct 23): "Add to my issue" on an image in Explore opens the page preview: the image full-bleed, plus an optional "+ Add your words" line on the same screen, then "Keep page". She chooses image alone OR image + words (Megan, Oct 23: "she should have the option to do both"). Hearting is still only a save. Pages come from 5 places (5 = "Add to my issue" on an image):
  1. Her weekly move + proof ("I made room for it" -> Add proof -> "It's real" = 1 page).
  2. Journal: "Keep page" = 1 page.
  3. Make a page (she builds it herself, below).
  4. Her cover and the first 8 starter pages (from onboarding).
- MAKE A PAGE (screens/51-make-a-page-flow.png): a pink "+ Make a page" button at the top of My saves (next to "+ Add your photo") and on any empty page in the Issue's 40-page grid.
  Step 1 "Pick 1 to 3 images." from My saves or My photos (numbers show her order) -> "Next".
  Step 2 "Now, one line." She must write one line ("What does it mean to you? Or a moment you lived."). OPTIONAL (Megan, Oct 23: "An Image alone can definitely be a full bleed page"): if she skips it, the Editor makes a full-bleed image page with no text, and she can add words later with "Edit my words". Small note: "Your words stay exactly as you write them." -> "Make my page".
  Step 3 the Editor shows the designed page ("★ The Editor designed p.[29]") with "↻ Another look" and "Keep page". Keep page = added to her Issue (+1 of 40). Closing without keeping = nothing is added.
- The floating 11 stays on every step.
- NOTE: screens 17, 17b, 01 (Home) and 30 still show the old "4 more saves = 1 new page" tile/line. Ignore that part: this logic and screens/51-make-a-page-flow.png win.

MAGAZINE PAGES = TEMPLATES (important logic, not an editor)
- Every Issue page is built from a fixed library of PAGE TEMPLATES (indie fashion/beauty magazine look: collage grids, giant cropped type, pink duotone, color blocks, spreads). The final templates come later; for now build 6 simple placeholder templates as data (JSON: image slots + text slot + color), e.g. 1) full photo + small caption, 2) 3x3 photo grid, 3) giant word + 1 photo, 4) pink duotone photo + quote, 5) color block (pink/red/yellow/black) + big quote, 6) cover.
- The Editor only CHOOSES: which template, which of her images go in the slots, and the color treatment. Her words go in the text slot unchanged.
- PICK A LAYOUT (Megan, Oct 23: "We can give her a layout option she wants. Select from it, and that would be what the editor does for her"): under the page preview, a strip of 4 layouts the Editor made from her image(s) and words (e.g. Full photo · Photo + words · Big word · Pink). She taps one; the preview updates. This replaces "↻ Another look" everywhere (Make a page, Journal, Edit). Same images + words, another template. She never drags, resizes or styles anything. No Canva-style tools.
- Edit a page = only 3 things: "↻ Another look" · "Swap a photo" (pick from her saves/photos) · "Edit my words". (Replaces the old Photo / Text / Layout / Mood / Words on-off tools.)
- Pages render as real printed pages: page proportion (US Letter 8.5x11), white paper edge, page number. Turning the phone sideways shows two-page spreads.
- Templates must be easy to add later without code changes (new JSON file = new template).
- See screens/52-magazine-templates-logic.png for the logic and the 6 placeholder templates (placeholders only; final templates come later).

EXPLORE (like Instagram Explore + Pinterest)
- Search bar on top: "Search sessions and images".
- One row of chips: For you · Sessions · My saves · then topics (Money, Love, ...).
- "Sessions" chip = organized like Spotify: one big "Picked for you tonight" card on top, then horizontal shelves by type (Visualizations, Affirmations, Meditations, Breath), each with "See all"; extra chips "5 min" and "10 min" filter by length.
- "See all" on a row opens that type's page (screens/16b): "‹ Sessions" back link, big title (e.g. "Visualizations"), one grey line "[count] sessions · [short description]", chips All · 5 min · 10 min · 15 min, then a 2-column grid of the same tiles (image, round pink play, name, length). Tap a tile = session page. No sort menus, no play counts.
- "For you" chip = one Pinterest-style grid that mixes images and sessions. Sessions show a round pink play button on the top-left of the image, plus their name and length at the bottom. Images show a heart (tap or double-tap to save).
- "My saves" chip (her vision board): one grey line on top, "Your saves set the vibe of your Issue. The Editor designs your pages with them." Then a row with a pink "+ Make a page" button and a dashed "+ Add your photo" button. Then her own photos, hearted images and saved sessions. "+ Add your photo" opens the iPhone photo picker (only the photos she picks). No pink counter tile.
- Bottom of "My saves" (screens/17b): after her last saves, a clean ending, left-aligned: big "That's everything you've saved.", a pink glass button "+ Make a page" and a glass button "Find more in For you ›" (switches to the For you chip). Nothing else below it: no old content, no disclaimers, no storage notes.
- Tap a session -> Session page like a Spotify album page (big image, title, length, "Picked for you", big pink play, "What you'll rehearse", "Up next") -> full-screen Player like Spotify Now Playing (video, live words like lyrics, scrubber, back/forward 15 s, save; a small "Voice · Music" slider under the words (each session has 2 audio files of the same length, voice-only and music-only, played together; the slider changes the balance, remembered per user); swipe down = keeps playing in a glass mini player above the tabs; audio keeps playing with the phone locked). Every session has its own video, animation or image (no audio-only mode, no Watch/Listen switch).
- When a session ends: no new screen. The video dims, the last line stays, and a small glass card rises: "Keep a line from this? · What did you see yourself do?" with "Write it" (opens Journal with that prompt) and "Not now". It fades away by itself after a few seconds.

ISSUE
- Her magazine reads like a real magazine: swipe left/right (or tap the edges) to turn pages, NO timer, no progress bars; top shows "p.15 / 40". Swipe down to close. Shows "14 of 40 pages · 26 to print". Every Issue has exactly 40 pages to print; it starts with 8 and fills up as she adds proof, photos and journal lines. At 40: "Ready to print".
- Bottom row: a glass pill "25 pages to print ›" (tap = shows how to fill the next page and jumps there; at 40 it becomes "Ready to print"), a pink "Edit" button (opens the edit sheet: ↻ Another look · Swap a photo · Edit my words), and a round Share button. The floating 11 stays on this screen too.
- Share button: share the current page as an image (iOS share sheet).
- Tap Edit -> edit sheet: "↻ Another look" (another template), "Swap a photo", "Edit my words". Nothing else.
- Issue 02 starts after she orders the print: Issue 01 moves to a shelf of past Issues and Issue 02 begins with 8 fresh pages and a new cover reveal.
- At 40 of 40 pages: "Ready to print" screen with a grid of all 40 pages and the button "I love it · Approve my Issue".
- Only after she approves: "Order my print" screen (cover preview, copies, shipping address, price "$29.99" per Issue, three shipping options "Standard · 11–14 business days · Free" (selected), "Expedited · 6–9 business days · + $16", "Express · 5–8 business days · + $32", a Total line "$29.99 + tax", and a small note "Printing takes 3–5 business days before shipping. Estimates, not guaranteed. Hawaii, Alaska and Puerto Rico take longer." Rules: purchase happens inside the app (not a web page), US addresses only; if the address is a PO box or APO/FPO, show only "Standard" and "Priority Mail · 9–12 business days · + $10". see 04-print-purchase.md; Apple Pay button "Place my order"). No real payment yet.

JOURNAL = "the studio" (see design/brand-revamp/20-journal-loop-simplified.png)
1. Studio open: dark full photo, small "Wed 22 Oct · Day 33", big "Your studio is open.", today's prompt, white button "Start today's page", small link "your wall".
2. Write: a sketchbook spread (her photo left, her words right in italic, appearing live). "+ tape in a photo" right on the page (her saves / photos). Text bar "Keep writing...". Black button "Keep page". Small: "Private until you keep it."
3. The Editor designs: the page laid out from a template, her words unchanged ("Your words, unchanged. The Editor picked the layout."). Buttons "↻ Another look" / "Keep page".
4. In print: the page shown slightly tilted on the grey background, "That's in print.", "15 of 40 pages. Future you is getting closer.", button "Back to the studio".
5. Your wall (Megan LOVES this: "It's really giving creative studio"): a dotted pinboard of her pinned ideas, lines and images (white cards, slight tilts, one baby-pink note). Title "Your wall." + "Ideas, lines and images you pinned. Tap one to make it a page." Button "Pin an idea +". Tap a pin -> Make a page with it.
   RULES: NO columns, NO statuses (no Ideas / Moving / Printed), no due dates, no checkboxes. It must never look like a task board. Pins are inspiration, not tasks.
- No sub-tabs inside Journal. The weekly move stays ONE move on Home.

YOU
- Top: her photo, her name, "The Freedom Issue · 14 of 40 pages".
- A horizontal row of her proof tiles ("It's real" moments), "See all" opens the full grid.
- Below, a big settings list in huge uppercase type, one row each with an arrow: notifications (on/off + time), app icon & widgets (one screen: pick the app icon; the widget style cards stay HIDDEN until widgets are built after launch, because Apple rejects unfinished features), my issues (opens My shelf), membership (manage subscription, restore purchases), "The Editor & AI" on/off switch, help & support (short FAQ + contact email, also used as Apple's support URL), privacy policy, terms, sign out, delete account (with a confirm screen).

MORE SCREENS (inside You and around the app)
- App icon & widgets: my 6 icons in a 3x2 grid (Classic, Eleven, Swirl red, Pink eleven, Swirl noir, Green), button "Save my look". (The 2 widget style cards, Stickers and Dreamy glass, are designed in the mockup but stay hidden until widgets exist.)
- Notifications: one switch per reminder with its time (This week's move · Monday 9:00, Journal prompt · daily, optional, New page in your Issue, the Editor max once a day, Quiet hours 22:00-7:00) + a preview of the notification.
- Membership: black card "ISSUE11 Monthly · $9.99 / month · renews [date]", what's included, rows "Manage or cancel" (opens App Store subscriptions), "Restore purchases", "My print orders". One line: "Printed Issues are ordered separately ($29.99). Your Issues stay yours to read, even if you cancel."
- The Editor & AI: on/off switch, plain-words explanation of what it reads, "What the Editor remembers", "Clear the Editor's memory", "How your data is used". App works with it off.
- Order status: her cover, steps Order placed -> Printing (3-5 business days) -> Shipped (tracking link) -> On its way, estimates note, "Need help with my order".
- Safety: if she writes crisis words, the Editor stops and shows a full red (#D40806) screen with white text and white cards "You don't have to carry this alone." with "Call or text 988" (US) and "Call 911", plus help outside the US. No AI suggestions on this screen.
- My shelf (You → header → "My Issues"): BLACK background with a soft pink glow. Her Issues glide sideways like album covers (current one big and centered with a reflection, neighbours smaller and angled). A pink "Printed" sticker on finished Issues; the one in progress shows "12 of 40". Under it: dates, pages, moves kept, and page dots. Tap a cover to reread it. Below: a dark glass "Then → now" card with her first proof (date + her words) next to her latest proof.
- First-day states: each tab has one. Issue: "8 of 40 · 32 to print" and a grid of all 40 pages (8 filled with her pages, 32 dashed and labeled with what fills them, page 9 outlined in pink) + pink glass button "Fill page 9 · your first move".

THE 11 (The Editor)
Tapping it on Home opens a full-screen sheet; inside other tabs it rises as a half sheet (pink glow on its top edge) so she still sees the screen it helps with. While the Editor thinks, the pink glow slowly breathes and one small line says what it is reading ("Reading your Journal..."), no spinners. Under each answer, small pink tags show what it used ("Journal · Oct 12", "Career board"). The floating 11 gets a small pink dot when it has something for her (max once a day, no numbers); holding the 11 anywhere starts voice right away. The sheet (copy the look from my the Editor screenshots): a soft pink glow behind the 11 sticker, ONE big card in the middle with 1-2 pill buttons, a close X top right, and at the bottom a "Talk to the Editor..." bar with a send arrow and a big pink hold-to-talk mic. Under it: "The Editor is AI and can make mistakes".
What the card offers depends on the screen:
- Home: one next thing (start tonight's session / keep my move / add proof)
- My saves: "It's missing a feeling" + 3 images -> ADD ALL 3 / SWAP ONE
- Sessions: one of the pre-made sessions picked for her and why ("Picked for you"). It never makes new sessions.
- Journal: one gentle question
- Issue: another version of this page
Buttons inside the Editor are liquid glass (frosted, see-through white over the pink glow); the main action is pink-tinted glass. Every action ends in something real, then a black toast at the top: "Added to ... · UNDO". Nothing changes without her tap.
If "The Editor & AI" is off, the sheet says "The Editor is off. You can turn it on in You." and the rest of the app still works.
Use placeholder results for now.

IRRESISTIBLE (all approved)
1. Monthly recap: at the end of each month, a 5-card story "Your [month] in ISSUE11", bold Wrapped style: full pink (#F65AAD) background, one giant red (#D40806) number (e.g. "4"), the cream 11 sticker tilted, a big headline ("moves you made room for.") and one short line listing them. Cards: moves she kept, her proof, most-saved image, the line she wrote that came true. Buttons: white "Share my month" + "Next".
2. Collectible stickers: at 10, 20, 30 and 40 pages she unlocks a sticker (zebra, red 11, cheetah 11, ...) for her cover or pages. Unlock screen with the pink glow; locked slots show the page number.
3. Final stretch: from page 35, her cover on Home glows pink with a tag "5 pages to print" (counts down) and "Your next page: ... · Fill it".
4. Arrival: when the print is delivered, the Editor asks "Is it in your hands? Take a photo with your Issue." The photo becomes page 1 of Issue 02.
5. Sound + touch: soft page-turn sound, sticker-peel sound (reveal + unlocks), light haptic when a page is added, a deep one at 40. Sounds follow the silent switch.
6. Share in our look: any page or her cover shares to Instagram Stories / TikTok / Messages, framed in blush with the wavy ISSUE11 masthead and "made in ISSUE11".

UX RULES (apply everywhere)
- Never lose her words: the Journal autosaves while typing, works offline, syncs later.
- Notifications open the exact screen they talk about.
- Same gestures everywhere: swipe down closes anything full-screen; swipe from the left edge goes back.
- Main actions in the bottom half of the screen (thumb reach).
- Ask permissions only at the moment they're needed (photos when she taps "+ Add your photo", mic when she holds the 11).
- First week: max 3 tiny one-time tips, never a tour.
- Contrast (WCAG AA): brand pink #F65AAD only for big text, fills, glows and dots. Small pink text uses #C2207E. Grey captions use #6B6762 (never #8A8A8A or lighter). Labels on pink buttons are ink #0D0D0D. Follow the iPhone text-size setting; no label under 11pt.
- Tab bar: labels 11pt; the current tab is ink + bold + the small pink dot, others grey #6B6762; every tab is at least 44x44pt.
- The floating 11 stays on every screen (never hide it).
- Every icon button has a VoiceOver name (the 11 = "The Editor").
- Preload the next story/page; soft placeholders instead of spinners.

STATES
Every tab needs an empty state. Also: a loading state ("The Editor is building"), an offline message ("You're offline. Your Issue is saved.") and a friendly error.

RULES
- Keep our design system exactly. Flat, printed-magazine feel.
- "Weeks showing up" streak (Megan, Oct 23: "Yes streaks"): a week counts if she does her move, the smaller move, or keeps any page. It never resets and there are no loss messages. No to-do lists, no stats, no goal trackers.
- UNLOCKS (Megan, Oct 23): every 5 pages (10, 15 ... 40) unlocks one layout, cover style or sticker, announced in one line on the page-lands moment ("Unlocked: Pink layout."). Locked layouts show at the end of the Pick a layout strip with a lock and "at p.20". Page 40 unlocks a special cover.
- Warm, simple copy. Never promise outcomes.
- Put all wording (prompts, move suggestions, card lines) in ONE strings file so it can change without code.
- Layouts must stretch to any screen size (no fixed widths).

Work in this order: 1) navigation, the 5 tabs and the floating 11; 2) Home; 3) Explore + player; 4) Issue + print order; 5) Journal; 6) You + settings; 7) the Editor; 8) first-day/empty states. After each step, stop so I can check it on my phone.
```
