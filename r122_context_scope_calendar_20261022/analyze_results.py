"""Summarize actual saved API responses and verification; never run requests."""
import collections,hashlib,json,statistics
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r121_context_planner_training_20261022';A=R/'api02'
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(s) for s in p.read_text('utf8').splitlines()]
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def events(x):
 found={}
 def walk(v):
  if isinstance(v,dict):
   if v.get('id') and 'transport_ok' in v and 'schema_ok' in v:found[v['id']]=v
   for z in v.values():walk(z)
  elif isinstance(v,list):
   for z in v:walk(z)
 walk(x);return list(found.values())
assert read(A/'TEST_COMPLETE.json')['complete']
rs={arm:rows(A/arm/'RESULTS.jsonl') for arm in ['base','trained']}
assert all(len(v)==len({x['key'] for x in v})==8 for v in rs.values())
summary={};locale={}
def score(xs):
 positives=[g for x in xs for g in x['grades'] if g['positive_literal']]
 return {'requests':len(xs),'http_200':sum(x['http_status']==200 for x in xs),'strict_pass':sum(g['passed'] for x in xs for g in x['grades']),'grades':sum(len(x['grades']) for x in xs),'positive_literal_pass':sum(g['literal_passed'] for g in positives),'positive_literal_checks':len(positives),'positive_questions':sum(any(g['positive_literal'] for g in x['grades']) for x in xs),'median_elapsed_sec':statistics.median(x['elapsed_sec'] for x in xs),'semantic_accuracy':None}
for arm,xs in rs.items():
 summary[arm]=score(xs)
 summary[arm]['failure_partition_occurrences']=dict(collections.Counter(k for x in xs for g in x['grades'] for k,values in g.get('partitions',{}).items() for v in values))
 locale[arm]={loc:score([x for x in xs if x['locale']==loc]) for loc in sorted({x['locale'] for x in xs})}
calls=rows(R/'inference02/REQUESTS.jsonl');transport={
 'actual_backend_requests':len(calls),'success':sum(x['transport_ok'] for x in calls),
 'failed':[x for x in calls if not x['transport_ok']],
 'by_stage':dict(collections.Counter(x.get('stage','unknown') for x in calls)),
 'profiles':dict(collections.Counter(x.get('profile',x.get('requested_profile','unknown')) for x in calls))}
proof=read(A/'MODEL_IDENTITY.json');expected=read(OLD/'inference01/SERVER.json')
assert proof['digests']==expected['digests'] and proof['adapter_sha256']==expected['adapter_sha256']
assert all(x.get('provenance',{}).get('adapter_active')==(x.get('stage')=='context' and x.get('profile')=='psu-r121-trained:latest') for x in calls if x['transport_ok'])
assert all(read(p)=={'OLLAMA_URL':'http://127.0.0.1:12121',**{k:'psu-r121-'+arm+':latest' for k in ['PSU_CHATBOT_OLLAMA_MODEL','PSU_KNOWLEDGE_LLM_MODEL','PSU_QUERY_PLANNER_MODEL','PSU_TOOL_ROUTER_MODEL','PSU_INTENT_LLM_MODEL']}} for arm in rs for p in (A/arm).glob('MODEL_ENV_*.json'))
parent=read(R/'PARENT_FREEZE.json');frozen=read(A/'RUN_FREEZE.json')
assert all(sha(Path(p))==h for p,h in {**parent,**frozen}.items())
protected=read(OLD/'PROTECTED_INPUTS.json');assert all(sha(Path(p))==h for p,h in protected.items())
training=read(OLD/'train02/RUN_FREEZE.json');assert all(sha(Path(p))==h for p,h in training.items())
verification={'parent_source_files_unchanged':len(parent),'original_protected_files_unchanged':len(protected),'current_frozen_files_unchanged':len(frozen),'training_frozen_files_unchanged':len(training),'same_adapter_verified':True,'same_model_revision_verified':True,'all_runtime_model_variables_verified':True,'production_installed':False}
old_bykey={x['key']:x for x in rows(OLD/'api02/trained/RESULTS.jsonl')}
report=['# R122 revision02 — คำถามเดิมผ่าน API จริง','', '8 คำถามต่อแขน ใช้ Flow และฐานข้อมูลเดียวกัน เปลี่ยน adapter เฉพาะ context stage; คำถามเคยใช้พัฒนาแล้ว จึงไม่ใช่ fresh holdout หรือ Full Test','', '## ตัวเลข','', '```json',json.dumps({'scores':summary,'by_locale':locale,'model_transport':transport,'verification':verification},ensure_ascii=False,indent=2),'```','', '## คำตอบและหลักฐานรายข้อ','']
for b,t in zip(rs['base'],rs['trained']):
 assert b['key']==t['key']
 report+=['### '+b['question'],'',f"key: `{b['key']}`; locale: {b['locale']}",'']
 for label,x in [('R121 trained ที่บันทึกไว้ (มีข้อจำกัด config เดิม)',old_bykey[b['key']]),('R122 base',b),('R122 trained',t)]:
  ev=events(x['response'].get('decision_artifact',{}))
  report+=['#### '+label,'',x['response'].get('answer') or '(ไม่มีคำตอบ)','',f"HTTP {x['http_status']}; {x['elapsed_sec']} วินาที",'', 'แผน/การตรวจบริบท:', '```json',json.dumps([{k:e.get(k) for k in ['stage','reason','schema_ok','transport_ok','raw_content','independent_subtask_reviews','context_scope_review','model_provenance']} for e in ev],ensure_ascii=False,indent=2),'```','','ผลเกณฑ์เดิม:','```json',json.dumps(x['grades'],ensure_ascii=False,indent=2),'```','']
(R/'API_PER_REQUEST_TH.md').write_text('\n'.join(report),'utf8')
for name,value in [('API_COMPARISON.json',{'scores':summary,'by_locale':locale,'model_transport':transport}),('FINAL_VERIFICATION.json',verification)]:
 (R/name).write_text(json.dumps(value,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'scores':summary,'transport':transport,'verification':verification},ensure_ascii=False,indent=2))
