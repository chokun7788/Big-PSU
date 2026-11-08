"""Actual output-dependent tasks, source outcomes and independent siblings."""
import json,time,os,copy
from unittest.mock import patch
from verification_support import R
out=R/('execution_dependencies_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'conversation.sqlite')
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False);checks={};details=[]
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
service=create('service','controlled_dependency_service',{'name':{'th':'บริการอำพัน','en':'Amber service'},'platform':'PC','resource_ids':[],'session_minutes':30,'capacity_min':1,'capacity_max':1})
audience=create('audience','controlled_dependency_audience',{'name':{'th':'กลุ่มทดสอบ','en':'Amber visitors'}})
rate=create('rate','controlled_dependency_rate',{'service_id':service['record_id'],'audience_id':audience['record_id'],'amount_minor':10000,'currency':'THB','unit':'per_session','duration_minutes':30})
book=create('faq','controlled_dependency_booking',{'question':{'th':'วิธีจอง','en':'How to book'},'answer':{'th':'ส่งแบบฟอร์มอำพัน','en':'Submit the controlled Amber booking form.'},'topic':'C08','intent_key':'booking_steps'})
game=create('game','controlled_dependency_game',{'title':{'th':'เกมไพลิน','en':'Sapphire game'},'genre':{'th':'แนวเกมทดสอบ','en':'Controlled Sapphire genre'}})
view=DraftSnapshotView(store);clock='2026-10-26T12:00:00+07:00'
def run(condition,extra_price=False):
 e=Engine.from_snapshot(view.snapshot(),cache_key=view.path)
 first='What is the price of Amber service for Amber visitors?';second=condition+', how do I book Amber service?';third='What genre is Sapphire game?';q='; '.join([first,second,third])
 tasks=[MeaningTask(first,'service_fee','C06','detail','amount','Amber service'),MeaningTask(second,'reservation','C08','detail','owner_policy','Amber service',canonical_operation='policy.booking_steps'),MeaningTask(third,'games','C04','detail','genre','Sapphire game')]
 if extra_price:
  extra='How much does Sapphire service cost for Amber visitors?';tasks.insert(1,MeaningTask(extra,'service_fee','C06','detail','amount','Sapphire service'));q='; '.join([first,extra,second,third])
 from app.knowledge.common.domain_flow.capabilities import dispatch
 calls=[]
 def tracked(engine,task,meaning,question,at):calls.append({'id':task.id,'category':task.category});return dispatch(engine,task,meaning,question,at)
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')),patch('app.knowledge.common.domain_flow.capabilities.dispatch',side_effect=tracked):r=e.answer(q,'en',at=clock,allow_llm=False,understanding=Understanding(tasks,True,'controlled_source_dependencies',{'model_called':False}))
 r['controlled_dispatch_calls']=calls
 details.append({'condition':condition,'result':r});return r
