import ast,copy,hashlib,json,os,sys,time,traceback
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S));os.environ['PYTHONDONTWRITEBYTECODE']='1'
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask,parse,schema
from app.knowledge.common.domain_flow.context_guard import apply
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.span_provenance import alignment,resolve_span
from app.knowledge.common.domain_flow.authority_resolution import resolve,signature
from app.knowledge.common.domain_flow.contracts import RequestBudget
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.domain_flow.graph_protocol import VERSION
OUT=R/('graph_verification_'+str(time.time_ns()));OUT.mkdir();checks={};details={}
def check(k,v,detail=None):
 checks[k]=bool(v)
 if detail is not None:details[k]=detail
engine=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot());index=engine.index
snapshot={'release_id':engine.data['release_id'],'epoch':engine.data['epoch'],'reference_time':'2026-10-24T12:00:00+07:00'}
def task(q,cat,domain,facet,target='',op='detail',constraints=None):return MeaningTask(q,domain,cat,op,facet,target,constraints or [])
def compile(q,tasks):
 u=Understanding(tasks,True,'structural_fixture');v=apply(q,index,u);return v,compile_request(q,v,index,snapshot)
try:
 q='สำหรับนักศึกษา PSU วันนี้ ราคา PC เท่าไหร่ แล้วจองยังไง'
 u,c=compile(q,[task('ราคา PC เท่าไหร่','C06','service_fee','amount','PC','price_calculate'),task('แล้วจองยังไง','C08','reservation','owner_policy')])
 check('shared_prefix_audience_reaches_both_relevant_tasks',all(any(s.kind=='audience' and s.scope=='shared' for s in t.slots) for t in c.tasks),c.as_dict())
 check('shared_prefix_date_reaches_both_relevant_tasks',all(any(s.kind=='date' for s in t.slots) for t in c.tasks))
 check('request_prefix_edges_have_request_source',all(b.source_task_id=='request' for t in c.tasks for b in t.bindings if b.basis=='shared_prefix'))
 check('shared_context_is_not_execution_dependency',all(not b.execution_dependency for t in c.tasks for b in t.bindings))
 q='สำหรับนักศึกษา PSU ราคา PC เท่าไหร่ และบุคคลทั่วไปจ่ายเท่าไหร่'
 u,c=compile(q,[task('ราคา PC เท่าไหร่','C06','service_fee','amount','PC'),task('บุคคลทั่วไปจ่ายเท่าไหร่','C06','service_fee','amount')])
 check('local_audience_overrides_shared_prefix',not any(s.kind=='audience' and s.scope=='shared' for s in c.tasks[1].slots))
 q='ราคา VR 30 นาที เทียบ 1 ชั่วโมง แล้วจองยังไง'
 u,c=compile(q,[task('ราคา VR 30 นาที เทียบ 1 ชั่วโมง','C06','service_fee','duration_minutes','VR','compare'),task('แล้วจองยังไง','C08','reservation','owner_policy')])
 check('booking_does_not_inherit_comparison_durations',not any(s.kind=='duration' for s in c.tasks[1].slots))
 check('booking_keeps_source_named_service',c.tasks[1].target_span is not None and c.tasks[1].target_span.text=='VR',c.as_dict())
 q='PC ราคาเท่าไหร่ PS5 ราคาเท่าไหร่ และมันมีเกมอะไรบ้าง'
 u,c=compile(q,[task('PC ราคาเท่าไหร่','C06','service_fee','amount','PC'),task('PS5 ราคาเท่าไหร่','C06','service_fee','amount','PS5'),task('และมันมีเกมอะไรบ้าง','C04','games','game_catalog')])
 check('thai_multiple_antecedents_preserve_ambiguity',c.tasks[2].ambiguities and c.tasks[2].target_span is None)
 # Explicit English pronoun matches the same referent compiler path.
 q='PC price, PS5 price, what games does it offer?'
 u,c=compile(q,[task('PC price','C06','service_fee','amount','PC'),task('PS5 price','C06','service_fee','amount','PS5'),task('what games does it offer?','C04','games','game_catalog')])
 check('multiple_antecedents_do_not_choose_last_silently',c.tasks[2].ambiguities and c.tasks[2].target_span is None,c.as_dict())
 x=json.loads((R/'test.jsonl').read_text('utf8').splitlines()[0]);p=copy.deepcopy(x['label']);check('new_wire_parses',parse(json.dumps(p),x['question']).accepted)
 p['shared_bindings']=[{'source_task_id':'t1','target_task_id':'t1','slot':'target','quote':x['question'][:3],'basis':'explicit_anaphor'}]
 check('self_cycle_rejected',not parse(json.dumps(p),x['question']).accepted)
 p=x['label'];bad=copy.deepcopy(p);bad['tasks'][0]['constraints'].append({'slot':'duration','quote':'invented 999 minutes','source_record_id':'','scope':'local'})
 check('invented_source_quote_rejected',not parse(json.dumps(bad),x['question']).accepted)
 check('wire_schema_has_graph_fields',set(schema()['required'])=={'version','focus','context_quotes','tasks','shared_bindings'})
 m=alignment('ราคา PC หนึ่งชั่วโมง','ราคา PC 60 นาที',{'kind':'deterministic_unit_resolution','source_quote':'หนึ่งชั่วโมง'})
 a=resolve_span(m,8,14);check('derived_units_not_claimed_exact_raw',a['status']=='derived_with_provenance' and not a['exact_current_raw_quote'] and not a['semantic_transformation_verified'])
 a=resolve_span(alignment('PC price','PC invented field'),3,17);check('unattested_derived_span_marked_unresolved',a['status']=='unresolved_derivation')
 a=resolve_span(alignment('aß b','ass b'),1,3);check('unicode_casefold_does_not_forge_offsets',a['status']=='unresolved_derivation')
 candidates=next((v for cat in ['C09','C10'] for v in [[f for f in index.bycat[cat] if f.get('facet')=='owner_policy']] if v),[])
 if len(candidates)>=2:
  first=copy.deepcopy(candidates[0]);other=copy.deepcopy(first);other['id']='injected:policy';other['record_id']='injected';other['value']['en']+=' changed condition'
  fake=copy.copy(index);fake.records={**index.records,'injected':copy.deepcopy(index.records[first['record_id']])};fake.records['injected']['record_id']='injected'
  check('english_clause_difference_not_literal_duplicate',signature(fake,first)!=signature(fake,other))
  decision=resolve(fake,[first,other],reference_time(snapshot['reference_time']));check('authority_bit_without_scoped_mapping_does_not_hide_conflict',decision['status']=='conflict')
 check('source_snapshots_available_for_authority_pointer_checks',bool(index.source_pairs))
 check('all_candidate_python_syntax_valid',all(ast.parse(p.read_text('utf-8-sig')) is not None for p in S.rglob('*.py')))
except Exception:
 checks['suite_exception']=False;details['exception']=traceback.format_exc()
result={'all_passed':all(checks.values()),'checks':checks,'details':details,'new_model_inferences':0,'accuracy_benchmark':False}
(OUT/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8');print(json.dumps({k:v for k,v in result.items() if k!='details'},ensure_ascii=False));print(OUT)
if not result['all_passed']:print(json.dumps({k:v for k,v in details.items() if not checks.get(k)},ensure_ascii=False)[:6500]);sys.exit(1)
