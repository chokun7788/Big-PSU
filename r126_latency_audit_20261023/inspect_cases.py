import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'));OUT=Path(c['output']);wanted=set(sys.argv[1:])
for line in (OUT/'HTTP_RESULTS.jsonl').read_text('utf8').splitlines():
 row=json.loads(line)
 if wanted and row['category'] not in wanted:continue
 response=row.get('response',{});art=response.get('decision_artifact',{})
 print(json.dumps({'case':row['category'],'q':row['question'],'answer':response.get('answer'),'understanding':art.get('understanding'),'need_results':[{k:n.get(k) for k in ['category','status','reason_codes','source_span','execution_query','execution_contract']} for n in art.get('need_results',[])],'query_plan':art.get('query_plan')},ensure_ascii=False))
