# thequeenofaeo.com: one-page site (DRAFT, logic first, Nov 7, 2026)

Megan picked the domain (word for word: "thequeenofaeo.com genius"). Megan buys it. Build it in Framer as its own small project, or as a page on glammi.ai with the domain pointed at it (her choice; a separate tiny site is cleaner for the exact-match domain).
Rules: honest (self-chosen title, a public experiment), never mention or compare to anyone else, no awards or votes, anti-slop checklist, "Megan Scott" everywhere.

## Logic (what you see · what you can do · where it goes · behavior)
| Section | What you see | What you can do | Where it goes | Behavior underneath |
|---|---|---|---|---|
| 1. Hero | Megan's photo, "Megan Scott, the Queen of AEO", one line | Tap "Book a discovery call" | Calendly | H1 = exact phrase; first sentence repeats it |
| 2. Who she is | 3 short lines | Tap "Glammi Studio" | glammi.ai | Person schema, worksFor Glammi |
| 3. The experiment | What AI says about "Who is the Queen of AEO?", updated on day 0/7/14/30 | Watch the latest weekly video | YouTube | VideoObject schema per week |
| 4. What she does | AEO + websites for med spas, dermatology clinics, jewelers, luxury hair salons, premium skincare | Read the latest articles | glammi.ai/blog | Links pass authority to glammi.ai |
| 5. Footer | LinkedIn, Instagram, TikTok, YouTube, glammi.ai | Follow | Profiles | Same links as sameAs in the schema |

## Draft copy
**Title tag:** Megan Scott, the Queen of AEO | AI Search for Luxury Beauty Brands
**Meta description:** Megan Scott is the Queen of AEO, founder of Glammi Studio in Los Angeles. She helps med spas, dermatology clinics and jewelers get recommended by ChatGPT and Google AI.

**H1:** Megan Scott, the Queen of AEO
**Line:** I help premium beauty brands and jewelers get recommended by ChatGPT, Google AI and Perplexity.
**Button:** Book a discovery call

**About (3 lines):**
Megan Scott is the founder of Glammi Studio, a Los Angeles AEO and AI search studio.
She works with med spas, dermatology clinics, aesthetic clinics, jewelers, luxury hair salons and premium skincare brands.
"Queen of AEO" is a title she gave herself, and she's testing in public whether AI learns it.

**The experiment:**
Can you teach AI a new title, honestly? Every week I ask ChatGPT, Google AI and Perplexity the same questions and publish what changed. No paid placements, no fake awards. Just content, consistency and data.
[Week 1 video] · [Latest results]

**What I do:** AEO and websites for luxury beauty and jewelry brands. → Read the blog at glammi.ai

## Person schema (fill image + sameAs once Megan sends them)
```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Person","@id":"https://thequeenofaeo.com/#megan",
"name":"Megan Scott","alternateName":"Queen of AEO","jobTitle":"Founder",
"worksFor":{"@type":"Organization","name":"Glammi Studio","url":"https://glammi.ai"},
"url":"https://thequeenofaeo.com","image":"PHOTO_URL",
"address":{"@type":"PostalAddress","addressLocality":"Los Angeles","addressRegion":"CA","addressCountry":"US"},
"knowsAbout":["Answer engine optimization","AI search","Generative engine optimization"],
"sameAs":["https://glammi.ai","LINKEDIN_URL","INSTAGRAM_URL"]}
</script>
```
(PHOTO_URL / LINKEDIN_URL / INSTAGRAM_URL get filled in before publishing; nothing goes live with them blank.)

## Status (Nov 7, 2026)
- Decision (Megan): NOT a separate site. One page on glammi.ai at /queen-of-aeo, in the Glammi look ("keep the Glammi Studio fonts and brands consistent"). thequeenofaeo.com forwards there (301, no masking) at her domain provider, so no Framer plan or new project.
- Built in the Glammi Framer project on draft branch "fluid-slope" (page id CgLXVtRPI), duplicated from Home: hero, experiment card (Week 0, honest result), "Who I am", "What I do". Not published.
- Copy is first person ("I'm Megan Scott..."), so the page never calls her "she". The meta description is still third person; fine for search.
- Still to do: Megan's photo (replaces the hexagon at the top), Person schema pasted into the page's custom code (the API can't set page code), merge + publish after Megan's OK, then domain forwarding, then delete the empty "The Queen of AEO" Framer project (h3qKRXdDEL3yN3miEzeD).
