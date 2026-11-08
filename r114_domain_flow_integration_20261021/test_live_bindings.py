"""New provider binding, fresh/stale/unknown and one request-scoped read."""
import copy,json,os,sqlite3,sys,dataclasses
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'system';T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False);sys.path.insert(0,str(S))
os.environ.update(PSU_ESPORTS_NOW='2026-10-19T12:00:00+07:00',PSU_LOCAL_LLM_ASSIST_ENABLED='0')
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.flow_context import request_context
from app.booking.live_status import LiveBookingSnapshot,LiveResource,LiveSlot
from app.knowledge.common.dialogue import state_from_answer
src=R.parent/'r58_examples_240_20261012/DEMO_ONLY.sqlite';db=T/'SYNTHETIC_LIVE_ONLY.sqlite'
with sqlite3.connect(src.as_uri()+'?mode=ro',uri=True) as a,sqlite3.connect(db) as b:a.backup(b)
store=CommonStore(db);records=store.snapshot()['release']['records'];binding=copy.deepcopy(next(r for r in records.values() if r['kind']=='live_binding'))
binding['fields']={**template('live_binding')['fields'],**binding['fields']}
binding['fields']['freshness_max_age_seconds'].update(status='known',value=30)
binding['fields']['external_resource_key']['value']='R101_NEW_EXTERNAL_POOL'
binding=save_owner_record(store,binding,binding['revision'],'isolated-live-test')['record']
service=copy.deepcopy(records[value(binding,'service_id')]);service['aliases']['en'].append('Aurora Live Fixture')
service=save_owner_record(store,service,service['revision'],'isolated-live-test')['record']
raw=next(m['raw'] for m in value(binding,'status_mapping') if m['normalized']=='free')
resource=LiveResource('R101_NEW_EXTERNAL_POOL','Synthetic provider pool',1,raw,1,())
def snapshot(generated='2026-10-19T12:00:00+07:00',resources=(resource,)):
 return LiveBookingSnapshot(True,'2026-10-19','2026-10-19T12:00:00+07:00',generated,'remote_csv_live',True,'fixture',(),resources)
checks=[]
def check(name,ok,detail=None):
 row={'case':name,'passed':bool(ok),'detail':detail};checks.append(row);print(name,bool(ok),flush=True)
def ask(q='Is Aurora Live Fixture available now?',history=None):return CommonAnswerer(DraftSnapshotView(store)).answer(q,locale='en',history=history)
with patch('app.booking.live_status.get_live_booking_status',return_value=snapshot()) as provider,request_context():
 a=ask();b=ask()
 check('owner-added external binding is read without hardcoded resource names',a is not None and 'available (' in a.answer,a.answer if a else None)
 check('freshness and provider scope are recorded',a.decision_artifact['live_booking']['observations'][0]['freshness_checked'])
 check('same provider/date fetched once for whole request',provider.call_count==1)
with patch('app.booking.live_status.get_live_booking_status',return_value=snapshot()) as provider:
 a=ask('Is Aurora Live Fixture available now?; Is Aurora Live Fixture available now?')
 check('compound live tasks use actual adapter and one provider read',provider.call_count==1 and a.answer.count('available (')==2,a.answer)
 check('compound task ledger preserves both needs',len(a.decision_artifact.get('need_results',[]))==2 and all(n['status']=='supported' for n in a.decision_artifact['need_results']))
with patch('app.booking.live_status.get_live_booking_status',return_value=snapshot('2026-10-19T11:58:00+07:00')):
 a=ask();check('expired observation is never available',a.decision_artifact['response_type']=='live_unavailable' and 'available (' not in a.answer)
unknown=LiveResource('R101_NEW_EXTERNAL_POOL','Synthetic provider pool',1,'UNMAPPED_STATUS',1,())
with patch('app.booking.live_status.get_live_booking_status',return_value=snapshot(resources=(unknown,))):
 a=ask();check('unknown status with positive count is not inferred free',a.decision_artifact['response_type']=='live_unavailable')
occupied_raw=next(m['raw'] for m in value(binding,'status_mapping') if m['normalized']=='occupied')
future_resource=dataclasses.replace(resource,slots=(LiveSlot('15:00','16:00',occupied_raw,1,0,0),))
with patch('app.booking.live_status.get_live_booking_status',return_value=snapshot(resources=(future_resource,))):
 a=ask('Is Aurora Live Fixture available at 15:00?')
 check('future point uses its slot, not available_now','occupied (' in a.answer and '15:00' in a.answer,a.answer)
 a=ask('Is Aurora Live Fixture available from 14:00 to 16:00?')
 check('range with uncovered interval cannot be confirmed free',a.decision_artifact['response_type']=='live_unavailable')
tomorrow=dataclasses.replace(snapshot(resources=(dataclasses.replace(resource,slots=(LiveSlot('15:00','16:00',raw,0,0,1),)),)),date='2026-10-20')
with patch('app.booking.live_status.get_live_booking_status',return_value=tomorrow):
 q='Is Aurora Live Fixture available tomorrow?';a=ask(q)
 check('future day without time asks material time slot',a.decision_artifact['need_results'][0]['status']=='needs_user_slot')
 h=[{'role':'user','text':q},{'role':'assistant','text':a.answer,'common_read_state':state_from_answer(a),'delivery_status':'server_written'}]
 b=ask('15:00',h)
 check('bare time preserves selected service and future date','15:00' in b.answer and 'available (' in b.answer,b.answer)
binding=store.get(binding['record_id'])['record'];binding['fields']['freshness_max_age_seconds']={'status':'unknown','value':None,'note':'No policy confirmed in this fixture','evidence_refs':[]}
save_owner_record(store,binding,binding['revision'],'isolated-live-test')
with patch('app.booking.live_status.get_live_booking_status',side_effect=AssertionError('No provider read without freshness policy')):
 a=ask();check('missing freshness policy remains unknown',a.decision_artifact['response_type']=='live_unavailable')
summary={'count':len(checks),'passed':sum(c['passed'] for c in checks),'failed':[c['case'] for c in checks if not c['passed']],'provider':'simulated aggregate only','real_booking_observed':False,'checks':checks}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(summary);sys.exit(bool(summary['failed']))
