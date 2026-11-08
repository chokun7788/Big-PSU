import json,re,time
from pathlib import Path
import r33_full as runner
R=Path(Path(__file__).with_name('r33_report_path.txt').read_text().strip())
start=time.perf_counter();replaced={};jobs=[]
for line in (R/'final_G_all_results.jsonl').open(encoding='utf-8'):
 x=json.loads(line);q=x['question']
 if not ((re.search(r'อีเมล|\be-?mail\b',q,re.I) and re.search(r'เบอร์|โทร|\b(?:phone|telephone|tel)\b',q,re.I)) or 'KeyError' in x.get('exception','')):continue
 entries=[{k:v for k,v in g.items() if k in ('corpus','row_index','id','variant')}|{'case':g['expected']} for g in x['grades']]
 jobs.append(dict(key=x['key'],question=q,locale=x['locale'],reference_date=x.get('reference_date',''),entries=entries))
with (R/'final_H_replay_results.jsonl').open('x',encoding='utf-8') as out:
 for job in jobs:
  x=runner.execute(job);x['runtime_generation']='final_H';replaced[x['key']]=x;out.write(json.dumps(x,ensure_ascii=False)+'\n');out.flush()
with (R/'final_H_all_results.jsonl').open('x',encoding='utf-8') as out:
 for line in (R/'final_G_all_results.jsonl').open(encoding='utf-8'):
  x=json.loads(line);out.write(json.dumps(replaced.get(x['key'],x),ensure_ascii=False)+'\n')
with (R/'final_H_replay_scope.json').open('x',encoding='utf-8') as out:json.dump(dict(requests=len(jobs),elapsed=time.perf_counter()-start,scope='Only final G to H difference is skipping metadata rows without id in Thai compound contact lookup. Replay all email+phone queries and all G KeyError exceptions. Other records retain D/G provenance.'),out,indent=2)
print(dict(contact_replays=len(jobs),elapsed=time.perf_counter()-start))
