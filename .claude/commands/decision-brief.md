---
description: Chief of Staff decision brief for Megan. One recommendation, the numbers, the reasoning, 2 alternatives, risks. Adapted from Anthropic's claude-cookbooks "Chief of Staff agent" (MIT), security-checked Nov 14, 2026.
---

Write a decision brief for Megan on: $ARGUMENTS

Megan reads this on her phone and has about 30 seconds (Megan: "for each decision I want you to help me make it and the reasoning behind it").

Before writing:
- Read CLAUDE.md, `.pipeline/lessons.md` (CURRENT FACTS and RULE lines) and any repo/Notion page the topic points to. Reuse existing work; don't research what's already known.
- Only use real numbers you can point to (a file, Notion, Mangools, Apify, Meta Ads read-only, Framer analytics). If a number is missing, say what's missing. Never invent one.
- Pull in other agents only when the topic needs them (💚 Growth/Media Buyer for ads and channels, 💛 Revenue for pricing, 🎨 The Editor for design). Load the skills they need (e.g. `marketing-psychology`, `pricing`, `ads-math`).

Format (plain words, no jargon):

**RECOMMENDATION:** one sentence, what to do.

**WHY (numbers):** at most 3 bullets, each with a real number and where it came from.

**REASONING:** 2–3 sentences. Include the easiest path and the cheapest path (CLAUDE.md rule 11).

**OTHER OPTIONS:** 2 alternatives, one line each, with the trade-off.

**RISKS:** one line each. Flag anything that touches the Production Safety Rule (payments, user data, secrets, live site, store).

**NEXT STEP FOR MEGAN:** one tap-sized action, or "nothing, I'll do it" when agents can do it themselves.

After writing: if Megan answers, save her decision word for word in `.pipeline/lessons.md` and on Megan Today.
