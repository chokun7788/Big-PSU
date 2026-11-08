"""48 natural questions: 1 record per kind, Thai and English, real local LLM planner.
Does not enable legacy factual fallback or live WordPress for fictional records.
"""
import os,json,time
import build_and_test as task
os.environ['PSU_KNOWLEDGE_DB']=str(task.DB);os.environ['PSU_COMMON_ALLOW_DEMO']='1'
from app.knowledge.common.planner import plan_fields
from app.pipeline.llm_health import preflight_ollama,llm_health_snapshot
def main():
    model=os.getenv('PSU_KNOWLEDGE_LLM_MODEL','scb10x/typhoon2.5-qwen3-4b')
    warm=preflight_ollama(model=model,kind='demo_schema_preflight',timeout_sec=30,num_predict=1,num_ctx=3072)
    task.filejson('LLM_PREFLIGHT.json',warm)
    store=task.CommonStore(task.DB);records=store.snapshot()['release']['records'];reader=task.CommonAnswerer(store)
    qs=[c for c in task.cases(records) if c['style']=='natural' and c['rid'].endswith('_01')];rows=[]
    with (task.BASE/'LLM_SAMPLE_RESULTS.jsonl').open('x',encoding='utf-8') as log:
        for n,c in enumerate(qs,1):
            proposals=[]
            def traced(q,recs,ids):
                start=time.perf_counter();p=plan_fields(q,recs,ids);proposals.append({'checked_plan':p,'elapsed_seconds':time.perf_counter()-start});return p
            result=reader.answer(c['question'],locale=c['lang'],at=task.AT,planner=traced);ok,why=task.score(result,c,records)
            r={**c,'passed':ok,'reasons':why,'answer':result.answer if result else None,'decision':result.decision_artifact if result else None,'planner_attempts':proposals,'health_after':llm_health_snapshot()}
            rows.append(r);log.write(json.dumps(r,ensure_ascii=False)+'\n');log.flush();print(f'LLM sample {n}/48; passed={ok}; planner_attempts={len(proposals)}',flush=True)
    task.filejson('LLM_SAMPLE_SUMMARY.json',{'queries':len(rows),'pass':sum(r['passed'] for r in rows),'fail':sum(not r['passed'] for r in rows),'with_planner_attempt':sum(bool(r['planner_attempts']) for r in rows),'accepted_plans':sum(any(p['checked_plan'] for p in r['planner_attempts']) for r in rows),'model':model,'scope':'real local bounded schema planner; 1 example per kind per language; no legacy facts/live WordPress'})
if __name__=='__main__':main()
