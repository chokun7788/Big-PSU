"""Mixed-audience source arithmetic and actual dependent dispatch, no inference."""
import copy,json,time,os
from unittest.mock import patch
from verification_support import R
out=R/('mixed_billing_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'dialogue.sqlite')
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.integration import answer as integrated
from app.knowledge.common.domain_flow.execution_dependencies import evaluate
store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False);checks={};details=[]
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
s=create('service','mixed_service',{'name':{'th':'บริการอำพัน','en':'Amber service'},'platform':'PC','resource_ids':[],'session_minutes':30})
a=create('audience','mixed_amber',{'name':{'th':'กลุ่มอำพัน','en':'Amber visitors'}});b=create('audience','mixed_azure',{'name':{'th':'กลุ่มไพลิน','en':'Azure visitors'}})
rates=[]
for group,amount in [(a,10000),(b,20000)]:rates.append(create('rate','mixed_rate_'+group['record_id'],{'service_id':s['record_id'],'audience_id':group['record_id'],'amount_minor':amount,'currency':'THB','unit':'per_person','duration_minutes':30,'calculation_rule':'linear'}))
create('faq','mixed_booking',{'question':{'th':'วิธีจอง','en':'How to book'},'answer':{'th':'ส่งแบบฟอร์มสองกลุ่ม','en':'Submit the mixed audience booking form.'},'topic':'C08','intent_key':'booking_steps'})
create('game','mixed_game',{'title':{'th':'เกมบุษราคัม','en':'Topaz game'},'genre':{'th':'แนวทดสอบสองกลุ่ม','en':'Mixed audience game genre'}})
create('schedule','mixed_calendar',{'weekday':0,'open_periods':[{'start':'09:00','end':'17:00'}],'bookable_periods':[{'start':'09:00','end':'16:00'}],'maintenance_periods':[],'zone_ids':[],'service_closed':False,'service_slots':[{'code':'morning','start':'09:00','end':'12:00','state':'open'},{'code':'afternoon','start':'13:00','end':'17:00','state':'open'}]})
view=DraftSnapshotView(store);reader=CommonAnswerer(view);clock='2026-10-26T12:00:00+07:00'
def run(threshold=1700,mode='engine',audiences='Amber visitors 2 people and Azure visitors 3 people',op='price_calculate',prefix='What is the total price',condition=None):
 first=prefix+' of Amber service for '+audiences+' for 2 sessions?';second=(condition or f'If the total price is below {threshold} THB')+', how do I book?';third='What genre is Topaz game?';texts=[first,second,third];tasks=[MeaningTask(first,'service_fee','C06',op,'amount','Amber service'),MeaningTask(second,'reservation','C08','detail','owner_policy',canonical_operation='policy.booking_steps'),MeaningTask(third,'games','C04','detail','genre','Topaz game')]
 if mode!='engine':texts.append('What are Monday opening hours?');tasks.append(MeaningTask(texts[-1],'schedule','C11','detail','open_periods'))
 question='; '.join(texts);proposal=Understanding(tasks,True,'controlled_mixed_billing',{'model_called':False});engine=Engine.from_snapshot(view.snapshot(),cache_key=view.path);reads=[];old=Engine.plan
 def tracked(e,cat,q,*args,**kwargs):reads.append(cat);return old(e,cat,q,*args,**kwargs)
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')),patch.object(Engine,'plan',tracked):
  if mode=='engine':r=engine.answer(question,'en',at=clock,allow_llm=False,understanding=proposal);text=r['answer'];contract=r['execution_contract']
  elif mode=='common':
   with patch('app.knowledge.common.domain_flow.native_intents.propose',return_value=None),patch('app.knowledge.common.domain_flow.meaning_review.review',side_effect=lambda q,i,r:r),patch('app.knowledge.common.domain_flow.understanding.interpret',return_value=proposal):r=reader.answer(question,locale='en',at=clock,planner=None)
   text=r.answer;contract=r.decision_artifact['execution_contract']
  else:r=integrated(reader,question,locale='en',at=clock,planner=None,_understanding=proposal);text=r.answer;contract=r.decision_artifact['execution_contract']
 details.append({'question':question,'mode':mode,'answer':text,'contract':contract,'reads':reads});(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');return text,contract,engine,reads
def gate(c):return next(iter(c['executor_results'][1].get('dependency_receipts',[])),{})
for mode in ['engine','integration','common']:
 text,c,e,reads=run(mode=mode);checks[mode+'_two_source_lines_total_1600']=sorted(x['total_thb'] for x in c['executor_results'][0]['calculation_receipts'])==[400,1200]
 checks[mode+'_total_1600_true_dispatch']='Submit the mixed audience booking form.' in text and 'C08' in reads and gate(c).get('verified') and gate(c).get('outcome')=='true'
 checks[mode+'_independent_game_preserved']='Mixed audience game genre' in text
 checks[mode+'_source_audience_claims_complete']=len(c['executor_results'][0]['claims'])==2
 if mode=='common':checks['common_people_session_and_condition_receipts_verified']=c['verifier_result']['constraint_coverage']['status']=='observed_constraints_verified'
 text,c,e,reads=run(1500,mode);checks[mode+'_total_1600_false_withholds_before_reader']='Submit the mixed audience booking form.' not in text and 'C08' not in reads and gate(c).get('verified') and gate(c).get('outcome')=='false'
 if mode!='engine':checks[mode+'_independent_calendar_survives']='17:00' in text
for label,scope in [('missing_count','Amber visitors 2 people and Azure visitors'),('negative_count','Amber visitors -2 people and Azure visitors 3 people'),('fractional_count','Amber visitors 2.5 people and Azure visitors 3 people'),('repeated_count','Amber visitors 2 people and Amber visitors 4 people and Azure visitors 3 people')]:
 text,c,e,reads=run(audiences=scope);checks[label+'_not_a_complete_total']='C08' not in reads and not gate(c).get('verified') and c['executor_results'][0]['status']!='supported'
text,c,e,reads=run(audiences='2 people Amber visitors and 3 people Azure visitors');checks['prefix_counts_bind_actual_audience_roles']='Submit the mixed audience booking form.' in text and gate(c).get('observed_amount_thb')=='1600.0'
text,c,e,reads=run(audiences='กลุ่มอำพัน 2 คน และ กลุ่มไพลิน 3 คน');checks['thai_source_labels_bind_each_count']='Submit the mixed audience booking form.' in text and gate(c).get('observed_amount_thb')=='1600.0'
text,c,e,reads=run(condition='If it is below 1700 THB');checks['implicit_total_uses_all_purchase_lines']='Submit the mixed audience booking form.' in text and len(gate(c).get('lines',[]))==2
text,c,e,reads=run();plan=c['request_plan'];original=c['executor_results']
for label,change in [('swapped_audience_counts',lambda rows:(rows[0].update(billing_quantity=3,total_thb=600),rows[1].update(billing_quantity=2,total_thb=800))),('missing_line',lambda rows:rows.pop()),('duplicate_line',lambda rows:rows.append(copy.deepcopy(rows[0]))),('wrong_source_ref',lambda rows:rows[0].update(evidence_refs=[])),('wrong_session_count',lambda rows:rows[0].update(sessions=1)),('fake_aggregate',lambda rows:rows[0].update(total_thb=1))]:
 edited=copy.deepcopy(original);change(edited[0]['calculation_receipts']);p=evaluate(e.index,plan['question'],plan['tasks'],'t2',edited,plan['snapshot']);checks[label+'_not_total_authority']=not p['verified']
edited=copy.deepcopy(original);edited[0]['claims'].pop();checks['missing_actual_audience_claim_not_total_authority']=not evaluate(e.index,plan['question'],plan['tasks'],'t2',edited,plan['snapshot'])['verified']
edited=copy.deepcopy(original);edited[0]['receipts'][0]['record_revision']+=1;checks['changed_source_revision_not_total_authority']=not evaluate(e.index,plan['question'],plan['tasks'],'t2',edited,plan['snapshot'])['verified']
from app.knowledge.common.domain_flow.request_verifier import verify
edited=copy.deepcopy(c);edited['executor_results'][0]['calculation_receipts'][0]['billing_quantity']=3;v=verify(e.index,plan['question'],edited,text);checks['independent_verifier_rejects_wrong_audience_quantity_even_when_number_occurs_elsewhere']=any(x['kind']=='persons' and x['status']=='review_required' for x in v['constraint_coverage']['constraints'])
text,c,e,reads=run(audiences='Amber visitors 2 people or Azure visitors 3 people');checks['alternative_audiences_not_summed_into_purchase']='C08' not in reads and not gate(c).get('verified')
text,c,e,reads=run(op='compare',prefix='Compare the prices');checks['comparison_operation_not_summed_into_purchase']='C08' not in reads and not gate(c).get('verified')
third=create('audience','mixed_topaz',{'name':{'th':'กลุ่มบุษราคัม','en':'Topaz visitors'}});create('rate','mixed_rate_topaz',{'service_id':s['record_id'],'audience_id':third['record_id'],'amount_minor':5000,'currency':'THB','unit':'per_person','duration_minutes':30,'calculation_rule':'linear'})
text,c,e,reads=run(1701,audiences='Amber visitors 2 people and Azure visitors 3 people and Topaz visitors 1 person');checks['new_source_audience_and_rate_need_no_router_edit']='Submit the mixed audience booking form.' in text and gate(c).get('observed_amount_thb')=='1700.0' and len(gate(c).get('lines',[]))==3
group_rate=copy.deepcopy(rates[1]);group_rate['fields']['unit']['value']='per_group'
for k,v in [('persons_min',1),('persons_max',4)]:group_rate['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
saved=save_owner_record(store,group_rate,group_rate['revision'],'controlled-test')['record'];text,c,e,reads=run(801);checks['mixed_group_rate_uses_one_group_not_member_count']='Submit the mixed audience booking form.' in text and gate(c).get('observed_amount_thb')=='800.0'
saved['fields']['persons_max']['value']=2;save_owner_record(store,saved,saved['revision'],'controlled-test');text,c,e,reads=run(1700);checks['each_audience_group_capacity_checked_before_price_claim']=c['executor_results'][0]['status']=='missing_input' and not c['executor_results'][0]['claims'] and 'C08' not in reads
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_empirical_model_accuracy':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
