# ❤️ BRAND + 💜 PR + 💚 GROWTH · Holding page copy for issue11.com
Oct 1, 2026 · DRAFT for Megan to paste into Framer. Goal: one page, one action (join the waitlist), live in the **second half of October** for the Hey Helen grant.
issue11.app redirects here (301). Builds on briefs/landing-page-11-11.md (that full page stays parked; this is the small version).

## Page copy

**Top line (the plain "what is it" sentence for AI search):**
ISSUE11 is a manifestation journal app for iPhone that turns your dreams, intentions and journal entries into your own personal magazine.

**Headline:**
# Your future self is the cover story.

**Sub:**
See it. Write it. Become it. ISSUE11 launches on iPhone on January 11, 2027. Join the waitlist to hear first.

**3 benefit lines:**
- **See it.** Collect the images of the life you're becoming, all in one place.
- **Write it.** Short immersive audio and visual sessions, then a few honest lines in your journal.
- **Become it.** Your words and images become pages in your own magazine, and Past Proof shows you what has already come true.

**Waitlist form**
- Field: **Email** (required). Nothing else. Reason: one field gets the most sign-ups and collects the least personal data. Name/phone add nothing we need before launch.
- Button: **Get early access**
- Consent line (under the button):
  > By joining, you agree to receive emails from ISSUE11 about early access and the launch. Unsubscribe anytime. See our [Privacy Policy](/privacy).
- Success message:
  > You're on the list. Check your inbox to confirm your email.

**FAQ** (written as plain, quotable answers; add FAQ schema, below)

**What is ISSUE11?**
ISSUE11 is a manifestation journal app for iPhone. You collect images, listen to short audio and visual sessions, and write in your journal, and ISSUE11 turns it all into your own personal magazine about the life you're becoming.

**Who is ISSUE11 for?**
ISSUE11 is for anyone who wants to become the person they keep imagining. It's made first for ambitious, creative women in their 20s and 30s who use manifestation and journaling and want something more personal and beautifully designed.

**When and where can I get ISSUE11?**
ISSUE11 launches on the Apple App Store for iPhone on January 11, 2027. A small private beta starts on November 11, 2026. Join the waitlist at issue11.com to hear first.

**Is ISSUE11 free?**
Joining the waitlist is free. The app will be a premium subscription, and the price will be announced before launch.

**How is ISSUE11 different from a vision board or a journaling app?**
A vision board shows what you want and a journal holds what you write. ISSUE11 puts both together and turns them into a magazine about your future self, one issue at a time, so you can see your vision, write it, and look back at what has already come true.

**Footer:**
© 2026 ISSUE11 · [Privacy Policy](/privacy) · Instagram [@issue11.app](https://instagram.com/issue11.app) · TikTok [@issue11.app](https://tiktok.com/@issue11.app) · Contact: hello@issue11.com *(set up this inbox first, or remove)*

## Notes on copy
- No price, trial length or Android promise, because they're not decided (💛 REVENUE + Megan). "Premium subscription" is decided (Brand log, Sep 26).
- "Private beta on Nov 11": keep only if waitlist members can actually get a TestFlight invite. Otherwise change to "The App Store launch is January 11, 2027."
- No ratings, reviews, user counts or "as seen in" (nothing exists yet; App Store 2.3 and trust).
- No outcome promises: Past Proof "shows what has come true", it doesn't promise it will.

## FAQ schema for Framer (Site Settings → Custom Code → End of <head>)
```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"What is ISSUE11?","acceptedAnswer":{"@type":"Answer","text":"ISSUE11 is a manifestation journal app for iPhone. You collect images, listen to short audio and visual sessions, and write in your journal, and ISSUE11 turns it all into your own personal magazine about the life you're becoming."}},
{"@type":"Question","name":"Who is ISSUE11 for?","acceptedAnswer":{"@type":"Answer","text":"ISSUE11 is for anyone who wants to become the person they keep imagining. It's made first for ambitious, creative women in their 20s and 30s who use manifestation and journaling and want something more personal and beautifully designed."}},
{"@type":"Question","name":"When and where can I get ISSUE11?","acceptedAnswer":{"@type":"Answer","text":"ISSUE11 launches on the Apple App Store for iPhone on January 11, 2027. A small private beta starts on November 11, 2026. Join the waitlist at issue11.com to hear first."}},
{"@type":"Question","name":"Is ISSUE11 free?","acceptedAnswer":{"@type":"Answer","text":"Joining the waitlist is free. The app will be a premium subscription, and the price will be announced before launch."}},
{"@type":"Question","name":"How is ISSUE11 different from a vision board or a journaling app?","acceptedAnswer":{"@type":"Answer","text":"A vision board shows what you want and a journal holds what you write. ISSUE11 puts both together and turns them into a magazine about your future self, one issue at a time, so you can see your vision, write it, and look back at what has already come true."}}
]}
</script>
```
If the FAQ copy changes, change it here too (the schema must match the visible text).
Also set the page **title** "ISSUE11 · The manifestation journal that becomes your magazine" and **meta description** = the top line.

## Waitlist tool: recommend **Kit** (free Newsletter plan)
- **Why:** Framer has a built-in Kit (ConvertKit) connection, so the form sends emails straight to Kit with no code. The free plan holds up to **10,000 subscribers** (more than the roadmap goal of 1,000 by Dec 31), includes double opt-in, unsubscribe links and tags (e.g. tag "beta-interest"), and lets Megan send the launch emails from the same place.
- Set up: Kit → create a form with **double opt-in on** → Framer form "Send to" Kit → test with your own email.
- Fact check (Oct 1, 2026): Framer's Kit/Mailchimp/Loops form options per [Framer Help](https://www.framer.com/help/articles/how-can-i-add-a-contact-form-to-my-framer-website/) and [Loops docs](https://loops.so/docs/integrations/framer); Kit's free plan limit per third-party 2026 pricing reviews (e.g. [sendx.io](https://www.sendx.io/blog/convertkit-pricing)). Confirm on kit.com/pricing when signing up.
- ⚠️ Kit (and the law: CAN-SPAM) needs a **physical postal address** in every email footer. Use a PO box or virtual mailbox, not a home address.

## What the privacy page must say (draft it before the form goes live)
Short, plain, at issue11.com/privacy:
1. **Who we are:** the business name (or Megan's name if no company yet) and a contact email.
2. **What we collect:** your email address; basic technical data the site and email tool log (IP address, browser, sign-up time, email opens/clicks if tracking stays on); site analytics if Framer Analytics or cookies are used.
3. **Why:** to send early access, beta and launch updates you asked for. Nothing else.
4. **Legal basis (EU/UK visitors):** your consent. You can withdraw it anytime.
5. **Who processes it:** Framer (website hosting) and Kit (email list). We never sell your data or share it for ads.
6. **Where it's stored:** these providers may store data in the US.
7. **How long:** until you unsubscribe or ask us to delete it, or until the waitlist is no longer needed.
8. **Your rights:** access, correct, delete, unsubscribe, complain to your data protection authority (EU/UK); California residents: right to know and delete.
9. **Children:** the waitlist is not for people under 16.
10. **Cookies:** say which are used. If non-essential cookies/analytics are used for EU visitors, add Framer's cookie banner.
11. **Changes + date:** "Last updated: [date]".
⚠️ This page is about the waitlist only. The app needs its own fuller policy before the beta (journal, photos, audio, AI processing, account deletion, RevenueCat). That one touches **user data** → Megan approves it (CLAUDE.md).
