"""Independent source-positive/negative controls for two saved-input bugs."""
import copy,json,os,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.duration_scope import repeated_duration
from app.knowledge.common.domain_flow.offering_intent import named_game_offering
from app.knowledge.common.domain_flow.routing import route
from app.knowledge.common.domain_flow.request_verifier import observe
from app.knowledge.common.domain_flow.understanding import MeaningTask
O=R/('duration_offering_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'isolated.sqlite');store=CommonStore(O/'source.sqlite');store.initialize(allow_demo=False);bi=lambda s:{'th':s,'en':s};checks={};details=[];clock='2026-10-27T10:00:00+07:00'
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'isolated-duration-offering')['record']
create('zone','amber_zone',{'name':bi('Amber zone')});create('service','amber_service',{'name':bi('Amber service'),'platform':'PC','session_minutes':60,'capacity_min':1,'capacity_max':1,'resource_ids':[],'studio_zone_ids':['amber_zone']});create('audience','amber_visitors',{'name':bi('Amber visitors')});rate=create('rate','amber_rate',{'service_id':'amber_service','audience_id':'amber_visitors','amount_minor':10000,'currency':'THB','unit':'per_session','duration_minutes':60,'calculation_rule':'linear','persons_min':1,'persons_max':1});create('game','cobalt_game',{'title':bi('Cobalt story'),'genre':bi('Source Cobalt genre'),'studio_zone_ids':['amber_zone']});create('game_service','cobalt_offer',{'game_id':'cobalt_game','service_id':'amber_service','offered':True});create('game','duration_named_game',{'title':bi('1 hour 1 hour'),'genre':bi('Named duration genre')});view=DraftSnapshotView(store);engine=Engine.from_snapshot(view.snapshot())
for q,name in [('Amber service 1 hour 1 hour','numeric_english'),('Amber service 1 ชั่วโมง 1 ชั่วโมง','numeric_thai'),('Amber service 1ชั่วโมง1ชั่วโมง','no_space_thai'),('Amber service one hour one hour','verbal_english'),('Amber service 1.0 hours 1 hour','numeric_equal_forms')]:
 p=repeated_duration(engine.index,q);checks[name+'_raw_repeat_observed']=bool(p) and q[p['source_span']['start']:p['source_span']['end']]==p['source_span']['text'];meaning=MeaningTask(q,'service_fee','C06','price_calculate','amount',ambiguous=False);r=engine.plan('C06',q,clock,meaning);checks[name+'_unambiguous_proposal_cannot_override_raw']=r.status=='missing_input' and not r.ids and r.metadata.get('context_clarification') is not None
for q,name in [('Amber service 1 hour 30 minutes','compound_duration'),('Amber service 30 minutes or 1 hour','alternative_durations'),('Amber service 1 hour per session for 2 hours','billing_period'),('What is the price to play the game "1 hour 1 hour"?','source_name')]:checks[name+'_not_mistaken_for_adjacent_repeat']=repeated_duration(engine.index,q) is None
def public(q,key):
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected actual HTTP')):r=CommonAnswerer(view).answer(q,locale='en',at=clock,planner=None)
 details.append({'case':key,'question':q,'answer':r.answer,'artifact':r.decision_artifact});return r
for duration in ['1 hour 1 hour','1 ชั่วโมง 1 ชั่วโมง']:
 r=public('What is the price of Amber service for Amber visitors '+duration+'?',duration)
 c=r.decision_artifact.get('execution_contract',{});checks[duration+'_public_no_price_claim']=not r.decision_artifact.get('domain_flow',{}).get('typed_claims') and ('confirm' in r.answer.lower() or 'specify' in r.answer.lower() or 'unresolved' in r.answer.lower());checks[duration+'_compiler_ambiguity_preserved']=any('adjacent_repeated_duration_requires_clarification' in t.get('ambiguities',[]) for t in c.get('request_plan',{}).get('tasks',[]))
