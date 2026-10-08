# ISSUE11 Onboarding (v3) · 🔒 LOCKED
**Locked by Megan, Oct 8, 2026.** Megan: "I'm happy." (the onboarding flow; she clarified: "not paywall lol I meant onboarding").
This is the final onboarding logic: screen order, questions, answer options, replies and what each answer feeds. It replaces onboarding v2 (design/FLOW-MAP.md) and wins wherever another doc differs.

**🔒 Lock rule:** no agent changes the order, adds or removes screens, or rewrites copy without Megan's explicit OK. Megan's corrections get logged word for word. Allowed without asking: fixing typos and adapting layout in the visual design pass.

**Still open (not locked):**
- **Paywall prices and offers** (screen 37 and 37b): price, free-trial length, discount and downsell amounts. Payments → Megan's explicit approval + Revenue (CLAUDE.md). Agreed direction (Oct 8): Yearly with a free trial (pre-selected) + Monthly without trial; weekly / $0.99 intro = test after launch; Duo/Family = V1.1. See research/paywall-notes.md.
- **Visual design**: Megan: "the design needs to be worked on" → Claude Design pass next (brief: design/claude-design/ONBOARDING-V3-DESIGN-BRIEF.md), then the tappable prototype.
- **Timing**: screen 1 says "About 5 minutes". Time it in the prototype; it must be true.

