import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent
rows=[json.loads(s) for s in (R/sys.argv[1]/'RESULTS.jsonl').read_text('utf8').splitlines()]
for row in rows:
 if len(sys.argv)>2 and not any(row['key'].startswith(k) for k in sys.argv[2:]):continue
 result=row.get('result',{});art=result.get('decision_artifact') or {}
 print(json.dumps({'key':row['key'][:8],'question':row['question'],'answer':result.get('answer'),
  'understanding':art.get('understanding'), 'needs':art.get('need_results'),'plan':art.get('query_plan')},ensure_ascii=False)[:22000])
