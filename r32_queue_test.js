const assert = require('node:assert/strict');
const {requestChat} = require('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/web_chat/chat_request.js');
function response(status,data,raw) {return {status,ok:status===200,text:async()=>raw??JSON.stringify(data)};}
async function scenario(items) {
 let sent=[],delays=[],notices=[],clock=0;
 const result=await requestChat({question:'PC1 free?',recent_history:[],client_session_id:'independent-test'}, {
  fetchImpl:async(url,init)=>{sent.push({url,body:init.body});const item=items.shift();if(item instanceof Error)throw item;return item;},
  sleep:async ms=>{delays.push(ms);clock+=ms;}, now:()=>clock, onRetry:(d,n)=>notices.push(n)
 });return {result,sent,delays,notices};
}
(async()=>{
 const busy={ok:false,error:'server_busy',retryable:true,retry_after_ms:250};
 let x=await scenario([response(503,busy),response(200,{ok:true,answer:'available'})]);
 assert.equal(x.sent.length,2);assert.deepEqual(x.delays,[250]);assert.equal(x.sent[0].body,x.sent[1].body);assert.equal(x.result.data.answer,'available');
 x=await scenario([response(503,busy),response(503,busy),response(503,busy)]);assert.equal(x.sent.length,3);assert.equal(x.result.response.status,503);
 for (const data of [{...busy,retryable:false},{...busy,error:'internal_error'},{...busy,error:'pipeline_timeout'}]) {
  x=await scenario([response(503,data)]);assert.equal(x.sent.length,1);assert.equal(x.delays.length,0);
 }
 x=await scenario([response(500,busy)]);assert.equal(x.sent.length,1);
 x=await scenario([response(503,{...busy,retry_after_ms:1e10}),response(200,{ok:true})]);assert.deepEqual(x.delays,[1500]);
 await assert.rejects(scenario([new Error('network')]),/network/);
 await assert.rejects(scenario([response(503,null,'<html>')]),/non-JSON/);
 console.log('queue protocol: 9 scenarios passed (bounded retries, identical payload, no replay on ambiguous failure)');
})().catch(e=>{console.error(e);process.exitCode=1;});
