# THE DREAM LIFE GAP TEST · v2 build sheet (DRAFT for Megan)
Oct 13, 2026 · 📣 Content Room · v2 = Megan's psychological structure (her ChatGPT session, Oct 13): 10 questions in a SPIN order (Situation → Problem → Implication → Need-payoff), scored by dimensions, 5 profiles, insight before any ask. v1 is in git history.
Tools: **Tally** (free) + **Kit** (free). Megan builds it in Tally from this sheet. Draft only: nothing is live.

**What it is, honestly (internal):** an original self-reflection tool drawing on established ideas (self-discrepancy, self-efficacy, the intention-behavior gap, self-determination theory, self-regulation, implementation intentions). It is **not validated and not a clinical assessment.** The public pages never cite studies or theory names as proof (Megan's rule, POSITIONING.md); they just say the score comes from your answers.

**Rules it follows:** make people feel understood before asking for anything · result shown free, no email needed · the full first-week reset is what goes by email · kind, never a judgment · no promised outcomes · gain-first (see the Q9 change) · no "plan" language that makes ISSUE11 sound like a productivity app · no "becoming her" · stages stay hidden (profiles are named after behaviors) · "™" waits for the trademark self-check.

### What changed from Megan's draft (and why)
| Megan's draft | v2 | Why |
|---|---|---|
| Q9 "Imagine another year goes by and nothing changes" | "Imagine it's a year from now and it worked. What would you be proudest of?" | Our marketing rule is gain-first, no cost-of-inaction or regret. Same insight, positive frame. It also mirrors onboarding screen 20 ("I actually did it") |
| "7-day plan" / "Turn your magazine into a plan" | "Your first-week reset" / "Turn your magazine into moves" | "Plan" reads as productivity app (architecture lock) |
| "Do it even when you're tired" | "Do it on the days you don't feel like it too. Tiny counts." | Same idea without pressure or guilt |
| Result says "a well-studied approach" | Not on public pages | No research as proof in marketing |
| [START YOUR ISSUE] | Before launch: [SAVE MY BETA SPOT] · after launch: [START YOUR ISSUE] | Nothing to start until the app is live |
| 4 profiles | 5 profiles, incl. **The Juggler** (practical barriers) | Megan's point: never tell an overwhelmed person to try harder |

---

## 1. Landing page (Tally start screen or issue11.com/gap)
> # You have a vision for your life. So why aren't you living it?
> You've made plans, set goals and promised yourself this would be the time. But somewhere between wanting it and doing it, things fall apart.
> Find out where you're getting stuck, and the one thing to change first.
> 10 questions. About 2 minutes. Your answers make the result.
> **[TAKE THE TEST]**

## 2. The 10 questions (one per screen)
Points go into hidden **calculated fields**. Field names in CAPS. Each answer's points are in brackets.

**Q1 · DESIRE** · If you could change one thing about your life right now, what would it be?
- My career or money → `GOAL = career`
- My health, body or confidence → `GOAL = health`
- My relationships or love life → `GOAL = love`
- My lifestyle and everyday happiness → `GOAL = lifestyle`
*(Use a hidden field or pass it in the redirect link; it personalizes the result line and the Kit tag.)*

**Q2 · HOW FAR IT FEELS** · How different is your life today from the one you imagine?
- Very different. Some days it feels like the wrong life. → GAP +45
- Different enough that it bothers me regularly. → GAP +35
- I'm getting closer, but there's a lot I want to change. → GAP +25
- I'm mostly happy. I just want more. → GAP +15

**Q3 · WHAT YOU'VE DONE** · Think about the last month. How much have you actually done toward it?
- I've thought about it constantly, but haven't done much. → GAP +40 · COLLECTOR +1
- I've researched and planned, but haven't really started. → GAP +35 · COLLECTOR +2
- I've taken some steps, but not consistently. → GAP +25 · REINVENTOR +1
- I've made progress, even if it's slower than I'd like. → GAP +10 · DOUBTER +2

**Q4 · WHEN YOU START** · What usually happens when you start working toward something new?
- I get really into it, then slowly lose interest. → REINVENTOR +2
- I spend so long finding the best approach that I delay starting. → COLLECTOR +2
- I'm consistent until something disrupts my routine. → JUGGLER +2
- I keep going, but get discouraged when results take a while. → DOUBTER +2

**Q5 · BELIEF** · When you think about your biggest goal, what feels most true?
- I believe I can do it. I just struggle to follow through. → REINVENTOR +1
- I want it, but I'm not sure I have what it takes. → `SELFDOUBT = 1` · DOUBTER +1
- I could do it if my circumstances were different. → JUGGLER +2
- I'm confident I'll get there eventually. → DOUBTER +1

**Q6 · WHOSE DREAM** · Where do most of your goals come from?
- Things I've wanted for years. They feel very personal. → (no points)
- A mix of what I want and what I feel I should have by now. → BLURRY +1
- Seeing other people live the life I want. → BLURRY +2 · COLLECTOR +1
- I'm still figuring out what I genuinely want. → BLURRY +3

**Q7 · AFTER A SLIP** · You miss three days of a routine you promised yourself. What happens next?
- I tell myself I'll start fresh on Monday. → REINVENTOR +2
- I rethink the whole routine. Maybe there's a better way. → COLLECTOR +2
- I try to get back into it, but it takes a while. → JUGGLER +1
- I pick it up again without making a big deal of it. → DOUBTER +1

**Q8 · WHAT'S IN THE WAY** · What's the biggest thing between you and the life you want?
- My habits. I keep falling back into the same patterns. → REINVENTOR +2
- My own doubts and overthinking. → COLLECTOR +1 · `SELFDOUBT = 1`
- Time, money, energy or other responsibilities. → JUGGLER +3
- Impatience. I struggle when progress isn't obvious. → DOUBTER +2

**Q9 · WHAT MATTERS** · Imagine it's a year from now and it worked. What would you be proudest of?
- That I finally followed through. → REINVENTOR +1
- That I stopped planning and actually started. → COLLECTOR +1
- That I made it work with the life I really have. → JUGGLER +1
- That I can finally see how far I've come. → DOUBTER +1
*(Shown in the result as "what this is really about for you".)*

**Q10 · WHAT WOULD HELP** · What would make the biggest difference right now?
- Staying consistent after the excitement fades. → `NEED = consistency` · REINVENTOR +1
- Knowing exactly where to start. → `NEED = start` · BLURRY +1 · COLLECTOR +1
- Small steps that fit my actual life. → `NEED = fit` · JUGGLER +1
- Seeing that the small things are adding up. → `NEED = proof` · DOUBTER +1

## 3. Scoring (Tally logic, checked in this order)
**The Dream Life Gap %** = Q2 + Q3 points (range 25-85%). Shown with: *"Your gap combines two of your answers: how far your life feels from the one you imagine, and how much you've done toward it lately. It's a mirror, not a test result."*

**Profile** (first rule that's true wins):
1. **JUGGLER ≥ 4** → The Juggler *(practical barriers come first, so we never tell an overwhelmed person to try harder)*
2. **BLURRY ≥ 3** → The Blurry Dreamer *(clarity before action)*
3. Otherwise the highest of REINVENTOR, COLLECTOR, DOUBTER. Ties: Reinventor, then Collector, then Doubter. *(Tally compares fields pairwise: "REINVENTOR ≥ COLLECTOR and REINVENTOR ≥ DOUBTER" → Reinventor, and so on.)*
4. Fallback → The Serial Reinventor.

**Extras passed to the result page and Kit:** `GOAL`, `NEED`, `SELFDOUBT`. If `SELFDOUBT = 1`, the result page shows the extra paragraph in section 4.
**Before going live:** take the test 10 times as different people (and ask 5 friends) to check the profiles feel right. Adjust the thresholds, then adjust again after the first 100 real results. No accuracy claims, ever.

## 4. The 5 result reports
Same layout for all: **profile → what's happening → where you're getting stuck → what to work on → your first step → your first-week reset (email) → ISSUE11.** The Reinventor in full; the other four follow the same shape.

### The Serial Reinventor (full)
> YOUR DREAM LIFE GAP: **[GAP]%** · for your **[GOAL]** goal
> # THE SERIAL REINVENTOR
> You know how to start. You've done it more times than you can count.
> A new goal shows up and you can see exactly how different life could be. You make the plan, change the routine and feel like you're finally getting somewhere. Then the excitement wears off, the routine starts to feel like work, you miss a few days, and you wait for the motivation to come back. Eventually, you start over.
>
> **WHERE YOU'RE GETTING STUCK**
> Your routines depend on how motivated you feel. Motivation comes and goes for everyone, so anything that only works on good days is hard to keep.
>
> **WHAT TO WORK ON**
> Consistency that doesn't need a good day. Pick one action that takes less than ten minutes. Do it on the days you don't feel like it too. Tiny counts.
>
> **YOUR FIRST STEP**
> Finish this sentence: "When [time], at [place], I will [small action]." Small enough to fit an ordinary Tuesday.
>
> **YOUR FIRST-WEEK RESET**
> We made you a 7-day reset from your answers: one small action, a two-minute check-in and what to do when you miss a day (because you will, and that's fine).
> *[Email me my reset]* (Kit form, one field)
>
> **WHERE ISSUE11 COMES IN** *(line changes with NEED; see table)*
> *[SAVE MY BETA SPOT]* (before launch) · *[START YOUR ISSUE]* (after launch)

### The Pinterest Collector
- **What's happening:** You're brilliant at the dreaming part: the research, the boards, the saved reels, the perfect plan. Collecting feels like progress, so starting keeps moving to "once I've figured it out".
- **Stuck:** you're waiting for the right approach before you begin, and there's always one more thing to research.
- **Work on:** starting before you feel ready. A rough start beats a perfect plan you never open.
- **First step:** pick the one image or idea you'd keep if you could keep only one. "When [time], at [place], I will [the smallest version of it]."

### The Progress Doubter
- **What's happening:** You're doing more than you give yourself credit for. But the big result isn't here yet, so the small wins don't feel like they count, and you keep moving the finish line.
- **Stuck:** you measure progress only by the outcome, so the process feels like nothing is happening.
- **Work on:** noticing proof. Change you can see is change you'll keep.
- **First step:** write three things you've done this year that the old you wouldn't have. Add one more each week.

### The Blurry Dreamer
- **What's happening:** You know something needs to change. You're just not sure yet what you want, or whether the goals you have are really yours. That's honest, not a flaw. It's hard to move toward a life you can't quite see.
- **Stuck:** you're trying to act before you're clear, so nothing feels worth committing to.
- **Work on:** clarity before effort.
- **First step:** describe one ordinary Tuesday in the life you want: where you wake up, what you wear, who you text. One paragraph. Then underline the part that feels most like you.

### The Juggler (practical barriers)
- **What's happening:** It's not that you don't want it or don't try. Your life is full: work, money, energy, people who need you. Most advice assumes you have spare time. You don't.
- **Stuck:** the routines you try are built for a different life than the one you have.
- **Work on:** steps that fit your real week, not an ideal one. Small and flexible beats ambitious and fragile.
- **First step:** find one ten-minute window you already have (the commute, the school run, the coffee). "When [that moment], I will [small action]."

**If SELFDOUBT = 1 (any profile), add:**
> **A NOTE ON "WHAT IT TAKES"**
> You said you're not sure you have what it takes. Confidence usually comes after action, not before. Each small thing you finish is evidence. Start collecting it.

**"Where ISSUE11 comes in" line, by NEED (Q10):**
| NEED | Line |
|---|---|
| consistency | One small move a week, no streaks to break and no starting over. |
| start | Lucky Star helps you find where to start, then your first Issue makes it visible. |
| fit | Small moves that fit the life you actually have. |
| proof | A place to keep your proof, so you can see how far you've come. |
Then for all: *"ISSUE11 turns your dream life into your own magazine, and helps you take the small steps that make it real."*

## 5. The first-week reset email (Kit, one form per profile, signed Megan)
**Subject:** Your first-week reset (Serial Reinventor)
> Hi,
>
> Here's your reset, built from your answers. One action, seven days, no streaks.
>
> **Your action:** the sentence you wrote: "When [time], at [place], I will [small action]." If you skipped it, use this: two minutes on the thing you want, right after your morning coffee.
>
> **Days 1-3:** do it. That's all. Small is the point.
> **Day 4:** notice how it felt. Easier than you thought, or harder? Adjust the size, not the goal.
> **Days 5-6:** keep going. If you miss a day, the rule is simple: never miss twice. No Monday restart needed.
> **Day 7:** write one line: what's different, even slightly? That line is proof.
>
> That's how ISSUE11 works too: your dream life as a magazine you actually open, and one small move a week toward it. The beta opens on November 11 and your spot is saved.
>
> One small action you keep beats ten big Mondays.
>
> Megan
> *Founder, ISSUE11*

**Other profiles, swap the action and Day 4:**
- **Collector:** action = the smallest version of the one image you kept. Day 4: "Did it look different in real life than on the board? Good. Real beats perfect."
- **Doubter:** action = one line of proof every evening. Day 4: "Read your list. That's more than nothing."
- **Blurry Dreamer:** action = add one detail a day to your Tuesday paragraph. Day 4: "Underline what keeps showing up. That's a want, not a should."
- **Juggler:** action = your ten-minute window, three times this week (not seven). Day 4: "Three times in a full week is a win. Count it."

## 6. Hooks to test
1. "You know what you want. So why aren't you getting there?" (Megan's favorite)
2. "You've planned your dream life a hundred times. What's stopping you from living it?" (manifestation and vision board crowd)
3. "You're obsessed with changing your life. So why does nothing change?" (TikTok)
4. "How far are you from the life you actually want?" (Pinterest)
Every post ends with: "Take the 2-minute test, link in bio."

## 7. Before it goes live
- [ ] Megan reads every question and result: does it feel like a friend who gets you?
- [ ] 10 self-tests + 5 friends → tune the thresholds.
- [ ] Privacy page: quiz answers collected through Tally, emails through Kit. Q1 asks about health/love/career, so don't store more than the answer letter, and never sell or share it.
- [ ] Kit: one form per profile, double opt-in, physical mailing address in the footer (PO box, never a home address).
- [ ] Launch date fixed everywhere (Dec 11 vs Jan 11).
