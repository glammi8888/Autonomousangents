# Spec: Lucky Star ★, the contextual "11" editor (draft v2, for Megan's approval)
Design Room · Oct 2, 2026 · Status: **WAITING FOR MEGAN'S APPROVAL**. This touches **user data** (journal, goals, pages and images go to an AI service), so per CLAUDE.md nothing gets built before Megan approves this spec.

## Megan's direction (Oct 2, 2026, her words)
> "When you tap the little 11, I would NOT immediately open a full-screen chatbot. Instead, Lucky Star pops up as a small bottom sheet over whatever you're currently doing. It knows the context of the screen."
>
> "Tap 11 → contextual Lucky Star sheet → choose an action OR talk → Lucky Star actually modifies/creates something in ISSUE11. That last part is critical. The chat isn't the feature. The actions it can take are the feature."
>
> "I wouldn't make it look like ChatGPT. Keep the bottom sheet extremely editorial—big typography, maybe 3–4 giant commands, the crooked 11 sticker sitting on its edge. It should feel like you're opening a secret editorial tool inside your magazine."

Role: Lucky Star is a **manifestation + magazine publisher agent**. It replaces "+ new entry".

## The interaction
1. She taps the crooked 11 sticker (tab bar). It's available on every screen.
2. A **small bottom sheet** opens over the current screen (no full-screen chat, and the screen stays visible behind it).
3. The sheet shows **3–4 giant commands** for *this* screen, plus "Ask Lucky Star anything…" underneath.
4. She picks a command or talks/types.
5. Lucky Star **creates or changes something real** (a page, a script, a ritual, a to-do), shows it, and she keeps it or undoes it.

## The commands by screen
| Where she taps 11 | Header | Commands |
|---|---|---|
| **Home** | "Where are we going next?" | Final copy (Megan, Oct 2): **CREATE FOR ME** — Build something from my goals · **HELP ME FIGURE THIS OUT** — Talk through a goal, decision or block · **GIVE ME MY NEXT MOVE** — Give me one action I can take today · **SURPRISE ME** — Create something based on what you know about me |
| **Magazine page** | "This page" | Edit this page · Make this more "me" · Turn this into actions · Create another page like this |
| **Curate** | "Your imagery" | Curate imagery for this goal · Help define my aesthetic · Build this page for me |
| **Script** | "Your script" | Rewrite this · Make it more specific · Turn it into audio · What should I actually DO? |
| **First-ever open (any screen)** | Adds one onboarding line under the header (Megan, Oct 2): "I help turn the future you want into something you can see, hear and do." Shown once, then only the header. | |
| Other screens (Explore, Issue, You, Session) | To define | Default to the Home set until defined |

What each Home command creates:
- **Create for me:** turns her goals into a page, a script, an audio or a ritual (she picks which one).
- **Help me figure this out:** a short guided talk about what she wants and what's blocking her. It must **end in something saved** (a script, a goal, a next move), not an endless chat.
- **Give me my next move:** turns a manifestation into one small thing she can do today (saved as a to-do or ritual).
- **Surprise me:** Lucky Star picks one of the above, based on her goals.

## How it works (safe by design)
- **Context:** the app sends Lucky Star the screen type plus what's on it (this page's text, this script, this goal). Nothing else.
- **Actions, not chat:** every answer ends in one action from a fixed list (create page, edit page text, swap layout, create script, rewrite script, create audio, create ritual/to-do, add images, save win). The app does the action; the AI never touches the database directly.
- **Preview + Undo:** changes show before they're kept (Keep / Try again), with Undo after.
- **Magazine pages:** only Megan's approved layouts (design/magazine-ai-spec.md). "Make this more me" changes text, photos and colors within the layout, never the design.
- **Her words stay hers:** rewrites keep her meaning and don't invent facts about her life.

## ⚠️ Open questions before this can be approved
1. **"Help me figure this out"** is the closest thing to coaching. Rules: it doesn't act as a therapist, has a crisis-word stop with help resources, gives no health/medical/money advice, and is short (a few turns, then it saves something).
2. **"Turn it into audio"** needs a text-to-voice service: extra cost per audio, the voice license must allow commercial use, and no cloned real voices. Megan picks the voice.
3. **"Curate imagery for this goal"**: picking from the app's image library (Megan's Midjourney images) is simple. *Generating* new images is a bigger feature (cost, rights, likeness rules). Recommend: library only in V1.
4. **Cost:** some commands cost more (pages, audio). Revenue + Megan to set fair-use limits per plan. Check current prices before deciding.

## Look
- Extremely editorial: cream sheet, huge Archivo Black commands (3–4 max), small mono labels, the crooked 11 sticker sitting on the sheet's top edge. One input line at the bottom. No chat bubbles on open.
- When Lucky Star answers, the result appears as a **magazine-style card** (a page preview, a script, a ritual), not a chat bubble.

## Not in V1
Open-ended companion chat · therapy or coaching claims · health/medical/legal/money advice · Lucky Star messaging her first · image generation (if Megan agrees with open question 3).

## Data and privacy (needs Megan's approval)
- One consent screen shared with the AI magazine; AI can be turned off in Settings. Without AI, the 11 falls back to a simple "Create" sheet (new entry, log a win, add image).
- The AI provider must not train on or keep user data. Verify its current terms before building.
- Send only the current screen's context. No email or payment data.
- Privacy labels, AI data disclosure and the "Lucky Star is AI and can make mistakes" label. Account deletion deletes everything. Re-check the App Store guidelines at build start and before submission.

## For Megan to approve (yes/no)
1. The contextual sheet and the command table above.
2. The rules for "Help me figure this out" (open question 1).
3. Audio: yes in V1, with a licensed voice she picks? (open question 2)
4. Imagery: library only in V1? (open question 3)
5. Sending context to an AI service, with the consent screen and data rules above.
