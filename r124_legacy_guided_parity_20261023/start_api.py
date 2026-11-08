"""Launch only R124 candidate with on-demand live WordPress, leaving R78 intact."""
import argparse,json,os,socket,subprocess,sys,time,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'revision05_system'
p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=12422);p.add_argument('--model-port',type=int,default=12421);p.add_argument('--check-config',action='store_true');a=p.parse_args()
endpoint=f'http://127.0.0.1:{a.model_port}';profile='psu-r121-trained:latest'
settings={k:profile for k in ['PSU_CHATBOT_OLLAMA_MODEL','PSU_KNOWLEDGE_LLM_MODEL','PSU_QUERY_PLANNER_MODEL','PSU_TOOL_ROUTER_MODEL','PSU_INTENT_LLM_MODEL']}
config={'candidate':str(S),'url':f'http://127.0.0.1:{a.port}','model_endpoint':endpoint,'model_profile':profile,
 'live_provider':'wordpress','read_on_question_only':True,'production_installed':False,'controlled_fixture':False,'reference_clock':'real Asia/Bangkok clock, no retained-test override'}
if a.check_config:print(json.dumps(config,ensure_ascii=False,indent=2));raise SystemExit()
with socket.socket() as sock:sock.bind(('127.0.0.1',a.port))
with urllib.request.urlopen(endpoint+'/health',timeout=4) as response:health=json.load(response)
assert health['training_complete_verified'],'Expected isolated R121 model provenance'
OUT=R/('live_api_'+str(time.time_ns()));OUT.mkdir();env=os.environ.copy();env.update(settings)
for k in ('PSU_ESPORTS_NOW','PSU_ESPORTS_TODAY'):env.pop(k,None)
env.update(OLLAMA_URL=endpoint,PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=str(S),R124_RUN_DIR=str(OUT),PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),
 PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PSU_RUNTIME_PROFILE='r124-legacy-guided-live',PSU_RUNTIME_VERSION='R124-revision05-live',
 PSU_CHAT_LOG_DIR=str(OUT/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(OUT/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(OUT/'conversation.sqlite'),
 PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1',
 PSU_SEMANTIC_RETRIEVAL='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='180',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='190',
 PSU_LIVE_BOOKING_ENABLED='1',PSU_LIVE_BOOKING_FETCH_MODE='wordpress')
log=(OUT/'CHAT.log').open('x',encoding='utf8')
proc=subprocess.Popen([sys.executable,'-B','-X','utf8',str(R/'serve_live.py'),'--host','127.0.0.1','--port',str(a.port)],cwd=R.parent,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
config.update(pid=proc.pid,output=str(OUT));(OUT/'CONFIG.json').write_text(json.dumps(config,ensure_ascii=False,indent=2),'utf8');(R/'LIVE_API_PROCESS.json').write_text(json.dumps(config,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(config,ensure_ascii=False,indent=2),flush=True)
