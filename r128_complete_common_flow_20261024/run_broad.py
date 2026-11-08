import hashlib,json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'));OUT=R/('retained61_'+str(time.time_ns()));OUT.mkdir()
(R/'BROAD_PROCESS.json').write_text(json.dumps({'output':str(OUT),'api':c['url']},indent=2),'utf8')
freeze={str(p.relative_to(R/'system')):hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'system/app').rglob('*.py') if '__pycache__' not in p.parts};(OUT/'SOURCE_FREEZE.json').write_text(json.dumps(freeze,indent=2),'utf8')
jobs=[json.loads(l) for l in (R.parent/'r124_legacy_guided_parity_20261023/ALL_RETAINED_JOBS.jsonl').read_text('utf8').splitlines()]
for i,j in enumerate(jobs,1):
 payload={'question':j['question'],'locale':j.get('locale','auto'),'debug':True,'experimental_rag_fallback':True,'client_session_id':'r128-broad-'+uuid.uuid4().hex,'client_turn_id':'turn-'+uuid.uuid4().hex};before=time.perf_counter();row={'i':i,'key':j['key'],'question':j['question'],'locale':payload['locale'],'started_at':time.time()}
 try:
  req=urllib.request.Request(c['url']+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=195) as f:row['response']=json.load(f)
 except Exception as e:row['error']=repr(e)
 row['wall_sec']=time.perf_counter()-before
 with (OUT/'RESULTS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 (OUT/'PROGRESS.json').write_text(json.dumps({'completed':i,'total':len(jobs),'latest':j['question'],'seconds':row['wall_sec']},ensure_ascii=False,indent=2),'utf8')
 print(json.dumps({'i':i,'key':j['key'][:8],'seconds':round(row['wall_sec'],3),'answer':row.get('response',{}).get('answer','')[:120],'error':row.get('error')},ensure_ascii=False),flush=True)
unchanged=all(hashlib.sha256((R/'system'/p).read_bytes()).hexdigest()==h for p,h in freeze.items())
(OUT/'COMPLETE.json').write_text(json.dumps({'completed':True,'requests':len(jobs),'source_unchanged':unchanged,'full_test':False,'baseline_rerun':False},indent=2),'utf8');assert unchanged