r=run('If it is below 150 THB');checks['conditional_has_real_execution_dependency']=bool(r['execution_contract']['request_plan']['tasks'][1]['execution_dependencies']);checks['true_condition_delivers_booking']='Submit the controlled Amber booking form.' in r['answer'];checks['independent_game_still_delivered']='Controlled Sapphire genre' in r['answer']
checks['independent_typed_read_precedes_dependent_dispatch']=[c['id'] for c in r['controlled_dispatch_calls']]==['t1','t3','t2']
checks['true_condition_has_independent_verifier_proof']=any(c['kind']=='condition' and c['status']=='structurally_supported' and c['proof'][0]['outcome']=='true' for c in r['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
from app.knowledge.common.domain_flow.execution_dependencies import evaluate
from app.knowledge.common.domain_flow.request_verifier import verify
e=Engine.from_snapshot(view.snapshot(),cache_key=view.path);contract=r['execution_contract'];snapshot=contract['request_plan']['snapshot'];tasks=contract['request_plan']['tasks'];executors=contract['executor_results'];question=contract['request_plan']['question']
forged=copy.deepcopy(tasks);forged[1]['execution_dependencies'][0]['threshold']='0';checks['forged_threshold_not_authorized_by_stored_receipt']=evaluate(e.index,question,forged,'t2',executors,snapshot)['outcome']=='unknown'
forged_contract=copy.deepcopy(contract);forged_contract['executor_results'][1]['dependency_receipts'][0].update(outcome='false',verified=True);v=verify(e.index,question,forged_contract,r['answer'],r['needs']);checks['verifier_recomputes_instead_of_trusting_false_outcome_flag']=not any(n['status']=='conditional_not_applicable' for n in v['plan_coverage']['needs'])
changed=copy.copy(e.index);changed.snapshot_identity={**changed.snapshot_identity,'epoch':999};checks['changed_epoch_invalidates_dependency_proof']=evaluate(changed,question,tasks,'t2',executors,snapshot)['reason']=='dependency_source_snapshot_changed'
changed=copy.copy(e.index);changed.records=copy.deepcopy(e.index.records);changed.records[rate['record_id']]['fields']['amount_minor']['value']=1000;checks['source_pointer_change_not_hidden_by_old_numeric_claim']=evaluate(changed,question,tasks,'t2',executors,snapshot)['outcome']=='unknown'
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.context_guard import apply
u=Understanding([MeaningTask(t['source_span']['text'],{'C06':'service_fee','C08':'reservation','C04':'games'}[t['category']],t['category'],t['operation'],t['facet'],(t.get('target_span') or {}).get('text','')) for t in tasks],True,'controlled_cycle')
compiled=compile_request(question,apply(question,e.index,u),e.index,snapshot);compiled.tasks[1].execution_dependencies[0]['source_task_id']='t2'
try:compiled.validate();checks['self_cycle_rejected_before_execution']=False
except ValueError:checks['self_cycle_rejected_before_execution']=True
from app.knowledge.common.domain_flow.native_contract import invalidate
invalidated=invalidate(contract);checks['snapshot_retry_withdraws_dependency_receipts']=not any(x.get('dependency_receipts') for x in invalidated['executor_results']) and not any(x.get('dependency_receipts') for x in invalidated['tasks'])
r=run('If it is below 50 THB');checks['false_condition_does_not_deliver_booking']=not any(c['record_id']==book['record_id'] for c in r['claims']);checks['false_condition_explained']='condition is not met' in r['answer'];checks['false_condition_preserves_independent_price_and_game']={rate['record_id'],game['record_id']}<={c['record_id'] for c in r['claims']}
checks['false_condition_does_not_call_dependent_reader']=all(c['category']!='C08' for c in r['controlled_dispatch_calls'])
checks['false_condition_has_distinct_not_applicable_completion']=r['execution_contract']['executor_results'][1]['completeness']['kind']=='conditional_not_applicable' and any(n['status']=='conditional_not_applicable' for n in r['execution_contract']['verifier_result']['plan_coverage']['needs'])
for condition,key in [('If the price is affordable','unsupported_condition'),('If it is below 150 THB, and if I pay cash','unsupported_compound_condition')]:
 r=run(condition);checks[key+'_withheld_without_reader']=not any(c['category']=='C08' for c in r['controlled_dispatch_calls']) and not any(c['record_id']==book['record_id'] for c in r['claims'])
r=run('If the price is below 150 THB');checks['output_price_condition_not_an_extra_price_request']=len(r['execution_contract']['request_plan']['tasks'])==3 and sum(t['category']=='C06' for t in r['execution_contract']['request_plan']['tasks'])==1
r=run('If the total price is below 150 THB');checks['total_condition_requires_calculation_prerequisite_not_unit_assumption']=not any(c['category']=='C08' for c in r['controlled_dispatch_calls']) and any(d.get('reason')=='calculation_prerequisite_required' for e in r['execution_contract']['executor_results'] for d in e.get('dependency_receipts',[]))
r=run('If yes');checks['undeclared_affirmative_output_not_silently_independent']=not any(c['category']=='C08' for c in r['controlled_dispatch_calls']) and any(e['status']=='unsupported_operation' for e in r['execution_contract']['executor_results'])
for condition,wanted in [('If it is below 100 THB',False),('If it is at most 100 THB',True),('If it is above 100 THB',False),('If it is over 99 THB',True),('If it is at least 100 THB',True),('If it is equal to 100 THB',True),('ถ้าราคาไม่เกิน 100 บาท',True)]:
 r=run(condition);checks['comparison_boundary_'+condition]=any(c['record_id']==book['record_id'] for c in r['claims']) is wanted
r=run('ถ้าราคาต่ำกว่า 150 บาท');checks['thai_source_price_condition_uses_same_dependency_flow']='Submit the controlled Amber booking form.' in r['answer'] and any(c['kind']=='condition' and c['status']=='structurally_supported' for c in r['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
second_service=create('service','controlled_dependency_second_service',{'name':{'th':'บริการไพลิน','en':'Sapphire service'},'platform':'PS5','resource_ids':[],'session_minutes':30,'capacity_min':1,'capacity_max':1});create('rate','controlled_dependency_second_rate',{'service_id':second_service['record_id'],'audience_id':audience['record_id'],'amount_minor':20000,'currency':'THB','unit':'per_session','duration_minutes':30})
r=run('If it is below 150 THB',extra_price=True);checks['multiple_price_antecedents_do_not_choose_last']=not any(c['category']=='C08' for c in r['controlled_dispatch_calls']) and 'Which price option' in r['answer']
edit=copy.deepcopy(rate);edit['fields']['amount_minor']={'status':'unknown','value':None,'evidence_refs':[],'note':'Controlled unavailable amount'};save_owner_record(store,edit,edit['revision'],'controlled-test')
r=run('If it is below 150 THB');checks['unknown_prerequisite_does_not_deliver_booking']=not any(c['record_id']==book['record_id'] for c in r['claims']);checks['unknown_prerequisite_preserves_independent_game']=any(c['record_id']==game['record_id'] for c in r['claims'])
checks['unknown_prerequisite_does_not_call_dependent_reader']=all(c['category']!='C08' for c in r['controlled_dispatch_calls'])
checks['known_service_missing_amount_is_source_gap_not_repeat_service_question']=r['needs'][0]['execution_contract']['terminal_state']=='missing_source' and 'rate_not_recorded_for_bound_service' in r['needs'][0]['execution_contract']['reason_codes'] and 'Which service' not in r['needs'][0]['answer']
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_real_business_data':True}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
