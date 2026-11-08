"""Replay actual R124 proposals through updated readers; no new model call.

This is an executor regression diagnostic, not a fresh end-to-end accuracy run.
Live is deliberately excluded: a saved proposal is not a saved occupancy oracle.
"""
import copy,json,os,sys,time
from pathlib import Path
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'revision03_system';sys.path.insert(0,str(S))
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PYTHONDONTWRITEBYTECODE='1')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.domain_flow.integration import answer
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.meaning_review import review
from app.knowledge.common.domain_flow.scope import reference_time
OUT=R/('executor_replay_'+str(time.time_ns()));OUT.mkdir();store=MigratedView(S/'data/knowledge/common.sqlite');reader=CommonAnswerer(store)
engine=Engine.from_snapshot(store.snapshot(),cache_key=store.path.resolve());seen=set();rows=[]
def forbidden(*args,**kwargs):raise AssertionError('Replay must not call model/provider')
deadline=time.monotonic()+3600
with (OUT/'RESULTS.jsonl').open('x',encoding='utf8') as output:
 while time.monotonic()<deadline:
  for line in (R/'candidate02/RESULTS.jsonl').read_text('utf8').splitlines():
   source=json.loads(line);key=source['key']
   if key in seen:continue
   seen.add(key);a=source.get('result',{}).get('decision_artifact') or {};saved=a.get('understanding')
   row={'key':key,'question':source['question'],'source_arm':'actual_candidate02_inference','model_calls':0,'provider_calls':0}
   if not saved:
    row['skipped']='no_saved_context_proposal'
   elif any(t.get('category')=='C12' for t in saved['tasks']):
    row['skipped']='live_observation_not_replayed'
   else:
    q=saved['event'].get('input_question',source['question']);u=Understanding([MeaningTask(**t) for t in saved['tasks']],saved['accepted'],saved['reason'],copy.deepcopy(saved['event']))
    u=review(q,engine.index,u)
    try:
     with patch('urllib.request.urlopen',forbidden),patch('app.booking.live_status.get_live_booking_status',forbidden):
      result=answer(reader,q,locale=source.get('locale','auto'),at=reference_time('2026-10-21T12:00:00+07:00'),planner=None,_understanding=u)
     row.update(answer=result.answer,artifact=result.decision_artifact,validation=result.validation.ok,proposal=saved,revised=u.as_dict())
    except Exception as exc:row['error']=repr(exc)
   rows.append(row);output.write(json.dumps(row,ensure_ascii=False,default=str)+'\n');output.flush()
  (OUT/'PROGRESS.json').write_text(json.dumps({'completed':len(rows),'expected':61,'model_calls':0,'provider_calls':0,'pid':os.getpid()},indent=2),'utf8')
  if (R/'candidate02/COMPLETE.json').exists() and len(rows)==61:break
  time.sleep(1)
summary={'complete':len(rows)==61,'rows':len(rows),'skipped':sum('skipped' in x for x in rows),'errors':sum('error' in x for x in rows),
 'mode':'saved actual context proposals, current reader execution; not new model inference','output':str(OUT)}
(OUT/'COMPLETE.json').write_text(json.dumps(summary,indent=2),'utf8');print(json.dumps(summary),flush=True)
