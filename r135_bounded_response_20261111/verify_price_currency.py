"""Known minor amounts cannot supply an unconfirmed currency."""
import copy,json,time
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import MeaningTask,Understanding
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
out=R/('price_currency_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False);checks={};rows=[]
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
create('zone','currency_zone',{'name':{'th':'ห้องอำพัน','en':'Amber hall'}});create('service','currency_service',{'name':{'th':'บริการอำพัน','en':'Amber service'},'platform':'PC','resource_ids':[],'session_minutes':30});create('audience','currency_audience',{'name':{'th':'กลุ่มอำพัน','en':'Amber visitors'}})
rate=create('rate','currency_rate',{'service_id':'currency_service','audience_id':'currency_audience','amount_minor':12300,'currency':'THB','unit':'per_person','duration_minutes':30})
package=create('rental_package','currency_package',{'name':{'th':'แพ็กเกจอำพัน','en':'Amber package'},'zone_ids':['currency_zone'],'audience_id':'currency_audience','amount_minor':45600,'currency':'THB','period_label':'custom','duration_minutes':120})
view=DraftSnapshotView(store)
def run(cat,facet,question):
 e=Engine.from_snapshot(view.snapshot());u=Understanding([MeaningTask(question,'service_fee' if cat=='C06' else 'rental',cat,'detail',facet)],True,'controlled_currency',{'model_called':False});r=e.answer(question,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=u);rows.append({'category':cat,'question':question,'result':r});return r,e,u
for cat,record,q,facet,expected in [('C06',rate,'What is the price of Amber service for Amber visitors?','amount',123),('C07',package,'What is the price of Amber package?','amount_thb',456)]:
 r,e,u=run(cat,facet,q);claim=next(c for c in r['claims'] if c['facet']==facet);checks[cat+'_known_amount_and_currency_delivered']=claim['numeric']==expected and 'THB' in claim['value']
 refs=record['fields']['currency']['evidence_refs'];checks[cat+'_currency_has_actual_source_locator_in_claim']=bool(refs) and all(ref in claim['evidence_refs'] for ref in refs)
 task=compile_request(q,u,e.index,r['execution_contract']['request_plan']['snapshot']).tasks[0];child=copy.deepcopy(r['needs'][0]);child['claims'][0]['evidence_refs']=[ref for ref in child['claims'][0]['evidence_refs'] if ref not in refs];ledger=assess(e.index,task,child,r['execution_contract']['request_plan']['snapshot'],q);checks[cat+'_missing_currency_evidence_rejected']='source_receipt_price_currency_unconfirmed' in ledger['fatal']
 tampered=copy.deepcopy(e.index);tampered.records[record['record_id']]['fields']['currency']={'status':'unknown','value':None,'evidence_refs':[]};ledger=assess(tampered,task,r['needs'][0],r['execution_contract']['request_plan']['snapshot'],q);checks[cat+'_old_fact_not_authority_after_currency_unconfirmed']='source_receipt_price_currency_unconfirmed' in ledger['fatal']
 changed=copy.deepcopy(record);changed['fields']['currency']={'status':'unknown','value':None,'evidence_refs':[],'note':'Controlled missing currency'};save_owner_record(store,changed,changed['revision'],'controlled-test');r,e,_=run(cat,facet,q);checks[cat+'_unknown_currency_no_numeric_price_claim']=not r['claims'] and r['status']=='missing_source'
 d,_,_=run(cat,'duration_minutes','What is the duration of '+('Amber service for Amber visitors' if cat=='C06' else 'Amber package')+'?');checks[cat+'_independent_duration_not_erased_with_currency']=any(c['facet']=='duration_minutes' for c in d['claims'])
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_real_business_data':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
