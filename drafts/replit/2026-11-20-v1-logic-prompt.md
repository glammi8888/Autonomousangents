# Replit update 2 · v1 logic (approved by Megan Nov 20) · send ONLY after update 1 has finished

Follow-up to the v1 screens update. Build the behavior underneath the new tabs. Keep it lean to save credits: reuse the existing local storage (IssueProvider), no new packages unless required for the AI call, no long self-testing loops; stop and list what changed and what you skipped.

Do not change: onboarding, the cover reveal, the existing paywall, sign-in, payments or the api-server database. Account data stays on the phone in this update.

Design updates: brand pale pink #F4E4E4 to #F0D0D8 replaces the old ombre gradient (first open and paywall only). Floating 11: bright pink glow #F6AAC6 to #FFD6E4 about 26px that shows on every background and gently pulses (2.8s loop, opacity 0.85 to 1, scale 1 to 1.08).

What the app remembers (on the phone): the current issue (number, title, pages max 40, start date); each page (photos, words, layout, source: action/journal/save/upload, date); the weekly action (text, week starting Monday, status open/smaller/done/moved); journal entries (date, question, text, photo, always private); saves (images and sessions hearted or uploaded, with topic); the player position; settings (notification switches, quiet hours, app icon, name).

Home: "[pages] of 40" everywhere = pages kept in the current issue. First open on a Monday with no action opens Focus pick. "I did it" marks the action done, shows the celebration, and "See my page" opens the page maker with the action text already in. "Not yet" opens the smaller-action sheet, offered once a week. Today's question and tonight's session rotate daily from a fixed list. Vision shows the 3 newest saves (none: only the "Explore your vision" button).

Focus: one action a week, week starts Monday. "Make it smaller" swaps in a smaller version the user can edit; "Keep it for next week" moves it to next Monday. "Weeks showing up" counts weeks with a done action; it never resets; no streaks, no guilt. Optional reminder Monday 9:00.

Explore: heart saves on the phone; "Upload your own" adds the photo to saves; Saved boards grouped by topic; "Add to my issue" opens the page maker with that image; sessions play on tap, the mini player stays across tabs and remembers position; search filters titles and topics; "Send" on no results and on "What are we missing?" opens an email to support@issue11.app.

Issue: new page in 3 steps (content, layout with "Editor decides" as default, keep). "Keep page" adds it and shows the toast; "Undo" for 5 seconds removes it. Edit swaps layout, photo or words, and never changes the user's words. Pencil names the issue. Print screen unlocks at 40 pages: "Order my print · $29.99" opens the issue11.app order page in the browser (no in-app payment), then an "I've ordered it" button starts Issue 02 (new empty issue, number +1; the finished issue is kept).

Journal: entries are private and autosave while typing; wall newest first; empty wall shows "Write my first page"; "Add to my issue" opens the page maker with the words exactly as written.

You: notification switches schedule local reminders (action Monday 9:00, journal daily if on, new page, Editor at most 1 a day, quiet hours 22:00 to 7:00). App icon switches the iOS alternate icon. Help us improve opens an email to support@issue11.app then "Thank you. We read every one." Membership is display only for now. Sign out and Delete account stay as they are.

The Editor (the 11) uses real AI through Replit's built-in AI integration (use Anthropic Claude; no API key in the code). Before the first AI use, show the consent screen: names the AI provider, "Allow and continue", "Not now", "How we use your data"; store the choice; add an on/off switch in You > The Editor & AI. Tap the 11 = one card for the current screen (Home: 3 smaller steps or action ideas; Explore: 3 images for a board or tonight's session; Issue: "Let me lay this out." and pick a layout; Journal: one gentle question; You: nothing). Hold = the live chat, answers as action cards, never a long thread. Send the AI only what the card needs (the current action, page or question); journal text only if "read my journal" is on. Without consent or offline, show fixed suggestions instead. Never rewrite the user's words; never call the user "she" or "her"; say "action", never "move". Keep the existing crisis-word safety stop (988). Skip affirmations from journal.
