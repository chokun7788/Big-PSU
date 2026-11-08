import json
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;seen={}
paths=[ROOT/'r121_context_planner_training_20261022/API_SELECTED_JOBS.jsonl',ROOT/'r120_teacher_distillation_20261022/DEVELOPMENT_JOBS.jsonl',ROOT/'r121_context_planner_training_20261022/GUARD_SELECTED_JOBS.jsonl',ROOT/'r121_context_planner_training_20261022/PRIORITY_SELECTED_JOBS.jsonl']
for path in paths:
 for line in path.read_text('utf8').splitlines():
  row=json.loads(line);seen.setdefault(row['key'],row)
rows=list(seen.values());pilot=rows[:8]
# Include actual calendar, controls and tournament failures from the retained
# pool instead of inventing another benchmark.
for domain in ['schedule','game_controls','competition_rules','rental']:
 match=next((x for x in rows[8:] if any(e['case'].get('domain')==domain or domain in e['case'].get('expected_route_categories',[]) for e in x.get('entries',[]))),None)
 if match and match not in pilot:pilot.append(match)
for name,data in [('ALL_RETAINED_JOBS.jsonl',rows),('PILOT_JOBS.jsonl',pilot)]:
 (R/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in data),'utf8')
print(json.dumps({'all_retained_keys':len(rows),'pilot_keys':len(pilot),'new_questions':0}))
