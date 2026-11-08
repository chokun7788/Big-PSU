"""The original Full sample through a frozen native chat HTTP API, LLM ON."""
import collections,hashlib,json,os,socket,subprocess,sys,time,traceback,urllib.request,urllib.error,uuid
from datetime import datetime
from pathlib import Path
from evaluation import evaluate,from_http
R=Path(__file__).resolve().parent;S=R/'system';OUT=R/'regression02'
MODEL='scb10x/typhoon2.5-qwen3-4b:latest';DIGEST='b1f251ef835962b270ba48266d4e32e6f90b29f10930d0712ef5eaabec773a05'
def read(p):return json.loads(p.read_text('utf8'))
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
 return h.hexdigest()
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
def get(url,timeout=3):
 with urllib.request.urlopen(url,timeout=timeout) as h:return json.load(h)
def tags():
 x=get('http://127.0.0.1:11434/api/tags',5)
 assert next(m['digest'] for m in x['models'] if m['name']==MODEL)==DIGEST
 return {'model':MODEL,'digest':DIGEST,'verified_at':datetime.now().astimezone().isoformat()}
def events(response):
 out={}
 def visit(x):
  if isinstance(x,dict):
   if 'transport_ok' in x and 'schema_ok' in x and x.get('id'):out[x['id']]=x
   for v in x.values():visit(v)
  elif isinstance(x,list):
   for v in x:visit(v)
 visit(response.get('decision_artifact') or {});return list(out.values())

