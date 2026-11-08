"""Existing training questions expose false positives; no new questions."""
import json,os,sys
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r121_context_planner_training_20261022';S=R/'revision03_system'
os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview';sys.path.insert(0,str(S))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.understanding import parse
from app.knowledge.common.domain_flow.context_guard import apply
index=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot()).index
prefixes=['Could you please help me with this: Is it open on Sundays','Write one polite promotional sentence for the event.','Can outsiders come in and use the equipment?','Can a tourist use the studio','Can I carry a water bottle inside?','How is VR for 30 minutes different from VR for 1 hour']
jobs=[json.loads(s) for s in (OLD/'train.jsonl').read_text('utf8').splitlines()];rows=[]
for prefix in prefixes:
 j=next(j for j in jobs if j['question'].startswith(prefix))
 u=parse(json.dumps(j['label'],ensure_ascii=False),j['question']);assert u.accepted
 u=apply(j['question'],index,u)
 rows.append({'key':j['key'],'question':j['question'],'no_new_ambiguity':all(t.ambiguous==j['label']['tasks'][i]['ambiguous'] for i,t in enumerate(u.tasks)),'tasks':[t.as_dict() for t in u.tasks]})
(R/'CONTEXT_REGRESSION_VERIFICATION03.json').write_text(json.dumps({'all_passed':all(r['no_new_ambiguity'] for r in rows),'existing_questions':len(rows),'new_model_calls':0,'rows':rows},ensure_ascii=False,indent=2),'utf8')
print(json.dumps([{k:r[k] for k in ['question','no_new_ambiguity']} for r in rows],ensure_ascii=False,indent=2));assert all(r['no_new_ambiguity'] for r in rows)
