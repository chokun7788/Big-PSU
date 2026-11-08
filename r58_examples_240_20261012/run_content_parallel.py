"""Resume completed demo queries; evaluate independent remaining cases with 4 CPU workers.
No production file edits, LLM calls or external API requests.
"""
import json,time,statistics,collections,multiprocessing
import build_and_test as task
from run_content_fast import OneReleaseStore
def initialize():
    global store,records,answerer
    store=OneReleaseStore(task.DB).freeze()
    if not store.frozen['allow_demo']:raise RuntimeError('Refuse non-demo DB')
    records=store.frozen['release']['records'];answerer=task.CommonAnswerer(store)
def evaluate(c):
    start=time.perf_counter()
    try:
        result=answerer.answer(c['question'],locale=c['lang'],history=c['history'],at=task.AT)
        ok,reasons=task.score(result,c,records)
        return {**c,'passed':ok,'reasons':reasons,'answer':result.answer if result else None,'mode':result.mode if result else None,'decision':result.decision_artifact if result else None,'evidence':result.hits if result else [],'elapsed_seconds':time.perf_counter()-start,'exception':None}
    except Exception:
        return {**c,'passed':False,'reasons':['exception'],'answer':None,'exception':task.traceback.format_exc(),'elapsed_seconds':time.perf_counter()-start}
def main():
    root=task.BASE;rec=OneReleaseStore(task.DB).freeze().frozen['release']['records'];allcases=task.cases(rec)
    prior={}
    for line in (root/'content_round2/ANSWERS_AND_DECISIONS.jsonl').read_text(encoding='utf-8').splitlines():
        try:r=json.loads(line);prior[r['id']]=r
        except json.JSONDecodeError:pass
    folder=root/'content_final';folder.mkdir(exist_ok=False);task.BASE=folder
    task.filejson('QUESTIONS_EXPECTED.json',allcases)
    task.filejson('EVALUATION_SCOPE.json',{'warning':task.WARNING,'immutable_demo_release':True,'actual_common_answerer':True,'epoch_checked_per_answer':True,'resumed_complete_cases':len(prior),'workers':4,'llm':False,'live_wordpress':False,'not_a_latency_benchmark':True})
    missing=[c for c in allcases if c['id'] not in prior];results=dict(prior)
    with (folder/'ANSWERS_AND_DECISIONS.jsonl').open('x',encoding='utf-8') as log:
        for r in prior.values():log.write(json.dumps(r,ensure_ascii=False)+'\n')
        with multiprocessing.Pool(4,initializer=initialize) as pool:
            for n,r in enumerate(pool.imap(evaluate,missing,chunksize=8),len(prior)+1):
                results[r['id']]=r;log.write(json.dumps(r,ensure_ascii=False)+'\n')
                if n%100==0:log.flush();print(f'completed {n}/{len(allcases)}',flush=True)
    ordered=[results[c['id']] for c in allcases];summary=collections.defaultdict(collections.Counter);fails=[]
    for r in ordered:
        for d in [('overall','all'),('kind',r['kind']),('language',r['lang']),('style',r['style']),('kind_style',r['kind']+'/'+r['style'])]:summary['/'.join(d)]['pass' if r['passed'] else 'fail']+=1
        if not r['passed']:fails.append(r)
    stats={k:dict(v) for k,v in summary.items()};task.filejson('SUMMARY.json',stats);task.filejson('FAILURES.json',fails)
    with (folder/'SUMMARY_BY_CATEGORY.csv').open('x',encoding='utf-8-sig',newline='') as f:
        w=task.csv.writer(f);w.writerow(['category','records','pass','fail'])
        for k in task.ORDER:w.writerow([k,10,summary['kind/'+k]['pass'],summary['kind/'+k]['fail']])
    print(json.dumps({'completed':len(ordered),'overall':stats['overall/all'],'failed':len(fails)}),flush=True)
if __name__=='__main__':multiprocessing.freeze_support();main()
