"""Resumable complete backend sweep with a wall watchdog around each request."""
import concurrent.futures,json,multiprocessing as mp,sys,time,faulthandler,collections
from pathlib import Path
import harness
B=Path(__file__).resolve().parent
def child(conn,mode,log):
 f=open(log,'a',encoding='utf-8');faulthandler.enable(file=f)
 try:
  harness.init(mode,False);conn.send({'ready':True})
  while True:
   job=conn.recv()
   if job is None:return
   print('BEGIN '+job['key']+' '+job['question'],file=f,flush=True)
   faulthandler.dump_traceback_later(12,file=f,repeat=True)
   result=harness.execute(job)
   faulthandler.cancel_dump_traceback_later();conn.send(result)
 finally:f.close();conn.close()
def start(mode,n):
 a,b=mp.Pipe();p=mp.Process(target=child,args=(b,mode,str(B/(mode+'_bounded_worker_'+str(n)+'.log'))));p.start();b.close()
 ready=False
 for _ in range(6):
  if a.poll(30):ready=True;break
  if not p.is_alive():break
 if not ready:p.terminate();p.join(10);a.close();raise RuntimeError('startup timeout after bounded 180s')
 a.recv();return p,a
def timeout(job):return {'key':job['key'],'question':job['question'],'requested_locale':job['locale'],'exception':'backend_wall_watchdog_20s','grades':[{'file':x['file'],'row':x['row'],'variant':x['variant'],'passed':False,'failures':['backend_wall_watchdog_20s'],'content_asserted':False,'content_checks_passed':None} for x in job['entries']]}
def main():
 mode=sys.argv[1];resumed='--resume' in sys.argv;tag=sys.argv[sys.argv.index('--tag')+1] if '--tag' in sys.argv else 'pruned' if resumed else '';out=B/(mode+'_bounded'+('_'+tag if tag else ''));out.mkdir(exist_ok=False);prior=[B/(mode+'_offline')/'RESULTS.jsonl',B/(mode+'_offline_resumed')/'RESULTS.jsonl']+([B/(mode+'_bounded')/'RESULTS.jsonl',B/(mode+'_bounded_pruned')/'RESULTS.jsonl'] if resumed else []);seen=set()
 prior += sorted(B.glob(mode+'_bounded_*/RESULTS.jsonl'))
 for path in prior:
  if path.exists():
   for line in path.open(encoding='utf-8'):
    try:seen.add(json.loads(line)['key'])
    except ValueError:pass
 jobs=[json.loads(line) for line in (B/'JOBS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()];jobs=[x for x in jobs if x['key'] not in seen]
 n=0;p,conn=start(mode,n);pool=concurrent.futures.ThreadPoolExecutor(max_workers=2);counts=collections.Counter();started=time.perf_counter()
 try:
  with (out/'RESULTS.jsonl').open('x',encoding='utf-8') as f:
   for done,job in enumerate(jobs,1):
    begin=time.perf_counter();future=pool.submit(conn.send,job)
    try:
     future.result(timeout=5);future=pool.submit(conn.recv);r=future.result(timeout=max(0,20-(time.perf_counter()-begin)))
    except (concurrent.futures.TimeoutError,EOFError,OSError):
     r=timeout(job);p.terminate();p.join(10);conn.close();pool.shutdown(wait=False,cancel_futures=True);pool=concurrent.futures.ThreadPoolExecutor(max_workers=2);n+=1;p,conn=start(mode,n)
    f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush()
    for g in r['grades']:counts['total']+=1;counts['passed']+=g['passed'];counts.update({'failure:'+v:1 for v in g['failures']})
    if done%100==0 or done==len(jobs):print(json.dumps({'completed_new':done,'previous':len(seen),'total_unique':done+len(seen),'remaining':len(jobs)-done,'elapsed':time.perf_counter()-started}),flush=True)
  (out/'SUMMARY.json').write_text(json.dumps({'new_requests':len(jobs),'previous_requests':len(seen),'counts':counts,'watchdog_sec':20,'no_answer_fabricated':True},ensure_ascii=False,indent=2),encoding='utf-8')
 finally:
  if p.is_alive():p.terminate();p.join(10)
  conn.close();pool.shutdown(wait=False,cancel_futures=True)
if __name__=='__main__':main()
