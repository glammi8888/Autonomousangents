// Sets ONE ISSUE11 blog item live and publishes issue11.app.
// usage: node i11-publish-one.mjs <slug>
// Aborts (changes nothing) if: Megan has unpublished page changes, the item has no cover,
// or the live homepage still shows the template's fake user reviews.
// (Nov 5: narrowed from any "NexApp" text to the review section, after Megan removed the reviews;
// the leftover NexApp footer/download text is a cleanup item, not a fake-review risk.)
// Key: FRAMER_API_KEY_ISSUE11landing (env).
import { connect } from "framer-api";
const slug = process.argv[2];
if (!slug) { console.error("slug required"); process.exit(1); }
const res0 = await fetch("https://issue11.app/?x=" + Date.now()).then(r => r.text()).catch(() => "");
if (/USER REVIEWS|rave about ISSUE11|mariah\.writes|DylanK_92/i.test(res0)) { console.error("ABORT: issue11.app still shows the template's fake reviews. Not publishing."); process.exit(5); }
const f = await connect("https://framer.com/projects/NexApp-copy--37tiwNB9SSyPzkNCFNlD", process.env.FRAMER_API_KEY_ISSUE11landing);
try {
  const ch = await f.getChangedPaths();
  const n = (ch.added || []).length + (ch.removed || []).length + (ch.modified || []).length;
  if (n > 0) { console.error("ABORT: Megan has unpublished page changes:", JSON.stringify(ch)); process.exit(2); }
  const bp = (await f.getCollections()).find(c => c.name === "Blog Posts");
  const F = Object.fromEntries((await bp.getFields()).map(x => [x.name, x.id]));
  const it = (await bp.getItems()).find(i => i.slug === slug);
  if (!it) { console.error("ABORT: no item", slug); process.exit(3); }
  const cov = it.fieldData[F["Cover Image"]];
  if (!(cov && cov.value)) { console.error("ABORT: no cover"); process.exit(4); }
  await bp.addItems([{ id: it.id, slug, draft: false }]);
  const pub = await f.publish();
  const hosts = await f.deploy(pub.deployment.id);
  const after = await bp.getItems();
  console.log("published", slug, "hosts", hosts.map(h => h.hostname || JSON.stringify(h)).join(","), "live:", after.filter(i => !i.draft).length, "drafts:", after.filter(i => i.draft).length);
} finally { await f.disconnect(); }
