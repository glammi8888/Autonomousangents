# Voice Lock Kit
### Turn one video into a week of posts that actually sound like you

AI repurposing tools write captions that sound like everyone. The reason is simple: your voice never reaches the AI. This kit fixes that in three steps:

1. **Extract** your voice from your own transcripts, once (≈15 min)
2. **Lock** it into a one-page Voice Guide you reuse forever
3. **Repurpose** any new video with prompts that load that guide first

Works with Claude, ChatGPT, or any chat AI. No subscriptions, no extra software.

---

## What you need

- Transcripts of **3–5 of your own videos** where you felt most like yourself. Unscripted/talking-head is best. (Free: YouTube's "Show transcript", TikTok's auto-captions, or any transcription tool.)
- Optionally, **10–20 of your own captions/posts** that performed well.

> Tip: pick videos with different moods (a teaching one, a story one, a rant). Range makes the guide more accurate.

---

## STEP 1 — Voice Extraction prompt

Paste this, then paste your transcripts underneath.

```
You are a voice analyst. Below are transcripts (and optionally captions) written or spoken by one creator. Your job is to capture HOW they communicate, not WHAT they talk about.

Analyse the material and produce a Voice Guide with exactly these sections:

1. VOICE IN ONE LINE — a single sentence a stranger could use to imitate them.
2. TONE DIALS — rate 1–10 and give one quoted example each:
   formal↔casual, serious↔playful, calm↔high-energy, humble↔confident, polished↔raw
3. SIGNATURE PHRASES — 10+ words, phrases, openers, and sign-offs they actually use. Quote them exactly.
4. SENTENCE SHAPE — typical length, rhythm, use of questions, fragments, lists, repetition.
5. HOW THEY OPEN — the patterns they use in the first 1–2 sentences (with quotes).
6. HOW THEY EXPLAIN — do they use stories, analogies, numbers, personal confessions, hot takes? Give examples.
7. HOW THEY TALK TO THE AUDIENCE — "you", "we", "you guys", a community name, etc.
8. HUMOUR & EMOTION — what kind, how often, how they signal it.
9. NEVER-SAY LIST — words, clichés and tones that would sound fake coming from them (include generic AI phrases like "dive in", "game-changer", "unlock", "in today's fast-paced world" unless they genuinely use them).
10. FORMATTING HABITS — emoji use, caps, punctuation, line breaks, hashtags (from captions if provided).
11. BEFORE/AFTER EXAMPLE — write one generic AI-style caption about a topic from the transcripts, then rewrite it in their voice.

Rules:
- Every claim must be backed by a direct quote from the material.
- Do not flatter or polish them. Capture their real quirks, including the messy ones.
- Keep the whole guide under 700 words so it fits at the top of future prompts.

MATERIAL:
[paste transcripts here]
```

---

## STEP 2 — Lock it: your Voice Guide

Save the output as a note called **MY VOICE GUIDE**. Read it once and fix anything that feels off. You know yourself better than the AI.

Then run this to tighten it:

```
Here is my Voice Guide. Test it: write three short captions about [a topic I talk about] using ONLY this guide. Then list anything in the guide that is vague, contradictory, or would let generic AI phrasing slip through, and give me a revised guide that fixes it. Keep it under 700 words.

[paste Voice Guide]
```

**Where to keep it:**
- Claude: add it to a Project's instructions (it loads automatically every chat)
- ChatGPT: paste into a Custom GPT or "Customize ChatGPT"
- Anywhere else: paste it at the top of each prompt below

---

## STEP 3 — Repurposing prompts

Every prompt starts the same way. **Always include your Voice Guide and the new transcript.**

### 3A. The master repurpose (1 video → 10 pieces)

```
[paste MY VOICE GUIDE]

Using ONLY the voice above, turn this video transcript into:
1. 3 short-form clip ideas — for each: the exact timestamp/quote to cut, a hook line for the first 2 seconds, and on-screen text
2. 3 captions (Instagram/TikTok) — different angles: story, lesson, hot take
3. 1 X/Threads thread (5–8 posts)
4. 1 LinkedIn post
5. 1 newsletter intro paragraph
6. 1 YouTube community post or poll

Rules:
- Reuse my signature phrases where they fit naturally; never force them.
- Nothing from my NEVER-SAY list.
- Keep my real opinions and examples from the transcript, don't invent new facts, stats, or stories.
- If a platform format clashes with my voice, keep the voice and bend the format.

TRANSCRIPT:
[paste]
```

### 3B. Hook generator

```
[paste MY VOICE GUIDE]

From this transcript, write 15 opening hooks (max 12 words each) that I would genuinely say out loud. Group them: curiosity, contrarian, confession, "you" callout, result-first. Star the 3 strongest and explain why in one line each.

TRANSCRIPT:
[paste]
```

### 3C. Clip finder

```
[paste MY VOICE GUIDE]

Find the 5 moments in this transcript most likely to work as standalone 20–60s clips. For each: start/end quote, why it works without context, a caption in my voice, and on-screen text (max 6 words).

TRANSCRIPT:
[paste]
```

### 3D. Content idea bank (never run out again)

```
[paste MY VOICE GUIDE]

Here are comments from my recent videos. Find recurring questions, frustrations and disagreements. Turn them into 20 video ideas I could make, each with: title in my style, the comment(s) it answers, and a one-line hook I'd actually say.

COMMENTS:
[paste]
```

---

## STEP 4 — The Voice Check (quality gate)

Run anything, whether AI-written, from a VA, or a tool like Opus Clip, through this before posting.

```
[paste MY VOICE GUIDE]

Score this draft 1–10 on how much it sounds like me. Then:
- Highlight every phrase that sounds generic or like AI
- Flag anything from my NEVER-SAY list
- Flag any fact, number or story that is not in my original transcript
- Rewrite it in my voice, changing as little as possible

DRAFT:
[paste]
```

**Rule of thumb:** only post at 8+.

---

## Weekly routine (30 minutes)

| When | Do | Prompt |
|---|---|---|
| After filming | Get transcript | — |
| 5 min | Master repurpose | 3A |
| 5 min | Pick hooks + clips | 3B, 3C |
| 10 min | Edit + Voice Check each piece | 4 |
| 10 min | Schedule | — |
| Monthly | Refresh idea bank from comments | 3D |
| Every 3 months | Re-run Step 1 with new videos (your voice evolves) | 1 |

---

## Troubleshooting

- **Still sounds generic?** Add more raw, unscripted transcripts, and grow your NEVER-SAY list with every phrase you delete.
- **Too much catchphrase?** Add to the guide: "Use signature phrases at most once per piece."
- **Making things up?** Keep the "don't invent facts" rule in every prompt, and run the Voice Check.
- **Different voice per platform?** Add a short "Platform notes" section to your guide (e.g. "LinkedIn: same voice, fewer jokes").
