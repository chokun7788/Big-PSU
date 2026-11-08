import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent
for line in (R/sys.argv[1]/'RESULTS.jsonl').read_text('utf8').splitlines():
 r=json.loads(line)
 if not any(r['key'].startswith(k) for k in sys.argv[2:]):continue
 a=r.get('result',{}).get('decision_artifact') or {}
 print(json.dumps({'question':r['question'],'answer':r.get('result',{}).get('answer'),'understanding':a.get('understanding'),'live':a.get('live_booking')},ensure_ascii=False,indent=2))
