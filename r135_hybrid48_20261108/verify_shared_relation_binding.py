"""An omitted game target requires an actual service/offering source edge."""
import copy,json,time
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.context_guard import apply
from app.knowledge.common.domain_flow.plan_contract import compile_request
out=R/('shared_relation_binding_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False);checks={};details={}
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated'
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
service=create('service','controlled_blue_service',{'name':{'th':'บริการบลู','en':'Blue'},'platform':'PC','resource_ids':[],'capacity_min':1,'capacity_max':2})
game=create('game','controlled_blue_game',{'title':{'th':'เกมบลู','en':'Blue'},'genre':{'th':'แนวทดสอบ','en':'Controlled genre'}})
audience=create('audience','controlled_relation_audience',{'name':{'th':'กลุ่มทดสอบ','en':'Controlled audience'}})
rate=create('rate','controlled_relation_rate',{'service_id':service['record_id'],'audience_id':audience['record_id'],'amount_minor':10000,'currency':'THB','unit':'per_session','duration_minutes':30})
other=create('service','controlled_red_service',{'name':{'th':'บริการเรด','en':'Red'},'platform':'PC','resource_ids':[]})
othergame=create('game','controlled_other_game',{'title':{'th':'เกมอื่น','en':'Other game'}})
create('game_service','controlled_other_offering',{'game_id':othergame['record_id'],'service_id':other['record_id'],'offered':True})
q='How many people can Blue accommodate, and what games are offered?';quote1='How many people can Blue accommodate';quote2='what games are offered?'
u=Understanding([MeaningTask(quote1,'equipment','C03','detail','service_capacity','Blue'),MeaningTask(quote2,'games','C04','list','game_catalog')],True,'controlled_source_relation',{'model_called':False})
view=DraftSnapshotView(store)
def run():
 e=Engine.from_snapshot(view.snapshot(),cache_key=view.path);working=apply(q,e.index,copy.deepcopy(u));c=compile_request(q,working,e.index,{'release_id':'owner-draft-preview','epoch':view.snapshot()['epoch'],'reference_time':'2026-10-26T12:00:00+07:00'});r=e.answer(q,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=copy.deepcopy(u));return e,c,r
e,c,r=run();details['without_relation']={'plan':c.as_dict(),'result':r}
checks['shared_alias_alone_not_a_validated_service_game_relation']=not any(b.basis=='source_related_service_game_ellipsis' and getattr(b,'validation_outcome','validated')=='validated' for b in c.tasks[1].bindings)
checks['missing_relation_does_not_deliver_unrelated_global_catalog']=not any(claim['facet']=='game_catalog' for claim in r['claims'])
relation=create('game_service','controlled_blue_offering',{'game_id':game['record_id'],'service_id':service['record_id'],'offered':True})
e,c,r=run();details['with_relation']={'plan':c.as_dict(),'result':r};bindings=c.tasks[1].bindings
checks['actual_offering_relation_allows_ellipsis']=any(b.basis=='source_related_service_game_ellipsis' for b in bindings) and any(claim['facet']=='game_catalog' and 'Blue' in claim['value'] and 'Other game' not in claim['value'] for claim in r['claims'])
checks['shared_binding_preserves_relation_record_and_revision']=any(any(ref.get('record_id')==relation['record_id'] and ref.get('record_revision')==relation['revision'] and ref.get('evidence_refs') for ref in getattr(b,'relation_refs',[])) for b in bindings)
checks['shared_binding_preserves_source_entity_refs_and_validation']=any(service['record_id'] in getattr(b,'entity_refs',[]) and getattr(b,'validation_outcome',None)=='validated' for b in bindings)
checks['root_shared_binding_keeps_typed_relation_proof']=any(b.get('basis')=='source_related_service_game_ellipsis' and b.get('relation_refs') and b.get('validated') for b in c.shared_bindings)
from app.knowledge.common.domain_flow.obligation_verifier import assess
forged=copy.deepcopy(c.tasks[1]);forged.bindings[0].relation_refs[0]['record_revision']=9999
proof=assess(e.index,forged,copy.deepcopy(r['needs'][1]),r['execution_contract']['request_plan']['snapshot'],q);checks['forged_shared_relation_revision_rejected']='source_receipt_shared_relation_unproven' in proof['fatal']
store.withdraw(relation['record_id'],actor='controlled-test');e,c,r=run();details['withdrawn_relation']={'plan':c.as_dict(),'result':r};checks['withdrawn_relation_not_a_cached_shared_edge']=not any(claim['facet']=='game_catalog' for claim in r['claims'])
checks['unresolved_relation_keeps_independent_capacity_evidence']=any(claim['record_id']==service['record_id'] and claim['facet']=='service_capacity' for claim in r['claims'])
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'user_data_modified':False,'controlled_source_not_real_business_data':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
