import sys,os,json
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B.parent/'r58_examples_20sets_20261012'))
import experiment as t
from evaluate import score
from app.pipeline.engine import answer_question_pipeline_debug
os.environ['PSU_KNOWLEDGE_DB']=str(t.DB);os.environ['PSU_COMMON_ALLOW_DEMO']='1'
records=t.CommonStore(t.DB).snapshot()['release']['records']
rows=json.loads((B/'DEVELOPMENT.json').read_text(encoding='utf-8'))
focus=[r for r in rows if r['style']=='clean_new' and r['kind'] in {'game','service','competition','procedure','live_binding','person'}]
out=B/'pipeline_verified';out.mkdir(exist_ok=False);result=[]
with (out/'RESULTS.jsonl').open('x',encoding='utf-8') as f:
    for c in focus:
        c=dict(c);c['rid']=t.rid(c['kind'],c['profile']);c['question']=records[c['rid']]['aliases'][c['lang']][0]+' '+c['phrase']
        ans=answer_question_pipeline_debug(c['question'],locale=c['lang'],experimental_allow_llm=True,experimental_rag_fallback=False,global_timeout_sec=30)
        ok,why,quality=score(ans,c,records)
        r={**c,'passed':ok,'reasons':why,'quality':quality,'answer':ans.answer,'decision':ans.decision_artifact,'mode':ans.mode};result.append(r);f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush()
        print(c['id']+' '+str(ok),flush=True)
summary={'cases':len(result),'passed':sum(r['passed'] for r in result),'failures':[r['id'] for r in result if not r['passed']],'actual_pipeline':True,'actual_llm':True,'live_wordpress':False,'no_fake_planner':True}
(out/'SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(summary)
