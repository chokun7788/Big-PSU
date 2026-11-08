const assert=require('assert');const fs=require('fs');const path=require('path');
const out=fs.readFileSync(path.join(__dirname,'r56_current_path.txt'),'utf8').trim();
const {requestChat}=require('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/web_chat/chat_request.js');
const response=(status,data)=>({status,ok:status<400,text:async()=>JSON.stringify(data)});
(async()=>{
 const checks=[];
 for(const locale of ['th','en']){
  const messages=[];let calls=[];const data=[response(202,{job_id:'j',session_id:'s',status:'queued',timing:{elapsed_sec:0}}),response(200,{ok:true,status:'running',timing:{elapsed_sec:2}}),response(200,{ok:true,status:'completed',result:{ok:true,answer:'done'},timing:{elapsed_sec:3}})];
  const r=await requestChat({locale},{fetchImpl:async(u,o)=>{calls.push([u,o]);return data.shift()},sleep:async()=>{},onRetry:(x)=>messages.push(x.message)});
  assert.equal(r.data.answer,'done');assert.equal(calls.filter(x=>x[1]?.method==='POST').length,1);
  assert(messages.some(s=>locale==='th'?s.includes('2 วินาที'):s.includes('2 s elapsed')));checks.push({locale,progress_elapsed_visible:true,post_count:1});
 }
 let count=0;await assert.rejects(requestChat({locale:'en'},{fetchImpl:async()=>{count++;throw Error('ambiguous lost network')}}));assert.equal(count,1);checks.push({ambiguous_network_not_replayed:true});
 let called=0;const r=await requestChat({locale:'en'},{fetchImpl:async()=>{called++;return response(202,{job_id:'j',session_id:'s',status:'failed',error:'provider_unavailable'})}});assert.equal(called,1);assert.equal(r.data.retryable,false);checks.push({failed_job_not_replayed:true});
 fs.writeFileSync(path.join(out,'frontend_protocol_tests.json'),JSON.stringify(checks,null,2),{flag:'wx'});process.stdout.write('UI protocol checks '+checks.length+' passed\n');
})().catch(e=>{process.stderr.write(e.stack+'\n');process.exitCode=1});
