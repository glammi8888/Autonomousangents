# ISSUE11 · Replit update prompt (Oct 15, 2026)
Paste everything inside the box into Replit, together with the other files in this folder.

```
You already built a first version of ISSUE11. I've worked with a UI/UX designer and the flow changed. Please UPDATE the app to match the files I'm uploading, everything AFTER onboarding:
- 02-screens-mockup.html = the approved design for every screen (open it and copy the layouts, the order of things and the look exactly).
- 03-app-copy.md = all the words in the app. Put them in ONE strings file.
- 04-print-purchase.md = the print order rules.
- 05-design-tokens.md = colors, fonts, sizes. 06-lucky-star/ = my Lucky Star screens (copy their look).
Keep everything that already matches. Change what doesn't. Do NOT change onboarding (screens before the paywall) or the design system from step 1.
Sample content only for now: no real payments, sign-in, AI or API keys yet.

WHAT ISSUE11 IS
A process-focused manifestation app. She builds her dream life into her own magazine (her "Issue") and takes one small step a week. The magazine is the hero.

FEEL
It must feel instantly familiar: use the gestures people know from TikTok, Instagram, Pinterest and ChatGPT (listed per screen below). Borrow ONLY the gestures, never their look. No likes, followers, counts, comments, public posts or endless feeds.

NAVIGATION
Bottom tabs: Home · Explore · Issue · Journal · You. Issue sits in the centre (like TikTok's "+").
A floating round "11" sticker button on every screen (bottom right, above the tabs).

FIRST OPEN (right after the paywall and sign in, once)
- Full red screen (#D40806) with the big cream 11 sticker in the middle and "Peel to open your Issue ↗".
- She drags the corner (or taps): the red layer peels away like a sticker and her cover is underneath.
- Her cover settles, the cover lines appear one by one, the small 11 sticker pops onto the corner, a pink glow blooms.
- "Your Issue has started. 8 of 40 pages · 32 to go" + pink glass button "Open my Issue" -> Home. Soft haptic on the peel.

HOME (one long scrollable page, like my V4 Home)
- Top: the big wavy ISSUE11 masthead (about 75% of the screen width, centered) + a thin rule "VOL. 01 · [date]". When she scrolls down, it shrinks into a small sticky header (small masthead + "14 of 40 · Vol. 01"), like Apple Music large titles.
- Story bubbles (like Instagram): only what's new today: Today + New page. Pink ring = new. Tap = full-screen story cards. (Your move and Flashback live once, as cards below. Nothing appears twice on Home.)
- Her big Issue cover with a glass "Your issue" pill and a 40-tick progress bar "14 of 40 pages · 26 to print". Tap -> Issue tab.
- "Your move this week" black card with the pink glass button "I made room for it" -> Add Proof (one line, optional photo -> "Share to my Issue") -> "It's real".
- Resume capsule: "Resume: [session] · 6 min left" with pink play.
- Lucky Star flashback card (pink): one of her own Journal lines from months ago, "Does it feel truer now?" -> "Add proof" / "Not yet".
- "From your World" strip of her images + "4 more saves = 1 new page".
- "Latest pages" strip of her newest Issue pages -> "Open Issue".
- Ends with "That's today. See you tomorrow." (no endless feed).
- If the week has no move yet, the move card says "Pick this week's move" (her last move, 3 suggestions, "Write my own").

EXPLORE (like Instagram Explore + Pinterest)
- Search bar on top: "Search sessions and images".
- One row of chips: For you · Sessions · My World · then topics (Money, Love, ...).
- "Sessions" chip = organized like Spotify: one big "Picked for you tonight" card on top, then horizontal shelves by type (Visualizations, Affirmations, Meditations, Breath), each with "See all"; extra chips "5 min" and "10 min" filter by length.
- "For you" chip = one Pinterest-style grid that mixes images and sessions. Sessions show a round pink play button on the top-left of the image, plus their name and length at the bottom. Images show a heart (tap or double-tap to save).
- "My World" chip (her vision board): one grey line on top, "Your vision board. Everything here can become a page in your Issue." Then her own photos, hearted images and saved sessions. First tile: "+ Add your photo" (iPhone photo picker, only the photos she picks). A pink tile: "4 more saves = 1 new page".
- Tap a session -> Session page like a Spotify album page (big image, title, length, "Picked for you", big pink play, "What you'll rehearse", "Up next") -> full-screen Player like Spotify Now Playing (video, live words like lyrics, scrubber, back/forward 15 s, save; a small "Voice · Music" slider under the words (each session has 2 audio files of the same length, voice-only and music-only, played together; the slider changes the balance, remembered per user); swipe down = keeps playing in a glass mini player above the tabs; audio keeps playing with the phone locked). Every session has its own video, animation or image (no audio-only mode, no Watch/Listen switch).
- When a session ends: no new screen. The video dims, the last line stays, and a small glass card rises: "Keep a line from this? · What did you see yourself do?" with "Write it" (opens Journal with that prompt) and "Not now". It fades away by itself after a few seconds.

ISSUE
- Her magazine reads like a real magazine: swipe left/right (or tap the edges) to turn pages, NO timer, no progress bars; top shows "p.15 / 40". Swipe down to close. Shows "14 of 40 pages · 26 to print". Every Issue has exactly 40 pages to print; it starts with 8 and fills up as she adds proof, photos and journal lines. At 40: "Ready to print".
- Bottom row: a glass pill "25 pages to print ›" (tap = shows how to fill the next page and jumps there; at 40 it becomes "Ready to print"), a pink "Edit" button (opens the edit sheet: Cover · Mood · Words on/off · Photo · Layout · Update my Issue), and a round Share button. The floating 11 stays on this screen too.
- Share button: share the current page as an image (iOS share sheet).
- Tap a page -> edit sheet: swap photo, edit text, pick another layout (only from my layouts), "Try another version".
- Issue 02 starts after she orders the print: Issue 01 moves to a shelf of past Issues and Issue 02 begins with 8 fresh pages and a new cover reveal.
- At 40 of 40 pages: "Ready to print" screen with a grid of all 40 pages and the button "I love it · Approve my Issue".
- Only after she approves: "Order my print" screen (cover preview, copies, shipping address, price "$29.99" per Issue, three shipping options "Standard · 11–14 business days · Free" (selected), "Expedited · 6–9 business days · + $16", "Express · 5–8 business days · + $32", a Total line "$29.99 + tax", and a small note "Printing takes 3–5 business days before shipping. Estimates, not guaranteed. Hawaii, Alaska and Puerto Rico take longer." Rules: purchase happens inside the app (not a web page), US addresses only; if the address is a PO box or APO/FPO, show only "Standard" and "Priority Mail · 9–12 business days · + $10". see 04-print-purchase.md; Apple Pay button "Place my order"). No real payment yet.

JOURNAL (her words go straight onto a magazine page)
- Top line: "Journal" and, in pink, "You're writing page 28 of 40".
- A real magazine page (blush background, one of her images on the right): small label "In her words · p.28", and her words appear LIVE as a big uppercase pull quote while she types. Today's prompt sits small at the bottom of the page. Swipe the page sideways for another prompt.
- Under the page, small: "★ Lucky Star lays out your page" and a pink "↻ Another look" (tries another of my layouts and images). Lucky Star chooses the layout and image; her words are never changed.
- Below that: a text bar "Keep writing..." (the iPhone keyboard mic handles voice) and a pink glass button "Keep page". Keep page = it goes into her Issue. If she doesn't keep it, the entry stays private in her Journal.
- Past entries: a list under the page (scroll down).

YOU
- Top: her photo, her name, "The Freedom Issue · 14 of 40 pages".
- A horizontal row of her proof tiles ("It's real" moments), "See all" opens the full grid.
- Below, a big settings list in huge uppercase type, one row each with an arrow: notifications (on/off + time), app icon & widgets (one screen: pick the app icon; the widget style cards stay HIDDEN until widgets are built after launch, because Apple rejects unfinished features), my issues (opens My shelf), membership (manage subscription, restore purchases), "Lucky Star & AI" on/off switch, help & support (short FAQ + contact email, also used as Apple's support URL), privacy policy, terms, sign out, delete account (with a confirm screen).

MORE SCREENS (inside You and around the app)
- App icon & widgets: my 6 icons in a 3x2 grid (Classic, Eleven, Swirl red, Pink eleven, Swirl noir, Green), button "Save my look". (The 2 widget style cards, Stickers and Dreamy glass, are designed in the mockup but stay hidden until widgets exist.)
- Notifications: one switch per reminder with its time (Today's story 7:00, Your move Mondays 9:00, New page, Lucky Star max once a day, Quiet hours 22:00-7:00) + a preview of the notification.
- Membership: black card "ISSUE11 Monthly · $9.99 / month · renews [date]", what's included, rows "Manage or cancel" (opens App Store subscriptions), "Restore purchases", "My print orders". One line: "Printed Issues are ordered separately ($29.99). Your Issues stay yours to read, even if you cancel."
- Lucky Star & AI: on/off switch, plain-words explanation of what it reads, "What Lucky Star remembers", "Clear Lucky Star's memory", "How your data is used". App works with it off.
- Order status: her cover, steps Order placed -> Printing (3-5 business days) -> Shipped (tracking link) -> On its way, estimates note, "Need help with my order".
- Safety: if she writes crisis words, Lucky Star stops and shows a full red (#D40806) screen with white text and white cards "You don't have to carry this alone." with "Call or text 988" (US) and "Call 911", plus help outside the US. No AI suggestions on this screen.
- My shelf (You → header → "My Issues"): BLACK background with a soft pink glow. Her Issues glide sideways like album covers (current one big and centered with a reflection, neighbours smaller and angled). A pink "Printed" sticker on finished Issues; the one in progress shows "12 of 40". Under it: dates, pages, moves kept, and page dots. Tap a cover to reread it. Below: a dark glass "Then → now" card with her first proof (date + her words) next to her latest proof.
- First-day states: each tab has one. Issue: "8 of 40 · 32 to print" and a grid of all 40 pages (8 filled with her pages, 32 dashed and labeled with what fills them, page 9 outlined in pink) + pink glass button "Fill page 9 · your first move".

THE 11 (Lucky Star)
Tapping it on Home opens a full-screen sheet; inside other tabs it rises as a half sheet (pink glow on its top edge) so she still sees the screen it helps with. While Lucky Star thinks, the pink glow slowly breathes and one small line says what it is reading ("Reading your Journal..."), no spinners. Under each answer, small pink tags show what it used ("Journal · Oct 12", "Career board"). The floating 11 gets a small pink dot when it has something for her (max once a day, no numbers); holding the 11 anywhere starts voice right away. The sheet (copy the look from my Lucky Star screenshots): a soft pink glow behind the 11 sticker, ONE big card in the middle with 1-2 pill buttons, a close X top right, and at the bottom a "Talk to Lucky Star..." bar with a send arrow and a big pink hold-to-talk mic. Under it: "Lucky Star is AI and can make mistakes".
What the card offers depends on the screen:
- Home: one next thing (start tonight's session / keep my move / add proof)
- My World: "It's missing a feeling" + 3 images -> ADD ALL 3 / SWAP ONE
- Sessions: one of the pre-made sessions picked for her and why ("Picked for you"). It never makes new sessions.
- Journal: one gentle question
- Issue: another version of this page
Buttons inside Lucky Star are liquid glass (frosted, see-through white over the pink glow); the main action is pink-tinted glass. Every action ends in something real, then a black toast at the top: "Added to ... · UNDO". Nothing changes without her tap.
If "Lucky Star & AI" is off, the sheet says "Lucky Star is off. You can turn it on in You." and the rest of the app still works.
Use placeholder results for now.

IRRESISTIBLE (all approved)
1. Monthly recap: at the end of each month, a 5-card story "Your [month] in ISSUE11", bold Wrapped style: full pink (#F65AAD) background, one giant red (#D40806) number (e.g. "4"), the cream 11 sticker tilted, a big headline ("moves you made room for.") and one short line listing them. Cards: moves she kept, her proof, most-saved image, the line she wrote that came true. Buttons: white "Share my month" + "Next".
2. Collectible stickers: at 10, 20, 30 and 40 pages she unlocks a sticker (zebra, red 11, cheetah 11, ...) for her cover or pages. Unlock screen with the pink glow; locked slots show the page number.
3. Final stretch: from page 35, her cover on Home glows pink with a tag "5 pages to print" (counts down) and "Your next page: ... · Fill it".
4. Arrival: when the print is delivered, Lucky Star asks "Is it in your hands? Take a photo with your Issue." The photo becomes page 1 of Issue 02.
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
- Every icon button has a VoiceOver name (the 11 = "Lucky Star").
- Preload the next story/page; soft placeholders instead of spinners.

STATES
Every tab needs an empty state. Also: a loading state ("Lucky Star is building"), an offline message ("You're offline. Your Issue is saved.") and a friendly error.

RULES
- Keep our design system exactly. Flat, printed-magazine feel.
- No streaks, no to-do lists, no stats, no goal trackers.
- Warm, simple copy. Never promise outcomes.
- Put all wording (prompts, move suggestions, card lines) in ONE strings file so it can change without code.
- Layouts must stretch to any screen size (no fixed widths).

Work in this order: 1) navigation, the 5 tabs and the floating 11; 2) Home; 3) Explore + player; 4) Issue + print order; 5) Journal; 6) You + settings; 7) Lucky Star; 8) first-day/empty states. After each step, stop so I can check it on my phone.
```
