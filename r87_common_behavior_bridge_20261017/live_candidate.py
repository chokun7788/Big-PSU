"""Focused real-model conversations using a candidate overlay, not a full test."""
import hashlib,importlib.util,json,os,statistics,sys,time
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system';T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
db=S/'data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(db),PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(T/'state.sqlite'),PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WARMUP='0',PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0')
sys.path.insert(0,str(S))
import app.knowledge.common as pkg
pkg.__path__.insert(0,str(B/('before' if '--before' in sys.argv else 'candidate')/'app/knowledge/common'))
import app.pipeline as pipeline_pkg
pipeline_pkg.__path__.insert(0,str(B/'candidate/app/pipeline'))
from app.pipeline.migrated_chat import answer
from app.core.locale import LocaleDecision
from app.knowledge.common.dialogue import state_from_answer
spec=importlib.util.spec_from_file_location('r79_http',B.parent/'r79_connection_diagnostics_20261017/check_connection.py');helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
sys.path.insert(0,str(B.parent/'r82_automatic_llm_check_20261017'))
from auto_test import Runner
boot=T/'model_readiness';boot.mkdir();boot_runner=Runner(boot)
tags=boot_runner.get('model_list','http://127.0.0.1:11434/api/tags')
warm=boot_runner.ensure_model(tags,'scb10x/typhoon2.5-qwen3-4b')
helper.emit_json(T/'MODEL_PREFLIGHT.json',warm)
if not warm.get('http_ok') or not (warm.get('body') or {}).get('done'):raise SystemExit('Real model generation preflight did not finish')
from contracts import CASES,check

rows=[]
for case,lang,turns in CASES:
 if '--rules-only' in sys.argv and not case.startswith('rules-'):continue
 history=[]
 for q,expect in turns:
  start=time.perf_counter();r=answer(q,locale=LocaleDecision(lang,lang,lang,1,'explicit_focused_locale'),history=history,allow_llm=True);elapsed=time.perf_counter()-start
  p=(r.decision_artifact or {}).get('query_plan') or {};audit=p.get('entity_selection') or {};state=state_from_answer(r) or {};errors=[]
  errors=check({'decision_artifact':r.decision_artifact,'common_read_state':state,'answer':r.answer,'validation_ok':r.validation.ok},expect)
  model_errors=[]
  if audit.get('availability_failure'):model_errors.append(audit['availability_failure'])
  if audit.get('semantic_selection_accepted') is False and audit.get('reason'):model_errors.append(audit['reason'])
  row={'case':case,'locale':lang,'question':q,'expect':expect,'passed':not errors,'errors':errors,'model_errors':model_errors,'seconds':round(elapsed,3),'answer':r.answer,'plan':p,'state':state,'artifact':r.decision_artifact,'hits':r.hits};rows.append(row)
  with (T/'TURNS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n')
  print(json.dumps({'case':case,'question':q,'passed':not errors,'errors':errors,'model_errors':model_errors,'seconds':row['seconds'],'proposal_only':audit.get('topic_proposal_only'),'model_called':audit.get('attempted')},ensure_ascii=False),flush=True)
  history += [{'role':'user','text':q},{'role':'assistant','text':r.answer,'common_read_state':state,'delivery_status':'server_written'}]
summary={'count':len(rows),'passed':sum(r['passed'] for r in rows),'real_llm_generation_verified':True,'llm_enabled':True,'format':'common','candidate_overlay':True,'actual_web_http_tested':False,'full_corpus':False,'model_call_count':sum((r['plan'].get('entity_selection') or {}).get('attempted') is True for r in rows),'proposal_calls':sum(bool((r['plan'].get('entity_selection') or {}).get('topic_proposal_only')) for r in rows),'model_failures':[{'case':r['case'],'question':r['question'],'failures':r['model_errors']} for r in rows if r['model_errors']],'failed_answers':[{'case':r['case'],'question':r['question'],'errors':r['errors']} for r in rows if not r['passed']],'database_unchanged':before==hashlib.sha256(db.read_bytes()).hexdigest()}
helper.emit_json(T/'SUMMARY.json',summary);print(json.dumps(summary,ensure_ascii=False));raise SystemExit(any(not r['passed'] for r in rows) or any(r['model_errors'] for r in rows))
