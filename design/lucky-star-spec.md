# Spec: Lucky Star, the "11" AI helper (draft, for Megan's approval)
Design Room · Oct 2, 2026 · Status: **WAITING FOR MEGAN'S APPROVAL**. This touches **user data** (journal, goals and wins go to an AI service), so per CLAUDE.md nothing gets built before Megan approves this spec.

## Megan's decisions (Oct 2, 2026)
- The middle tab is the "11" logo and replaces "+ new entry". Megan: "the 11 is an ai agent actually ! Instead of the + sign".
- Its name is **Lucky Star**.
- For V1 it's a **do-it-for-me helper, not an open chat**. Megan: "Yes i agree".

## What Lucky Star does in V1 (a fixed list)
She taps 11, then types or talks (native iOS dictation). Lucky Star turns her request into **one action from this list**:

| She says | Lucky Star does |
|---|---|
| "Log a win: I signed my first client" | Saves a win (and it can show up in Past Proof) |
| "Write today's entry: …" / voice note | Turns it into a journal entry in her words, lightly tidied |
| "Save this quote: …" | Saves a quote for her issue |
| "I need a 10-min session for confidence" | Suggests 1–3 sessions from the library and starts the one she picks |
| "Make my issue" / "Remake page 3" | Runs the AI magazine (design/magazine-ai-spec.md) |
| "Add this to my world" | Opens the photo picker and adds the photo to My World |
| "What did I write about money last month?" | Finds and shows her own entries (search, no new advice) |

Anything else gets a friendly reply plus the list of what it can do. It never pretends.

## How it works (safe by design)
1. **Understand:** the AI only returns an action name from the list above plus its details (the text, the date, the session topic). It can't do anything outside the list.
2. **Preview:** the app shows what will happen ("Save this win?") with Edit and Save buttons. Nothing is saved without her tap.
3. **Do:** the app does the action itself (the AI never touches the database), then shows an Undo.
4. **Her words stay hers:** entries and quotes keep her meaning. The AI may fix typos and punctuation; it doesn't add feelings or facts.

## Look (from Claude Design V4)
- The 11 tab opens a sheet with "Lucky Star" at the top, a text field, a mic button and 3–4 suggestion chips (Log a win · Today's entry · A session · Make my issue).
- Uses the V4 visual language (glass capsules, Archivo, pink accents).

## Not in V1
- Open chat or "talk to Lucky Star about my life".
- Coaching, therapy, health, medical, legal or financial advice.
- Reminders or Lucky Star messaging her first (push stays as designed).
- Making images or video.

## Safety and trust
- **Crisis words** (self-harm, abuse, emergency): Lucky Star stops, shows a calm message plus crisis resources for her country, and does not give advice. Wording to be reviewed before launch.
- **No health claims** in any reply ("subliminals" wording rule still applies).
- **Clear label:** "Lucky Star is AI and can make mistakes."

## Data and privacy (needs Megan's approval)
- **Consent:** one consent screen shared with the AI magazine ("Lucky Star and your magazine use AI. What you write is sent to an AI service."). She can turn AI off in Settings; the rest of the app still works, and the old "+ new entry" sheet comes back as the fallback.
- **AI provider:** it must not train on or keep user data. Verify its current terms before building.
- **Minimum data:** send only the request plus the context needed (for search, only the matching entries). No email or payment data.
- **App Store:** privacy labels and the AI data disclosure updated. Account deletion deletes everything. Re-check current guidelines at build start and before submission.

## Cost
One small AI call per request. Revenue + Megan to set fair-use limits per plan. Check current API prices before deciding.

## For Megan to approve (yes/no)
1. The action list and "preview before saving" above.
2. The safety rules (crisis message, no advice, AI label).
3. Sending her text to an AI service, with the shared consent screen and data rules above.
