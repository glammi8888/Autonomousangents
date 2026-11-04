import { connect } from "framer-api";
const slug=process.argv[2];
const f=await connect("https://framer.com/projects/NexApp-copy--37tiwNB9SSyPzkNCFNlD", process.env.FRAMER_API_KEY_ISSUE11landing);
try{ const bp=(await f.getCollections()).find(c=>c.name==="Blog Posts");
 const it=(await bp.getItems()).find(i=>i.slug===slug);
 await bp.addItems([{id:it.id,slug,draft:true}]);
 const now=(await bp.getItems()).find(i=>i.slug===slug); console.log(slug,"draft:",now.draft);
 const pi=await f.getPublishInfo().catch(()=>null); console.log("publish info:",JSON.stringify(pi).slice(0,300));
}finally{await f.disconnect();}
