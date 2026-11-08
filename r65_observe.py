import collections,json,sqlite3,zlib
from pathlib import Path
BASE=Path(__file__).resolve().parent;O=BASE/'r65_detailed_failure_analysis_20261014';B=BASE/'r64_full_comparison_20261013'
c=sqlite3.connect(O/'evidence.sqlite');c.row_factory=sqlite3.Row
with sqlite3.connect((B/'common.sqlite').as_uri()+'?mode=ro',uri=True) as db:
 records={rid:json.loads(payload) for rid,payload in db.execute('SELECT r.record_id,r.payload FROM cc_revisions r JOIN cc_heads h USING(record_id) WHERE r.version=h.head AND h.withdrawn=0')}
(O/'COMMON_RECORDS.json').write_text(json.dumps(records,ensure_ascii=False),encoding='utf-8')
out={};sample=[]
for arm in ('legacy_offline','common_offline','legacy_llm','common_llm'):
 cnt=collections.Counter();methods=collections.Counter();unknown=collections.Counter();v_errors=collections.Counter();sem=collections.Counter();long=collections.Counter();selected_kinds=collections.Counter();audits=collections.Counter()
 for row in c.execute('SELECT raw FROM results WHERE arm=?',(arm,)):
  r=json.loads(zlib.decompress(row['raw']));resp=r.get('result') or {};a=resp.get('decision_artifact') or {};p=a.get('query_plan') or {};ans=resp.get('answer') or ''
  cnt['with_answer']+=bool(ans);cnt['over_2000_chars']+=len(ans)>2000;cnt['over_10000_chars']+=len(ans)>10000;cnt['english_with_Thai_source_marker']+=r.get('effective_locale')=='en' and '[Thai source]' in ans
  methods[p.get('method','no_common_plan')]+=1
  for rid in p.get('record_ids') or []:selected_kinds[records.get(rid,{}).get('kind','unmapped')]+=1
  if p.get('unresolved_clauses'):cnt['unresolved_clauses']+=1
  if p.get('semantic_plan_accepted'):cnt['semantic_plan_accepted_response']+=1
  sem[(p.get('planner_semantic_audit') or {}).get('semantic_status','no_semantic_audit')]+=1
  for ob in a.get('obligations') or []:
   if ob.get('status')!='known':unknown[str(ob.get('status'))+':'+str(ob.get('field'))]+=1
  for v in (resp.get('validation') or {}).get('errors') or []:v_errors[v]+=1
  for t in resp.get('trace') or []:
   if t.get('stage')=='common_query_planner':
    for event in t.get('metadata',{}).get('attempts',[]):
     audits['events']+=1
     for k in ('attempted','transport_ok','schema_accepted','final_plan_accepted'):
      if event.get(k) is True:audits[k]+=1
     semantic=event.get('semantic') or {};audits['semantic:'+semantic.get('semantic_status','absent')]+=1
     if event.get('gate_reason'):audits['gate:'+event['gate_reason']]+=1
   if t.get('stage')=='common_content' and len(ans)>10000:long[t.get('decision')]+=1
 out[arm]={'answer_observations':cnt,'methods':methods,'selected_record_kind_events':selected_kinds,'obligation_status_field_events':unknown,'validation_errors':v_errors,'semantic_status':sem,'planner_audit':audits,'long_response_modes':long}
field=collections.defaultdict(collections.Counter)
for rec in records.values():
 for k,v in rec['fields'].items():field[rec['kind']][v['status']]+=1
out['field_status_by_kind']=dict(field)
out['model_common_llm_comparison']={}
for condition,label in [('a.passed=1 AND b.passed=0','regressed_strict'),('a.passed=0 AND b.passed=1','improved_strict')]:
 rows=c.execute('SELECT b.issues,COUNT(*) n FROM grades a JOIN grades b ON a.key=b.key AND a.file=b.file AND a.rownum=b.rownum AND a.variant=b.variant WHERE a.arm="common_offline" AND b.arm="common_llm" AND '+condition+' GROUP BY b.issues').fetchall()
 out['model_common_llm_comparison'][label]={x['issues']:x['n'] for x in rows}
sessions={}
for m in ('legacy','common'):
 p=B/(m+'_http_protocol_network')/'RESULTS.jsonl';bad=[]
 for line in p.open(encoding='utf-8'):
  x=json.loads(line)
  if not x['passed']:
   response=x.get('response') or {};bad.append({'session':x['session'],'turn':x['turn'],'q':x['question'],'failures':x['failures'],'answer':response.get('answer'),'mode':response.get('mode'),'state':response.get('conversation_state'),'task_contract':response.get('task_contract')})
 sessions[m]=bad
out['failed_http_turns']=sessions
(O/'OBSERVATIONS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
brief={a:{'answers':x['answer_observations'],'methods':x['methods'],'top_validation':x['validation_errors'].most_common(7),'semantics':x['semantic_status']} for a,x in out.items() if a.endswith(('llm','offline'))}
brief['sessions']={m:[{k:v for k,v in x.items() if k not in ('state','task_contract')} for x in vals] for m,vals in sessions.items()};brief['llm_grade_changes']=out['model_common_llm_comparison'];brief['field_status']=out['field_status_by_kind']
print(json.dumps(brief,ensure_ascii=False,indent=2))
