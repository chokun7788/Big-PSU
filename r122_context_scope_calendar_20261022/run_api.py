"""Same candidate API/source: NF4 base versus NF4 plus context-only adapter."""
import collections,hashlib,json,os,socket,subprocess,sys,time,traceback,urllib.request,uuid
from pathlib import Path
from evaluation import evaluate,from_http
from runtime_profile import profile_environment
R=Path(__file__).resolve().parent;S=R/'system';OUT=R/'api01';MODEL_URL='http://127.0.0.1:12121'
def read(p):return json.loads(p.read_text('utf8'))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def get(url):
 with urllib.request.urlopen(url,timeout=5) as h:return json.load(h)
def post(url,data):
 req=urllib.request.Request(url,data=json.dumps(data,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=240) as h:return h.status,json.load(h)
def main():
 OUT.mkdir(exist_ok=False)
 jobs=list(map(json.loads,(R/'API_SELECTED_JOBS.jsonl').open(encoding='utf8')))
 assert len(jobs)==len({j['key'] for j in jobs})==8
 assert read(R.parent/'r121_context_planner_training_20261022/train02/TRAINING_COMPLETE.json')['complete']
 info=get(MODEL_URL+'/health');write(OUT/'MODEL_IDENTITY.json',info)
 freeze={str(p.resolve()):sha(p) for p in S.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.log'} and not p.name.endswith(('-wal','-shm'))}
 for name in ['serve_candidate.py','serve_planner.py',Path(__file__).name,'API_SELECTED_JOBS.jsonl','evaluation.py','reference_grader.py','retained_literal.py','runtime_profile.py','context_contract.py']:freeze[str((R/name).resolve())]=sha(R/name)
 write(OUT/'RUN_FREEZE.json',freeze);proc=None;log=None;rows=[]
 try:
  for profile in ['psu-r121-base:latest','psu-r121-trained:latest']:
   arm='base' if '-base:' in profile else 'trained';A=OUT/arm;A.mkdir();clock=None
   for name in ['PIPELINE_CAPTURE.jsonl','MODEL_TRANSPORT.jsonl']:(A/name).touch()
   for j in jobs:
    at=j.get('reference_date')+'T12:00:00+07:00' if j.get('reference_date') else '2026-10-21T12:00:00+07:00'
    if at!=clock:
     if proc is not None:
      proc.terminate();proc.wait(timeout=15);log.close()
     with socket.socket() as sock:sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
     env=os.environ.copy();env.update(PYTHONPATH=str(S),PYTHONDONTWRITEBYTECODE='1',R116_RUN_DIR=str(A),PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),
      PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PSU_RUNTIME_PROFILE='r121-context-lora',PSU_RUNTIME_VERSION='R121-context-lora',
      PSU_ESPORTS_NOW=at,PSU_CHAT_LOG_DIR=str(A/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(A/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(A/'conversation.sqlite'),
      PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1',
      PSU_SEMANTIC_RETRIEVAL='1',PSU_CHATBOT_OLLAMA_MODEL=profile,OLLAMA_URL=MODEL_URL,PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',
      PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='200',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='210',PSU_INPUT_QUALITY_GUARD_MODE='enforce',PSU_INPUT_QUALITY_REPEAT_POLICY='warn_and_continue')
     env.update(profile_environment(profile,MODEL_URL))
     write(A/('MODEL_ENV_'+str(time.time_ns())+'.json'),{k:env[k] for k in profile_environment(profile,MODEL_URL)})
     log=(A/('SERVER_'+str(time.time_ns())+'.log')).open('x',encoding='utf8')
     proc=subprocess.Popen([sys._base_executable,'-B','-X','utf8',str(R/'serve_candidate.py'),'--host','127.0.0.1','--port',str(port)],cwd=S,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
     url=f'http://127.0.0.1:{port}';clock=at
     for attempt in range(120):
      if proc.poll() is not None:raise RuntimeError('Candidate server exited')
      try:health=get(url+'/health');break
      except (OSError,ValueError):time.sleep(.4)
     else:raise RuntimeError('API startup timeout')
     assert health['runtime']['knowledge_draft_preview'] and health['features']['local_llm_assist']
     write(A/('HEALTH_'+str(time.time_ns())+'.json'),health)
    before=time.monotonic();error=None
    try:status,response=post(url+'/api/chat',{'question':j['question'],'locale':j['locale'],'debug':True,'experimental_allow_llm':True,'experimental_rag_fallback':False,'client_session_id':arm+'-'+j['key'],'client_turn_id':uuid.uuid4().hex})
    except (OSError,ValueError) as exc:status=0;response={};error=repr(exc)
    captures=[json.loads(line) for line in (A/'PIPELINE_CAPTURE.jsonl').open(encoding='utf8')]
    capture=next((x for x in captures if x.get('request_id')==response.get('request_id')),None)
    raw,kind,exact=from_http(response,capture);grades=evaluate(j,raw)
    row={'arm':arm,'profile':profile,'key':j['key'],'question':j['question'],'locale':j['locale'],'http_status':status,'elapsed_sec':round(time.monotonic()-before,3),'error':error,'response':response,'result':raw,'grades':grades,'capture_kind':kind,'capture_body_matches_api':exact}
    rows.append(row)
    with (A/'RESULTS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
    print(json.dumps({'arm':arm,'completed':sum(x['arm']==arm for x in rows),'total':len(jobs),'http_status':status,'elapsed_sec':row['elapsed_sec']}),flush=True)
   proc.terminate();proc.wait(timeout=15);proc=None;log.close();log=None
  assert all(sha(Path(p))==h for p,h in freeze.items()),'Candidate/source changed'
  assert len(rows)==len({(r['arm'],r['key']) for r in rows})==16,'Missing/duplicate requests'
  assert all(r['capture_body_matches_api'] is True for r in rows if r['http_status']==200),'Successful HTTP response missing faithful pipeline capture'
  # Completed measurement can include transport/content failures. They stay
  # in the denominator and are not silently retried or declared successful.
  write(OUT/'TEST_COMPLETE.json',{'complete':True,'requests_per_arm':8,'total_requests':16,'http_200':sum(r['http_status']==200 for r in rows),'all_requests_successful':all(r['http_status']==200 for r in rows),'same_candidate_source':True,'source_code_inputs_unchanged':True,'new_questions':0,'production_installed':False,'model_identity':info})
 except BaseException as exc:
  write(OUT/'FAILED.json',{'error':repr(exc),'traceback':traceback.format_exc(),'completed':len(rows)});raise
 finally:
  if proc is not None and proc.poll() is None:proc.terminate();proc.wait(timeout=15)
  if log:log.close()
if __name__=='__main__':main()
