import json,re,time,concurrent.futures,hashlib
from pathlib import Path
import r33_full as runner
W=Path(__file__).parent;P=runner.full.P;R=Path((W/'r34_report_path.txt').read_text().strip());OLD=Path((W/'r33_report_path.txt').read_text().strip())
from app.pipeline.competition_targets import looks_like_competition_rule_query
def selected(q):
 return bool(re.search(r'[A-Za-z]',q) and (re.search(r'\b(?:and|also)\b',q,re.I) or q.count('?')+q.count('？')>=2)) and not looks_like_competition_rule_query(q)
def manifest():return {f.relative_to(P).as_posix():hashlib.sha256(f.read_bytes()).hexdigest() for f in (P/'app').rglob('*.py') if '__pycache__' not in f.parts}
if __name__=='__main__':
 before=manifest();jobs=[]
 for line in (OLD/'final_H_all_results.jsonl').open(encoding='utf-8'):
  x=json.loads(line)
  if not selected(x['question']):continue
  entries=[{k:v for k,v in g.items() if k in ('corpus','row_index','id','variant')}|{'case':g['expected']} for g in x['grades']]
  jobs.append(dict(key=x['key'],question=x['question'],locale=x['locale'],reference_date=x.get('reference_date',''),entries=entries))
 with (R/'FINAL_I_SCOPE.json').open('x',encoding='utf-8') as f:json.dump(dict(requests=len(jobs),grades=sum(len(j['entries']) for j in jobs),manifest=before,scope='Replay all non-competition questions with Latin and/also or multiple question marks across the full preserved 20327 corpus. I differs from H only in English compound operation classification and two tests. Other answers retain H/r33 provenance, not a fresh all-corpus I sweep.'),f,indent=2)
 print(dict(I_replay_requests=len(jobs)),flush=True)
 with (R/'FINAL_I_RESULTS.jsonl').open('x',encoding='utf-8') as out,concurrent.futures.ProcessPoolExecutor(max_workers=6) as pool:
  for n,x in enumerate(pool.map(runner.execute,jobs),1):
   out.write(json.dumps(x,ensure_ascii=False)+'\n');out.flush()
   if n%100==0:print(dict(completed=n),flush=True)
 assert manifest()==before
 print('I replay complete; runtime stable',flush=True)
