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

HOME (3 blocks only)
0. A row of round story bubbles at the top (like Instagram): Today (one line on one of her images), Your move, Flashback (her own Journal words from 30+ days ago), New page. A pink ring means it is new; tap to open full-screen story cards (tap to go forward, like Instagram Stories). New "Today" line every day from the strings file.
1. Her Issue cover (photo, her name, "ISSUE 01") with a thin progress bar: "14 of 40 pages · 26 to print". Tap -> Issue tab.
2. "Next thing" card with one button. Pick it with these rules:
   - no move this week -> "Pick this week's move" -> Pick Move screen
   - move done but no proof -> "Add proof" -> Add Proof screen
   - otherwise -> "Today's session" -> Player
3. "This week's move" card with the button "I made room for it" -> Add Proof, like posting a story (write one line, optional photo -> "Share to my Issue") -> celebration screen "It's real".
Pick Move screen: her last move, 3 suggestions from a list, and "Write my own".

EXPLORE
- Top switch like TikTok: Sessions · My World.
- Sessions: full-screen vertical previews, swipe up for the next (like TikTok), "For you" first (matched to her onboarding topic). Only 7, no endless feed.
- Tap a session -> Session page like a Spotify album page (big image, title, length, "Picked for you", Watch/Listen switch, big pink play, "What you'll rehearse", "Up next") -> full-screen Player like Spotify Now Playing (video, live words like lyrics, scrubber, back/forward 15 s, save; swipe down = keeps playing in a glass mini player above the tabs; audio keeps playing with the phone locked, with lock-screen controls). Old line for reference: full-screen Player: Watch (image fills the screen) or Listen (dark screen). Play/pause and progress.
- When it ends: "How do you feel now?" -> button "Write it in my Journal".
- My World: Pinterest-style masonry grid. Her own photos and saved preset images show first. A "+ Add" button opens the iPhone photo picker (only the photos she picks, never her whole library). Tap the heart (or double-tap) on a preset to save it.

ISSUE
- Her magazine read like Instagram Stories: tap right/left to turn pages, thin page bars at the top, hold to pause, swipe down to close. Shows "14 of 40 pages · 26 to print". Every Issue has exactly 40 pages to print; it starts with 8 and fills up as she adds proof, photos and journal lines. At 40: "Ready to print".
- One row of edit icons under the page (like Instagram's edit tools): Cover · Mood · Words (on/off) · Update my Issue.
- Share button: share the current page as an image (iOS share sheet).
- Tap a page -> edit sheet: swap photo, edit text, pick another layout (only from my layouts), "Try another version".
- At 40 of 40 pages: "Ready to print" screen with a grid of all 40 pages and the button "I love it · Approve my Issue".
- Only after she approves: "Order my print" screen (cover preview, copies, shipping address, price placeholder "Price TBD", Apple Pay button "Place my order"). No real payment yet.

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
Tapping it opens a full-screen sheet (copy the look from my Lucky Star screenshots): a soft pink glow behind the 11 sticker, ONE big card in the middle with 1-2 pill buttons, a close X top right, and at the bottom a "Talk to Lucky Star..." bar with a send arrow and a big pink hold-to-talk mic. Under it: "Lucky Star is AI and can make mistakes".
What the card offers depends on the screen:
- Home: one next thing (start tonight's session / keep my move / add proof)
- My World: "It's missing a feeling" + 3 images -> ADD ALL 3 / SWAP ONE
- Sessions: one of the pre-made sessions picked for her and why ("Picked for you"). It never makes new sessions.
- Journal: one gentle question
- Issue: another version of this page
Every action ends in something real, then a black toast at the top: "Added to ... · UNDO". Nothing changes without her tap.
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