def source_price(r,expected):
 claims=[c for c in r.decision_artifact.get('domain_flow',{}).get('typed_claims',[]) if c.get('facet')=='amount'];return len(claims)==1 and claims[0]['record_id']=='amber_rate' and claims[0]['numeric']==expected and bool(claims[0]['evidence_refs'])
r=public('What is the price of Amber service for Amber visitors 1 hour?','single_source_positive');checks['single_hour_source_price_preserved']=source_price(r,rate['fields']['amount_minor']['value']/100)
r=public('What is the price of Amber service for Amber visitors 1 hour 30 minutes?','compound_source_positive');checks['compound_90minutes_source_price_preserved']=source_price(r,rate['fields']['amount_minor']['value']/100*1.5)
changed=copy.deepcopy(rate);changed['fields']['amount_minor']['value']=25000;changed=save_owner_record(store,changed,rate['revision'],'isolated-source-price-change')['record'];r=public('What is the price of Amber service for Amber visitors 1 hour?','changed_source_positive');checks['changed_source_rate_changes_next_actual_numeric_claim']=source_price(r,changed['fields']['amount_minor']['value']/100)
r=public('What is the price of Amber service for Amber visitors 1 hour 1 hour?; What genre is Cobalt story?','independent_after_ambiguous_price');claims=r.decision_artifact.get('domain_flow',{}).get('typed_claims',[]);checks['ambiguous_price_does_not_discard_independent_source_genre']=not any(c.get('facet')=='amount' for c in claims) and any(c.get('facet')=='genre' and c.get('record_id')=='cobalt_game' and c.get('value')=='Source Cobalt genre' for c in claims)
for q,name in [('Is there a Cobalt story game available?','exists'),('Is Cobalt story available?','named_available'),('Do you offer Cobalt story?','offered')]:
 checks[name+'_offering_predicate']=named_game_offering(engine.index,q) and route(engine.index,q)=='C04';obs=observe(engine.index,q);checks[name+'_independent_observer_offering_scope']=any(n['category']=='C04' and n['facet']=='studio_services' for n in obs['needs']) and all(n['category']!='C12' for n in obs['needs']);r=public(q,name);checks[name+'_positive_source_not_provider_failure']=bool(r.decision_artifact.get('domain_flow',{}).get('typed_claims')) and 'booking connection is unavailable' not in r.answer.lower()
 source=view.snapshot()['release']['records'];expected_service=source['amber_service']['fields']['name']['value']['en'];offering_refs=source['cobalt_offer']['fields']['offered']['evidence_refs'];claims=r.decision_artifact.get('domain_flow',{}).get('typed_claims',[]);checks[name+'_claim_bound_to_offered_relation_and_source_service']=any(c.get('record_id')=='cobalt_game' and c.get('facet')=='studio_services' and c.get('value')==expected_service and any(ref in c.get('evidence_refs',[]) for ref in offering_refs) for c in claims)
for q,name in [('Is Cobalt story available today?','dated'),('Is Cobalt story available now?','now'),('Is Cobalt story available at 15:00?','clock'),('Is Cobalt story available on Monday?','weekday'),('What is the price of Cobalt story?','price'),('What buttons are available in Cobalt story?','controls')]:checks[name+'_not_unconditionally_static']=not named_game_offering(engine.index,q)
# Remove only the source offering in this isolated DB; title presence must not
# turn into a confirmed studio offering or a false negative unavailability.
with store.connect(write=True) as c:c.execute('UPDATE cc_heads SET withdrawn=1 WHERE record_id=?',('cobalt_offer',));c.execute("UPDATE cc_meta SET value=CAST(value AS INTEGER)+1 WHERE key='epoch'")
r=public('Is there a Cobalt story game available?','offering_missing_negative');claims=r.decision_artifact.get('domain_flow',{}).get('typed_claims',[]);checks['missing_offer_not_confirmed_from_game_title']=not any(c.get('facet')=='studio_services' for c in claims)
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_HTTP':0,'owner_data_modified':False,'source_control_scope':'isolated actual owner-schema sources; not a semantic benchmark','gpu_or_training_started':False};(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
