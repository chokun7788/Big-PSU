import json,sys,time,urllib.request,uuid,re
from pathlib import Path
ROOT=Path(__file__).parent;R=Path((ROOT/'r33_report_path.txt').read_text().strip());base='http://127.0.0.1:'+sys.argv[1];run=sys.argv[2];cases=json.loads((Path((ROOT/'r32_report_path.txt').read_text().strip())/'R32_POSITIVE_SOURCE_ORACLE.json').read_text(encoding='utf-8'))['cases'];records=[]
health=json.load(urllib.request.urlopen(base+'/health',timeout=10));assert health['runtime']['version']=='2026.10.02-usable-task-frames-r33'
with (R/(run+'_positive_http.jsonl')).open('x',encoding='utf-8') as out:
 for c in cases:
  start=time.perf_counter();payload=dict(question=c['question'],locale=c['locale'],recent_history=[],client_session_id='r32-positive-'+uuid.uuid4().hex,debug=True,experimental_allow_llm=True,experimental_rag_fallback=True)
  raw=json.load(urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=30));errors=[];body=re.sub(r'\s+',' ',raw['answer']).casefold()
  for clause in c['clauses']:
   if re.sub(r'\s+',' ',clause).casefold() not in body:errors.append('missing_complete_clause:'+clause)
  for id in c['source_ids']:
   if not any(h['id']==id for h in raw.get('sources',[])):errors.append('missing_source:'+id)
  if raw.get('language',{}).get('effective')!=c['locale']:errors.append('wrong_locale')
  if raw.get('validation_ok') is False:errors.append('validation_rejected')
  x=dict(case=c,response=raw,elapsed=time.perf_counter()-start,passed=not errors,errors=errors);records.append(x);out.write(json.dumps(x,ensure_ascii=False)+'\n');out.flush()
  print(json.dumps({'id':c['id'],'passed':x['passed'],'errors':errors},ensure_ascii=False),flush=True)
with (R/(run+'_positive_http_summary.json')).open('x',encoding='utf-8') as out:json.dump(dict(url=base,health=health,total=len(records),passed=sum(x['passed'] for x in records)),out,ensure_ascii=False,indent=2)
