# 📈 Pipeline lessons learned

Every pipeline agent reads this before starting and adds max 2 dated lines at the end of its step.
Format: `- YYYY-MM-DD · <Planner|Builder|QA|Reviewer> · <lesson>`
A lesson that appears twice gets promoted into that agent's file in `.claude/agents/`, and is removed here.
Allowed: better ways of working. Never allowed: weakening tests, the App Store checklist or the Production Safety Rule.

## 💗 From Megan
- 2026-10-01 · Megan, word for word: "I love my agents" 💝 · To every agent: thank you. Keep doing smart things.

## Lessons
- 2026-10-02 · Manager · Megan (word for word): "everytime an agent designed in canva for me it was a bit of a disaster". Rule: agents never design marketing visuals from scratch in Canva. Megan makes or approves master templates; agents only fill them (copy, photos, crop), then a 3-variation test before any batch.
- 2026-09-30 · Design Room · Checking the wireframes against the Notion concept found the biggest gap (no cover reveal before the paywall). Always cross-check wireframes with the concept page before designing.
- 2026-09-30 · Design Room · Megan's answers can conflict ("no audio in v1" vs "ships when the app is out"). Log my reading in design/FLOW-MAP.md and confirm it in one line instead of guessing silently.
- 2026-10-01 · Design Room · Megan (word for word): "I thought you were designing based off that" (the Canva identity kit). Rule: before any visual design, get the full identity kit pages (not the text summary) and design from them.
- 2026-10-01 · Design Room · Megan: "for the 3D stickers they don't look good" — removed. Her taste: flat, graphic, printed (patterns, stickers, emoji) over glossy 3D renders.
- 2026-10-01 · Design Room · Megan: "we nailed the functionality but the design needs refinement". The flow is locked; she refines the look in Claude Design. Next time, lock the flow first, then do the visual design as a separate pass, so Figma polish isn't spent on screens before their look is final.
- 2026-10-01 · Launch Prep Room · Trademark databases (USPTO, WIPO, EUIPO, Justia, Trademarkia) are all blocked by this environment's network. Don't retry them: do the web/App Store knockout and give Megan the 5-minute self-check steps.
- 2026-10-01 · Launch Prep Room · The local branch had drifted from origin (stale history). Always `git fetch` and work from origin/<branch> before writing, so the next pull doesn't create a messy merge.

## Suggestions
Format: `- YYYY-MM-DD · <agent> · <what> · why · cost`
- 2026-10-01 · Launch Prep Room · 💡 Suggestion · A one-page "Launch calendar" (Oct 1 → Jan 11: grant, socials, holding page, recordings, beta, nomination, App Review) in the repo · why: dates now live in 6 files and two of them disagree (Hey Helen Oct vs Nov) · cost: 15 min, one agent run.
