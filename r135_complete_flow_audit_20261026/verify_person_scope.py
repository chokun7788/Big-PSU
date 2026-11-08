"""C02 public/date scope and both directions, using isolated owner records."""
import copy,json,time
from datetime import datetime
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
out=R/('person_scope_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'controlled_people.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);clock=datetime.fromisoformat('2026-10-26T12:00:00+07:00');checks={};rows=[]
def known(v):return {'status':'known','value':v,'evidence_refs':[],'note':''}
def person(name,role,public,start=None,end=None):
 r=template('person');r['record_id']='controlled_'+name.lower().replace(' ','_');r['aliases']['en']=[name];r['localization']['en_status']='agent_translated'
 r['validity']={'state':'known' if start else 'unknown','effective_from':start,'effective_until':end}
 for k,v in {'display_name':{'th':name,'en':name},'role':{'th':role,'en':role},'public_scope':{'th':public,'en':public},'period':{'th':(str(start)+' to '+str(end)) if start else 'ช่วงเวลายังไม่ยืนยัน','en':(str(start)+' to '+str(end)) if start else 'Unconfirmed profile period'}}.items():r['fields'][k]=known(v)
 return save_owner_record(store,r,0,'controlled-test')['record']
alice=person('Alice','Developer','Public profile','2025-01-01T00:00:00+07:00','2027-01-01T00:00:00+07:00')
bob=person('Bob','Developer','Public profile','2024-01-01T00:00:00+07:00','2025-01-01T00:00:00+07:00')
cara=person('Cara','Developer','Private internal profile','2025-01-01T00:00:00+07:00','2027-01-01T00:00:00+07:00')
dina=person('Dina','Designer','Public profile','2025-01-01T00:00:00+07:00','2027-01-01T00:00:00+07:00')
eve=person('Eve','Developer','Public profile');e=Engine.from_snapshot(view.snapshot(),cache_key=view.path)
def run(q,op='detail',facet='role',target=''):
 u=Understanding([MeaningTask(q,'members','C02',op,facet,target)],True,'controlled_person_source',{'model_called':False});r=e.answer(q,'en',at=clock,allow_llm=False,understanding=u);rows.append({'q':q,'result':r});return r,u
r,u=run('What is the role of Alice?',target='Alice');checks['current_public_person_to_role']=bool(r['claims']) and all(c['record_id']==alice['record_id'] for c in r['claims']) and 'Developer' in r['answer'] and '2027-01-01' in r['answer']
forged=copy.deepcopy(r['needs'][0]);forged['plan']['metadata']['person_scope_proofs'][alice['record_id']]['validity']['effective_until']='2030-01-01T00:00:00+07:00';context=r['execution_contract']['request_plan']['snapshot'];task=compile_request(u.tasks[0].quote,u,e.index,context).tasks[0];ledger=assess(e.index,task,forged,context,u.tasks[0].quote);checks['displayed_person_interval_cannot_be_forged']='source_receipt_person_projection_mismatch' in ledger['fatal']
r,_=run('What was the role of Bob on 2024-06-01?',target='Bob');cs=r['execution_contract']['verifier_result']['constraint_coverage']['constraints'];checks['dated_person_scope_has_independent_source_interval_proof']=bool(r['claims']) and any(c['kind']=='date' and c['status']=='structurally_supported' for c in cs)
r,_=run('What is the role of Bob?',target='Bob');checks['expired_profile_not_presented_as_current_role']=not r['claims'] and r['status']=='not_current'
r,_=run('What was the role of Bob in 2024?',target='Bob');checks['historical_role_keeps_effective_interval']=bool(r['claims']) and 'Developer' in r['answer'] and 'Recorded effective interval' in r['answer']
r,_=run('What is the role of Bob in 2026?',target='Bob');checks['wrong_historical_year_not_substituted']=not r['claims']
r,_=run('What is the role of Cara?',target='Cara');checks['private_profile_not_delivered']=not r['claims']
r,_=run('What is the role of Eve?',target='Eve');checks['unknown_period_recorded_profile_only']=bool(r['claims']) and r['status']=='partial' and 'current appointment period is unconfirmed' in r['answer']
r,_=run('What is the recorded period of Bob?',facet='period',target='Bob');checks['expired_recorded_period_can_be_read_without_current_role_claim']=bool(r['claims']) and all(c['facet']=='period' for c in r['claims'])
q='Who is a Developer?';r,u=run(q,op='role_lookup',facet='display_name');ids={c['record_id'] for c in r['claims']}
checks['inverse_role_lookup_delivers_explicit_name_claims']=ids=={alice['record_id'],eve['record_id']} and any(c['facet']=='display_name' for c in r['claims'])
checks['one_private_or_expired_person_does_not_erase_public_subset']=r['status']=='partial' and 'Alice' in r['answer'] and 'Cara' not in r['answer'] and 'Bob' not in r['answer']
child=copy.deepcopy(r['needs'][0]);fact=next(f for f in e.index.byrecord[dina['record_id']] if f['facet']=='display_name');child['claims']=[{'fact_id':fact['id'],'record_id':fact['record_id'],'facet':fact['facet'],'value':fact['value']['en'],'numeric':None,'evidence_refs':fact['evidence_refs']}]
from app.knowledge.common.domain_flow.person_scope import check as person_scope
child['plan']['metadata']['person_scope_proofs']={dina['record_id']:person_scope(e.index.records[dina['record_id']],q,clock)}
context=r['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,context).tasks[0];ledger=assess(e.index,task,child,context,q);checks['valid_public_other_role_receipt_not_accepted']='source_receipt_requested_role_mismatch' in ledger['fatal']
other=person('Alice Remote','Designer','Public profile','2025-01-01T00:00:00+07:00','2027-01-01T00:00:00+07:00');other['aliases']['en'].append('Alice');save_owner_record(store,other,1,'controlled-test');e=Engine.from_snapshot(view.snapshot(),cache_key=view.path)
r,_=run('What is the role of Alice?',target='Alice');checks['shared_alias_not_silently_multiple_roles_or_nearest_person']=not r['claims'] and r['status']=='missing_input' and 'multiple personnel identities' in r['answer']
r,_=run('What is the role of Alice Remote?',target='Alice Remote');checks['explicit_longer_full_name_resolves_shared_short_alias']=bool(r['claims']) and all(c['record_id']==other['record_id'] for c in r['claims']) and 'Designer' in r['answer']
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'user_data_modified':False};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
