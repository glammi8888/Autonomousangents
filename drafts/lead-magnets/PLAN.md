# Pinterest lead magnets plan (Megan, Nov 14 2026: "I think we should build them all")

Source: Apify Pinterest search suggestions (drafts/pinterest/2026-11-13-pinterest-keywords.md). These are suggested searches, not search volumes.
Everything is designed in Claude Design. Fonts: Inter Tight only. Colours: flat Electric Soft. No ombré, no collage.

| # | Freebie | Pinterest searches it matches | Status |
|---|---|---|---|
| 1 | 2027 Manifestation Wallpaper Pack (8 phone + 2 laptop) | manifestation wallpaper, manifestation phone wallpaper, manifestation wallpaper laptop, future self wallpaper, dream life wallpaper, vision board wallpaper, 2027 vision board wallpaper | v1 in Claude Design: https://claude.ai/artifact/MZr3GzSS5YdENf5x4D3DrT |
| 2 | 2027 Vision Board Kit (printable template + picture pack) | 2027 vision board template, ideas, pictures, aesthetic | Waiting on Megan's layout pick (Rebrand Kit canvas). Pin from early Dec (peak Dec–Jan). |
| 3 | 2027 Personal Rebrand Kit | personal rebrand checklist, template, prompts | Live at issue11.app/rebrand-kit. Restyle after layout pick; retitle pins with these keywords. |
| 4 | 2027 Journaling Prompts + Letter from Future You | journaling prompts, manifestation journal, future self letter, future self journal, future self questions | Waiting on layout pick. Reuses FutureLetter page from the Rebrand Kit. |

Delivery: same as the Rebrand Kit. Each freebie gets a Framer opt-in page (/wallpapers, /vision-board-kit, /journal-prompts) cloned from /rebrand-kit, with an email form and an optional newsletter tick box.
Wallpaper export: phone artboards are 390×844, so export at 3x to get 1170×2532. Keep the top ~300px calm for the lock-screen clock.

Format: all print pages and PDFs are US Letter (816×1056 px per page). Megan, Nov 14: "Ok so everything gotta be US letter then".

## Free wallpaper maker (Megan, Nov 14: "What if we created a manifestation wallpaper pack generator? For free? They can write their own goals and we lay it out for them instead")
Logic (OK'd by Megan): 1) write 3–7 goals in her words (example chips) → 2) pick a look (full photo, framed, scattered words, list) + an app colour → 3) upload her own photos OR pick from our library (Megan: "They can upload their own images too or pick from our library") → 4) preview phone + laptop, email (newsletter tick optional) → download → thank-you page with the waitlist CTA.
Underneath: everything runs in the browser, and her goals and photos are never uploaded. Only her email is collected (same Framer form as the Rebrand Kit). No AI, no cost. The ISSUE11 logo is on every wallpaper (Megan: "And issue11 logo appears of course on each").
Build: a Framer code component on issue11.app/wallpapers (like RebrandPrompts.tsx). The 8 static wallpapers become the examples and Pinterest pins.
Screens: lead magnets canvas, row 3 (GenWrite → GenDone).
