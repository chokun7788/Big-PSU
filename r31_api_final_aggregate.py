import json,collections
from pathlib import Path
r=Path(Path('r31_report_path.txt').read_text().strip());base={};current={}
def identity(x):return x['suite'],x['case']['id']
for line in (r/'api8091_B_http_results.jsonl').open(encoding='utf-8'):
    x=json.loads(line);key=identity(x);assert key not in base;base[key]=x
for line in (r/'api8091_C_http_results.jsonl').open(encoding='utf-8'):
    x=json.loads(line);key=identity(x);assert key in base and key not in current;assert x['case']==base[key]['case'];current[key]=x
counts=collections.defaultdict(collections.Counter)
with (r/'API_FINAL_B_C_RESULTS.jsonl').open('x',encoding='utf-8') as out:
    for key,b in base.items():
        x=current.get(key,b);x=dict(x,execution_provenance='C affected API replay' if key in current else 'B unchanged API case retained')
        counts[x['suite']]['total']+=1;counts[x['suite']]['passed']+=x['passed'];out.write(json.dumps(x,ensure_ascii=False)+'\n')
assert len(base)==941 and len(current)==482
data=dict(unique_case_grades=len(base),C_reexecuted=482,B_retained=459,by_suite=counts,all_passed=all(x['total']==x['passed'] for x in counts.values()),scope='941 unique API cases assembled from complete B run and C affected replay. C is not a new 941-request run. Strong content suites are distinct from target-only/locale/path cases; no real booking oracle.')
with (r/'API_FINAL_B_C_SUMMARY.json').open('x',encoding='utf-8') as out:json.dump(data,out,ensure_ascii=False,indent=2)
print(json.dumps(data,ensure_ascii=False),flush=True)
