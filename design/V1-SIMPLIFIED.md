# ISSUE11 V1, simplified (Design Room, Oct 14, 2026) · ⏳ PROPOSAL, waiting for Megan
Megan is building in Replit and asked for a "simplify" pass on **functionality, not the look**. Our design stays exactly as is (lesson Oct 9).
**Status:** proposal only. Nothing changes in the build until Megan approves. Onboarding (design/ONBOARDING-V3.md) is locked and untouched. The 5 tabs and the 4 functions stay.
**Sources:** design/APP-AFTER-PAYWALL.md · design/PRODUCT-ARCHITECTURE.md · design/POSITIONING.md · design/LUCKY-STAR-VOICE.md · design/claude-design/V1-SCREENS.md · drafts/replit/02-app-flow-prompt.md · .pipeline/app-store-checklist.md
**Replit prompt:** drafts/replit/02b-app-flow-simplified.md


## ✅ Final V1 design (Oct 14, design check) · mockup: https://claude.ai/artifact/QAbmsD9o7zGGY5qKHAQuFX
14 screens + Lucky Star A–G + first-open sticker peel. Megan's existing designs cover the rest: system states (design/claude-design/system-states), onboarding/notifications/Meet Lucky Star/paywall/sign in (ONBOARDING-V3, locked).
01 Home = a long scrollable page like Megan's V4 (Megan, Oct 15: "I do like the home screen to be a long scrollable page though"): wavy ISSUE11 masthead at about 75% width, centered (Megan: "I do like slightly smaller too"), that collapses into a small sticky header on scroll · story rings · big cover "x of 40" · your move · resume session · Lucky Star flashback · From your World strip · Latest pages strip · ends "That's today. See you tomorrow." (finite, no endless feed) · 02 Today story · 03 Explore ("For you" = one mixed feed; "Sessions" chip = organized like Spotify: "Picked for you tonight" + shelves by type + 5/10 min chips. Megan, Oct 14: "the feed should be a mix of both (the "for you" and the sessions should be organized (#2)") · 04 Player (session page, Now playing; at the end a glass card over the video "Keep a line from this?" replaces the "How do you feel now?" screen: Megan, Oct 15, "Not sure how I feel about this screen aesthetically... Is it necessary as well?"). Megan, Oct 15: the eyes-closed "Listen" screen is removed; "Every audio also has a video/animation/image with it." No Watch/Listen switch; audio keeps playing with the phone locked · 05 Issue reader · 06 Add proof · 07 It's real · 08 Journal = write straight into her Issue (Megan, Oct 15: "ok i love option 2"): her words appear live as a pull quote on a real magazine page, "You're writing page x of 40", "Keep page" puts it in her Issue. She writes, Lucky Star designs (Megan asked Oct 15 if this fits "the idea that AI creates the magazine for her": yes; Lucky Star picks the layout from Megan's set, the image, the page position and writes the small headline; her words stay her own, as magazine-ai-spec.md requires; "↻ Another look" tries another layout) · 09 You + settings list · 10 Lucky Star (Megan's look, dreamy glass buttons) · 11 Ready to print · 12 Place an order · 13 Edit a page · 14 Delete account.
✅ Lucky Star ideas 1–4 approved (Megan, Oct 15: "yes"): half sheet inside features (full screen on Home) · the pink fade breathes as the loading state · "Made from" tags · pink dot on the 11 (max once a day) + hold the 11 to talk. **Design is ready.** Print purchase: design/PRINT-PURCHASE.md.
**More screens (Oct 15, Megan: "Can you give me the app icon and widget pages? and all other pages that we haven't worked on yet today?"):** App icon & widgets (her 6 icons from 07 + Stickers/Dreamy glass) · Notifications (per-reminder switches, times, quiet hours, preview) · Membership ($9.99/mo, Manage or cancel → App Store, Restore, My print orders; yearly TBD) · Lucky Star & AI (switch, what it reads, memory, clear memory, data; copy to verify against the AI provider terms) · Pick this week's move · Order status (Placed → Printing → Shipped → On its way, honest estimates, help) · Safety screen on full red background (Megan, Oct 15: "when she's not okay I think should be RED (the background)" + "red but white color font, not cream" + white number cards; 988 call/text, 911, help outside the US; copy to verify) · First-day states: Issue = all 40 pages at a glance, 8 filled + 32 dashed and labeled, page 9 glowing pink, "Fill page 9 · your first move" (Megan, Oct 15: "8A is best").
The detailed sections below are the history of how we got here; where they differ, this block wins.

## The test for every screen
Does she need it on day one to feel the core loop? **Build her World → write → get her Issue → one small move a week → proof.**
And: does onboarding promise it? (Audio, one move a week, proof, Lucky Star "helps you create your Issue, build your practice and decide what to do next", app icon, notifications.) Promised = stays.

## V1 = only these screens (14 + system states)
| Tab | Screen | V1 version (simplest that still keeps the promise) |
|---|---|---|
| **Home** | 1. Home | 3 blocks only: **"Today" story rings** (today's line, her move, a flashback, her new page) · her cover (tap → Issue) · this week's move. Lucky Star's "one next thing" is the first ring. |
| | 2. Add proof | After "I made room for it": one short line of text → save. |
| | 3. "It's real" | Celebration (red full-bleed 11). Proof goes into her Issue's Proof page. |
| | 4. Pick this week's move | Shown when the week has no move: her last move + 3 written suggestions for her topic + "write my own". |
| **Explore** | 5. Explore | Top switch **Sessions · My World**. Sessions: Megan's pre-made sessions, "For you" first. My World: her own photos (iPhone picker) + saved presets. |
| | 6. Player | One full-screen player. **Watch** = her visuals; **Listen** = dark screen (this *is* "eyes closed"). Ends on "How do you feel now?" → Journal. |
| **Issue** | 7. Issue reader | Swipe her pages. "14 of 40 pages · 26 to print" + "Issue 02 in [month]". Share a page as an image (iOS share sheet). |
| | 8. Adjust | 4 controls: cover style · mood (her worlds) · her words in/out · **"Update my Issue"** (pulls in new Journal lines and proof). |
| **Journal** | 9. Journal | Today's prompt (refresh for another) · write (iOS keyboard mic for voice) · "Put this in my Issue" toggle, OFF by default · past entries. |
| **You** | 10. You | Past proof · notifications (on/off + time) · app icon · membership (manage, **restore purchases**) · **Lucky Star & AI on/off** · privacy policy + terms · sign out · **delete account**. |
| | 11. Delete account | Confirm screen; deletes everything, generated Issues and her uploaded photos included (Apple 5.1.1(v)). |
| **The 11** | 12. Lucky Star sheet | Small sheet with **one action for the screen she's on** (see below). Preview → KEEP / TRY AGAIN. |
| | 13. AI off state | When AI is off, the 11 says so kindly and the app still works (template Issue, written suggestions). |
| **All** | 14. Paywall (re-shown) | Same locked paywall if her membership ends. Restore + Terms + Privacy under the button. |
| | System states | Empty (each tab) · loading ("Lucky Star is building") · offline ("You're offline, your Issue is saved") · error. |

## Familiar on first tap (Megan, Oct 14: "make it intuitive and familiar, think: tiktok, Instagram, Pinterest" · "or even ChatGPT or Claude")
We borrow **gestures and patterns people already know**, never those apps' look or social mechanics. Our design stays.
| Screen | Pattern she already knows | How it works in ISSUE11 |
|---|---|---|
| Tab bar | Instagram / TikTok | 5 icons at the bottom; **Issue in the centre** like TikTok's "+". |
| Explore | TikTok top tabs + Pinterest | Top switch **Sessions · My World**. |
| Sessions | TikTok vertical feed | Full-screen session previews, **swipe up for the next one**, tap to play. A short, finite list (7), not an endless feed. |
| My World | Pinterest | Masonry grid of images; **tap the pin/heart to save** to her World. Saved ones show first. |
| Issue reader | Instagram Stories | **Tap right/left to turn pages**, thin page bars at the top, hold to pause. Swipe down to close. |
| Adjust Issue | Instagram edit tools | One row of icons under the page: Cover · Mood · Words · Update. |
| Add proof | Posting a story | "+ Add proof" → write one line → **Share to my Issue** → "It's real". |
| You | Instagram profile + Megan's V1 settings list | Her name + Issue on top, a **row of her proof**, then Megan's big settings list (Megan, Oct 14: "I do miss the last screen we used to have though... with all the settings"). |
| Journal | Story question sticker | Today's prompt as a big card; **swipe it away for another**; write underneath. |
| Lucky Star sheet | ChatGPT / Claude composer | A text box with a mic at the bottom + **2–3 suggestion chips** above it ("Pick a session for me"). Each answer is **one card** with KEEP / TRY AGAIN, not a long chat thread. |
| Save anywhere | Instagram | **Double-tap** an image or session to save it. |

**What we don't borrow:** likes, followers, counts, public posts, comments, endless feeds, streaks, notification badges that guilt. No public sharing also means no moderation system (Apple 1.2).

**Lucky Star in V1: ✅ DECIDED by Megan, Oct 14 ("this is the answer for Lucky Star (#1)"), her design in design/claude-design/lucky-star-v1/.** Full-screen aura sheet, one big card + 1–2 buttons, "Talk to Lucky Star…" bar with mic, AI label, Undo on every action. Megan (Oct 14): "You can use your UI/UX skill for Lucky star too.. I just like the pink gradient and how the screen looks" → Design Room designed screens A–G in the mockup (guide, hold to talk, one-card answer, curate, picked session, saved + undo, AI off). Rules: one card never a thread · "Why this?" names her own words · nothing without her tap, Undo 5 s · top label shows the screen · safety words stop it · works with AI off. Per screen:
Home → the "one next thing" card (no move yet → pick a move · move done, no proof → add proof · otherwise → today's session) · Explore → "Pick a session for me" · Journal → "Ask me a question" (one gentle question about what she wrote, never words put in her mouth) · Issue → "Try another version of this page" · World → "Find images for my topic".
Safety stays: "AI can make mistakes" label, crisis words stop the AI and show help, no health/money advice, nothing saved without KEEP.

## Why she comes back (Megan, Oct 14: "make the app addictive in a good way... making users wanting to come back" · "But still keeping the visual identity I created")
Mockup in Megan's V4 look: https://claude.ai/artifact/QAbmsD9o7zGGY5qKHAQuFX (source: design/claude-design/v1-simplified/index.html).
A magazine rhythm. Every hook reuses a V1 feature, so none of them adds build time:
- **Every day, 1 minute: "Today" story ring on Home.** 3 Stories cards: a line in her world on one of her images, her move, and a flashback. The pink ring means "new for you". Lines come from the strings file.
- **Every week: her Issue grows a page.** Move → proof → a new page (pink "New" on the Issue). Plus a flashback to her own Journal words from 30+ days ago.
- **Every 3 months: the next Issue reveal.** A countdown on her cover ("Issue 02 in 78 days").
- **Never:** streaks that break, guilt notifications, endless feeds, likes or counts, fake urgency, red badges. If she misses a week, nothing is lost.

## Her Issue = 40 pages to print (Megan, Oct 14, word for word: "The magazine must have 40 pages to print")
Day one she has 8 pages ("started", never "ready"). The rest fills over the quarter from what she already does in the app, in Megan's approved layouts (design/magazine-ai-spec.md). At 40 pages it's ready to print. Her own V4 Home already had this mechanic ("7 of 11 pages · 4 to print").
| Pages | Section | Comes from | When |
|---|---|---|---|
| 1 | Cover | Name, cover style, topic (onboarding) | Day 1 |
| 2 | Contents | Auto | Day 1 |
| 3 | Editor's letter | Her dream-life sentence (onboarding 27) | Day 1 |
| 4–5 | Her vision (spread) | Topic, feelings, celebrities' energy (onboarding) | Day 1 |
| 6–7 | Her world (spread) | Aesthetic picks (onboarding 25) | Day 1 |
| 8 | First proof | Onboarding 28 | Day 1 |
| 9–21 | Moves + proof (13 pages) | One per week: her move + what happened | Weekly |
| 22–27 | My World (6 pages) | Her own photos + saved presets (a new page every 6 saves) | As she saves |
| 28–33 | In her words (6 pages) | Journal lines she switched on | As she writes |
| 34–35 | Her rituals | Sessions she did + her affirmations | Over the quarter |
| 36–37 | Wrote it / did it | Flashbacks that came true | Over the quarter |
| 38 | Note to next-Issue her | One question from Lucky Star, her answer | Last month |
| 39 | Coming next | Teaser for Issue 02 | Auto |
| 40 | Back cover | Her closing line | Auto |
**Never short of pages:** if she reaches the end of the quarter with gaps, Lucky Star offers to fill them from her own World and Megan's editorial pages (full-bleed preset images, affirmation pages). She approves each page. Nothing invented about her.
**On screen:** cover progress "14 of 40 pages · 26 to print". At 40: "Ready to print" (cover reveal moment).
⚠️ Check with the print partner: is 40 an exact count or a minimum, and does it count the cover? (Saddle-stitched magazines need multiples of 4; 40 works.) Printing = physical goods paid outside Apple (e.g. Stripe) + shipping addresses → Megan approves that spec before building (CLAUDE.md rule 4).

**Print ordering in the Issue tab (Megan, Oct 14, word for word: "in the "Issue" section we need to add the shopping or "place an order" button once they agree on the magazine layout").** Flow: 40 of 40 → **Ready to print** (grid of all 40 pages; tap a page to swap photo, edit text or pick another of Megan's layouts) → **"I love it · Approve my Issue"** → **Order my print** (copies, address, shipping, Apple Pay → "Place my order"). The order button appears only after she approves. Price and shipping are TBD (Revenue + Megan). Physical goods are paid outside Apple in-app purchase (e.g. Stripe + Apple Pay); verify the current App Store rule at build start. ⚠️ Payments + shipping addresses → Megan approves that spec before building.
**Print price + shipping (Megan, Oct 14, word for word: "price is 29.99 for the issue... Shipping is free however takes 14 days faster shipping is more").** Order screen: Issue 01 · 40 pages $29.99 · Standard shipping free, 11–14 business days (pre-selected) · Expedited 6–9 business days +$15.99 (proposed) · Total. The pay button stays Apple's official black Apple Pay button (Apple's rule, not our glass). Still needs: the faster-shipping price, and Megan's OK of the payment/shipping spec before building (CLAUDE.md rule 4).
**➡️ Superseded by design/PRINT-PURCHASE.md (Megan's purchase-flow spec, Oct 15): Standard free · Expedited +$16 · Express +$32; PO box/APO/FPO = Standard or Priority +$10; paid inside the app; "Ready to print · x of 40" button.** History: **Lulu shipping (Megan, Oct 15; one 40-page issue, US):** free standard = Mail | Trackable, 11–14 business days, costs us $5.69. Add-ons above that: Ground 9–12 days +$8.05 · Priority Mail 9–12 days +$9.05 · Expedited 6–9 days +$15.05 · Express 5–8 days +$30.05.
Design Room recommendation: show only 2 choices. **Free · 11–14 business days** (selected) and **Expedited · 6–9 business days · +$15.99** (covers the $15.05 add-on + the card fee on it). Ground/Priority save only ~2 days; Express saves 1 day over Expedited for double the price. Fewer choices = faster checkout. Waiting for Megan's OK on $15.99.
⚠️ Still unknown: Lulu's print cost per 40-page issue (needed for her margin on $29.99), international shipping, and sales tax. Lulu prices change: re-check before launch.
**Lulu rules for the app (Megan, Oct 15):** prices are "starting at" for a US address, tax not included · estimates aren't guaranteed · printing takes 3–5 business days on top and can't be rushed · PO boxes and APO/FPO addresses can only use Mail or Priority · Hawaii, Alaska and Puerto Rico take longer.
In the app: show total arrival time including printing (Free ≈ 3–4 weeks = 14–19 business days; Expedited ≈ 2–3 weeks = 9–14 business days), label it an estimate, "$29.99 + tax" (tax calculated at checkout), hide Expedited for PO box/APO/FPO, add a "takes longer" note for HI/AK/PR. US addresses only at launch.
⚠️ Because Lulu prices are "starting at", our $15.99 Expedited and free standard may cost more for HI/AK/PR: decide whether to charge the real rate there or absorb it. Order confirmation email/screen should repeat the estimate (no promised date).
**Who makes the magazine: ✅ Lucky Star (Megan, Oct 14, word for word: "ok Lucky Star makes the magazine then").** Design Room reasoning: Lucky Star drafts it on Megan's layouts (approved Oct 9, design/magazine-ai-spec.md); she directs with tap-to-edit per page (photo, text, layout from Megan's set, "Try another version"). No Canva-style free editor on the phone: 40 pages is too much work on a small screen, free layouts break print quality (bleed, low-res photos, text overflow), and a blank canvas feels like homework. Stickers as a light personal layer = V1.1.

**Lucky Star UX ideas (Design Room, Oct 14) · ✅ approved by Megan Oct 15.** Megan: "I am open for UI/UX changes as long as we keep the 11 sticker and the pink fade". 1) Half sheet inside features (full screen stays for Home) · 2) The pink fade breathes as the loading state + one mono line "Reading your Journal…" · 3) "Made from" pink tags showing which of her things it used · 4) Pink dot on the floating 11 (max once a day, no numbers) + hold the 11 to talk.

