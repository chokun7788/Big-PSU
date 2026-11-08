"""Business-scope and corrupted-source regression checks on existing owner cases."""
import copy,json,hashlib,os,sys,time
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.source_decisions import match,unique,current_corrections,verified
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.domain_flow.exact_faq import key
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.contracts import RequestBudget
from app.knowledge.common.answer import CommonAnswerer
db=R/'system/data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
snap=MigratedView(db).snapshot();engine=Engine.from_snapshot(snap);idx=engine.index
at=reference_time('2026-10-25T12:00:00+07:00');checks={};outputs={}
origin=json.loads((R.parent/'r107_owner_questions_20261020/owner_update_50/SOURCE_OWNER_50.json').read_text('utf8'))
questions={i['number']:i['question'] for i in origin['source_items']}
def check(name,condition):checks[name]=bool(condition)
def run(n):
 with patch('urllib.request.urlopen',side_effect=AssertionError('No inference/provider in source-scope checks')):
  result=CommonAnswerer(MigratedView(db)).answer(questions[n],locale='th',at=at,planner=None)
 outputs[n]={'question':questions[n],'answer':result.answer,'artifact':result.decision_artifact}
 return result

check('thai_number_word_and_digit_identity',key(questions[13])==key(questions[13].replace('สี่คน','4 คน')))
check('thai_group_arrival_number_identity',key(questions[49])==key(questions[49].replace('หนึ่งคน','1 คน')))
r=run(27);check('latest_keyboard_permission_with_notification',r.decision_artifact['response_type']=='answer' and 'ใช้ได้' in r.answer and 'ต้องแจ้ง' in r.answer)
check('original_wrong_permission_not_selectable',not any(f['record_id'] in {'migrated_owner_claim_personal_keyboard_mouse','policy_personal_keyboard_mouse'} for f in idx.facts))
check('both_exact_faq_and_typed_policy_corrections_attested',len(current_corrections(idx))==2)
reader=CommonAnswerer(MigratedView(db));oldrid='migrated_owner_claim_personal_keyboard_mouse'
old=reader.finish(snap,time.perf_counter(),'ไม่อนุญาตให้นำคีย์บอร์ดส่วนตัวมาใช้',[],{'record_ids':[oldrid],'requested_fields':['answer'],'method':'controlled_old_compatibility_read'},[],response='answer')
with patch.object(reader,'_answer_unified',return_value=old):
 composed=reader.answer(questions[27],locale='th',at=at,planner=None,_composing=True,_snapshot=snap)
check('composed_child_rejects_old_permission_before_parent_aggregation','ใช้ได้' in composed.answer and 'ต้องแจ้ง' in composed.answer and oldrid not in composed.decision_artifact['query_plan']['record_ids'])
r=run(37);check('update_switch_is_not_generic_cancel_rebook','ไม่ได้' in r.answer and 'จองใหม่' not in r.answer)
r=run(26);check('forgot_logout_is_contact_action','Discord' in r.answer and 'เพจ' in r.answer and 'ไม่เก็บข้อมูล' not in r.answer)
r=run(32);check('seat_count_definition_not_user_audience','เล่นพร้อมกัน' in r.answer and 'ผู้ใช้ใด' not in r.answer)
r=run(50);check('rest_seating_static_not_provider_availability','โซนกลาง' in r.answer and r.decision_artifact['response_type']=='answer')
r=run(35);check('weekly_update_not_current_version_guarantee','จันทร์เช้า' in r.answer and 'ไม่ได้ยืนยัน' in r.answer and r.decision_artifact['response_type']=='partial_answer')
r=run(20);check('fifteen_minute_admission_not_fabricated',r.decision_artifact['response_type']=='partial_answer' and 'ยังไม่มีคำตอบยืนยัน' in r.answer)
r=run(47);check('closure_notification_not_disposition_guarantee',r.decision_artifact['response_type']=='partial_answer' and 'ยังไม่ยืนยัน' in r.answer)
r=run(42);check('underpayment_keeps_required_topup_and_contact','ต้องโอนเพิ่ม' in r.answer and 'หลักฐานการจอง' in r.answer)
r=run(39);check('wrong_phone_not_rebook_or_edit_permission','ไม่ต้องจองใหม่' in r.answer and 'อีเมลต้องถูกต้อง' in r.answer and 'ยังไม่ได้ระบุวิธีแก้ไข' in r.answer)
r=run(12);check('two_person_recommendations_visible_but_not_mode_proof',r.decision_artifact['response_type']=='partial_answer' and all(t in r.answer for t in ['PS5','Nintendo','Tekken 8','It Takes Two','ยังไม่ยืนยันโหมด','PC']))
r=run(11);check('general_friends_get_conditional_two_person_subset','สำหรับมา 2 คน' in r.answer and r.decision_artifact['response_type']=='partial_answer')
base=questions[12]
check('explicit_split_screen_not_owner_recommendation',not match(idx,base+' ต้องเล่นแบบ split-screen พร้อมกัน',at))
check('named_game_mode_not_entire_group_recommendations',not match(idx,'เกม Tekken 8 มีอะไรเล่นสำหรับ 2 คน',at))
check('tournament_does_not_inherit_general_device_permission',not match(idx,questions[27]+' ในการแข่งขัน',at))
check('dated_policy_does_not_infer_effective_year',not match(idx,questions[27]+' ในปี 2025',at))
check('extra_price_request_not_swallowed',not match(idx,questions[27]+' และราคา PC เท่าไหร่',at))
check('unrelated_thai_question_not_swallowed',not match(idx,questions[27]+' กับมีเกมอะไรบ้าง',at))
check('historical_policy_not_inferred_from_current_permission',not match(idx,'เมื่อก่อน '+questions[27],at))
u=Understanding([MeaningTask(questions[12],'games','C04','detail','players_max')],True,'controlled_existing_owner_question')
with patch('urllib.request.urlopen',side_effect=AssertionError('No model in typed subset check')):
 typed=engine.answer(questions[12],'th',at=at,allow_llm=False,budget=RequestBudget(),understanding=u)
