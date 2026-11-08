import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent
arms={a:[json.loads(x) for x in (R/a/'RESULTS.jsonl').read_text('utf8').splitlines()] for a in (sys.argv[1:3] or ('teacher01','candidate01'))}
for old,new in zip(*arms.values()):
 print('\nQUESTION',old['question'])
 for label,row in [('OLD',old),('NEW',new)]:
  result=row.get('result',{})
  print(label,json.dumps({k:v for k,v in result.items() if k in ('answer','answer_text','status','error')},ensure_ascii=False)[:3800])
  if not any(k in result for k in ('answer','answer_text')):print('KEYS',list(result))
