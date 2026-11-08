import json,os,socket,subprocess,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';port=int(os.environ.get('R130_PORT','13024'))
with socket.socket() as sock:sock.bind(('127.0.0.1',port))
OUT=R/('api_'+str(time.time_ns()));OUT.mkdir();env=os.environ.copy();model='psu-r129:latest'
for k in ['PSU_CHATBOT_OLLAMA_MODEL','PSU_KNOWLEDGE_LLM_MODEL','PSU_QUERY_PLANNER_MODEL','PSU_TOOL_ROUTER_MODEL','PSU_INTENT_LLM_MODEL']:env[k]=model
for k in ('PSU_ESPORTS_NOW','PSU_ESPORTS_TODAY'):env.pop(k,None)
env.update(PSU_PLANNER_PROFILE=os.environ.get('PSU_PLANNER_PROFILE','retained'),OLLAMA_URL='http://127.0.0.1:12921',PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=str(S),R124_RUN_DIR=str(OUT),PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PSU_RUNTIME_PROFILE='r130-owner-context-complete-flow',PSU_RUNTIME_VERSION='R130',PSU_CHAT_LOG_DIR=str(OUT/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(OUT/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(OUT/'conversation.sqlite'),PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='180',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='190',PSU_LIVE_BOOKING_ENABLED='1',PSU_LIVE_BOOKING_FETCH_MODE='wordpress')
log=(OUT/'SERVER.log').open('x',encoding='utf8');proc=subprocess.Popen([sys.executable,'-B','-X','utf8',str(R/'serve_api.py'),'--host','127.0.0.1','--port',str(port)],cwd=R.parent,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
config={'pid':proc.pid,'url':f'http://127.0.0.1:{port}','output':str(OUT),'candidate':str(S),'model':model,'actual_live_provider':True,'reference_clock':'real Asia/Bangkok'}
(R/'PROCESS.json').write_text(json.dumps(config,indent=2),'utf8');print(json.dumps(config,indent=2))
