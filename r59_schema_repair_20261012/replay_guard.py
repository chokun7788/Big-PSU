"""Replay captured model proposals through updated guard, no new model call."""
import sys,json
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B.parent/'r58_examples_20sets_20261012'))
import experiment as t
from app.knowledge.common.planner import checked_plan,semantic_guard
records=t.CommonStore(t.DB).snapshot()['release']['records']
original={r['id']:r for r in map(json.loads,(t.B/'LLM_RESULTS.jsonl').read_text(encoding='utf-8').splitlines())}
rows=[]
for r in map(json.loads,(B/'llm_round4_guard/RESULTS.jsonl').read_text(encoding='utf-8').splitlines()):
    proposal=r['audit'][0]['proposal'];ids=[original[r['id']]['rid']]
    plan,note=semantic_guard(r['question'],checked_plan(proposal,ids,records),ids,records)
    expected=set(r['expected_fields']);actual=set(plan['requested_fields']) if plan else set()
    rows.append({**r,'plan':plan,'semantic_replay':note,'exact_fields_replay':actual==expected,'replay_not_new_llm_call':True})
(B/'REPLAY_GUARDED_48.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
summary={'captured_actual_model_proposals':len(rows),'raw_exact_fields':sum(r['raw_exact_fields'] for r in rows),'post_guard_exact_fields_replay':sum(r['exact_fields_replay'] for r in rows),'no_new_llm_calls':True,'semantic_guard_uses_no_gold':True}
(B/'REPLAY_GUARDED_48_SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(summary)
