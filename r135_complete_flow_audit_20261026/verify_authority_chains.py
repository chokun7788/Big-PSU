"""Real isolated owner-attested mapping/authority source controls."""
import copy,json,time
from verification_support import R
from app.knowledge.common.registry import template,value
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.authority_resolution import resolve
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.claim_bindings import validate_bindings
out=R/('authority_chains_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False);checks={};details=[];at=reference_time('2026-10-26T12:00:00+07:00')
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
zone=create('zone','controlled_authority_zone',{'name':{'th':'โซนทดสอบ','en':'Controlled authority zone'}})
resource=create('resource','controlled_authority_resource',{'name':{'th':'เครื่องทดสอบ','en':'Controlled authority resource'},'zone_id':zone['record_id'],'physical_pool_key':'controlled_authority_pool','operational_status':'in_service'})
service=create('service','controlled_authority_service',{'name':{'th':'บริการอำพัน','en':'Amber service'},'resource_ids':[resource['record_id']],'platform':'PC','session_minutes':30,'occupancy_minutes':30,'capacity_min':1,'capacity_max':1})
other=create('service','controlled_authority_other_service',{'name':{'th':'บริการไพลิน','en':'Sapphire service'},'resource_ids':[resource['record_id']],'platform':'PS5','session_minutes':30,'occupancy_minutes':30,'capacity_min':1,'capacity_max':1})
old=create('faq','controlled_authority_old',{'question':{'th':'จองอย่างไร','en':'How to book Amber?'},'answer':{'th':'ขั้นตอนฉบับเก่า','en':'Old booking procedure'},'topic':'booking'})
new=create('faq','controlled_authority_new',{'question':{'th':'จองอย่างไร','en':'How to book Amber?'},'answer':{'th':'ขั้นตอนฉบับใหม่','en':'New booking procedure'},'topic':'booking'})
def bind(record,supersedes=None,app=None):
 return {'binding_id':'booking','predicate':'booking_policy','subject_ref':service['record_id'],'value_ref':{'record_id':record['record_id'],'field':'answer','path':'','projection':'identity'},'unit':None,'actor_scope':{'status':'known','value':[]},'conditions_status':'known','condition_refs':[],'exceptions_status':'known','exception_refs':[],'applicability':{'status':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None,'service_ids':[service['record_id']],'duration_minutes':None,'platform':None,**(app or {})},'dependency_refs':[],'supersedes_refs':supersedes or [],'evidence_refs':[],'authority_refs':[]}
def save(record,binding,authority=False):
 record=copy.deepcopy(record);record['claim_bindings']=[binding];return save_owner_record(store,record,record['revision'],'controlled-test',mapping_authority_confirmed=authority)['record']
old=save(old,bind(old));new=save(new,bind(new,[old['record_id']+'#booking']),True)
def evaluate(label):
 view=DraftSnapshotView(store);engine=Engine.from_snapshot(view.snapshot(),cache_key=view.path);i=engine.index
 facts=[]
 for rid in [old['record_id'],new['record_id']]:
  r=i.records[rid];facts.append({'id':'C08:'+rid+':answer','record_id':rid,'category':'C08','facet':'owner_policy','value':value(r,'answer'),'validity':r['validity'],'evidence_refs':r['fields']['answer']['evidence_refs']})
 result=resolve(i,facts,at);details.append({'case':label,'result':result,'validation_errors':{rid:validate_bindings(i.records[rid],i.records,i.source_pairs,publish=False,demo=False) for rid in [old['record_id'],new['record_id']]},'records':{rid:i.records[rid] for rid in [old['record_id'],new['record_id']]}});return result,i
r,i=evaluate('verified_same_scope_supersession');checks['positive_owner_attested_authority_selects_new']=r['status']=='equivalent' and [f['record_id'] for f in r['facts']]==[new['record_id']] and old['record_id'] in r['superseded']
checks['mapping_and_authority_pointers_independently_valid']=not validate_bindings(i.records[new['record_id']],i.records,i.source_pairs,publish=False,demo=False)
saved=copy.deepcopy(new);b=copy.deepcopy(new['claim_bindings'][0]);new=save(new,{**b,'applicability':{**b['applicability'],'service_ids':[other['record_id']]}},True)
r,i=evaluate('different_service_applicability');checks['other_service_scope_does_not_supersede_old']=not r['superseded'] and len(r['facts'])==2
new=save(new,bind(new,[old['record_id']+'#booking'],{'duration_minutes':60}),True);r,i=evaluate('different_duration_applicability');checks['other_duration_scope_does_not_supersede_old']=not r['superseded'] and len(r['facts'])==2
new=save(new,bind(new,[old['record_id']+'#booking'],{'platform':'PS5'}),True);r,i=evaluate('different_platform_applicability');checks['other_platform_scope_does_not_supersede_old']=not r['superseded'] and len(r['facts'])==2
new=save(new,bind(new,[old['record_id']+'#booking'],{'effective_from':'2027-01-01T00:00:00+07:00'}),True);r,i=evaluate('future_authority_applicability');checks['future_authority_not_effective_early']=not r['superseded']
new=save(new,bind(new,[old['record_id']+'#booking']),False);r,i=evaluate('source_mapping_without_confirmed_authority');checks['mapping_alone_does_not_supersede']=not r['superseded']
new=save(new,bind(new,[old['record_id']+'#booking']),True)
publish_ids=[zone['record_id'],resource['record_id'],service['record_id'],other['record_id'],old['record_id'],new['record_id']]
for rid in publish_ids:
 item=store.get(rid);store.approve(rid,item['record']['revision'],item['hash'],actor='controlled-reviewer')
release=store.publish(publish_ids,actor='controlled-reviewer',expected_active='',request_key='controlled-authority-publication')
published=store.snapshot();pi=Engine.from_snapshot(published,cache_key=store.path).index
checks['published_snapshot_pins_actual_source_bodies']=bool(pi.source_pairs) and set(pi.source_pairs)==set(published['release']['sources'])
checks['published_mapping_and_authority_still_valid']=not validate_bindings(pi.records[new['record_id']],pi.records,pi.source_pairs,publish=False,demo=False)
old=save(old,bind(old,[new['record_id']+'#booking']),True);r,i=evaluate('cyclic_draft_authority');checks['cyclic_draft_authority_does_not_remove_both_sources']=len(r['facts'])==2 and not r['superseded'] and bool(r['review_required'])
after=store.snapshot();checks['new_draft_mapping_source_not_mixed_into_published_release']=after['release']==published['release'] and after['source_pairs']==published['source_pairs'] and DraftSnapshotView(store).snapshot()['source_pairs']!=published['source_pairs']
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_real_business_data':True}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
