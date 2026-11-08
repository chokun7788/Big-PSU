import json,collections
from pathlib import Path
R=Path(Path(__file__).with_name('r33_report_path.txt').read_text().strip())
seen=set()
for line in (R/'full_D_NEW_FAILED.jsonl').open(encoding='utf-8'):
 x=json.loads(line);q=x['question']
 if q in seen or 'keyboard' in q.lower() or 'คีย์บอร์ด' in q:continue
 seen.add(q);print(json.dumps(dict(question=q,failures=x['grade']['failures'],answer=x['result']['answer'],mode=x['result']['mode']),ensure_ascii=False))
print('PAIRED REGRESSIONS')
for line in (R/'full_D_PAIRED.jsonl').open(encoding='utf-8'):
 x=json.loads(line)
 if x['v2']['regression']:print(json.dumps(x,ensure_ascii=False))
