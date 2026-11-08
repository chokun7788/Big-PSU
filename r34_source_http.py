import json,sys,urllib.request,time,uuid,collections,hashlib
from pathlib import Path
W=Path(__file__).parent;R=Path((W/'r34_report_path.txt').read_text().strip());run=sys.argv[1];base='http://127.0.0.1:'+sys.argv[2]
for attempt in range(25):
 try:
  health=json.load(urllib.request.urlopen(base+'/health',timeout=3));assert health['runtime']['version']=='2026.10.03-source-task-boundaries-r34';assert all(x['ready'] for x in health['pipeline_workers']['workers']);break
 except Exception:
  if attempt==24:raise
  time.sleep(2)
cases=[]
for name in (sys.argv[3:] or ['R34_SOURCE_REVIEWED_FIXTURE.json','R34_NOVEL_SOURCE_FIXTURE.json']):
 cases+=json.loads((R/name).read_text(encoding='utf-8'))['cases']
counts=collections.defaultdict(collections.Counter);latencies=[]
with (R/(run+'_source_http.jsonl')).open('x',encoding='utf-8') as out:
 for c in cases:
  start=time.perf_counter();errors=[]
  try:
   payload=dict(question=c['question'],locale=c['locale'],recent_history=[],client_session_id='r34-'+uuid.uuid4().hex,debug=True,experimental_allow_llm=True,experimental_rag_fallback=True)
   raw=json.load(urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=30));answer=raw['answer']
   for group in c['required']:
    if not any(w.casefold() in answer.casefold() for w in group):errors.append('missing:'+str(group))
   for w in c['forbidden']:
    if w.casefold() in answer.casefold():errors.append('forbidden:'+w)
   if not any(w in str(raw.get('sources',[])) for w in c['source']):errors.append('wrong_source')
   if raw.get('validation_ok') is False:errors.append('validation')
   if raw.get('language',{}).get('effective')!=c['locale']:errors.append('locale')
  except Exception as e:raw=dict(exception=str(e));errors=['transport:'+str(e)]
  elapsed=time.perf_counter()-start;latencies.append(elapsed);counts[c['group']]['total']+=1;counts[c['group']]['passed']+=not errors
  out.write(json.dumps(dict(case=c,response=raw,passed=not errors,failures=errors,elapsed=elapsed),ensure_ascii=False)+'\n');out.flush()
  if errors:print(dict(id=c['id'],failures=errors),flush=True)
latencies.sort();summary=dict(url=base,health=health,total=len(cases),passed=sum(c['passed'] for c in counts.values()),groups=counts,p50_sec=latencies[len(latencies)//2],p95_sec=latencies[int(len(latencies)*.95)],scope='Actual packaged API, source content and locale; no real booking occupancy oracle. This is regression evidence after fixes, not unseen holdout.')
with (R/(run+'_source_http_summary.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print({k:v for k,v in summary.items() if k!='health'},flush=True)
