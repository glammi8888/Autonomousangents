// usage: node related.mjs glammi|i11  (run after adding a post; adds 3 related LIVE links, skips posts that already have them)
// Adds a "Related reading" block (3 links to LIVE posts in the same topic) to every blog item. Keeps each item's draft state.
import { connect } from "framer-api";
const [site] = process.argv.slice(2);
const cfg = site === "glammi"
  ? { url: "https://framer.com/projects/Deliver-copy--CbF2PXgyZOvOV1SmANju-9HzHo", key: process.env.FRAMER_API_KEY_GLAMMI, coll: c => c.id === "R4mgLoqyF", base: "/blog/",
      groups: [["med-spa","dermatology","aesthetic","plastic"], ["jewel"], ["aeo","geo","seo","ai-","llm","visibility","positioning","queen","taste"]] }
  : { url: "https://framer.com/projects/NexApp-copy--37tiwNB9SSyPzkNCFNlD", key: process.env.FRAMER_API_KEY_ISSUE11landing, coll: c => c.name === "Blog Posts", base: "/blog/",
      groups: [["vision-board","pinterest"], ["manifest","journal"]] };
const f = await connect(cfg.url, cfg.key);
try {
  const blog = (await f.getCollections()).find(cfg.coll);
  const fields = await blog.getFields();
  const content = fields.find(x => x.name === "Content");
  const titleF = fields.find(x => x.name === "Title");
  const items = await blog.getItems();
  const live = items.filter(i => !i.draft);
  const grp = s => cfg.groups.findIndex(g => g.some(t => s.includes(t)));
  const updates = [];
  for (const it of items) {
    const html = it.fieldData[content.id]?.value || "";
    if (html.includes("Related reading")) continue;
    const g = grp(it.slug);
    let pool = live.filter(l => l.id !== it.id && grp(l.slug) === g);
    if (pool.length < 3) pool = pool.concat(live.filter(l => l.id !== it.id && !pool.includes(l)));
    const picks = pool.filter(l => !html.includes(cfg.base + l.slug)).slice(0, 3);
    if (!picks.length) continue;
    const block = `<p><strong>Related reading:</strong> ${picks.map(p => `<a href="${cfg.base}${p.slug}">${p.fieldData[titleF.id].value}</a>`).join(" · ")}</p>`;
    const i = html.lastIndexOf("<hr");
    const newHtml = i > 0 ? html.slice(0, i) + block + html.slice(i) : html + block;
    updates.push({ id: it.id, slug: it.slug, draft: !!it.draft, fieldData: { [content.id]: { type: it.fieldData[content.id].type, value: newHtml } } });
  }
  if (updates.length) await blog.addItems(updates);
  const after = await blog.getItems();
  const flips = updates.filter(u => !!after.find(a => a.id === u.id).draft !== u.draft).length;
  console.log(site, "updated", updates.length, "of", items.length, "draft flips", flips, "| example:", updates[0]?.slug);
} finally { await f.disconnect(); }
