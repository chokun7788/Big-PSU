"""C07 registered field/operation source controls and six retained packages."""
import copy,json,time,os
from unittest.mock import patch
from verification_support import R,snapshot
out=R/('rental_matrix_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'dialogue.sqlite')
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.answer import CommonAnswerer
store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False);checks={};details=[];clock='2026-10-26T12:00:00+07:00'
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2027-01-01T00:00:00+07:00'}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
for rid,en,th in [('rental_amber_zone','Amber hall','ห้องอำพัน'),('rental_azure_zone','Azure hall','ห้องไพลิน')]:create('zone',rid,{'name':{'th':th,'en':en}})
for rid,en,th in [('rental_internal','Internal test organization','หน่วยงานภายในทดสอบ'),('rental_external','External test organization','หน่วยงานภายนอกทดสอบ')]:create('audience',rid,{'name':{'th':th,'en':en}})
packages=[]
for rid,name,zone,group,amount,duration,equipment,seats,terms in [('rental_amber_package','Amber package','rental_amber_zone','rental_internal',90000,120,'Two controlled controllers',7,'Internal approval is required'),('rental_azure_package','Azure package','rental_azure_zone','rental_external',170000,240,'Four controlled controllers',13,'External approval is required')]:
 packages.append(create('rental_package',rid,{'name':{'th':name,'en':name},'zone_ids':[zone],'audience_id':group,'period_label':'custom','duration_minutes':duration,'amount_minor':amount,'currency':'THB','equipment_included':{'th':equipment,'en':equipment},'room_seats':seats,'terms':{'th':terms,'en':terms}}))
