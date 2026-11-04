// usage: node i11-set-cover.mjs <slug> <local.jpg> "<alt>"  (keeps draft state)
import { connect } from "framer-api"; import fs from "fs";
const [slug,file,alt]=process.argv.slice(2);
const f=await connect("https://framer.com/projects/NexApp-copy--37tiwNB9SSyPzkNCFNlD", process.env.FRAMER_API_KEY_ISSUE11landing);
try{
  const asset=await f.uploadImage({image:{bytes:new Uint8Array(fs.readFileSync(file)),mimeType:"image/jpeg"},name:slug+"-cover",altText:alt});
  const bp=(await f.getCollections()).find(c=>c.name==="Blog Posts");
  const F=Object.fromEntries((await bp.getFields()).map(x=>[x.name,x.id]));
  const it=(await bp.getItems()).find(i=>i.slug===slug);
  await bp.addItems([{id:it.id,slug,draft:true,fieldData:{[F["Cover Image"]]:{type:"image",value:asset.url,alt}}}]);
  const now=(await bp.getItems()).find(i=>i.slug===slug);
  console.log("cover set:",String(now.fieldData[F["Cover Image"]].value.url||now.fieldData[F["Cover Image"]].value).slice(0,80),"draft:",now.draft);
}finally{await f.disconnect();}
