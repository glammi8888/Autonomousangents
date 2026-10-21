# Settlement Finder

An agent that finds **open class-action settlements you can claim without proof of purchase** and matches them to your life.

1. Copy `profile.example.json` to `profile.json` and fill in only what's true: your state, products you buy, services and apps you use, data-breach letters you've received, places you've lived.
2. Run:
   ```bash
   pip install -r requirements.txt
   export ANTHROPIC_API_KEY=sk-ant-...
   python find_settlements.py profile.json
   ```
3. Open `settlements-report.md`: strong matches, possible matches, deadlines, and official claim links.

You file the claims yourself on the official administrator site. A few rules worth keeping:

- Only claim settlements you're actually a class member of. Claim forms are signed under penalty of perjury, and administrators audit and reject fraudulent claims.
- Real settlements never charge a fee to file.
- Payouts are pro rata; listed amounts often shrink when many people file.

Re-run it monthly: new settlements open all the time. `profile.json` is gitignored so your details stay local.
