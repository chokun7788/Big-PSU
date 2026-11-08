"""Explicit both-price output gates use two independent source prerequisites."""
import copy,json,time,os
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.execution_dependencies import evaluate
out=R/('both_price_dependencies_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);checks={};details=[];bi=lambda s:{'th':s,'en':s}
os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'dialogue.sqlite')
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
aud=create('audience','aud_amber',{'name':bi('Amber visitors')})
for name,amount in [('Amber',10000),('Cobalt',20000)]:
 create('service','service_'+name.lower(),{'name':bi(name+' service'),'platform':'PC','resource_ids':[],'session_minutes':30,'capacity_min':1,'capacity_max':1})
 create('rate','rate_'+name.lower(),{'service_id':'service_'+name.lower(),'audience_id':aud['record_id'],'amount_minor':amount,'currency':'THB','unit':'per_session','duration_minutes':30})
book=create('faq','amber_booking',{'question':bi('How to book'),'answer':bi('Submit the controlled booking form.'),'topic':'C08','intent_key':'booking_steps'})
create('game','sapphire_game',{'title':bi('Sapphire game'),'genre':bi('Controlled Sapphire genre')})
def run(condition,extra=False,mode='engine'):
 tasks=[]
 for name in ['Amber','Cobalt']:
  q='What is the unit price of '+name+' service for Amber visitors?';tasks.append(MeaningTask(q,'service_fee','C06','detail','amount',name+' service'))
 if extra:tasks.append(copy.deepcopy(tasks[0]));tasks[-1].quote='What is the unit price of Amber service for Amber visitors again?'
 q=condition+', how do I book Amber service?';tasks.append(MeaningTask(q,'reservation','C08','detail','owner_policy','Amber service',canonical_operation='policy.booking_steps'));q='What genre is Sapphire game?';tasks.append(MeaningTask(q,'games','C04','detail','genre','Sapphire game'));question='; '.join(t.quote for t in tasks);e=Engine.from_snapshot(view.snapshot());calls=[]
 from app.knowledge.common.domain_flow.capabilities import dispatch
 def tracked(engine,task,meaning,q,at):calls.append(task.category);return dispatch(engine,task,meaning,q,at)
 proposal=Understanding(tasks,True,'controlled_both_price_gate',{'model_called':False})
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')),patch('app.knowledge.common.domain_flow.capabilities.dispatch',side_effect=tracked):
  if mode=='engine':r=e.answer(question,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=proposal)
  else:
   from app.knowledge.common.answer import CommonAnswerer
   from app.knowledge.common.domain_flow.integration import answer
   reader=CommonAnswerer(view)
   if mode=='integration':a=answer(reader,question,locale='en',at='2026-10-26T12:00:00+07:00',planner=None,_understanding=proposal)
   else:
    with patch('app.knowledge.common.domain_flow.native_intents.propose',return_value=None),patch('app.knowledge.common.domain_flow.meaning_review.review',side_effect=lambda q,i,r:r),patch('app.knowledge.common.domain_flow.understanding.interpret',return_value=proposal):a=reader.answer(question,locale='en',at='2026-10-26T12:00:00+07:00',planner=None)
   contract=a.decision_artifact['execution_contract'];r={'answer':a.answer,'claims':[c for child in contract['executor_results'] for c in child['claims']],'execution_contract':contract,'artifact':a.decision_artifact}
 details.append({'condition':condition,'mode':mode,'controlled_proposal_not_model_accuracy':True,'result':r,'dispatch_calls':calls});(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');return r,e,calls
for condition,wanted,key in [('If both unit prices are below 250 THB',True,'both_true'),('If both unit prices are below 150 THB',False,'one_false'),('If both unit prices are below 50 THB',False,'both_false'),('ถ้าราคาต่อหน่วยทั้งสองไม่เกิน 250 บาท',True,'thai_both_true')]:
 r,e,calls=run(condition);checks[key+'_booking_dispatched_only_when_all_true']=('C08' in calls)==wanted;checks[key+'_independent_sources_and_game_preserved']={'rate_amber','rate_cobalt','sapphire_game'}<={c['record_id'] for c in r['claims']}
 checks[key+'_two_actual_prerequisite_edges']=len(r['execution_contract']['request_plan']['tasks'][2]['execution_dependencies'])==2
r,e,calls=run('If both unit prices are below 250 THB');checks['independent_reads_precede_both_dependent_dispatch']=calls==['C06','C06','C04','C08'];c=r['execution_contract'];tasks=c['request_plan']['tasks'];snap=c['request_plan']['snapshot'];question=c['request_plan']['question'];executors=c['executor_results'];target=tasks[2]['id']
forged=copy.deepcopy(tasks);forged[2]['execution_dependencies']=forged[2]['execution_dependencies'][:1];checks['removing_second_edge_cannot_keep_true']=evaluate(e.index,question,forged,target,executors,snap)['outcome']=='unknown'
if len(tasks[2]['execution_dependencies'])==2:
 forged=copy.deepcopy(tasks);forged[2]['execution_dependencies'][1]['threshold']='999';checks['forged_second_threshold_rejected']=evaluate(e.index,question,forged,target,executors,snap)['outcome']=='unknown'
else:checks['forged_second_threshold_rejected']=False
for condition,key in [('If both prices are affordable','unsupported_both_predicate'),('If both total prices are below 250 THB','unit_receipts_do_not_prove_both_totals')]:
 r,_,calls=run(condition);checks[key+'_withheld_before_reader']='C08' not in calls
r,_,calls=run('If both unit prices are below 250 THB',extra=True);checks['three_prior_prices_do_not_guess_which_two']='C08' not in calls
for mode in ['integration','common']:
 for threshold,wanted in [(250,True),(150,False)]:
  r,_,calls=run('If both unit prices are below '+str(threshold)+' THB',mode=mode);checks[mode+'_both_gate_'+str(threshold)]=any(c['record_id']==book['record_id'] for c in r['claims'])==wanted;checks[mode+'_both_gate_receipt_'+str(threshold)]=any(d.get('verified') and d.get('outcome')==('true' if wanted else 'false') for child in r['execution_contract']['executor_results'] for d in child.get('dependency_receipts',[]))
save_owner_record(store,{**copy.deepcopy(e.index.records['rate_cobalt']),'fields':{**copy.deepcopy(e.index.records['rate_cobalt']['fields']),'amount_minor':{'status':'unknown','value':None,'evidence_refs':[],'note':'controlled missing second rate'}}},1,'controlled-test')
r,_,calls=run('If both unit prices are below 250 THB');checks['unknown_second_source_withholds_booking_before_reader']='C08' not in calls;checks['unknown_second_source_retains_first_and_game']={'rate_amber','sapphire_game'}<={c['record_id'] for c in r['claims']}
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_empirical_accuracy':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
