# issue11.app: homepage SEO title/description + App schema (LIVE Nov 13 except llms.txt)

Megan, Nov 13: "Ok let's do it" (homepage title/description wording + App schema for review). Goal: make Google and AI read ISSUE11 as a **manifestation journal app** (Canva and Pinterest win those answers today without being journals).

## 1. Homepage title + description (Framer → Pages → Home → SEO)

**Now:** ISSUE11: Manifestation & Vision Board App for iPhone
**Proposed title:** ISSUE11: Manifestation Journal & Vision Board Magazine App
(60 characters. Adds "journal" and "magazine"; "for iPhone" moves to the description.)

**Now:** ISSUE11 turns your vision board into a personal magazine, with one small step each week. A process-focused manifestation app for iPhone.
**Proposed description:** ISSUE11 is a manifestation journal app for iPhone that turns your vision board into a personal magazine, with one small step each week.
(146 characters. Same promise, with "manifestation journal app" up front.)

Only the SEO title and description change. No visible page copy changes.

## 2. App schema (Framer → Site settings → Code → End of head → Page: Home only)

No price on purpose (prices differ by plan and change; Google flags mismatches) and no ratings (the app has none yet). Add `"downloadUrl"` with the App Store link on launch day.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MobileApplication",
  "name": "ISSUE11",
  "alternateName": "ISSUE11: Manifestation Journal",
  "description": "ISSUE11 is a manifestation journal app for iPhone that turns your vision board into a personal magazine, with one small step each week.",
  "applicationCategory": "LifestyleApplication",
  "operatingSystem": "iOS",
  "url": "https://issue11.app",
  "image": "https://framerusercontent.com/images/XnHnG3EBPLY3Hn7CnGsMMBO32gU.png",
  "creator": {
    "@type": "Person",
    "name": "Megan Scott Manolova",
    "address": { "@type": "PostalAddress", "addressLocality": "Los Angeles", "addressRegion": "CA", "addressCountry": "US" }
  },
  "publisher": { "@type": "Organization", "name": "ISSUE11", "url": "https://issue11.app" }
}
</script>
```

## 3. Found while checking: llms.txt is out of date
issue11.app/llms.txt still says "first 1,000 people get 50% off their first year" and "$9.99 a month". The live site says $39.99 for the first year (then $69.99/yr), and the Nov 6 rule is never to say "50% off". Fix: replace the Price line with the live site's wording (Megan re-uploads, 1 minute). Also add "manifestation journal app" to the first line.

## 4. Also outdated: the homepage FAQ code (Google and AI read it)
The hidden FAQ schema on issue11.app says two things that no longer match the page:
- "When can I get ISSUE11?" → says beta **November 11**, App Store **December 11**. The page says the private beta opens **Dec 11**.
- "Is ISSUE11 free?" → says "$9.99 a month" and "**50% off** their first year". The page says founding members pay **$39.99 the first year, then $69.99/yr**.

Corrected answers (replace the "text" values in that code; it lives in Framer → Site settings → Code, or Page → Home → Custom Code):
- When can I get ISSUE11? → "A private beta opens on December 11, 2026, with invites for the waitlist. The App Store launch follows after the beta."
- Is ISSUE11 free? → "Joining the waitlist is free. Founding members pay $39.99 for the first year, then $69.99 a year, digital magazine included. A printed Issue is optional: $29.99 with free standard shipping in the US."

## Status (Nov 13, verified on live issue11.app)
- ✅ 1 Homepage title + description: live.
- ✅ 2 App schema: live (Framer custom code "App Schema (MobileApplication)", Home only, end of body).
- ✅ 4 FAQ schema answers: live (no "50% off", no "November 11").
- ⏳ 3 llms.txt: Static Files can't be uploaded by agents. Handed to OPS (Freyja Inbox, Nov 13). Fallback: Megan.
