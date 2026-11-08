const assert = require('assert');
const {requestChat} = require('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/web_chat/chat_request.js');
function response(status, data) {return {status,ok:status>=200&&status<300,text:async()=>JSON.stringify(data)};}
const payload={question:'Explain latency.',locale:'en',client_session_id:'session-abcdefghijk',client_turn_id:'turn-abcdefghijk'};
(async()=>{
 const calls=[],states=[];
 const responses=[response(202,{job_id:'job1',session_id:payload.client_session_id,status:'queued'}),response(200,{ok:true,status:'running'}),response(200,{ok:true,status:'completed',result:{ok:true,answer:'Network delay.'}})];
 const completed=await requestChat(payload,{fetchImpl:async(url,args)=>{calls.push({url,args});return responses.shift();},sleep:async()=>{},onRetry:data=>states.push(data.job_status)});
 assert.equal(completed.data.answer,'Network delay.');assert.equal(calls.filter(c=>c.args?.method==='POST').length,1);
 assert.deepEqual(states,['queued','running','completed']);
 let calls2=0;
 const old=[response(404,{error:'jobs_disabled'}),response(503,{ok:false,retryable:true,error:'server_busy'}),response(200,{ok:true,answer:'Old endpoint works.'})];
 const result2=await requestChat(payload,{fetchImpl:async()=>{calls2++;return old.shift();},sleep:async()=>{}});
 assert.equal(result2.data.answer,'Old endpoint works.');assert.equal(calls2,3);
 let attempts=0;
 await assert.rejects(requestChat(payload,{fetchImpl:async()=>{attempts++;throw new Error('ambiguous transport failure');}}));
 assert.equal(attempts,1);
 const expired=[response(202,{job_id:'job2',session_id:payload.client_session_id,status:'queued'}),response(200,{ok:true,status:'failed',error:'queue_expired'})];
 const fail=await requestChat(payload,{fetchImpl:async()=>expired.shift(),sleep:async()=>{}});
 assert.equal(fail.data.ok,false);assert.equal(fail.data.error,'queue_expired');
 console.log('PASS browser request: durable polling, one submission, disabled fallback, bounded rejection retry, no ambiguous replay, expiry');
})().catch(e=>{console.error(e);process.exitCode=1;});
