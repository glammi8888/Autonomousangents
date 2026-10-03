# Design brief: Lucky Star sheet (for Claude Design)
Paste into Claude Design together with the V4 Home file. Based on design/PRODUCT-ARCHITECTURE.md (locked Oct 3, 2026).

---

**Design the Lucky Star sheet for ISSUE11, in the exact V4 Home style.**

**What it is:** Lucky Star is ISSUE11's AI guide. It opens when you tap the crooked 11 sticker in the tab bar. It's conversational (voice first, typing second), but it must look like a page from the magazine, **not a chatbot**: no chat bubbles, no avatars, no blank chat screen.

**Style (match V4 Home exactly):**
- Sheet background cream #F5EEE0, ink #0d0d0d, pink #F65AAD for accents.
- Big statements in Archivo Black, uppercase, very tight tracking (-0.05em).
- Small labels in IBM Plex Mono 11px, uppercase (this small font is key, keep it everywhere).
- Body text in Archivo Narrow.
- Buttons: the same pill buttons as V4 (44px tall, mono 11px labels; black filled + white outline variants).
- The crooked 11 sticker sits tilted on the top edge of the sheet.

**Layout:**
- A bottom sheet over the current screen (Home stays visible and dimmed behind it), not full screen.
- Top: mono label `LUCKY STAR ★`.
- **Lucky Star speaks first:** one "Guide card" with one next thing. A big Archivo statement, one or two short lines and one pill button.
- Bottom: a single input line "Talk to Lucky Star…" with a **large mic button** (voice is the main way in) and a small send arrow.
- Tiny mono line at the very bottom: "Lucky Star is AI and can make mistakes".

**Screens to design (5 states):**
1. **Home, Guide card (Embody):** "You've gotten really clear about the career you want. You've built the world around it, too. **YOU'RE READY TO EMBODY IT.** Let's create tonight's 5-minute visualization." → `START →`
2. **Home, weekly Next Move:** "You've been imagining this version of yourself for a while. **THIS WEEK, LET'S PRACTICE BEING HER.** Your move: Share one piece of work before you feel completely ready." → `KEEP MY MOVE →`
3. **Home, Proof:** "Something you wrote three months ago sounds a lot like what's happening now. **THAT'S PROOF.** Want to capture it?" → `ADD PROOF →`
4. **Listening (voice):** the mic is active (pink, gently pulsing) and her words appear live in Archivo Narrow. Lucky Star's reply then appears as a **magazine card**, e.g. a session card: `5 MIN · FUTURE SELF VISUALIZATION` + `START SESSION`.
5. **Inside Scribe (Assist mode):** same sheet, but Lucky Star starts with help for this screen only, e.g. "Want me to make this more specific?" with `MAKE IT MORE SPECIFIC` / `NOT NOW`. No generic menu.

**Rules:**
- Lucky Star always speaks first; the user never sees an empty chat.
- One next thing at a time. Never a list of options or tasks.
- Every conversation ends in something real (start a session, save to Scribe, keep a move, add proof) and shows a small confirmation with `UNDO`.
- Nothing is saved without her tap.
