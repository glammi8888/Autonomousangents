# ISSUE11 app: everything after the paywall (Design Room, Oct 9, 2026)
Megan: "So it should be everything after the paywall". Onboarding (screens 1–38) is done and saved.
Visual map: https://claude.ai/artifact/Tfe9RNTCYNHeaQagTtdyQf (screenshots of the existing screens per area).
Rules: design/PRODUCT-ARCHITECTURE.md (locked). 4 functions: Your World · Audio · Scribe · Publish. Lucky Star = the 11 sticker (GUIDE on Home, ASSIST inside features). Keep the magazine as the hero, the AI invisible until useful. Look = the onboarding v3 designed prototype (Archivo Black, mono kickers, statement screens, 11 stickers, calm "Be honest" cards).

## Map
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
