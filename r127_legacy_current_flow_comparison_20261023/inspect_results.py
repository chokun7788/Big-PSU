import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'))
for arm in ['legacy','current']:
 p=Path(c[arm]['output'])/'HTTP_RESULTS.jsonl'
 if not p.exists():continue
 rows=[json.loads(l) for l in p.read_text('utf8').splitlines()]
 for row in rows:
  if sys.argv[1:] and not any(s in row['key'] for s in sys.argv[1:]):continue
  b=row.get('response',{});art=b.get('decision_artifact',{})
  print(json.dumps({'arm':arm,'key':row['key'],'kind':row['kind'],'turn':row['turn'],'q':row['question'],'sec':row['wall_sec'],'answer':b.get('answer'),'mode':b.get('mode'),'resolution':b.get('context_resolution'),'resolved':b.get('resolved_question'),'read_state':b.get('common_read_state'),'understanding':art.get('understanding'),'error':row.get('error')},ensure_ascii=False))
