"""Read-only frozen fixture evaluation; not a live accuracy/latency benchmark."""
import sys,json,collections,time,functools,multiprocessing
from pathlib import Path
B=Path(__file__).resolve().parent;BASE=B.parent
sys.path.insert(0,str(BASE/'r58_examples_20sets_20261012'))
import experiment as t
from app.knowledge.common import answer as module

def initialize():
    t.init_worker();original=module.named;fixed=t.store.frozen['release']['names']
    @functools.lru_cache(maxsize=10000)
    def cached(q,allow_fuzzy):
        ids,method=original(q,fixed,allow_fuzzy=allow_fuzzy);return tuple(ids),method
    def only_identical(q,names,*,allow_fuzzy=True):
        if names!=fixed:raise RuntimeError('immutable release changed')
        ids,method=cached(q,allow_fuzzy);return list(ids),method
    module.named=only_identical

def main():
    tag=sys.argv[1];out=B/tag;out.mkdir(exist_ok=False)
    qs=json.loads((t.B/'QUESTIONS_EXPECTED.json').read_text(encoding='utf-8'))
    if len(sys.argv)>2:qs=[q for q in qs if q['rid'].endswith(('_01','_03','_20'))]
    rows=[];start=time.time()
    with (out/'RESULTS.jsonl').open('x',encoding='utf-8') as f,multiprocessing.Pool(4,initializer=initialize) as pool:
        for n,r in enumerate(pool.imap_unordered(t.evaluate,qs,chunksize=8),1):
            rows.append(r);f.write(json.dumps(r,ensure_ascii=False)+'\n')
            if n%100==0:f.flush();print(f'{n}/{len(qs)} passed={sum(x["passed"] for x in rows)}',flush=True)
    baseline={r['id']:r for r in map(json.loads,(t.B/'content_final/ANSWERS_AND_DECISIONS.jsonl').read_text(encoding='utf-8').splitlines())}
    sums=collections.defaultdict(collections.Counter);regressions=[];improved=[]
    for r in rows:
        for k in ['overall','kind/'+r['kind'],'style/'+r['style'],'language/'+r['lang']]:sums[k]['pass' if r['passed'] else 'fail']+=1
        if r['passed'] and not baseline[r['id']]['passed']:improved.append(r['id'])
        if not r['passed'] and baseline[r['id']]['passed']:regressions.append(r)
    summary={'queries':len(qs),'counts':dict(sums),'regressions':len(regressions),'improved':len(improved),'seconds_not_latency':time.time()-start,'actual_common_answerer':True,'llm':False,'live_wordpress':False,'test_only_cache':'Identical (question, allow_fuzzy) against immutable full names, never expected fields','regression_not_holdout':True}
    for name,obj in [('SUMMARY.json',summary),('FAILURES.json',[r for r in rows if not r['passed']]),('REGRESSIONS.json',regressions)]:
        (out/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False),flush=True)
if __name__=='__main__':multiprocessing.freeze_support();main()
