import collections,json,sqlite3,zlib
from pathlib import Path
BASE=Path(__file__).resolve().parent;O=BASE/'r65_detailed_failure_analysis_20261014';B=BASE/'r64_full_comparison_20261013'
c=sqlite3.connect(O/'evidence.sqlite');c.row_factory=sqlite3.Row
o=json.loads((O/'OBSERVATIONS.json').read_text(encoding='utf-8'));records=json.loads((O/'COMMON_RECORDS.json').read_text(encoding='utf-8'))
def val(r,k):
 f=r['fields'].get(k,{})
 return f.get('value') if f.get('status')=='known' else None
fields={};joins=[]
for kind in ('competition_rule','control_set','rate','schedule','game_service'):
 d=collections.defaultdict(collections.Counter)
 for r in records.values():
  if r['kind']==kind:
   for f,v in r['fields'].items():d[f][v['status']]+=1
 fields[kind]=dict(d)
for r in records.values():
 if r['kind']=='game' and any('counter' in str(x).lower() for x in r.get('aliases',{}).get('en',[])+r.get('aliases',{}).get('th',[])+[str(val(r,'title'))]):
  links=[x for x in records.values() if x['kind']=='game_service' and val(x,'game_id')==r['record_id']]
  joins.append({'game':r['record_id'],'game_service_links':[{'id':x['record_id'],'offered':val(x,'offered'),'service':val(x,'service_id'),'rates':len([y for y in records.values() if y['kind']=='rate' and val(y,'service_id')==val(x,'service_id')])} for x in links]})
diagnostics={}
for arm in ('legacy_offline','common_offline','legacy_llm','common_llm'):
 false_strong=0;schema_unverified=0;confidence8_wrong=0;all_unknown=[];aliasmulti=0
 for row in c.execute('SELECT * FROM grades WHERE arm=?',(arm,)):
  g=json.loads(row['grade_json']);d=g.get('grader_detail') or {}
  if row['passed'] and d.get('strong_outcome_matches') is False:false_strong+=1
 for row in c.execute('SELECT raw FROM results WHERE arm=?',(arm,)):
  r=json.loads(zlib.decompress(row['raw']));resp=r.get('result') or {};a=resp.get('decision_artifact') or {};p=a.get('query_plan') or {};obs=a.get('obligations') or []
  if p.get('method')=='exact' and len(p.get('record_ids') or [])>1:aliasmulti+=1
  if (p.get('planner_semantic_audit') or {}).get('semantic_status')=='schema_only_unverified_intent':schema_unverified+=1
  if resp.get('confidence')==.8 and c.execute('SELECT 1 FROM grades WHERE arm=? AND key=? AND passed=0 AND (issues LIKE "%missing_content%" OR issues LIKE "%validation%" OR issues LIKE "%source_target%") LIMIT 1',(arm,r['key'])).fetchone():confidence8_wrong+=1
  if a.get('response_type')=='answer' and obs and not any(x.get('status')=='known' for x in obs):all_unknown.append(r['key'])
 diagnostics[arm]={'passed_despite_false_strong_outcome_diagnostic':false_strong,'schema_only_unverified_intent_responses':schema_unverified,'confidence_0_8_with_contract_or_gate_failure':confidence8_wrong,'exact_multiple_primary_records':aliasmulti,'answer_type_without_known_obligation':len(all_unknown),'example_keys':all_unknown[:4]}
out={'field_status':fields,'cs2_join_graph':joins,'response_diagnostics':diagnostics,'llm_grade_changes':o['model_common_llm_comparison']}
(O/'EXTRA_METRICS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
print('HTTP FAILURES')
for arm,rows in o['failed_http_turns'].items():
 for x in rows:print(json.dumps({'arm':arm,'s':x['session'],'turn':x['turn'],'q':x['q'],'answer':x['answer'],'failure':x['failures'],'active_task':(x.get('state') or {}).get('active_task')},ensure_ascii=False))
