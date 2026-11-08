"""Source-controlled billing quantities, distinct from resource inventory counts."""
import json,time,os
from unittest.mock import patch
from verification_support import R
out=R/('quantity_roles_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'conversation.sqlite')
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False);checks={};details=[]
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated'
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
create('audience','controlled_quantity_audience',{'name':{'th':'กลุ่มทดสอบจำนวน','en':'Controlled visitors'}})
for rid,name,unit in [('session','Amber station','per_session'),('person','Sapphire station','per_person'),('group','Opal station','per_group'),('named_unit','One Hour','per_session')]:
 create('service','controlled_quantity_service_'+rid,{'name':{'th':'บริการทดสอบ '+name,'en':name},'platform':'PC','resource_ids':[],'session_minutes':30,'capacity_min':1,'capacity_max':4})
 fields={'service_id':'controlled_quantity_service_'+rid,'audience_id':'controlled_quantity_audience','amount_minor':10000,'currency':'THB','unit':unit,'duration_minutes':30,'calculation_rule':'linear'}
 if rid=='group':fields.update(persons_min=2,persons_max=4)
 create('rate','controlled_quantity_rate_'+rid,fields)
view=DraftSnapshotView(store);engine=Engine.from_snapshot(view.snapshot(),cache_key=view.path);clock='2026-10-26T12:00:00+07:00'
def run(name,tail):
 q='What is the total price of '+name+' for Controlled visitors '+tail+'?';u=Understanding([MeaningTask(q,'service_fee','C06','price_calculate','amount',name)],True,'controlled_quantities',{'model_called':False})
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):result=engine.answer(q,'en',at=clock,allow_llm=False,understanding=u)
 details.append({'question':q,'result':result});return result
def totals(r):return [c['total_thb'] for n in r['needs'] for c in n.get('computations',[])]
for name,tail,total,key in [('Amber station','2 sessions',200,'sessions_not_persons'),('Sapphire station','3 people',300,'persons_not_sessions'),('Sapphire station','3 people for 2 sessions',600,'persons_and_sessions_have_distinct_factors'),('Opal station','3 people',100,'group_rate_not_multiplied_by_members'),('Amber station','2 sessions totalling 60 minutes',200,'total_duration_agrees_with_sessions'),('Amber station','2 sessions of 30 minutes per session',200,'session_duration_not_total_duration')]:
 r=run(name,tail);checks[key]=totals(r)==[total]
r=run('Opal station','5 people');checks['group_capacity_bound_not_ignored']=not r['claims']
r=run('One Hour','for One Hour');checks['numeric_service_title_does_not_erase_identical_actual_duration']=totals(r)==[200]
for tail in ['-2 sessions','2.5 sessions','0 sessions','2 sessions and 3 sessions','-3 people','2.5 people']:
 r=run('Sapphire station',tail);checks['invalid_or_conflicting_quantity_not_first_integer_'+tail]=not r['claims'] and not totals(r)
for tail in ['2 machines','2 machines for 3 sessions']:
 r=run('Amber station',tail);checks['resource_count_not_silently_a_completed_price_'+tail]=r['terminal_state'] not in {'supported'} and any(c['kind']=='resource_quantity' and c['status']=='review_required' for c in r['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
 checks['resource_count_not_relabelled_as_sessions_'+tail]=not any(s['kind']=='sessions' and s['source_span']['text']=='2 machines' for t in r['execution_contract']['request_plan']['tasks'] for s in t['slots'])
 checks['resource_count_has_distinct_compiled_owner_slot_'+tail]=any(s['kind']=='resource_quantity' and s['normalized_value']==2 and s['owner_task_id']==t['id'] for t in r['execution_contract']['request_plan']['tasks'] for s in t['slots'])
 checks['resource_billing_limitation_is_visible_'+tail]='requested number of machines is not confirmed' in r['answer']
 checks['controlled_audience_name_not_a_controls_need_'+tail]=all(t['category']!='C05' for t in r['execution_contract']['request_plan']['tasks'])
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_real_business_data':True}
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
