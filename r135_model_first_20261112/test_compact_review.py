"""Compact plan correction is model-proposed, not a native replacement task."""
import json,os,time,types
from unittest.mock import patch
from verification_support import R
os.environ.update(PSU_MODEL_FIRST_TRIAL='1',PSU_MODEL_FIRST_PLANNER='compact',PSU_MODEL_FIRST_REVIEW='1',PSU_ANALYSIS_BUDGET_SEC='60')
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.plan_review import review
from app.knowledge.common.model_first import parse
reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/verified_sources.sqlite'));index=Engine.from_snapshot(reader.store.snapshot(),cache_key=reader.store.path.resolve()).index
checks={};rows=[]
def response(content):return {'message':{'content':content}}
def ask(name,q,contents):
 with patch('app.knowledge.common.domain_flow.model_gateway.call',side_effect=[response(c) for c in contents]) as call,patch('urllib.request.urlopen',side_effect=AssertionError('No real HTTP')):
  r=reader.answer(q,locale='th',planner=None)
 rows.append({'id':name,'answer':r.answer,'artifact':r.decision_artifact});return r,call.call_count
q='Tekken 8 อยู่โซนไหน แล้ว Tekken 8 มีให้เล่นบนเครื่องอะไรบ้าง'
r,n=ask('wrong_result_type',q,['[["Z",0,2],["C",4,6]]','[["Z",0,2],["S",4,6]]'])
a=r.decision_artifact['model_first'];checks['wrong_type_review_once']=n==2 and a['selected_attempt']==2
checks['repaired_static_source_delivered']='PC Zone' in r.answer and 'PC #01-#02' in r.answer
checks['review_keeps_old_plan_for_audit']=a['initial_validated_needs'][1]['category']=='C05'
q2='มีเกสอะไรบ้าง แล้วจองยังงไ'
r,n=ask('missing_secondary',q2,['[["G",0,1]]','[["G",0,0],["B",1,1]]'])
checks['secondary_need_restored_by_model']=n==2 and len(r.decision_artifact['model_first']['validated_needs'])==2
checks['booking_delivered_after_review']='สลิป' in r.answer
r,n=ask('review_invalid',q2,['[["G",0,1]]','not json'])
checks['invalid_review_no_third_call']=n==2 and r.decision_artifact['model_first']['selected_attempt']==1
checks['partial_supported_subset_retained']='Nintendo Switch' in r.answer and 'ส่วนที่ยังไม่มีแผนประมวลผล' in r.answer
q3='นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท แล้วจองยังไง'
r,n=ask('normal_complete',q3,['[["P",0,6],["B",7,7]]'])
checks['normal_plan_no_extra_call']=n==1 and '0 บาท' in r.answer and 'สลิป' in r.answer
items=parse('[["G",0,1]]',q2);audit={'raw_model_content':'[["G",0,1]]'}
with patch('app.knowledge.common.bounded_time.remaining',return_value=5),patch('app.knowledge.common.domain_flow.model_gateway.call',side_effect=AssertionError('No budget for review')):
 kept,info=review(q2,index,items,audit,types.SimpleNamespace(),{'messages':[]})
checks['low_budget_no_review']=info['plan_review']['attempted'] is False and len(kept)==1
checks['no_native_corrective_tasks_added']=info['native_corrective_tasks_added'] is False
os.environ['PSU_MODEL_FIRST_REVIEW']='guard'
r,n=ask('guard_only_known_conflict',q,['[["Z",0,2],["C",4,6]]'])
checks['guard_only_no_second_call']=n==1
checks['conflict_not_mislabeled_missing_data']='โมเดลยังตีความส่วนนี้ไม่ผ่านการตรวจ' in r.answer and 'PC Zone' in r.answer
checks['conflicting_task_invalid_plan']=r.decision_artifact['execution_contract']['tasks'][1]['terminal_state']=='invalid_plan'
out=R/('compact_review_controls_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'actual_model_calls':0,'mocked_gateway':True,'scope':'bounded review control and source dispatch; not actual model accuracy'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
