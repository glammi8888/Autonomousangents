# Winter arc pins (Nov 17, 2026)

Six pins for issue11.app/blog/winter-arc, drafted for Megan's approval. Nothing is posted or scheduled.

- `PINS.md`: keyword data, viral formats, sources for every line, SEO rows (title, description, board, alt text, link), QA notes and a suggested 72h posting order.
- `gen_winter_arc.py`: generates `WA1.html` to `WA6.html` from Megan's photos in `drafts/issue11-blog/images/` (approved and loved layouts only).
- `render.js`: renders `png/WA*.png` (1000×1500) and the phone contact sheets `png/sheet-390.png` and `png/sheet-236.png`.
- Rebuild: `python3 -I gen_winter_arc.py && node render.js`

Not on the Claude Design canvas yet. After Megan's pick, upload the photos as canvas assets and add the chosen pins as `.dc.html` boards (merge with the live canvas.json first).
