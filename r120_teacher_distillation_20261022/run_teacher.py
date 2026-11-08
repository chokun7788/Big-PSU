"""Observe the original R64 pipeline in isolation, LLM ON, no weight updates."""
import dataclasses,hashlib,json,os,sys,time,traceback,urllib.request
from datetime import date,datetime
from pathlib import Path
R=Path(__file__).resolve().parent;T=R/'teacher_system';OUT=R/'teacher01';OUT.mkdir(exist_ok=False)
sys.path.insert(0,str(T));MODEL='scb10x/typhoon2.5-qwen3-4b:latest';DIGEST='b1f251ef835962b270ba48266d4e32e6f90b29f10930d0712ef5eaabec773a05'
os.environ.update(PYTHONDONTWRITEBYTECODE='1',PSU_KNOWLEDGE_DB=str(R/'teacher.sqlite'),PSU_BILINGUAL_EN_ENABLED='1',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_SEMANTIC_RETRIEVAL='1',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WARMUP='0',PSU_PIPELINE_WORKER_SUPERVISOR='0',PSU_INPUT_QUALITY_GUARD_MODE='enforce',PSU_INPUT_QUALITY_REPEAT_POLICY='warn_and_continue',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='32',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='30',PSU_INTENT_LLM_TIMEOUT_SEC='14',PSU_INTENT_LLM_NUM_CTX='1536',PSU_INTENT_LLM_NUM_PREDICT='18',PSU_CHAT_LOG_DIR=str(OUT/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(OUT/'logs/transcripts.sqlite'),PSU_CHATBOT_OLLAMA_MODEL=MODEL,OLLAMA_URL='http://127.0.0.1:11434',PSU_CONVERSATION_STATE_PATH=str(OUT/'conversation.sqlite'),PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_LLM_MAX_CONCURRENCY='1')
write=lambda n,v:(OUT/n).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
def identity():
 with urllib.request.urlopen('http://127.0.0.1:11434/api/tags',timeout=5) as h:tags=json.load(h)
 assert next(m['digest'] for m in tags['models'] if m['name']==MODEL)==DIGEST
 return {'model':MODEL,'digest':DIGEST,'verified_at':datetime.now().astimezone().isoformat()}
write('MODEL_BEFORE.json',identity())
from app.booking import live_status
from app.runtime import fast_answer
from app.pipeline import bilingual_english
def unavailable(d):return live_status._unavailable(d,'R120 teacher controlled unavailable fixture; not actual live occupancy',error_code='fixture_offline')
for m in [live_status,fast_answer,bilingual_english]:m.get_live_booking_status=unavailable
from app.pipeline.engine import answer_question_pipeline_debug
from app.core.locale import resolve_locale
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
from app.pipeline.input_recovery import inspect_surface_input
from unittest.mock import patch
guard=RuntimeInputQualityGuard.from_environment()
jobs=list(map(json.loads,(R/'TEACHING_JOBS.jsonl').open(encoding='utf8')));started=time.monotonic();seen=set();stats={}
def progress(running):write('PROGRESS.json',{'running':running,'complete':not running and len(seen)==len(jobs),'completed':len(seen),'total':len(jobs),'elapsed_sec':round(time.monotonic()-started,2),'pid':os.getpid()})
progress(True)
try:
 with (OUT/'RESULTS.jsonl').open('x',encoding='utf8') as f:
  for j in jobs:
   start=time.monotonic();q=j['question'];quality=guard.inspect(q);surface=inspect_surface_input(q)
   locale=resolve_locale(q,requested=j['locale'],keyboard_layout_direction=quality.locale_layout_direction,surface_language=surface.language if surface.should_review_intent else None)
   try:
    with patch('app.booking.live_status.today_bangkok',return_value=date(2026,10,21)):
     result=answer_question_pipeline_debug(q,locale=j['locale'],locale_decision=locale,experimental_allow_llm=True,experimental_rag_fallback=True,global_timeout_sec=30,recent_history=[])
    raw=dataclasses.asdict(result) if dataclasses.is_dataclass(result) else result
    row={'key':j['key'],'question':q,'locale':j['locale'],'result':raw,'elapsed_sec':time.monotonic()-start,'teacher_llm_enabled':True,'observable_trace_only':True,'weights_updated':False}
   except Exception as exc:row={'key':j['key'],'question':q,'locale':j['locale'],'error':repr(exc),'elapsed_sec':time.monotonic()-start}
   assert j['key'] not in seen;f.write(json.dumps(row,ensure_ascii=False,default=str)+'\n');f.flush();seen.add(j['key']);progress(True)
 write('MODEL_AFTER.json',identity());progress(False)
 write('COMPLETE.json',{'complete':True,'requests':len(seen),'llm_enabled':True,'new_questions':0,'observable_pipeline_traces_retained':True,'model_identity_verified':True,'weights_updated':False,'production_installed':False,'elapsed_sec':time.monotonic()-started})
except BaseException as exc:write('FAILED.json',{'error':repr(exc),'traceback':traceback.format_exc(),'completed':len(seen)});raise