view=DraftSnapshotView(store)
questions={'amount_thb':('price',['900','1700']),'duration_minutes':('duration',['120','240']),'equipment_included':('included equipment',['Two controlled controllers','Four controlled controllers']),'room_seats':('room seats',['7','13']),'terms':('terms',['Internal approval is required','External approval is required']),'zone':('included zones',['Amber hall','Azure hall']),'audience':('organization scope',['Internal test organization','External test organization'])}
def run(question,facet,op='detail',mode='engine',data=None):
 engine=Engine.from_snapshot(data or view.snapshot());u=Understanding([MeaningTask(question,'rental','C07',op,facet)],True,'controlled_rental_matrix',{'model_called':False})
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
  if mode=='common':
   with patch('app.knowledge.common.domain_flow.native_intents.propose',return_value=None),patch('app.knowledge.common.domain_flow.meaning_review.review',side_effect=lambda q,i,r:r),patch('app.knowledge.common.domain_flow.understanding.interpret',return_value=u):r=CommonAnswerer(view).answer(question,locale='en',at=clock,planner=None)
   result={'answer':r.answer,'claims':r.decision_artifact['execution_contract']['executor_results'][0]['claims'],'execution_contract':r.decision_artifact['execution_contract']}
  else:result=engine.answer(question,'en',at=clock,allow_llm=False,understanding=u)
 details.append({'question':question,'facet':facet,'operation':op,'mode':mode,'result':result});(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');return result,engine,u
for facet,(word,expected) in questions.items():
 for n,name in enumerate(['Amber package','Azure package']):
  r,_,_=run('What is the '+word+' of '+name+'?',facet);claims=[c for c in r['claims'] if c['facet']==facet];checks['detail_'+facet+'_'+str(n)]=len(claims)==1 and expected[n] in claims[0]['value'] and claims[0]['record_id']==packages[n]['record_id']
 r,_,_=run('Compare the '+word+' of Amber package and Azure package.',facet,'compare');checks['compare_'+facet+'_both_source_options']=all(any(c['record_id']==packages[n]['record_id'] and c['facet']==facet and expected[n] in c['value'] for c in r['claims']) for n in range(2)) and '|---' in r['answer']
 if facet=='amount_thb':
  checks['cross_condition_price_compare_shows_zone_organization_duration_and_terms']=all(x in r['answer'] for x in ['Amber hall','Azure hall','Internal test organization','External test organization','120','240','Internal approval is required','External approval is required'])
  checks['price_compare_does_not_sum_alternatives']='Total:' not in r['answer']
r,e,u=run('Compare the price of Amber package and Azure package.','amount_thb','compare');task=compile_request(details[-1]['question'],u,e.index,r['execution_contract']['request_plan']['snapshot']).tasks[0];child=copy.deepcopy(r['needs'][0]);child['claims']=[c for c in child['claims'] if c['record_id']==packages[0]['record_id']];ledger=assess(e.index,task,child,r['execution_contract']['request_plan']['snapshot'],details[-1]['question']);checks['dropping_one_package_cannot_keep_complete_comparison']=ledger['terminal_state']!='supported' and not ledger['all_obligations_fulfilled']
details.append({'challenge':'one_package_removed','actual_claims':child['claims'],'ledger':ledger})
comparison_question=r['execution_contract']['request_plan']['question'];child=copy.deepcopy(r['needs'][0]);child['claims']=[c for c in child['claims'] if c['facet']!='audience'];ledger=assess(e.index,task,child,r['execution_contract']['request_plan']['snapshot'],comparison_question);checks['dropping_organization_context_cannot_keep_complete_comparison']=not ledger['all_obligations_fulfilled'] and any(o['kind']=='comparison_package_condition' and not o['fulfilled'] for o in ledger['obligations']);details.append({'challenge':'organization_context_removed','actual_claims':child['claims'],'ledger':ledger})
child=copy.deepcopy(r['needs'][0]);child['plan']['metadata']['package_comparison_fields']=['amount_thb'];ledger=assess(e.index,task,child,r['execution_contract']['request_plan']['snapshot'],comparison_question);checks['comparison_scope_metadata_not_verifier_authority']='source_receipt_package_comparison_projection_mismatch' in ledger['fatal'];details.append({'challenge':'comparison_scope_metadata_forged','ledger':ledger})
r,_,_=run('Compare the price of Amber package and Azure package.','amount_thb','compare',mode='common');checks['common_price_compare_keeps_source_conditions']=all(x in r['answer'] for x in ['Amber hall','Azure hall','Internal test organization','External test organization'])
for facet,word in [('amount_thb','price'),('terms','terms'),('equipment_included','included equipment')]:
 r,_,_=run('Compare the '+word+' of Amber package and Azure package for 2028.',facet,'compare');checks['expired_package_comparison_'+facet+'_not_claimed_for_future_year']=not r['claims'] and r['status']=='not_current'
r,_,_=run('What are the terms of Amber package for 2028?','terms');checks['nonprice_package_detail_checks_requested_validity']=not r['claims'] and r['status']=='not_current'
third=create('rental_package','rental_third_package',{'name':{'th':'Topaz package','en':'Topaz package'},'zone_ids':['rental_amber_zone'],'audience_id':'rental_internal','period_label':'custom','duration_minutes':60,'amount_minor':22200,'currency':'THB'})
r,e,u=run('Compare the price of Amber package and Azure package.','amount_thb','compare');snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0]);f=next(f for f in e.index.byrecord[third['record_id']] if f['facet']=='amount_thb');child['claims'].append({'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'numeric':f['numeric'],'value':f['value']['en'],'evidence_refs':f['evidence_refs']});ledger=assess(e.index,task,child,snap,details[-1]['question']);checks['valid_but_unrequested_package_cannot_enter_comparison']='source_receipt_package_comparison_scope_mismatch' in ledger['fatal'];details.append({'challenge':'unrequested_current_source_package_added','actual_claims':child['claims'],'ledger':ledger})
# Read every actual retained package, separately from the old six-case sample.
actual=snapshot();retained=Engine.from_snapshot(actual);ids=sorted(rid for rid,r in retained.index.records.items() if r['kind']=='rental_package');checks['retained_package_source_set_not_empty']=bool(ids)
for rid in ids:
 record=retained.index.records[rid];name=record['fields']['name']['value']['th'];r,_,_=run('ราคา '+name,'amount_thb','price_calculate',data=actual)
 checks['retained_source_price_'+rid]=any(c['record_id']==rid and c['facet']=='amount_thb' and c['numeric']==record['fields']['amount_minor']['value']/100 for c in r['claims'])
edit=copy.deepcopy(packages[0]);edit['fields']['terms']={'status':'unknown','value':None,'evidence_refs':[],'note':'Controlled missing terms'};edit=save_owner_record(store,edit,edit['revision'],'controlled-test')['record'];r,_,_=run('Compare the price of Amber package and Azure package.','amount_thb','compare');checks['unknown_package_conditions_visible_and_partial']=r['status']=='partial' and 'Not confirmed' in r['answer'] and any(o['kind']=='comparison_package_condition' and not o['fulfilled'] for o in r['execution_contract']['executor_results'][0]['unresolved_obligations'])
edit['fields']['currency']={'status':'unknown','value':None,'evidence_refs':[],'note':'Controlled missing currency'};save_owner_record(store,edit,edit['revision'],'controlled-test');r,_,_=run('What is the price of Amber package?','amount_thb');checks['unknown_currency_cannot_be_asserted_as_THB']=not any(c['facet']=='amount_thb' for c in r['claims']) and '900 THB' not in r['answer']
r,_,_=run('Compare the price of Amber package and Azure package.','amount_thb','compare');checks['missing_one_price_keeps_other_option_and_source_gap']=r['status']=='partial' and '1700 THB' in r['answer'] and '900 THB' not in r['answer'] and 'Not confirmed' in r['answer'] and all(name in r['answer'] for name in ['Amber package','Azure package'])
from app.knowledge.common.domain_flow.capabilities import SUPPORTED
tested={(row['operation'],row['facet']) for row in details if row.get('result')};registered={(op,facet) for op,fields in SUPPORTED['C07'].items() for facet in fields};checks['all_C07_registered_pairs_have_source_positive_cases']=registered<=tested
report={'all_passed':all(checks.values()),'checks':checks,'tested_operation_field_pairs':[{'operation':op,'field':field} for op,field in sorted(tested)],'registered_operation_field_pairs':[{'operation':op,'field':field} for op,field in sorted(registered)],'retained_package_records_checked':len(ids),'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'retained_package_inspection_not_new_sample_or_accuracy':True,'controlled_schema_operations_not_whole_flow_proof':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
