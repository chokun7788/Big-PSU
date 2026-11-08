"""Public CommonAnswerer delivery controls, including requested locale."""
import json,time
from datetime import datetime
from unittest.mock import patch
from verification_support import R,snapshot
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common import legacy_live_on_demand as bridge
from app.booking.live_status import LiveBookingSnapshot,LiveResource,LiveSlot
snap=snapshot();clock=datetime.fromisoformat('2026-10-27T10:00:00+07:00');checks={};rows=[]
class View:
 path=R/'system/data/knowledge/common.sqlite'
 def snapshot(self):return snap
 def still_current(self,s):return s is snap
def run(q,locale):
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected network')) as network:
  out=CommonAnswerer(View()).answer(q,locale=locale,at=clock,planner=None)
 rows.append({'question':q,'locale':locale,'answer':out.answer,'artifact':out.decision_artifact});return out,network
q='ที่อยู่ศูนย์คืออะไร ถ้ามาคนเดียว';out,network=run(q,'en');a=out.decision_artifact;c=a['execution_contract']
checks['unverified_condition_not_full_answer']=c['terminal_state']=='partial' and a['response_type']=='partial_answer' and c['verifier_result']['requires_partial_delivery']
checks['requested_english_notice_for_thai_question']='Application of these requested constraints remains unverified:' in out.answer
checks['requested_and_effective_locale_recorded']=c['dialogue_resolution']['requested_locale']=='en' and c['dialogue_resolution']['effective_locale']=='en'
checks['source_backed_answer_preserved_when_condition_unknown']=bool(a.get('domain_flow',{}).get('typed_claims')) and bool(c['executor_results'][0]['claims'])
checks['task_and_executor_keep_unverified_constraint_obligation']=c['tasks'][0]['terminal_state']=='partial' and any(o['kind']=='request_constraint' for o in c['executor_results'][0]['unresolved_obligations']) and not c['tasks'][0]['all_obligations_fulfilled'] and a['need_results'][0]['terminal_state']=='partial'
out,network=run('What is the studio address if I arrive alone?','th');checks['requested_thai_notice_for_english_question']='ยังยืนยันการใช้เงื่อนไขต่อไปนี้ในคำตอบไม่ได้:' in out.answer
catalog=json.loads((R.parent/'r124_legacy_guided_parity_20261023/LIVE_CONNECTION_PROBE.json').read_text('utf8'))['catalog'];name=next(r['name'] for r in catalog if r['id']=='15')
def fetch(day):return LiveBookingSnapshot(ok=True,date=day,now=clock.isoformat(),generated_at=clock.isoformat(),source='controlled_delivery_fixture',center_open=True,center_reason='controlled',open_periods=(('09:00','12:00'),),resources=(LiveResource('15',name,1,'available',1,(LiveSlot('09:00','12:00','available',0,0,1),)),))
with patch('app.booking.live_status.get_live_booking_status',fetch),patch.object(bridge,'freshness_now',lambda:clock):out,network=run('Is PC2 available on 2026-10-28 from 10:00-11:30?','en')
a=out.decision_artifact;c=a['execution_contract'];constraints=c['verifier_result']['constraint_coverage']['constraints']
checks['real_shared_runtime_date_window_verified']=bool(constraints) and all(x['status']=='structurally_supported' and x['proof'] for x in constraints)
checks['verified_temporal_conditions_do_not_create_false_partial']=c['terminal_state']=='supported' and a['response_type']=='answer' and 'remains unverified' not in out.answer
checks['no_unexpected_http']=not network.called
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_provider_calls':0,'user_data_changes':0};outdir=R/('request_delivery_'+str(time.time_ns()));outdir.mkdir();(outdir/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(outdir/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(outdir),**report}));assert report['all_passed']
