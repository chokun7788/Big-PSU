import sys,os,json,time,subprocess,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B),str(B/'system')]
def worker(tag,llm):
 from harness import init,execute
 os.environ.update(PSU_ESPORTS_NOW='2026-10-14T12:00:00+07:00',PYTHONPATH=str(B/'system'))
 init('common',llm)
 jobs=[json.loads(x) for x in (B/'COMMON_STRATIFIED_JOBS.jsonl').read_text(encoding='utf-8').splitlines()]
 out=B/('MATRIX_'+tag+'.jsonl');done=set()
 if out.exists():done={json.loads(x)['key'] for x in out.read_text(encoding='utf-8').splitlines() if x.strip()}
 start=time.perf_counter()
 for i,job in enumerate(jobs,1):
  if job['key'] in done:continue
  result=execute(job)
  # Additional semantic partitions; original grader failures remain unchanged.
  for g in result['grades']:
   reasons=g.get('failures',[])
   g['r66_partitions']={k:[] for k in ('protocol','performance','content_source_validation')}
   for reason in reasons:
    bucket='protocol' if reason.startswith(('route:','intent:','legacy_mode_prefix:','status:','forbidden_category','route expected','outcome expected','outcome ')) else 'performance' if 'latency' in reason or 'timeout' in reason else 'content_source_validation'
    g['r66_partitions'][bucket].append(reason)
  result['r66_config']={'format':'common','llm_enabled':llm,'clock':'2026-10-14T12:00:00+07:00','booking_oracle':'controlled_unavailable','draft_evaluation_only':True,'harness_sha256':hashlib.sha256((B/'harness.py').read_bytes()).hexdigest()}
  with out.open('a',encoding='utf-8') as f:f.write(json.dumps(result,ensure_ascii=False)+'\n')
  status={'arm':tag,'completed':i,'total':len(jobs),'elapsed':time.perf_counter()-start,'last_question':job['question'],'last_exception':result.get('exception'),'running':True}
  (B/('STATUS_'+tag+'.json')).write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding='utf-8')
  if i%10==0:print(json.dumps(status,ensure_ascii=False),flush=True)
 status['running']=False;(B/('STATUS_'+tag+'.json')).write_text(json.dumps(status,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(status,ensure_ascii=False),flush=True)
if __name__=='__main__':
 if len(sys.argv)>1:worker(sys.argv[1],sys.argv[2]=='1')
 else:
  # Serialize real model work; never run a legacy arm or overlap LLM arms.
  for tag,llm in [('offline_01',False),('llm_01',True)]:
   with (B/('matrix_'+tag+'.log')).open('x',encoding='utf-8') as log:
    subprocess.run([sys.executable,'-B',str(Path(__file__).resolve()),tag,'1' if llm else '0'],cwd=B,stdout=log,stderr=subprocess.STDOUT,check=True)
  (B/'MATRIX_COMPLETE_01.json').write_text(json.dumps({'arms':['common_offline','common_llm'],'full_20554_sweep':False,'complete':True}),encoding='utf-8')
