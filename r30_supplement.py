import sys,os,json,hashlib,importlib.util,collections,dataclasses,time
from pathlib import Path
from unittest.mock import patch
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(p));r=Path(Path('r30_report_path.txt').read_text().strip())
os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
from r30_full_corpus import plain,grade,read
# Independent source/builder provenance comparison, retain all Gold files.
spec=importlib.util.spec_from_file_location('r30_gold_builder',p/'tools/build_master_ground_truth_10000.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
built=b.build();diffs=[]
for loc in ('th','en'):
    stored=read(p/f'data/eval/master_ground_truth_{loc}_5000_v2.jsonl');generated=[v for v in built if v['locale']==loc]
    for n,(old,new) in enumerate(zip(stored,generated)):
        if old!=new:diffs.append({'locale':loc,'index':n,'id':old['id'],'changed_fields':{k:{'stored':old.get(k),'builder_now':new.get(k)} for k in old.keys()|new.keys() if old.get(k)!=new.get(k)}})
if not (r/'gold_builder_drift.json').exists():
    with (r/'gold_builder_drift.json').open('x',encoding='utf-8') as f:json.dump({'count':len(diffs),'differences':diffs,'decision':'frozen Gold retained; deterministic rebuild identity is not guaranteed when builder reads changing source data'},f,ensure_ascii=False,indent=2)
# Session turns: run context resolver for every turn, not just the first question.
from app.pipeline.engine import answer_question_pipeline_debug
from app.session.context_resolver import resolve_question_with_context
from tools.run_broad_usage_eval_v1 import _validate_single,_append_history
from app.booking.live_status import _unavailable
inventory=json.loads((r/'sweep_A_inventory.json').read_text(encoding='utf-8'));records=[]
with patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled offline evaluation',error_code='fixture_offline')):
    for entry in inventory['session_cases']:
        c=entry['case'];history=[]
        for i,turn in enumerate(c['turns']):
            resolved=resolve_question_with_context(turn['question'],history[-12:]);q=resolved.resolved_question
            result=answer_question_pipeline_debug(q,locale='auto',experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
            errors=_validate_single(turn,result)
            records.append({'corpus':entry['corpus'],'id':c['id'],'turn':i,'question':turn['question'],'resolved_question':q,'passed':not errors,'failures':errors,'result':plain(result),'context':plain(resolved)})
            _append_history(history,turn['question'],q,result)
with (r/((sys.argv[1]+'_' if len(sys.argv)>1 else '')+'all_session_turns.jsonl')).open('x',encoding='utf-8') as f:
    for x in records:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print(json.dumps({'builder_drift_rows':len(diffs),'session_turns':len(records),'session_passed':sum(x['passed'] for x in records)},ensure_ascii=False))
