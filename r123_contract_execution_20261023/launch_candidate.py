"""Manual isolated candidate launcher. Does not install or replace production.

The existing controlled-unavailable live-provider fixture is preserved.
--check-config only validates/prints config; it makes no model or API calls.
"""
import argparse,json,os,socket,subprocess,sys,time,urllib.request
from pathlib import Path
from runtime_profile import profile_environment
R=Path(__file__).resolve().parent;S=R/'revision03_system'
HF_PYTHON=Path('D:/CodexTraining/psu-r121-20261022/venv/Scripts/python.exe')
parser=argparse.ArgumentParser();parser.add_argument('--port',type=int,default=12122);parser.add_argument('--model-port',type=int,default=12121);parser.add_argument('--check-config',action='store_true');args=parser.parse_args()
endpoint=f'http://127.0.0.1:{args.model_port}';profile='psu-r121-trained:latest';settings=profile_environment(profile,endpoint)
config={'candidate':str(S),'model_settings':settings,'chat_url':f'http://127.0.0.1:{args.port}','training_complete':json.loads((R.parent/'r121_context_planner_training_20261022/train02/TRAINING_COMPLETE.json').read_text('utf8'))['complete'],'source_data_read_from_candidate':True,'production_install':False,'live_provider':'controlled unavailable fixture; not real occupancy','note':'R123 foundation revision03; unified profiles for every caller. P0/P1 foundation; no new model inference benchmark yet; native calendar/live special adapters remain; live provider controlled unavailable.'}
assert config['training_complete'] and HF_PYTHON.is_file() and S.is_dir()
if args.check_config:
 print(json.dumps(config,ensure_ascii=False,indent=2));raise SystemExit(0)
for port in [args.port,args.model_port]:
 with socket.socket() as sock:sock.bind(('127.0.0.1',port))
tag=str(time.time_ns());OUT=R/('manual_runtime_'+tag);OUT.mkdir();model=None;native=None;handles=[]
def spawn(name,python,script,env,*tail):
 log=(OUT/(name+'.log')).open('x',encoding='utf8');handles.append(log)
 return subprocess.Popen([str(python),'-B','-X','utf8',str(R/script),*tail],cwd=R.parent,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
def stop_own_tree(proc):
 if proc is None or proc.poll() is not None:return
 # psutil belongs to the isolated training environment. This helper is called
 # through that interpreter, and only addresses children created above.
 import psutil
 try:children=psutil.Process(proc.pid).children(recursive=True)
 except psutil.NoSuchProcess:children=[]
 for child in reversed(children):
  try:child.terminate()
  except psutil.NoSuchProcess:pass
 proc.terminate()
 try:proc.wait(timeout=15)
 except subprocess.TimeoutExpired:proc.kill();proc.wait(timeout=5)
try:
 for name in ['PIPELINE_CAPTURE.jsonl','MODEL_TRANSPORT.jsonl']:(OUT/name).touch()
 (OUT/'CONFIG.json').write_text(json.dumps(config,ensure_ascii=False,indent=2),'utf8')
 model=spawn('MODEL',HF_PYTHON,'serve_planner.py',os.environ.copy(),'--port',str(args.model_port),'--output-name','manual_inference_'+tag)
 for attempt in range(180):
  if model.poll() is not None:raise RuntimeError('Model server stopped; inspect MODEL.log')
  try:
   with urllib.request.urlopen(endpoint+'/health',timeout=2) as h:health=json.load(h)
   assert health['training_complete_verified'];break
  except (OSError,ValueError):time.sleep(2)
 else:raise RuntimeError('Model startup timed out')
 env=os.environ.copy();env.update(settings)
 env.update(PYTHONPATH=str(S),PYTHONDONTWRITEBYTECODE='1',R116_RUN_DIR=str(OUT),PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),
  PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PSU_RUNTIME_PROFILE='r123-foundation-r03',PSU_RUNTIME_VERSION='R123-foundation-r03',
  PSU_CHAT_LOG_DIR=str(OUT/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(OUT/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(OUT/'conversation.sqlite'),
  PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1',
  PSU_SEMANTIC_RETRIEVAL='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='200',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='210')
 native=spawn('CHAT',sys._base_executable,'serve_candidate.py',env,'--host','127.0.0.1','--port',str(args.port))
 print(json.dumps(config,ensure_ascii=False,indent=2),flush=True)
 while native.poll() is None and model.poll() is None:time.sleep(1)
 raise RuntimeError('A candidate process stopped; inspect the new runtime log directory')
except KeyboardInterrupt:pass
finally:
 stop_own_tree(native);stop_own_tree(model)
 for handle in handles:handle.close()
