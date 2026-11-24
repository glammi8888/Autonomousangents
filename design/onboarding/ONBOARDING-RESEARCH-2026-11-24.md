# Onboarding research: what the top earners do (Nov 24, 2026)
Made by 🩵 PRODUCT for Megan. Megan, Nov 24, word for word: "I just want one that finds the most successful apps onboarding's secrets and I want an agent to help me decide which screens to use" · "Then we can redesign the onboarding quiz based off the data of others (until we have ours)".
Skills used: onboarding, paywalls, signup, graphify (graphs/product/GRAPH_REPORT.md). Next step: `design/onboarding/ONBOARDING-QUIZ-LOGIC-DRAFT.md` (logic only).

**How this was made:** public pages only. ScreensDesign public app pages (`screensdesign.com/apps/<app>/` and `/showcase/<app>`), Apple App Store pages, RevenueCat's public State of Subscription Apps 2026 page. No logins, no paid content. ScreensDesign hides single screens behind its own "Unlock Pro" paywall, so the flows below come from the public chapter lists (video chapter names + timestamps) and screen captions. Exact answer options are often not public.
**Revenue and installs are ScreensDesign estimates** (per month, as shown on Nov 24, 2026). Some pages show two different numbers; both are given. Treat them as rough size signals, never as facts.
**Tags:** [Fact] = shown on the source page · [Inference] = our reading, not proven.

---

## 1. The apps, one by one

### 1. I am – Daily Affirmations (Monkey Taps) · closest in feel, Megan's favourite (Oct 7)
- **Size (estimate):** ~$730k/mo, 150k installs, 4.8★. Source: https://screensdesign.com/apps/i-am-daily-affirmations/ (our own Oct 7 teardown of Megan's recording: research/i-am-onboarding-teardown.md)
- **Flow [Fact], 25 chapters before the paywall, ~2.5 min:** 1 App tracking prompt → 2 Welcome + social proof ("Twenty million lives changed", stars) → 3 How did you hear about us → 4 Name → 5 Age range (skip) → 6 Gender → 7 Zodiac (skip) → 8 Religious beliefs (skip) → 9 Relationship (skip) → 10 How familiar with affirmations → 11 Benefits (3 bullets) → 12 Time per day goal → 13 Notification schedule with a live preview card → 14 iOS notification prompt → 15 App icon pick → 16 Theme pick → 17 Bundle cross-sell → 18 Mood → 19 Reason for mood → 20 Areas to improve → 21 Mental health practices → 22 Self-acceptance topics → 23 Free-text goals → 24 Achievement goals → **25 Paywall**.
- **Sign-in:** not in onboarding at all. It lives in Settings (Apple, Google) for backup.
- **Paywall + trial [Fact]:** yearly plan, **3-day free trial**, trial timeline, a **"remind me" toggle** before the trial ends. Price not shown on the public page (Oct 7 recording: $59.99/yr shown as $4.99/mo).
- **What makes it work [Inference]:** fast easy questions first, name used right away, aesthetic choices (icon, theme) just before the paywall so the app already feels like hers, notifications primed with a preview of the real message, the reminder toggle lowers trial fear.
- **Don't copy:** unverified "20 million lives changed", religion/zodiac/mental-health questions, the bundle.

### 2. Stella – Manifest Anything · closest in category
- **Size (estimate):** ~$290k/mo (page title in another listing: $350k/mo), 55k installs, 4.7★. Source: https://screensdesign.com/apps/stella-manifest-anything/
- **Flow [Fact], ~25 chapters, paywall at ~4:11:** 1 Value promise ("Create the life you desire") → 2 Notification warm-up ("Stella works better with Notifications") → 3 iOS prompt → 4 In-app star rating → 5 Referral code (skip) → 6 Welcome → 7 Quiz explained → 8 Privacy note → 9 Name → 10 Personal greeting → 11 Where do you live → 12 Gender → 13 Sexuality → 14 Age → 15 Kids? → 16 Work → 17 How you feel about work → 18 Describe yourself (free text) → 19 Something that shaped you → 20 Something you're struggling with → 21 Relationship → 22 Most important people (add names) → 23 What matters most (grid) → 24 What resonates (multi) → 25 "Building your plan" loader → **26 Paywall** → personalized audio.
- **Sign-in:** not shown in onboarding.
- **Paywall + trial [Fact]:** "**7-day free trial, then $6.99 per week**", button "Try Stella for free".
- **What makes it work [Inference]:** a privacy note before the deep questions, then many free-text answers that come back inside the personalized audio (it feels made for her). Weekly pricing earns a lot per user but draws refund complaints.
- **Don't copy:** rating prompt before any value, sexuality/kids questions, weekly price (off-brand for a calm app).

