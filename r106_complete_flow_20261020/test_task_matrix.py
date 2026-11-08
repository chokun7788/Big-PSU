"""32 executable-task contracts on source-backed synthetic schema fixtures."""
import os,sys,json,sqlite3,copy,dataclasses
from pathlib import Path
R=Path(__file__).resolve().parent;T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False);sys.path[:0]=[str(R/'system'),str(R)]
os.environ.update(PSU_COMMON_ALLOW_DEMO='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_ESPORTS_NOW='2026-10-12T15:00:00+07:00')
from datetime import datetime
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
from app.knowledge.common.answer import CommonAnswerer,title
from app.knowledge.common.task_contracts import TASKS
from app.knowledge.common.read_graph import compile,evaluate
from app.knowledge.common.complete_flow import execute,certify
from app.knowledge.common.request_plan import Need,RequestPlan,VERSION,attach
from app.knowledge.common.flow_context import request_context
from task_questions import QUESTIONS
from app.knowledge.common.read_graph import REQUIRED
source=R.parent/'r58_examples_240_20261012/DEMO_ONLY.sqlite';db=T/'SYNTHETIC_TASKS.sqlite'
with sqlite3.connect(source.as_uri()+'?mode=ro',uri=True) as a,sqlite3.connect(db) as b:a.backup(b)
store=CommonStore(db);snapshot=store.snapshot();records=snapshot['release']['records'];at=datetime.fromisoformat('2026-10-12T15:00:00+07:00');reader=CommonAnswerer(store);checks=[];task_rows=[]
for task,contract in TASKS.items():
 try:
  if task=='live_status':
   # The live lane supplies a real task result from a simulated provider; do
   # not pretend static graph readiness proves live availability.
   row={'task':task,'positive_evidence':'test_live_bindings.py owner-added binding and explicit window','negative_evidence':'test_live_bindings.py stale/unmapped/gap','delegated_to_live_lane':True}
   task_rows.append(row);continue
  selected=None
  preferred={'equipment_list':'zone','price':'service','rental':'rental_package','policy':'policy','procedure':'procedure'}
  ordered=sorted(records.items(),key=lambda kv:kv[1]['kind']!=preferred.get(task))
  for rid,r in ordered:
   if r['kind'] not in contract.kinds:continue
   fields=contract.fields
   if task=='schema_attributes':fields=[next(k for k,f in r['fields'].items() if f['status']=='known')]
   graph,ids,edges=compile(task,[rid],records,fields=fields,predicate='service_schedule' if task=='schedule' else task)
   proof=evaluate(graph,snapshot,at)
   if proof['status']=='supported':selected=(rid,graph,ids,edges,proof,fields);break
  if selected is None:
   checks.append({'case':task+' positive source precondition','passed':False,'detail':'No complete graph in the synthetic fixture'});task_rows.append({'task':task,'status':'fixture_precondition_missing'});continue
  rid,graph,ids,edges,proof,fields=selected
  query=title(records[rid],'en')+(' Monday' if task=='schedule' else '')
  n=Need('n1',task,query,query,[rid],[],predicate=task)
  with request_context():
   if task=='schema_attributes':result=reader.execute_task(n.query,snap=snapshot,at=at,lang='en',plan={'record_ids':[rid],'requested_fields':list(fields),'method':'r102_task_matrix_schema_attributes','all_fields':False,'operation':'read','unresolved_clauses':[],'task_plan':{'task':task}})
   else:result=execute(reader,n,snapshot,at,'en')
  passed=result is not None and result.validation.ok and bool(result.answer) and bool(proof['receipts'])
  checks.append({'case':task+' graph and executor positive','passed':passed,'detail':{'root':rid,'targets':ids,'graph_status':proof['status'],'result':dataclasses.asdict(result) if result else None}})
  damaged=copy.deepcopy(snapshot)
  for k in ids:
   for field in damaged['release']['records'][k]['fields'].values():field.update(status='unknown',value=None,evidence_refs=[])
  invalid=evaluate(graph,damaged,at)
  checks.append({'case':task+' missing fields cannot certify graph','passed':invalid['status']!='supported','detail':invalid})
  task_rows.append({'task':task,'root':rid,'read_paths':edges,'source_receipts':proof['receipts'],'positive_passed':passed,'negative_passed':invalid['status']!='supported','natural_language_understanding_tested':False})
  target_rate=next((records[k] for k in ids if records[k]['kind']=='rate'),None)
  audience=records.get(value(target_rate,'audience_id')) if target_rate else None
  for locale in ['th','en','auto']:
   language='en' if locale=='en' else 'th'
   names=title(records[rid],language);a=title(audience,language) if audience else ''
   weekday=value(records[rid],'weekday') if task=='schedule' else 0
   days_th=['จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์','อาทิตย์'];days_en=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
   q=QUESTIONS[task][language=='en'].format(n=names,a=a,d=(days_en if language=='en' else days_th)[weekday or 0])
   for form in [0,1]:
    actual=q if form==0 else (q+' ขอแบบสั้น ๆ' if language=='th' else 'Please explain: '+q)
    from app.pipeline.request_deadline import request_deadline
    from app.core.locale import resolve_locale
    effective_locale=resolve_locale(actual,requested=locale).effective
    with request_deadline(25):natural=reader.answer(actual,locale=effective_locale,at=at,planner=lambda *args:None)
    expected_ids=set(ids)
    if task=='price' and audience:expected_ids={k for k in ids if value(records[k],'audience_id')==audience['record_id']}
    actual_fields={h.get('field') for h in natural.hits if h.get('record_id') in expected_ids} if natural else set()
    required=REQUIRED[task] if task!='schema_attributes' else (tuple(fields),)
    display_only={'contact':(('value',),),'people':(('role',),),'audience':(('eligibility',),),'competition_metadata':(('rulebook_release',),),'rental':(('amount_minor',),)}
    required=display_only.get(task,required)
    if task=='schedule':expected_ids={k for k,r in records.items() if r['kind']=='schedule' and value(r,'weekday')==(weekday or 0)};actual_fields={h.get('field') for h in natural.hits if h.get('record_id') in expected_ids} if natural else set()
    matched=bool(natural and natural.validation.ok and any(set(branch)<=actual_fields for branch in required))
    checks.append({'case':task+' NLU '+locale+' '+str(form),'passed':matched,
      'detail':{'question':actual,'requested_locale':locale,'effective_locale':language,'required_alternatives':required,'actual_fields':sorted(str(x) for x in actual_fields),
        'result':dataclasses.asdict(natural) if natural else None}})
 except Exception as e:
  import traceback
  checks.append({'case':task+' execution','passed':False,'error':str(e),'traceback':traceback.format_exc()});task_rows.append({'task':task,'status':'execution_exception'})
(T/'CHECKS.jsonl').write_text('\n'.join(json.dumps(c,ensure_ascii=False,default=str) for c in checks)+'\n','utf8')
(T/'TASK_MATRIX.json').write_text(json.dumps(task_rows,ensure_ascii=False,indent=2,default=str),'utf8')
summary={'count':len(checks),'passed':sum(x['passed'] for x in checks),'failed':[x['case'] for x in checks if not x['passed']],'tasks':len(task_rows),
 'scope':'executor/graph + task-specific language probes; live task verified in its dedicated lane','llm_enabled':True}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(summary);sys.exit(bool(summary['failed']))
