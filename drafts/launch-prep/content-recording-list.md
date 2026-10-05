# 🩵 PRODUCT · Content recording list for the Nov 11 beta
Oct 1, 2026 · DRAFT. Based on design/prototype (v1), design/FLOW-MAP.md and design/WIREFRAMES.md. Megan records all audio + video herself.
**Target: everything recorded by Oct 16, edited and delivered by Oct 19** (build starts Oct 15; the developer can start with the first 2 sessions).

## What the screens actually need
| Screen | Needs recorded content? |
|---|---|
| 07 Sessions question (onboarding) | No recording. ⚠️ Its options must match what exists (see "Scope note"). |
| Home "Today's experience" (e.g. *Become her*, Self concept, 12 min) | Yes: rotates through the sessions. |
| Explore: 4 collections (Confidence, Travel, Style & Beauty, Wealth) | Yes: each needs at least 2 sessions so none looks empty. |
| Player (full-screen audio + moving visuals) | Yes: a voice track + music bed + a video loop per session. |
| Journal after a session ("How are you feeling now?") | No: users' own voice notes. |
| Cover reveal "Printing your issue…" | No: built as an in-app animation. |
| Paywall, Past Proof, Issue, You | No. |

The prototype lists 26 sessions (8+6+7+5). That's the Jan 11 picture, not the beta. **Beta minimum = 10 sessions + 4 video loops** (8 + Subliminal + Angel numbers, Megan Oct 5). Launch target stays 10–20 (Megan, Oct 1): add 2–12 more in November.

## Scope note (Product recommendation, Megan decides)
- Beta uses **2 session types only: Guided visualization (10–12 min) and Affirmations (5–6 min).** They need only Megan's voice + music, and they match the prototype ("Visualization · 12 min", "Affirmations · 6 min").
- Leave out for the beta: **Subliminals** (wording/health-claim risk, see WIREFRAMES.md), **Meditation** and **Breathwork** (more script risk, add later). The onboarding 07 question then shows only the types that exist, so nothing is "coming soon" (App Store 2.1 at launch).
- **Scope update (Megan, Oct 5):** for the **Jan 11 App Store launch**, Audio also includes **Subliminal** and **Angel numbers** sessions (audio/video), and Scribe includes **writing prompts** and **gratitude writing**. **Megan, Oct 5: in the Nov 11 beta too** (A9, A10 below; prompts + gratitude in Scribe). The onboarding 07 question shows: Guided visualizations · Affirmations · Subliminals · Angel numbers. They are listed as App Store keywords, so they **must ship complete in the Jan 11 build** (Apple 2.3.7) or the keywords get swapped before submission. Copy rule: experiences, never promised results or health effects (1.4.1); BRAND + Megan approve scripts.

## The list (10 sessions + 4 loops)

### Audio sessions
| # | Name | Collection | Type | Length (finished) |
|---|---|---|---|---|
| A1 | Become her | Confidence (Home hero) | Guided visualization | 12 min |
| A2 | I back myself | Confidence | Affirmations | 6 min |
| A3 | The trip you keep picturing | Travel | Guided visualization | 10 min |
| A4 | I belong everywhere I go | Travel | Affirmations | 5 min |
| A5 | Getting dressed as her | Style & Beauty | Guided visualization | 10 min |
| A6 | I like what I see | Style & Beauty | Affirmations | 5 min |
| A7 | A day in her rich life | Wealth | Guided visualization | 12 min |
| A8 | Money moves with me | Wealth | Affirmations | 5 min |
| A9 | Under the music: I am her | Confidence | Subliminal | 10 min |
| A10 | 11:11 | Wealth / Home | Angel numbers | 6 min |
Total finished audio ≈ 81 min. Names are working titles; ❤️ BRAND polishes.

### Video loops (shared per collection)
| # | Name | Used in | Length |
|---|---|---|---|
| V1 | Confidence loop | A1, A2, A9 | 20–30 s seamless loop |
| V2 | Travel loop | A3, A4 | 20–30 s seamless loop |
| V3 | Style & Beauty loop | A5, A6 | 20–30 s seamless loop |
| V4 | Wealth loop | A7, A8, A10 | 20–30 s seamless loop |
Direction: slow, cinematic, editorial (brand photography rules). Ideas: V1 light moving over a mirror and silk; V2 window/ocean light, curtains in wind; V3 fabric, lipstick, jewelry close-ups; V4 a calm, sunlit room, pages of a magazine turning. No readable brand logos. Faces optional; if anyone but Megan appears, get a signed release.
Bonus: the same footage feeds the Instagram reels (instagram-launch.md).

