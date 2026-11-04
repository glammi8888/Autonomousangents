// Sets ONE Glammi blog item live and publishes the site to production.
// usage: node glammi-publish-one.mjs <slug>
// Aborts if Megan has unpublished page changes, or if the item has no cover.
import { connect } from "framer-api";
const slug = process.argv[2];
if (!slug) { console.error("slug required"); process.exit(1); }
const URL = "https://framer.com/projects/Deliver-copy--CbF2PXgyZOvOV1SmANju-9HzHo";
const f = await connect(URL, process.env.FRAMER_API_KEY_GLAMMI);
try {
  const ch = await f.getChangedPaths();
  const n = (ch.added || []).length + (ch.removed || []).length + (ch.modified || []).length;
  if (n > 0) { console.error("ABORT: unpublished page changes:", JSON.stringify(ch)); process.exit(2); }
  const blog = (await f.getCollections()).find(c => c.id === "R4mgLoqyF");
  const img = (await blog.getFields()).find(x => x.type === "image");
  const it = (await blog.getItems()).find(i => i.slug === slug);
  if (!it) { console.error("ABORT: no item", slug); process.exit(3); }
  if (!(img && it.fieldData[img.id] && it.fieldData[img.id].value)) { console.error("ABORT: no cover"); process.exit(4); }
  await blog.addItems([{ id: it.id, slug, draft: false }]);
  const res = await f.publish();
  const hosts = await f.deploy(res.deployment.id);
  const after = await blog.getItems();
  console.log("published", slug, "deployment", res.deployment.id, "hosts", hosts.map(h => h.hostname || h.url || JSON.stringify(h)).join(","));
  console.log("live now:", after.filter(i => !i.draft).length, "drafts:", after.filter(i => i.draft).length);
} finally { await f.disconnect(); }
