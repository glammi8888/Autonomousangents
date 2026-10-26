# Glammi Studio: pricing & business model evaluation
🩶 OPS Manager, Oct 26, 2026 · for Megan's brief "GLAMMI STUDIO — PRICING & BUSINESS MODEL" (Oct 26). **Nothing implemented or published.**
All costs and hours are **estimates** (labeled), not quotes. Framer prices are from third-party 2026 pricing guides that partly disagree: confirm on framer.com/pricing before signing anything. Founder time is costed at a notional **$50/h** so margins reflect real effort.

## TL;DR (recommendation)
1. **Launch 2 offers first, not 7:** **AEO/GEO Essentials $499/mo** and **one website subscription $199/mo**. Add Growth $799 as the upgrade. Park the one-time sites, $159 tier and multi-location until 3 clients are live.
2. **Merge $159 and $199.** They are $40 apart, both hosted, both "SEO/AEO foundations + limited updates", likely both built in Framer. Customers won't see the difference; you'd support two products.
3. **AEO first** for cash flow: the work is already running (daily articles, audits, Mangools data, 17MedSpa case study), it pays 2.5–4× more per client, and needs no new template.
4. **Cap Glammi at ~5 founder hours/week until Dec 11** so ISSUE11's beta and launch don't slip further.
5. **Blockers before charging anyone:** business bank + Stripe (same blocker as ISSUE11), a lawyer-checked service agreement, and a Glammi Framer template.

## 1. Fulfillment cost & gross margin (estimates)
Assumes Framer per-site plans: **Basic ~$10/mo (yearly) / $15 (monthly)**, Pro ~$30/$45; Stripe ~2.9% + $0.30; agents run on the existing Claude subscription (no extra cash cost, but usage limits: see §2).

| Service | Price | Founder + agent time | Cash costs | Est. gross margin |
|---|---|---|---|---|
| Essential site (3 pages) | $499 once | ~5 h ($250) | ~$15 (Stripe) | **~47%** |
| Premium site (5 pages) | $999 once | ~10 h ($500) | ~$30 | **~47%** |
| Managed site | $159/mo | build ~5 h, then ~0.75 h/mo | Framer ~$15 + Stripe ~$5/mo | **~63% monthly**, ~50% in year 1 after build |
| Premium Framer site | $199/mo | build ~10 h, then ~1 h/mo | ~$21/mo | **~64% monthly**, ~43% in year 1 after build |
| AEO/GEO Essentials | $499/mo | ~3 h/mo review | tools ~$30–50/mo share, Stripe ~$15 | **~60%** |
| AEO/GEO Growth | $799/mo | ~6 h/mo | ~$50 + ~$24 | **~53%** |
| Multi-location | from $699/loc | shared setup + ~2 h/loc/mo | ~$40/loc | ~55–65% if shared work isn't re-charged |

Takeaways: the one-time sites are the weakest (≈ $50/h effective, no recurring). A $199 site only beats a one-time sale after ~month 7. **AEO is the best margin per founder hour.** Margins improve fast once a template cuts build time to ~3 h.

