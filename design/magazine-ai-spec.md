# Spec: AI-made magazine on Megan's layouts (draft, for Megan's approval)
Design Room · Oct 1, 2026 · Status: **WAITING FOR MEGAN'S APPROVAL**. This touches **user data** (journal text goes to an AI service), so per CLAUDE.md nothing gets built before Megan approves this spec.

## Megan's decision (Oct 1, 2026)
- The magazine is made by AI, and she only does small edits.
- The desktop web editor is **dropped from V1**.
- Megan: "I do want the AI to generate the magazine based off the layouts I have sent. So it doesn't just freelance everything and does bad work."

## The rule: AI fills, it never designs
The AI **only chooses and fills** Megan's approved layouts. It never invents a layout, color, font or graphic.

| The AI may | The AI may not |
|---|---|
| Pick a cover from Megan's cover set | Create new layouts or page designs |
| Pick spreads from the approved layout library | Change fonts, sizes or spacing |
| Put her photos into a layout's photo slots | Generate or alter images of her |
| Write headlines and captions within each slot's character limit, from her own words | Invent facts, events, numbers or quotes she didn't write |
| Pick a page color from the approved theme list | Use colors outside the theme list |
| Suggest stickers from the approved sticker set | Make health or medical claims |

## Layout library (the only thing the AI can use)
From the Magazine Lab (design/magazine/index.html): 7 covers, 34 "Feature" spreads, the basic pages (Contents, Your vision, Pull quote, Your steps, Her world, The proof) and 9 Zine pages.
- **Megan's step first:** a keep/cut pass. Only layouts she marks ✅ go into the AI library.
- Each layout gets a small "slot sheet": photo slots, text slots with max characters, the tone of each slot (headline / quote / caption / body), and which themes it allows.

## How an issue gets made
1. **Input:** her name, goals, life areas, chosen images, journal entries, logged wins and saved quotes.
2. **Plan:** the AI returns a plan only: which layouts, in what order, which photo goes where, and the text for each slot.
3. **Check:** the app validates the plan:
   - Only approved layout IDs are used.
   - Text fits every slot's character limit.
   - Colors come from the theme list.
   - No banned words or health claims.
   - Quotes match her own saved text.
   If anything fails, it retries once, then falls back to a safe default issue.
4. **Render:** the app draws the pages with Megan's real layouts. The AI never draws pixels.
5. **She tweaks it:** swap a layout (between approved ones only), change a page color, edit text, add or move stickers, undo, and "Remake this page".

## Small edits kept in V1
Swap layout · page color · edit text · stickers (incl. emoji, pinch to resize) · patterns (waves, zebra, cheetah, hearts) · undo · remake page.

Cut from V1: free-form full editor and desktop editor.

## Data, privacy and trust (needs Megan's approval)
- **Consent:** a clear screen before the first issue: "Your journal entries are sent to an AI service to write your magazine." The magazine can't be made without it, and she can turn it off in Settings.
- **AI provider:** to be chosen. Pick one that does not train on user data and does not keep it. Verify its current terms before building.
- **Minimum data:** send only what the issue needs (no email, no payment data). Images stay on our storage; the AI gets photo IDs, not the photos.
- **App Store:** update the privacy labels and the AI data disclosure; account deletion also deletes generated issues. Re-check the current App Store guidelines at build start.
- **Wording:** no health claims. Every quote is attributed to her own entry.

## Cost
Each issue costs one AI call (plus a retry at most). Revenue + Megan to set the limits, e.g. issues per month per plan. Check current API prices before deciding; I'm not quoting a price here.

## Effect on the plan
- Removes the desktop editor (big time saving).
- Shrinks the phone editor to small edits.
- Adds the AI pipeline, consent screen and plan checker.
- Overall: smaller V1 than before. Flag to the Manager for re-planning.

## For Megan to approve (yes/no)
1. The "AI fills, never designs" rule and the edit list above.
2. Sending journal text to an AI service, with the consent screen and data rules above.
3. Next step: you do the keep/cut pass on the layouts in the Magazine Lab.
