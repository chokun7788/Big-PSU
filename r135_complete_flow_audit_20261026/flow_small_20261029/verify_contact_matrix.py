"""C01 actual field values, institution/channel scope and independent receipts."""
import copy,json,time,os
from datetime import datetime
from unittest.mock import patch
from verification_support import R,snapshot
out=R/('contact_matrix_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'dialogue.sqlite')
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.answer import CommonAnswerer
store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);clock=datetime.fromisoformat('2026-10-26T12:00:00+07:00');checks={};details=[]
bi=lambda s:{'th':s,'en':s}
def create(kind,rid,name,fields,aliases=()):
 r=template(kind);r['record_id']=rid;r['aliases']['en']=list(aliases);r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2027-01-01T00:00:00+07:00'}
 for k,v in {'name':bi(name),**fields}.items():
  if k in {'building','floor'}:v=v['en']
  r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
amber=create('center','center_amber','Amber Studio',{'operator':bi('Amber Institute'),'description':bi('Amber controlled studio identity'),'address':bi('11 Amber Road'),'building':bi('Amber Hall'),'floor':bi('3'),'map_url':'https://example.org/amber-map','timezone':'Asia/Bangkok'})
other=create('center','center_cobalt','Cobalt Studio',{'operator':bi('Cobalt Institute'),'description':bi('Cobalt controlled identity'),'address':bi('22 Cobalt Road'),'building':bi('Cobalt Hall'),'floor':bi('5'),'map_url':'https://example.org/cobalt-map','timezone':'Asia/Bangkok'})
phone=create('contact','amber_phone','Amber Phone Desk',{'channel':'phone','value':'+66 000 000 111','purpose':bi('Amber controlled telephone contact'),'office_hours':bi('09:00-12:00')},['Amber Desk'])
email=create('contact','amber_email','Amber Email Desk',{'channel':'email','value':'amber@example.org','purpose':bi('Amber controlled email contact'),'office_hours':bi('13:00-16:00')},['Amber Desk'])
facility=create('facility','amber_locker','Amber Locker',{'location':bi('Amber Hall floor 3'),'usage_conditions':bi('Bring your own lock')})
def run(q,facet,mode='engine',data=None):
 e=Engine.from_snapshot(data or view.snapshot());u=Understanding([MeaningTask(q,'contact','C01','detail',facet)],True,'controlled_contact_matrix',{'model_called':False})
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):
  if mode=='common':
   a=CommonAnswerer(view).answer(q,locale='en',at=clock,planner=None);r={'answer':a.answer,'claims':[c for child in a.decision_artifact['execution_contract']['executor_results'] for c in child['claims']],'artifact':a.decision_artifact}
  else:r=e.answer(q,'en',at=clock,allow_llm=False,understanding=u)
 details.append({'question':q,'facet':facet,'mode':mode,'result':r});(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');return r,e,u
cases=[('operator','Who operates Amber Studio?','Amber Institute','center_amber'),('description','What is Amber Studio?','Amber controlled studio identity','center_amber'),('address','What is the address of Amber Studio?','11 Amber Road','center_amber'),('building','Which building is Amber Studio in?','Amber Hall','center_amber'),('floor','Which floor is Amber Studio on?','3','center_amber'),('map_url','What is the map link for Amber Studio?','https://example.org/amber-map','center_amber'),('value','What is the contact for Amber Phone Desk?','+66 000 000 111','amber_phone'),('office_hours','What are the office hours of Amber Email Desk?','13:00-16:00','amber_email'),('location','What is the location of Amber Locker?','Amber Hall floor 3','amber_locker'),('usage_conditions','How do I use Amber Locker?','Bring your own lock','amber_locker')]
for facet,q,expected,rid in cases:
 r,_,_=run(q,facet);checks['source_field_'+facet]=any(c['record_id']==rid and c['facet']==facet and expected==c['value'] for c in r['claims']) and all(c['record_id']==rid for c in r['claims'])
for facet in ['value','office_hours']:
 r,_,_=run('What is the email '+('contact' if facet=='value' else 'office hours')+' for Amber Desk?',facet);checks['requested_email_channel_'+facet]=bool(r['claims']) and all(c['record_id']=='amber_email' for c in r['claims'])
r,e,u=run('What is the map link for Amber Studio?','map_url');snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0]);f=next(f for f in e.index.byrecord[other['record_id']] if f['facet']=='map_url');child['claims']=[{'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'value':f['value']['en'],'numeric':None,'evidence_refs':f['evidence_refs']}];ledger=assess(e.index,task,child,snap,details[-1]['question']);checks['other_institution_valid_map_receipt_rejected_without_planner_target']=bool(ledger['fatal']);details.append({'challenge':'other_institution_map','claims':child['claims'],'ledger':ledger})
r,_,_=run('What is the map link for Unknown Studio?','map_url');checks['unknown_institution_not_replaced_by_neighbor']=not r['claims']
r,_,_=run('What is the email contact for Amber Desk?','value',mode='common');checks['natural_common_email_channel_not_phone']=any(c['record_id']=='amber_email' for c in r['claims']) and all(c['record_id']=='amber_email' for c in r['claims'])
data=copy.deepcopy(view.snapshot());data['release']['records']['amber_email']['fields']['value']={'status':'unknown','value':None,'evidence_refs':[],'note':'controlled missing email value'}
r,_,_=run('What is the email contact for Amber Desk?','value',data=data);checks['missing_email_not_replaced_by_recorded_phone']=not r['claims']
for channel,val in [('facebook','https://example.org/amber-facebook'),('website','https://example.org/amber-website'),('onsite','Amber Reception Desk')]:
 create('contact','amber_'+channel,'Amber '+channel+' Desk',{'channel':channel,'value':val,'purpose':bi('Controlled '+channel+' contact'),'office_hours':bi('10:00-14:00')},['Amber Desk'])
for channel in ['email','phone','facebook','website','onsite']:
 r,_,_=run('What is the '+channel+' contact for Amber Desk?','value');checks['exact_source_channel_'+channel]=bool(r['claims']) and all(c['record_id']=='amber_'+channel for c in r['claims'])
r,e,u=run('What is the email contact for Amber Desk?','value');snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(details[-1]['question'],u,e.index,snap).tasks[0];child=copy.deepcopy(r['needs'][0]);channel_refs=email['fields']['channel']['evidence_refs'];child['claims'][0]['evidence_refs']=[ref for ref in child['claims'][0]['evidence_refs'] if ref not in channel_refs];ledger=assess(e.index,task,child,snap,details[-1]['question']);checks['omitted_actual_channel_locator_rejected']=bool(ledger['fatal']);details.append({'challenge':'missing_actual_channel_locator','claims':child['claims'],'ledger':ledger})
f=next(f for f in e.index.byrecord['amber_phone'] if f['facet']=='value');child=copy.deepcopy(r['needs'][0]);child['claims']=[{'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'value':f['value']['en'],'numeric':None,'evidence_refs':f['evidence_refs']}];ledger=assess(e.index,task,child,snap,'What is the email contact for Amber Desk?');checks['valid_phone_receipt_cannot_satisfy_email_request']=bool(ledger['fatal']);details.append({'challenge':'valid_wrong_channel','claims':child['claims'],'ledger':ledger})
r,_,_=run('ขออีเมลติดต่อ Amber Desk','value',mode='common');checks['natural_Thai_email_channel_not_phone']=bool(r['claims']) and all(c['record_id']=='amber_email' for c in r['claims'])
r,_,_=run('What is the map link for the studio?','map_url');checks['generic_multiple_centers_require_identity']=not r['claims'] and r['status']=='missing_input'
data=copy.deepcopy(view.snapshot());data['withdrawn']=['center_amber'];r,_,_=run('What is the map link for Amber Studio?','map_url',data=data);checks['withdrawn_institution_not_replaced_by_remaining_neighbor']=not r['claims']
actual=snapshot();actual_records=[r for r in actual['release']['records'].values() if r['kind']=='contact']
for record in actual_records:
 if record['fields'].get('value',{}).get('status')!='known':continue
 r,_,_=run('What is the contact for '+record['record_id']+'?','value',data=actual);checks['retained_contact_'+record['record_id']]=any(c['record_id']==record['record_id'] and c['value']==record['fields']['value']['value'] for c in r['claims']) and all(c['record_id']==record['record_id'] for c in r['claims'])
(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');report={'all_passed':all(checks.values()),'checks':checks,'actual_contact_records_readonly':len(actual_records),'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_empirical_accuracy':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
