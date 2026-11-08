"""Replay questions that can see the changed CS2 pause contract; retain other rows with provenance."""
import json,collections,re,concurrent.futures,time,hashlib
from pathlib import Path
import r31_full as runner
f=runner.full;r=f.REPORT
def main():
    freeze=json.loads((r/'app_freeze_final_C.json').read_text());assert all(hashlib.sha256((f.P/k).read_bytes()).hexdigest()==v for k,v in freeze.items())
    initial=json.loads((r/'final_B_all_summary.json').read_text());counts=collections.defaultdict(collections.Counter);failures=collections.Counter();seen=set();affected=[];total=0
    def account(row):
        nonlocal total
        assert row['key'] not in seen;seen.add(row['key']);total+=len(row['grades'])
        for g in row['grades']:counts[g['corpus']]['total']+=1;counts[g['corpus']]['passed']+=g['passed'];failures.update(g['failures'])
    started=time.perf_counter()
    with (r/'final_C_all_results.jsonl').open('x',encoding='utf-8') as out:
        for name in initial['raw_parts']:
            for line in (r/name).open(encoding='utf-8'):
                x=json.loads(line);z=x.get('result',{});q=x['question']
                # Selection uses raw + normalized text + actual route. Include
                # all game comparisons and historical competition pathways.
                normalized=str(z.get('entities',{}).get('raw',{}).get('normalized_query',''))
                selected=bool(re.search(r'pause|timeout|หยุดเกม|เวลานอก',q+' '+normalized,re.I))
                if selected:
                    affected.append(dict(key=x['key'],question=q,locale=x['locale'],reference_date=x.get('reference_date',''),entries=[{k:v for k,v in g.items() if k in ['corpus','row_index','id','variant']}|{'case':g['expected']} for g in x['grades']]))
                else:
                    x['execution_provenance']='r31 A/B unaffected by local technical-timeout suppression; V2 rescored separately';account(x);out.write(json.dumps(x,ensure_ascii=False)+'\n')
        print(json.dumps(dict(reexecutions=len(affected),retained=len(seen))),flush=True)
        with concurrent.futures.ProcessPoolExecutor(max_workers=6) as pool:
            futures=[pool.submit(runner.execute,j) for j in affected]
            for n,future in enumerate(concurrent.futures.as_completed(futures),1):
                x=future.result();x['execution_provenance']='r31 C local pause/timeout replay';account(x);out.write(json.dumps(x,ensure_ascii=False)+'\n');out.flush()
                if n%200==0:print(json.dumps(dict(replayed=n,remaining=len(affected)-n)),flush=True)
    assert len(seen)==20327 and total==55583
    with (r/'final_C_all_summary.json').open('x',encoding='utf-8') as out:json.dump(dict(unique_requests=len(seen),case_grades=total,reexecuted_requests=len(affected),retained_previous_requests=20327-len(affected),raw_parts=['final_C_all_results.jsonl'],by_corpus=counts,failure_counts=failures,elapsed_sec=time.perf_counter()-started,deferred_sessions=12,scope='Full A sweep + conservative B competition replay + local C pause/timeout replay. C was not a new execution of all 20327 inputs. Same corpus and unchanged data.'),out,ensure_ascii=False,indent=2)
    print(json.dumps(dict(completed=len(seen),replayed=len(affected))),flush=True)
if __name__=='__main__':main()
