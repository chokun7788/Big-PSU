"""Actual saved two-service plan: a PC proof must not certify PS5 duration."""
import json,os,time
from unittest.mock import patch
from verification_support import R
os.environ.update(PSU_MODEL_FIRST_TRIAL='1',PSU_MODEL_FIRST_PLANNER='compact',PSU_MODEL_FIRST_REVIEW='0')
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.policy_scope import requested_actions
reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/verified_sources.sqlite'));checks={};rows=[]
def ask(q,plan):
 with patch('app.knowledge.common.domain_flow.model_gateway.call',return_value={'message':{'content':plan}}),patch('urllib.request.urlopen',side_effect=AssertionError('No HTTP in source replay')):
  r=reader.answer(q,locale='th',planner=None)
 rows.append({'question':q,'answer':r.answer,'artifact':r.decision_artifact});return r
q='นักศึกษา PSU เล่น PC 30 นาทีราคาเท่าไหร่ และบุคคลทั่วไปเล่น PS5 30 นาทีราคาเท่าไหร่'
checks['price_not_change_service']='change_service' not in requested_actions(q,'C08')
r=ask(q,'[["P",0,5],["P",6,9]]');c=r.decision_artifact['execution_contract'];durations=[x for x in c['verifier_result']['constraint_coverage']['constraints'] if x['kind']=='duration']
checks['two_duration_constraints']=len(durations)==2
checks['pc_duration_verified']=durations[0]['status']=='structurally_supported'
checks['ps5_duration_not_borrowed_from_pc']=durations[1]['status']=='review_required'
checks['duration_has_single_correct_owner']=durations[0]['planned_task_ids']==['t1'] and durations[1]['planned_task_ids']==['t2']
checks['no_false_booking_plan_notice']='ส่วนที่ยังไม่มีแผนประมวลผล' not in r.answer
checks['unverified_second_duration_visible']='ยังยืนยันการใช้เงื่อนไข' in r.answer
checks['pc_price_retained']='0 บาท' in r.answer and 'PSU Student' in r.answer
for text in ['PC ไป PS5 ได้ไหม','เปลี่ยนเครื่องระหว่างเล่นได้ไหม','จาก PC ไปเป็น PS5 ได้ไหม','PC แล้วเปลี่ยนไปเล่น PS5 ได้ไหม','Can I change service after booking?']:
 checks['transition_'+str(len(checks))]='change_service' in requested_actions(text,'C08')
for text in ['ราคา PC และ PS5 เท่าไหร่','PC สำหรับบุคคลทั่วไปกับ PS5 ราคาเท่าไหร่','คนทั่วไปเล่น PC 30 นาที และนักศึกษา PSU เล่น PS5 30 นาทีราคาเท่าไหร่']:
 checks['nontransition_'+str(len(checks))]='change_service' not in requested_actions(text,'C08')
q2='นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท แล้วจองยังไง';r=ask(q2,'[["P",0,6],["B",7,7]]')
checks['normal_price_booking_positive']='0 บาท' in r.answer and 'สลิป' in r.answer
checks['normal_duration_no_false_notice']='ยังยืนยันการใช้เงื่อนไข' not in r.answer
out=R/('numeric_scope_'+str(time.time_ns()));out.mkdir();report={'all_passed':all(checks.values()),'checks':checks,'actual_model_calls':0,'mocked_gateway':True,'scope':'source replay of saved two-service context and independent numeric ownership; not model accuracy'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({'output':str(out),**report}))
assert report['all_passed']
