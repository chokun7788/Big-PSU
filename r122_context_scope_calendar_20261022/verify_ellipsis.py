"""Execute the existing annotated compound questions with current sources."""
import json,os,sys
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r121_context_planner_training_20261022';S=R/'revision03_system'
os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview';sys.path.insert(0,str(S))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.understanding import parse
engine=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot())
jobs=[json.loads(s) for s in (OLD/'train.jsonl').read_text('utf8').splitlines()]
selected=[next(j for j in jobs if j['question'].startswith(p)) for p in ['What is the price of Cockpit and what games are available','How is VR for 30 minutes different from VR for 1 hour']]
out=[]
for j in selected:
 u=parse(json.dumps(j['label'],ensure_ascii=False),j['question']);assert u.accepted
 result=engine.answer(j['question'],j['locale'],at='2026-10-21T12:00:00+07:00',allow_llm=False,understanding=u)
 out.append({'key':j['key'],'question':j['question'],'result':result})
games=out[0]['result']['needs'][1];tasks=out[0]['result']['understanding']['tasks'];vr=out[1]['result']['understanding']['tasks']
checks={'elliptical_catalog_target_is_cockpit':tasks[1]['target'].casefold()=='cockpit','catalog_has_bound_source_claims':bool(games['claims']),'catalog_scope_contains_cockpit':all('cockpit' in json.dumps(c,ensure_ascii=False).casefold() for c in games['claims']),'vr_anaphor_preserved':vr[1]['target'].casefold()=='vr','vr_duration_not_leaked_to_booking':not any(c['slot']=='duration' for c in vr[1]['constraints'])}
(R/'ELLIPSIS_VERIFICATION.json').write_text(json.dumps({'checks':checks,'all_passed':all(checks.values()),'new_model_calls':0,'new_questions':0,'rows':out},ensure_ascii=False,indent=2),'utf8')
print(json.dumps(checks,ensure_ascii=False,indent=2));assert all(checks.values())
