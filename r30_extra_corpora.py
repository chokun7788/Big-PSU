import json,sys,os,collections,concurrent.futures,time
from pathlib import Path
os.environ['PSU_INPUT_QUALITY_GUARD_MODE']='enforce';os.environ['PSU_INPUT_QUALITY_REPEAT_POLICY']='warn_and_continue'
from r30_full_corpus import REPORT,P,plain
def execute(job):
    from app.pipeline.engine import answer_question_pipeline_debug
    from app.booking.live_status import _unavailable
    from unittest.mock import patch
    from tools.run_ground_truth_fast_eval import keyword_status,source_status
    with patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled offline extra corpus evaluation',error_code='fixture_offline')):
        result=answer_question_pipeline_debug(job['question'],locale='th',experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
    grades=[]
    for e in job['entries']:
        c=e['case'];errors=[]
        if e['observation_only']:level='pending_human_review_observation_only'
        else:
            level='legacy_keyword_source_mode_contract'
            ok,missing=keyword_status(result.answer,c.get('expected_keywords',[]))
            if not ok:errors+=['missing_keyword:'+v for v in missing]
            ok,missing=source_status(result.hits,c.get('expected_source_keywords',[]))
            if not ok:errors+=['missing_source:'+v for v in missing]
            if result.route.category!=c.get('category'):errors.append('wrong_category:'+result.route.category)
            if c.get('expected_mode_prefix') and not result.mode.startswith(c['expected_mode_prefix']):errors.append('legacy_mode_prefix:'+c['expected_mode_prefix'])
        if not result.validation.ok:errors.append('validation_rejected')
        grades.append({**e,'passed':not errors,'failures':errors,'level':level})
    return {'question':job['question'],'result':plain(result),'grades':grades}
def main():
    inventory=json.loads((REPORT/'extra_corpus_inventory.json').read_text(encoding='utf-8'));jobs={};coverage=[];parent_rows=None
    for entry in inventory:
        f=P/entry['file'];rows=[json.loads(l) for l in f.read_text(encoding='utf-8').splitlines() if l.strip()]
        if f.name=='ground_truth_competition_all_games_v2_diverse.jsonl':parent_rows=rows
        if 'competition_by_game_v2' in str(f) and f.name!='ground_truth_competition_all_games_v2_diverse.jsonl' and parent_rows and all(c in parent_rows for c in rows):
            coverage.append({'file':entry['file'],'rows':len(rows),'status':'exact_row_subset_alias','alias_of':'ground_truth_competition_all_games_v2_diverse.jsonl'});continue
        observation='human_review' in entry['file'];coverage.append({'file':entry['file'],'rows':len(rows),'status':'observations_no_human_oracle' if observation else 'evaluated'})
        for i,c in enumerate(rows):
            q=c['question'];jobs.setdefault(q,{'question':q,'entries':[]})['entries'].append({'corpus':f.name,'id':c.get('id') or c.get('review_id',i),'case':c,'observation_only':observation})
    start=time.perf_counter();counts=collections.defaultdict(collections.Counter)
    with (REPORT/'EXTRA_CORPUS_RESULTS.jsonl').open('x',encoding='utf-8') as f,concurrent.futures.ProcessPoolExecutor(max_workers=2) as pool:
        for n,row in enumerate(pool.map(execute,jobs.values()),1):
            f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
            for g in row['grades']:counts[g['corpus']]['total']+=1;counts[g['corpus']]['passed']+=g['passed']
            if n%100==0:print(json.dumps({'completed':n,'total':len(jobs)}),flush=True)
    with (REPORT/'EXTRA_CORPUS_SUMMARY.json').open('x',encoding='utf-8') as f:json.dump({'coverage':coverage,'unique_requests':len(jobs),'by_corpus':counts,'elapsed':time.perf_counter()-start,'scope':'source keyword and legacy mode contracts; empty human review rows are observations, not correct answer proof'},f,ensure_ascii=False,indent=2)
    print(json.dumps({'unique_requests':len(jobs),'by_corpus':counts}),flush=True)
if __name__=='__main__':main()
