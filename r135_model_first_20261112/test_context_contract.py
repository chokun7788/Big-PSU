"""Focused source/contract replay with supplied plans; zero actual model calls."""
import copy,json,os,time
from unittest.mock import patch
from verification_support import R
os.environ['PSU_MODEL_FIRST_TRIAL']='1'
from app.knowledge.common.model_first import parse
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.request_verifier import verify
reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/verified_sources.sqlite'))
q='นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท แล้วจองยังไง'
out=R/('context_contract_'+str(time.time_ns()));out.mkdir();checks={};rows=[]
def ask(name,text,plan):
 with patch('app.knowledge.common.domain_flow.model_gateway.call',return_value={'message':{'content':plan}}),patch('urllib.request.urlopen',side_effect=AssertionError('No HTTP in supplied-plan tests')):
  result=reader.answer(text,locale='th',planner=None)
 rows.append({'id':name,'question':text,'plan':plan,'answer':result.answer,'mode':result.mode,'artifact':result.decision_artifact});return result
r=ask('full_context',q,'[["P",6,6,0,6],["B",7,7,7,7]]')
checks['full_context_price_zero']='0 บาท' in r.answer
checks['booking_delivered']='สลิป' in r.answer
checks['no_false_missing_plan']='ส่วนที่ยังไม่มีแผนประมวลผล' not in r.answer
checks['no_false_duration_notice']='ยังยืนยันการใช้เงื่อนไข' not in r.answer
art=r.decision_artifact;c=art['execution_contract'];tasks=c['request_plan']['tasks']
checks['two_distinct_parent_tasks']=len(tasks)==2 and len({t['id'] for t in tasks})==2
checks['parent_spans_exact']=all(q[t['source_span']['start']:t['source_span']['end']]==t['source_span']['text'] for t in tasks)
checks['context_has_audience_service_duration']=tasks[0]['source_span']['text']=='นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท'
checks['predicates_separate_from_context']=c['literal_context_bindings'][0]['predicate_span']['text']=='เสียกี่บาท'
checks['receipt_task_ids_preserved']=all(l['task_id']==t['id'] for l,t in zip(c['tasks'],tasks)) and bool(c['tasks'][0]['receipts'])
checks['no_semantic_completeness_claim']=c.get('whole_question_semantics_verified') is False
index=Engine.from_snapshot(reader.store.snapshot(),cache_key=reader.store.path.resolve()).index
bad=copy.deepcopy(c);bad['request_plan']['tasks']=bad['request_plan']['tasks'][:1]
omitted=verify(index,q,bad,r.answer)
checks['omitted_booking_still_detected']=bool(omitted['plan_coverage']['uncovered_need_ids'])
bad=copy.deepcopy(c);bad['executor_results'][0]['claims']=[];bad['executor_results'][0]['calculation_receipts']=[];bad['tasks'][0]['receipts']=[]
unproven=verify(index,q,bad,r.answer)
checks['duration_without_source_proof_not_accepted']=any(x['kind']=='duration' and x['status']=='review_required' for x in unproven['constraint_coverage']['constraints'])
r=ask('truncated_context',q,'[["P",6,6],["B",7,7]]')
checks['missing_context_not_silently_repaired']='บริการใด' in r.answer and '0 บาท' not in r.answer
r=ask('unknown_service','บริการ NONEXISTENT ราคาเท่าไหร่ แล้วจองยังไง','[["P",2,2,0,2],["B",3,3,3,3]]')
checks['unknown_service_no_zero_price']='0 บาท' not in r.answer
r=ask('static_two','Tekken 8 อยู่โซนไหน แล้ว Tekken 8 มีให้เล่นบนเครื่องอะไรบ้าง','[["Z",2,2,0,2],["S",6,6,4,6]]')
checks['static_source_positive']='PC Zone' in r.answer and 'PC #01-#02' in r.answer
checks['static_no_missing_plan']='ส่วนที่ยังไม่มีแผนประมวลผล' not in r.answer
r=ask('ready_ambiguity','Tekken 8 อยู่โซนไหน แล้วเครื่องไหนพร้อมให้เล่น Tekken 8 บ้าง','[["Z",2,2,0,2],["R",3,6,3,6]]')
checks['clarification_and_source_retained']='PC Zone' in r.answer and 'หมายถึงเครื่องที่รองรับเกม' in r.answer and 'partial' in r.mode
for name,plan in [('foreign_predicate_context','[["P",6,6,0,7],["B",7,7,7,7]]'),('noncontaining_context','[["P",6,6,0,5]]'),('bool_offset','[["P",true,6,0,6]]'),('forged_number_value','[["P",6,6,0,6,0]]')]:
 try:parse(plan,q);checks[name+'_rejected']=False
 except (ValueError,TypeError,KeyError):checks[name+'_rejected']=True
report={'actual_model_calls':0,'mocked_gateway':True,'all_passed':all(checks.values()),'checks':checks,'scope':'source and contract wiring with supplied predicate/context proposals; not model reasoning accuracy'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'output':str(out),**report}));print(json.dumps([{'id':r['id'],'answer':r['answer']} for r in rows],ensure_ascii=False))
assert report['all_passed']
