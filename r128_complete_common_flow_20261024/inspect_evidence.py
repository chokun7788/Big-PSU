import json
from pathlib import Path
R=Path(__file__).resolve().parent
c=json.loads((R/'BROAD_PROCESS.json').read_text('utf8'));p=Path(c['output'])/'RESULTS.jsonl'
for l in p.read_text('utf8').splitlines():
 r=json.loads(l);a=r.get('response',{});artifact=a.get('debug',{}).get('decision_artifact',{})
 print(json.dumps({'i':r['i'],'key':r['key'][:8],'q':r['question'],'answer':a.get('answer',''),'sec':round(r['wall_sec'],2),'error':r.get('error')},ensure_ascii=False))