### 3. Aya – Manifest Your Dream Self (Lit Apps, released Apr 2026)
- **Size (estimate):** ~$93k/mo (title: $100k/mo), 85k installs, 4.8★. Source: https://screensdesign.com/apps/aya-manifest-your-dream-self/
- **Flow [Fact], 21 quiz chapters, paywall at ~5:12:** 1 Welcome ("manifest your dream self") → 2 Intro from Aya (chat style) → 3 Name → 4 Age → 5 Gender → 6 Location → 7 "Let's go a little deeper" → 8 What fills your days → 9 Do you love your life (4 options) → 10 "Tell the truth" → 11 Something people misunderstand about you → 12 A life-changing event → 13 What keeps you up at night → 14 Courage reply → 15 Love life → 16 Strength reply using her name → 17 Key people → 18 What matters most (grid) → 19 Values → 20 **Dream visualization** (free text + "why do you want this life") → 21 **Ideal home** (where you'd wake up) → 22 Building your plan → 23 **Listens to a first audio session** → **24 Paywall** → create an affirmation → **manifestation board**.
- Also before the paywall: notification pre-prompt + iOS prompt, "Are you enjoying it?" + rating prompt, a transition line "I see you now. So clearly."
- **Sign-in:** none shown.
- **Paywall [Fact]:** current vs future comparison, social proof, **$9.99/week**. No trial mentioned.
- **What makes it work [Inference]:** the user *hears* her own answers (name, dream) in a first audio session **before** paying. That is the value moment the paywall leans on. Warm reply screens after the hard questions.

### 4. Finch – Self-Care Pet
- **Size (estimate):** ~$1M/mo, 250k installs. Source: https://screensdesign.com/apps/finch-self-care-pet/
- **Flow [Fact], 30 steps to the paywall:** 1 Welcome (+ log in link) → 2 Choose egg → **3 Account creation (email, code, password)** → 4 Hatch pet → 5 Pet pronouns → 6 Name pet → 7 Pet trait → 8 Your name → 9 Self-care dialogue → 10 Reinforcement → 11 Notification warm-up → 12 iOS prompt → 13 Quiz intro → 14–26 Age, gender, past experience, sleep, morning routine, activity, stress, support, happiness, challenges, support areas, eating and activity obstacles → 27 Building plan → 28 **Starter plan reveal** → 29 Pre-paywall endorsement (Editors' Choice badge) → **30 Paywall** → welcome, how did you hear, contacts, affirmation, streak intro, commitment, widget.
- **Paywall + trial [Fact]:** "See my FREE offer", 50% discount + **7-day free trial**, **$34.99/yr** shown on a trial timeline.
- **What makes it work [Inference]:** something cute is created (the pet) before any question, so she's invested before the account step. The plan reveal makes the paywall feel like unlocking *her* plan.
- **Don't copy:** streaks, mental-health questions.

### 5. Fabulous – Daily Habit Tracker
- **Size (estimate):** $39k/mo and 20k downloads (header) vs $50k/mo and 55k installs (app info). Source: https://screensdesign.com/showcase/fabulous-daily-habit-tracker
- **Flow [Fact]:** **42 steps** (category average on ScreensDesign ≈ 13). Long quiz with a sound + visual reply on every tap → **"Sign to commit"** contract → a **letter from your Future Self** → soft paywall with a trial switch, quarterly price shown per week. Questions not public.
- **Sign-in:** not shown publicly.
- **What makes it work [Inference]:** the signed commitment and the future-self letter create a peak moment just before the ask. ScreensDesign itself flags the length as a drop-off risk.

### 6. Rosebud – AI Journal (journaling, AI)
- **Size (estimate):** ~$103k/mo, <5k installs, 4.9★. Source: https://screensdesign.com/apps/rosebud-ai-journal-diary/
- **Flow [Fact], 17 chapters to the paywall:** 1 Splash → **2–3 Sign up first (Google, Apple, email)** → 4 Main goal (5 options) → 5 How did you hear → 6 Age → 7 Gender → 8 Work → 9 Relationship → 10 Spiritual practice → 11 Recent struggles → 12 Therapy experience → 13 Theme colour (6) → 14 "Personalization complete" + what the AI does, privacy → 15 **Writes her first journal entry** (voice option, mic prompt) → 16 Set goals → reminders (morning/evening) + iOS prompt → **17 Paywall**.
- **Paywall + trial [Fact]:** "**7-day free trial**", then **$12.99/month** ("Rosebud Bloom"); monthly and annual shown.
- **What makes it work [Inference]:** account first is fine when the app holds private writing (saving matters), and the first real entry happens **before** the paywall.

### 7. Stoic – journal & mental health
- **Size (estimate):** $15k/mo (header) vs $35k/mo and 40k monthly installs (app info), 4.8★. Source: https://screensdesign.com/showcase/journal-mental-health-stoic
- **Flow [Fact]:** **9 steps**: short personalization quiz → paywall at ~0:51 → plan choice → welcome → **first daily reflection** → streaks, badges, mood check-in.
- **Paywall [Fact]:** leads with social proof (App of the Day, reviews) and shows **one discounted yearly plan first**; monthly and AI tiers hide behind "view more plans". Labelled "free trial, soft paywall"; length not public.
- **What makes it work [Inference]:** short, and one plan on screen = less choice to think about.

### 8. Day One – Journal (freemium benchmark)
- **Size:** not on a public ScreensDesign page (placeholder only). App Store: 4.8★ from ~119k ratings, Editors' Choice. Source: https://apps.apple.com/us/app/day-one-journal-private-diary/id1044867788
- **Model [Fact]:** "FREE to use forever with unlimited entries"; Silver $8.99/mo or $49.99/yr, Gold $74.99 (AI features), "Start a free trial today". Google sign-in added 2026. No public onboarding flow.
- **Why it's here [Inference]:** the freemium counter-example. Big, loved, but RevenueCat's data (below) says freemium converts far fewer users.

### 9. Calm (top-earning benchmark)
- **Size (estimate):** ~$2.8M/mo, 100k installs. Source: https://screensdesign.com/apps/calm/
- **Flow [Fact], ~6 steps:** 1 Notification prompt → 2 App tracking prompt → 3 **One goal question** (list) → **4 Account creation (email, Apple, Google)** → 5 "Building your plan" loader with a quote → **6 Paywall**.
- **Paywall + trial [Fact]:** individual and family yearly with a **7-day free trial**, then **$59.99/yr** (iOS sheet). Monthly in a variant. Our Oct 8 screenshot: monthly $16.99 with **no** trial, yearly with trial (research/paywall-notes.md).
- **What makes it work [Inference]:** brand strength lets Calm be short. Sign-in sits right before the paywall, the same order Megan approved Nov 20.

### 10. Noom (quiz-onboarding benchmark)
- **Size (estimate):** ~$500k/mo, 35k installs. Source: https://screensdesign.com/apps/noom-weight-loss-food-tracker/
- **Flow [Fact]:** ~50 chapters. **Account early** (after the value slides, ~0:34) → name, age, body, goals → focus areas, event date, pace → 10-question behaviour profile ("Proof Seeker" result) → many lifestyle questions → prediction charts updated as she answers → "Analyzing your profile…" → plan summary → **paywall at ~7:38**.
- **Paywall [Fact]:** 7-day free trial, 2-month plan, **countdown timers** on the plan and paywall.
- **What makes it work [Inference]:** the result keeps changing as she answers (a chart that moves), so every question feels useful. **Don't copy:** countdown timers, "32% faster" style claims, medical questions.

### 11. Vision board apps (aesthetic / collage category)
- Checked on the App Store: Vision Board Maker, Vision Board ++, Vision Board by SuccessKit, Horizons, Launch!, AI VisionBoard. Sources: https://apps.apple.com/us/app/vision-board-maker-manifest/id6755936917 · https://apps.apple.com/us/app/horizons-vision-board-maker/id1594714973
- **[Fact]:** mostly freemium with a **board limit** + a 7-day trial on yearly; one reviewer complained the limit felt like a surprise charge. No public onboarding quiz found, no ScreensDesign revenue page.
- **[Inference]:** the category is small and tool-like; none turns the board into a finished, named object. That gap is ISSUE11's magazine.

### Market data: RevenueCat, State of Subscription Apps 2026 (115,000+ apps, 2025 data)
Source: https://www.revenuecat.com/state-of-subscription-apps-2026/
- **Hard paywall vs freemium [Fact]:** Day-35 download-to-paid median **10.7% vs 2.1%**. One-year retention of yearly subscribers about the same (27% vs 28%, via the paywalls skill reference).
- **Trial length [Fact]:** median trial-to-paid **25.5% (≤4 days) · 37.4% (5–9 days) · 42.5% (17–32 days)**.
- **Day 0 [Fact]:** **82.1%** of Health & Fitness trials start on the install day. 3-day trials: 55.4% cancel on day 0; 7-day trials: 39.8%.
- **Health & Fitness [Fact]:** trial-to-paid median 37.7%; download-to-paid 2.9%.
- (The page contradicts itself on plan mix; not used.)

---

## 2. Patterns that repeat in the top earners

| # | Pattern | Facts | Our inference for ISSUE11 |
|---|---|---|---|
| 1 | **Paywall comes right after a personal result** | All 10 flows: quiz → "building your plan" → reveal/plan → paywall. 82.1% of H&F trials start on day 0. | The paywall must sit inside onboarding, right after she sees **her own cover**. A paywall before anything personal has nothing to lean on. |
| 2 | **Manifestation earners ask 20–25 questions (2.5–5 min)** | I am 24 screens before the paywall, Stella ~24, Aya ~21; Calm 1, Stoic short. | Long works for an emotional purchase if every answer shows up later. ~18–22 screens is in range; 38 (V3) is at the long end, near Fabulous (42), which ScreensDesign flags as a drop-off risk. |
| 3 | **Answers come back inside the product** | Stella and Aya reuse name and free-text answers in the audio; Noom's chart moves with each answer. | Every ISSUE11 answer must visibly land on the cover, the first action or tonight's session. Questions that change nothing get cut. |
| 4 | **A small real value moment before paying** | Aya plays a first audio session; Rosebud writes a first entry; Finch hatches the pet; Fabulous signs a commitment. | Our moment = her real cover + page 1 (her first action). Optional later: a short audio preview (needs audio built). |
| 5 | **Notifications primed with a preview, before the iOS prompt** | I am (schedule + preview), Stella, Aya, Finch, Rosebud. | Tie it to **Your pace** (daily / weekly / monthly) so the preview shows her real first reminder. |
| 6 | **Yearly + 7-day trial is the most common offer** | Calm, Finch, Rosebud, Noom, Stella: 7 days. I am: 3 days + reminder toggle. 5–9 day trials convert 37.4% vs 25.5% for ≤4 days. | Keeps Megan's approved 7-day trial on yearly. Add a real "we'll remind you before it ends" (I am). |
| 7 | **Sign-in placement splits by app type** | Account before the paywall: Calm, Rosebud, Finch, Noom (apps that save private data). No account in onboarding: I am, Stella, Aya. | ISSUE11 saves private pages and print orders, so **Sign in → Paywall** (approved Nov 20) fits. Best spot: right after the cover, framed as "save your cover" (ScreensDesign 2026 trends: ask for an account when it protects something she made). |
| 8 | **Easy, playful choices before hard ones** | Finch egg/pet, I am icon + theme, Rosebud theme colour, Aya ideal home. | Aesthetic + cover picks early (they're fun and feed the cover); one effortful free-text input late (dream sentence). |

**Patterns we skip (trust rules):** rating prompts before value (Stella, Aya) · unverified social proof (I am "Twenty million lives changed") · countdown timers (Noom) · sensitive questions (religion, sexuality, mental health, therapy, kids) · weekly pricing · streaks (Finch, Stoic) · tracking prompt as the first screen.

**What we couldn't see:** ScreensDesign's single screens, exact answer options and paywall designs (behind its paid "Unlock Pro"); Fabulous and Stoic question lists; Day One's onboarding; any conversion rates per app (no public source has them).
