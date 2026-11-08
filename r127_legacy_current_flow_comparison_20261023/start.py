import json,os,socket,subprocess,sys,time,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
systems={'legacy':R.parent/'r124_legacy_guided_parity_20261023/teacher','current':R.parent/'r125_date_context_presentation_20261023/system'}
manifest=json.loads((R/'PROCESS.json').read_text('utf8')) if (R/'PROCESS.json').exists() else {}
for arm,S in systems.items():
 if os.environ.get('R127_ONLY') and arm!=os.environ['R127_ONLY']:continue
 port=12721 if arm=='legacy' else 12722
 with socket.socket() as sock:sock.bind(('127.0.0.1',port))
 OUT=R/(arm+'_'+str(time.time_ns()));OUT.mkdir()
 hashes={str(p.relative_to(S)):hashlib.sha256(p.read_bytes()).hexdigest() for top in ['app','data','config','booking_dashboard'] if (S/top).exists() for p in (S/top).rglob('*') if p.is_file() and '__pycache__' not in str(p) and p.suffix not in ['.pyc','.log']}
 (OUT/'SOURCE_BEFORE.json').write_text(json.dumps(hashes,indent=2),'utf8')
 profile='psu-r121-base:latest' if arm=='legacy' else 'psu-r121-trained:latest'
 env=os.environ.copy()
 for k in ('PSU_ESPORTS_NOW','PSU_ESPORTS_TODAY'):env.pop(k,None)
 for k in ['PSU_CHATBOT_OLLAMA_MODEL','PSU_KNOWLEDGE_LLM_MODEL','PSU_QUERY_PLANNER_MODEL','PSU_TOOL_ROUTER_MODEL','PSU_INTENT_LLM_MODEL']:env[k]=profile
 env.update(R127_ARM=arm,R127_SYSTEM=str(S),R124_RUN_DIR=str(OUT),PYTHONPATH=str(S),PYTHONDONTWRITEBYTECODE='1',OLLAMA_URL='http://127.0.0.1:12421',PSU_COMMON_CHAT_PROFILE='' if arm=='legacy' else 'r69-migration-preview',PSU_KNOWLEDGE_DB=str(OUT/'legacy_empty.sqlite') if arm=='legacy' else str(S/'data/knowledge/common.sqlite'),PSU_DOMAIN_FLOW_ENABLED='1',PSU_RUNTIME_PROFILE='r127-readonly-comparison',PSU_RUNTIME_VERSION=arm,PSU_CHAT_LOG_DIR=str(OUT/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(OUT/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(OUT/'conversation.sqlite'),PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='1',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='180',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='190',PSU_LIVE_BOOKING_ENABLED='1',PSU_LIVE_BOOKING_FETCH_MODE='wordpress',PSU_INPUT_QUALITY_REPEAT_POLICY='warn_and_continue')
 log=(OUT/'SERVER.log').open('x',encoding='utf8')
 proc=subprocess.Popen([sys.executable,'-B','-X','utf8',str(R/'serve.py'),'--host','127.0.0.1','--port',str(port)],cwd=R.parent,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
 manifest[arm]={'pid':proc.pid,'url':f'http://127.0.0.1:{port}','output':str(OUT),'system':str(S),'profile':profile}
(R/'PROCESS.json').write_text(json.dumps(manifest,indent=2),'utf8');print(json.dumps(manifest,indent=2))
