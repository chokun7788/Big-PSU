import copy,dataclasses,json,time
from unittest.mock import patch
from datetime import datetime
from verification_support import R,snapshot
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.integration import answer
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common import legacy_live_on_demand as bridge,live_window_receipt as receipt_module
from app.booking.live_status import LiveBookingSnapshot,LiveResource,LiveSlot
snap=snapshot();clock=datetime.fromisoformat('2026-10-27T10:00:00+07:00');catalog=json.loads((R.parent/'r124_legacy_guided_parity_20261023/LIVE_CONNECTION_PROBE.json').read_text('utf8'))['catalog'];checks={};rows=[]
class View:
 path=R/'system/data/knowledge/common.sqlite'
 def snapshot(self):return snap
 def still_current(self,s):return s is snap
def fixture(day,slots):return LiveBookingSnapshot(ok=True,date=day,now=clock.isoformat(),generated_at=clock.isoformat(),source='controlled_window_fixture',center_open=True,center_reason='controlled',open_periods=(('09:00','12:00'),('13:00','16:00')),resources=tuple(LiveResource(r['id'],r['name'],5 if 'VR ' in r['name'] else 1,'available',1,slots if r['id']=='15' else (LiveSlot('09:00','12:00','available',0,0,1),LiveSlot('13:00','16:00','available',0,0,1))) for r in catalog))
def run(slots,q='PC2 2026-10-28 ว่าง 10:00-11:30 ไหม',tamper=None,source_snapshot=None):
 global snap
 if source_snapshot is not None:snap=source_snapshot
 calls=[]
 def fetch(day):calls.append(day);return fixture(day,slots)
 u=Understanding([MeaningTask(q,'live','C12','availability','live_status')],True,'controlled_window_source',{'model_called':False})
 with patch('app.booking.live_status.get_live_booking_status',fetch),patch.object(bridge,'freshness_now',lambda:clock):
  if tamper:
   with patch.object(receipt_module,'build',tamper):result=answer(CommonAnswerer(View()),q,locale='en',at=clock,planner=None,_understanding=u)
  else:result=answer(CommonAnswerer(View()),q,locale='en',at=clock,planner=None,_understanding=u)
 from app.knowledge.common.domain_flow.result_contract import attach_runtime
 from app.knowledge.common.domain_flow.engine import Engine
 result=attach_runtime(result,{'execution_question':q},snap,index=Engine.from_snapshot(snap).index)
 row={'question':q,'answer':result.answer,'artifact':result.decision_artifact,'provider_reads':len(calls)};rows.append(row);return row
free=(LiveSlot('09:00','12:00','available',0,0,1),)
busy=(LiveSlot('09:00','10:30','available',0,0,1),LiveSlot('10:30','11:00','busy',1,0,0),LiveSlot('11:00','12:00','available',0,0,1))
r=run(busy);o=r['artifact']['live_booking']['observations'][0];ledger=r['artifact']['execution_contract']['tasks'][0]
checks['window_busy_not_current_resource_free']=o['normalized_status']=='occupied' and ledger['live_observations'][0]['decision']['normalized_status']=='occupied' and 'not available for the full period' in r['answer']
checks['executor_carries_actual_observation_receipt']=bool(r['artifact']['execution_contract']['executor_results'][0]['observation_receipts'])
gap=(LiveSlot('09:00','10:30','available',0,0,1),LiveSlot('11:00','12:00','available',0,0,1));r=run(gap)
checks['missing_half_hour_not_occupied_or_free']=r['artifact']['execution_contract']['tasks'][0]['terminal_state']=='missing_source' and 'Neither free nor occupied status can be confirmed' in r['answer'] and 'is not available for the full period' not in r['answer']
r=run(());checks['no_slots_not_occupied']=r['artifact']['execution_contract']['tasks'][0]['terminal_state']=='missing_source'
r=run((LiveSlot('09:00','12:00','new_unmapped_status',0,0,1),));checks['unknown_slot_status_is_mapping_gap']=r['artifact']['execution_contract']['tasks'][0]['terminal_state']=='missing_source'
r=run((LiveSlot('09:00','12:00','busy',1,0,1),));checks['inconsistent_status_and_count_not_guessed']=r['artifact']['execution_contract']['tasks'][0]['terminal_state']=='missing_source'
r=run((LiveSlot('09:00','12:00','available',0,0,1),LiveSlot('13:00','16:00','unmapped_other_scope',0,0,1)))
checks['unrelated_future_slot_does_not_block_known_window']=r['artifact']['execution_contract']['tasks'][0]['terminal_state']=='supported'
r=run(free,'PC2 2026-10-28 ว่างไหม');o=r['artifact']['live_booking']['observations'][0]
checks['day_list_not_single_free_claim']=o['normalized_status']=='unknown' and o['window_receipt']['decision']['decision_kind']=='recorded_day_slots'
r=run(free,'PC2 2026-10-26 ว่าง 10:00-11:00 ไหม');o=r['artifact']['live_booking']['observations'][0]
checks['historical_unbooked_not_bookable_now']=o['window_receipt']['decision']['decision_kind']=='historical_not_booked' and not o['window_receipt']['decision']['bookable_now_claimed'] and 'had no booking' in r['answer']
r=run(gap,'PC กับ VR 2026-10-28 ว่าง 10:00-11:30 ไหม')
checks['known_resources_preserved_when_one_window_unconfirmed']=r['artifact']['response_type']=='partial_answer' and 'Verified resource subset only' in r['answer'] and r['artifact']['execution_contract']['tasks'][0]['terminal_state']=='partial'
checks['one_provider_snapshot_for_partial_multi_resource']=r['provider_reads']==1
original_build=receipt_module.build
def tampered(*args,**kwargs):
 r=original_build(*args,**kwargs);r['payload']['resource']['slots'][0]['available_count']=0;r['payload']['resource']['slots'][0]['status']='busy';r['payload']['resource']['slots'][0]['booked_count']=1;r['payload_sha256']=receipt_module.digest(r['payload']);r['decision']=receipt_module.verify(r,r['status_mapping']);return r
