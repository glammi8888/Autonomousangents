// usage: node glammi-link-before-faq.mjs <slug> '<p>html</p>'  inserts a paragraph before the FAQ H2 (skips if the href is already there)
import { connect } from "framer-api";
const [slug, para] = process.argv.slice(2); const href = para.match(/href="([^"]+)"/)[1];
const f = await connect("https://framer.com/projects/Deliver-copy--CbF2PXgyZOvOV1SmANju-9HzHo", process.env.FRAMER_API_KEY_GLAMMI);
try { const blog = (await f.getCollections()).find(c => c.id === "R4mgLoqyF"); const F = Object.fromEntries((await blog.getFields()).map(x => [x.name, x.id]));
  const it = (await blog.getItems()).find(i => i.slug === slug); const c = it.fieldData[F["Content"]].value;
  if (c.includes(`href="${href}"`)) { console.log("skip (already linked)", slug); process.exit(0); }
  const h = c.lastIndexOf('<h2 dir="auto">Frequently Asked Questions</h2>'); if (h < 0) throw "no FAQ h2 in " + slug;
  await blog.addItems([{ id: it.id, slug, draft: it.draft, fieldData: { [F["Content"]]: { type: "formattedText", value: c.slice(0, h) + para + c.slice(h), contentType: "html" } } }]);
  console.log("linked", slug, "->", href);
} finally { await f.disconnect(); }
