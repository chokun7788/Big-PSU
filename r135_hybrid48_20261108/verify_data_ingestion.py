"""Requirement-specific owner data controls, isolated from all business stores."""
import copy,json,time
from verification_support import R
from app.knowledge.common.registry import template,validate,schema_errors
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView,PinnedSnapshotView
from app.knowledge.common.task_registry import readiness
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.capabilities import catalog_for,resolve
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
out=R/('data_ingestion_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False);checks={};details={}
def known(v):return {'status':'known','value':v,'evidence_refs':[],'note':''}
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated'
 for k,v in fields.items():r['fields'][k]=known(v)
 return save_owner_record(store,r,0,'controlled-test')['record']
service=create('service','controlled_data_service',{'name':{'th':'บริการทดสอบไพลิน','en':'Sapphire controlled service'},'resource_ids':[],'platform':'PC','session_minutes':30,'occupancy_minutes':35,'capacity_min':1,'capacity_max':1})
audience=create('audience','controlled_data_audience',{'name':{'th':'กลุ่มทดสอบ','en':'Controlled audience'}})
rate=create('rate','controlled_data_rate',{'service_id':service['record_id'],'audience_id':audience['record_id'],'amount_minor':25000,'currency':'THB','unit':'per_session','duration_minutes':30})
with store.connect() as c:records=store.heads(c);sources=store.sources(c)
checks['valid_price_relation_and_currency_accepted']=not validate(rate,records,sources)
for label,key,value in [('currency','currency','USD'),('unit','unit','per_unknown'),('duration_zero','duration_minutes',0),('duration_string','duration_minutes','30'),('negative_price','amount_minor',-1)]:
 bad=copy.deepcopy(rate);bad['fields'][key]['value']=value;checks[label+'_rejected_before_index']=bool(schema_errors(bad))
for label,key,value,needle in [('missing_service','service_id','missing_service','missing reference'),('wrong_service_kind','service_id',audience['record_id'],'wrong reference kind')]:
 bad=copy.deepcopy(rate);bad['fields'][key]['value']=value;checks[label+'_reported']=any(needle in e for e in validate(bad,records,sources))
for state in ['unknown','not_applicable','conflicted']:
 bad=copy.deepcopy(rate);bad['fields']['amount_minor']={'status':state,'value':None,'evidence_refs':copy.deepcopy(rate['fields']['amount_minor']['evidence_refs'])*2 if state=='conflicted' else [],'note':'Controlled unresolved source'}
 checks[state+'_has_explicit_nonasserting_representation']=not schema_errors(bad)
 if state=='conflicted':checks['conflicted_not_publishable']=any('unresolved conflict' in e for e in validate(bad,records,sources,publish=True))
game=create('game','controlled_data_game',{'title':{'th':'เกมทดสอบโอปอล','en':'Controlled Opal'},'genre':{'th':'แนวทดสอบ','en':'Controlled genre'}})
readiness_before=readiness(game,{**records,game['record_id']:game},locale='en')
checks['missing_game_service_relation_reported']=any(t['task']=='game_offerings' and t['status']=='needs_data' and any(m.get('relation')=='game_service' for m in t['missing']) for t in readiness_before['tasks'])
relation=create('game_service','controlled_data_offering',{'game_id':game['record_id']})
with store.connect() as c:partial_records=store.heads(c)
checks['incomplete_offering_relation_not_ready']=next(t for t in readiness(game,partial_records)['tasks'] if t['task']=='game_offerings')['status']=='needs_data'
relation['fields'].update({k:known(v) for k,v in {'service_id':service['record_id'],'offered':True,'installed_resource_ids':[]}.items()});relation=save_owner_record(store,relation,1,'controlled-test')['record']
with store.connect() as c:all_records=store.heads(c)
checks['explicit_relation_resolves_owner_gap']=next(t for t in readiness(game,all_records)['tasks'] if t['task']=='game_offerings')['status']=='data_ready'
bad_rel=copy.deepcopy(relation);bad_rel['fields']['service_id']=known(audience['record_id']);bad_records={**all_records,relation['record_id']:bad_rel}
checks['related_wrong_target_kind_not_ready']=next(t for t in readiness(game,bad_records)['tasks'] if t['task']=='game_offerings')['status']=='needs_data'
bad_rel['record_id']='controlled_data_unfinished';bad_rel['fields']['service_id']={'status':'unknown','value':None,'evidence_refs':[],'note':'Unresolved service'}
checks['unfinished_sibling_does_not_erase_complete_relation']=next(t for t in readiness(game,{**all_records,bad_rel['record_id']:bad_rel})['tasks'] if t['task']=='game_offerings')['status']=='data_ready'
view=DraftSnapshotView(store);pinned=PinnedSnapshotView(view);before=pinned.snapshot();idx=Engine.from_snapshot(before,cache_key=view.path).index
game_update=copy.deepcopy(game);game_update['aliases']['en']=['New Opal Alias'];saved=save_owner_record(store,game_update,1,'controlled-test')
checks['pinned_records_and_aliases_remain_one_revision']=pinned.snapshot()['release']['records'][game['record_id']]['revision']==1 and 'New Opal Alias' not in pinned.snapshot()['release']['records'][game['record_id']]['aliases']['en']
checks['source_change_invalidates_old_request']=not pinned.still_current(before)
new_index=Engine.from_snapshot(view.snapshot(),cache_key=view.path).index
checks['new_alias_without_prompt_or_weights_change']=bool(new_index.bind('C04','New Opal Alias')) and not idx.bind('C04','New Opal Alias')
cat=catalog_for(new_index);rows=[row for c in cat['categories'] for row in c['adapter_rows']]
checks['catalog_is_bound_to_added_price_and_game_sources']=any(rate['record_id'] in row['source_inputs']['source_record_ids'] for row in rows if row['category']=='C06') and any(game['record_id'] in row['source_inputs']['source_record_ids'] for row in rows if row['category']=='C04')
checks['offering_projection_keeps_relation_evidence']=any(f['facet']=='studio_services' and f['record_id']==game['record_id'] and any(ref in f['evidence_refs'] for ref in relation['fields']['offered']['evidence_refs']) for f in new_index.bycat['C04'])
checks['unknown_operation_not_advertised_or_silently_detail']=resolve('C04','invent_operation','genre')['status']=='unsupported_operation'
equipment=create('equipment_model','controlled_data_equipment',{'name':{'th':'เครื่องทดสอบบุษราคัม','en':'Controlled Topaz device'},'device_type':'peripheral','specifications':[{'key':'buttons','value':'twelve buttons','unit':None}]})
def typed(q,category,facet,target):
 e=Engine.from_snapshot(view.snapshot(),cache_key=view.path);u=Understanding([MeaningTask(q,'controlled_data',category,'detail',facet,target)],True,'controlled_data_no_inference',{'model_called':False})
 result=e.answer(q,'en',at=reference_time('2026-10-26T12:00:00+07:00'),allow_llm=False,understanding=u)
 details.setdefault('typed_answers',[]).append({'question':q,'result':result});return result
genre=typed('What genre is New Opal Alias?','C04','genre','New Opal Alias');checks['new_game_alias_reaches_typed_answer_without_training']=any(c['record_id']==game['record_id'] and 'Controlled genre' in c['value'] for c in genre['claims'])
specs=typed('What are the specifications of Controlled Topaz device?','C03','specifications','Controlled Topaz device');checks['new_equipment_source_reaches_typed_answer_without_training']=any(c['record_id']==equipment['record_id'] and 'twelve buttons' in c['value'] for c in specs['claims'])
quote=typed('What is the price of Sapphire controlled service for Controlled audience?','C06','amount','Sapphire controlled service');checks['new_rate_reaches_typed_answer_without_training']=any(c['record_id']==rate['record_id'] and '250' in c['value'] for c in quote['claims'])
edited=copy.deepcopy(rate);edited['fields']['amount_minor']=known(37500);save_owner_record(store,edited,1,'controlled-test')
quote=typed('What is the price of Sapphire controlled service for Controlled audience?','C06','amount','Sapphire controlled service');checks['edited_rate_changes_next_typed_answer_without_training']=any(c['record_id']==rate['record_id'] and '375' in c['value'] for c in quote['claims']) and all('250' not in c['value'] for c in quote['claims'])
from app.knowledge.common.answer import CommonAnswerer
from unittest.mock import patch
with patch('urllib.request.urlopen',side_effect=AssertionError('No model/provider HTTP permitted in data-addition controls')):
 for label,q,expected in [('game','What genre is New Opal Alias?','Controlled genre'),('equipment','What are the specifications of Controlled Topaz device?','twelve buttons'),('rate','What is the price of Sapphire controlled service for Controlled audience?','375')]:
  natural=CommonAnswerer(view).answer(q,locale='en',at=reference_time('2026-10-26T12:00:00+07:00'),planner=None)
  details.setdefault('natural_answers',[]).append({'question':q,'answer':natural.answer,'artifact':natural.decision_artifact});checks[label+'_new_data_works_through_normal_common_answerer']=expected in natural.answer
checks['save_does_not_create_any_publication_or_approval']=store.snapshot()['release'] is None
with store.connect() as c:checks['all_created_sources_still_unapproved']=c.execute('SELECT count(*) FROM cc_approvals').fetchone()[0]==0
# A bookable interval may span adjacent opening segments, but never a real gap.
schedule=template('schedule');schedule['record_id']='controlled_data_schedule'
for k,v in {'weekday':0,'timezone':'Asia/Bangkok','zone_ids':[],'open_periods':[{'start':'09:00','end':'11:00'},{'start':'11:00','end':'13:00'}],'bookable_periods':[{'start':'10:00','end':'12:00'}],'maintenance_periods':[]}.items():schedule['fields'][k]=known(v)
try:save_owner_record(store,copy.deepcopy(schedule),0,'controlled-test');checks['adjacent_opening_union_accepts_valid_booking']=True
except ValueError as e:checks['adjacent_opening_union_accepts_valid_booking']=False;details['adjacent_opening_error']=str(e)
gap=copy.deepcopy(schedule);gap['record_id']='controlled_data_gap';gap['fields']['open_periods']['value'][1]['start']='11:30'
try:save_owner_record(store,gap,0,'controlled-test');checks['real_opening_gap_rejects_booking']=False
except ValueError as e:checks['real_opening_gap_rejects_booking']='Booking period outside opening' in str(e)
report={'all_passed':all(checks.values()),'checks':checks,'details':{k:v for k,v in details.items() if k not in {'typed_answers','natural_answers'}},'actual_model_inferences':0,'user_data_modified':False,'publication_approval_created':False,'controlled_source_not_real_business_data':True}
(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8')
(out/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report},ensure_ascii=False));assert report['all_passed']
