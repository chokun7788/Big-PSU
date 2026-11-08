"""Fresh hybrid48 HTTP sample; append results, preserve ordinary application logs."""
import concurrent.futures,hashlib,json,os,sys,threading,time,urllib.request,urllib.error,uuid
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
JOBS=OUT/'SELECTED_5_PERCENT_v2.jsonl'
URL='http://127.0.0.1:8125/'
BUILD='common-r135-hybrid48-trial'
def read_json(url):
 with urllib.request.urlopen(url,timeout=5) as r:return json.load(r)
def health():
 x=read_json(URL+'health')
 if x.get('common_loaded_build',{}).get('build_id')!=BUILD:raise RuntimeError('wrong candidate build')
 if x.get('runtime',{}).get('version')!='R135-Hybrid48':raise RuntimeError('small trial runtime identity mismatch')
 return x
jobs=[json.loads(x) for x in JOBS.read_text('utf8').splitlines() if x.strip()]
assert len(jobs)==1056 and len({x['key'] for x in jobs})==len(jobs)
h=health()
manifest={'created':datetime.now().astimezone().isoformat(),'sample_size':len(jobs),'selection':'deterministic nested 1056 of prior 2111 stratified keys, one category preservation swap','selection_sha256':hashlib.sha256(JOBS.read_bytes()).hexdigest(),'runtime':h['runtime'],'build':h['common_loaded_build'],'mode':'fresh isolated small-flow trial local HTTP, actual clock, debug false','booking':'live runtime configuration; no booking transactions','historic_reference_dates':'not injected into live runtime','logs':'application automatic JSONL and SQLite plus this run results','workers':2}
(OUT/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
lock=threading.Lock(); start=time.time(); completed=0; success=0; failed=0
def progress(running):
 state={'completed':completed,'total':len(jobs),'percent':round(100*completed/len(jobs),2),'http_ok':success,'unassessed':failed,'running':running,'elapsed_seconds':round(time.time()-start),'updated_at':datetime.now().astimezone().isoformat()}
 t=OUT/'PROGRESS.tmp';t.write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf8');os.replace(t,OUT/'PROGRESS.json')
def one(job):
 session='eval-hybrid48-5pct-'+uuid.uuid4().hex
 body={'question':job['question'],'locale':job['locale'],'client_session_id':session,'client_turn_id':'turn-'+uuid.uuid4().hex,'recent_history':job.get('history',[]),'debug':False}
 row={'key':job['key'],'question':job['question'],'locale':job['locale'],'session_id':session,'stratum':job.get('r70_stratum'),'started_at':datetime.now().astimezone().isoformat()}
 try:
  req=urllib.request.Request(URL+'api/chat',data=json.dumps(body,ensure_ascii=False).encode('utf8'),headers={'Content-Type':'application/json'},method='POST')
  with urllib.request.urlopen(req,timeout=225) as res: row['http_status']=res.status;row['response']=json.load(res)
  row['transport_ok']=row['http_status']==200 and bool(row['response'].get('ok'))
 except Exception as exc:row['transport_ok']=False;row['error']=repr(exc)
 row['elapsed_seconds']=round(time.time()-datetime.fromisoformat(row['started_at']).timestamp(),3)
 return row
if (OUT/'RESULTS.jsonl').exists():raise RuntimeError('existing measured results must not be overwritten or resumed silently')
progress(True)
with (OUT/'RESULTS.jsonl').open('x',encoding='utf8',buffering=1) as f, concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 pending=set(); iterator=iter(jobs)
 for _ in range(2):pending.add(pool.submit(one,next(iterator)))
 while pending:
  done,pending=concurrent.futures.wait(pending,return_when=concurrent.futures.FIRST_COMPLETED)
  for future in done:
   row=future.result()
   with lock:
    f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush();completed+=1
    if row['transport_ok']:success+=1
    else:failed+=1
    progress(True)
   if completed%25==0:health()
   try:pending.add(pool.submit(one,next(iterator)))
   except StopIteration:pass
import subprocess
score=subprocess.run([sys.executable,str(OUT/'score_results.py')],capture_output=True,text=True,encoding='utf8')
(OUT/'SCORING_LOG.txt').write_text(score.stdout+'\n'+score.stderr,encoding='utf8')
if score.returncode: (OUT/'SCORING_FAILED.txt').write_text(str(score.returncode),encoding='utf8')
progress(False)
