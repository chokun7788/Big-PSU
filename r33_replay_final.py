import sys,json,time,collections,concurrent.futures,re
from pathlib import Path
import r33_full as runner
R=Path(Path(__file__).with_name('r33_report_path.txt').read_text().strip());run='final_G'
def selected(x):
    if any(g['corpus']=='master_gt_bilingual_multi_error_2000_20260929_r15.jsonl' or not g['passed'] for g in x['grades']):return True
    if re.search(r'\b(?:studio|gaming|house|home|minecraft|transfer|contact)\b|อีเมล|เบอร์โทร|สูบ|เปียด|คำพู|แพงกว่า|เช็ก|เช็ค',x['question'],re.I):return True
    return False
if __name__=='__main__':
    jobs=[];source_rows={}
    for line in (R/'candidate_D_all_results.jsonl').open(encoding='utf-8'):
        x=json.loads(line)
        if not selected(x):continue
        source_rows[x['key']]=x
        entries=[{k:v for k,v in g.items() if k in ('corpus','row_index','id','variant')}|{'case':g['expected']} for g in x['grades']]
        jobs.append(dict(key=x['key'],question=x['question'],locale=x['locale'],reference_date=x.get('reference_date',''),entries=entries))
    with (R/(run+'_replay_scope.json')).open('x',encoding='utf-8') as f:json.dump(dict(requests=len(jobs),grades=sum(len(j['entries']) for j in jobs),selection='All 2000 clean/noisy pairs, all failed D requests, and affected studio/hardware/contact/calendar-gap/payment vocabulary. Unreplayed D records retain D provenance.'),f,indent=2)
    print(json.dumps(dict(replay_requests=len(jobs))),flush=True);start=time.perf_counter()
    with (R/(run+'_replay_results.jsonl')).open('x',encoding='utf-8') as out,concurrent.futures.ProcessPoolExecutor(max_workers=6) as pool:
        fs=[pool.submit(runner.execute,j) for j in jobs]
        for n,f in enumerate(concurrent.futures.as_completed(fs),1):
            x=f.result();x['runtime_generation']='final_G';out.write(json.dumps(x,ensure_ascii=False)+'\n');out.flush()
            if n%200==0:print(json.dumps(dict(completed=n,remaining=len(jobs)-n,elapsed=round(time.perf_counter()-start))),flush=True)
    replacements={json.loads(l)['key']:json.loads(l) for l in (R/(run+'_replay_results.jsonl')).open(encoding='utf-8')}
    with (R/(run+'_all_results.jsonl')).open('x',encoding='utf-8') as out:
        for line in (R/'candidate_D_all_results.jsonl').open(encoding='utf-8'):
            old=json.loads(line);x=replacements.get(old['key'],old)
            if old['key'] not in replacements:x=dict(x,runtime_generation='candidate_D')
            out.write(json.dumps(x,ensure_ascii=False)+'\n')
    with (R/(run+'_replay_summary.json')).open('x',encoding='utf-8') as f:json.dump(dict(requests=len(jobs),elapsed_sec=time.perf_counter()-start,composite_requests=20327),f,indent=2)
    print('Final G replay complete',flush=True)
