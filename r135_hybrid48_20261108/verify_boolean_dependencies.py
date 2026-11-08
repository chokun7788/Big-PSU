"""Finite source predicates; isolated owner data and controlled provider snapshots."""
import copy,json,time,os,dataclasses
from datetime import datetime,timedelta
from unittest.mock import patch
from verification_support import R,snapshot
out=R/('boolean_dependencies_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'conversation.sqlite')
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.integration import answer
from app.knowledge.common import legacy_live_on_demand as bridge
from app.booking.live_status import LiveBookingSnapshot,LiveResource,LiveSlot
from app.knowledge.common.flow_context import CURRENT,request_context
from app.knowledge.common.domain_flow.execution_dependencies import evaluate
store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False)
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
create('faq','controlled_boolean_booking',{'question':{'th':'วิธีจอง','en':'How to book'},'answer':{'th':'ส่งแบบฟอร์มเงื่อนไข','en':'Submit the controlled boolean booking form.'},'topic':'C08','intent_key':'booking_steps'})
create('game','controlled_boolean_game',{'title':{'th':'เกมอำพัน','en':'Amber game'},'genre':{'th':'แนวเงื่อนไขทดสอบ','en':'Controlled boolean game genre'}})
schedule=create('schedule','controlled_boolean_schedule',{'weekday':2,'open_periods':[{'start':'09:00','end':'17:00'}],'bookable_periods':[{'start':'09:00','end':'17:00'}],'maintenance_periods':[],'zone_ids':[],'service_closed':False,'service_slots':[{'code':'morning','start':'09:00','end':'12:00','state':'open'},{'code':'afternoon','start':'13:00','end':'17:00','state':'open'}]})
base=snapshot();base['release']['records']={k:v for k,v in base['release']['records'].items() if v['kind'] not in {'faq','game','schedule','closure'}};delta=DraftSnapshotView(store).snapshot()
for key in ['records','sources']:base['release'][key].update(delta['release'][key])
base['source_pairs'].update(delta['source_pairs']);base['epoch']+=delta['epoch']
clock=datetime.fromisoformat('2026-10-27T10:00:00+07:00');checks={};details=[]
class View:
 path=out/'controlled.sqlite'
 def snapshot(self):return base
 def still_current(self,s):return s is base
free=(LiveSlot('09:00','12:00','available',0,0,1),)
busy=(LiveSlot('09:00','12:00','busy',1,0,0),)
def fixture(day,slots,age=0):
 resources=tuple(LiveResource(key,name,1,'available',1,slots) for key,name in [('15','PC #2'),('16','PC #3')])
 return LiveBookingSnapshot(ok=True,date=day,now=clock.isoformat(),generated_at=(clock-timedelta(seconds=age)).isoformat(),source='controlled_boolean_fixture',center_open=True,center_reason='controlled',open_periods=(('09:00','17:00'),),resources=resources)
