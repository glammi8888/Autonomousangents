# ISSUE11 · UI/UX laws & principles audit (Design Room, Oct 15, 2026)
Megan's brief: review the whole app against the core UX laws, Gestalt, cognitive psychology, behavioral design, Nielsen's heuristics, IA and WCAG 2.2 AA. Recommend only where it helps; keep the brand, the editorial look and the functionality. **No changes made. Nothing applied until Megan approves.**
Scope reviewed: the approved V1 mockup (https://claude.ai/artifact/QAbmsD9o7zGGY5qKHAQuFX), drafts/replit/handoff/01-app-flow-prompt.md, onboarding v3 (locked, read-only), design/claude-design/system-states.

## Part 1 · What's already strong (keep)
| Area | Principles already working | Where |
|---|---|---|
| Familiarity | Jakob's Law, Law of Past Experience, Mental Models | Stories, Pinterest grid, Spotify player, Apple Pay, IG profile |
| Progress & motivation | Goal-Gradient, Endowed Progress (starts at 8/40), Zeigarnik (dashed empty pages), Visibility of System Status | "14 of 40", final stretch, 40-page grid, order status |
| Memorable moments | Peak-End Rule, Emotional Design, Von Restorff | Sticker peel, "It's real", monthly recap, arrival photo |
| Habit | Habit Loop, Fogg (prompt + tiny ability + motivation), Fresh Start (Monday move, monthly recap, Issue 02), Variable Reward (stories, stickers, flashbacks), Mere Exposure (daily story, widgets) | Home, notifications, Lucky Star |
| Ownership | IKEA Effect, Endowment, Self-Determination (autonomy: choose/write your own move) | Edit a page, Journal "Keep page", proof |
| Control | Forgiveness, User Control & Freedom, Default Effect (Standard shipping preselected, AI on with an off switch) | Undo toasts, Not now, AI off |
| Complexity | Tesler's Law (Lucky Star absorbs layout work), Occam's Razor, Minimum Viable Complexity | Lucky Star makes the magazine |
| Speed | Doherty Threshold (preload, breathing-glow state), Parkinson's Law (Apple Pay checkout) | UX rules, Lucky Star |
| Onboarding | Progressive Onboarding, Paradox of the Active User (max 3 one-time tips, no tour) | UX rules |
| Ethics | No streak loss, no fake urgency, no fake social proof | Trust rules |

## Part 2 · Recommendations (ranked by impact)
| # | Issue found | Principles | Recommendation | Benefit | Effort |
|---|---|---|---|---|---|
| 1 | **Pink text and white-on-pink buttons fail contrast.** Measured: pink #F65AAD on white = 3.0:1; white on pink buttons = 3.0:1 (AA needs 4.5:1 for small text). Grey #8A8A8A on white = 3.5:1; #BDBDBD placeholders = 1.9:1. Pink on cream = 2.6:1. | WCAG 2.2 AA (Perceivable), Contrast Principle | Keep the brand pink for glows, fills, big headlines and dots. For **small text** use ink, or a deeper text-pink (#C2207E = 5.5:1). On pink buttons, make the label **ink** (≈7:1) or bold ≥14pt white. Replace #8A8A8A captions with #6B6762 (5.6:1). | Readable for everyone; passes Apple review; the look stays pink | Small (tokens) |
| 2 | **Journal: the keyboard will hide the live page.** With the keyboard up, the magazine page plus the text bar won't fit, so she can't see her words appear. | Direct Manipulation, Mapping, Feedback | Let her **tap the page and type on it directly**; while typing, the page scales to fit above the keyboard. Remove the separate text bar. | The wow moment actually works on a real phone | Medium |
| 3 | **Issue reader borrows Stories but a magazine shouldn't auto-advance.** Stories timers + "hold to pause" don't fit reading; 40 thin bars are tiny. Edit icons + share + Ready to print + 11 crowd the bottom. | Jakob's Law (right model), Progressive Disclosure, Aesthetic-Minimalist, Fitts's Law | Swipe or tap edges to turn pages, **no timer**; replace 40 bars with "p.15 / 40". Put the edit tools behind one **"Edit"** button. | Calm reading, bigger targets, cleaner pages | Small |
| 4 | **Disabled "Ready to print" button at 15/40.** Grey buttons that do nothing confuse people. | Affordances, Signifiers, Error Prevention, Information Scent | Show it as a **progress pill** ("25 pages to print"); tapping explains how to fill the next page and jumps there. Becomes a real button at 40. | No dead taps; guides her to the next page | Small |
| 5 | **The floating 11 covers content** (cards, last row of grids, buttons) and sits on full-screen moments. | Fitts's Law, Figure-Ground, Law of Focal Point | Hide the 11 on full-screen moments (stories, player, peel, safety, checkout, Lucky Star itself); add bottom padding on scroll screens so nothing hides under it. | Nothing blocked; the 11 stays special | Small |
| 6 | **Weekly move has no "when".** | Implementation Intentions, Commitment & Consistency, Fogg (prompt) | After "Keep my move": one optional row "When? Mon · Tue · … · Morning/Evening", which sets that reminder. | Strongest research-backed lift for follow-through, still no to-do list | Small |
| 7 | **Home repeats itself.** "Your move", "Flashback" and "New page" appear as story bubbles **and** as cards/strips below. | Hick's Law, Occam's Razor, Choice Overload, Serial Position | Story bubbles = only what's new today (Today + whatever is new). The cards below are the permanent home for move, flashback, World, latest pages. | Shorter, clearer Home; each thing has one place | Small |
| 8 | **Tab bar: 9px mono labels, active tab shown only by a 4px pink dot.** | Touch Target Accessibility (44pt), WCAG non-text contrast / not color alone, Recognition over Recall | Labels ≥11pt; active tab = **ink + bold** plus the dot; each tab target ≥44pt. (Optional: tiny icons above labels.) | Easier to read and hit; clear "where am I" | Small |
| 9 | **No help or support path** (needed for print orders; Apple requires a support URL). My Issues only reachable from the You header. | Help & Documentation, Wayfinding, Information Scent | Add two rows to the You list: **"My Issues"** and **"Help & support"** (FAQ + contact). | Users and Apple find help; shelf easy to find | Small |
| 10 | **What happens to her Issues if she cancels?** Unstated. | Trust, Loss Aversion (used ethically), Endowment | One line on Membership: "Your Issues stay yours to read, even if you cancel." Never use fear-of-loss in cancel flows. | Trust; fewer support tickets; Apple-safe | Tiny |
| 11 | **Motion-heavy moments** (peel, breathing glow, page turns, sliding covers, cover glow). | Reduced Motion (WCAG 2.3.3), Multiple Means of Interaction | With iPhone "Reduce Motion" on: crossfades instead of peel/slide/turn, static glow. Every gesture also has a tap (peel already does; hold-the-11 also via the mic button). | Comfortable for motion-sensitive users | Small |
| 12 | **Too much pink competing on some screens** (rings, tags, dots, buttons, glows together). | Von Restorff, Law of Focal Point, Figure-Ground | Rule: **one pink hero per screen** (the main action or the newest thing); other accents ink/cream. | Eyes go straight to what matters; feels more premium | Small (rule) |
| 13 | **Glass buttons with white text over busy photos** (player, cover, peel). | Figure-Ground, Contrast | Always a soft dark scrim behind glass on photos. | Buttons readable on any image | Tiny |
| 14 | **Huge Archivo Black headlines with large iPhone text sizes** can overflow. | Robust, Dynamic Type | Body/labels scale; headlines scale up to a cap and wrap; never truncate her words. | Works for low-vision users without breaking the look | Small |
| 15 | **Checkout error prevention.** | Error Prevention, Constraint Principle, Postel's Law | Address autocomplete + validation; detect PO box/APO before showing options (already specced); a short "review your order" summary in the Apple Pay sheet; clear what's editable after ordering. | Fewer failed or wrong prints | Small |
| 16 | **Lucky Star waits.** | Doherty Threshold, Visibility of System Status | Stream the answer card in as it's written (after the breathing "Reading your…" line); if over ~8 s, offer "Keep browsing, I'll tap you when it's ready". | Feels instant; never stuck | Small |

### Considered and not recommended (would hurt or isn't relevant)
- **Social proof inside the app:** no real data yet and it would break the "about her" feeling; use real reviews on the App Store page later.
- **Loss aversion / streaks / scarcity:** against ISSUE11's trust rules.
- **Breadcrumbs:** a 5-tab mobile app with shallow screens doesn't need them; clear titles + back gesture are enough.
- **Three-click rule:** already met (everything is ≤3 taps from a tab).
- **Card sorting:** worth a 10-minute test with 5 beta users on the Explore chips and You list, not a design change now.
- **Amdahl's Law:** a performance/engineering concern; covered by "preload the next story/page".

## Part 3 · Suggested order
Approve 1, 2, 3, 5, 8 first (accessibility + real-phone usability, all small except the Journal). Then 4, 6, 7, 9, 10. The rest are rules the Replit prompt can carry.

## Megan's decisions (Oct 15)
Word for word: "1. yes 2. no 3. yes but keep 11 luckystar sticker 4. ABSOLUTELY NOT 5. yes"
- #1 Contrast: **applied** (text-pink #C2207E for small text, grey #6B6762, ink labels on pink buttons).
- #2 Journal typing on the page: **no**, Journal stays as designed.
- #3 Issue reader: **applied**, swipe + "p.15 / 40" + one Edit button + progress pill, **the floating 11 stays**.
- #4 Hide/move the floating 11: **no, never**. The 11 stays on every screen.
- #5 Tab bar: **applied** (11pt, current tab bold ink + dot, 44pt targets).
Word for word (Oct 15, later): "1.2 yes that sounds great BUT how do I do that in action? 1.3 No too complicated 7/ Remove the repeat 8. ok 9. ok 10. ok"
- #6 "When?" row for the weekly move: **no** ("too complicated").
- #7 Home repeat: **applied**, story bubbles = Today + New page only; move and flashback live once, as cards.
- #8 Tab bar: already applied with #5.
- #9 You rows **"My Issues"** + **"Help & support"**: **applied**.
- #10 Membership line "Your Issues stay yours to read, even if you cancel.": **applied**.
- Voice · Music slider in the player: **applied** (each session = a voice-only file + a music-only file of the same length, played together).
Not yet decided: #11–#16 (the Replit prompt carries them as rules).
