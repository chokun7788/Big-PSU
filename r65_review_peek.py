import json,collections,sqlite3,zlib
from pathlib import Path
BASE=Path(__file__).resolve().parent;O=BASE/'r65_detailed_failure_analysis_20261014'
records=json.loads((O/'COMMON_RECORDS.json').read_text(encoding='utf-8'));samples=json.loads((O/'REVIEW_SAMPLES.json').read_text(encoding='utf-8'))
for s in samples:
 if s['arm']=='common_llm':
  plan=(s.get('artifact') or {}).get('query_plan') or {}
  print(json.dumps({'topic':s['topic'],'key':s['key'][:12],'q':s['question'],'answer':(s.get('answer') or '')[:550],'fields':plan.get('requested_fields'),'ids':plan.get('record_ids'),'errors':(s.get('artifact') or {}).get('coverage_errors'),'needs':plan.get('read_contract'),'expected':(s.get('grades') or [{}])[0].get('expected',{}).get('answer_contract')},ensure_ascii=False))
for s in samples:
 if 'General Adult' in s['question'] and s['arm']=='common_llm':
  ids=(s['artifact'].get('query_plan') or {}).get('record_ids') or []
  for rid in ids[:4]:
   rec=records[rid];print('PRICE RECORD',json.dumps(rec,ensure_ascii=False))
  break
for kind in ('competition_rule','control_set','rate','audience','schedule'):
 fs=collections.defaultdict(collections.Counter)
 for r in records.values():
  if r['kind']==kind:
   for f,v in r['fields'].items():fs[f][v['status']]+=1
 print('FIELDS',kind,json.dumps(dict(fs)))
print('RECORD_KEYS',list(next(iter(records.values()))))
