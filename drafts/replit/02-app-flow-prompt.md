# Replit prompt 02: ISSUE11 app flow (after onboarding)
Made by 🩶 Manager, Oct 14, 2026, from design/APP-AFTER-PAYWALL.md (Megan's Oct 9 decisions) and design/PRODUCT-ARCHITECTURE.md.
How to use: paste AFTER prompt 01 (design system). Then upload screenshots of the V1 Prototype / Home V4 so Replit copies the look.

---

```
Now build the app's structure and flow (everything AFTER onboarding). Use ONLY the design system from step 1 (theme file, fonts, buttons). Keep it simple: build the screens and navigation with sample content first. No real payments, no real sign-in, no API keys yet.

WHAT ISSUE11 IS
A process-focused manifestation app. You build your dream life into your own personal magazine (your "Issue") and take small steps that make it real. The magazine is the hero. The AI (called Lucky Star) stays invisible until it's useful.

NAVIGATION
Bottom tab bar with 5 tabs: Home · Explore · Issue · Journal · You.
Plus a floating round "11" sticker button on EVERY screen (bottom right, above the tab bar). Tapping it opens Lucky Star (see below).

1. HOME (her daily edition, like a magazine front page)
- Top: her Issue cover (big photo, her name, "VOL. 01") with a thin progress line to her next Issue.
- "This week's move": ONE small action card for the week (not daily), with a button "I made room for it". Tapping it opens "Add proof" (a short note or photo), then a celebration screen "It's real".
- One audio session card (tap to play).
- One inspiration image from her World.
- One short note from Lucky Star (1-2 sentences).
- First-time state: "Your Issue has started" with her first move.

2. EXPLORE (Audio + Your World)
- Audio sessions grouped by goal (e.g. Confidence, Money, Love, Body, Calm). Tap a session -> full-screen immersive player (big image, play/pause, progress) -> optional "eyes closed" mode (dark screen, minimal) -> after the session: "How do you feel now?" with a button to write it in the Journal.
- Your World: a grid of images (preset worlds + her own photos at the top). Tapping "save" on any image adds it to her World. Button to add her own photo.

3. ISSUE (her magazine)
- Shows her magazine as swipeable pages (like a real magazine).
- Built automatically from her onboarding answers, her World images and the Journal lines she chose. For now use sample pages.
- Simple adjust controls: change cover, change mood (pick a world), include or leave out her words, and "Ask Lucky Star to change this page".
- Shows "Issue 1 of 4 this year". Default is one Issue every 3 months. Never push monthly.
- Button "Download my Issue" (PDF later).

4. JOURNAL
- One prompt a day at the top, with a refresh button for another prompt. Two types: prompts and gratitude.
- She can type or speak her answer.
- Each entry has a toggle "Put this in my Issue" (OFF by default). Only lines she marks go into her magazine.
- List of past entries below.

5. YOU
- This week's intention.
- Past proof (all her "It's real" moments).
- Settings: notifications, app icon, membership (manage / restore purchases), privacy, "Lucky Star & AI" on/off switch, sign out, delete account.

LUCKY STAR (the floating 11)
- On Home: opens a calm chat sheet (text + microphone) where she can talk about what she wants. It asks ONE thoughtful question at a time.
- Inside other tabs: opens a small sheet that helps with THAT screen only (Explore: suggest a session; Journal: suggest a prompt; Issue: change a page; World: suggest images).
- Anything Lucky Star creates shows as a preview with KEEP / EDIT / TRY AGAIN. Nothing is saved without her tapping KEEP.
- For now, use placeholder replies. No real AI connection yet.

RULES
- Keep our design system exactly. Flat, printed-magazine feel: huge Archivo Black uppercase headlines with tiny IBM Plex Mono labels.
- No streaks, no to-do lists, no goal trackers, no productivity features.
- Warm, simple copy. Never promise outcomes.
- Every screen needs an empty state (when there's no content yet).

Build the 5 tabs and the floating 11 first so I can tap through the whole app on my phone. Then we'll make each screen real one by one.
```

---

## After pasting
- Upload screenshots from your designs so Replit matches the look:
  - V1 Prototype: https://claude.ai/artifact/3T2jdNK2ZT1J5gzKjwhyTM
  - Home V4: https://claude.ai/artifact/NGegZJ3v8wQHbafL1Dcv9G
  - App Map: https://claude.ai/artifact/Tfe9RNTCYNHeaQagTtdyQf
- Check on your phone: can you tap through all 5 tabs and open the 11 everywhere?
- ⚠️ Later steps need Megan's approval before building: real sign-in, payments (RevenueCat), delete account, sending journal text to AI (consent + AI-off switch). Keys go in Replit Secrets only.
