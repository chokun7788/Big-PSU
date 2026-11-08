import sys,os,json,collections,time
from pathlib import Path
from unittest.mock import patch
from r30_full_corpus import P,REPORT,plain,read
from app.pipeline.engine import answer_question_pipeline_debug
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
from app.core.locale import resolve_locale
from app.pipeline.input_recovery import inspect_surface_input
from app.booking.live_status import _unavailable
os.environ['PSU_INPUT_QUALITY_GUARD_MODE']='enforce';os.environ['PSU_INPUT_QUALITY_REPEAT_POLICY']='warn_and_continue'
guard=RuntimeInputQualityGuard.from_environment();cases=read(P/'data/eval/keyboard_input_anomaly_ground_truth_500_20260830.jsonl');counts=collections.Counter();start=time.perf_counter()
with (REPORT/'final_G5_runtime_guard500_results.jsonl').open('x',encoding='utf-8') as out:
    for c in cases:
        q=c['observed_input'];quality=guard.inspect(q);surface=inspect_surface_input(q)
        decision=resolve_locale(q,requested='auto',keyboard_layout_direction=quality.locale_layout_direction,surface_language=surface.language if surface.should_review_intent else None)
        expected_block=bool(c['should_detect_keyboard_layout']) # repeat is warn/continue in this production profile
        counts['total']+=1;counts['applied_block_correct']+=expected_block==quality.should_short_circuit
        counts['original_label_block_match']+=bool(c['should_block_answer'])==quality.should_short_circuit
        counts['blocked']+=quality.should_short_circuit
        result=None
        if not quality.should_short_circuit:
            with patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled offline guard evaluation',error_code='fixture_offline')):
                result=answer_question_pipeline_debug(q,locale='auto',locale_decision=decision,experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
            counts['pipeline_executed']+=1;counts['validation_ok']+=result.validation.ok
        record={'case':c,'quality':quality.to_log_dict(),'locale':plain(decision),'applied_block_correct':expected_block==quality.should_short_circuit,'result':plain(result) if result else None,'scope':'production guard flow, static pipeline for continued inputs; no complete answer oracle and no live occupancy oracle; synthetic benchmark is not independent holdout'}
        out.write(json.dumps(record,ensure_ascii=False)+'\n');out.flush()
        if counts['total']%100==0:print(json.dumps(counts),flush=True)
with (REPORT/'final_G5_runtime_guard500_summary.json').open('x',encoding='utf-8') as f:json.dump({'counts':counts,'elapsed_sec':time.perf_counter()-start,'profile':'runtime published corpus, fixed thresholds, enforce layout / warn and continue repeat','raw_gold_expects_repeat_to_block':True,'answer_correctness_proven':False},f,ensure_ascii=False,indent=2)
print(json.dumps(counts),flush=True)