r=run(free,tamper=tampered)
checks['self_consistent_forged_receipt_rejected_against_actual_request_snapshot']=r['artifact']['execution_contract']['tasks'][0]['terminal_state']=='invalid_plan' and 'could not be verified' in r['answer']
# Current scoped owner calendar comes from the same pinned source snapshot.
from app.knowledge.common.registry import template
from app.knowledge.common.store import CommonStore
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
base=snapshot();work=R/('live_calendar_fixture_'+str(time.time_ns()));work.mkdir();store=CommonStore(work/'source.sqlite');store.initialize(allow_demo=False)
c=template('closure');c['record_id']='controlled_live_closure';c['localization']['en_status']='agent_translated';c['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2027-01-01T00:00:00+07:00'}
for key,value in {'local_date':'2026-10-28','zone_ids':[],'state':'closed','reason':{'th':'ปิดทดสอบ','en':'Controlled closure'}}.items():c['fields'][key]={'status':'known','value':value,'evidence_refs':[],'note':''}
version=0
def merged():
 global c,version
 saved=save_owner_record(store,copy.deepcopy(c),version,'controlled-test');version=saved['version'];c=saved['record'];delta=DraftSnapshotView(store).snapshot();s=copy.deepcopy(base)
 for key in ['records','sources']:s['release'][key].update(delta['release'][key])
 with store.connect() as connection:s['source_pairs'].update(CommonStore.sources(connection))
 s['epoch']+=version;return s
controlled=merged();r=run(free,source_snapshot=controlled);ledger=r['artifact']['execution_contract']['tasks'][0]
checks['current_global_closure_detected_from_pinned_source']=ledger['terminal_state']=='conflict' and ledger['live_observations'][0]['binding_mapping_and_clock_checked'] and ledger['live_observations'][0]['calendar_crosscheck']['record_ids']==[c['record_id']]
checks['verified_live_date_and_time_proof']=all(x['status']=='structurally_supported' and x['proof'] for x in r['artifact']['execution_contract']['verifier_result']['constraint_coverage']['constraints'])
c['validity']={'state':'unknown','effective_from':None,'effective_until':None};r=run(free,source_snapshot=merged());checks['unknown_validity_not_proven_calendar_conflict']=r['artifact']['execution_contract']['tasks'][0]['terminal_state']=='supported'
c['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2027-01-01T00:00:00+07:00'};c['fields']['zone_ids']={'status':'unknown','value':None,'evidence_refs':[],'note':'Controlled unknown zone'};r=run(free,source_snapshot=merged());checks['unknown_zone_not_proven_calendar_conflict']=r['artifact']['execution_contract']['tasks'][0]['terminal_state']=='supported'
# An actual existing zone unrelated to PC2 does not close this resource.
binding=next(x for x in base['release']['records'].values() if x['kind']=='live_binding' and x['fields']['external_resource_key']['value']=='15')
physical=base['release']['records'][binding['fields']['physical_pool_key']['value']];zone=physical['fields']['zone_id']['value']
other=next(rid for rid,x in base['release']['records'].items() if x['kind']=='zone' and rid!=zone)
delta=copy.deepcopy(controlled);delta['release']['records'][c['record_id']]['fields']['zone_ids']['value']=[other]
r=run(free,source_snapshot=delta);checks['other_zone_closure_not_this_resource']=r['artifact']['execution_contract']['tasks'][0]['terminal_state']=='supported'
withdrawn=copy.deepcopy(controlled);withdrawn['release']['records'].pop(c['record_id']);withdrawn['withdrawn'].append(c['record_id']);withdrawn['epoch']+=100;r=run(free,source_snapshot=withdrawn);checks['withdrawn_closure_not_reused_from_prior_snapshot']=r['artifact']['execution_contract']['tasks'][0]['terminal_state']=='supported'
snap=base
report={'all_passed':all(checks.values()),'checks':checks,'actual_provider_http_calls':0,'actual_model_inferences':0,'user_data_changes':0};out=R/('live_window_proofs_'+str(time.time_ns()));out.mkdir();(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
