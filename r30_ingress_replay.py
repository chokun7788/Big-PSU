"""Replay Auto inputs with the same locale binding used by the HTTP server."""
import sys,os,json,time,concurrent.futures,collections
from pathlib import Path
os.environ['PSU_INPUT_QUALITY_GUARD_MODE']='enforce';os.environ['PSU_INPUT_QUALITY_REPEAT_POLICY']='warn_and_continue'
from r30_full_corpus import P,REPORT,plain,grade
def execute(job):
    from app.pipeline.engine import answer_question_pipeline_debug
    from app.core.locale import resolve_locale
    from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
    from app.pipeline.input_recovery import inspect_surface_input
    from app.booking.live_status import _unavailable
    from unittest.mock import patch
    global GUARD
    if 'GUARD' not in globals():GUARD=RuntimeInputQualityGuard.from_environment()
    quality=GUARD.inspect(job['question']);surface=inspect_surface_input(job['question'])
    decision=resolve_locale(job['question'],requested='auto',keyboard_layout_direction=quality.features.layout_direction,surface_language=surface.language if surface.should_review_intent else None)
    with patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled offline evaluation; no real booking oracle',error_code='fixture_offline')):
        result=answer_question_pipeline_debug(job['question'],locale='auto',locale_decision=decision,experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
    rows=[]
    for entry in job['entries']:
        try:g=grade(entry['expected'],result,entry['corpus'])
        except Exception as e:g={'passed':False,'failures':['grader_exception:'+str(e)]}
        rows.append({'corpus':entry['corpus'],'id':entry['id'],'variant':entry['variant'],'previous_passed':entry['passed'],**g})
    return {'key':job['key'],'question':job['question'],'previous_locale':job['previous_locale'],'locale_decision':plain(decision),'result':plain(result),'grades':rows,'scope':'HTTP-equivalent locale binding, static direct execution; LLM/semantic disabled'}
def main():
    assert (REPORT/'final_F_all_summary.json').exists()
    jobs=[]
    with (REPORT/'final_F_all_results.jsonl').open(encoding='utf-8') as f:
        for line in f:
            row=json.loads(line)
            if row['locale']=='auto':jobs.append({'key':row['key'],'question':row['question'],'previous_locale':row.get('result',{}).get('language'),'entries':row['grades']})
    counts=collections.defaultdict(collections.Counter);new_wrong=[];resolved=0;locale_changed=0
    with (REPORT/'HTTP_INGRESS_AUTO_REPLAY.jsonl').open('x',encoding='utf-8') as f,concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
        for n,r in enumerate(pool.map(execute,jobs),1):
            f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush()
            locale_changed+=((r.get('previous_locale') or {}).get('effective')!=r['locale_decision']['effective'])
            for g in r['grades']:
                counts[g['corpus']]['total']+=1;counts[g['corpus']]['passed']+=g['passed'];counts[g['corpus']]['previous_passed']+=g['previous_passed']
                resolved+=g['passed'] and not g['previous_passed']
                if g['previous_passed'] and not g['passed']:new_wrong.append({'question':r['question'],**g})
            if n%100==0:print(json.dumps({'completed':n,'total':len(jobs)}),flush=True)
    with (REPORT/'HTTP_INGRESS_AUTO_SUMMARY.json').open('x',encoding='utf-8') as f:json.dump({'auto_requests':len(jobs),'locale_changed_requests':locale_changed,'resolved_case_grades':resolved,'previous_pass_new_fail_grades':new_wrong,'by_corpus':counts,'scope':'ingress parity supplement; original full-sweep grades retained, not a production model benchmark'},f,ensure_ascii=False,indent=2)
    print(json.dumps({'total':len(jobs),'resolved_case_grades':resolved,'previous_pass_new_fail':len(new_wrong)}),flush=True)
if __name__=='__main__':main()
