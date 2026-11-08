"""Full paired model-enabled evaluation, serial GPU work, per-request watchdog."""
import collections,gzip,json,multiprocessing as mp,sys,time,traceback,zlib
from pathlib import Path
import harness
B=Path(__file__).resolve().parent
def worker(conn,mode):
 try:
  harness.init(mode,True);conn.send({'event':'ready'})
  while True:
   job=conn.recv()
   if job is None:return
   conn.send({'event':'result','result':harness.execute(job)})
 except BaseException as e:
  try:conn.send({'event':'worker_error','error':repr(e),'trace':traceback.format_exc()})
  except (OSError,BrokenPipeError):pass
 finally:conn.close()
def start(mode):
 a,b=mp.Pipe();p=mp.Process(target=worker,args=(b,mode),daemon=False);p.start();b.close()
 ready=False
 for _ in range(6):
  if a.poll(30):ready=True;break
  if not p.is_alive():break
 if not ready:p.terminate();p.join(10);a.close();raise RuntimeError('Worker startup timeout '+mode)
 event=a.recv()
 if event['event']!='ready':raise RuntimeError(str(event))
 return p,a
def failed(job,reason):return {'key':job['key'],'question':job['question'],'requested_locale':job['locale'],'exception':reason,'grades':[{'file':x['file'],'row':x['row'],'variant':x['variant'],'passed':False,'failures':[reason],'content_asserted':False,'content_checks_passed':None} for x in job['entries']]}
def main():
 resume='--resume' in sys.argv
 tag=sys.argv[sys.argv.index('--tag')+1] if '--tag' in sys.argv else 'pruned' if resume else ''
 root=B/('model_matrix_'+tag if tag else 'model_matrix');root.mkdir(exist_ok=False);jobs=[json.loads(x) for x in (B/'JOBS.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
 seen={mode:set() for mode in ['legacy','common']}
 if resume:
  for mode in seen:
   for previous in [B/'model_matrix']+sorted(B.glob('model_matrix_*')):
    if not previous.is_dir() or previous==root:continue
    p=previous/(mode+'_RESULTS.jsonl.gz')
    if not p.exists():continue
    from analyze import read
    for row in read(p):seen[mode].add(row['key'])
  jobs=[job for job in jobs if not all(job['key'] in seen[mode] for mode in seen)]
 if '--limit' in sys.argv:jobs=jobs[:int(sys.argv[sys.argv.index('--limit')+1])]
 state={};files={};counts={mode:collections.defaultdict(collections.Counter) for mode in ['legacy','common']};failures={mode:collections.Counter() for mode in counts};languages={mode:collections.Counter() for mode in counts};modes={mode:collections.Counter() for mode in counts};started=time.perf_counter()
 try:
  for mode in counts:state[mode]=start(mode);files[mode]=gzip.open(root/(mode+'_RESULTS.jsonl.gz'),'xt',encoding='utf-8')
  print(json.dumps({'requests_per_format':len(jobs),'LLM_enabled':True,'serial_model_work':True,'watchdog_sec':30}),flush=True)
  for n,job in enumerate(jobs,1):
   for mode in counts:
    if job['key'] in seen[mode]:continue
    p,conn=state[mode];conn.send(job)
    if conn.poll(30):
     event=conn.recv();r=event['result'] if event['event']=='result' else failed(job,'worker_error:'+event.get('error','unknown'))
    else:
     r=failed(job,'harness_timeout_30s');p.terminate();p.join(10);conn.close();state[mode]=start(mode)
    files[mode].write(json.dumps(r,ensure_ascii=False)+'\n');files[mode].flush();languages[mode][r.get('effective_locale',r['requested_locale'])]+=1;modes[mode][r.get('result',{}).get('mode','exception')]+=1
    for g in r['grades']:
     c=counts[mode][g['file']];c['total']+=1;c['passed']+=g['passed'];c['content_asserted']+=g.get('content_asserted',False);c['content_passed']+=g.get('content_checks_passed') is True;failures[mode].update(g['failures'])
   if n%100==0 or n==len(jobs):
    progress={'completed_pairs':n,'total_pairs':len(jobs),'elapsed_sec':round(time.perf_counter()-started,1),'passed':{mode:sum(c['passed'] for c in counts[mode].values()) for mode in counts}}
    (root/'PROGRESS.json').write_text(json.dumps(progress),encoding='utf-8');print(json.dumps(progress),flush=True)
  summary={'requests_per_format':len(jobs),'previous_requests':{mode:len(seen[mode]) for mode in seen},'elapsed_sec':time.perf_counter()-started,'by_format':{mode:{'by_corpus':dict(counts[mode]),'failure_counts':failures[mode],'languages':languages[mode],'modes':modes[mode]} for mode in counts},'LLM_enabled':True,'embedding_enabled':True,'common_is_readonly_draft_view':True,'actual_bookings':'controlled unavailable; known occupancy covered by fixture tests','not_a_load_benchmark':True,'evaluation_pruning':True,'production_latency_certified':False}
  (root/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print('FINISHED',flush=True)
 finally:
  for f in files.values():f.close()
  for p,conn in state.values():
   if p.is_alive():
    try:conn.send(None)
    except OSError:pass
    p.join(5)
   if p.is_alive():p.terminate();p.join(10)
   conn.close()
if __name__=='__main__':main()
