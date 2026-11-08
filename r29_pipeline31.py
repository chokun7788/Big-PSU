import json,os,sys,copy,time
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from unittest.mock import patch
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(project));report=Path((root/'r29_report_path.txt').read_text(encoding='utf-8').strip())
os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0';os.environ['PSU_LIVE_BOOKING_ENABLED']='1';os.environ['PSU_LIVE_BOOKING_FETCH_MODE']='wordpress';os.environ['PSU_LIVE_BOOKING_CACHE_SEC']='0'
from app.pipeline.engine import answer_question_pipeline_debug
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
from tools.run_master_ground_truth_eval import actual_status,expected_status_ok,contains_contract
from tests.test_available_equipment_only_20261001 import fixture
from app.booking.live_status import reset_live_booking_cache
guard=RuntimeInputQualityGuard.from_environment();guard.mode='enforce';guard.repeat_policy='warn_and_continue'
cases=[c for c in json.loads((report/'blocked36_fixture.json').read_text(encoding='utf-8'))['cases'] if not c['expected_blocked']]
records=[]
run=sys.argv[1] if len(sys.argv)>1 else 'B'
with (report/f'pipeline31_{run}_details.jsonl').open('x',encoding='utf-8') as output:
    for c in cases:
        gold=c['source_gold'];pair={}
        for form,q in [('clean',c['clean_question']),('noisy',c['question'])]:
            decision=guard.inspect(q);assert not decision.should_short_circuit,(c['id'],q)
            reset_live_booking_cache()
            with patch('app.calendar.service_calendar.now_bangkok',return_value=datetime(2026,10,1,14,30,tzinfo=ZoneInfo('Asia/Bangkok'))),patch('app.booking.wordpress_status.fetch_wordpress_status',return_value=fixture()) as fetch:
                result=answer_question_pipeline_debug(q,locale=c['locale'],experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
            status=actual_status(result.mode,result.answer,result.route.category)
            _,failures=contains_contract(result.answer,gold.get('answer_contract') or {})
            if result.route.category not in gold['expected_route_categories']:failures.append('legacy_route_mismatch:'+result.route.category)
            if not expected_status_ok(gold['expected_answer_status'],status,result.mode):failures.append('legacy_status_mismatch:'+status)
            if not result.validation.ok:failures.append('validation_rejected')
            pair[form]={'question':q,'answer':result.answer,'mode':result.mode,'route':result.route.category,'status':status,'elapsed':result.elapsed,'failures':failures,'legacy_passed':not failures,'hits':result.hits,'trace':[vars(t) for t in result.trace],'guard':decision.to_log_dict(),'mock_live_calls':fetch.call_count}
        r={'id':c['id'],'locale':c['locale'],'domain':c['domain'],'expected':gold,'clean':pair['clean'],'noisy':pair['noisy'],'answers_identical':pair['clean']['answer']==pair['noisy']['answer'],'scope':'legacy route/status/content contracts are weak or dated; clean parity not independent correctness; fixture booking only'}
        records.append(r);output.write(json.dumps(r,ensure_ascii=False)+'\n');output.flush()
        print(json.dumps({'id':c['id'],'clean_passed':pair['clean']['legacy_passed'],'noisy_passed':pair['noisy']['legacy_passed'],'same_answer':r['answers_identical']},ensure_ascii=False),flush=True)
summary={'total':len(records),'guard_noisy_passed':len(records),'legacy_clean_passed':sum(r['clean']['legacy_passed'] for r in records),'legacy_noisy_passed':sum(r['noisy']['legacy_passed'] for r in records),'identical_answers':sum(r['answers_identical'] for r in records),'new_noisy_failures_when_clean_passed':[r['id'] for r in records if r['clean']['legacy_passed'] and not r['noisy']['legacy_passed']],'scope':'31 source-labelled ordinary questions; 62 clean/noisy responses; requires manual/source review; booked/free uses fixture, real oracle deferred'}
with (report/f'pipeline31_{run}_summary.json').open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False))
