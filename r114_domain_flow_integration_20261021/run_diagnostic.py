"""Development-only typed diagnostics; never changes baseline/source/oracles."""
import collections,importlib.util,json,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent/'r113_multi_flow_benchmark_20261021';sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.engine import Engine
spec=importlib.util.spec_from_file_location('retained_r113_grader',B/'benchmark.py');g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
out=R/'verification'/sys.argv[1];out.mkdir(parents=True,exist_ok=False)
data=json.loads((B/'COMMON_READ_MODEL.json').read_text('utf8'));engine=Engine(data)
jobs=[json.loads(x) for x in (B/'EFFECTIVE_QUESTIONS_1400.jsonl').read_text('utf8').splitlines()];counts=collections.defaultdict(collections.Counter);started=time.monotonic()
with (out/'RESULTS.jsonl').open('x',encoding='utf8') as f:
    for j in jobs:
        r=engine.answer(j['question'],j['locale'],category=None if '--automatic' in sys.argv else j['category'],at=j['reference_time'],allow_llm=False)
        grade=g.grade(j,r);counts[j['category']]['questions']+=1;counts[j['category']]['passed']+=grade['passed'];counts[j['category']]['ambiguous']+=any(n['reason']=='typed_interpretation_unresolved' for n in r['needs']);counts[j['category']]['routing_exact']+=all(n['category']==j['category'] for n in r['needs'])
        f.write(json.dumps({'id':j['id'],'question':j['question'],'category':j['category'],'result':r,'grade':grade},ensure_ascii=False)+'\n')
summary={'development_diagnostic':True,'llm':False,'questions':len(jobs),'elapsed_sec':round(time.monotonic()-started,2),'scores':{c:dict(s) for c,s in counts.items()}}
(out/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False))
