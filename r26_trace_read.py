import json
from pathlib import Path
report=Path(Path(__file__).with_name('r25_report_path.txt').read_text(encoding='utf-8').strip())
rows=json.loads((report/'http_ready_8090.json').read_text(encoding='utf-8'))['cases']
for row in rows:
 if row['case'] not in ('th-rov-disconnect-prefix','th-settings-prefix','th-technical-communication'):continue
 response=row['response']
 print(json.dumps({'case':row['case'],'keys':list(response),'debug_keys':list(response.get('debug',{})),'elapsed_sec':row['elapsed_sec']},ensure_ascii=False))
 trace=response.get('trace') or response.get('debug',{}).get('trace') or []
 for item in trace:
  if item.get('stage') in ('universal_intent','intent_classifier','query_planner','semantic_route_refiner','timing','competition_source_contract','question_frame'):
   print(json.dumps(item,ensure_ascii=False))
