import collections,json,zlib
from pathlib import Path
B=Path(__file__).resolve().parent
summary={}
for name in ['legacy_offline','common_offline']:
 p=B/name/'RESULTS.jsonl'
 if p.exists():
  rows=p.read_text(encoding='utf-8').splitlines();summary[name]={'written':len(rows),'last_question':json.loads(rows[-1]).get('question') if rows else None}
for name in ['legacy','common']:
 p=B/'model_matrix'/(name+'_RESULTS.jsonl.gz')
 if p.exists():
  try:
   raw=zlib.decompressobj(31).decompress(p.read_bytes()).decode('utf-8');rows=[]
   for line in raw.splitlines():
    try:rows.append(json.loads(line))
    except ValueError:pass
   summary[name+'_model']={'written':len(rows),'last_question':rows[-1].get('question') if rows else None,'last_seconds':rows[-1].get('elapsed_wall') if rows else None}
  except Exception as e:summary[name+'_model']={'reader_error':str(e)}
print(json.dumps(summary,ensure_ascii=False),flush=True)
