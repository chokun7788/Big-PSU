"""Resume immutable completed rows after a process interruption; do not rerun or edit them."""
import json, collections, concurrent.futures, time, hashlib
from pathlib import Path
import r31_full as runner
f=runner.full

def main():
    r=f.REPORT
    freeze=json.loads((r/'app_freeze_final_A.json').read_text())
    assert all(hashlib.sha256((f.P/k).read_bytes()).hexdigest()==v for k,v in freeze.items())
    jobs={};rowsets={}
    for path in sorted([*(f.P/'data/eval').glob('*.json'),*(f.P/'data/eval').glob('*.jsonl'),*(f.P/'data/routing').glob('*eval*.jsonl')]):
        rows=f.read(path);name=path.name
        if not rows:continue
        fp=f.fingerprint(rows)
        if fp in rowsets:continue
        rowsets[fp]=name
        for index,c in enumerate(rows):
            if not isinstance(c,dict) or c.get('kind')=='session' or c.get('turns'):continue
            if 'noisy_question' in c:variants=[('clean',c['clean_question']),('noisy',c['noisy_question'])]
            elif 'noisy' in c:variants=[('clean',c['clean']),('noisy',c['noisy'])]
            elif c.get('observed_input'):continue
            else:
                q=c.get('question_en') or c.get('question')
                if not q:continue
                variants=[('question',q)]
            for variant,q in variants:
                loc=c.get('locale') or ('en' if 'question_en' in c or name.startswith('english_') else 'auto')
                ref=str((c.get('metadata') or {}).get('reference_date','')) if c.get('domain')=='weekday_live_slots' else ''
                key=f.fingerprint([q,loc,ref]);job=jobs.setdefault(key,dict(key=key,question=q,locale=loc,reference_date=ref,entries=[]))
                job['entries'].append(dict(corpus=name,row_index=index,id=str(c.get('id',index)),variant=variant,case=dict(c,question=q,locale=loc)))
    keys=set();counts=collections.defaultdict(collections.Counter);failures=collections.Counter();grades=0
    def account(row):
        nonlocal grades
        assert row['key'] not in keys
        assert row['key'] in jobs
        assert len(row['grades'])==len(jobs[row['key']]['entries'])
        keys.add(row['key']);grades+=len(row['grades'])
        for g in row['grades']:
            counts[g['corpus']]['total']+=1;counts[g['corpus']]['passed']+=g['passed'];failures.update(g['failures'])
    for line in (r/'final_A_all_results.jsonl').open(encoding='utf-8'):account(json.loads(line))
    completed=len(keys);remaining=[job for key,job in jobs.items() if key not in keys]
    assert len(jobs)==20327 and completed==18894 and len(remaining)==1433
    print(json.dumps(dict(completed_preserved=completed,remaining=len(remaining))),flush=True)
    started=time.perf_counter()
    with (r/'resume_A_results.jsonl').open('x',encoding='utf-8') as out,concurrent.futures.ProcessPoolExecutor(max_workers=6) as pool:
        for n,row in enumerate(pool.map(runner.execute,remaining,chunksize=1),1):
            account(row);out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush()
            if n%100==0:print(json.dumps(dict(resume_completed=n,remaining=len(remaining)-n)),flush=True)
    assert len(keys)==20327 and grades==55583
    summary=dict(unique_requests=len(keys),case_grades=grades,by_corpus=counts,failure_counts=failures,deferred_sessions=12,raw_parts=['final_A_all_results.jsonl','resume_A_results.jsonl'],preserved_rows=completed,newly_executed_rows=len(remaining),resume_elapsed_sec=time.perf_counter()-started,same_app_freeze='app_freeze_final_A.json')
    with (r/'complete_A_all_summary.json').open('x',encoding='utf-8') as out:json.dump(summary,out,ensure_ascii=False,indent=2)
    print(json.dumps(dict(completed=len(keys),grades=grades)),flush=True)

if __name__=='__main__':main()