**Sources:** design/POSITIONING.md (Megan's 10 pain points, 10 desired outcomes, USP, value equation) · Headway structure (research/web2app-strategy.md, research/web2app-headway-transcript.md) · HeyCatch research + Megan's Sep 24 "full strength, as long as every claim is true" (Notion: ISSUE11: App Concept + Onboarding Flow) · I am's rhythm and aesthetic picks (research/i-am-onboarding-teardown.md) · the loop DESIRE → IMAGINE → EMBODY → BECOME underneath (design/PRODUCT-ARCHITECTURE.md), never shown as labels.
**Storyboard:** https://claude.ai/artifact/2GVFgdAkAuns1UuHYXuqyG (source: design/claude-design/onboarding-v3/, rebuild with `python3 build_ob3.py`).

## The logic in one line
Every answer builds her magazine. She feels the pain (Part 3), sees the way out (**her Issue + her actions in the app = the solution to her pain, leading to her desired outcome**), builds step one (Part 4), sees her real cover as a sneak peek, and pays to keep going.
**Value line:** YOUR ISSUE + YOUR ACTIONS = YOUR WAY THERE · **Philosophy line:** You can't control the outcome. You are in control of the process.
**Rhythm:** easy → personal → pain → way out → build → started → sneak peek → pay. Every answer gets a reply or a breather. No screen without a payoff.
**Length is intentional (Megan, Oct 8, word for word): "The length is intentional because of the sunk cost fallacy when they hit the paywall".** 38 screens + the downsell. Balance: ~8 pain screens, ~7 desired-outcome screens. Only cut a screen if it doesn't pay her back.

## The flow
| # | Screen | Copy | Borrowed from | Feeds |
|---|---|---|---|---|
| **PART 1 · HELLO** |||||
| 1 | Welcome + first question | **TURN YOUR DREAMS INTO REALITY.** "Step one: your own magazine. About 5 minutes." (time it in the prototype; must be true) (Megan, Oct 7) Below: *Where are you with manifesting?* Just curious · Tried it, nothing changed yet · Sometimes · It's part of my life | Megan's positioning (Oct 7) · Headway (question on screen 1) | tone of replies |
| 2 | Name | **WHAT SHOULD WE CALL OUR COVER STAR?** "It goes on the cover of your Issue." | I am #2 · our Q01 | cover |
| 3 | Reward | Her name appears on a blank ISSUE11 cover with a little sticker: "Hi Megan. Your cover's waiting." | Headway reward screen | — |
| 4 | Age (easy) | **HOW OLD ARE YOU?** "So your Issue speaks your language." 18–24 · 25–34 · 35–44 · 45+ **Kept (Megan, Oct 7): "age is good for data and identifying our audience".** Declare it in the App Store privacy label. | I am #3 · Headway | tone |
| **PART 2 · DESIRE** |||||
| 5 | Topic | **WHAT'S YOUR FIRST ISSUE ABOUT?** Love · Money & freedom · My own thing · A home I love · Glow-up · Peace · Travel · *Help me choose* | HeyCatch #3 · our Q03 | cover headline, World |
| 6 | Payoff (curiosity gap) | **THIS IS WHAT A REAL ISSUE LOOKS LIKE.** A sample cover + spread for her topic, sample headlines and a process-focused session title ("5 MIN · REHEARSE TOMORROW MORNING"). No feature list. | Headway curiosity gap | — |
| 7 | Feel | **WHAT DO YOU WANT TO FEEL MORE OF?** Like I'm moving forward · Unstuck · In control · Confident · Calm · Proud of myself · Excited about my life · Like myself again | Megan (Oct 7): "feel like I'm moving forward" "feeling unstuck?" | affirmations, Audio |
| 8 | Implied authority | **WHOSE LIFE INSPIRES YOUR ISSUE?** Zara Larsson · Hailey Bieber · Zendaya · Bella Hadid · Alix Earle · Sabrina Carpenter · Simone Biles · Selena Gomez (Megan's list, Oct 7). On screen: "Pick any." Internal rule (not shown): names only, no photos, nothing saying they're involved. | Headway · Sep 24 decision | tone |
| 9 | Label | **ARE YOU A DREAMER OR A DOER?** A dreamer · A doer · A bit of both | Headway labeling · Sep 24 | reply |
| 10 | Reply (changes with answer) | Dreamer: **YOU ALREADY SEE IT.** "Dreamers are great at the vision. ISSUE11 adds the steps." · Doer: **YOU'RE ALREADY MOVING.** "Doers are great at action. ISSUE11 points it toward the life you actually want." · Both: **THE BEST OF BOTH.** "You see it and you move. Your Issue keeps them together." | Headway feedback · Megan (Oct 7) | — |
| **PART 3 · THE PAIN, THEN THE WAY OUT** |||||
| 11 | Clear vision? | **DO YOU HAVE A CLEAR PICTURE OF THE LIFE YOU WANT?** Yes · Working on it · One day at a time · Not really | I am #22 | reply tone |
| 12 | Pain card 1 (yes/no) | "I've started over more times than I can count." → yes: "Most people have. That's why your Issue meets you every day." | Pain 1 (POSITIONING.md) · Headway | — |
| 13 | Pain card 2 (yes/no) | "My vision board inspired me for a week. Now I don't even see it. I forgot about it." (Megan) → yes: "A board you forget isn't a vision. An Issue you open every day is." | Pain 6 (POSITIONING.md) · Headway | — |
| 14 | Pain card 3 (yes/no) | "I say 'I'm a millionaire' and feel a little delulu." → yes: "Fair. No 'I'm a millionaire' here. Just your next real step." | Pain 5 (POSITIONING.md) · Headway | — |
| 15 | Pain card 4 (yes/no) | "I watch manifestation content but nothing in my life changes." → yes: "Watching isn't doing. ISSUE11 gives you one small step a week." | Pain 9 (POSITIONING.md) · Headway | — |
| 16 | Pain card 5 (yes/no) | "I keep waiting for my life to start while I watch others living theirs fully." (Megan) → yes: "It doesn't start later. It starts with what you do this week." | Pain 4 (POSITIONING.md) · Headway | — |
| 17 | Pain card 6 (yes/no) | "I know exactly who I want to be. I just don't know how to get there." → yes: "Then you're in the right place." | Pain 10 (core) (POSITIONING.md) · Headway | — |
| 18 | What else sounds like you | **WHAT ELSE SOUNDS LIKE YOU?** I don't know what I'm supposed to do · Generic affirmations don't feel like me · I can't tell if I'm progressing · Honestly? All of it | Pains 2, 7, 8 | Lucky Star (known context) |
| 19 | Mirror (breather) | **YOU KNOW THE LIFE YOU WANT.** "The hard part is the in-between. That's what ISSUE11 is for." | Pain 10 (core) · I am calm statement | — |
| 20 | Desired outcome | **A YEAR FROM NOW, WHAT WOULD MAKE YOU SAY "I ACTUALLY DID IT"?** I stuck with it · I finally feel clear · I took real steps · I can see how far I've come · I'm proud of who I am | Megan's desired outcomes (Oct 7) | paywall "Built for" |
| 21 | Goals should feel | **HOW DO YOU WANT YOUR GOALS TO FEEL?** Exciting, not stressful · Simple, not overwhelming · Achievable, not out of reach · Motivating, not pressuring · Calm, not anxious | Desired outcome 9 · Megan (Oct 7): "overwhelm and realistic" | tone of Audio + Lucky Star |
| 22 | Before / after | **HERE'S WHAT CHANGES.** "Your Issue + your actions in the app solve this:" WHAT HURTS NOW → WHERE IT LEADS, built only from the pain cards she said yes to: Starting over every week → A practice you actually stick to · A vision board you forget → A magazine you open every day · Feeling delulu → Real steps, no fake affirmations · Waiting for life to start → One move this week · Watching content → Doing · Not knowing how → Knowing exactly what's next | Headway before/after · Megan's outcomes | — |
| 23 | The answer (how it works) | **YOU CAN'T CONTROL THE OUTCOME. YOU ARE IN CONTROL OF THE PROCESS.** STEP 1 · YOUR ISSUE: see exactly what you're working toward · STEP 2 · AUDIO: rehearse the steps, not just the dream · STEP 3 · ONE MOVE A WEEK: act on it in real life · STEP 4 · PROOF: see that it's working. Pink line: **YOUR ISSUE + YOUR ACTIONS = YOUR WAY THERE** Button: **BUILD MY ISSUE** | Megan (Oct 7): process over outcome; "becoming her" retired · our 02b | — |
| **PART 4 · BUILD HER ISSUE** |||||
| 24 | First step (breather) | **YOUR MAGAZINE IS YOUR FIRST STEP.** "You can't move toward a life you can't see. Let's make it clear, then make it happen." → BUILD MY ISSUE (Megan: the magazine is the first step into action) | Desired outcome 4 | — |
| 25 | Aesthetic 1 | **PICK WHAT FEELS LIKE FUTURE YOU.** Image grid (3+) | I am themes · our Q04 | Your World |
| 26 | Aesthetic 2 | **PICK YOUR COVER.** Cream on Red · Noir · Over a photo (Megan's Claude Design covers) | I am theme pick · HeyCatch #13 | cover style |
| 27 | The one effortful input | **DESCRIBE YOUR DREAM LIFE IN ONE SENTENCE.** "This becomes your cover story." Mic (iOS dictation) + tap-to-use examples. | I am #36 · HeyCatch #10 | cover story, Scribe |
| 28 | Past proof | **NAME ONE THING YOU ALREADY MADE HAPPEN.** "Your first proof. It opens your Issue." Skip allowed. | our Q08 | Proof page |
| 29 | Practice | **HOW DO YOU WANT TO PRACTICE?** Listen · Watch · Both + 5 / 10 / 15 min | I am #27 · our Q05 | Audio |
| 30 | First move | **ONE SMALL STEP THIS WEEK?** "Something small the future you would do." → "This becomes your first move." | our Q09 | Next Move |
| 31 | Day 1 | Big "1", week row with today ticked: **YOUR ISSUE STARTS TODAY.** | I am #21 | streak |
| 32 | Aesthetic 3 | **PICK YOUR ICON.** (Megan's 07-app-icon-picker) | I am #29 | app icon |
| 33 | Primed notifications | Live preview of her notification ("Your Issue: *the woman who shares her work*") · how many · from/to → **ALLOW** → iOS prompt | I am #14 · HeyCatch #15 | reminders |
| 34 | Meet Lucky Star + AI consent | Existing screen. The one place we say "AI", plainly. | our 09b | consent |
| **PART 5 · STARTED → SNEAK PEEK → PAY** |||||
| 35 | Bridge (her words back) | **YOU SAID YOU START STRONG, THEN STOP.** "This time you'll have one move a week and proof that you're changing." → START MY ISSUE. Line changes with the pain she picked. | Megan: pain → outcome | — |
| 36 | Started + your future (one screen) | **WE'VE STARTED YOUR FIRST ISSUE.** A timeline that fills in live while it builds: TODAY ✓ your cover and cover story · ◐ your first session → THIS WEEK your first move → IN 30 DAYS your first proof → A YEAR FROM NOW your 4th Issue: "Flip back to the first one and think: holy shit, I actually did it." Mini-question: "Want to hear your vision read aloud?" Button: **SEE MY SNEAK PEEK →** → paywall with her cover (Megan: "instead of saying that it is ready… want a sneak peek? Yes -> paywall") | Megan (Oct 8): merged loader + future | Audio prefs |
| 37 | Paywall (with the sneak peek) | Her real cover at the top, the rest of her Issue blurred. **YOUR ISSUE IS STEP ONE. KEEP GOING.** + pink line **YOUR ISSUE + YOUR ACTIONS = YOUR WAY THERE** BUILT FOR: *her desired-outcome answer*. Benefits: dreams as a magazine you open every day · audio that rehearses the steps · one small move a week, no pressure · proof of your progress. START MY ISSUE, then real reviews (the beta review moved here from the loader), FAQ (cancel anytime, renewal price), price again. Real intro discount vs our real standard price. | Headway paywall · I am benefits · Megan | — |
| 37b | If she closes the paywall | Downsell (App Store promotional offer) | Headway · Sep 24 | — |
| 38 | Save your Issue | Sign in with Apple / email, after purchase so nothing she made is lost | HeyCatch #20 | account |

## Decisions log (Megan, Oct 7–8)
- Pain points must be "super painful" and the desired outcome "really obvious" → 6 pain cards + 4 outcome screens (20, 21, 22, 24) + the bridge (35).
- "delulu" instead of "delusional" · "becoming her" retired ("it's been overused") · process over outcome.
- Screen 1: "Turn your dreams into reality" · Screen 7: "feel like I'm moving forward", "unstuck" · Screen 8: her celebrity list, "Pick any." · Screen 9: "A bit of both" added · Screen 21: overwhelm + achievable · Screen 25: "future you".
- Honest ending: the Issue has *started*, never "ready" → sneak peek → paywall. Screens "started" + "your future" + "sneak peek?" merged into 36.
- The magazine is **step one** into action; magazine + in-app actions = solution to pain → desired outcome.
- Issue rhythm: default 4 a year (never push monthly); the timeline says "your 4th Issue".
- Age kept: "age is good for data and identifying our audience".
- Length intentional (sunk cost before the paywall).

## Trust rules (always win)
- No fake numbers, logos, countdowns or testimonials. Social proof only from real data (beta reviews first).
- Copy only claims what the app has really made at that moment ("started", "sneak peek", never "ready").
- No outcome promises; pain copy stays warm, never shaming (design/LUCKY-STAR-VOICE.md).
- The paywall is always easy to close; "Cancel anytime" visible.
- Not copied from I am: religion/beliefs (sensitive data), zodiac, job/relationship, mental-health questions, uncited "studies show" / "rewire your brain", the bundle.
- Age is collected data → App Store privacy label. Celebrity names on screen 8 only, never in ads, no photos or implied endorsement.
- Re-check App Store rules on paywalls, trials and permission priming before build.
