import os,sys,json,time,collections,concurrent.futures
from pathlib import Path
ROOT=Path(__file__).parent;R=Path((ROOT/'r33_report_path.txt').read_text().strip());OLD=Path((ROOT/'r32_report_path.txt').read_text().strip())
import r33_full as runner
from app.core.intent_cue_recovery import recover_intent_cue_sequence
from tools.eval_contract_v2 import rescore_pair
P=runner.full.P
overlay={x['id']:x for x in map(json.loads,(P/'data/eval/typo_r16_contract_overlay_20260930.jsonl').read_text(encoding='utf-8').splitlines())}
run=sys.argv[1]
def job(x):
    exp=x['noisy']['expected'];return dict(key=x['id'],question=x['noisy']['question'],locale=x['locale'],reference_date=str(exp.get('metadata',{}).get('reference_date','')) if exp.get('domain')=='weekday_live_slots' else '',entries=[dict(corpus='master_gt_bilingual_multi_error_2000_20260929_r15.jsonl',id=x['id'],variant='noisy',row_index=0,case=exp)])
def execute(x):
    actual=runner.execute(job(x));z=actual.get('result',{});exp=x['noisy']['expected'];clean=x['score']['v2']['clean']
    cleanraw=x['clean']['result']
    def score_result(raw):return dict(actual_route=raw['route']['category'],mode=raw['mode'],answer=raw['answer'],latency_ok=raw['elapsed']<=exp.get('latency_ceiling_sec',20),passed=True)
    pair=rescore_pair(dict(**exp,clean=score_result(cleanraw),noisy=score_result(z),regression=False),overlay.get(x['id']))
    recovered,steps=recover_intent_cue_sequence(x['noisy']['question'])
    return dict(id=x['id'],locale=x['locale'],positive=x['positive_contract'],question=actual['question'],recovered=recovered,recoveries=runner.full.plain(steps),previous=x['noisy']['result'],result=z,score=pair,grades=actual['grades'])
if __name__=='__main__':
    rows=[json.loads(l) for l in (OLD/'REMAINING_107_FINAL13_DETAILED.jsonl').read_text(encoding='utf-8').splitlines()]
    start=time.perf_counter();records=[]
    with (R/(run+'_focus.jsonl')).open('x',encoding='utf-8') as out,concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for x in pool.map(execute,rows):
            records.append(x);out.write(json.dumps(x,ensure_ascii=False)+'\n');out.flush()
            print(json.dumps(dict(id=x['id'],passed=x['score']['v2']['noisy']['passed'],recovered=x['recovered'],mode=x['result']['mode'],answer=x['result']['answer'][:270]),ensure_ascii=False),flush=True)
    summary=dict(total=len(records),passed=sum(x['score']['v2']['noisy']['passed'] for x in records),positive_total=sum(x['positive'] for x in records),positive_passed=sum(x['positive'] and x['score']['v2']['noisy']['passed'] for x in records),elapsed=time.perf_counter()-start)
    (R/(run+'_focus_summary.json')).write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(summary)
