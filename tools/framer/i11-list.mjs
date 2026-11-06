import { connect } from "framer-api";
const f=await connect("https://framer.com/projects/NexApp-copy--37tiwNB9SSyPzkNCFNlD",process.env.FRAMER_API_KEY_ISSUE11landing);
try{const bp=(await f.getCollections()).find(c=>c.name==="Blog Posts");const F=Object.fromEntries((await bp.getFields()).map(x=>[x.name,x.id]));
for(const it of await bp.getItems()){const c=it.fieldData[F["Cover Image"]];console.log(it.draft?"DRAFT":"LIVE ",c&&c.value?"cover":"NO-COVER",String(it.fieldData[F["Published Date"]]?.value||"").slice(0,10),it.slug);}}finally{await f.disconnect();}
