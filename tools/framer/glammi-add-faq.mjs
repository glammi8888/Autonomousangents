// usage: node glammi-add-faq.mjs <slug> <qa.json>  qa.json = [{q,a}]  Inserts H3+P at end of FAQ section + FAQ Schema. Keeps draft state.
import { connect } from "framer-api"; import fs from "fs";
const [slug, qaFile] = process.argv.slice(2); const qa = JSON.parse(fs.readFileSync(qaFile, "utf8"));
const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;");
const f = await connect("https://framer.com/projects/Deliver-copy--CbF2PXgyZOvOV1SmANju-9HzHo", process.env.FRAMER_API_KEY_GLAMMI);
try {
  const blog = (await f.getCollections()).find(c => c.id === "R4mgLoqyF");
  const F = Object.fromEntries((await blog.getFields()).map(x => [x.name, x.id]));
  const it = (await blog.getItems()).find(i => i.slug === slug);
  let c = it.fieldData[F["Content"]].value; const sch = JSON.parse(it.fieldData[F["FAQ Schema"]].value);
  const h = c.lastIndexOf("Frequently Asked Questions</h2>"); if (h < 0) throw "no FAQ h2";
  const end = c.indexOf('<p dir="auto"><strong>', h); if (end < 0) throw "no end marker";
  const todo = qa.filter(x => !c.includes(">" + esc(x.q) + "<"));
  const add = todo.map(x => `<h3 dir="auto">${esc(x.q)}</h3><p dir="auto">${esc(x.a)}</p>`).join("");
  c = c.slice(0, end) + add + c.slice(end);
  for (const x of todo) sch.mainEntity.push({ "@type": "Question", name: x.q, acceptedAnswer: { "@type": "Answer", text: x.a } });
  await blog.addItems([{ id: it.id, slug, draft: it.draft, fieldData: {
    [F["Content"]]: { type: "formattedText", value: c, contentType: "html" },
    [F["FAQ Schema"]]: { type: "string", value: JSON.stringify(sch) } } }]);
  const now = (await blog.getItems()).find(i => i.slug === slug);
  console.log("added", todo.length, "draft:", now.draft, "faqCount:", JSON.parse(now.fieldData[F["FAQ Schema"]].value).mainEntity.length);
} finally { await f.disconnect(); }
