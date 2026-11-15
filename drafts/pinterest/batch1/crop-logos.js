const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const D=process.argv[2];
const jobs=[
 {src:'14.webp',out:'n14.jpg',crop:[0,0,928,820],blur:[]},
 {src:'16.webp',out:'n16.jpg',crop:[0,0,928,760],blur:[]},
 {src:'17.webp',out:'n17.jpg',crop:[0,0,928,1020],blur:[]},
 {src:'18.webp',out:'n18.jpg',crop:[0,0,690,1232],blur:[]},
];
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const j of jobs){
 const data='data:image/webp;base64,'+fs.readFileSync(path.join(D,'images',j.src)).toString('base64');
 const out=await p.evaluate(async({data,j})=>{const img=new Image();img.src=data;await img.decode();
  const [x,y,w,h]=j.crop;const c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d');
  g.drawImage(img,x,y,w,h,0,0,w,h);
  for(const [cx,cy,r] of j.blur){g.save();g.beginPath();g.arc(cx-x,cy-y,r,0,7);g.clip();g.filter='blur(14px)';g.drawImage(c,0,0);g.drawImage(c,0,0);g.restore();}
  for(const [cx,cy,r,sx,sy] of (j.fill||[])){const d=g.getImageData(sx-x,sy-y,1,1).data;g.save();g.filter='blur(3px)';g.fillStyle=`rgb(${d[0]},${d[1]},${d[2]})`;g.beginPath();g.ellipse(cx-x,cy-y,r,r*0.9,0,0,7);g.fill();g.restore();}
  return c.toDataURL('image/jpeg',0.9);},{data,j});
 fs.writeFileSync(path.join(D,'newimg',j.out),Buffer.from(out.split(',')[1],'base64'));
}
await p.setViewportSize({width:1200,height:700});
fs.writeFileSync(path.join(D,'newimg','sheet.html'),'<body style="margin:0;display:flex;gap:8px;align-items:flex-start">'+jobs.map(j=>`<img src="${j.out}" style="width:290px">`).join('')+'</body>');
await p.goto('file://'+path.join(D,'newimg','sheet.html'));await p.waitForTimeout(400);await p.screenshot({path:path.join(D,'newimg','sheet.png'),fullPage:true});
await b.close();})();
