import dataclasses
from unittest.mock import patch
def plain(v):
    if dataclasses.is_dataclass(v):return {k:plain(x) for k,x in dataclasses.asdict(v).items()}
    if isinstance(v,dict):return {k:plain(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [plain(x) for x in v]
    return v

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