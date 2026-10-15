# Replit prompt 02b: ISSUE11 app flow, SIMPLIFIED (after onboarding)
Made by 🎨🩵 Design Room, Oct 14, 2026, from design/V1-SIMPLIFIED.md. Replaces prompt 02 **once Megan approves the 3 decisions** in that file. Until then, don't paste it.
Mockup to upload as screenshots: https://claude.ai/artifact/QAbmsD9o7zGGY5qKHAQuFX (+ Megan's 5 Lucky Star screens in design/claude-design/lucky-star-v1/)
How to use: paste AFTER prompt 01 (design system). Then upload screenshots of the V1 Prototype so Replit copies the look.

---

```
Now build the app's screens and navigation for everything AFTER onboarding. Use ONLY the design system from step 1 (theme, fonts, buttons). Sample content only for now: no real payments, sign-in, AI or API keys yet.

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
- Top: the big wavy ISSUE11 masthead (full width) + a thin rule "VOL. 01 · [date]". When she scrolls down, it shrinks into a small sticky header (small masthead + "14 of 40 · Vol. 01"), like Apple Music large titles.
- Story bubbles (like Instagram): Today, Your move, Flashback, New page. Pink ring = new. Tap = full-screen story cards.
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
- Tap a session -> Session page like a Spotify album page (big image, title, length, "Picked for you", big pink play, "What you'll rehearse", "Up next") -> full-screen Player like Spotify Now Playing (video, live words like lyrics, scrubber, back/forward 15 s, save; swipe down = keeps playing in a glass mini player above the tabs; audio keeps playing with the phone locked). Every session has its own video, animation or image (no audio-only mode, no Watch/Listen switch).
- When a session ends: no new screen. The video dims, the last line stays, and a small glass card rises: "Keep a line from this? · What did you see yourself do?" with "Write it" (opens Journal with that prompt) and "Not now". It fades away by itself after a few seconds.

ISSUE
- Her magazine read like Instagram Stories: tap right/left to turn pages, thin page bars at the top, hold to pause, swipe down to close. Shows "14 of 40 pages · 26 to print". Every Issue has exactly 40 pages to print; it starts with 8 and fills up as she adds proof, photos and journal lines. At 40: "Ready to print".
- One row of edit icons under the page (like Instagram's edit tools): Cover · Mood · Words (on/off) · Update my Issue.
- Share button: share the current page as an image (iOS share sheet).
- Tap a page -> edit sheet: swap photo, edit text, pick another layout (only from my layouts), "Try another version".
- Under her Issue: a "Ready to print · 15 of 40 pages" button, greyed out until 40 pages, then active.
- At 40 of 40 pages: "Ready to print" screen with a grid of all 40 pages and the button "I love it · Approve my Issue".
- Only after she approves: "Order my print" screen (cover preview, copies, shipping address, price "$29.99" per Issue, shipping options three shipping options "Standard · 11–14 business days · Free" (selected), "Expedited · 6–9 business days · + $16", "Express · 5–8 business days · + $32", a Total line "$29.99 + tax", and a small note "Printing takes 3–5 business days before shipping. Estimates, not guaranteed. Hawaii, Alaska and Puerto Rico take longer." Rules: purchase happens inside the app (not a web page), US addresses only; if the address is a PO box or APO/FPO, show only "Standard" and "Priority Mail · 9–12 business days · + $10". Full spec: design/PRINT-PURCHASE.md, Apple Pay button "Place my order"). No real payment yet.

JOURNAL
- Today's prompt as a big card (like an Instagram question sticker). Swipe it away for another prompt.
- A text box (the iPhone keyboard mic handles voice).
- Toggle on each entry: "Put this in my Issue" (OFF by default).
- Past entries listed below.

YOU
- Top: her photo, her name, "The Freedom Issue · 14 of 40 pages".
- A horizontal row of her proof tiles ("It's real" moments), "See all" opens the full grid.
- Below, a big settings list in huge uppercase type, one row each with an arrow: notifications (on/off + time), app icon, membership (manage subscription, restore purchases), "Lucky Star & AI" on/off switch, privacy policy, terms, sign out, delete account (with a confirm screen).

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

STATES
Every tab needs an empty state. Also: a loading state ("Lucky Star is building"), an offline message ("You're offline. Your Issue is saved.") and a friendly error.

RULES
- Keep our design system exactly. Flat, printed-magazine feel.
- No streaks, no to-do lists, no stats, no goal trackers.
- Warm, simple copy. Never promise outcomes.
- Put all wording (prompts, move suggestions, card lines) in ONE strings file so it can change without code.
- Layouts must stretch to any screen size (no fixed widths).

Build the 5 tabs and the 11 first so I can tap through the whole app on my phone. Then we make each screen real one by one.
```

---

## After pasting
- Check on your phone: can you tap through all 5 tabs, finish a move → proof → "It's real", and open the 11 everywhere?
- ⚠️ Need your approval before building (CLAUDE.md rule 4): real sign-in, payments (RevenueCat), delete account, sending journal text to AI (consent + AI-off switch). Keys go in Replit Secrets only.
