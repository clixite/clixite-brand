const {Resvg}=require('@resvg/resvg-js');const fs=require('fs');
const [,,inp,out,w]=process.argv;
const svg=fs.readFileSync(inp,'utf8');
const r=new Resvg(svg,{fitTo:{mode:'width',value:parseInt(w||'1600')},background:'transparent'});
fs.writeFileSync(out,r.render().asPng());console.log('rendered',out);
