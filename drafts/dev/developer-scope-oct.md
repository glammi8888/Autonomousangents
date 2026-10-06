# Developer scope: ISSUE11 iOS app (October–November 2026)
Draft by 🩶 Manager, Oct 6. Megan sends it; nothing is agreed until she and the developer confirm scope + price.

## Message to send (edit freely)
Hi [name]! Good news: ISSUE11 is moving into development. We're building the iPhone app with Expo (React Native, SDK 57) and Claude Code agents, who write most of the screens and tests. I'd love your help with the technical setup and the tricky native parts, plus your weekly code review.

Timeline: build Oct 9 – Nov 4 · TestFlight beta Nov 11 · App Store launch Dec 11.

Scope I have in mind (details below):
1. Supabase setup: dev project, auth (Sign in with Apple + email code), row-level security review, private photo storage
2. Sign in with Apple end to end (Apple Developer config + app)
3. RevenueCat subscriptions + paywall wiring (sandbox testing)
4. EAS builds + internal TestFlight setup
5. Unblocking: fixing issues the agents get stuck on (native modules, build errors)
6. Weekly code review (security, payments, App Store risks)

Could you share your availability in October/November, your hourly rate, and an estimate per item (or a fixed price for 1–4)? Code lives in our GitHub repo; I'll give you access once we agree.

Thank you!
Megan

## Scope details (for the developer)
| # | Item | Done when | Week |
|---|---|---|---|
| 1 | Supabase dev project + auth + RLS + private storage | Her data is visible only to her (tested with 2 accounts); photos private | Oct 9–16 |
| 2 | Sign in with Apple | Works on a real iPhone in a dev build | Oct 9–16 |
| 3 | RevenueCat + paywall | Sandbox purchase, restore, cancel all work | Oct 26 – Nov 2 |
| 4 | EAS builds + internal TestFlight | Megan installs the app from TestFlight | by Oct 21 |
| 5 | Unblocking | As needed, hourly, capped at [x] h/week | ongoing |
| 6 | Weekly code review | Short written notes in the repo each Friday | weekly |

## Rules (non-negotiable)
- Access: App Store Connect **Developer** role (not Admin), Supabase team member, GitHub collaborator. Never Megan's passwords.
- Secrets only as environment variables, never in code or chat.
- Work on `feature/*` branches; the agent pipeline (QA + Reviewer) checks his code too. No merges to main, no TestFlight/App Store submission, no live database migrations without Megan.
- Megan approves anything touching sign-in, user data, payments or account deletion before it's built.
