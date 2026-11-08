import json,collections
from pathlib import Path
R=Path(Path(__file__).with_name('r33_report_path.txt').read_text().strip())
grouped={}
for l in (R/'composed_H_NEW_FAILED.jsonl').open(encoding='utf-8'):
 x=json.loads(l);q=x['question'];z=x['result'];grouped.setdefault(q,dict(question=q,mode=z.get('mode'),answer=z.get('answer'),grades=[]))['grades'].append(dict(corpus=x['grade']['corpus'],id=x['grade']['id'],errors=x['grade']['failures']))
with (R/'NEW_FAILED_LEGACY_SOURCE_REVIEW.json').open('x',encoding='utf-8') as f:json.dump(list(grouped.values()),f,ensure_ascii=False,indent=2)
counts=collections.Counter()
for x in grouped.values():
 counts[x['mode']]+=len(x['grades'])
 if 'personal_peripheral' not in x['mode']:print(json.dumps(x,ensure_ascii=False))
print(json.dumps(counts,ensure_ascii=False))
