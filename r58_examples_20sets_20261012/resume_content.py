"""Resume without overwriting. Cache only repeated pure name searches in test memory."""
import experiment as t
import functools,json,multiprocessing,collections,time
from app.knowledge.common import answer as module
def initialize():
    t.init_worker()
    original=module.named
    fixed=t.store.frozen['release']['names']
    @functools.lru_cache(maxsize=10000)
    def computed(q):
        ids,method=original(q,fixed)
        return tuple(ids),method
    def repeated_only(q,names):
        # The full validated release stays immutable for this test run.
        if names!=fixed:raise RuntimeError('Names changed; cached test is invalid')
        ids,method=computed(q)
        return list(ids),method
    module.named=repeated_only
def main():
    folder=t.B/'content_final';folder.mkdir(exist_ok=False)
    qs=json.loads((t.B/'QUESTIONS_EXPECTED.json').read_text(encoding='utf-8'))
    records=t.CommonStore(t.DB).snapshot()['release']['records'];snap=t.CommonStore(t.DB).snapshot()
    old={};ignored=0
    for line in (t.B/'ANSWERS_AND_DECISIONS.jsonl').read_text(encoding='utf-8').splitlines():
        try:r=json.loads(line);old[r['id']]=r
        except json.JSONDecodeError:ignored+=1
    with (folder/'EVALUATION_SCOPE.json').open('x',encoding='utf-8') as f:json.dump({'actual_common_answerer':True,'llm':False,'live_wordpress':False,'not_latency_benchmark':True,'workers':4,'immutable_release_reused':True,'epoch_checked_each_answer':True,'retained_complete_cases':len(old),'ignored_partial_log_lines':ignored,'test_only_pure_name_cache':'Only exact same question and immutable full names map reuses original named() result. No expected fields, routing shortcuts or production code changes.'},f,ensure_ascii=False,indent=2)
    result=dict(old);missing=[c for c in qs if c['id'] not in old]
    with (folder/'ANSWERS_AND_DECISIONS.jsonl').open('x',encoding='utf-8') as f:
        for r in old.values():f.write(json.dumps(r,ensure_ascii=False)+'\n')
        with multiprocessing.Pool(4,initializer=initialize) as pool:
            for n,r in enumerate(pool.imap_unordered(t.evaluate,missing,chunksize=4),len(old)+1):
                result[r['id']]=r;f.write(json.dumps(r,ensure_ascii=False)+'\n')
                if n%100==0:f.flush();print(f'completed {n}/{len(qs)}',flush=True)
    sums=collections.defaultdict(collections.Counter)
    for r in result.values():
        for name in ['overall/all','style/'+r['style'],'kind/'+r['kind'],'language/'+r['lang'],'kind_style/'+r['kind']+'/'+r['style']]:sums[name]['pass' if r['passed'] else 'fail']+=1
    with (folder/'SUMMARY.json').open('x',encoding='utf-8') as f:json.dump({k:dict(v) for k,v in sums.items()},f,ensure_ascii=False,indent=2)
    with (folder/'FAILURES.json').open('x',encoding='utf-8') as f:json.dump(sorted([r for r in result.values() if not r['passed']],key=lambda r:r['id']),f,ensure_ascii=False,indent=2)
    assert len(result)==len(qs) and t.CommonStore(t.DB).still_current(snap)
    print('COMPLETE '+json.dumps({'queries':len(qs),'result':dict(sums['overall/all'])}),flush=True)
if __name__=='__main__':multiprocessing.freeze_support();main()
