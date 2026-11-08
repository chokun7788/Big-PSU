import json
from pathlib import Path
R=Path(__file__).resolve().parent
failed=[x for x in map(json.loads,(R/'regression03/RESULTS.jsonl').open(encoding='utf8')) if x.get('error') or not x['result']['answer']]
keys={x['key'] for x in failed};jobs=[j for j in map(json.loads,(R/'DEVELOPMENT_JOBS.jsonl').open(encoding='utf8')) if j['key'] in keys]
assert len(jobs)==len(keys)==1
(R/'RETRY_JOBS.jsonl').write_text(''.join(json.dumps(j,ensure_ascii=False)+'\n' for j in jobs),'utf8')
m=json.loads((R/'DEV_MANIFEST.json').read_text('utf8'));m.update(requests=len(jobs),grades=sum(len(j['entries']) for j in jobs),retry_reason='original API TimeoutError; original output retained')
(R/'RETRY_MANIFEST.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),'utf8')
s=(R/'run_regression03.py').read_text('utf8').replace("OUT=R/'regression03'","OUT=R/'transport_retry01'").replace('DEVELOPMENT_JOBS.jsonl','RETRY_JOBS.jsonl').replace('DEV_MANIFEST.json','RETRY_MANIFEST.json').replace("'run_regression03.py']","'run_regression03.py','run_transport_retry.py']")
(R/'run_transport_retry.py').write_text(s,'utf8')
print('Prepared retry of original failed request only; no replacement of prior results.')
