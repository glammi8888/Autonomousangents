// Replaces the cover image of Glammi blog items, LIVE or draft, keeping each item's draft state.
// Megan, Nov 13: "can you change the current images on glammi?" (chrome covers for every article).
// usage: node glammi-recover.mjs <map.json>   map = [{ "slug": "...", "file": "/abs/cover.jpg", "alt": "..." }, ...]
// Changes to live items go live with the next site publish.
import { connect } from "framer-api"; import fs from "fs"; import { execFileSync } from "child_process";
const map = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const f = await connect("https://framer.com/projects/Deliver-copy--CbF2PXgyZOvOV1SmANju-9HzHo", process.env.FRAMER_API_KEY_GLAMMI);
try {
  const blog = (await f.getCollections()).find(c => c.id === "R4mgLoqyF");
  const img = (await blog.getFields()).find(x => x.type === "image");
  const items = await blog.getItems();
  for (const { slug, file, alt } of map) {
    const it = items.find(i => i.slug === slug);
    if (!it) { console.error("skip, no item:", slug); continue; }
    const webp = file.replace(/\.\w+$/, ".webp");
    execFileSync("convert", [file, "-resize", "1600x1067!", "-quality", "82", webp]);
    const asset = await f.uploadImage({ image: { bytes: new Uint8Array(fs.readFileSync(webp)), mimeType: "image/webp" }, name: slug + "-cover-chrome", altText: alt });
    await blog.addItems([{ id: it.id, slug, draft: it.draft, fieldData: { [img.id]: { type: "image", value: asset.url, alt } } }]);
    console.log("cover set", slug, it.draft ? "(draft)" : "(LIVE)");
  }
  const after = await blog.getItems();
  console.log("live:", after.filter(i => !i.draft).length, "drafts:", after.filter(i => i.draft).length);
} finally { await f.disconnect(); }
