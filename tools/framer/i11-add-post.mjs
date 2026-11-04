// usage: node i11-add-post.mjs <html> <slug> <date YYYY-MM-DD> <imageUrl|""> "<alt>"
// Always creates/updates the item as a DRAFT.
import { connect } from "framer-api"; import fs from "fs";
const [html,slug,date,img,alt]=process.argv.slice(2);
const src=fs.readFileSync(html,"utf8");
const title=src.match(/<title>(.*?)<\/title>/)[1].replace(/\s*\|\s*ISSUE11$/,"").replace(/&amp;/g,"&");
const seoTitle=src.match(/<title>(.*?)<\/title>/)[1].replace(/&amp;/g,"&");
const desc=src.match(/<meta name="description" content="([^"]*)"/)[1];
const faq=src.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1].trim();
let body=src.split("<body>")[1].split("</body>")[0].replace(/<script[\s\S]*?<\/script>/g,"").replace(/<!--[\s\S]*?-->/g,"").trim();
const f=await connect("https://framer.com/projects/NexApp-copy--37tiwNB9SSyPzkNCFNlD", process.env.FRAMER_API_KEY_ISSUE11landing);
try{
  const bp=(await f.getCollections()).find(c=>c.name==="Blog Posts");
  const F=Object.fromEntries((await bp.getFields()).map(x=>[x.name,x.id]));
  const existing=(await bp.getItems()).find(i=>i.slug===slug);
  const fd={
    [F["Title"]]:{type:"string",value:title},
    [F["Excerpt"]]:{type:"string",value:desc},
    [F["Published Date"]]:{type:"date",value:date},
    [F["Author"]]:{type:"string",value:"ISSUE11"},
    [F["Content"]]:{type:"formattedText",value:body,contentType:"html"},
    [F["SEO Title"]]:{type:"string",value:seoTitle},
    [F["SEO Description"]]:{type:"string",value:desc},
    [F["FAQ Schema"]]:{type:"string",value:faq},
  };
  if(img) fd[F["Cover Image"]]={type:"image",value:img,alt};
  const item={slug,draft:true,fieldData:fd}; if(existing) item.id=existing.id;
  await bp.addItems([item]);
  const now=(await bp.getItems()).find(i=>i.slug===slug);
  const cov=now.fieldData[F["Cover Image"]];
  console.log("saved",slug,"draft:",now.draft,"cover:",cov&&cov.value?String(cov.value.url||cov.value).slice(0,90):"none");
}finally{await f.disconnect();}
