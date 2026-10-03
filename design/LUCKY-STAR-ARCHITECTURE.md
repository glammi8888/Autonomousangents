# Lucky Star Architecture (PROPOSAL v1, for Megan's review)
Design Room · Oct 3, 2026 · Status: **WAITING FOR MEGAN'S APPROVAL. Nothing gets built until she approves it.**
This touches **user data, security and permissions**, so CLAUDE.md requires Megan to approve the spec before building and the result before merging.

Read with: design/LUCKY-STAR-VOICE.md (personality, locked) · design/PRODUCT-ARCHITECTURE.md (locked; it wins wherever this differs) · design/magazine-ai-spec.md · design/lucky-star-spec.md (older, superseded where this differs).

---

## Megan's rules this is built on (Oct 3, 2026, her words)
> "Do not redesign the existing app architecture around Lucky Star."

> "Nothing changes until you keep it."

> **CONTEXT INTEGRITY — HARD RULE.** "KNOWN → RETRIEVE → ASK → GENERATE". Never "MISSING CONTEXT → ASSUME → GENERATE".
> "PERSONALIZED WITHOUT HALLUCINATING. CURIOUS WITHOUT BEING ANNOYING."
> "A clarifying question is ALWAYS preferable to a fabricated personalized answer."

> Safety (her list): "it cannot silently overwrite important user content" · "destructive actions require explicit confirmation" · "generated content is distinguishable from user-authored content internally" · "tool access is scoped by context" · "failures fail safely" · "actions can be logged" · "agent decisions can be evaluated" · "user approvals/rejections are recorded" · "the model does not fabricate user history" · "prompt injection from user content/assets cannot grant additional permissions" · "tool permissions are enforced by application code, NOT merely by prompting"

> "Sophisticated underneath. Extremely simple on the surface."

---

## 1. What exists today (honest map)
**There is no app code yet.** The repo has design docs, brand files and HTML prototypes. The "current architecture" is the **V1 prototype** (design/claude-design/v1-prototype, artifact 3T2jdNK2ZT1J5gzKjwhyTM) plus the specs. Planned stack: Lovable → Despia (iOS wrapper) → Supabase (login, database, storage) → RevenueCat.

