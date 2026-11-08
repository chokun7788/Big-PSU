"""Use the actual subprocess worker path; no HTTP/socket/model success claim."""
import hashlib,json,os,sys
from pathlib import Path
B=Path(__file__).resolve().parent;S=B/'system';T=B/'verification'/sys.argv[1]
os.environ.update(PYTHONUTF8='1',PYTHONDONTWRITEBYTECODE='1',PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),PSU_CONVERSATION_STATE_PATH=str(T/'state.sqlite'),PSU_CHAT_LOG_DIR=str(T/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(T/'logs/transcripts.sqlite'),PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_PIPELINE_WORKER_SUPERVISOR='1',PSU_PIPELINE_WORKERS='2',PSU_PIPELINE_WORKER_WARMUP_EMBEDDING='0',PSU_PIPELINE_WORKER_WARMUP_LLM='0',PSU_PIPELINE_WARMUP='0',PSU_LLM_PREFLIGHT='0',PSU_BILINGUAL_EN_ENABLED='1',PSU_QUERY_PLANNER_TIMEOUT_SEC='2.5')
sys.path.insert(0,str(S))
def main():
 from app.web_api.pipeline_supervisor import PipelineWorkerSupervisor
 from concurrent.futures import ThreadPoolExecutor
 T.mkdir(parents=True,exist_ok=False)
 before=hashlib.sha256((S/'data/knowledge/common.sqlite').read_bytes()).hexdigest()
 worker=PipelineWorkerSupervisor(workers=2);rows=[]
 try:
  worker.start()
  health=worker.health()
  rows.append({'case':'two workers alive and ready','passed':len(health['workers'])==2 and all(w['alive'] and w['ready'] for w in health['workers']),'detail':health})
  def ask(pair):
   q,lang,need=pair
   call=worker.answer(q,timeout_sec=20,experimental_rag_fallback=False,experimental_allow_llm=True,locale=lang)
   result=getattr(call,'result',None)
   if result is None:result=getattr(call,'answer',None)
   txt=getattr(result,'answer','')
   actual_lang=getattr(getattr(result,'language',None),'effective',None)
   return {'case':q,'passed':call.status=='ok' and need in txt and actual_lang==lang and (result.decision_artifact or {}).get('migration',{}).get('legacy_fallback_used') is False,'status':call.status,'answer':txt,'effective_language':actual_lang,'elapsed_sec':call.elapsed_sec,'error':call.error}
  with ThreadPoolExecutor(max_workers=2) as pool:
   rows.extend(pool.map(ask,[('PS5 มีเกมอะไรบ้าง','th','God of War'),('List all games on PC','en','Counter-Strike')]))
 except Exception as exc:rows.append({'case':'worker transport available','passed':False,'error_type':type(exc).__name__,'error':str(exc)})
 finally:worker.shutdown()
 rows.append({'case':'copied database unchanged','passed':before==hashlib.sha256((S/'data/knowledge/common.sqlite').read_bytes()).hexdigest()})
 result={'cases':len(rows),'passed':sum(r['passed'] for r in rows),'details':rows}
 (T/'RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str),encoding='utf8')
 print(json.dumps(result,ensure_ascii=False,default=str))
 raise SystemExit(any(not r['passed'] for r in rows))
if __name__=='__main__':main()