def run(kind='live',slots=free,window='10:00-11:00',mode='integration',condition='If yes',age=0,first=None):
 first=first or (f'Is PC2 available on 2026-10-28 at {window}?' if kind=='live' else f'Is the studio open for play on 2026-10-28 at {window}?')
 second=condition+', how do I book?';third='What genre is Amber game?';q='; '.join([first,second,third]);proposal=Understanding([MeaningTask(first,'live' if kind=='live' else 'schedule','C12' if kind=='live' else 'C11','availability' if kind=='live' else 'detail','live_status' if kind=='live' else 'open_periods'),MeaningTask(second,'reservation','C08','detail','owner_policy',canonical_operation='policy.booking_steps'),MeaningTask(third,'games','C04','detail','genre','Amber game')],True,'controlled_boolean_dependency',{'model_called':False});calls=[];reads=[];observations=[]
 def fetch(day):calls.append(day);p=fixture(day,slots,age);observations.append(p);return p
 old=Engine.plan
 def tracked(engine,category,question,*args,**kwargs):reads.append(category);return old(engine,category,question,*args,**kwargs)
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')),patch('app.booking.live_status.get_live_booking_status',fetch),patch.object(bridge,'freshness_now',lambda:clock),patch.object(Engine,'plan',tracked):
  reader=CommonAnswerer(View())
  if mode=='common':
   with patch('app.knowledge.common.domain_flow.native_intents.propose',return_value=None),patch('app.knowledge.common.domain_flow.meaning_review.review',side_effect=lambda q,i,r:r),patch('app.knowledge.common.domain_flow.understanding.interpret',return_value=proposal):r=reader.answer(q,locale='en',at=clock,planner=None)
  else:r=answer(reader,q,locale='en',at=clock,planner=None,_understanding=proposal)
 details.append({'kind':kind,'mode':mode,'question':q,'answer':r.answer,'artifact':r.decision_artifact,'reads':reads,'provider_reads':len(calls)})
 (out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8')
 return r,reads,observations
def proof(r):
 rows=r.decision_artifact['execution_contract']['executor_results']
 return next((p for row in rows if row['task_id']=='t2' for p in row.get('dependency_receipts',[])),{'verified':False,'outcome':'unknown','reason':'expected_dependency_receipt_missing'})
for mode in ['integration','common']:
 for kind in ['live','calendar']:
  r,reads,obs=run(kind=kind,mode=mode);checks[mode+'_'+kind+'_affirmative_true_dispatch']='Submit the controlled boolean booking form.' in r.answer and 'C08' in reads and proof(r)['verified'] and proof(r)['outcome']=='true'
  checks[mode+'_'+kind+'_independent_game_preserved']='Controlled boolean game genre' in r.answer
  if mode=='common':checks[kind+'_final_date_time_and_condition_reverified']=r.decision_artifact['execution_contract']['verifier_result']['constraint_coverage']['status']=='observed_constraints_verified' and 'constraints remains unverified' not in r.answer
  r,reads,obs=run(kind=kind,mode=mode,slots=busy,window='12:00-13:00' if kind=='calendar' else '10:00-11:00');checks[mode+'_'+kind+'_false_withholds_before_dispatch']='Submit the controlled boolean booking form.' not in r.answer and 'C08' not in reads and proof(r)['verified'] and proof(r)['outcome']=='false'
  checks[mode+'_'+kind+'_false_preserves_independent_game']='Controlled boolean game genre' in r.answer
  if kind=='live':checks[mode+'_one_provider_snapshot_for_live_condition']=len(obs)==1
r,reads,_=run(kind='calendar',condition='If no',window='12:00-13:00');checks['negative_boolean_uses_same_recomputed_window']='Submit the controlled boolean booking form.' in r.answer and proof(r)['observed_boolean'] is False
r,reads,_=run(first='PC2 วันที่ 2026-10-28 ว่าง 10:00-11:00 ไหม',condition='ถ้าใช่');checks['thai_affirmative_live_same_source_proof']='Submit the controlled boolean booking form.' in r.answer and proof(r)['verified']
for condition,kind in [('If it is available','live'),('If it is free','live'),('ถ้าว่าง','live'),('If it is open','calendar'),('ถ้าเปิดให้เล่น','calendar')]:
 r,reads,_=run(kind=kind,condition=condition);checks['explicit_state_true_'+condition]='C08' in reads and proof(r)['verified'] and proof(r)['outcome']=='true'
r,reads,_=run(slots=busy,condition='If it is not available');checks['explicit_negative_state_recomputed']='C08' in reads and proof(r)['observed_boolean'] is False
r,reads,_=run(kind='calendar',condition='If it is available');checks['play_calendar_not_resource_availability_predicate']='C08' not in reads and not proof(r)['verified']
r,reads,_=run(condition='If it is open');checks['live_availability_not_play_calendar_predicate']='C08' not in reads and not proof(r)['verified']
for label,kwargs in [('stale',{'age':99999}),('slot_gap',{'slots':(LiveSlot('09:00','10:30','available',0,0,1),)}),('historical',{'first':'Is PC2 available on 2026-10-26 at 10:00-11:00?'}),('daywide',{'first':'Is PC2 available on 2026-10-28?'}),('multi_resource',{'first':'Are PC2 and PC3 available on 2026-10-28 at 10:00-11:00?'}),('calendar_listing',{'kind':'calendar','first':'What are Wednesday opening hours?'})]:
 r,reads,_=run(**kwargs);checks[label+'_not_promoted_to_affirmative']='C08' not in reads and 'Submit the controlled boolean booking form.' not in r.answer and not proof(r)['verified']
r,reads,_=run(first='Is PC2 and PC3 available on 2026-10-28 at 10:00-11:00?');checks['singular_grammar_does_not_collapse_multiple_station_ids']='C08' not in reads and not proof(r)['verified']
checks['live_multi_station_preserves_both_actual_observations']=len(r.decision_artifact['execution_contract']['executor_results'][0]['observation_receipts'])==2 and 'PC #2' in r.answer and 'PC #3' in r.answer
r,reads,_=run(first='Is PC #02-#03 available on 2026-10-28 at 10:00-11:00?');checks['station_range_not_a_scalar_boolean']='C08' not in reads and not proof(r)['verified'] and len(r.decision_artifact['execution_contract']['executor_results'][0]['observation_receipts'])==2
r,reads,observations=run(first='Is PC #03-#02 available on 2026-10-28 at 10:00-11:00?');checks['reversed_station_range_clarified_before_provider']=not observations and r.decision_artifact['execution_contract']['executor_results'][0]['status']=='missing_input' and 'C08' not in reads
r,reads,_=run(first='Is PC2 and PC99 available on 2026-10-28 at 10:00-11:00?');checks['missing_station_not_replaced_by_known_station_free']='C08' not in reads and r.decision_artifact['execution_contract']['executor_results'][0]['status']=='missing_source' and 'PC #2 is available' not in r.answer
# Forged audit outcomes and proof material cannot replace source/request data.
r,_,observed=run();contract=r.decision_artifact['execution_contract'];plan=contract['request_plan'];engine=Engine.from_snapshot(base);executors=contract['executor_results']
with request_context() as ctx,patch.object(bridge,'freshness_now',lambda:clock):
 ctx.live[('wordpress_booking','2026-10-28')]=observed[0]
 for label,field,changed in [('decision','decision',{'verified':True,'normalized_status':'occupied'}),('payload','payload_sha256','f'*64),('window','requested_window',{'start':'11:00','end':'12:00','explicit':True}),('revision','binding_revision',999),('snapshot','source_snapshot',{'release_id':'forged','epoch':0})]:
  edited=copy.deepcopy(executors);edited[0]['observation_receipts'][0][field]=changed;p=evaluate(engine.index,plan['question'],plan['tasks'],'t2',edited,plan['snapshot']);checks['forged_'+label+'_receipt_not_boolean_authority']=not p['verified']
 p=evaluate(engine.index,plan['question'],plan['tasks'],'t2',executors,plan['snapshot']);checks['untampered_live_proof_recomputed_again']=p['verified'] and p['outcome']=='true'
 with patch.object(bridge,'freshness_now',lambda:clock+timedelta(days=1)):
  p=evaluate(engine.index,plan['question'],plan['tasks'],'t2',executors,plan['snapshot']);checks['fresh_receipt_flag_not_authority_after_expiry']=not p['verified']
 edited_index=Engine.from_snapshot(copy.deepcopy(base)).index;bid=executors[0]['observation_receipts'][0]['binding_id'];edited_index.records[bid]['fields']['freshness_max_age_seconds']['value']+=1
 p=evaluate(edited_index,plan['question'],plan['tasks'],'t2',executors,plan['snapshot']);checks['binding_value_without_matching_source_pointer_not_authority']=not p['verified']
 edited=copy.deepcopy(executors);edited[1]['dependency_receipts'][0].update(verified=False,outcome='false')
 checks['stored_outcome_flag_not_authority']=evaluate(engine.index,plan['question'],plan['tasks'],'t2',edited,plan['snapshot'])['outcome']=='true'
p=evaluate(engine.index,plan['question'],plan['tasks'],'t2',executors,plan['snapshot']);checks['saved_live_receipt_without_current_request_cache_not_reused']=not p['verified']
r,_,_=run(kind='calendar');contract=r.decision_artifact['execution_contract'];plan=contract['request_plan'];edited=copy.deepcopy(contract['executor_results']);edited[0]['claims'][0]['value']='Open all day regardless of source'
p=evaluate(engine.index,plan['question'],plan['tasks'],'t2',edited,plan['snapshot']);checks['calendar_claim_prose_cannot_change_source_predicate']=not p['verified']
original=base
closure=create('closure','controlled_boolean_closure',{'local_date':'2026-10-28','zone_ids':[],'state':'closed','reason':{'th':'ปิดทดสอบเงื่อนไข','en':'Controlled predicate closure'}});delta=DraftSnapshotView(store).snapshot();base=copy.deepcopy(original)
for key in ['records','sources']:base['release'][key].update(delta['release'][key])
base['source_pairs'].update(delta['source_pairs']);base['epoch']+=delta['epoch']
r,reads,_=run();checks['live_provider_free_with_pinned_closure_not_affirmative']='C08' not in reads and not proof(r)['verified']
r,reads,_=run(kind='calendar');checks['calendar_special_closure_recomputed_false']='C08' not in reads and proof(r)['verified'] and proof(r)['outcome']=='false'
base=original
checks['request_provider_cache_does_not_leak']=CURRENT.get() is None
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_http_calls':0,'user_data_modified':False,'controlled_source_and_proposals_not_empirical_model_accuracy':True}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