def main():
 OUT.mkdir(exist_ok=False)
 jobs=list(map(json.loads,(R/'DEVELOPMENT_JOBS.jsonl').open(encoding='utf8')));manifest=read(R/'DEV_MANIFEST.json')
 assert len(jobs)==len({j['key'] for j in jobs})==manifest['requests']
 for name in ['PIPELINE_CAPTURE.jsonl','MODEL_TRANSPORT.jsonl','MODEL_EVENTS.jsonl']:(OUT/name).touch(exist_ok=False)
 baseline=read(R/'REFERENCE_HASHES.json');assert all(sha(Path(p))==h for p,h in baseline.items())
 files=[p for p in S.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.log'} and not p.name.endswith(('-wal','-shm'))]
 files += [R/n for n in ['DEVELOPMENT_JOBS.jsonl','DEV_MANIFEST.json','SPLIT_MANIFEST.json','serve_frozen.py','evaluation.py','reference_grader.py','retained_literal.py','run_baseline.py','run_student.py','run_regression.py','run_regression02.py']]
 freeze={str(p.resolve()):sha(p) for p in files};write(OUT/'RUN_FREEZE.json',{'files':freeze,'model':MODEL,'digest':DIGEST,'new_questions':0,'category_hints_sent':False,'candidate':'R120 distilled student','started_at':datetime.now().astimezone().isoformat()})
 proc=None;log=None;url=None;clock=None;clock_index=0;healths=[];captures={};cap_offset=0;seen=set();stats=collections.Counter();locales=collections.defaultdict(collections.Counter);started=time.monotonic()
 def progress(running=True):
  state={'running':running,'complete':not running and len(seen)==len(jobs),'completed':len(seen),'total':len(jobs),'grades':stats['grades'],
     'stats':dict(stats),'by_locale':{k:dict(v) for k,v in locales.items()},'elapsed_sec':round(time.monotonic()-started,2),'runner_pid':os.getpid(),
     'server_pid':proc.pid if proc and proc.poll() is None else None,'clock':clock,'updated_at':datetime.now().astimezone().isoformat()}
  tmp=OUT/'progress.new';write(tmp,state)
  for i in range(8):
   try:os.replace(tmp,OUT/'PROGRESS.json');break
   except PermissionError:time.sleep(.05*(i+1))
  else:write(OUT/('PROGRESS_IO_'+str(time.time_ns())+'.json'),state)
  write(R/'STATUS.json',{'phase':'running' if running else 'completed_awaiting_analysis','complete':False,'completed':len(seen),'target':len(jobs),'new_questions':0,'production_installed':False})
  return state
 def stop():
  nonlocal proc,log
  if proc is None:return
  if proc.poll() is None:
   after=get(url+'/health');assert after['common_loaded_build']==healths[-1]['health_before']['common_loaded_build'];healths[-1]['health_after']=after
   proc.terminate()
   try:proc.wait(timeout=10)
   except subprocess.TimeoutExpired:proc.kill();proc.wait(timeout=5)
  healths[-1]['stopped_exit_code']=proc.returncode
  write(OUT/'SERVERS.json',healths);proc=None
  if log:log.close();log=None
 def start(at):
  nonlocal proc,log,url,clock,clock_index
  stop();clock=at;clock_index+=1
  with socket.socket() as sock:sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
  env=os.environ.copy();env.update(PYTHONPATH=str(S),PYTHONDONTWRITEBYTECODE='1',R116_RUN_DIR=str(OUT),PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),
      PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PSU_RUNTIME_PROFILE='r120-student',PSU_RUNTIME_VERSION='R120-distilled-student',
      PSU_ESPORTS_NOW=at,PSU_CHAT_LOG_DIR=str(OUT/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(OUT/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(OUT/'conversation.sqlite'),
      PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1',
      PSU_SEMANTIC_RETRIEVAL='1',PSU_CHATBOT_OLLAMA_MODEL=MODEL,OLLAMA_URL='http://127.0.0.1:11434',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',
      PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='30',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='32',PSU_INPUT_QUALITY_GUARD_MODE='enforce',PSU_INPUT_QUALITY_REPEAT_POLICY='warn_and_continue')
  log=(OUT/f'SERVER_{clock_index:02}.log').open('x',encoding='utf8')
  proc=subprocess.Popen([sys.executable,'-B','-X','utf8',str(R/'serve_frozen.py'),'--host','127.0.0.1','--port',str(port)],cwd=S,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
  url='http://127.0.0.1:'+str(port)
  record={'server_pid':proc.pid,'runner_pid':os.getpid(),'url':url,'clock':clock,'command':'serve_frozen.py','candidate_only':True};healths.append(record);write(OUT/'SERVERS.json',healths)
  for _ in range(120):
   if proc.poll() is not None:raise RuntimeError('Candidate server exited; see SERVER log')
   try:health=get(url+'/health');break
   except (OSError,ValueError):time.sleep(.4)
  else:raise RuntimeError('Candidate startup timeout')
  assert health['runtime']['knowledge_draft_preview'] and health['features']['local_llm_assist'];record['health_before']=health;write(OUT/'SERVERS.json',healths)
 try:
  write(OUT/'MODEL_BEFORE.json',tags());progress()
  with (OUT/'RESULTS.jsonl').open('x',encoding='utf8') as output,(OUT/'MODEL_EVENTS.jsonl').open('a',encoding='utf8') as ef:
   for j in jobs:
    at=(j.get('reference_date')+'T12:00:00+07:00') if j.get('reference_date') else manifest['default_reference_clock']
    if at!=clock:start(at)
    assert proc.poll() is None,'Candidate server stopped unexpectedly'
    payload={'question':j['question'],'locale':j['locale'],'debug':True,'experimental_allow_llm':True,'experimental_rag_fallback':False,
        'client_session_id':'r120-student-'+j['key'],'client_turn_id':uuid.uuid4().hex}
    req=urllib.request.Request(url+'/api/chat',data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
    before=time.monotonic();status=0;error=None
    try:
     with urllib.request.urlopen(req,timeout=65) as h:status=h.status;response=json.load(h)
    except urllib.error.HTTPError as exc:
     status=exc.code;error='HTTP '+str(status)
     try:response=json.loads(exc.read())
     except (ValueError,TypeError):response={}
    except (OSError,ValueError) as exc:response={};error=type(exc).__name__+':'+str(exc)
    elapsed=time.monotonic()-before
    # The serializer logs the actual PipelineAnswer under its PUBLIC request_id.
    with (OUT/'PIPELINE_CAPTURE.jsonl').open(encoding='utf8') as cf:
     cf.seek(cap_offset)
     for line in cf:
      c=json.loads(line);captures[c['request_id']]=c
     cap_offset=cf.tell()
    capture=captures.pop(response.get('request_id'),None)
    raw,kind,exact=from_http(response,capture);grades=evaluate(j,raw)
    row={'key':j['key'],'question':j['question'],'requested_locale':j['locale'],'domain':j['r70_stratum']['domain'],'reference_clock':at,
       'http_status':status,'elapsed_sec':round(elapsed,4),'error':error,'response':response,'result':raw,'grades':grades,
       'capture_kind':kind,'capture_body_matches_api':exact,'capture_window':(capture or {}).get('window')}
    assert j['key'] not in seen;output.write(json.dumps(row,ensure_ascii=False)+'\n');output.flush();seen.add(j['key'])
    for e in events(response):ef.write(json.dumps({**e,'key':j['key']},ensure_ascii=False)+'\n');ef.flush()
    positive=[g for g in grades if g['positive_literal']]
    for c in [stats,locales[j['locale']]]:
     c['requests']+=1;c['http_ok']+=200<=status<300;c['validation_ok']+=response.get('validation_ok') is True;c['grades']+=len(grades)
     c['strict_pass']+=sum(g['passed'] for g in grades);c['positive_grades']+=len(positive);c['positive_pass']+=sum(g['literal_passed'] for g in positive)
     c['positive_requests']+=bool(positive);c['positive_requests_pass']+=bool(positive) and all(g['literal_passed'] for g in positive)
     c['capture_mismatch']+=exact is False;c['grader_errors']+=sum(any(s.startswith('grader_exception') for s in g['failures']) for g in grades)
     c['timed_out']+=bool(response.get('timed_out'));c['empty_answers']+=not bool(response.get('answer'))
    progress()
    if len(seen)%100==0:print(json.dumps(progress()),flush=True)
  stop();write(OUT/'MODEL_AFTER.json',tags())
  changed=[p for p,h in freeze.items() if sha(Path(p))!=h];assert not changed,changed
  originals_changed=[p for p,h in baseline.items() if sha(Path(p))!=h];assert not originals_changed,originals_changed
  assert len(seen)==manifest['requests'] and stats['grades']==manifest['grades'] and not stats['capture_mismatch']
  done={'complete':True,'unique_request_keys':len(seen),'grades':stats['grades'],'all_selected_keys_recorded':True,'source_code_inputs_unchanged':True,
       'original_sources_and_results_unchanged':True,'model_identity_verified':True,'new_questions':0,'category_hints_sent':False,'stats':dict(stats),
       'elapsed_sec':round(time.monotonic()-started,2),'completed_at':datetime.now().astimezone().isoformat()}
  write(OUT/'TEST_COMPLETE.json',done);progress(False);print(json.dumps(done),flush=True)
 except BaseException as exc:
  write(OUT/'FAILED.json',{'complete':False,'completed':len(seen),'expected':len(jobs),'error':repr(exc),'traceback':traceback.format_exc()});raise
 finally:
  stop()
if __name__=='__main__':main()
