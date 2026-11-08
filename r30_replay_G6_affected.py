import json,collections,concurrent.futures,time,hashlib,re
from pathlib import Path
from r30_full_G import execute
from r30_full_corpus import P,REPORT
def related(row):
    # Broad conservative coverage includes all competition grades/routes and
    # CS2 mentions anywhere in the recorded raw/normalized/source trace.
    raw=json.dumps(row,ensure_ascii=False).casefold()
    return any(x in raw for x in ['competition_rule','cs2','counter-strike','counter strike','เคาน์เตอร์สไตรก์','เคาเตอร์สไตรก์'])
def main():
    a=json.loads((REPORT/'app_freeze_G5b.json').read_text());b=json.loads((REPORT/'app_freeze_G6.json').read_text())
    changed=[k for k in a if a[k]!=b[k]];assert changed==['app/pipeline/competition_detail.py'],changed
    jobs=[];start=time.perf_counter()
    for line in (REPORT/'final_G5_all_results.jsonl').open(encoding='utf-8'):
        row=json.loads(line)
        if related(row):
            entries=[{k:g[k] for k in ['corpus','row_index','id','variant']}|{'case':g['expected']} for g in row['grades']]
            jobs.append({k:row[k] for k in ['key','question','locale','reference_date']}|{'entries':entries})
    with (REPORT/'final_G6_affected_results.jsonl').open('x',encoding='utf-8') as out,concurrent.futures.ProcessPoolExecutor(max_workers=6) as pool:
        for n,row in enumerate(pool.map(execute,jobs),1):
            row['execution_provenance']='G6 affected competition replay';out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush()
            if n%300==0:print(json.dumps({'completed':n,'affected_total':len(jobs)}),flush=True)
    updated={json.loads(l)['key']:json.loads(l) for l in (REPORT/'final_G6_affected_results.jsonl').open(encoding='utf-8')};counts=collections.defaultdict(collections.Counter);failures=collections.Counter();n=0;deltas=[]
    with (REPORT/'final_G6_all_results.jsonl').open('x',encoding='utf-8') as out:
        for line in (REPORT/'final_G5_all_results.jsonl').open(encoding='utf-8'):
            old=json.loads(line);row=updated.get(old['key'],old)
            if old['key'] not in updated:row['execution_provenance']='G5 complete sweep, unaffected by the only G6 CS2 concept change'
            else:
                changes=[{'corpus':a['corpus'],'id':a['id'],'variant':a['variant'],'before_passed':a['passed'],'after_passed':b['passed'],'before_failures':a['failures'],'after_failures':b['failures']} for a,b in zip(old['grades'],row['grades']) if a['passed']!=b['passed']]
                if changes or old.get('result',{}).get('answer')!=row.get('result',{}).get('answer'):deltas.append({'key':row['key'],'question':row['question'],'before_answer':old.get('result',{}).get('answer'),'after_answer':row.get('result',{}).get('answer'),'grade_changes':changes})
            out.write(json.dumps(row,ensure_ascii=False)+'\n');n+=1
            for g in row['grades']:counts[g['corpus']]['total']+=1;counts[g['corpus']]['passed']+=g['passed'];failures.update(g['failures'])
    with (REPORT/'final_G6_all_summary.json').open('x',encoding='utf-8') as out:json.dump({'unique_requests':n,'by_corpus':counts,'failure_counts':failures,'scope':'G5 complete sweep + conservative G6 affected competition replay; not a new 20327-input G6 run','reexecuted_requests':len(jobs),'replay_elapsed_sec':time.perf_counter()-start,'only_production_file_changed_from_G5b':changed,'deferred_sessions':12},out,ensure_ascii=False,indent=2)
    with (REPORT/'final_G6_inventory.json').open('x',encoding='utf-8') as out:out.write((REPORT/'final_G5_inventory.json').read_text(encoding='utf-8'))
    with (REPORT/'G5_TO_G6_REPLAY_DIFFERENCES.json').open('x',encoding='utf-8') as out:json.dump(deltas,out,ensure_ascii=False,indent=2)
    print(json.dumps({'unique_current_coverage':n,'replayed_requests':len(jobs),'changed_grade_requests':len(deltas),'newly_failed_grades':sum(not g['after_passed'] for d in deltas for g in d['grade_changes'])}),flush=True)
if __name__=='__main__':main()
