import sys,os,json,time
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip());run=sys.argv[1];root=Path(sys.argv[2]) if len(sys.argv)>2 else p
sys.path.insert(0,str(root));sys.path.append(str(p));os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0';os.environ['PSU_INPUT_QUALITY_GUARD_MODE']='enforce';os.environ['PSU_INPUT_QUALITY_REPEAT_POLICY']='warn_and_continue'
from app.pipeline.engine import answer_question_pipeline_debug
from app.booking.live_status import _unavailable
from unittest.mock import patch
cases=json.loads((r/'focused_fixture_G6_source.json').read_text(encoding='utf-8'))['cases'];counts={'total':len(cases),'passed':0};start=time.perf_counter()
with (r/(run+'_source_G6_results.jsonl')).open('x',encoding='utf-8') as out,patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled fixture; no real occupancy oracle',error_code='fixture_offline')):
    for c in cases:
        if c['group']=='true_wrong_layout':
            from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
            guard=RuntimeInputQualityGuard.from_environment();d=guard.inspect(c['question'])
            errors=[] if d.should_short_circuit and d.mode==c['mode_prefix'] else ['guard_did_not_request_retype']
            counts['passed']+=not errors
            out.write(json.dumps({'case':c,'answer':d.message,'mode':d.mode,'quality':d.to_log_dict(),'scope':'server entry guard decision; actual HTTP separately verified','passed':not errors,'failures':errors},ensure_ascii=False)+'\n');out.flush()
            if errors:print(json.dumps({'id':c['id'],'failures':errors}),flush=True)
            continue
        a=answer_question_pipeline_debug(c['question'],locale=c['locale'],experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
        errors=['missing:'+v for v in c['must_contain'] if v.casefold() not in a.answer.casefold()]+['forbidden:'+v for v in c['must_not_contain'] if v.casefold() in a.answer.casefold()]
        if c.get('mode_prefix') and not a.mode.startswith(c['mode_prefix']):errors.append('mode_contract:'+a.mode)
        if c.get('required_source') and not any(c['required_source'] in str(h) for h in a.hits):errors.append('wrong_source')
        if c.get('not_mode_prefix') and a.mode.startswith(c['not_mode_prefix']):errors.append('forbidden_mode:'+a.mode)
        if not a.validation.ok:errors.append('validation_rejected')
        counts['passed']+=not errors
        record={'case':c,'answer':a.answer,'mode':a.mode,'hits':a.hits,'trace':[vars(t) for t in a.trace],'passed':not errors,'failures':errors};out.write(json.dumps(record,ensure_ascii=False)+'\n');out.flush()
        if errors:print(json.dumps({'id':c['id'],'question':c['question'],'failures':errors,'answer':a.answer},ensure_ascii=False),flush=True)
counts['elapsed']=time.perf_counter()-start
with (r/(run+'_source_G6_summary.json')).open('x',encoding='utf-8') as out:json.dump(counts,out,indent=2)
print(json.dumps(counts),flush=True)
