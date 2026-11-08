import json,collections,sys
from pathlib import Path
ROOT=Path(__file__).parent;R=Path((ROOT/'r33_report_path.txt').read_text().strip());OLD=Path((ROOT/'r32_report_path.txt').read_text().strip())
def identity(g):return g['corpus'],g['id'],g['variant'],g['row_index']
base={}
for l in (OLD/'final13_all_results.jsonl').open(encoding='utf-8'):
    x=json.loads(l);base[x['key']]={identity(g):g['passed'] for g in x['grades']}
new=[];counts=collections.Counter();pairs=[]
for l in (R/'candidate_D_all_results.jsonl').open(encoding='utf-8'):
    try:x=json.loads(l)
    except json.JSONDecodeError:break
    counts['requests']+=1
    for g in x['grades']:
        counts['grades']+=1;counts['passed']+=g['passed']
        if base[x['key']][identity(g)] and not g['passed']:
            new.append(dict(question=x['question'],locale=x['locale'],answer=x.get('result',{}).get('answer'),mode=x.get('result',{}).get('mode'),grade=g))
        counts['improved']+=not base[x['key']][identity(g)] and g['passed']
summary=dict(counts=counts,new_failed_grades=len(new),new_failure_types=collections.Counter(e for x in new for e in x['grade']['failures']))
with (R/(sys.argv[1]+'_interim_new_failures.json')).open('x',encoding='utf-8') as out:json.dump(dict(summary=summary,rows=new),out,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False))
for x in new[:12]:print(json.dumps(dict(question=x['question'],mode=x['mode'],failures=x['grade']['failures'],answer=(x['answer'] or '')[:230]),ensure_ascii=False))
