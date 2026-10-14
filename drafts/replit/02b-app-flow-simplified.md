# Replit prompt 02b: ISSUE11 app flow, SIMPLIFIED (after onboarding)
Made by 🎨🩵 Design Room, Oct 14, 2026, from design/V1-SIMPLIFIED.md. Replaces prompt 02 **once Megan approves the 3 decisions** in that file. Until then, don't paste it.
How to use: paste AFTER prompt 01 (design system). Then upload screenshots of the V1 Prototype so Replit copies the look.

---

```
Now build the app's screens and navigation for everything AFTER onboarding. Use ONLY the design system from step 1 (theme, fonts, buttons). Sample content only for now: no real payments, sign-in, AI or API keys yet.

WHAT ISSUE11 IS
A process-focused manifestation app. She builds her dream life into her own magazine (her "Issue") and takes one small step a week. The magazine is the hero.

NAVIGATION
Bottom tabs: Home · Explore · Issue · Journal · You.
A floating round "11" sticker button on every screen (bottom right, above the tabs).

HOME (3 blocks only)
1. Her Issue cover (photo, her name, "ISSUE 01"). Tap -> Issue tab.
2. "Next thing" card with one button. Pick it with these rules:
   - no move this week -> "Pick this week's move" -> Pick Move screen
   - move done but no proof -> "Add proof" -> Add Proof screen
   - otherwise -> "Today's session" -> Player
3. "This week's move" card with the button "I made room for it" -> Add Proof (one short line of text) -> celebration screen "It's real".
Pick Move screen: her last move, 3 suggestions from a list, and "Write my own".

EXPLORE
- One list of sessions, "For you" first (matched to her onboarding topic).
- Tap a session -> full-screen Player: Watch (image fills the screen) or Listen (dark screen). Play/pause and progress.
- When it ends: "How do you feel now?" -> button "Write it in my Journal".
- Below the sessions: Your World, a grid of preset images. Tap the heart to save one to her World.

ISSUE
- Her magazine as swipeable pages. Shows "Issue 01 · next one in [month]".
- Adjust panel with 4 controls: cover style, mood, "Your words" on/off, and a button "Update my Issue".
- Share button: share the current page as an image (iOS share sheet).

JOURNAL
- Today's prompt at the top with a refresh button.
- A text box (the iPhone keyboard mic handles voice).
- Toggle on each entry: "Put this in my Issue" (OFF by default).
- Past entries listed below.

YOU
- Past proof (all her "It's real" moments).
- Settings: notifications (on/off + time), app icon, membership (manage subscription, restore purchases), "Lucky Star & AI" on/off switch, privacy policy, terms, sign out, delete account (with a confirm screen).

THE 11 (Lucky Star)
Tapping it opens a small sheet with ONE action for the screen she is on:
- Explore: "Pick a session for me"  - Journal: "Ask me a question"
- Issue: "Try another version of this page"  - World: "Find images for my topic"
- Home: shows the same "next thing" as the Home card.
Anything it makes shows as a preview with KEEP / TRY AGAIN. Nothing is saved without KEEP.
If "Lucky Star & AI" is off, the sheet says "Lucky Star is off. You can turn it on in You." and the rest of the app still works.
No chat screen. Use placeholder results for now.

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
