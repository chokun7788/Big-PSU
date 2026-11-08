"""Guard/projection replay of frozen actual LLM proposals, not new model calls."""
import sys,json
from pathlib import Path
B=Path(__file__).resolve().parent
sys.path.insert(0,str(B.parent/'r58_examples_20sets_20261012'));import experiment as t
sys.path.insert(0,str(B.parent/'r60_generalization_20261012'));from evaluate import score
from app.knowledge.common.planner import FieldPlan,checked_plan,semantic_guard
from app.knowledge.common.answer import CommonAnswerer
source=B.parent/'r60_generalization_20261012/r61_dev_final/RESULTS.jsonl'
store=t.OneReleaseStore(t.DB).freeze();records=store.frozen['release']['records'];out=[]
for line in source.read_text(encoding='utf-8').splitlines():
 row=json.loads(line)
 def planner(q,recs,ids):
  audits=row.get('planner_audits',[])
  if not audits:return None
  old=audits[-1]
  clean,semantic=semantic_guard(q,checked_plan(old.get('proposal'),ids,recs),ids,recs)
  if clean is None:return None
  semantic['unclear_clauses']=old.get('semantic',{}).get('unclear_clauses',[])
  return FieldPlan(clean,semantic)
 ans=CommonAnswerer(store).answer(row['question'],locale=row['lang'],history=row['history'],at=t.AT,planner=planner)
 ok,why,quality=score(ans,row,records)
 out.append({**row,'passed':ok,'reasons':why,'quality':quality,'answer':ans.answer,'decision':ans.decision_artifact,'replayed_actual_proposal':True})
with (B/'GUARD_REPLAY.jsonl').open('x',encoding='utf-8') as f:
 for r in out:f.write(json.dumps(r,ensure_ascii=False)+'\n')
summary={'cases':len(out),'passed':sum(r['passed'] for r in out),'new_llm_calls':0,'proposal_origin':'actual LLM r61_dev_final','seen_regression':True,'exact_fields':sum(r['quality']['exact_required_fields'] for r in out),'extra_field_count':sum(len(r['quality']['extra_fields']) for r in out),'failed':[r['id'] for r in out if not r['passed']]}
with (B/'GUARD_REPLAY_SUMMARY.json').open('x',encoding='utf-8') as f:json.dump(summary,f,indent=2)
print(summary)
