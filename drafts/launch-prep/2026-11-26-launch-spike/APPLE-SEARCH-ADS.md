# Apple Search Ads · launch weeks Dec 11 to 25, 2026 (DRAFT for Megan)
Nov 26, 2026 · 💚 GROWTH (Media Buyer) · skills: ads-apple, copywriting, graphify.
Megan, Nov 26: "Ok let's definitely do 3 and 2 And 4 too" (3 = Apple Search Ads in launch week on our exact keywords).
Nothing created or spent by an agent. Megan opens the account, adds the card and presses every button.

## 🟡 NEEDS MEGAN'S OK: budget
**Proposed: $10/day for 15 days (Dec 11 to 25) = $150 total, hard cap.**
- Why $10: it's half the size of the $300/mo Meta test (`drafts/ads/2026-11-17-launch-checklist.md`), enough for roughly 5 to 10 taps a day at the $1 to $2 tap prices third-party guides report, and small enough that a bad week costs little.
- Why not more: our break-even cost per install is only about $1.00 to $1.70 until we know real trial-to-paid conversion (lessons, Nov 19, 660 plan). So these ads are a **measuring tool** first: which of our keywords bring installs that start trials.
- Optional bump: if after Dec 18 the cost per install is under $2 and trials are starting, raise to $15/day for the last week (+$35, total $185). Megan decides on Dec 18.

## ✅ Basics checked today (Nov 26, 2026)
- **Basic vs Advanced** (Apple's own page): Basic = pay per install, **no keyword choice**, search results only, up to $10,000/month. Advanced = pay per tap (max price you set), **you choose keywords**, daily budget per campaign, no maximum. Source: [Compare Apple Ads solutions](https://ads.apple.com/app-store/help/apple-ads-basic/0001-compare-apple-ads-solutions)
- **We need Advanced**, because the plan is our exact keywords. Basic can't do that.
- **Minimum bid / budget:** Apple's page lists none. In the tool, Apple shows a suggested bid per keyword. Third-party guides (e.g. [Adapty, 2026](https://adapty.io/blog/apple-search-ads/)) also report no minimum spend. Not an Apple number, so we start low and read real tap prices on day 1.

## The campaign (one, simple)
- **Where:** ads.apple.com → Apple Ads **Advanced** → sign in with the Apple ID that owns the developer account.
- **When:** Fri Dec 11, morning, once the app shows on the App Store (you can't promote an app that isn't live).
- **Campaign:** `ISSUE11 · Search results · US · Exact · Launch` · Placement: **Search results** · Country: **United States** · Daily budget **$10** · End date **Dec 25**.
- **Ad group:** `Core keywords exact` · Devices: iPhone · **Search Match: OFF** (otherwise Apple picks words for us) · Audience: everyone (age 16+ comes from the App Store rating anyway).
- **Ad:** the default ad (it uses the App Store screenshots). No custom page needed for a first test.

### Keywords (exact match, starting max tap price)
Data: Applyra traffic / difficulty, 0 to 100 tool scores, from `drafts/aso/2026-11-22-keyword-optimization.md`.
| # | Keyword | Applyra T / D | Start bid | Why |
|---|---|---|---|---|
| 1 | issue11 | brand | $0.50 | Protects our own name from competitors. Usually the cheapest installs. |
| 2 | zine maker | 48 / 13 | $1.00 | Best ratio we have, the apps there make photo zines like us. |
| 3 | mood board maker | 45 / 38 | $1.00 | My saves is a mood board. |
| 4 | manifestation journal | 43 / 40 | $1.25 | Our app name. Core intent. |
| 5 | vision board maker | 25 / 54 | $1.25 | Exactly what we do, harder to rank organically, so paid helps most here. |
| 6 | personal magazine | 8 / 22 | $0.75 | The TikTok trend term. Tiny search today; cheap to own early. |
| 7 | magazine maker | 37 / 32 | $0.75 | Many searchers want a fake cover. Low bid, watch closely. |
Left out on purpose: **vision board free** (taps from people who want free, then meet a paywall: likely wasted money and bad reviews; organic keyword field only, per Megan's Nov 26 decision) and **manifest / vision board** (head terms, big apps, expensive taps).
Add as **negative keywords** (campaign level, exact): `magazine cover`, `fake magazine cover`, `canva`.

## What to watch daily (5 minutes, about 8 AM)
In Apple Ads → Campaigns → the ad group → Keywords tab, columns: Spend · Taps · Installs · Avg tap price · Tap-through rate.
Then App Store Connect → Analytics → Sources for installs, and RevenueCat (or App Store Connect Subscriptions) for trial starts.
Send me a screenshot of the Keywords tab each morning, or every 2 days if you're busy. I'll reply with max 3 changes.

## Stop rules (decided now so nobody guesses later)
1. **A keyword spends $15 with 0 installs** → pause that keyword.
2. **Avg tap price over $2.50** on a keyword after 3 days → lower its bid by 25%.
3. **Cost per install over $4 overall after Dec 15** → drop the daily budget to $5 and keep only the best 3 keywords.
4. **Installs but 0 trials after 25 installs** → stop the ads and look at the paywall first. Ads can't fix that.
5. **Ad rejected or app not live** → nothing runs, nothing spent. Tell OPS.
6. **Total spend reaches $150** → campaign ends, whatever the date. More only with Megan's OK.
Honest note: Apple doesn't publish whether paid installs lift organic rank. We count these as real installs that also tell us which keywords convert.

## Megan's setup steps (about 20 minutes on Dec 11)
1. ads.apple.com → **Sign in** → choose **Advanced**.
2. Add the business details and card (ISSUE11, not personal).
3. **Create campaign** → app ISSUE11 → Search results → United States → name + $10 daily budget + end Dec 25.
4. Ad group: name, iPhone, **turn Search Match off**.
5. **Add keywords** → paste the 7 above → set each to **Exact** → set the bids from the table.
6. Campaign negatives: paste the 3 negatives as exact.
7. Keep the default ad → **Start campaign** → screenshot the Campaigns page for me.
