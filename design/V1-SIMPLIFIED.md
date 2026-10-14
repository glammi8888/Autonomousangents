# ISSUE11 V1, simplified (Design Room, Oct 14, 2026) · ⏳ PROPOSAL, waiting for Megan
Megan is building in Replit and asked for a "simplify" pass on **functionality, not the look**. Our design stays exactly as is (lesson Oct 9).
**Status:** proposal only. Nothing changes in the build until Megan approves. Onboarding (design/ONBOARDING-V3.md) is locked and untouched. The 5 tabs and the 4 functions stay.
**Sources:** design/APP-AFTER-PAYWALL.md · design/PRODUCT-ARCHITECTURE.md · design/POSITIONING.md · design/LUCKY-STAR-VOICE.md · design/claude-design/V1-SCREENS.md · drafts/replit/02-app-flow-prompt.md · .pipeline/app-store-checklist.md
**Replit prompt:** drafts/replit/02b-app-flow-simplified.md

## The test for every screen
Does she need it on day one to feel the core loop? **Build her World → write → get her Issue → one small move a week → proof.**
And: does onboarding promise it? (Audio, one move a week, proof, Lucky Star "helps you create your Issue, build your practice and decide what to do next", app icon, notifications.) Promised = stays.

## V1 = only these screens (14 + system states)
| Tab | Screen | V1 version (simplest that still keeps the promise) |
|---|---|---|
| **Home** | 1. Home | 3 blocks only: her cover (tap → Issue) · **one next thing** card from Lucky Star · this week's move. |
| | 2. Add proof | After "I made room for it": one short line of text → save. |
| | 3. "It's real" | Celebration (red full-bleed 11). Proof goes into her Issue's Proof page. |
| | 4. Pick this week's move | Shown when the week has no move: her last move + 3 written suggestions for her topic + "write my own". |
| **Explore** | 5. Explore | One list of sessions ("For you" first, matched to her onboarding topic + feeling) + her World grid below. |
| | 6. Player | One full-screen player. **Watch** = her visuals; **Listen** = dark screen (this *is* "eyes closed"). Ends on "How do you feel now?" → Journal. |
| **Issue** | 7. Issue reader | Swipe her pages. "Issue 01 · next one in [month]". Share a page as an image (iOS share sheet). |
| | 8. Adjust | 4 controls: cover style · mood (her worlds) · her words in/out · **"Update my Issue"** (pulls in new Journal lines and proof). |
| **Journal** | 9. Journal | Today's prompt (refresh for another) · write (iOS keyboard mic for voice) · "Put this in my Issue" toggle, OFF by default · past entries. |
| **You** | 10. You | Past proof · notifications (on/off + time) · app icon · membership (manage, **restore purchases**) · **Lucky Star & AI on/off** · privacy policy + terms · sign out · **delete account**. |
| | 11. Delete account | Confirm screen; deletes everything, generated Issues included (Apple 5.1.1(v)). |
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
| You | Instagram profile | Her cover as the header, **grid of her proof** below, gear icon top right for settings. |
| Journal | Story question sticker | Today's prompt as a big card; **swipe it away for another**; write underneath. |
| Lucky Star sheet | ChatGPT / Claude composer | A text box with a mic at the bottom + **2–3 suggestion chips** above it ("Pick a session for me"). Each answer is **one card** with KEEP / TRY AGAIN, not a long chat thread. |
| Save anywhere | Instagram | **Double-tap** an image or session to save it. |

**What we don't borrow:** likes, followers, counts, public posts, comments, endless feeds, streaks, notification badges that guilt. No public sharing also means no moderation system (Apple 1.2).

**Lucky Star in V1 (chips + a box, answers as cards):**
Home → the "one next thing" card (no move yet → pick a move · move done, no proof → add proof · otherwise → today's session) · Explore → "Pick a session for me" · Journal → "Ask me a question" (one gentle question about what she wrote, never words put in her mouth) · Issue → "Try another version of this page" · World → "Find images for my topic".
Safety stays: "AI can make mistakes" label, crisis words stop the AI and show help, no health/money advice, nothing saved without KEEP.

## SIMPLIFY (keep the feature, build the easy version)
| Item | Was | V1 | Why |
|---|---|---|---|
| Home | 5 blocks (cover, move, session, inspiration image, Lucky Star note) | 3 blocks | The Lucky Star card already routes to the session; the cover is already the image. Less to build, calmer screen. |
| Lucky Star Home GUIDE | AI reads everything and picks one next thing | 3 simple rules pick it; AI only words it (written lines if AI is off) | Same promise, works offline and with AI off, no prompt tuning before launch. |
| Weekly move | Lucky Star invents one each week | Week 1 = her onboarding answer. After that: 3 written suggestions per topic + "write my own" (AI suggestion if AI on) | Content team writes ~21 lines once; no AI needed to keep the loop alive. |
| Proof | Note or photo | Short text | No photo storage needed. Photo proof in V1.1 with own photos. |
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
| Her own photos in Your World + photo proof | V1.1 (January) | Photo storage = user data spec + privacy label + deletion. Presets carry day one. **Megan decides (Q3).** |
| Page editor (layouts, colours, stickers, patterns) | V1.1+ | Biggest build item; adjust controls cover day one. |
| Issue 2, 3, 4 + rhythm setting (1/2/4/12 a year) | V1.1 (before March) | First users reach Issue 2 around March. V1 shows "next one in [month]" only. |
| PDF download / print | V2 | Printing not confirmed; share-as-image covers sharing. |
| Downloadable sessions (offline audio) | V1.1 | Nice to have. |
| Spread view for iPhone Duo | V1.1 | Featuring idea, not needed to launch. V1 must still use flexible layouts (no fixed widths). |
| Streak calendar / ritual history | Not planned | Against our own "no streaks, no guilt" rule. |
| AI-generated images in Megan's look | V2 (premium) | Already decided Oct 9. |

## Kept for Apple (never cut)
Sign in with Apple (onboarding 38) · restore purchases · manage subscription · delete account in the app · privacy policy + terms links · AI consent (onboarding 34) + Lucky Star & AI off switch · "AI can make mistakes" · crisis-word help · every permission asked only when needed · no "coming soon" or placeholders in the January build (anything unfinished is hidden, not teased).

## 3 decisions only Megan can make
1. **Lucky Star in V1: a ChatGPT/Claude-style box with suggestion chips, where every answer is one action card (KEEP / TRY AGAIN), no long chat thread?** Recommended: yes. Familiar, keeps your Oct 2 rule ("The actions it can take are the feature"), and much safer to build than open chat. Long conversations on Home move to V1.1.
2. **Sessions at launch: 7 (one per onboarding topic), audio + a slow-moving image, each in a 5 and 10 min cut (15 min = the 10 min + 5 min of quiet music)?** Recommended: yes. Easiest for you to make; "Watch" still works.
3. **Your own photos (and photo proof) in January, not Dec 11?** Recommended: yes. Presets carry launch; it removes a user-data approval from the critical path. (Changes your Oct 9 decision.)

⚠️ Still needs Megan's approval before building, whatever she decides: design/magazine-ai-spec.md (journal text → AI), payments/RevenueCat, sign in, delete account (CLAUDE.md rule 4).
