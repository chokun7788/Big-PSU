import json,sys,os,time
from pathlib import Path
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(project));report=Path((root/'r30_report_path.txt').read_text(encoding='utf-8').strip());run=sys.argv[1]
os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
if len(sys.argv)>3:
    os.environ['PSU_INPUT_QUALITY_GUARD_MODE']='enforce';os.environ['PSU_INPUT_QUALITY_REPEAT_POLICY']='warn_and_continue'
from app.pipeline.engine import answer_question_pipeline_debug
from tools.run_master_ground_truth_eval import actual_status
cases=json.loads((report/('focused_fixture_v2.json' if len(sys.argv)>2 else 'focused_fixture_v1.json')).read_text(encoding='utf-8'))['cases'];records=[]
with (report/(run+'_focused_details.jsonl')).open('x',encoding='utf-8') as f:
    for c in cases:
        result=answer_question_pipeline_debug(c['question'],locale=c['locale'],experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
        errors=['missing:'+s for s in c['must_contain'] if s.casefold() not in result.answer.casefold()]+['forbidden:'+s for s in c['must_not_contain'] if s.casefold() in result.answer.casefold()]
        status=actual_status(result.mode,result.answer,result.route.category)
        if c['outcome']!=status:errors.append('wrong_outcome:'+status)
        if not result.validation.ok:errors.append('validation_rejected')
        r={'case':c,'answer':result.answer,'mode':result.mode,'category':result.route.category,'status':status,'elapsed_sec':result.elapsed,'failures':errors,'hits':result.hits,'trace':[vars(t) for t in result.trace]};records.append(r);f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush()
summary={'total':len(records),'passed':sum(not r['failures'] for r in records),'failures_by_group':{g:sum(bool(r['failures']) for r in records if r['case']['group']==g) for g in sorted({c['group'] for c in cases})}}
with (report/(run+'_focused_summary.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps(summary));sys.exit(summary['passed']!=summary['total'])
