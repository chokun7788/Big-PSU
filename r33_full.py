"""Full final sweep using the server's classified locale binding."""
import sys,os,time,json
from datetime import date
from unittest.mock import patch
import r33_full_corpus as full

def execute(job):
    from app.pipeline.engine import answer_question_pipeline_debug
    from app.core.locale import resolve_locale
    from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
    from app.pipeline.input_recovery import inspect_surface_input
    from app.booking.live_status import _unavailable
    global GUARD
    if 'GUARD' not in globals():GUARD=RuntimeInputQualityGuard.from_environment()
    start=time.perf_counter();q=job['question'];loc=job['locale'];ref=job['reference_date']
    try:
        quality=GUARD.inspect(q);surface=inspect_surface_input(q)
        decision=resolve_locale(q,requested=loc,keyboard_layout_direction=quality.locale_layout_direction,surface_language=surface.language if surface.should_review_intent else None)
        kw=dict(locale=loc,locale_decision=decision,experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
        with patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled offline evaluation; no real booking oracle',error_code='fixture_offline')), patch('app.runtime.fast_answer.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled offline evaluation; no real booking oracle',error_code='fixture_offline')):
            if ref:
                with patch('app.booking.live_status.today_bangkok',return_value=date.fromisoformat(ref)):r=answer_question_pipeline_debug(q,**kw)
            else:r=answer_question_pipeline_debug(q,**kw)
        grades=[]
        for entry in job['entries']:
            try:g=full.grade(entry['case'],r,entry['corpus'])
            except Exception as e:g={'passed':False,'failures':['grader_exception:'+type(e).__name__+':'+str(e)],'evidence_level':'grader_error'}
            grades.append({k:v for k,v in entry.items() if k!='case'}|{'expected':entry['case'],**g})
        return {'key':job['key'],'question':q,'locale':loc,'reference_date':ref,'elapsed_wall':time.perf_counter()-start,'result':full.plain(r),'grades':grades,'binding':'HTTP-equivalent classified layout direction and surface review'}
    except Exception as e:return {'key':job['key'],'question':q,'locale':loc,'exception':type(e).__name__+':'+str(e),'grades':[{k:v for k,v in x.items() if k!='case'}|{'passed':False,'failures':['pipeline_exception'],'expected':x['case']} for x in job['entries']]}

if __name__=='__main__':
    full.execute=execute
    full.main()
