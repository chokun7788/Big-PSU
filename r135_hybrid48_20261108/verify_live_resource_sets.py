"""Explicit same-family station sets must not collapse to the first station."""
import json,time,dataclasses
from datetime import datetime
from unittest.mock import patch
from verification_support import R,snapshot
from app.booking import live_status as live
from app.booking.live_status import LiveBookingSnapshot,LiveResource,LiveSlot
slots=(LiveSlot('09:00','12:00','available',0,0,1),)
snap=LiveBookingSnapshot(ok=True,date='2026-10-28',now='2026-10-27T10:00:00+07:00',generated_at='2026-10-27T10:00:00+07:00',source='controlled_resource_set',center_open=True,center_reason='controlled',open_periods=(('09:00','17:00'),),resources=tuple(LiveResource(str(n),'PC #'+str(n),1,'available',1,slots) for n in range(2,11)))
checks={};rows=[]
for text,expected in [('Is PC2 and PC3 available 10:00-11:00?',{'2','3'}),('PC #02 กับ PC #03 ว่าง 10:00-11:00 ไหม',{'2','3'}),('Is PC2 available 10:00-11:00?',{'2'}),('PC available 10:00-11:00?',{str(n) for n in range(2,11)}),('Is PC #03-#10 available right now',{str(n) for n in range(3,11)}),('PC #03–#05 ว่าง 10:00-11:00 ไหม',{'3','4','5'})]:
 got={r.resource_id for _,members in live._resource_groups_for_query(snap,text) for r in members};checks[text]=got==expected;rows.append({'question':text,'expected':sorted(expected),'actual':sorted(got)})
out=R/('live_resource_sets_'+str(time.time_ns()));out.mkdir()
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common import legacy_live_on_demand as bridge
source=snapshot();catalog=json.loads((R.parent/'r124_legacy_guided_parity_20261023/LIVE_CONNECTION_PROBE.json').read_text('utf8'))['catalog'];clock=datetime.fromisoformat('2026-10-27T10:00:00+07:00')
class View:
 path=out/'readonly-source.sqlite'
 def snapshot(self):return source
 def still_current(self,s):return s is source
for q,missing in [('Is PC #03-#10 available right now',False),('Is PC #03-#10 available right now',True),('Is PC #10-#03 available right now',False)]:
 calls=[]
 def fetch(day):
  calls.append(day);resources=tuple(LiveResource(r['id'],r['name'],1,'available',1,slots) for r in catalog if not missing or r['id']!='19')
  return LiveBookingSnapshot(ok=True,date=day,now=clock.isoformat(),generated_at=clock.isoformat(),source='controlled_original_range',center_open=True,center_reason='controlled',open_periods=(('09:00','17:00'),),resources=resources)
 with patch('app.booking.live_status.get_live_booking_status',fetch),patch.object(bridge,'freshness_now',lambda:clock):r=CommonAnswerer(View()).answer(q,locale='en',at=clock,planner=None)
 executor=r.decision_artifact['execution_contract']['executor_results'][0];rows.append({'question':q,'missing_pc6':missing,'answer':r.answer,'artifact':r.decision_artifact,'provider_reads':len(calls)})
 if '#10-#03' in q:checks['reversed_range_public_clarification_no_provider']=not calls and executor['status']=='missing_input'
 elif missing:checks['missing_middle_range_member_not_supported_subset']=executor['status']=='missing_source' and len(calls)==1 and not executor['receipts']
 else:
  checks['original_R123_range_has_all_eight_current_source_observations']={o['binding_id'] for o in executor['observation_receipts']}=={rid for rid,b in source['release']['records'].items() if b['kind']=='live_binding' and b['fields']['external_resource_key'].get('value') in {str(n) for n in range(16,24)}} and len(executor['observation_receipts'])==8 and executor['status']=='supported'
  checks['original_R123_range_single_provider_read']=len(calls)==1
report={'all_passed':all(checks.values()),'checks':checks,'actual_http_calls':0,'actual_model_inferences':0};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
