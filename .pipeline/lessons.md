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
- 2026-10-04 · 💚 GROWTH (ASO Scout) · Marketplace plugins installed in the Claude desktop app don't reach cloud Code sessions. Megan uploaded the zip; the skill now lives in `.claude/skills/aso-specialist/` (MIT). Next time: check `.claude/skills/` first, and ask for the plugin zip right away instead of retrying the plugin list.
- 2026-10-04 · 💚 GROWTH (ASO Scout) · Re-checking metadata against Apple's own docs (developer.apple.com is reachable; the App Store and iTunes API are not) caught 2 real issues: "goals" contradicts the locked architecture, and the Mexico keywords repeated US words. Always run a duplicate-word script across both listings, not just within each one.
- 2026-10-05 · 💚 GROWTH (Opportunity Scout) · SplitMetrics, AppGoblin, ScreensDesign and apps.apple.com are all egress-blocked; search-result snippets were the only source of ratings and revenue ranges. Next time: skip direct fetches of those domains and spend the budget on targeted searches like "<app> AppGoblin revenue".
- 2026-10-05 · Manager · Expo's create-expo-app template already ships Claude Code setup (issue11/.claude/settings.json enables expo@claude-plugins-official + AGENTS.md). Cloud rooms can't reach Megan's phone (ngrok tunnel times out): verify with `expo start --web` + a Playwright iPhone screenshot, and use EAS builds (needs EXPO_TOKEN env var) for real device tests.
- 2026-10-06 · Planner · Scope changed 4 times during one planning run (onboarding out, Your World mechanics only, Scribe prompts out then back in). Re-read request.md after every update and patch the spec in place; Manager: ask "what's final?" before starting the Planner.
- 2026-10-06 · Planner · Wording still being drafted (prompts, copy) goes in data (a DB table or one strings file), so it changes without code or an app release.
- 2026-10-06 · Manager · Megan (word for word): "i have a EIN already remember". Rule: before listing setup steps, check the Roadmap for what she already has; never re-list a done item.
- 2026-10-07 · Manager · Megan (word for word): "in the future, instead of leading me towards a difficult path (like using claude + expo...) if there is any easier path it should be recommended to me... I discovered by myself that I could use replit. So in the future, ALWAYS suggest the easiest path or the path of least resistance". I compared Lovable/Despia/Base44 but never checked Replit (its mobile builder uses Expo under the hood and has guided App Store publishing). Rule promoted to CLAUDE.md #11.

## Suggestions
Format: `- YYYY-MM-DD · <agent> · <what> · why · cost`
- 2026-10-01 · Launch Prep Room · 💡 Suggestion · A one-page "Launch calendar" (Oct 1 → Jan 11: grant, socials, holding page, recordings, beta, nomination, App Review) in the repo · why: dates now live in 6 files and two of them disagree (Hey Helen Oct vs Nov) · cost: 15 min, one agent run.
- 2026-10-02 · Design Room · Megan (word for word): "The chat isn't the feature. The actions it can take are the feature." Rule: AI features in ISSUE11 are contextual, action-first and editorial (never a ChatGPT-style chat). Every AI answer must create or change something real.
- 2026-10-03 · Design Room · Megan locked the architecture: "Do not redesign ISSUE11 around Lucky Star. Keep the original app simple." I had drifted toward adding stage labels and an actions area. Rule: new ideas plug into the 4 functions (Your World · Audio · Scribe · Publish); never add sections, task lists or visible frameworks without Megan asking.
- 2026-10-03 · Design Room · Megan defined Lucky Star in one line: "It understands where you are between DESIRE and BECOME and guides you toward what you need next. When you're inside a feature, Lucky Star helps you use that feature." Rule: no generic AI menus; Home = GUIDE (one next thing), features = ASSIST (context only). No new Lucky Star responsibilities for V1.
- 2026-10-03 · Design Room · Megan (word for word): "I don't know why but adding AI feature inside the app is overwhelming to me." Lucky Star moved to V2. Lesson: when ideas pile up fast, pause and offer the smallest version before specifying more; scope creep overwhelms the founder before it overwhelms the build.
- 2026-10-03 · Design Room · Megan asked to inspect the codebase before designing Lucky Star; there is no app code yet. Rule: say that plainly and map the prototype + specs as the "current architecture" instead of inventing one.
- 2026-10-03 · Design Room · Megan's tone and context rules ("PERSONALIZED WITHOUT HALLUCINATING", "Nurturing does not mean sycophantic") only hold if code checks them. Rule: every AI behavior rule gets an enforcement line (code check, schema or eval), never prompt-only.
- 2026-10-05 · 🩷 EXTERNAL (AEO) · Plugin zips install fine as project skills once `${CLAUDE_PLUGIN_ROOT}` and cross-skill imports are re-pointed; smoke-test each script after moving. Prefix third-party skill names (SearchFit had `seo-audit` like Ultimate) so they don't clash.
- 2026-10-05 · 🩷 EXTERNAL (AEO) · Read third-party skills for trust problems, not just security: one had a "republish to look fresh" trick and every SearchFit skill pushed its paid product. Strip those lines before install and log every edit in `.claude/vendor/INSTALLED-SKILLS.md`.
