"""Terminal result adapter shared by common readers and dispatcher fallbacks."""
from dataclasses import replace

def status(result,coverage=None):
    art=result.decision_artifact or {};plan=art.get('query_plan') or {};response=art.get('response_type') or result.route.answer_type
    errors=list(result.validation.errors);reason=[]
    if art.get('store_error_type') or response in {'unavailable','retry'}:return 'temporary_failure',['store_or_snapshot_unavailable']
    if errors:
        if any('source_pointer' in e for e in errors):return 'broken_relation',errors
        if any(e.startswith('missing_requested_field') for e in errors):return 'missing_source',errors
        return 'ambiguous_interpretation',errors
    live=art.get('live_booking')
    if plan.get('time_required'):return 'needs_user_slot',['time_required']
    if isinstance(live,dict):
        if response=='live_unavailable' or live.get('status')=='unavailable' or 'unavailable' in result.mode:return 'live_unavailable',['provider_unavailable']
        return 'scope_unverified',['legacy_live_adapter_freshness_contract']
    if (plan.get('entity_selection') or {}).get('availability_failure'):return 'temporary_failure',['model_or_retrieval_unavailable']
    obs=art.get('obligations',[])
    if any(o.get('status')=='conflicted' for o in obs) and not any(o.get('status')=='known' for o in obs):return 'conflict',['source_conflict']
    if response=='not_current':return 'not_current',['source_not_effective']
    if response in {'unconfirmed','withdrawn'}:return 'missing_source',[plan.get('method') or 'unconfirmed_source']
    if response=='live_unavailable':return 'live_unavailable',['provider_not_read']
    if response=='clarification':
        if any(plan.get(k) for k in ('price_scope_request','pending_selection','profile_confirmation','r98_pending_context','pending_target')):return 'needs_user_slot',['explicit_pending_selection']
        if plan.get('date_required'):return 'needs_user_slot',['date_required']
        if any(o.get('status')=='needs_clarification' for o in obs):return 'needs_user_slot',['executor_missing_slot']
        return 'ambiguous_interpretation',['no_accepted_interpretation']
    if response in {'scope','unsupported'}:return 'unsupported',['outside_supported_capability']
    if response=='greeting':return 'interface',['assistant_interface']
    if coverage and coverage['decision']=='predicate_mismatch':return ('missing_source' if 'temporal_applicability_unconfirmed' in coverage['reason_codes'] else 'ambiguous_interpretation'),coverage['reason_codes']
    if response=='partial_answer':return 'partial_supported',['explicit_partial_response']
    if coverage and coverage['decision']=='contract_supported':return 'supported',[]
    return 'scope_unverified',['compatibility_scope_not_migrated']

def finalize(result,question,snapshot=None,history=None):
    """Cover final rejection/fallback paths without restoring rejected facts."""
    from .request_plan import make_plan,attach,VERSION
    art=dict(result.decision_artifact or {})
    if art.get('request_plan',{}).get('version')==VERSION and art.get('need_results'):
        from .query_contract import normalize
        art['request_plan']['raw_question']=question
        for need in art['request_plan'].get('needs',[]):
            for slot in need.get('slots',{}).values():
                if isinstance(slot,dict) and normalize(slot.get('source_span') or '')==normalize(question):slot['source_span']=question
        target=art.get('target_binding')
        if target and normalize(target.get('source_span',''))==normalize(question):
            target['source_span']=question;art['request_plan']['question']=question
            for need in art['request_plan']['needs']:
                need['source_span']=question
                if 'subject' in need['slots']:need['slots']['subject']['source_span']=question
            for row in art['need_results']:row['source_span']=question
        return replace(result,decision_artifact=art)
    records=(((snapshot or {}).get('release') or {}).get('records') or {})
    names=(((snapshot or {}).get('release') or {}).get('names') or {})
    rejected=art.get('rejected_candidate') or {}
    if rejected.get('request_plan'):
        # Preserve the rejected need structure and reason, never its claims.
        rows=[]
        for row in rejected.get('need_results',[]):
            state=row.get('status','ambiguous_interpretation')
            if state in {'supported','partial_supported','scope_unverified'}:state='ambiguous_interpretation'
            coverage={**row.get('coverage',{}),'decision':'rejected','receipts':[]}
            rows.append({**row,'status':state,'reason_codes':rejected.get('validation_errors',[]),'receipts':[],'coverage':coverage})
        if rows:
            art.update(request_plan=rejected['request_plan'],need_results=rows,result_contract={'version':1,'path':'rejection','fact_restoration':False})
            return replace(result,decision_artifact=art)
    plan=make_plan(question,records,names,history,split=False)
    result=attach(result,plan,snapshot)
    art=dict(result.decision_artifact or {});art['result_contract']={'version':1,'path':'dispatcher_finalizer','semantic_correctness_verified':False}
    return replace(result,decision_artifact=art)
