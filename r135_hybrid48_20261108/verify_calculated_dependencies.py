"""Total-price dependency must recompute source arithmetic, not trust a number."""
import copy,json,os,time
from unittest.mock import patch
from verification_support import R
out=R/('calculated_dependencies_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'conversation.sqlite')
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.integration import answer as integrated_answer
from app.knowledge.common.domain_flow.execution_dependencies import evaluate
store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False);checks={};details=[]
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
s=create('service','controlled_total_dep_service',{'name':{'th':'บริการอำพัน','en':'Amber service'},'platform':'PC','resource_ids':[],'session_minutes':30,'capacity_min':1,'capacity_max':1})
a=create('audience','controlled_total_dep_audience',{'name':{'th':'กลุ่มอำพัน','en':'Amber visitors'}})
rate=create('rate','controlled_total_dep_rate',{'service_id':s['record_id'],'audience_id':a['record_id'],'amount_minor':10000,'currency':'THB','unit':'per_person','duration_minutes':30,'calculation_rule':'linear'})
book=create('faq','controlled_total_dep_booking',{'question':{'th':'วิธีจอง','en':'How to book'},'answer':{'th':'ส่งแบบฟอร์มอำพัน','en':'Submit the total controlled Amber form.'},'topic':'C08','intent_key':'booking_steps'})
create('game','controlled_total_dep_game',{'title':{'th':'เกมไพลิน','en':'Sapphire game'},'genre':{'th':'แนวทดสอบ','en':'Total controlled Sapphire genre'}})
create('schedule','controlled_total_dep_schedule',{'weekday':0,'open_periods':[{'start':'09:00','end':'17:00'}],'bookable_periods':[{'start':'09:00','end':'16:00'}],'maintenance_periods':[],'zone_ids':[],'service_closed':False,'service_slots':[{'code':'morning','start':'09:00','end':'12:00','state':'open'},{'code':'afternoon','start':'13:00','end':'17:00','state':'open'}]})
view=DraftSnapshotView(store);reader=CommonAnswerer(view);clock='2026-10-26T12:00:00+07:00'
def run(threshold,mode='engine',tail='3 people for 2 sessions',condition=None):
 first='What is the total price of Amber service for Amber visitors '+tail+'?';second=(condition or ('If the total price is below '+str(threshold)+' THB'))+', how do I book Amber service?';third='What genre is Sapphire game?';texts=[first,second,third];tasks=[MeaningTask(first,'service_fee','C06','price_calculate','amount','Amber service'),MeaningTask(second,'reservation','C08','detail','owner_policy','Amber service',canonical_operation='policy.booking_steps'),MeaningTask(third,'games','C04','detail','genre','Sapphire game')]
 if mode!='engine':texts.append('What are Monday opening hours?');tasks.append(MeaningTask(texts[-1],'schedule','C11','detail','open_periods'))
 q='; '.join(texts);proposal=Understanding(tasks,True,'controlled_calculated_dependency',{'model_called':False});e=Engine.from_snapshot(view.snapshot(),cache_key=view.path)
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
  if mode=='engine':r=e.answer(q,'en',at=clock,allow_llm=False,understanding=proposal);answer=r['answer'];contract=r['execution_contract']
  elif mode=='common':
   with patch('app.knowledge.common.domain_flow.native_intents.propose',return_value=None),patch('app.knowledge.common.domain_flow.meaning_review.review',side_effect=lambda q,i,r:r),patch('app.knowledge.common.domain_flow.understanding.interpret',return_value=proposal):r=reader.answer(q,locale='en',at=clock,planner=None)
   answer=r.answer;contract=r.decision_artifact['execution_contract']
  else:r=integrated_answer(reader,q,locale='en',at=clock,planner=None,_understanding=proposal);answer=r.answer;contract=r.decision_artifact['execution_contract']
 details.append({'mode':mode,'question':q,'answer':answer,'contract':contract});return answer,contract,e
for mode in ['engine','integration','common']:
 answer,c,e=run(700,mode);checks[mode+'_source_total_600_allows_booking']='Submit the total controlled Amber form.' in answer;checks[mode+'_independent_game_preserved']='Total controlled Sapphire genre' in answer
 checks[mode+'_source_total_receipt_survives_parent_bridge']=any(calc.get('total_thb')==600 for calc in c['executor_results'][0].get('calculation_receipts',[]))
 checks[mode+'_dependency_names_recomputed_total_600']=any(d.get('verified') and d.get('observed_amount_thb')=='600.0' and d.get('amount_kind')=='calculated_total' for d in c['executor_results'][1].get('dependency_receipts',[]))
 if mode=='common':checks['common_final_people_and_session_constraints_recomputed_from_parent_receipts']=c['verifier_result']['constraint_coverage']['status']=='observed_constraints_verified'
 answer,c,e=run(500,mode);checks[mode+'_source_total_600_does_not_pass_500']='Submit the total controlled Amber form.' not in answer and 'condition is not met' in answer
 if mode!='engine':checks[mode+'_calendar_survives_both_outcomes']='17:00' in answer
answer,c,e=run(700);snap=c['request_plan']['snapshot'];tasks=c['request_plan']['tasks'];question=c['request_plan']['question'];executors=c['executor_results']
for name,change in [('total',lambda x:x.update(total_thb=1)),('people',lambda x:x.update(billing_quantity=1)),('sessions',lambda x:x.update(sessions=9)),('billing_unit',lambda x:x.update(billing_unit='per_group')),('unit_rate',lambda x:x.update(unit_rate_thb=1)),('input_refs',lambda x:x.update(input_claim_refs=[])),('source_refs',lambda x:x.update(evidence_refs=[])),('unit_calc',lambda x:x['unit_calculation'].update(amount_thb=1))]:
 forged=copy.deepcopy(executors);change(forged[0]['calculation_receipts'][0]);checks['forged_'+name+'_receipt_not_gate_authority']=evaluate(e.index,question,tasks,'t2',forged,snap)['outcome']=='unknown'
answer,c,e=run(700,tail='2 machines for 2 sessions');checks['unknown_per_machine_basis_not_a_confirmed_total']='Submit the total controlled Amber form.' not in answer
answer,c,e=run(700,condition='If it is below 700 THB');checks['implicit_pronoun_uses_calculated_total_not_unit_rate']='Submit the total controlled Amber form.' in answer and any(d.get('amount_kind')=='calculated_total' for d in c['executor_results'][1].get('dependency_receipts',[]))
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_and_proposals_not_empirical_model_accuracy':True}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
