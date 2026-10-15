# ISSUE11 printed magazine: purchase flow (Megan, Oct 15, 2026)
Source of truth for the print purchase. Megan's spec, word for word below. Mockup: https://claude.ai/artifact/QAbmsD9o7zGGY5qKHAQuFX (screens 05, 11, 12). Print partner: Lulu.

> ISSUE11 PRINTED MAGAZINE - PURCHASE FLOW
>
> Product: printed issue, 40 pages, full color, US Letter (8.5x11), glued spine. Price: $29.99. Standard shipping is free (about 11-14 business days). Digital magazine is free in the app. Subscription is $9.99/month.
>
> Fast shipping add-ons (paid, shown at checkout):
> - Ground: +$9, 9-12 business days
> - Priority Mail: +$10, 9-12 business days
> - Expedited: +$16, 6-9 business days
> - Express: +$32, 5-8 business days
> (Optional: offer only Standard, Expedited and Express.)
>
> Notes for UI:
> - Purchase happens inside the app, not a web page.
> - Estimates are not guaranteed. Printing takes 3-5 business days before shipping.
> - PO boxes and APO/FPO addresses can only use Standard or Priority Mail.
> - Hawaii, Alaska and Puerto Rico take longer.
> - Show a "Ready to print" button with page progress, like "12 of 40 pages", active at 40 pages.

## How the design applies it (Design Room)
- **Issue tab:** a "Ready to print · 12 of 40 pages" button under her Issue, greyed out until 40, then active → Ready to print (review all 40, edit, "I love it · Approve my Issue") → Order my print.
- **Checkout options:** Standard (free, 11–14 business days, pre-selected) · Expedited +$16 (6–9) · Express +$32 (5–8), following Megan's optional 3-choice set. **PO box / APO / FPO:** show Standard + Priority Mail +$10 only.
- **Every screen with dates:** "Printing takes 3–5 business days before shipping. Estimates, not guaranteed." · "Hawaii, Alaska and Puerto Rico take longer." · Total "$29.99 + tax" (Lulu prices exclude tax). US addresses only at launch.
- **Lulu cost reference (Megan, Oct 15):** free standard costs us $5.69; Lulu add-ons are "starting at" prices: Ground $8.05, Priority $9.05, Expedited $15.05, Express $30.05.

## Rules and open items
- **Apple:** physical goods must NOT be sold with Apple in-app purchase; they use another in-app payment such as Apple Pay / card (e.g. Stripe), inside the app as Megan wants. Verify the current App Review Guidelines (3.1) at build start (CLAUDE.md "verify facts that change").
- **Megan's approval before building** (CLAUDE.md rule 4): payment provider, card data handling, shipping-address storage and deletion.
- **Open:** Lulu print cost per issue (for the margin) · whether HI/AK/PR surcharges are absorbed · sales tax setup.
- **Subscription $9.99/month** is new here: the onboarding paywall's yearly price and trial are still open (ONBOARDING-V3 "Still open") → 💛 Revenue + Megan.
