"""Parent R122 reader replay with saved proposals; no legacy baseline inference."""
import json,os,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;OLD=ROOT/'r122_context_scope_calendar_20261022';T=ROOT/'r121_context_planner_training_20261022';S=OLD/'revision04_system'
os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview';sys.path.insert(0,str(S))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.understanding import parse
from app.knowledge.common.domain_flow.meaning_review import review
engine=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot())
def rows(p):return [json.loads(s) for s in p.read_text('utf8').splitlines()]
inputs=[]
for g,p in zip(rows(T/'test.jsonl'),rows(T/'train02/trained_test.jsonl')):
 assert g['key']==p['key'];inputs.append((g['key'],g['question'],g['locale'],p['raw_output']))
for row in rows(OLD/'api02/trained/RESULTS.jsonl')+rows(OLD/'ellipsis01/trained/RESULTS.jsonl'):
 u=row['response']['decision_artifact']['understanding'];inputs.append((row['key'],u['event']['input_question'],row['locale'],u['event']['raw_content']))
out=[]
for key,q,loc,raw in inputs:
 u=parse(raw,q);u.event['raw_content']=raw;u=review(q,engine.index,u)
 result=engine.answer(q,loc,at='2026-10-21T12:00:00+07:00',allow_llm=False,understanding=u)
 out.append({'key':key,'question':q,'result':result})
target=R/('PARENT_REPLAY_'+str(time.time_ns())+'.json');target.write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'parent':'R122 revision04','saved_proposals_replayed':len(out),'new_model_inferences':0,'output':str(target)}),flush=True)
