# ISSUE11 v1 · logic per tab (APPROVED by Megan, Nov 20, 2026: "ok" · Q2 "ok" · Q3 "No")

Source: "ISSUE11 — Design Handoff v1" (taps + copy) + what Replit already has (audit Oct 21). This is the behavior *underneath* the screens. Nothing here goes to Replit until Megan says OK.

## Ground rules
- **Data stays on the phone** (the app's existing local storage). No cloud database, no sign-in, no payments, no backend changes in this round. Those need their own spec (CLAUDE.md rule 4).
- **The Editor uses real AI** (Megan, Q3: "No" to fixed lists). It uses Replit's built-in AI connection (no API key pasted by us), only after the AI consent screen (CP5) is accepted. Without consent or offline, it falls back to fixed suggestions. Journal text is only sent if "read my journal" is on.
- **One issue at a time = 40 pages.** "15 of 40" always means pages kept in the current issue.
- **A week starts Monday.** One action per week.

## What the app remembers
| Thing | What it holds |
|---|---|
| Issue | number, title, list of pages (max 40), start date |
| Page | photos, words, layout, where it came from (action, journal, save, upload), date |
| Weekly action | text, week, status: open · smaller · done · moved to next week |
| Journal entry | date, question, text, photo, private (always) |
| Saves | images and sessions you hearted or uploaded, topic |
| Player | the session playing and where you stopped |
| Settings | notification switches, quiet hours, app icon, your name |

## Home
- **Sees:** cover with "[pages] of 40", this week's action, today's question, tonight's session, 3 latest saves, Your Issue.
- **Does:** I did it · Not yet · Write today's page · Listen now · Explore your vision · Open my issue.
- **Underneath:** first open on a Monday with no action → Focus pick (FC1). "I did it" marks the action done → celebration (FC5) → "See my page" opens the page maker with the action already written in. "Not yet" opens the smaller-action sheet, offered once a week. Today's question and tonight's session change daily from a fixed list. Vision shows your 3 newest saves; with none, it shows "Explore your vision" only.

## Focus
- **Underneath:** FC1 offers 3 Editor suggestions (fixed list by topic) or "Write my own". "Make it smaller" swaps in the smaller version; you can edit it. "Keep it for next week" moves it to next Monday. "Weeks showing up" = number of weeks with a done action. It never resets, and there's no streak and no guilt. Optional reminder Monday 9:00.

## Explore
- **Underneath:** heart = saved on the phone. "Upload your own" adds your photo to saves. Saved boards are grouped by topic (the Editor's sorting for v1). "Add to my issue" opens the page maker with that image. Sessions start playing on tap; the mini player stays across tabs and remembers where you stopped. Search filters titles and topics; "Send" on no results or "What are we missing?" opens an email to support@issue11.app.

## Issue
- **Underneath:** new page in 3 steps (content → layout, "Editor decides" by default → keep). "Keep page" adds it and shows the toast; "Undo" (5 seconds) removes it. Edit swaps layout, photo or words (your words are never changed by the app). The pencil names the issue (Editor ideas = fixed list). The print screen unlocks at 40 pages; "Order my print · $29.99" opens the issue11.app order page (no in-app payment). An "I've ordered it" button then starts Issue 02 (Megan, Q2: "ok").

## Journal
- **Underneath:** entries are private and autosave as you type. The wall shows newest first; empty wall → "Write my first page". "Add to my issue" opens the page maker with your words exactly as written. Tapping the 11 here gives one gentle question (JR6).

## You
- **Underneath:** notification switches schedule reminders on the phone (action Mon 9:00, journal daily if on, new page, Editor max 1 a day, quiet 22:00–7:00). App icon switches the iPhone icon. Help us improve opens an email to support@issue11.app → "Thank you." Membership is display only for now. Sign out and Delete account stay exactly as they are (making Delete real is a separate, required item before the App Store).

## The 11 (Editor)
- **Tap:** one card for the screen you're on (Home: 3 smaller steps · Explore: 3 images or tonight's session · Issue: "Let me lay this out." · Journal: one question · You: nothing).
- **Hold:** the existing chat preview stays as it is (not connected to AI). Affirmations (ED3) are skipped.

## New in the handoff doc (updated Nov 20, evening)
- **Brand pale pink** #F4E4E4 → #F0D0D8 replaces the old ombre; only on first open and the paywall (exact hex to confirm).
- **Floating 11 glow:** bright pink #F6AAC6 → #FFD6E4, ~26px, gentle pulse (2.8s loop, opacity 0.85→1, scale 1→1.08).
- **App Store screens CP1–CP5** (Apple rejects v1 without them):
  - CP1 Sign in: Sign in with Apple first, email second, Terms + Privacy line.
  - CP2 Paywall: Yearly with 7 days free (preselected) $69.99 · Monthly $9.99 · founding $39.99 first year as intro offer · Restore · Terms (EULA) · Privacy · Close.
  - CP3/CP4 Delete account from You: warns it doesn't cancel the subscription + link to manage it → deletes account and all content → back to sign-in.
  - CP5 AI consent the first time the 11 is held: names the AI provider, Allow / Not now / How we use your data; switch in You › The Editor & AI.
  - Plus setup: bundle id com.issue11.app, remove demo/"preview" content, support page, privacy labels, demo account for Apple review.

### What CP1–CP5 change in this logic
These need a real account and real purchases, so the "data stays on the phone, no sign-in, no payments" ground rule can't hold for them. They touch sign-in, payments, user data, AI and account deletion: every one is on the "Megan approves the spec before building" list (CLAUDE.md rule 4). Recommended order to keep Replit credits low:
1. **Now:** tabs + logic above (phone-only data) + the pink and 11 glow updates.
2. **Next, one separate update after your OK:** CP1–CP5, using Replit's built-in sign-in and database, StoreKit via RevenueCat, and deleting everything in one place. Spec: `drafts/dev/signin-payments-spec-v1.md` (needs its price fixed to $69.99 first).

## 2 questions for Megan
1. **After ordering the print**, when does Issue 02 start? We can't see the website order from the app. Recommend: a "I've ordered it" button on the print screen starts Issue 02.
2. **The Editor's suggestions:** fixed lists for v1 until AI is connected? Recommend: yes.

## Download my issue (Megan, Nov 21: "they should be able to download their issue anytime" + "(once they reach the 40 pages)")
- **When:** unlocks when an issue reaches 40 of 40, and stays available anytime for every finished issue.
- **Where:** Print screen (IS7) next to "Order my print" · Issue reader → Share · You → My Issues → each finished issue → Download · Delete account (CP3), above "Delete my account" (open: allow a partial PDF there even before 40, recommended).
- **Underneath:** builds a PDF of all pages kept so far (cover + pages in order, print layout) on the phone and opens the iOS share sheet (save to Files, AirDrop, email). Works offline; nothing is uploaded. The same page layouts later make the print file.

## Your pace: daily, weekly or monthly actions (PROPOSED, waiting for Megan's OK)
Megan, Nov 21, word for word: "I'm thinking maybe we can have them choose if they want daily action reminders or weekly or monthly so they can act at their pace" + "No they can get daily actions that are different too doesn't have to be weekly".
- **Choose:** first time on Focus (FC1), a "Your pace" choice: Daily · Weekly (default) · Monthly. Can be changed anytime in You › Your pace; the change starts with the next day, week or month. Onboarding is unchanged (locked).
- **One action per period:** Daily = a new action each day (can differ every day); Weekly = one a week (Monday); Monthly = one a month (the 1st).
- **Home:** the label follows the pace: "Today's action" · "This week's action" · "This month's action". I did it / Not yet work the same.
- **Focus:** FC1 pick (3 Editor suggestions or Write my own) opens at the start of each period. "Make it smaller" is the same. "Keep it for next week" becomes "Keep it for tomorrow / next week / next month".
- **Progress:** "Weeks showing up" becomes "Actions done" (total, never resets, no streak, no guilt). Missing a day changes nothing.
- **Your issue:** unchanged. Any done action can become a page ("See my page"), so a daily pace fills the 40 pages faster.
- **The Editor:** with AI consent, fresh suggestions each period; without consent or offline, a fixed list per topic big enough for daily use (about 30 per topic) without repeats.
- **Reminders:** follow the pace (daily morning, Monday 9:00, or the 1st), quiet hours 22:00–7:00, all can be turned off.
- **Screens touched:** Home 01 label, FC1–FC6 copy, You (new "Your pace" row + a small picker). Megan to OK the logic, then draw the picker, then it goes in ONE Replit update.
