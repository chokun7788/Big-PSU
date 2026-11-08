"""Actual source lifecycle + predeclared legacy reader + direct receipt forgery."""
import copy,json,os,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.hybrid_policy import choose

out=R/('hybrid_routes_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'sessions.sqlite')
store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store)
checks={};details=[];q='What device type is Amber Console?';at='2026-11-08T12:00:00+07:00'
def create(rid,name,kind):
    r=template('equipment_model');r['record_id']=rid;r['localization']['en_status']='agent_translated'
    r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
    for k,v in {'name':{'th':name,'en':name},'device_type':kind}.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
    return save_owner_record(store,r,0,'hybrid-controlled')['record']
record=create('amber_console','Amber Console','console');create('cobalt_console','Cobalt Console','vr')
def run():
    e=Engine.from_snapshot(view.snapshot());u=Understanding([MeaningTask(q,'equipment','C03','detail','device_type')],True,'controlled',{'model_called':False})
    with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=e.answer(q,'en',at=at,allow_llm=False,understanding=u)
    details.append(r);return r,e,u
r,e,u=run();child=r['needs'][0]
checks['positive_source_claim']=any(c['record_id']=='amber_console' and c['value']=='console' for c in r['claims'])
checks['predeclared_legacy_used']=child['plan']['metadata']['hybrid_route']['reader']=='r134_compat'
checks['same_snapshot']=r['execution_contract']['request_plan']['snapshot']['epoch']==e.data['epoch']
checks['legacy_receipts_checked']=bool(child['execution_contract']['receipts']) and not child['execution_contract']['fatal']
task=compile_request(q,u,e.index,r['execution_contract']['request_plan']['snapshot']).tasks[0]
forged=copy.deepcopy(child);f=next(f for f in e.index.byrecord['cobalt_console'] if f['facet']=='device_type');forged['claims']=[{'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'value':f['value']['en'],'numeric':None,'evidence_refs':f['evidence_refs']}]
checks['wrong_entity_direct_injection_rejected']=bool(assess(e.index,task,forged,r['execution_contract']['request_plan']['snapshot'],q)['fatal'])
edited=copy.deepcopy(record);edited['fields']['device_type']['value']='pc';record=save_owner_record(store,edited,record['revision'],'hybrid-owner-edit')['record'];updated,_,_=run()
checks['actual_owner_edit']=any(c['value']=='pc' for c in updated['claims']) and all(c['value']!='console' for c in updated['claims'])
with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):natural=CommonAnswerer(view).answer(q,locale='en',at=at,planner=None)
details.append({'natural_answer':natural.answer,'artifact':natural.decision_artifact})
checks['natural_common_positive']='pc' in natural.answer and natural.decision_artifact.get('hybrid',{}).get('experimental') is True
checks['natural_common_uses_legacy_route']=any(x.get('reader')=='r134_compat' for x in natural.decision_artifact['hybrid']['reader_routes'])
from app.knowledge.common.domain_flow.native_intents import propose
checks['type_predicate_alone_does_not_bind_entity']=propose(e.index,'What device type is Unknown Console?') is None
checks['conditional_type_not_shortcut']=propose(e.index,'If Amber Console is available, what device type is it?') is None
store.withdraw('amber_console',actor='hybrid-owner-withdraw');withdrawn,_,_=run()
checks['actual_withdrawal']=not any(c['record_id']=='amber_console' for c in withdrawn['claims'])
checks['unknown_route_withheld']=choose('C03','invented_operation','device_type')['reader']=='withhold'
checks['no_post_failure_fallback']=choose('C03','detail','device_type')['fallback_after_rejection'] is False
report={'all_passed':all(checks.values()),'checks':checks,'scope':'controlled source and natural CommonAnswerer, no model/HTTP or production authority'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
