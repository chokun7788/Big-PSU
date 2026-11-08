import json,re,collections,concurrent.futures,time
from pathlib import Path
import r31_extra as extra
r=extra.REPORT
def main():
    old=json.loads((r/'R31_EXTRA_EXTRA_CORPUS_SUMMARY.json').read_text());counts=collections.defaultdict(collections.Counter);selected=[];keys=set();started=time.perf_counter()
    def account(row):
        assert row['question'] not in keys;keys.add(row['question'])
        for g in row['grades']:counts[g['corpus']]['total']+=1;counts[g['corpus']]['passed']+=g['passed']
    with (r/'R31_C_EXTRA_CORPUS_RESULTS.jsonl').open('x',encoding='utf-8') as out:
        for line in (r/'R31_EXTRA_EXTRA_CORPUS_RESULTS.jsonl').open(encoding='utf-8'):
            row=json.loads(line);normalized=str(row['result'].get('entities',{}).get('raw',{}).get('normalized_query',''))
            if re.search(r'cs2|counter|เคาน|pause|timeout|หยุดเกม|เวลานอก',row['question']+' '+normalized,re.I):selected.append(dict(question=row['question'],entries=[{k:g[k] for k in ['corpus','id','case','observation_only']} for g in row['grades']]))
            else:row['execution_provenance']='A extra unaffected by B/C pause changes';account(row);out.write(json.dumps(row,ensure_ascii=False)+'\n')
        print(json.dumps(dict(replayed=len(selected),retained=len(keys))),flush=True)
        with concurrent.futures.ProcessPoolExecutor(max_workers=3) as pool:
            for row in pool.map(extra.execute,selected):row['execution_provenance']='C CS2/pause extra replay';account(row);out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush()
    assert len(keys)==970
    with (r/'R31_C_EXTRA_CORPUS_SUMMARY.json').open('x',encoding='utf-8') as out:json.dump(dict(coverage=old['coverage'],unique_requests=len(keys),reexecuted_requests=len(selected),retained_A_requests=970-len(selected),by_corpus=counts,elapsed_sec=time.perf_counter()-started,scope='Original keyword/source/mode gates retained; observation rows are not human oracle; only affected queries reexecuted in C'),out,ensure_ascii=False,indent=2)
    print(json.dumps(dict(completed=len(keys),replayed=len(selected))),flush=True)
if __name__=='__main__':main()
