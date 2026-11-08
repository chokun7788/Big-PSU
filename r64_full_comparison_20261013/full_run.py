import collections,concurrent.futures,json,sys,time
from pathlib import Path
import harness
B=Path(__file__).resolve().parent
def main():
 mode=sys.argv[1];llm=sys.argv[2]=='llm';tag=mode+'_'+sys.argv[2]+('_resumed' if '--resume' in sys.argv else '');out=B/tag;out.mkdir(exist_ok=False)
 jobs=[json.loads(x) for x in (B/'JOBS.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
 workers=int(sys.argv[sys.argv.index('--workers')+1]) if '--workers' in sys.argv else 1 if llm else 3
 if '--resume' in sys.argv:
  path=Path(sys.argv[sys.argv.index('--resume')+1]);seen=set()
  for line in path.open(encoding='utf-8'):
   try:seen.add(json.loads(line)['key'])
   except ValueError:pass
  jobs=[job for job in jobs if job['key'] not in seen]
 if '--limit' in sys.argv:jobs=jobs[:int(sys.argv[sys.argv.index('--limit')+1])]
 counts=collections.defaultdict(collections.Counter);failures=collections.Counter();modes=collections.Counter();language=collections.Counter();start=time.perf_counter()
 print(json.dumps({'mode':mode,'llm':llm,'jobs':len(jobs),'workers':workers}),flush=True)
 with (out/'RESULTS.jsonl').open('x',encoding='utf-8') as f,concurrent.futures.ProcessPoolExecutor(max_workers=workers,initializer=harness.init,initargs=(mode,llm)) as pool:
  for n,r in enumerate(pool.map(harness.execute,jobs,chunksize=4 if llm else 12),1):
   f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush();language[r.get('effective_locale',r['requested_locale'])]+=1;modes[r.get('result',{}).get('mode','exception')]+=1
   for g in r['grades']:
    c=counts[g['file']];c['total']+=1;c['passed']+=g['passed'];c['content_asserted']+=g.get('content_asserted',False);c['content_passed']+=g.get('content_checks_passed') is True;c['protocol_failed']+=bool(g.get('protocol_failures'));failures.update(g['failures'])
   if n%100==0 or n==len(jobs):print(json.dumps({'completed':n,'total':len(jobs),'elapsed_sec':round(time.perf_counter()-start,1),'grades':sum(c['total'] for c in counts.values()),'passed':sum(c['passed'] for c in counts.values())}),flush=True)
 summary={'unique_requests':len(jobs),'elapsed_sec':time.perf_counter()-start,'by_corpus':dict(counts),'failure_counts':failures,'modes':modes,'languages':language,'model_enabled':llm,'draft_only':mode=='common','resumed_from':str(path) if '--resume' in sys.argv else None,'scope':'all deduplicated existing questions; route/mode contracts retained separately from content; live unavailable fixture; backend without worker watchdog'}
 (out/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print('FINISHED '+json.dumps({'unique_requests':len(jobs),'elapsed':summary['elapsed_sec']}),flush=True)
if __name__=='__main__':main()
