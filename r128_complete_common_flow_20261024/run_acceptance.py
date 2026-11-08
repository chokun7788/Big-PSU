import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'));OUT=Path(c['output'])
errors=[]
for n in range(60):
 try:
  with urllib.request.urlopen(c['url']+'/health',timeout=3) as f:json.load(f)
  break
 except OSError:time.sleep(1)
else:raise RuntimeError('Candidate API startup failed')
def call(kind,key,q,session,last='',turn=1):
 row={'kind':kind,'key':key,'turn':turn,'question':q,'started_at':time.time()};before=time.perf_counter();payload={'question':q,'locale':'auto','debug':True,'experimental_rag_fallback':True,'client_session_id':session,'client_turn_id':'turn-'+uuid.uuid4().hex,'last_seen_response_id':last};row['request']=payload
 try:
  req=urllib.request.Request(c['url']+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=195) as f:row['response']=json.load(f)
 except Exception as e:row['error']=repr(e)
 row['wall_sec']=time.perf_counter()-before
 if 'error' in row:errors.append({'key':key,'turn':turn,'error':row['error']})
 with (OUT/'ACCEPTANCE.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 print(json.dumps({'key':key,'turn':turn,'sec':round(row['wall_sec'],3),'answer':row.get('response',{}).get('answer','')[:170],'error':row.get('error')},ensure_ascii=False),flush=True)
 (OUT/'PROGRESS.json').write_text(json.dumps({k:row[k] for k in ['kind','key','turn','wall_sec']},ensure_ascii=False,indent=2),'utf8')
 return row.get('response',{}).get('request_id','')
cases=json.loads((R.parent/'r126_latency_audit_20261023/run_1792765098897050300/CASES.json').read_text('utf8'))
for category,q in cases:call('single',category,q,'r128-'+uuid.uuid4().hex)
for name,qs in json.loads((R.parent/'r127_legacy_current_flow_comparison_20261023/CONVERSATIONS.json').read_text('utf8')):
 session='r128-'+uuid.uuid4().hex;last=''
 for i,q in enumerate(qs,1):last=call('conversation',name,q,session,last,i)
(OUT/'COMPLETE.json').write_text(json.dumps({'completed':not errors,'single':34,'conversation_turns':19,'llm_allowed':True,'full_test':False,'http_errors':errors},indent=2),'utf8');assert not errors
