import json,collections,time
from pathlib import Path
from types import SimpleNamespace
from r30_full_corpus import REPORT,grade
counts=collections.defaultdict(collections.Counter);failures=collections.Counter();changed=[];start=time.perf_counter();n=0
with (REPORT/'final_F_rescored_all_results.jsonl').open('x',encoding='utf-8') as out,(REPORT/'final_F_all_results.jsonl').open(encoding='utf-8') as inp:
    for line in inp:
        row=json.loads(line);n+=1
        for g in row['grades']:
            if any('grader_exception:TypeError:startswith' in v for v in g['failures']):
                raw=row['result'];r=SimpleNamespace(**raw);r.route=SimpleNamespace(**raw['route']);r.validation=SimpleNamespace(**raw['validation']);r.trace=[SimpleNamespace(**v) for v in raw['trace']]
                r.universal_intent=SimpleNamespace(**raw['universal_intent']) if raw.get('universal_intent') else None
                r.language=SimpleNamespace(**raw['language']) if raw.get('language') else None
                old={'passed':g['passed'],'failures':g['failures'],'evidence_level':g.get('evidence_level')};new=grade(g['expected'],r,g['corpus']);g.update(new);g['original_grader_result']=old
                changed.append({'corpus':g['corpus'],'id':g['id'],'old':old,'new':new})
            counts[g['corpus']]['total']+=1;counts[g['corpus']]['passed']+=g['passed'];failures.update(g['failures'])
        out.write(json.dumps(row,ensure_ascii=False)+'\n')
with (REPORT/'final_F_rescored_all_summary.json').open('x',encoding='utf-8') as f:json.dump({'unique_requests':n,'by_corpus':counts,'failure_counts':failures,'grading_elapsed_sec':time.perf_counter()-start,'pipeline_reexecuted':False,'original_results_retained':True,'grader_corrections':changed,'scope':'supports the list of allowed mode prefixes, same native contract, no Gold or output rewriting'},f,ensure_ascii=False,indent=2)
print(json.dumps({'requests':n,'grader_corrections':len(changed),'passed_after_correction':sum(x['new']['passed'] for x in changed)}),flush=True)
