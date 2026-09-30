# Research tools: running steps 1 & 2 for real

## Step 1: YouTube autocomplete

**Option A: script (any computer, or this cloud env once allowed)**
```
python3 youtube_autocomplete.py "content creator" --csv creator.csv
python3 youtube_autocomplete.py "repurpose content"
python3 youtube_autocomplete.py "ai captions"
```
Then paste the output into the ranking prompt below.

In a Claude Code cloud session, add `suggestqueries.google.com` to the environment's allowed domains (environment menu in the session title bar → Edit → Network access).

**Option B: phone, 5 minutes, no tools**
Open YouTube search, type the seed, then the seed + `a`, `b`, `c`… Screenshot the dropdowns and send the screenshots to Claude.

## Step 2: Competitor reviews (Etsy / Amazon / Gumroad)

Etsy and Amazon block automated scrapers even when the network allows them, so a scraper isn't reliable. Use one of these instead:

- **Copy-paste (most reliable):** open the top 3–5 competing listings, sort reviews by *lowest rating*, select all, and paste into Claude with the prompt below.
- **Screenshots:** scroll the review section on your phone, screenshot, and send them. Claude reads images.
- **Unblocked sources for the same signal:** Reddit threads (r/NewTubers, r/socialmedia, r/Notion) and YouTube comments on "best Notion template" / "Opus Clip review" videos. Paste those too.

## Ranking prompt (step 3)

```
You are validating digital product ideas for [niche].

AUTOCOMPLETE DATA (phrase + times suggested):
[paste script output or describe screenshots]

COMPETITOR REVIEWS / COMMENTS:
[paste]

1. Group autocomplete phrases into problem themes; rank themes by total frequency.
2. From the reviews, list the top recurring complaints and missing features, quoting each.
3. Cross them: which high-demand themes do current products fail at?
4. Propose 5 digital products (template, prompt kit, guide, checklist, mini-course) that fill those gaps. For each: demand evidence, competition level, price, and the one-line promise.
5. Rank them and recommend one to validate first.
Only use evidence from the data above, and mark anything that is a guess.
```
