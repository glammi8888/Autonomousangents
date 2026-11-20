Read replit.md first. It is the only source of truth; anything older in the code or chat history is outdated.

Goal: rebuild the 5 tabs (Home, Explore, Issue, Journal, You) and the Editor to the v1 design, with the logic underneath. Keep it lean: reuse existing components, no new packages unless needed for the AI call, no long self-testing loops. When done, stop and give me a short list: what changed, what you skipped, what needs my decision. Do NOT touch onboarding, the first-open cover reveal, the paywall, sign-in, payments or the api-server database.

STEP 1 · Cleanup
- Rename every "Lucky Star" / "Lucky" to "The Editor" in code, labels and file names (including the 11 button).
- "My saves" / "Her world" becomes Explore → Saved.
- Delete screens not in v1 and their links: session detail, eyes-closed, how-do-you-feel, ritual, progress, streak, old Listen tab, her-world, any "BECOME HER" sample.
- Use only Inter Tight; remove Archivo Black, Archivo Narrow, IBM Plex Mono. Move all colors into constants/colors.ts (tokens in replit.md).

STEP 2 · Screens (open these images; phone 390×844)
Home full scroll https://framerusercontent.com/images/9sieMdhQCXA2bXugVtIORB0dJCg.jpg
Explore images https://framerusercontent.com/images/LS5kKvfcu4R467bWXknQZbc8.jpg
Explore close-up https://framerusercontent.com/images/ywsOCLU651rxLjHHhjWsdnZL9nQ.jpg
Sessions https://framerusercontent.com/images/CVqLG1zXp6T9kME0pjQ4kxcJLY.jpg
Player https://framerusercontent.com/images/mvUtTmdX9PjVITUkkzchPF07tns.jpg
Saved boards https://framerusercontent.com/images/xVnu5zReQc8cWHM4dkiuqpBl7E.jpg
Focus pick https://framerusercontent.com/images/zdkrJy7Nn8468PsVu8be9ZAE.jpg
Focus not yet https://framerusercontent.com/images/ntRyznCTF3arZtagx8F05rJvLA.jpg
Your Issue https://framerusercontent.com/images/74OkzX3wzShtyjHByNCiMtLraQ.jpg
Reader https://framerusercontent.com/images/jQpe918M23uUmZ7wbyByG7Ss64.jpg
New page layout https://framerusercontent.com/images/dQJVKVbbcV97PsFGKQN0c98gCLM.jpg
Print at 40 https://framerusercontent.com/images/XTHWPa6o677R1c6tJZovFzr8MDk.jpg
Journal wall https://framerusercontent.com/images/T5RTyVVR4ZnzGSQHHg6LmU8URnE.jpg
Journal write https://framerusercontent.com/images/flvamS72M2bzUO2mbIvphD939w.jpg
Editor card https://framerusercontent.com/images/jbzPrvtTwqJKaTmiPFHqqDAGw8.jpg
You https://framerusercontent.com/images/7fTHe4zJr5hQJleY6VRDcAuRJ9I.jpg