**Lucky Star buttons: B+ "Dreamy" (Megan, Oct 14: "I actually like "dreamy""):** all liquid glass; the main action is pink-tinted glass.
**Explore player, Spotify-style (Megan, Oct 14: "there is a meditation/listening/immersive visual experience... Think Spotify, when they're listening to a meditation that is inside "Explore"")**, built from Megan's V4 Immersive + Eyes-closed screens: A session page (image, title, length, "Picked for you", Watch/Listen, pink play, what you'll rehearse, up next) · B Now playing (video + live words like lyrics, scrubber, ±15 s, save, Watch/Listen glass, swipe down → mini player) · C Listen = eyes-closed screen, plays with the phone locked + lock-screen controls · D "How do you feel now?" glass chips → Journal.
**Explore = one feed with chips (proposal, Oct 14).** Megan: "I also wonder if the meditations could be part of explore as long as they have a (play) in front of their image... I kind if want to simplify it but also find a way to organize it and make it familiar too". Design Room: one Pinterest-style grid mixing images and sessions (sessions show the pink ▶, name and length; images show the heart), like Instagram Explore. Search on top + one chip row: For you · Sessions · My World · her topics. "My World" chip = her own photos + hearted images + saved sessions, with "+ Add your photo". Replaces the Sessions/My World top switch and the TikTok vertical feed. Tap ▶ → session page → player.
**Cover reveal (Megan, Oct 14: "I need something more wow"):** 3 animated options in the mockup: A the press (pages riffle, cover lands, 11 stamps on) · B the sticker peel (she peels Megan's red full-bleed 11 to reveal her cover) · C paparazzi (camera flashes, "Cover star: [name]", pays off onboarding screen 2). ✅ **Megan picked B, the sticker peel** (Oct 14: "ok for the issue reveal i like B").
**Widgets ✅ (Megan, Oct 15: "I think widget wise we should let the users pick, just like the app ... I like option 2 and 3"):** she chooses a style, like her app icon: Stickers (B) or Dreamy glass (C), in You → "App icon & widgets" or long-press → Edit widget → Style. V1.1. Earlier draft: **Widgets (Megan: "the widgets need to be prettier too"):** large = her cover as a mini magazine (wavy masthead, 40 page ticks, "14 of 40 · 26 to print") · small = the 11 in the pink fade ("Lucky Star has one thing for you") · small = her move in dreamy glass · lock screen = 14/40 ring + today's line. V1.1.
**Around the app (Design Room suggestions, Oct 14):** cover reveal on first open ("Your Issue has started · 8 of 40") · glass mini player above the tabs · teaching empty states ("4 more saves = 1 new page") · iPhone widgets (V1.1) · dreamy glass buttons app-wide · gentle haptics · paper page-turn in the Issue.

## SIMPLIFY (keep the feature, build the easy version)
| Item | Was | V1 | Why |
|---|---|---|---|
| Home | 5 blocks (cover, move, session, inspiration image, Lucky Star note) | 3 blocks | The Lucky Star card already routes to the session; the cover is already the image. Less to build, calmer screen. |
| Lucky Star Home GUIDE | AI reads everything and picks one next thing | 3 simple rules pick it; AI only words it (written lines if AI is off) | Same promise, works offline and with AI off, no prompt tuning before launch. |
| Weekly move | Lucky Star invents one each week | Week 1 = her onboarding answer. After that: 3 written suggestions per topic + "write my own" (AI suggestion if AI on) | Content team writes ~21 lines once; no AI needed to keep the loop alive. |
| Proof | Note or photo | Short text, optional photo | Same photo picker as My World, so photo proof costs almost nothing extra. |
| Sessions | Grouped by goal; separate eyes-closed mode | One list; Listen mode = eyes closed | One player, one screen fewer. |
| Journal | Prompts + gratitude types; custom voice recording | One prompt list (gratitude prompts mixed in); iOS dictation for voice | No audio recording, storage or transcription to build. |
| Issue editing | Free prompting ("change this page") + page editor (layouts, colours, stickers, patterns, drag) | 4 adjust controls + "Try another version" | Free prompting and a drag editor are the two hardest things in the whole app. Megan's layouts stay the hero. |
| Issue updates | Rebuilds itself live | One "Update my Issue" button | She stays in control; fewer surprises; simpler to build. |
| Download | "Download my Issue" (PDF) | Share a page as an image | Share sheet is easy, native (helps Apple 4.2) and free marketing. |
| You | Intention, stats, ritual history, profile | Past proof + settings | "This week's intention" = the move (duplicate). No stats or streaks (our own rule). |
| Offline | Offline basics | Saved Issue + "You're offline" message | Downloadable sessions later. |

## LATER (V1.1+), with the reason
| Item | When | Reason to wait |
|---|---|---|
| Lucky Star long conversations (chat thread) | V1.1 | Hardest to make safe and on-voice; the box + action cards keep the onboarding promise. **Megan decides (Q1).** |
| Stickers + patterns on pages | V1.1 | A fun personal layer; tap-to-edit (photo, text, layout) is in V1 for print. |
| Issue 2, 3, 4 + rhythm setting (1/2/4/12 a year) | V1.1 (before March) | First users reach Issue 2 around March. V1 shows "next one in [month]" only. |
| Print ordering (40-page Issue) | Megan to confirm: Dec 11 or right after | Needs print partner, Stripe payment and shipping spec. The 40-page count shows from day one either way. |
| Downloadable sessions (offline audio) | V1.1 | Nice to have. |
| Spread view for iPhone Duo | V1.1 | Featuring idea, not needed to launch. V1 must still use flexible layouts (no fixed widths). |
| Streak calendar / ritual history | Not planned | Against our own "no streaks, no guilt" rule. |
| AI-generated images in Megan's look | V2 (premium) | Already decided Oct 9. |

## Kept for Apple (never cut)
Sign in with Apple (onboarding 38) · restore purchases · manage subscription · delete account in the app · privacy policy + terms links · AI consent (onboarding 34) + Lucky Star & AI off switch · "AI can make mistakes" · crisis-word help · every permission asked only when needed · no "coming soon" or placeholders in the January build (anything unfinished is hidden, not teased).

## Megan's 3 decisions (all made Oct 14)
1. ✅ **Lucky Star: decided** (Megan's 5 screens, Oct 14).
2. ✅ **Sessions: decided.** Megan, Oct 14, word for word: "Pick one of the sessions (they are pre-designed for quality control)". Lucky Star picks one of Megan's pre-made sessions and says why; copy says "picked for you", never "made". AI-made sessions are not planned.
3. ✅ **Her own photos: in V1.** Megan, Oct 14, word for word: "yes she definitely can upload her own images... She can also pick from our pre-set images as well". My World = presets + her own photos (iPhone photo picker, no full-library access). ⚠️ Storing her photos is user data → Megan approves a short photo-storage spec before it is built (CLAUDE.md rule 4): where they are kept, who can see them, how she deletes them.

⚠️ Still needs Megan's approval before building, whatever she decides: design/magazine-ai-spec.md (journal text → AI), payments/RevenueCat, sign in, delete account (CLAUDE.md rule 4).
