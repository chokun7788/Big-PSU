"""Live bridge fault checks, using controlled aggregate payloads, no network."""
import copy,dataclasses,hashlib,json,os,sys,time
from pathlib import Path
from datetime import datetime,timedelta
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'revision04_system';sys.path.insert(0,str(S))
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PYTHONDONTWRITEBYTECODE='1')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.integration import answer
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.registry import value
from app.booking.live_status import LiveBookingSnapshot,LiveResource,LiveSlot
from app.knowledge.common import legacy_live_on_demand as bridge
OUT=R/('live_verification_'+str(time.time_ns()));OUT.mkdir();checks={};outputs=[]
snap=MigratedView(S/'data/knowledge/common.sqlite').snapshot();records=snap['release']['records']
clock=datetime.fromisoformat('2026-10-27T10:00:00+07:00');catalog=json.loads((R/'LIVE_CONNECTION_PROBE.json').read_text('utf8'))['catalog']
class MemoryView:
 path=S/'data/knowledge/common.sqlite'
 def __init__(self,s):self.data=s
 def snapshot(self):return self.data
 def still_current(self,s):return self.data is s
def fixture(day,**changes):
 resources=tuple(LiveResource(r['id'],r['name'],5 if 'VR ' in r['name'] else 1,'available',1,
  (LiveSlot('09:00','12:00','available',0,0,1),LiveSlot('13:00','16:00','available',0,0,1))) for r in catalog)
 data=dict(ok=True,date=day,now=clock.isoformat(),generated_at=clock.isoformat(),source='controlled_aggregate_fixture',center_open=True,
  center_reason='fixture',open_periods=(('09:00','12:00'),('13:00','16:00')),resources=resources)
 data.update(changes);return LiveBookingSnapshot(**data)
def run(q='PC2 ว่างไหม',*,transform=lambda s:s,snapshot=None,reference=None):
 calls=[]
 def fetch(day):calls.append(day);return transform(fixture(day))
 with patch('app.booking.live_status.get_live_booking_status',fetch),patch.object(bridge,'freshness_now',lambda:clock):
  u=Understanding([MeaningTask(q,'live','C12','availability','live_status')],True,'controlled_live_intent',{})
  result=answer(CommonAnswerer(MemoryView(snapshot or snap)),q,locale='th',at=reference or clock,planner=None,_understanding=u)
 assert result is not None
 art=result.decision_artifact;row={'question':q,'answer':result.answer,'artifact':art,'calls':calls,'controlled_fixture':True};outputs.append(row)
 return result,art,calls
def state(art):return art['execution_contract']['tasks'][0]['terminal_state']
result,art,calls=run();checks['narrow_pc2_uses_one_call']=len(calls)==1
checks['narrow_pc2_selects_only_provider_id_15']=art['query_plan']['selected_external_resource_ids']==['15']
checks['fresh_payload_supported']=state(art)=='supported'
_,art,_=run(transform=lambda s:dataclasses.replace(s,generated_at=clock.replace(tzinfo=None).isoformat()))
checks['declared_bangkok_naive_timestamp_supported']=state(art)=='supported'
_,art,_=run(reference=clock-timedelta(days=6));checks['freshness_independent_of_semantic_booking_date']=state(art)=='supported'
for label,change in [('stale',{'generated_at':(clock-timedelta(seconds=60)).isoformat()}),('future',{'generated_at':(clock+timedelta(seconds=60)).isoformat()}),('wrong_date',{'date':'2000-01-01'}),('transport_failure',{'ok':False,'error_code':'timeout'})]:
 _,art,_=run(transform=lambda s,c=change:dataclasses.replace(s,**c));checks[label+'_never_supported']=state(art)!='supported'
checks['failed_provider_is_not_model_transport_failure']=not any(o.get('model_transport_failure') for o in outputs[-1]['artifact'].get('need_results',[]))
def unknown_status(s):
 return dataclasses.replace(s,resources=tuple(dataclasses.replace(r,status='provider_new_status') if r.resource_id=='15' else r for r in s.resources))
_,art,_=run(transform=unknown_status);checks['unmapped_status_is_source_mapping_gap']=state(art)=='missing_source' and art['live_booking']['provider_payload_ok']
_,art,calls=run('PC99 ว่างไหม');checks['unknown_exact_station_does_not_fetch']=not calls and state(art)=='missing_source'
missing=copy.deepcopy(snap);missing['active']='missing-binding';missing['epoch']+=10000
missing['release']['records']={k:r for k,r in missing['release']['records'].items() if r['kind']!='live_binding'}
_,art,calls=run(snapshot=missing);checks['missing_bindings_do_not_fetch_or_claim_transport_failure']=not calls and state(art)=='missing_source'
_,art,calls=run('PC กับ VR ว่างไหม');checks['multi_group_one_request_snapshot']=len(calls)==1 and len(art['query_plan']['selected_external_resource_ids'])>1
gap=LiveSlot('10:30','11:00','busy',1,0,0)
def gap_range(s):
 return dataclasses.replace(s,resources=tuple(dataclasses.replace(r,slots=(LiveSlot('09:00','10:30','available',0,0,1),gap,LiveSlot('11:00','12:00','available',0,0,1))) if r.resource_id=='15' else r for r in s.resources))
result,art,_=run('PC2 ว่าง 10:00-11:30 ไหม',transform=gap_range)
checks['range_uses_legacy_contiguous_slot_decision']='ไม่ว่างตลอดช่วง 10:00-11:30' in result.answer
checks['all_native_contracts_present']=all(r['artifact'].get('execution_contract') for r in outputs)
summary={'all_passed':all(checks.values()),'checks':checks,'cases':len(outputs),'actual_provider_calls':0,'model_calls':0,'production_installed':False}
(OUT/'RESULTS.json').write_text(json.dumps(outputs,ensure_ascii=False,indent=2),'utf8');(OUT/'VERIFICATION.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'output':str(OUT),**summary},ensure_ascii=False,indent=2));assert summary['all_passed']
