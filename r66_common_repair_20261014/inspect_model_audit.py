import sys,json,collections
from pathlib import Path
B=Path(__file__).resolve().parent;tag=sys.argv[1];count=0
for line in (B/('MATRIX_'+tag+'.jsonl')).read_text(encoding='utf-8').splitlines():
 r=json.loads(line);result=r.get('result') or {}
 for t in result.get('trace',[]):
  if any(s in str(t.get('stage','')).lower() for s in ('llm','semantic','entity')) or 'transport_ok' in str(t):
   print(json.dumps({'question':r['question'],'trace':t},ensure_ascii=False));count+=1
   if count>=15:raise SystemExit
