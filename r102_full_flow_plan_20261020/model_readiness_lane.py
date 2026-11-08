"""Warm the configured existing model inside the batch, separate from accuracy."""
import os,sys,json,time
from pathlib import Path
R=Path(__file__).resolve().parent;T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False);sys.path.insert(0,str(R/'system'))
from app.knowledge.local_models import MODEL_WORK,_local_url
from app.pipeline.llm_health import preflight_ollama
model=os.getenv('PSU_KNOWLEDGE_LLM_MODEL','scb10x/typhoon2.5-qwen3-4b');start=time.perf_counter();acquired=False
try:
 acquired=MODEL_WORK.acquire(timeout=30)
 if not acquired:raise TimeoutError('Configured model gate busy during batch readiness')
 result=preflight_ollama(model=model,kind='r102_batch_readiness',timeout_sec=60,num_predict=8,num_ctx=3072,ollama_url=_local_url(os.getenv('OLLAMA_URL','http://127.0.0.1:11434')))
 summary={'count':1,'passed':int(bool(result.get('ok'))),'failed':[] if result.get('ok') else ['configured model not ready'],'result':result,
  'real_model_call':True,'model':model,'elapsed_sec':time.perf_counter()-start,'studio_content_accuracy_test':False,'model_downloaded':False}
except Exception as e:
 summary={'count':1,'passed':0,'failed':['configured model not ready'],'error_type':type(e).__name__,'elapsed_sec':time.perf_counter()-start,'studio_content_accuracy_test':False,'model_downloaded':False}
finally:
 if acquired:MODEL_WORK.release()
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2,default=str),'utf8');print(json.dumps({k:v for k,v in summary.items() if k!='result'},ensure_ascii=False));sys.exit(not summary['passed'])
