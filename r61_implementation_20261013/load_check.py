"""Warm local concurrent pipeline measurement on synthetic known-answer inputs."""
import sys,os,json,time,threading,statistics
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
B=Path(__file__).resolve().parent
sys.path.insert(0,str(B.parent/'r58_examples_20sets_20261012'));import experiment as t
sys.path.insert(0,str(B.parent/'r60_generalization_20261012'));from evaluate import score
from app.pipeline.engine import answer_question_pipeline_debug
os.environ['PSU_KNOWLEDGE_DB']=str(t.DB);os.environ['PSU_COMMON_ALLOW_DEMO']='1'
records=t.CommonStore(t.DB).snapshot()['release']['records']
cases=[r for r in json.loads((B/'DEVELOPMENT.json').read_text(encoding='utf-8')) if r['style']=='clean_new' and r['kind'] in {'game','procedure','competition','person'}]
result=[]
for clients in ([8] if len(sys.argv)>1 else [1,2,4,8]):
 barrier=threading.Barrier(clients)
 def work(index):
  c=dict(cases[index%len(cases)]);c['rid']=t.rid(c['kind'],c['profile']);c['question']=records[c['rid']]['aliases'][c['lang']][0]+' '+c['phrase']
  barrier.wait(timeout=10);start=time.perf_counter()
  answer=answer_question_pipeline_debug(c['question'],locale=c['lang'],experimental_allow_llm=True,experimental_rag_fallback=False,global_timeout_sec=19)
  elapsed=time.perf_counter()-start;ok,why,quality=score(answer,c,records)
  return {'clients':clients,'index':index,'id':c['id'],'seconds':elapsed,'passed':ok,'reasons':why,'answer':answer.answer,'decision':answer.decision_artifact}
 started=time.perf_counter()
 with ThreadPoolExecutor(max_workers=clients) as pool:rows=list(pool.map(work,range(clients)))
 values=sorted(r['seconds'] for r in rows);duration=time.perf_counter()-started
 summary={'clients':clients,'passed':sum(r['passed'] for r in rows),'requests':len(rows),'p50_sec':statistics.median(values),'p95_observed_sec':values[min(len(values)-1,int(.95*len(values)))],'max_sec':max(values),'requests_per_sec':len(rows)/duration,'small_sample':True}
 result.append({'summary':summary,'rows':rows});print(summary,flush=True)
with (B/('LOAD_RESULTS_QUEUE12.json' if len(sys.argv)>1 else 'LOAD_RESULTS.json')).open('x',encoding='utf-8') as f:json.dump({'actual_pipeline':True,'actual_llm':True,'synthetic':True,'warmth_not_independently_verified':True,'threads_not_browser_or_worker_process_capacity_proof':True,'runs':result},f,ensure_ascii=False,indent=2)
