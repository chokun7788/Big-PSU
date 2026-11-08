"""Actual on-demand common calls plus legacy renderer on identical observations."""
import dataclasses,json,os,sys,time,subprocess
from pathlib import Path
R=Path(__file__).resolve().parent
if '--teacher' in sys.argv:
 sys.path.insert(0,str(R/'teacher'))
 from app.booking.live_status import _snapshot_from_payload,render_live_booking_answer
 data=json.loads(Path(sys.argv[-1]).read_text('utf8'));snap=_snapshot_from_payload(data['snapshot'])
 print(json.dumps({'answer':render_live_booking_answer(data['question'],snap,data['locale']),'observable_flow':['resolve resource scope','requested time window','resource slot selection','render_live_booking_answer']},ensure_ascii=False));raise SystemExit()
S=R/'system';sys.path.insert(0,str(S));os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PSU_LIVE_BOOKING_FETCH_MODE='wordpress',PYTHONDONTWRITEBYTECODE='1')
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.booking import live_status
from app.knowledge.common.domain_flow.integration import answer
OUT=R/('live_probe_'+str(time.time_ns()));OUT.mkdir();rows=[]
original=live_status.get_live_booking_status
for i,q in enumerate(['PC2 ว่างไหม','ตอนนี้ PC กับ VR ว่างไหม','PS5 #1 ว่างไหม']):
 observed=[]
 def fetched(day):
  snap=original(day);observed.append(snap);return snap
 live_status.get_live_booking_status=fetched
 start=time.monotonic();result=answer(CommonAnswerer(MigratedView(S/'data/knowledge/common.sqlite')),q,locale='th',planner=None)
 assert result is not None
 row={'question':q,'answer':result.answer,'artifact':result.decision_artifact,'elapsed_sec':time.monotonic()-start,'actual_on_demand_provider_calls':len(observed)}
 if observed:
  fixture={'question':q,'locale':'th','snapshot':observed[0].as_public_dict()};p=OUT/(str(i)+'_AGGREGATE_OBSERVATION.json');p.write_text(json.dumps(fixture,ensure_ascii=False,indent=2),'utf8')
  child=subprocess.run([sys.executable,'-B',str(Path(__file__).resolve()),'--teacher',str(p)],capture_output=True,encoding='utf8',env={**os.environ,'PSU_COMMON_CHAT_PROFILE':''})
  if child.returncode:raise RuntimeError(child.stderr)
  row['legacy_same_observation']=json.loads(child.stdout);row['answer_matches_legacy_renderer']=row['answer']==row['legacy_same_observation']['answer']
 rows.append(row)
 print(json.dumps({'question':q,'provider_calls':len(observed),'status':result.decision_artifact.get('response_type'),'path':result.decision_artifact.get('execution_contract',{}).get('path'),'matches_legacy':row.get('answer_matches_legacy_renderer'),'answer':result.answer[:180]},ensure_ascii=False),flush=True)
(OUT/'RESULTS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8')
(OUT/'COMPLETE.json').write_text(json.dumps({'complete':True,'on_demand_called':all(r['actual_on_demand_provider_calls']==1 for r in rows),'same_observation_legacy_parity':all(r.get('answer_matches_legacy_renderer') for r in rows),'new_model_calls':0,'actual_live_provider':True,'production_installed':False},indent=2),'utf8')
print(OUT)
