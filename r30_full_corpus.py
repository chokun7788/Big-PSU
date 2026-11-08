"""Read every local evaluation corpus; never modify input or historical logs."""
import os,sys,json,time,hashlib,dataclasses,collections,concurrent.futures
from pathlib import Path
from unittest.mock import patch
from datetime import date
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
ROOT=Path(__file__).parent
REPORT=Path((ROOT/'r30_report_path.txt').read_text().strip())
sys.path.insert(0,str(P));sys.path.insert(0,str(ROOT/'work/r30_test_dependencies'))
os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0';os.environ['PYTHONDONTWRITEBYTECODE']='1'
if len(sys.argv)>1 and sys.argv[1]!='sweep_A':
    os.environ['PSU_INPUT_QUALITY_GUARD_MODE']='enforce'
    os.environ['PSU_INPUT_QUALITY_REPEAT_POLICY']='warn_and_continue'
def plain(v):
    if dataclasses.is_dataclass(v):return {k:plain(x) for k,x in dataclasses.asdict(v).items()}
    if isinstance(v,dict):return {k:plain(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [plain(x) for x in v]
    return v
def fingerprint(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def read(f):
    d=json.loads(f.read_text(encoding='utf-8-sig')) if f.suffix=='.json' else [json.loads(l) for l in f.read_text(encoding='utf-8-sig').splitlines() if l.strip()]
    if isinstance(d,list):return d
    return d.get('cases',[]) if isinstance(d,dict) else []
def grade(c,r,name):
    from tools.run_master_ground_truth_eval import actual_status,expected_status_ok,contains_contract
    from tools.eval_contract_v2 import contract_matches,answer_outcome,status_matches
    errs=[];level='route_outcome_only';native=None
    response={'answer':r.answer,'mode':r.mode,'category':r.route.category,'hits':r.hits,'valid':r.validation.ok}
    if 'required_clauses' in c:
        from tools.run_competition_contract_r27 import check_content_contract
        errs=check_content_contract(c,response);level='complete_clause_content'
    elif 'clauses' in c and 'sources' in c:
        from tools.run_competition_composition_r28 import check
        errs=check(c,response);level='complete_clause_composition'
    elif 'expected_game_id' in c:
        import tools.run_competition_rules_rag_ground_truth as g
        with patch.object(g,'answer_question_pipeline_debug',return_value=r):native=g.evaluate_case(c,allow_llm=False,rag_fallback=True,include_trace=False)
        errs=native['failures'];level='competition_legacy_evidence'
    elif 'source_keywords' in c and 'min_score' in c:
        import tools.run_answer_quality_eval as g
        with patch.object(g,'answer_question_pipeline_debug',return_value=r):native=g._evaluate_case(c,allow_llm=False)
        if not native['passed']:errs=['quality_score_or_required_gate_failed',*native['missing'],*native['forbidden']]
        level='native_answer_quality'
    else:
        cats=c.get('expected_route_categories') or c.get('expected_categories') or c.get('expected_category') or []
        if isinstance(cats,str):cats=[cats]
        if cats and r.route.category not in cats:errs.append('route:'+r.route.category+' expected:'+str(cats))
        status=actual_status(r.mode,r.answer,r.route.category);expected=c.get('expected_answer_status') or c.get('outcome')
        if expected and expected in ('answer','clarification','no_answer'):
            if status!=expected:errs.append('status:'+status+' expected:'+expected)
        elif expected and not expected_status_ok(expected,status,r.mode):errs.append('status:'+status+' expected:'+expected)
        contract=c.get('answer_contract') or {k:c[k] for k in ('must_contain','must_contain_any','must_not_contain') if k in c}
        _,fail=contract_matches(r.answer,contract);errs+=fail
        if any(contract.values()):level='literal_content_contract'
        prefix=c.get('expected_mode_prefix')
        prefixes=prefix if isinstance(prefix,list) else [prefix] if prefix else []
        if prefixes and not any(r.mode.startswith(v) for v in prefixes):errs.append('legacy_mode_prefix:'+str(prefixes))
        intent=c.get('expected_intent')
        if intent and 'expected_route_categories' not in c and r.route.intent!=intent:errs.append('intent:'+r.route.intent+' expected:'+intent)
        if c.get('must_not_category') and r.route.category in c['must_not_category']:errs.append('forbidden_category')
        if name.startswith('english_'):
            from app.core.locale import contains_thai_prose
            if contains_thai_prose(r.answer):errs.append('legacy_english_thai_prose_flag')
        if expected:
            strong=status_matches(expected,answer_outcome(r.mode,r.answer,r.route.category),r.mode,r.route.category)
        else:strong=None
        native={'strong_outcome_matches':strong,'positive_content_asserted':any(contract.get(k) for k in ('must_contain','must_contain_any','must_contain_all_groups'))}
    if not r.validation.ok:errs.append('validation_rejected')
    if r.elapsed>float(c.get('latency_ceiling_sec',20)):errs.append('latency_ceiling')
    return {'passed':not errs,'failures':errs,'evidence_level':level,'grader_detail':native}
def execute(job):
    from app.pipeline.engine import answer_question_pipeline_debug
    from app.booking.live_status import _unavailable
    start=time.perf_counter();q=job['question'];loc=job['locale'];ref=job['reference_date']
    try:
        with patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled offline evaluation; no real booking oracle',error_code='fixture_offline')):
            if ref:
                with patch('app.booking.live_status.today_bangkok',return_value=date.fromisoformat(ref)):
                    r=answer_question_pipeline_debug(q,locale=loc,experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
            else:r=answer_question_pipeline_debug(q,locale=loc,experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
        grades=[]
        for entry in job['entries']:
            try:g=grade(entry['case'],r,entry['corpus'])
            except Exception as e:g={'passed':False,'failures':['grader_exception:'+type(e).__name__+':'+str(e)],'evidence_level':'grader_error'}
            grades.append({k:v for k,v in entry.items() if k!='case'}|{'expected':entry['case'],**g})
        return {'key':job['key'],'question':q,'locale':loc,'reference_date':ref,'elapsed_wall':time.perf_counter()-start,'result':plain(r),'grades':grades}
    except Exception as e:return {'key':job['key'],'question':q,'locale':loc,'exception':type(e).__name__+':'+str(e),'grades':[{k:v for k,v in x.items() if k!='case'}|{'passed':False,'failures':['pipeline_exception'],'expected':x['case']} for x in job['entries']]}
def main():
    run=sys.argv[1];jobs={};inventory=[];rowsets={};sessions=[]
    files=sorted([*(P/'data/eval').glob('*.json'),*(P/'data/eval').glob('*.jsonl'),*(P/'data/routing').glob('*eval*.jsonl')])
    for f in files:
        rows=read(f);name=f.name;relative=str(f.relative_to(P));sha=hashlib.sha256(f.read_bytes()).hexdigest()
        if not rows:inventory.append({'file':relative,'sha256':sha,'status':'metadata_not_questions','rows':0});continue
        fp=fingerprint(rows)
        if fp in rowsets:inventory.append({'file':relative,'sha256':sha,'rows':len(rows),'status':'exact_corpus_alias','alias_of':rowsets[fp]});continue
        rowsets[fp]=name
        rec={'file':relative,'sha256':sha,'rows':len(rows),'status':'evaluated','requests':0,'pending_blank':0,'non_questions':0,'sessions':0}
        for index,c in enumerate(rows):
            if not isinstance(c,dict):rec['non_questions']+=1;continue
            if c.get('kind')=='session' or c.get('turns'):
                sessions.append({'corpus':name,'row_index':index,'case':c});rec['sessions']+=1;continue
            variants=[]
            if 'noisy_question' in c:variants=[('clean',c['clean_question']),('noisy',c['noisy_question'])]
            elif 'noisy' in c:variants=[('clean',c['clean']),('noisy',c['noisy'])]
            elif c.get('observed_input'):variants=[('guard',c['observed_input'])]
            else:
                q=c.get('question_en') or c.get('question')
                if q:variants=[('question',q)]
                elif 'question_en' in c:rec['pending_blank']+=1
                else:rec['non_questions']+=1
            for variant,q in variants:
                if variant=='guard':continue # full detector corpus has its own native scoring below
                loc=c.get('locale') or ('en' if 'question_en' in c or name.startswith('english_') else 'auto')
                ref=str((c.get('metadata') or {}).get('reference_date','')) if c.get('domain')=='weekday_live_slots' else ''
                key=fingerprint([q,loc,ref]);job=jobs.setdefault(key,{'key':key,'question':q,'locale':loc,'reference_date':ref,'entries':[]})
                normalized=dict(c,question=q,locale=loc)
                job['entries'].append({'corpus':name,'row_index':index,'id':str(c.get('id',index)),'variant':variant,'case':normalized});rec['requests']+=1
        if name.startswith('keyboard_input'):rec['status']='native_guard_evaluation_separate'
        elif rec['pending_blank']==len(rows):rec['status']='pending_blank_translation_has_machine_counterpart'
        elif not rec['requests'] and not rec['sessions']:rec['status']='metadata_not_questions'
        inventory.append(rec)
    with (REPORT/(run+'_inventory.json')).open('x',encoding='utf-8') as f:json.dump({'files':inventory,'unique_requests':len(jobs),'case_executions':sum(len(j['entries']) for j in jobs.values()),'session_cases':sessions,'scope':{'llm':False,'semantic_retrieval':False,'booking':'controlled unavailable snapshot; live paths only, occupancy not verified'}},f,ensure_ascii=False,indent=2)
    print(json.dumps({'unique_requests':len(jobs),'case_grades':sum(len(j['entries']) for j in jobs.values()),'sessions':len(sessions)}),flush=True)
    counts=collections.defaultdict(collections.Counter);failures=collections.Counter();start=time.perf_counter()
    with (REPORT/(run+'_all_results.jsonl')).open('x',encoding='utf-8') as out,concurrent.futures.ProcessPoolExecutor(max_workers=6 if run!='sweep_A' else 3) as pool:
        futures=[pool.submit(execute,j) for j in jobs.values()]
        for n,future in enumerate(concurrent.futures.as_completed(futures),1):
            r=future.result();out.write(json.dumps(r,ensure_ascii=False)+'\n');out.flush()
            for g in r['grades']:
                counts[g['corpus']]['total']+=1;counts[g['corpus']]['passed']+=g['passed'];failures.update(g['failures'])
            if n%200==0:print(json.dumps({'completed':n,'remaining':len(jobs)-n,'elapsed':round(time.perf_counter()-start)}),flush=True)
    with (REPORT/(run+'_all_summary.json')).open('x',encoding='utf-8') as f:json.dump({'unique_requests':len(jobs),'elapsed_sec':time.perf_counter()-start,'by_corpus':counts,'failure_counts':failures,'deferred_sessions':len(sessions)},f,ensure_ascii=False,indent=2)
    print(json.dumps({'finished':len(jobs),'elapsed_sec':time.perf_counter()-start,'by_corpus':counts}),flush=True)
if __name__=='__main__':main()