## Specs (give these to the developer too)
**Voice recording (master):** WAV, 48 kHz, 24-bit, mono. Quiet, soft room (closet/duvet works), mic 15–20 cm away with a pop filter, phone in airplane mode. Record 10 s of room silence at the start of each take (for noise cleanup).
**Music bed:** from a source with a commercial license that allows use in an app (check the tool's terms, e.g. Suno paid plan). Mixed about 18–20 dB under the voice. No cloned voices.
**Delivered audio (in the app):** AAC (.m4a), 48 kHz, stereo, 256 kbps. Loudness **-16 LUFS integrated, true peak -1 dBTP**, so all sessions play at the same volume. 3 s fade in, 5 s fade out. File name: `A1_become-her_v1.m4a`.
**Transcript:** a .txt of the final script per session (accessibility, App Store featuring, and App Review can read it). No extra recording.
**Video (master):** record 4K or 1080p, 9:16 vertical, 24 or 30 fps, steady (tripod/gimbal), no audio needed.
**Delivered video:** MP4 (H.264) or HEVC, 1080×1920, 30 fps, 4–6 Mbps, **no audio track**, first frame = last frame (seamless loop). Keep the bottom 30% calm (player controls sit there) and the top 15% calm (title). Plus a poster image `V1_poster.jpg` 1080×1920.
**Captions:** not needed (video has no speech).

## Script outlines
Rules for every script: process, not promises ("imagine", "notice", "practice"), never "you will get/manifest". No health, medical, therapy, sleep or anxiety claims. Second person, calm, editorial. Ends by inviting her to write in the journal.

**Guided visualization (10–12 min)**
1. Arrive (1 min): "Find a comfortable place. Close your eyes if you like." Two slow breaths, no instructions about health.
2. Set the scene (2 min): one specific morning in her future life (place, light, sounds).
3. Walk through it (5–6 min): what she wears, what she does, who she talks to, how she carries herself. Sensory detail.
4. The identity line (1–2 min): "This is who you're becoming." Let her name one thing future-her does differently.
5. One small action (1 min): "What's one thing she would do today?"
6. Return + journal prompt (1 min): "When you're ready, open your eyes. Write down what you saw."
Theme per session: A1 self-concept/presence · A3 a trip she keeps picturing · A5 getting dressed as her future self · A7 an ordinary day with financial freedom.

**Affirmations (5–6 min)**
1. Intro (30 s): "Listen, or say them with me."
2. 12–15 affirmations, first person, present tense, each said twice with a 3–4 s pause.
3. Close (30 s): "Pick the one that felt truest. Save it to your issue."
Themes: A2 self-trust · A4 travel/belonging · A6 self-image and style (no body-change claims) · A8 money and work (no income promises; e.g. "I make decisions about money with clarity", not "money comes to me easily").
**Subliminal (10 min), A9**
1. Spoken intro (30 s), honest about what it is: "Music with affirmations layered softly underneath. You may hear them faintly."
2. 15–20 affirmations recorded at normal volume, mixed **quietly but audibly** under the music bed (no hidden or inaudible messages: trust + App Review).
3. Close (30 s) + journal prompt. Never claim it "reprograms" the mind or works without effort.

**Angel numbers (6 min), A10 "11:11"**
1. Intro (1 min): what people mean by angel numbers (11:11, 111, 222), framed as a moment to pause and notice, not a prediction.
2. Reflection (3 min): "When you see 11:11, what were you just thinking about?"
3. 6–8 affirmations (1.5 min), close + journal prompt. No fortune-telling, no promises ("this means money is coming"). Ties into the ISSUE11 name.

**Scribe additions (not recordings):** PRODUCT drafts ~30 writing prompts (desire, future self, scripting, proof) + a simple gratitude entry ("3 things I'm grateful for today"); BRAND + Megan approve. Developer builds both into Scribe.

❤️ BRAND + Megan approve all scripts before recording. ~~Keep "subliminal" out of all titles and copy.~~ Superseded Oct 5: "Subliminal" may be a session type name; no claims in titles or copy.

## Recording plan (2 sessions)
**Session 1 · Voice · ~Oct 8–10 (one half day, ~3 h)**
- Warm up, record A1–A10 (≈81 min finished, plan ~3 h with retakes). Record each script in sections so mistakes are easy to redo.
- Same mic, same room, same position for all (so they sound alike).
- Then: edit + mix + loudness by Oct 14 → send A1 + A2 to the developer first.

**Session 2 · Video + pickups · ~Oct 13–16 (one day, golden hour)**
- Shoot V1–V4 (20–30 min of raw footage each, pick the best loops).
- Re-record any voice lines that came out wrong.
- Shoot extra clips for Instagram posts 2–4 in the same session.
- Edit loops + posters by Oct 18. **All files delivered Oct 19.**

## Megan-only checks
- [ ] Each music/visual tool's license allows commercial use in an app (and printing, if used in issues).
- [ ] Scripts approved before recording.
- [ ] Recordings stored in one shared folder (e.g. Drive "ISSUE11 / Sessions / Beta") with the file names above.
