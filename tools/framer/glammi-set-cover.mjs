// Sets the cover image of a Glammi blog DRAFT (never touches live items).
// usage: node glammi-set-cover.mjs <slug> <local.jpg> "<alt>"
import { connect } from "framer-api"; import fs from "fs"; import { execFileSync } from "child_process";
const [slug, file, alt] = process.argv.slice(2);
const webp = file.replace(/\.\w+$/, ".webp");
execFileSync("convert", [file, "-resize", "1600x1067!", "-quality", "82", webp]);
const f = await connect("https://framer.com/projects/Deliver-copy--CbF2PXgyZOvOV1SmANju-9HzHo", process.env.FRAMER_API_KEY_GLAMMI);
try {
  const blog = (await f.getCollections()).find(c => c.id === "R4mgLoqyF");
  const img = (await blog.getFields()).find(x => x.type === "image");
  const it = (await blog.getItems()).find(i => i.slug === slug);
  if (!it) { console.error("ABORT: no item", slug); process.exit(3); }
  if (!it.draft) { console.error("ABORT: item is live; not touching it"); process.exit(2); }
  const asset = await f.uploadImage({ image: { bytes: new Uint8Array(fs.readFileSync(webp)), mimeType: "image/webp" }, name: slug + "-cover", altText: alt });
  await blog.addItems([{ id: it.id, slug, draft: true, fieldData: { [img.id]: { type: "image", value: asset.url, alt } } }]);
  const now = (await blog.getItems()).find(i => i.slug === slug);
  console.log("cover set", slug, "draft:", now.draft, "KB:", Math.round(fs.statSync(webp).size / 1024));
} finally { await f.disconnect(); }
