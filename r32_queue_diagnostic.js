const fs=require('node:fs');const assert=require('node:assert/strict');
const {requestChat}=require('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/web_chat/chat_request.js');
const report=fs.readFileSync('r32_report_path.txt','utf8').trim();const base='http://127.0.0.1:'+process.argv[2];
(async()=>{
 const health=await (await fetch(base+'/health')).json();assert.equal(health.runtime.version,'2026.10.02-source-content-reliability-r32');
 const rows=await Promise.all(Array.from({length:10},async(_,i)=>{
  const locale=i%2?'th':'en';const question=locale==='th'?'มีเกมอะไรบ้าง':'What games are available?';let retries=0;const started=Date.now();
  try{
   const {response,data}=await requestChat({question,locale:'auto',client_session_id:'r32-client-'+Date.now()+'-'+i,recent_history:[],debug:false,experimental_allow_llm:false,experimental_rag_fallback:false},{fetchImpl:(url,options)=>fetch(base+url,options),onRetry:()=>{retries+=1;}});
   const errors=[];if(response.status!==200)errors.push('http:'+response.status);else{if(response.headers.get('content-language')!==locale||data.language.effective!==locale)errors.push('locale');if(!data.answer.includes('42'))errors.push('catalog_count');}
   return {i,locale,retries,elapsed_ms:Date.now()-started,http_status:response.status,passed:errors.length===0,errors,response:data};
  }catch(e){return {i,locale,retries,passed:false,errors:[String(e)],cause: e.cause ? {name:e.cause.name,message:e.cause.message,code:e.cause.code,errors:e.cause.errors?.map(x=>({code:x.code,message:x.message}))}:null,elapsed_ms:Date.now()-started};}
 }));
 const summary={scope:'Actual ten simultaneous HTTP requests through the same retry helper used by the webpage; simple catalog locale/count oracle, not WordPress load SLA',url:base,total:rows.length,passed:rows.filter(x=>x.passed).length,retries:rows.reduce((n,x)=>n+x.retries,0),rows};
 fs.writeFileSync(report+'/'+process.argv[3]+'_browser_helper_concurrency.json',JSON.stringify(summary,null,2),{flag:'wx'});console.log(JSON.stringify({total:summary.total,passed:summary.passed,retries:summary.retries,rows:rows.map(({i,http_status,retries,elapsed_ms,errors})=>({i,http_status,retries,elapsed_ms,errors}))}));
})().catch(e=>{console.error(e);process.exitCode=1});
