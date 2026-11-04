import { connect } from "framer-api";
const URL="https://framer.com/projects/NexApp-copy--37tiwNB9SSyPzkNCFNlD";
const add=process.argv[2]==="add";
const f=await connect(URL, process.env.FRAMER_API_KEY_ISSUE11landing);
try{
  const cols=await f.getCollections();
  for(const c of cols){const it=await c.getItems();console.log("collection:",c.name,"items:",it.length);}
  const bp=cols.find(c=>c.name==="Blog Posts");
  if(!bp){console.log("NO Blog Posts collection");}
  else{
    let fields=await bp.getFields();
    console.log("Blog Posts fields:",fields.map(x=>`${x.name}(${x.type})`).join(", "));
    if(add && !fields.some(x=>x.name==="FAQ Schema")){
      await bp.addFields([{type:"string",name:"FAQ Schema"}]);
      fields=await bp.getFields();
      console.log("AFTER:",fields.map(x=>`${x.name}(${x.type})`).join(", "));
    }
  }
}finally{await f.disconnect();}