| Function | Prototype screens | Future route | Data it will need |
|---|---|---|---|
| **Home** | `home` (MOVE card, HOLD button, streak), `streak` | `/` | reads everything (summary only) |
| **Your World** | `world`, `board` | `/world` | world_assets |
| **Audio** | `explore`, `collection`, `player`, `eyes`, `after` | `/audio`, `/audio/:id` | audio_sessions, audio_plays |
| **Scribe** | `scribe`, `write`, `empty` | `/scribe`, `/scribe/:id` | scribe_entries |
| **Publish** | `issue`, `reader`, `page`, `edit` | `/issue`, `/issue/:page/edit` | issues, pages (Megan's layouts only) |
| **Proof** (part of Become) | `proof`, `proofdone`, `proofs` | `/proof` | proofs |
| **Lucky Star / 11 sticker** | `aura` + the sheet in the prototype JS (GUIDE, ASSIST, lsReply) | sheet over any screen | everything above via tools |
| Onboarding | `welcome` … `q01–q09`, `meet` (AI consent), `building`, `reveal` | `/onboarding` | profile, onboarding_answers |
| Settings | `you`, `delete`, `offline` | `/you` | AI on/off, delete account |

## 2. What we reuse (no rework)
- **All V1 screens and the flow.** Lucky Star sits on top as a sheet. No new tabs, no new sections.
- **The 11 sticker** in the tab bar = the only entry point. The `aura` screen = the Home Guide look.
- **The prototype's Lucky Star logic** (a Guide line for Home, an Assist set per screen) becomes the real routing table in section 4A.
- **"AI fills, never designs"** (magazine-ai-spec.md): Publish only fills Megan's layouts.
- **The editor's undo snapshots** = the "Keep / Undo" model for Publish.
- **The Meet Lucky Star consent screen** and the "AI can make mistakes" line.
- **The Proof screens** = the "Add as Proof?" flow.
- **iOS dictation** for voice input (free, on-device, no new service).

## 3. The smallest changes needed
Only 5 additions to the planned app:
1. **One server function, `lucky-star`** (a Supabase Edge Function). It's the only place that talks to the AI. The phone never holds the AI key.
2. **Every screen sends a small `context`** when the 11 is tapped: `{ screen, item_id }`. That's all the screen does.
3. **A few columns on tables we'd build anyway:** `source` (user | lucky_star) and `confidence` (known | inferred) on content tables.
4. **One `proposals` table:** everything Lucky Star makes waits here until she taps KEEP.
5. **One `agent_log` table:** every AI decision, tool call, keep/reject and error.

No other app changes. If Lucky Star is off or down, every screen still works without it.

## 4. The architecture

```
 11 tapped on a screen
        │  { screen, item_id, message? }
        ▼
 ┌──────────────── lucky-star (server) ───────────────────┐
 │ 1. ROUTER     screen → mode (GUIDE/ASSIST) → skill      │
 │ 2. PERMISSION allowed tools for that skill (in code)    │
 │ 3. CONTEXT    load user state for this skill only       │
 │ 4. GATE       known? → retrieve → ask → generate        │
 │ 5. MODEL      Claude, strict tools, returns ONE result  │
 │ 6. CHECK      code validates the output + safety rules  │
 │ 7. SAVE       write a PROPOSAL (never her real content) │
 │ 8. LOG        agent_log                                  │
 └─────────────────────────────────────────────────────────┘
        ▼
 Sheet shows a PREVIEW card → [KEEP] [EDIT] [TRY AGAIN]
        ▼ KEEP
 App code (not the AI) writes it into World/Scribe/Issue
```

### 4A. Contextual routing
The **app code** picks the mode from the screen. The model never picks its own mode or tools.

| Screen | Mode | Skill | Tools it can use (enforced in code) |
|---|---|---|---|
| Home | GUIDE | `guide` | read: state summary · propose: next_experience, next_move, proof_question · ask_user |
| Your World | ASSIST | `world` | read: world_assets, desires · propose: curation (from the library), board_order, caption · ask_user |
| Audio | ASSIST | `audio` | read: desires, identity, audio history · propose: session_pick, personal_script · ask_user |
| Scribe | ASSIST | `scribe` | read: this entry, desires · propose: continue, clarify_question, rewrite, theme · ask_user |
| Publish | ASSIST | `publish` | read: issue, pages, world, scribe · propose: fill_layout (Megan's layouts only), copy_edit, layout_swap · ask_user |
| Anything else | ASSIST | Home's `guide` | same as Home |

### 4B. User state (structured memory, not chat history)
Lucky Star reads **facts from tables**, not old chats. Every row has `source` (user | lucky_star) and, for anything Lucky Star noticed, `confidence` (known | inferred).

| Table | What | Who writes it |
|---|---|---|
| `profile` + `onboarding_answers` | name, becoming (Q02), vision (Q07), etc. | user |
| `desires` | what she wants, her words | user, or Lucky Star proposal she kept |
| `identity` | who she's becoming | user, or kept proposal |
| `themes` | patterns noticed (e.g. "independence") | Lucky Star, always `inferred` until she confirms |
| `world_assets` | images on her board | user only (Lucky Star can only suggest) |
| `scribe_entries` | her writing | user; kept AI text marked `source=lucky_star` |
| `audio_sessions` / `audio_plays` | library + what she played | app |
| `issues` / `pages` | her magazine | app, after KEEP |
| `next_moves` | one per week: current / done / expired | kept proposal |
| `proofs` | evidence of BECOME | user, after "Add as Proof?" |
| `proposals` | everything waiting for KEEP | Lucky Star |
| `agent_log` | decisions, tools, keeps, rejects, errors | server |

The old chat is kept only for the current conversation (short). What matters long-term is saved as rows she approved.

### 4C. Context integrity (KNOWN → RETRIEVE → ASK → GENERATE)
This is a **code step before the AI writes anything**, not just a prompt line.
1. **KNOWN:** the skill's required facts are already in state → go.
2. **RETRIEVE:** look them up with read tools (this skill's tables only).
3. **ASK:** still missing → Lucky Star asks **one** short question (`ask_user`) and stops. Example: "What's the version of you this session is for?"
4. **GENERATE:** only when the facts are there.

Rules in code:
- **Confidence:** high (known facts) → prepare a preview. Medium (only inferred) → suggest and confirm ("A lot of what you've been adding lately relates to independence and creative work. Is building your own business part of what you're moving toward?"). Low → ask.
- **Inferred is never fact.** Themes stay `inferred` until she says yes.
- **No fake memory:** the server checks for phrases like "you told me / I remember / you've always wanted". If they don't point to a real row id, the reply is blocked and regenerated. If retrieval fails: "I don't have enough context on that yet."
- **Don't re-ask:** a question is only allowed if the answer isn't already in state.

### 4D. Tools and actions
- Two kinds only: **read_*** (her data, this skill only) and **propose_*** (writes a proposal). Plus `ask_user`.
- **There is no tool that writes, edits or deletes her real content.** KEEP is a button, and app code does the write.
- Tools use strict schemas (structured outputs). The server validates every tool call against the skill's allowlist and her user id. A call outside the list is refused and logged.
- Her content (Scribe text, image captions, page text) is sent as **data, clearly marked untrusted**. Text inside it like "ignore your rules" can't unlock tools, because tools are decided by code from the screen, not by the model.

### 4E. Approval system
| What Lucky Star made | What she sees | On KEEP |
|---|---|---|
| Text (Scribe, page copy, script) | PREVIEW · [KEEP] [EDIT] [TRY AGAIN] | saved, marked `source=lucky_star` |
| Page / layout change | preview of the page · KEEP / TRY AGAIN, then UNDO | new page version (old one kept) |
| Image suggestions | "Add these to your World?" · pick which | only the ones she taps |
| Next Move | the move · [KEEP MY MOVE] [NOT NOW] | becomes this week's move |
| Proof | "Add as Proof?" · [ADD PROOF] [NOT NOW] | saved to Proof |
| Audio session | "I made something for you. 5 MIN · FUTURE SELF VISUALIZATION [PLAY]" | play is the approval; saving it is a KEEP |
| Delete / replace anything | always a confirm screen | — |

Every KEEP, EDIT, TRY AGAIN and NOT NOW is saved (`proposals.status` + `agent_log`). A NOT NOW lowers how soon the same idea comes back.

### 4F. Home guidance logic (GUIDE)
Two steps, so it's cheap and predictable:
1. **Code reads simple signals** (no AI): has a desire? World/Scribe filled? Issue made? A Next Move this week? Move done or expired? Recent Scribe that sounds like proof?
2. **Code picks the internal stage** (Desire / Imagine / Embody / Become, never shown as navigation) and the **AI writes ONE card** for that stage from real facts: one line + one button.

| Signals | Stage | The one next thing |
|---|---|---|
| No clear desire | Desire | a conversation ("What do you want more of?") |
| Desire, thin World/Scribe | Imagine | build World or Scribe, or a visualization |
| Issue exists, no move this week | Embody | one Next Move (max 1 per week) |
| Move tried or time passed | Become | "Did something show up?" → Add as Proof? |

If signals are thin, the card asks one question instead of guessing.

### 4G. Feature skills (V1: 2–3 actions each, no more)
- **World:** suggest images from the ISSUE11 library for a desire · find her aesthetic pattern (as a question) · organize her board.
- **Audio:** recommend a session for where she is · write a personal affirmation / visualization script from her own words (read in the app, or played over existing audio).
- **Scribe:** ask one useful question · continue her thought · turn a thought into a manifestation statement · prep text for the magazine.
- **Publish:** fill a page from World + Scribe (Megan's layouts) · rewrite copy · small edits by prompt ("make the title bolder", "swap the photo").

### 4H. Safety boundaries
- Permissions live in code (4A). The prompt can't widen them.
- No silent writes, no deletes by AI, versions kept for pages.
- Generated content is always tagged `source=lucky_star`.
- Crisis words → stop, show help resources, no AI reply.
- No health, medical, legal or money advice. No therapy claims.
- **Never present manifestation as guaranteeing outcomes.** Copy checks block "you will get…".
- Only the data this skill needs is sent. No email or payment data. AI provider must not train on it (verify terms before build).
- AI can be turned off in Settings; then the 11 is a plain "Create" sheet.

### 4I. Logging and evaluation
`agent_log` row per turn: user, screen, skill, stage, tools called, rows read (ids only), confidence, result, her decision, error, cost. No full text in logs beyond what's needed.
Evaluation in V1 = simple numbers: keep rate per skill, NOT NOW rate, questions asked per turn, blocked "fake memory" replies, errors. Megan's success metric stays: **Next Moves tried and Proofs added**.

### 4J. Errors and fallbacks
- AI down / slow / refused → "Lucky Star can't help right now" + the normal non-AI path. Nothing half-saved.
- Bad tool output → discarded, logged, one retry, then the fallback.
- Missing context → ask, never guess.
- Model: Claude via the Anthropic API, current default `claude-opus-5-5` (verify model, price and terms at build start).

### 4K. Personality and tone (design/LUCKY-STAR-VOICE.md, locked)
> "A nurturing, perceptive guide who helps you imagine your future, understand what you really want, and gently practice becoming her."

How the voice is enforced, not just hoped for:
- **System prompt:** Megan's voice text is the core of the prompt, with her BAD/GOOD examples.
- **Shape in code:** chat replies max ~4 short paragraphs, max **one question** per reply, no bullet lists in conversation (long text only when she asked for a script or page copy).
- **Phrase check on every reply:** blocks outcome promises and false validation ("the universe is sending you", "this is meant for you", "your manifestation is coming", "I know this will happen", "you will get…", "you're absolutely right") and fake memory (4C). Blocked → regenerate once → safe fallback line.
- **Next Move = an invitation, not an order:** it's offered as a question or a gentle suggestion, and she can always say NOT NOW.
- **Evals (V1):** a small test set of Megan's examples (the "successful" and "famous actress" ones, plus no-context cases) run before every prompt change. Megan reviews a sample of real replies before launch.

## 5. V1 REQUIRED vs LATER
| V1 REQUIRED | LATER / NICE TO HAVE |
|---|---|
| 11 sheet: GUIDE on Home, ASSIST in the 4 functions | Lucky Star messaging her first (push) |
| Text + iOS dictation input | AI voice replies / generated voice audio |
| The 5 server pieces in section 3 | Image generation (library only in V1) |
| Context integrity gate + one-question asks | Deeper memory: long-term themes, monthly reflections |
| Proposals + KEEP / EDIT / TRY AGAIN + UNDO | Preparing things in the background before she opens the app |
| One Next Move per week | Evals dashboard, A/B tests of prompts |
| Proof detect-and-ask | Proof auto-placed into a new Issue each month |
| Audio: recommend + personal script on existing audio | Fully generated personalized audio sessions |
| Logging, keep/reject records, AI off switch, voice + phrase checks | Cost tiers per plan (needs Revenue + Megan) |

## 6. For Megan to approve (yes/no)
1. **The approach:** one server function, AI only proposes, app code saves after KEEP, permissions in code.
2. **User data:** her World, Scribe and Issue content is sent to the AI service (Anthropic), only per skill, with the consent screen and AI-off switch.
3. **Audio in V1 = recommend + written personal script** (no generated voice until later).

Next after approval: the pipeline Planner turns this into a build spec on a `feature/lucky-star` branch. Language: TypeScript (Lovable + Supabase), to confirm at build start.
