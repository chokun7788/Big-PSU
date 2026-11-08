"""Run the fixed 1056-key trial once; freeze source/model/code and retain errors."""
import concurrent.futures,datetime,hashlib,json,os,pathlib,sqlite3,subprocess,sys,time,urllib.request,uuid
O=pathlib.Path(__file__).resolve().parent;R=O.parent
URL='http://127.0.0.1:8127/'
def read(url):
 with urllib.request.urlopen(url,timeout=7) as response:return json.load(response)
def epoch():
 with sqlite3.connect((R/'system/data/knowledge/evaluation_frozen.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as db:return dict(db.execute('select key,value from cc_meta'))
def fingerprint():
 d=hashlib.sha256()
 for folder in ['app','web_chat','tools']:
  for p in sorted((R/'system'/folder).rglob('*')):
   if p.is_file() and '__pycache__' not in p.parts and p.suffix in {'.py','.json','.js','.html','.css'}:d.update(str(p.relative_to(R)).encode());d.update(p.read_bytes())
 return d.hexdigest()
gates=json.loads((R/'GATES.json').read_text('utf8'));assert gates['ready_for_eval']
if (O/'RESULTS.jsonl').exists() or (O/'START_LOCK.json').exists():raise RuntimeError('A measured trial already exists; no automatic retry or overwrite.')
health=read(URL+'health');assert health['runtime']['version']=='R135-Hybrid48-eval5' and health['common_loaded_build']['build_id']=='common-r135-hybrid48-trial'
preflight_body={'question':'What is the studio contact email?','locale':'en','client_session_id':'eval-preflight-'+uuid.uuid4().hex,'client_turn_id':uuid.uuid4().hex,'recent_history':[],'debug':False}
preflight_request=urllib.request.Request(URL+'api/chat',data=json.dumps(preflight_body,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST')
with urllib.request.urlopen(preflight_request,timeout=195) as preflight_response:preflight=json.load(preflight_response)
(O/'CONTENT_PREFLIGHT.json').write_text(json.dumps(preflight,ensure_ascii=False,indent=2),'utf8')
if not preflight.get('ok') or 'migrated_unavailable' in preflight.get('mode','') or '@' not in preflight.get('answer',''):raise RuntimeError('The actual pinned knowledge view did not pass contact-source preflight')
(O/'CONTENT_PREFLIGHT.json').write_text(json.dumps(preflight,ensure_ascii=False,indent=2),'utf8')
model=read('http://127.0.0.1:12921/health');assert model['model']=='psu-r129:latest' and model['profiles']['retained']=='e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8'
jobs=[json.loads(x) for x in (O/'SELECTED_5_PERCENT_v2.jsonl').read_text('utf8').splitlines() if x.strip()];assert len(jobs)==1056 and len({x['key'] for x in jobs})==1056
frozen=fingerprint();source=epoch();started=time.time();completed=success=failed=0
(O/'START_LOCK.json').write_text(json.dumps({'pid':os.getpid(),'started_at':datetime.datetime.now().astimezone().isoformat()}),'utf8');(O/'PID.txt').write_text(str(os.getpid()),'utf8')
manifest={'count':1056,'selection_sha256':hashlib.sha256((O/'SELECTED_5_PERCENT_v2.jsonl').read_bytes()).hexdigest(),'code_sha256':frozen,'source_meta':source,'runtime':health['runtime'],'build':health['common_loaded_build'],'model':model,'clock':'actual Asia/Bangkok runtime, historical reference dates not injected','workers':2,'source_conditions_differ_from_saved_R134':True,'bookings':'read only; no transactions','automatic_logs':'runtime/logs'}
(O/'MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf8')
def progress(running,error=None):
 d={'completed':completed,'total':len(jobs),'percent':round(100*completed/len(jobs),2),'http_ok':success,'transport_errors':failed,'unassessed':failed,'running':running,'elapsed_seconds':round(time.time()-started),'updated_at':datetime.datetime.now().astimezone().isoformat(),'error':error,'percent_is_processing_not_correctness':True}
 temp=O/'PROGRESS.tmp';temp.write_text(json.dumps(d,indent=2),'utf8');os.replace(temp,O/'PROGRESS.json')
def one(job):
 start=time.time();session='hybrid48-eval-'+uuid.uuid4().hex;row={k:job[k] for k in ['key','question','locale']};row.update(session_id=session,started_at=datetime.datetime.now().astimezone().isoformat())
 try:
  body={'question':job['question'],'locale':job['locale'],'client_session_id':session,'client_turn_id':uuid.uuid4().hex,'recent_history':job.get('history',[]),'debug':False}
  req=urllib.request.Request(URL+'api/chat',data=json.dumps(body,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'},method='POST')
  with urllib.request.urlopen(req,timeout=225) as response:row.update(http_status=response.status,response=json.load(response))
  row['transport_ok']=row['http_status']==200 and bool(row['response'].get('ok'))
 except Exception as exc:row.update(transport_ok=False,error=repr(exc))
 row['elapsed_seconds']=round(time.time()-start,3);return row
error=None;infrastructure_failure=False;progress(True)
try:
 with (O/'RESULTS.jsonl').open('x',encoding='utf8',buffering=1) as file,concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
  iterator=iter(jobs);pending={pool.submit(one,next(iterator)) for _ in range(2)}
  while pending:
   done,pending=concurrent.futures.wait(pending,return_when=concurrent.futures.FIRST_COMPLETED)
   for f in done:
    row=f.result();file.write(json.dumps(row,ensure_ascii=False)+'\n');file.flush();completed+=1;success+=int(row['transport_ok']);failed+=int(not row['transport_ok']);progress(True)
    if completed%25==0:
     current=read(URL+'health')
     if current['common_loaded_build']!=health['common_loaded_build'] or epoch()!=source or fingerprint()!=frozen:raise RuntimeError('Source, loaded build, or code changed during measurement.')
     subprocess.run([sys.executable,'-B',str(R/'build_report.py')],stdout=subprocess.DEVNULL,check=True)
    if 'migrated_unavailable' in row.get('response',{}).get('mode',''):infrastructure_failure=True
    try:
     if not infrastructure_failure:pending.add(pool.submit(one,next(iterator)))
    except StopIteration:pass
 if infrastructure_failure:raise RuntimeError('Database became unavailable during trial; all in-flight requests retained, no new requests scheduled')
 if fingerprint()!=frozen or epoch()!=source:raise RuntimeError('Final frozen identity mismatch')
 score=subprocess.run([sys.executable,'-B',str(O/'score_results.py')],capture_output=True,text=True,encoding='utf8')
 (O/'SCORING_LOG.txt').write_text(score.stdout+'\n'+score.stderr,'utf8')
 if score.returncode:(O/'SCORING_FAILED.txt').write_text(str(score.returncode),'utf8')
except Exception as exc:
 error=repr(exc);(O/'RUN_FAILED.txt').write_text(error,'utf8');raise
finally:
 progress(False,error)
 status=json.loads((R/'STATUS.json').read_text('utf8'));status.update(phase='evaluation_complete' if completed==len(jobs) and not error else 'evaluation_stopped',evaluation_started=True,evaluation_requests_completed=completed,evaluation_total=1056,blockers=[error] if error else [],full_r135_complete=False)
 (R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),'utf8')
 subprocess.run([sys.executable,'-B',str(R/'build_report.py')],check=False)
