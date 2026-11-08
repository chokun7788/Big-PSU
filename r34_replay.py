import json,re,time,concurrent.futures,hashlib,sys
from pathlib import Path
import r33_full as runner
W=Path(__file__).parent;P=runner.full.P
R=Path((W/'r34_report_path.txt').read_text().strip());OLD=Path((W/'r33_report_path.txt').read_text().strip())
def manifest():
 return {f.relative_to(P).as_posix():hashlib.sha256(f.read_bytes()).hexdigest() for f in (P/'app').rglob('*.py') if '__pycache__' not in f.parts}
def selected(x):
 return any(g['corpus']=='master_gt_bilingual_multi_error_2000_20260929_r15.jsonl' for g in x['grades']) or bool(re.search(r'แพง|ถูกกว่า|ค่าบริการ|ชำร|จ่าย|โอน|คำพู|ดูหมิ่น|เสียดสี|อ้างอิงติกา|จำนวย|\b(?:pay\w*|payment|transfer|expens\w*|cheaper|compare|insult\w*|mock\w*|offensive|speech)\b',x['question'],re.I))
if __name__=='__main__':
 prefix=sys.argv[1] if len(sys.argv)>1 else 'LARGE_REPLAY'
 before=manifest();jobs=[]
 for line in (OLD/'final_H_all_results.jsonl').open(encoding='utf-8'):
  x=json.loads(line)
  if not selected(x):continue
  entries=[{k:v for k,v in g.items() if k in ('corpus','row_index','id','variant')}|{'case':g['expected']} for g in x['grades']]
  jobs.append(dict(key=x['key'],question=x['question'],locale=x['locale'],reference_date=x.get('reference_date',''),entries=entries))
 with (R/(prefix+'_SCOPE.json')).open('x',encoding='utf-8') as f:json.dump(dict(requests=len(jobs),grades=sum(len(j['entries']) for j in jobs),manifest=before,scope='Fresh r34 pipeline: all 2000 bilingual clean/noisy pairs plus affected price/payment/speech and typo competition references from preserved r33 composite. LLM/semantic off; live booking mocked unavailable. Not a fresh sweep of all 20327 questions.'),f,indent=2)
 print(dict(requests=len(jobs)),flush=True);start=time.perf_counter()
 with (R/(prefix+'_RESULTS.jsonl')).open('x',encoding='utf-8') as out,concurrent.futures.ProcessPoolExecutor(max_workers=6) as pool:
  futures=[pool.submit(runner.execute,j) for j in jobs]
  for i,f in enumerate(concurrent.futures.as_completed(futures),1):
   out.write(json.dumps(f.result(),ensure_ascii=False)+'\n');out.flush()
   if i%200==0:print(dict(completed=i,remaining=len(jobs)-i,elapsed=round(time.perf_counter()-start)),flush=True)
 assert manifest()==before,'Runtime changed during replay'
 with (R/(prefix+'_EXECUTION.json')).open('x',encoding='utf-8') as f:json.dump(dict(requests=len(jobs),elapsed=time.perf_counter()-start,runtime_unchanged=True),f,indent=2)
 print('Large replay completed with stable runtime',flush=True)


