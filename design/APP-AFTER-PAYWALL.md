# ISSUE11 app: everything after the paywall (Design Room, Oct 9, 2026)
Megan: "So it should be everything after the paywall". Onboarding (screens 1–38) is done and saved.
Visual map: https://claude.ai/artifact/Tfe9RNTCYNHeaQagTtdyQf (screenshots of the existing screens per area).
Rules: design/PRODUCT-ARCHITECTURE.md (locked). 4 functions: Your World · Audio · Scribe · Publish. Lucky Star = the 11 sticker (GUIDE on Home, ASSIST inside features). Keep the magazine as the hero, the AI invisible until useful. Look = the onboarding v3 designed prototype (Archivo Black, mono kickers, statement screens, 11 stickers, calm "Be honest" cards).

## Combined structure (Oct 9, Megan: "ok let's do that")
**Our design stays.** Megan, word for word: "I want to keep our design though!!!!! Just the functionality of replit... Please we really worked hard on that design". Every screen keeps the ISSUE11 look (onboarding v3 designed + Megan's Claude Design screens). From Replit we take **only what the buttons and screens do**, never its colours, fonts, icons or layout.
Replit's functionality (Megan's Replit build, screenshots shared Oct 9) merged with the locked rules. This replaces the Map's navigation.

**Bottom bar (decided by Megan, Oct 9):** Home · Explore · Issue · Journal · You, plus **the 11 floating on every screen** (Lucky Star). Megan: "Let's keep our aesthetic but keeping replit's split because it's much clearer in my opinion".
The 4 functions are all there behind friendlier tab names: Audio + Your World live in **Explore**, Scribe is **Journal**, Publish is **Issue**.

| Tab | What it does | Function taken from Replit | Changed vs Replit |
|---|---|---|---|
| **Home** | Her daily edition: cover, this week's move, one session, one inspiration, one note from Lucky Star | Daily-edition sections; "I made room for it" logs the move in one tap | No DESIRE→BECOME stage tracker; move is weekly, not daily |
| **Explore** | Audio sessions by goal + your preset worlds; saving an image adds it to her World (shown at the top with her own photos) | Library by goal; save to keep a feeling | Her own photos added; retire "Become her" |
| **Issue** | Her magazine, **built by AI** from her onboarding answers, World and the Journal lines she marks, using only Megan's approved layouts (design/magazine-ai-spec.md). She reads it, then adjusts: swap the cover, change the mood (her worlds), include or leave out her words, or ask Lucky Star to change a page | Simple adjust controls (cover, mood, "your words, if you choose") | AI builds the first draft, the controls only adjust it; "Create" + sign renamed Issue |
| **Journal** | One prompt a day, typed or spoken; only lines she marks go into her Issue | Prompt + refresh + "Save to my story"; "only the lines you choose" | — |
| **You** | This week's intention, past proof, settings, membership, delete account | Intention + past proof on one page | No stage bar, no "Chapter 03", no zero counters; Lucky Star is the floating 11, not a link |

**Decided (Megan, Oct 9):** "I do think we should have AI build her magazine though". Matches the locked plan and the Oct 1 spec (AI fills Megan's layouts, never designs). **Still needs Megan's approval of design/magazine-ai-spec.md before building** (her journal text goes to an AI service = user data). Cost note: AI cost per Issue is real but small at 4 Issues a year; Revenue to check it against the price.

## Map (first version, areas)
| # | Area | Screens | Already designed (reuse) | Status |
|---|---|---|---|---|
| 1 | **First open** | Home, first-run state: her cover with her name, "Your Issue has started", her first move this week, her worlds | V4 Home | Gap: the first-run state |
| 2 | **Home (daily)** | Issue hero (cover + progress to her next Issue) · Lucky Star Guide card (one next thing) · Audio · Scribe · Your World · Publish · ritual/streak · 11 sticker | V4 Home, 12 Streak | Restyle to onboarding look; tiles renamed to the 4 functions |
| 3 | **Next Move + proof** | Weekly move card · Done → Add proof → "It's real" celebration · proof archive | V1 prototype (proof, proofdone), red full-bleed 11 | Core retention loop |
| 4 | **Publish / My Issue** | Issue reader (swipe pages) · Page editor ("change this page" by prompting) · Cover · 4 Issues a year progress | V4 My Issue, V1 page editor | Magazine = the hero |
| 5 | **Your World** | World board · Add image (presets or her own photos) · World detail | 14 Vision board, V2 In frame, design/AESTHETICS.md | New: presets + own photos (Oct 9) |
| 6 | **Scribe** | Notes list · Write (text + voice) · Empty state | V4 Notes to self | Restyle |
| 7 | **Audio** | Session library · Immersive player · Eyes-closed mode · "How do you feel now?" → Scribe | V4 Immersive player, V4 Eyes closed | Restyle |
| 8 | **Lucky Star** | Home Guide chat (text + voice) · Assist sheet inside each feature (context only, no menu) | Lucky Star aura | Copy rules: design/LUCKY-STAR-VOICE.md |
| 9 | **You** | Profile · Ritual history · App icon · Notifications · Membership (manage, restore) · Privacy · Lucky Star & AI data · Sign out · Delete account | 07 App icon picker, V1 you/delete | ⚠️ Membership, privacy, delete account need Megan's spec approval |
| 10 | **System states** | Offline · Empty states · Loading ("Lucky Star is building") · Errors · Notifications | V1 offline | Last |

## Design order (recommended)
1. **Home** (first-run + daily). It routes to everything, so the rest follows from it.
2. **Next Move + proof.** The weekly loop that makes people come back.
3. **Publish / My Issue.** The hero.
4. **Your World → Scribe → Audio.** The 3 inputs to the Issue.
5. **Lucky Star sheets.** Once the screens they sit on exist.
6. **You + system states.** Needed for the App Store (delete account, restore purchases, privacy).

## Trust rules that carry over
- Only claim what the app has actually made ("started", not "ready").
- One Next Move a week. No to-do lists, no goal tracking.
- Save to Scribe only with her permission. Preview before anything is saved.
- No health or money advice. Crisis words stop the AI and show help.
