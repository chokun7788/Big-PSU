import json,os,socket,subprocess,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;S=R.parent/'r125_date_context_presentation_20261023/system';P=R.parent/'r125_date_context_presentation_20261023'
with socket.socket() as s:s.bind(('127.0.0.1',12622))
# Reuse the tested runtime environment with separate sessions and logs.
text=(P/'start_api.py').read_text('utf8');prefix=text[text.index("settings={"):text.index("if a.check_config:")]
env=os.environ.copy();profile='psu-r121-trained:latest'
for k in ['PSU_CHATBOT_OLLAMA_MODEL','PSU_KNOWLEDGE_LLM_MODEL','PSU_QUERY_PLANNER_MODEL','PSU_TOOL_ROUTER_MODEL','PSU_INTENT_LLM_MODEL']:env[k]=profile
for k in ('PSU_ESPORTS_NOW','PSU_ESPORTS_TODAY'):env.pop(k,None)
OUT=R/('run_'+str(time.time_ns()));OUT.mkdir()
env.update(OLLAMA_URL='http://127.0.0.1:12421',PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=str(S),R124_RUN_DIR=str(OUT),PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PSU_RUNTIME_PROFILE='r126-readonly-latency-audit',PSU_RUNTIME_VERSION='R125-instrumented-audit',PSU_CHAT_LOG_DIR=str(OUT/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(OUT/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(OUT/'conversation.sqlite'),PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='180',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='190',PSU_LIVE_BOOKING_ENABLED='1',PSU_LIVE_BOOKING_FETCH_MODE='wordpress')
log=(OUT/'SERVER.log').open('x',encoding='utf8');proc=subprocess.Popen([sys.executable,'-B','-X','utf8',str(R/'serve_audit.py'),'--host','127.0.0.1','--port','12622'],cwd=R.parent,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
config={'pid':proc.pid,'url':'http://127.0.0.1:12622','output':str(OUT),'read_only_system':str(S),'active_user_api_unchanged':'http://127.0.0.1:12422'}
(R/'PROCESS.json').write_text(json.dumps(config,indent=2),'utf8');print(json.dumps(config,indent=2))
