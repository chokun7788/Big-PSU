"""Public Common/integration native compound paths must honor the same gates."""
import copy,json,time,os
from unittest.mock import patch
from verification_support import R
out=R/('execution_dependency_native_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'conversation.sqlite')
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.integration import answer as integrated_answer
from app.knowledge.common.flow_context import CURRENT
store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False);checks={};details=[]
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
s=create('service','controlled_native_dep_service',{'name':{'th':'บริการอำพัน','en':'Amber service'},'platform':'PC','resource_ids':[],'session_minutes':30,'capacity_min':1,'capacity_max':1})
a=create('audience','controlled_native_dep_audience',{'name':{'th':'กลุ่มอำพัน','en':'Amber visitors'}})
rate=create('rate','controlled_native_dep_rate',{'service_id':s['record_id'],'audience_id':a['record_id'],'amount_minor':10000,'currency':'THB','unit':'per_session','duration_minutes':30})
book=create('faq','controlled_native_dep_book',{'question':{'th':'วิธีจอง','en':'How to book'},'answer':{'th':'ส่งแบบฟอร์มอำพัน','en':'Submit the native controlled Amber form.'},'topic':'C08','intent_key':'booking_steps'})
create('game','controlled_native_dep_game',{'title':{'th':'เกมไพลิน','en':'Sapphire game'},'genre':{'th':'แนวเกมทดสอบ','en':'Native controlled Sapphire genre'}})
create('schedule','controlled_native_dep_schedule',{'weekday':0,'open_periods':[{'start':'09:00','end':'17:00'}],'bookable_periods':[{'start':'09:00','end':'16:00'}],'maintenance_periods':[],'zone_ids':[],'service_closed':False,'service_slots':[{'code':'morning','start':'09:00','end':'12:00','state':'open'},{'code':'afternoon','start':'13:00','end':'17:00','state':'open'}]})
view=DraftSnapshotView(store);reader=CommonAnswerer(view);clock='2026-10-26T12:00:00+07:00'
def run(threshold,mode='integration',dependent='booking'):
 first='What is the price of Amber service for Amber visitors?'
 action='how do I book Amber service?' if dependent=='booking' else 'what are Monday opening hours?'
 second='If it is below '+str(threshold)+' THB, '+action;third='What genre is Sapphire game?';fourth='What are Monday opening hours?'
 texts=[first,second,third]+([fourth] if dependent=='booking' else []);q='; '.join(texts)
 tasks=[MeaningTask(first,'service_fee','C06','detail','amount','Amber service'),MeaningTask(second,'reservation' if dependent=='booking' else 'schedule','C08' if dependent=='booking' else 'C11','detail','owner_policy' if dependent=='booking' else 'open_periods','Amber service' if dependent=='booking' else '',canonical_operation='policy.booking_steps' if dependent=='booking' else ''),MeaningTask(third,'games','C04','detail','genre','Sapphire game')]
 if dependent=='booking':tasks.append(MeaningTask(fourth,'schedule','C11','detail','open_periods'))
 proposal=Understanding(tasks,True,'controlled_native_dependency_proposal',{'model_called':False});reads=[];old_plan=Engine.plan
 def tracked(engine,category,question,*args,**kwargs):reads.append({'category':category,'question':question});return old_plan(engine,category,question,*args,**kwargs)
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')),patch.object(Engine,'plan',tracked):
  if mode=='common':
   with patch('app.knowledge.common.domain_flow.native_intents.propose',return_value=None),patch('app.knowledge.common.domain_flow.meaning_review.review',side_effect=lambda q,i,r:r),patch('app.knowledge.common.domain_flow.understanding.interpret',return_value=proposal):result=reader.answer(q,locale='en',at=clock,planner=None)
  else:result=integrated_answer(reader,q,locale='en',at=clock,planner=None,_understanding=proposal)
 details.append({'mode':mode,'dependent':dependent,'threshold':threshold,'answer':result.answer,'artifact':result.decision_artifact,'reads':reads});return result,reads
for mode in ['integration','common']:
 r,reads=run(150,mode);checks[mode+'_true_booking_preserved']='Submit the native controlled Amber form.' in r.answer;checks[mode+'_true_native_calendar_preserved']='17:00' in r.answer;checks[mode+'_true_independent_game_preserved']='Native controlled Sapphire genre' in r.answer
 checks[mode+'_true_parent_dependency_receipt']=any(d.get('verified') and d.get('outcome')=='true' for e in r.decision_artifact['execution_contract']['executor_results'] for d in e.get('dependency_receipts',[]))
 r,reads=run(50,mode);checks[mode+'_false_booking_withheld']='Submit the native controlled Amber form.' not in r.answer and 'condition is not met' in r.answer;checks[mode+'_false_calendar_and_game_preserved']='17:00' in r.answer and 'Native controlled Sapphire genre' in r.answer
 checks[mode+'_false_does_not_read_booking']=not any(x['category']=='C08' for x in reads)
r,reads=run(50,dependent='calendar');checks['conditional_calendar_false_never_reads_calendar']=not any(x['category']=='C11' for x in reads) and '17:00' not in r.answer and 'Native controlled Sapphire genre' in r.answer
r,reads=run(150,dependent='calendar');checks['conditional_calendar_true_uses_native_source']='17:00' in r.answer and any(x['category']=='C11' for x in reads)
edit=copy.deepcopy(rate);edit['fields']['amount_minor']={'status':'unknown','value':None,'evidence_refs':[],'note':'Controlled missing price'};save_owner_record(store,edit,edit['revision'],'controlled-test')
r,reads=run(150);checks['unknown_price_withholds_booking_before_reader']=not any(x['category']=='C08' for x in reads) and 'Submit the native controlled Amber form.' not in r.answer;checks['unknown_price_keeps_native_calendar_and_game']='17:00' in r.answer and 'Native controlled Sapphire genre' in r.answer
checks['parent_dependency_scope_does_not_leak_after_request']=CURRENT.get() is None
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_proposals_not_empirical_model_accuracy':True}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