## 2. Tech stack & automation architecture (reuse first)
- **Sites:** Framer + one reusable Glammi template + component library. **Framer Server API** (`framer-api`, scanned SAFE Oct 20) for CMS/blog automation. Publishing stays human-approved.
- **Leads/CRM:** Notion "🎯 Med Spa Leads (LA)" database (exists) + 🩷 Lead Gen agent (created Oct 23).
- **AEO:** 🩷 AEO agent + Mangools (KWFinder + AI Search Watcher for visibility tracking, already connected) + monthly report template in Notion/PDF.
- **Intake:** Tally form (free) + Google Drive folder per client for assets.
- **Billing:** Stripe Billing subscriptions (needs Glammi's business bank account). E-sign: any low-cost e-sign tool.
- **Support:** glammiagency@gmail.com with agent-applied labels (Request / Bug / Billing / Urgent).
- **Human gates:** publishing, client-facing claims, contracts, refunds, anything medical.
- ⚠️ **Capacity limit:** every client adds agent runs on the same Claude subscription. Daily articles × many clients will hit usage limits. Price content-heavy work (Growth) accordingly and track usage per client.

## 3. Build hours & recurring support (estimates)
- Template build (one-time, before client #1): ~15–20 h, mostly agent + Megan's design review.
- Per client site with template: ~3–5 h (Essential/Managed), ~8–10 h (Premium/Framer custom).
- Monthly site support: 0.5–1 h/client (updates, checks). AEO: 3 h (Essentials) to 6 h (Growth) per client per month.
- At 10 site + 3 AEO clients: ~25–30 h/month total; ~8–12 h of it Megan's (reviews, calls, approvals).

## 4. Framer cost implications
- **Every site needs its own Framer site plan.** Basic (~$10–15/mo) covers most 3–5 page sites (Basic ≈ 30 pages; small CMS). Pro (~$30–45/mo) only if the client needs a big CMS/blog.
- **Monthly billing loses the free custom domain**: buy yearly plans, or have the client own the domain (recommended).
- **Extra editor seats ~$20/mo each:** don't give clients editor access on Glammi's workspace; do updates for them.
- **Hand-off:** Framer's official "Project Transfer" moves the live site to the client's account; their own site plan then starts and Glammi's is cancelled (pro-rated credit). This makes clean exit terms possible.
- Third-party costs stay separate (booking software, paid forms, fonts).

## 5. Are $159 and $199 differentiated? No.
Same hosting, same SEO/AEO foundations, same "limited updates", $40 apart. **Recommendation:** one subscription, **"Glammi Site" $199/mo, 12-month minimum** (template-based, up to 5 pages, 1 small update/month). Offer **custom design as a one-time add-on** (e.g. $499) instead of a second plan. If you want a lower door-opener later, make it clearly smaller (1-page site, no updates) rather than $40 cheaper.

## 6. Contract structure (needs a lawyer's review before use)
- **Website subscription:** 12-month minimum, then month-to-month, 30 days' notice. Early exit = remaining months **or** a buyout (e.g. $499) that includes transferring the Framer project.
- **Ownership:** client owns their **domain** (registered in their name), content, photos and logo. Glammi owns templates, components and code; client gets a licence while subscribed, and the site itself on buyout or after 12 paid months via Framer Project Transfer (client then pays Framer directly).
- **AEO/GEO:** 3-month minimum, then monthly, 30 days' notice. **No guaranteed rankings or AI mentions** (wording already used in Glammi articles).
- **Scope limits in writing:** pages, revision rounds, updates/month, response times; integrations quoted separately.
- ⚠️ **Med spa specifics:** no health data through Framer forms (route intake to the client's HIPAA-compliant booking tool); client approves all medical/treatment claims (FTC + state medical-board advertising rules); before/after photos only with the client's documented patient consent.
- Easiest path: an attorney-reviewed agency template (one-time fee) rather than writing from scratch.

## 7. Acquisition workflow (beauty businesses without websites)
1. **Find:** Lead Gen agent searches Google Maps + Instagram in LA for beauty/med spa businesses with only a booking link or Linktree, 20+ reviews, active posting.
2. **Qualify:** visible pricing/booking, recent posts, reviews ≥4.3; score into the Notion leads DB.
3. **Personalize:** a 1-page "what your website could look like" preview in the Glammi template (~30 min agent time) + 3 quick wins.
4. **Reach out (Megan sends):** Instagram DM or personal Gmail drafts, ~10/week (the Oct 20 outreach plan). Agents draft only. CAN-SPAM compliant footer on emails.
5. **Convert:** 15-min call → Tally intake → contract + Stripe link.
6. **Upsell:** after 60–90 days, a free AI-visibility snapshot (Mangools AI Search Watcher) → AEO Essentials.
Track: replies, calls, closes, build hours per site, support hours, churn.

## 8. Pilot plan (3–5 paying clients, ~6 weeks)
- **Offer:** "Founding client" pricing = list price, but with a 60-day cancel-anytime guarantee (reduces risk without discounting).
- **Mix:** 2–3 AEO Essentials ($499) + 1–2 Glammi Sites ($199). Ask 17MedSpa (existing relationship) first, if appropriate.
- **Weeks 1–2:** template, contract, Stripe, intake form. **Weeks 2–4:** 30–40 personalized outreaches. **Weeks 4–6:** onboard and deliver.
- **Success criteria:** ≥3 paying clients · site build ≤5 h actual · ≥55% gross margin on actual hours · zero scope disputes · ≥1 AEO upgrade conversation.
- **Kill/adjust rule:** <2% reply rate after 40 outreaches → change message/channel before changing price.

## 9. What to launch first
**AEO/GEO Essentials ($499/mo) now** (no new build, highest margin per hour, case-study material exists), **then the $199 Glammi Site** once the template is done (it's also needed for Glammi's own blog page, which is blocking 9 drafted articles). Everything else waits for pilot data.
**ISSUE11 guardrail:** Glammi ≤5 h/week of Megan's time until Dec 11, with agents doing production and Megan only approving, calling and sending.

## Needs Megan
1. Is Glammi a separate business (own bank/Stripe), or under the same DBA as ISSUE11? This decides the billing setup.
2. OK to merge $159/$199 into one $199 plan?
3. OK to start with AEO Essentials + 17MedSpa as the first pilot ask?
