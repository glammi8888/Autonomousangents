# Replit prompt 04: Lucky Star to Megan's A–G design (change 2 of 4, Oct 21, 2026)
Made by 🩵 PRODUCT (Build Room) from drafts/dev/replit-build-audit-2026-10-21.md (Lucky Star row), design/V1-SIMPLIFIED.md (Lucky Star in V1 + UX ideas 1–4, approved Oct 14–15), drafts/replit/handoff/01-app-flow-prompt.md ("THE 11") and design/claude-design/lucky-star-v1/.
**Status: DRAFT, not sent. Megan reviews first.** Send only after change 1 is verified and Megan says go.
Scope note: the magazine page and Journal page designs are not final (Megan, Oct 21), so this prompt does not touch page layouts or the Journal screen. Placeholder answers only. No real AI, no API keys, no data sent anywhere (AI data handling needs Megan's spec approval, CLAUDE.md rule 4).

```
Lucky Star update only. Keep the 11 sticker, the pink fade/glow and the dreamy glass buttons exactly as they look now. Don't change onboarding, the tabs, colors or any other screen. Use placeholder answers (no real AI, nothing sent online).

1. One answer card, never a chat thread. Remove the list of past messages. After she asks or taps a suggestion, the sheet shows ONE big card (small kicker, headline, 1-2 lines) with 1-2 pill buttons (main one = pink-tinted glass), and small pink "Made from" tags under it (for example "Journal · Oct 12"). A new question replaces the card. Keep the "Talk to Lucky Star..." bar with send arrow and the big pink hold-to-talk mic, the close X, and the line "Lucky Star is AI and can make mistakes".

2. Size: tapping the 11 on Home opens the full-screen sheet (as now). Inside Explore, Journal, Issue and My saves it opens as a half sheet with a pink glow on its top edge, so she still sees the screen behind it. Drag down or X closes it.

3. While it "thinks", no spinner: the pink glow slowly breathes and one small mono line says what it is reading ("Reading your Journal..."), then the card appears.

4. The card depends on the screen she opened it from (the top label shows that screen's name):
   - Home: the one next thing (no move this week -> "Pick my move" · move done but no proof -> "Add proof" · otherwise -> start tonight's session).
   - Explore: "Pick a session for me" -> it picks ONE of the existing demo sessions, shows its image, name and length, says "Picked for you" plus one line why, and a "Play" button that opens Now Playing for that session. It never says "made" and never shows "NO SESSIONS ADDED YET".
   - Journal: one gentle question about what she wrote (never words put in her mouth). Only the Lucky Star card changes; don't touch the Journal screen itself, its design isn't final.
   - Issue: "Try another version of this page" (swap between the existing placeholder layouts only; don't restyle the magazine pages or add new layouts, their design isn't final).
   - My saves: "It's missing a feeling" + 3 images -> ADD ALL 3 / SWAP ONE (keep the current behavior).
   Rename every old label: "In Scribe" -> "Journal", "Listen" -> "Explore", "Curate" / "My World" / "Your World" -> "My saves".

5. Every action ends in something real, then a black toast at the top: "Added to ... · UNDO" (Undo works for 5 seconds). Nothing changes without her tap. Keep this as it works now.

6. "Lucky Star & AI" off state: add an on/off switch on the "Lucky Star & AI" row in You (saved on the phone, default on). When it's off, tapping the 11 shows one card: "Lucky Star is off." / "Everything else works as usual: your Issue, sessions and Journal. You can turn it on in You." with one button "Turn on in You" that opens that setting. The rest of the app keeps working.

7. Keep the safety behavior exactly as it is: crisis words stop Lucky Star and show the full red safety screen with 988 / 911.

8. Run the typecheck and the tests and fix anything this change broke. Tell me which files you changed and whether typecheck + tests pass.

Don't publish or deploy anything.
```

## Acceptance criteria (Build lead verifies by reading the code)
1. No message list/thread is rendered in the Lucky Star sheet; one card at a time, with "Made from" tags.
2. Full screen from Home, half sheet from the other tabs.
3. Explore pick returns a real demo session and its Play opens Now Playing; no "NO SESSIONS ADDED YET"; copy says "picked", never "made".
4. "Lucky Star & AI" switch exists in You, persists, and the off card shows the approved copy.
5. No old labels left (grep: "In Scribe", "Curate", "My World", "Your World" in Lucky Star files; "Listen" as a screen label).
6. Safety screen path unchanged; onboarding files unchanged; typecheck + tests pass.
Limits: max 2 attempts.

Out of scope (later): pink dot on the 11 (max once a day), snapping the 11 to the nearest edge (change 4), real mic/voice, real AI.