check('typed_execution_keeps_limited_adjacent_recommendations',bool(typed['claims']) and typed['status']=='partial' and 'Tekken 8' in typed['answer'])
check('recommendations_do_not_mark_player_mode_obligation_fulfilled',any(not o.get('fulfilled') for t in typed['execution_contract']['tasks'] for o in t['obligations']))
outputs['typed_recommendation_subset']=typed
u=Understanding([MeaningTask(questions[32],'equipment','C03','detail','capacity_persons',questions[32])],True,'controlled_existing_definition_with_numeric_planner_field')
with patch('urllib.request.urlopen',side_effect=AssertionError('No model in definition check')):
 definition=engine.answer(questions[32],'th',at=at,allow_llm=False,budget=RequestBudget(),understanding=u)
check('numeric_planner_field_does_not_erase_seat_definition',bool(definition['claims']) and definition['status']=='partial' and 'เล่นพร้อมกัน' in definition['answer'])
check('seat_definition_does_not_fabricate_numeric_capacity',any(not o.get('fulfilled') for t in definition['execution_contract']['tasks'] for o in t['obligations']))
outputs['typed_definition_not_numeric_capacity']=definition

# Memory-only faults. The answer and mapping must both match immutable source
# pointers; changing metadata or trust without source evidence cannot authorize.
data=copy.deepcopy(engine.data);rid='r130_owner_27_scoped';data['records'][rid]['fields']['answer']['value']['th']='tampered'
bad=Engine(data);check('tampered_answer_removed_from_typed_pool',rid in bad.index.invalid_source_decisions and not bad.index.byrecord[rid])
check('tampered_answer_cannot_use_exact_source_gate',not unique(bad.index,questions[27],at))
data=copy.deepcopy(engine.data);data['records']['policy_personal_keyboard_mouse']['revision']+=1
changed=Engine(data);check('correction_cannot_replace_another_revision',not any(p['record_id']=='policy_personal_keyboard_mouse' for p in current_corrections(changed.index)))
data=copy.deepcopy(engine.data);data['records'].pop(rid);data['facts']=[f for f in data['facts'] if f['record_id']!=rid]
withdrawn=Engine(data);check('withdrawn_permission_not_replayed',not unique(withdrawn.index,questions[27],at))
check('withdrawing_replacement_does_not_revive_attested_migration_error',not any(f['record_id'] in {'migrated_owner_claim_personal_keyboard_mouse','policy_personal_keyboard_mouse'} for f in withdrawn.index.facts))
check('source_database_unchanged_by_tests',before==hashlib.sha256(db.read_bytes()).hexdigest())
out=R/('owner_scope_verification_'+str(time.time_ns()));out.mkdir()
report={'all_passed':all(checks.values()),'checks':checks,'new_benchmark_questions':0,'controlled_fault_mutations_not_new_benchmark':True,'model_inferences':0,'network_calls':0,'database_unchanged':checks['source_database_unchanged_by_tests'],'semantic_accuracy_benchmark':False}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');(out/'READ_OUTPUTS.json').write_text(json.dumps(outputs,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(report,ensure_ascii=False));print(out)
if not report['all_passed']:raise SystemExit(1)
