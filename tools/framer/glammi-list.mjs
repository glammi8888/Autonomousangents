// Lists Glammi Blog items (slug, draft, has cover, date). Read only.
// Key: FRAMER_API_KEY_GLAMMI (env). Setup: npm i --ignore-scripts framer-api@5.1.0
import { connect } from "framer-api";
const URL = "https://framer.com/projects/Deliver-copy--CbF2PXgyZOvOV1SmANju-9HzHo";
const f = await connect(URL, process.env.FRAMER_API_KEY_GLAMMI);
try {
  const blog = (await f.getCollections()).find(c => c.id === "R4mgLoqyF");
  const fields = await blog.getFields();
  const img = fields.find(x => x.type === "image");
  const date = fields.find(x => x.type === "date");
  const items = await blog.getItems();
  for (const it of items) {
    const cov = img && it.fieldData[img.id] && it.fieldData[img.id].value;
    const d = date && it.fieldData[date.id] && it.fieldData[date.id].value;
    console.log(`${it.draft ? "DRAFT" : "LIVE "} ${cov ? "cover" : "NO-COVER"} ${String(d || "").slice(0, 10)} ${it.slug}`);
  }
  const pages = await f.getNodesWithType("WebPageNode");
  console.log("pages:", pages.map(p => p.path).join(" "));
  const changes = await f.getChangedPaths().catch(e => "n/a: " + e.message);
  console.log("unpublished page changes:", JSON.stringify(changes).slice(0, 300));
} finally { await f.disconnect(); }
