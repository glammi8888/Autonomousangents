// Adds a Glammi blog article as a DRAFT (never touches live items).
// usage: node glammi-add-post.mjs <html> <slug> <YYYY-MM-DD>
import { connect } from "framer-api"; import fs from "fs";
const [html, slug, date] = process.argv.slice(2);
const src = fs.readFileSync(html, "utf8");
const seoTitle = src.match(/<title>(.*?)<\/title>/)[1].replace(/&amp;/g, "&");
const title = seoTitle.replace(/\s*\|\s*Glammi Studio$/, "");
const desc = src.match(/<meta name="description" content="([^"]*)"/)[1];
const faq = src.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1].trim();
const body = src.split("<body>")[1].split("</body>")[0].replace(/<script[\s\S]*?<\/script>/g, "").replace(/<!--[\s\S]*?-->/g, "").trim();
const f = await connect("https://framer.com/projects/Deliver-copy--CbF2PXgyZOvOV1SmANju-9HzHo", process.env.FRAMER_API_KEY_GLAMMI);
try {
  const blog = (await f.getCollections()).find(c => c.id === "R4mgLoqyF");
  const F = Object.fromEntries((await blog.getFields()).map(x => [x.name, x.id]));
  const existing = (await blog.getItems()).find(i => i.slug === slug);
  if (existing && !existing.draft) { console.error("ABORT: item is live; not touching it"); process.exit(2); }
  const item = { slug, draft: true, fieldData: {
    [F["Title"]]: { type: "string", value: title },
    [F["Date"]]: { type: "date", value: date },
    [F["Summary"]]: { type: "string", value: desc },
    [F["SEO Title"]]: { type: "string", value: seoTitle },
    [F["SEO Description"]]: { type: "string", value: desc },
    [F["Content"]]: { type: "formattedText", value: body, contentType: "html" },
    [F["FAQ Schema"]]: { type: "string", value: faq },
  } };
  if (existing) item.id = existing.id;
  await blog.addItems([item]);
  const now = (await blog.getItems()).find(i => i.slug === slug);
  console.log("saved", slug, "draft:", now.draft);
} finally { await f.disconnect(); }
