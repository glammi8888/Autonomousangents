# THE DREAM LIFE GAP · Quiz build sheet (DRAFT for Megan)
Oct 13, 2026 · 📣 Content Room · Megan's idea (from her ChatGPT session), built on the 10 pain points in `design/POSITIONING.md`. Tool: **Tally** (free) + **Kit** (free). Megan builds it in Tally from this sheet (no agent access to Tally). Draft only: nothing is live.

**Rules it follows:** feels like an insightful friend, never a judgment · the score comes from the answers and says so · no promised outcomes · no "becoming her" · the 4 profiles are named after behaviors (the DESIRE → IMAGINE → EMBODY → BECOME stages stay hidden, per the architecture rule) · "™" left off until the trademark self-check is done.

---

## How it works (Tally)
1. **Two kinds of hidden calculated fields** (Tally → "Calculated field", start value in brackets):
   - `GAP` (starts at **20**). Each answer adds 0, 5 or 10. Final range 20-90, shown as a %.
   - `BLURRY`, `COLLECTOR`, `REINVENTOR`, `DOUBTER` (start at **0**). Each answer adds **1** to one profile.
2. **8 questions**, one per page, single choice. Each answer: `+1` to its profile, `+N` to `GAP` (in the brackets below).
3. **Result:** after Q8, conditional logic redirects to one of 4 result pages on issue11.com, passing the score in the link (e.g. `issue11.com/gap/reinventor?gap=@GAP`).
   **Which profile wins** (check in this order; the first that is true wins, so ties go to the more common pain):
   1. REINVENTOR ≥ COLLECTOR and REINVENTOR ≥ BLURRY and REINVENTOR ≥ DOUBTER → `/gap/reinventor`
   2. COLLECTOR ≥ BLURRY and COLLECTOR ≥ DOUBTER → `/gap/collector`
   3. BLURRY ≥ DOUBTER → `/gap/blurry`
   4. Otherwise → `/gap/doubter`
   *(Tally's help says personality quizzes can send people to their highest category. If comparing two fields isn't offered in the logic menu, use Tally's personality quiz template instead and keep this content.)*
4. **Email:** each result page has a Kit form, "Email me my full profile". One Kit form per profile → its own welcome email (below) + a tag (`gap-reinventor` etc.).

---

## The quiz copy

**Start screen**
> # THE DREAM LIFE GAP
> How far are you from the life you actually want?
> 8 questions. 60 seconds. Your answers make the score: no magic, no judgment.
> **[START]**

**Q1. When you picture your dream life, how clear is it?**
- Blurry. I just know it's not this. → BLURRY (+10)
- Clear, and saved in about 400 Pinterest pins. → COLLECTOR (+5)
- Clear. I've started chasing it a few times. → REINVENTOR (+5)
- Clear, and bits of it are already happening. → DOUBTER (+0)

**Q2. Where does your dream life live right now?**
- In my head, in pieces. → BLURRY (+10)
- Pinterest, saved reels, screenshots. → COLLECTOR (+5)
- In a notebook I started with big energy. → REINVENTOR (+5)
- Little bits of it, in my actual week. → DOUBTER (+0)

**Q3. The last time you got really motivated to change your life...**
- I didn't know where to start, so I didn't. → BLURRY (+10)
- I made a beautiful board. Then I forgot about it. → COLLECTOR (+5)
- I went all in for a week. Then life happened. → REINVENTOR (+5)
- I did it, but it didn't feel like it counted. → DOUBTER (+0)

**Q4. Your manifestation content diet:**
- I watch it, but none of it feels like me. → BLURRY (+5)
- I save everything. I'll use it "later". → COLLECTOR (+10)
- I binge it, then try five methods at once. → REINVENTOR (+10)
- I barely watch it. I'm busy doing things. → DOUBTER (+0)

**Q5. "I am a millionaire." Saying that out loud feels...**
- Confusing. Is that even what I want? → BLURRY (+5)
- Inspiring, for about five minutes. → COLLECTOR (+5)
- A little delulu, so I quit after a few days. → REINVENTOR (+5)
- Fine. But I want proof, not slogans. → DOUBTER (+0)

**Q6. When you think about the next three months, you feel...**
- Unsure what I'm even aiming for. → BLURRY (+10)
- Excited, in theory. → COLLECTOR (+5)
- Determined. This time is different. → REINVENTOR (+5)
- Impatient. Why isn't it here yet? → DOUBTER (+5)

**Q7. Be honest: how many times have you "started over" this year?**
- Hard to start over when I'm not sure where I'm going. → BLURRY (+10)
- I've made a new vision board a few times. → COLLECTOR (+5)
- More Mondays than I can count. → REINVENTOR (+10)
- I don't start over. I just doubt it's working. → DOUBTER (+0)

**Q8. What would help most right now?** *(profile only, no GAP points)*
- Knowing what I actually want. → BLURRY
- Turning my vision into something I actually use. → COLLECTOR
- One small thing I can keep doing. → REINVENTOR
- Seeing how far I've already come. → DOUBTER

**Before the redirect (optional loading screen):** "Reading your answers..."

---

## The 4 result pages (issue11.com/gap/...)
Same layout on all four. `[GAP]` = the number from the link.
Small print under the score on every page: *"Your score comes from your answers in this quiz. It's a mirror, not a scientific test."*

### /gap/reinventor
> YOUR DREAM LIFE GAP: **[GAP]%**
> # THE SERIAL REINVENTOR
> You know what you want, and you've gone after it more than once. You get excited, build an ambitious new routine, and then a normal week slowly pulls you back. That's not a lack of willpower. Big restarts are just hard to repeat.
> **THE ONE THING TO CHANGE FIRST:** shrink the start. Pick one small action you can repeat this week, small enough that a busy Tuesday can't stop it. Consistency beats intensity.
> **Where ISSUE11 comes in:** one small move a week, no streaks to break, and a magazine that keeps your why in front of you.
> *[Email me my full profile + save my beta spot]* (Kit form)

### /gap/collector
> YOUR DREAM LIFE GAP: **[GAP]%**
> # THE PINTEREST COLLECTOR
> Your taste is impeccable and your vision is clear. It's just stored somewhere you don't visit: 400 pins, a camera roll of screenshots, a board you stopped seeing. The dream is there. It's not part of your days yet.
> **THE ONE THING TO CHANGE FIRST:** pick the one image that makes your heart beat a little faster, and ask what the woman in it would do this week. Then do the smallest version of that.
> **Where ISSUE11 comes in:** your images become a magazine you actually open, with one small move a week tied to it.
> *[Email me my full profile + save my beta spot]*

### /gap/blurry
> YOUR DREAM LIFE GAP: **[GAP]%**
> # THE BLURRY DREAMER
> You know something needs to change. You're just not sure what you're aiming for yet, and that's honest, not a flaw. It's hard to move toward a life you can't quite see.
> **THE ONE THING TO CHANGE FIRST:** get specific before you get busy. Describe one ordinary Tuesday in the life you want: where you wake up, what you wear, who you text. One paragraph.
> **Where ISSUE11 comes in:** it starts with what you want, in your words and images, and turns it into your first Issue so you can finally see it.
> *[Email me my full profile + save my beta spot]*

### /gap/doubter
> YOUR DREAM LIFE GAP: **[GAP]%**
> # THE PROGRESS DOUBTER
> You're closer than you think. You're already doing things, but because the big result isn't here yet, the small wins don't feel like they count. So you keep moving the finish line.
> **THE ONE THING TO CHANGE FIRST:** write down three things you've done this year that the old you wouldn't have. That's proof, and it counts.
> **Where ISSUE11 comes in:** a place to keep your proof, so you can look back and see how far you've come.
> *[Email me my full profile + save my beta spot]*

**Kit form on each page:** one field (email). Button: "Send my profile". Under it: "Free. You'll also get early access news from ISSUE11. Unsubscribe anytime. [Privacy]"

---

## The 4 profile emails (Kit welcome email per form, signed Megan)
Same shape for all four; the Reinventor version in full, the others swap the middle.

**Subject:** Your Dream Life Gap profile: The Serial Reinventor
> Hi,
>
> Here's your full profile. Fair warning: most of us are Reinventors at some point. I've lost count of my own Mondays.
>
> The pattern is simple. Motivation shows up, you build something big, and the size of it is what makes it hard to repeat. So this week, try the opposite. Pick one action so small it feels almost silly: two minutes, once a day, or three times this week. Write it where you'll see it. When you do it, notice it.
>
> That's the whole idea behind ISSUE11: your dream life as a magazine you actually open, and one small move a week toward it. No streaks, no starting over.
>
> The beta opens on November 11 and your spot is saved. I'll email you before it starts.
>
> One small move beats one big Monday.
>
> Megan
> *Founder, ISSUE11*

**Other three, middle paragraph:**
- **Collector:** "Your vision isn't the problem, it's where it lives. Open your boards and pick the one image you'd keep if you could keep only one. Put it as your lock screen this week, and each time you see it, ask: what would she do today? Do the smallest version once."
- **Blurry Dreamer:** "Clarity comes from detail, not from thinking harder. Write one ordinary Tuesday in the life you want, from waking up to going to bed, in one paragraph. Don't make it impressive. Make it specific. Then underline the one thing you could try this week."
- **Progress Doubter:** "Proof is hiding in plain sight. Write down three things you've done this year that the old you wouldn't have. Keep the list somewhere you'll see it, and add one thing every week. Progress you can see is progress you'll keep."

*(Megan: the "I've lost count of my own Mondays" line is a guess at your voice; keep it only if it's true for you.)*

---

## Hooks to test (from Megan's ChatGPT session)
1. "You're obsessed with changing your life. So why does nothing change?" (TikTok)
2. "How far are you from the life you actually want?" (Pinterest)
3. "You have the vision board. You have the goals. So what's missing?"
Every quiz post ends with: "Take the 60-second test, link in bio."

## Before it goes live
- [ ] Privacy page: add "quiz answers are collected through Tally" (and Kit for emails).
- [ ] Kit: one form per profile, double opt-in on, physical mailing address in the footer (PO box, never a home address).
- [ ] Test all 4 paths yourself, plus one tie, and check the % shows on the result page.
- [ ] Launch date fixed everywhere (Dec 11 vs Jan 11).