Shared pieces: header (ISSUE11 logo left, label right, rule under; white on photos) · tab bar 84px with line icons · floating 11 (54px white circle, pink glow #F6AAC6→#FFD6E4 that gently pulses: 2.8s loop, opacity 0.85→1, scale 1→1.08) on every screen except You · mini player 60px dark bar above the tab bar while a session plays · bottom sheets · toast "Added to your issue · p.16 · Undo".

STEP 3 · Copy and logic per tab (data stays on the phone, IssueProvider)
HOME (one long scroll): "Your magazine. Your evolution." · "Good morning, [Name]." · cover with looping video, "Who told you your destiny was already written?", "A different future begins with a different narrative.", "[pages] of 40 pages" · 01 / Focus "Become the person your future requires." with this week's action, I did it / Not yet · 02 / Write "A different future begins with a different narrative." today's question + "Write today's page" · 03 / Listen "Imagine it. Act on it. Evolve into it." tonight's session + "Listen now" · 04 / Vision "Gorgeous, gifted & well paid." "A little reminder of what you're working toward." 3 newest saves + "Explore your vision" · Your Issue "The story is changing. So are you." "[pages] of 40 pages." "Open my issue".
Logic: first open on a Monday with no action → Focus pick. Today's question and tonight's session rotate daily from a fixed list. No saves yet → Vision shows only the button.

FOCUS: FC1 "Be your own dream girl." "You've got plans. Let's pick one worth acting on this week." 3 Editor suggestions + "Write my own action →" + "This is my action" · FC2 sheet "What's one thing you could do this week?" "Keep it small enough to do by Sunday." · FC3 sheet "Not yet? That's all right." "A different future begins with a different narrative. Sometimes that means starting smaller." "Make it smaller" / "Keep it for next week" (offered once a week) · FC4 Home with the smaller action "Small still counts." · FC5 celebration "You did the thing." "You said you'd do it. And you did. Another page of your story is ready." "See my page" → page maker with the action text already in · FC6 Home done "Now p.[n] of your issue →".
Logic: one action a week, week starts Monday. Smaller version is editable. "Keep it for next week" moves it to next Monday. "Weeks showing up" = weeks with a done action, never resets. Optional reminder Monday 9:00.

EXPLORE: tabs Images / Sessions / Saved, search, chips All, Money, Love, Body, Home, Style, Travel. Images = endless 2-column grid, first tile "Upload your own", heart saves, tile → close-up ("Add to my issue", "Saved", "More like this"). Sessions: tap plays straight into the mini player; tap mini player → full player; swipe down → mini player; remembers position. Saved = boards grouped by topic. No results: "Can't find it?" "Tell us what you'd like to see." "Send". Every ~100 tiles: "What are we missing?" card. Both Send buttons open an email to support@issue11.app.

ISSUE: IS1 "Issue [01] · [Nov 2026]" "Your personal magazine" "[title]" "[pages] / 40 pages · [left] to print" "Read my issue" / "New page" + thumbnails, pencil → name issue · IS2 reader, swipe pages, Done / Edit / Share · IS3 "What goes on this page?" "Photos, words or both. An image alone is a page too." Your saves / Upload / Words · IS4 "This is how it will print" layouts: Editor decides (default), Photo, Words, Collage, "More layouts →", "Keep page" · IS5 toast with Undo (5 seconds) · IS6 "Edit this page." layout / swap a photo / edit my words · IS7 at 40 pages: "40 of 40." "Your issue is ready to print." "Order my print · $29.99" opens the issue11.app order page in the browser, then an "I've ordered it" button starts Issue 02 (finished issue is kept) · IS8 "Name your issue." with Editor ideas, "Save title", "Let the Editor name it".

JOURNAL: JR1 "Today's question" "What would future you do?" "Write today's page" "Your wall." "Just your thoughts, exactly as you left them." · JR2 write, autosaves, "Private · Saved", Add a photo, Done, Add to my issue · JR3 "Saved. Just for you." "Nobody else needs to read this. Your words stay here unless you decide to put them in your magazine." · JR4 read entry: Edit, Share, Add to my issue · JR5 empty: "The page is blank. The possibilities are not." "Write my first page".
Logic: entries always private; "Add to my issue" sends the words exactly as written.

YOU: rows My Issues, Notifications, App icon, Membership, The Editor & AI, Help us improve (dark card "Tell us what you need."), Help, Privacy, Terms, Sign out, Delete account. Help us improve: chips Feature idea / Something's annoying / What I need + text → email support@issue11.app → "Thank you. We read every one." Notifications switches schedule phone reminders: action Mon 9:00, journal daily (optional), new page, Editor max 1/day, quiet hours 22:00–7:00. Membership shows "Gorgeous, gifted & well paid." Yearly $69.99 · Monthly $9.99 · "Printed copies $29.99 each" (display only). Keep Sign out and Delete account logic exactly as it is.

STEP 4 · The Editor (the 11) with real AI
Use Replit's built-in AI integration (Anthropic Claude); no API key in the code. Before the first AI use, show a consent screen naming the AI provider: "Allow and continue" / "Not now" / "How we use your data"; save the choice; on/off switch in You → The Editor & AI.
Tap the 11 = one card for that screen: Home 3 smaller steps or action ideas · Explore 3 images for a board or tonight's session · Issue "Let me lay this out." · Journal one gentle question · You nothing. Hold = live chat that answers as action cards, never a long thread.
Send the AI only what the card needs; journal text only if "read my journal" is on. Without consent or offline, show fixed suggestions. Skip affirmations from journal.
