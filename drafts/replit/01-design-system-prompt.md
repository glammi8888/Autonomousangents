# Replit prompt 01: ISSUE11 design system (paste FIRST, before any screen)
Made by 🩶 Manager, Oct 7, 2026, from brand/BRAND-GUIDE.md and design/claude-design/V4-TOKENS.md (Megan's approved V4 look).
How to use: start a new Replit **mobile app**, paste everything inside the box, then upload the asset files listed at the bottom.

---

```
I'm building ISSUE11, an iPhone app (Expo / React Native): a manifestation app where you create your own personal magazine.

STEP 1 ONLY: set up the design system. Don't build any screens or navigation yet.

Create ONE theme file (e.g. theme.ts) with every color, font, size, spacing and radius below, and use ONLY these values everywhere in the app. Never hard-code colors or fonts in screens.

COLORS
- ink #0D0D0D (text, thin rules, black cards)
- page #FFFFFF (app background)
- cream #F5EEE0 (11 sticker, small tiles)
- pink #F65AAD (main accent, play button, main action)
- blush #FCD2DD (soft pink cards)
- red #D40806 (rare accent)
- green #4BA551 (rare accent)
- grey #F2F2F2, #D0D0D0, #BDBDBD, warm grey #BDB6AA (empty/inactive states)

FONTS (load with @expo-google-fonts)
- Display: Archivo Black, ALWAYS uppercase, very tight: letter-spacing about -0.06em, line-height about 0.85.
  Sizes: hero 58, card title 38, section title 26-28.
- Body and labels: Archivo Narrow (400, 600, 700).
- Small labels: IBM Plex Mono, 11px, uppercase, letter-spacing +0.03em. Use it for kickers, dates, page counts ("07 / 11", "VOL. 01"), card labels, buttons and tab labels.
  Every screen pairs a huge Archivo Black headline with these tiny mono labels. That contrast is the signature look.

SHAPES
- Images and progress segments: radius 3 (near-square, editorial)
- Cards: radius 16
- Pills: radius 22
- Capsule buttons: radius 33-48
- Thin 1px ink hairlines between sections, like a printed magazine.

BUTTONS (make reusable components)
1. Main action: "liquid glass" capsule in pink glass, label in Archivo Black uppercase.
2. Secondary: clear glass capsule (white gradient 24% to 6%, 1px white border at 50%, background blur 16, slightly saturated).
3. Cover capsule: round thumbnail on the left + title + small pink circle button on the right (used for sessions and "your issue").

STYLE RULES
- Flat, graphic, printed magazine feel. NO glossy 3D, no heavy shadows, no generic app look.
- Photos are full-bleed and editorial (fashion-magazine style), with a soft dark gradient where text sits on top.
- Patterns (like the cheetah print) are semi-transparent, like print, never fully opaque.

Finally, build ONE test screen called "Design System" that shows every color swatch, each font style with sample text ("THE FUTURE ISSUE", "VOL. 01 · 07 / 11"), and the 3 buttons, so I can check the look on my phone.
```

---

## Upload to Replit after pasting (from the repo)
- Wavy ISSUE11 logo and "11" sticker: `brand/logo/` (PNG) · identity kit pages: `brand/identity-kit/`
- Button references: `design/buttons/` (open index.html for the chosen 13 · 11 · 07 styles)
- Font reference page: `design/fonts/`
- Approved home look: `design/claude-design/v4-home-html/` (screenshot it and upload the image)

## Check on your phone (Expo Go QR) before moving on
- Headlines look tight and bold like the magazine, not loose?
- Tiny mono labels present?
- Pink glass button looks like glass, not flat pink?
If not, tell Replit exactly what's off (e.g. "headline letter-spacing tighter, -0.06em").

## Notes
- Navigation/tabs are NOT in this prompt on purpose: the tab question (4 function tabs vs Home tab) is still open with Megan.
- Studio Shodwe (display font in the Canva kit) is left out until its app license is checked.
