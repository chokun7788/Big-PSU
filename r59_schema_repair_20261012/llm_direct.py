"""Force bounded planning only to measure schema and semantic outcomes separately."""
import sys,json,time
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B.parent/'r58_examples_20sets_20261012'))
import experiment as t
from app.knowledge.common.planner import plan_fields
from app.knowledge.common.query_contract import strip_names
store=t.OneReleaseStore(t.DB).freeze();snap=store.frozen;records=snap['release']['records']
rows=[json.loads(l) for l in (t.B/'LLM_RESULTS.jsonl').read_text(encoding='utf-8').splitlines()]
out=B/sys.argv[1];out.mkdir(exist_ok=False);results=[]
with (out/'RESULTS.jsonl').open('x',encoding='utf-8') as f:
    for n,c in enumerate(rows,1):
        q=strip_names(c['question'],[c['rid']],snap['release']['names']);audit=[];start=time.perf_counter()
        plan=plan_fields(q,records,[c['rid']],diagnostic=audit.append)
        fields=set(plan['requested_fields']) if plan else set();expected=set(c['expected_fields'])
        raw=set(audit[0].get('proposal',{}).get('requested_fields',[])) if audit else set()
        r={'id':c['id'],'kind':c['kind'],'lang':c['lang'],'style':c['style'],'question':q,'expected_fields':c['expected_fields'],'plan':plan,'audit':audit,'selected_expected_fields':expected<=fields,'extra_fields':sorted(fields-expected),'raw_exact_fields':raw==expected,'elapsed':time.perf_counter()-start,'forced_planner_not_final_answer':True}
        f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush();results.append(r)
        if n%8==0:print('LLM '+str(n)+'/'+str(len(rows)),flush=True)
summary={'total':len(results),'transport_ok':sum(bool(r['audit'] and r['audit'][0]['transport_ok']) for r in results),'schema_accepted':sum(bool(r['audit'] and r['audit'][0]['schema_accepted']) for r in results),'requested_fields_recall_pass':sum(r['selected_expected_fields'] for r in results),'exact_fields_pass':sum(r['selected_expected_fields'] and not r['extra_fields'] for r in results),'raw_exact_fields_pass':sum(r['raw_exact_fields'] for r in results),'invalid_platform':sum(bool(r['audit'] and r['audit'][0].get('rejection_reason')=='invalid_platform') for r in results),'forced_planner_not_final_answer':True,'no_expected_fields_in_prompt':True,'llm':True,'wordpress':False}
(out/'SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary),flush=True)
