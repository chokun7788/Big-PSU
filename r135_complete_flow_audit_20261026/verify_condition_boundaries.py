"""Source-positive/negative conditional dispatch controls beyond an 'if' prefix."""
import copy,json,os,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.execution_dependencies import evaluate
O=R/('condition_boundaries_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'isolated.sqlite');store=CommonStore(O/'source.sqlite');store.initialize(allow_demo=False);checks={};details=[];bi=lambda x:{'th':x,'en':x};clock='2026-10-27T10:00:00+07:00'
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'isolated-conditional-source')['record']
create('service','amber_service',{'name':bi('Amber service'),'platform':'PC','resource_ids':[],'session_minutes':30,'capacity_min':1,'capacity_max':1});create('audience','amber_visitors',{'name':bi('Amber visitors')});rate=create('rate','amber_rate',{'service_id':'amber_service','audience_id':'amber_visitors','amount_minor':10000,'currency':'THB','unit':'per_session','duration_minutes':30,'calculation_rule':'linear'});create('faq','amber_booking',{'question':bi('How to book'),'answer':bi('Submit the Amber booking form.'),'topic':'C08','intent_key':'booking_steps'});create('game','sapphire_game',{'title':bi('Sapphire game'),'genre':bi('Controlled Sapphire genre')});view=DraftSnapshotView(store)
def run(condition,public=False,purchase=False):
 first='What is the total price of Amber service for Amber visitors 2 people and Azure visitors 3 people?' if purchase else 'What is the price of Amber service for Amber visitors?';second=condition if condition.startswith('How') else condition+', how do I book Amber service?';third='What genre is Sapphire game?';question='; '.join([first,second,third]);u=Understanding([MeaningTask(first,'service_fee','C06','price_calculate' if purchase else 'detail','amount','Amber service'),MeaningTask(second,'reservation','C08','detail','owner_policy','Amber service',canonical_operation='policy.booking_steps'),MeaningTask(third,'games','C04','detail','genre','Sapphire game')],True,'controlled_condition_boundary',{'model_called':False});calls=[];old=Engine.plan
 def traced(e,c,q,*a,**k):calls.append(c);return old(e,c,q,*a,**k)
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')),patch.object(Engine,'plan',traced):
  if public:
   out=CommonAnswerer(view).answer(question,locale='en',at=clock,planner=None);r={'answer':out.answer,'claims':out.decision_artifact.get('domain_flow',{}).get('typed_claims',[]),'execution_contract':out.decision_artifact.get('execution_contract',{}),'artifact':out.decision_artifact}
  else:r=Engine.from_snapshot(view.snapshot()).answer(question,'en',at=clock,allow_llm=False,understanding=u)
 r['reader_categories']=calls;details.append({'question':question,'condition':condition,'public':public,'result':r});(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');return r
cases=[('Unless the price is above 50 THB',False),('Unless the price is above 150 THB',True),('Unless it is below 150 THB',False),('Unless it is equal to 100 THB',False),('Unless it is equal to 150 THB',True),('Provided that the price is below 150 THB',True),('Provided that the price is below 50 THB',False),('If it is not below 150 THB',False),('If it is not below 50 THB',True),('เว้นแต่ราคามากกว่า 50 บาท',False),('เว้นแต่ราคามากกว่า 150 บาท',True),('How do I book Amber service only if the price is below 150 THB?',True),('How do I book Amber service only if the price is below 50 THB?',False),('How do I book Amber service unless the price is above 150 THB?',True),('How do I book Amber service unless the price is above 50 THB?',False)]
for condition,wanted in cases:
 r=run(condition);checks['source_condition_'+condition]=any(c['record_id']=='amber_booking' for c in r['claims']) is wanted
 checks['reader_dispatch_'+condition]=('C08' in r['reader_categories']) is wanted
 checks['independent_source_'+condition]=any(c['record_id']=='sapphire_game' for c in r['claims'])
 if wanted:checks['condition_proof_'+condition]=any(c['kind']=='condition' and c['status']=='structurally_supported' for c in r['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
for condition in ['Unless the price is affordable','Provided that it is affordable','How do I book Amber service only if the price is affordable?','How do I book Amber service unless the price is affordable?','How do I book Amber service if I pay cash, only if the price is below 150 THB?']:
 r=run(condition);checks['unresolved_condition_withheld_'+condition]='C08' not in r['reader_categories'] and not any(c['record_id']=='amber_booking' for c in r['claims']);checks['independent_after_unresolved_'+condition]=any(c['record_id']=='sapphire_game' for c in r['claims'])
for condition,wanted in [('Unless the price is above 50 THB',False),('Unless the price is above 150 THB',True)]:
 r=run(condition,True);checks['normal_Common_'+condition]=any(c['record_id']=='amber_booking' for c in r['claims']) is wanted
 if wanted:checks['normal_Common_condition_independently_supported']=any(c['kind']=='condition' and c['status']=='structurally_supported' for c in r['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
r=run('Unless the price is above 150 THB');contract=r['execution_contract'];tasks=copy.deepcopy(contract['request_plan']['tasks']);snapshot=contract['request_plan']['snapshot'];e=Engine.from_snapshot(view.snapshot());checks['unless_has_dependency']=bool(tasks[1]['execution_dependencies'])
if tasks[1]['execution_dependencies']:
 tasks[1]['execution_dependencies'][0]['operator']='gt';checks['forged_unless_polarity_rejected']=evaluate(e.index,contract['request_plan']['question'],tasks,'t2',contract['executor_results'],snapshot)['outcome']=='unknown'
else:checks['forged_unless_polarity_rejected']=False
rate=copy.deepcopy(rate);rate['fields']['unit']={'status':'known','value':'per_person','evidence_refs':[],'note':''};rate=save_owner_record(store,rate,rate['revision'],'isolated-conditional-source')['record'];create('audience','azure_visitors',{'name':bi('Azure visitors')});create('rate','azure_rate',{'service_id':'amber_service','audience_id':'azure_visitors','amount_minor':5000,'currency':'THB','unit':'per_person','duration_minutes':30,'calculation_rule':'linear'})
for condition,wanted in [('Unless the total price is equal to 350 THB',False),('Unless the total price is equal to 400 THB',True)]:
 r=run(condition,purchase=True);checks['mixed_total_'+condition]=any(c['record_id']=='amber_booking' for c in r['claims']) is wanted and ('C08' in r['reader_categories']) is wanted
 if wanted:checks['mixed_total_negative_equality_source_proof']=any(c['kind']=='condition' and c['status']=='structurally_supported' for c in r['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
unknown=copy.deepcopy(rate);unknown['fields']['amount_minor']={'status':'unknown','value':None,'evidence_refs':[],'note':'Controlled unavailable source amount'};save_owner_record(store,unknown,unknown['revision'],'isolated-conditional-source');r=run('Unless the price is above 150 THB');checks['unknown_price_not_negated_into_true']='C08' not in r['reader_categories'] and not any(c['record_id']=='amber_booking' for c in r['claims'])
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_HTTP':0,'owner_data_modified':False,'semantic_accuracy_benchmark':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(O),**report}));assert report['all_passed']
