"""One internal taxonomy with explicit adapters for the existing public API."""
VERSION='r135-terminal-states-v1'
PUBLIC={'supported':'answer','partial':'partial_answer','missing_input':'clarification','missing_source':'unconfirmed',
        'conflict':'partial_answer','not_current':'not_current','provider_unavailable':'unavailable',
        'model_unavailable':'unavailable','budget_exhausted':'partial_answer','unsupported_operation':'unconfirmed','invalid_plan':'unconfirmed'}
TERMINALS=frozenset(PUBLIC)
LEGACY_NEED={'supported':'supported','partial':'partial_supported','missing_input':'needs_user_slot','missing_source':'missing_source',
             'conflict':'partial_supported','not_current':'not_current','provider_unavailable':'temporary_failure','model_unavailable':'temporary_failure',
             'budget_exhausted':'partial_supported','unsupported_operation':'missing_source','invalid_plan':'missing_source'}
PLAN={'answer':'supported','partial':'partial','missing_input':'missing_input','missing_source':'missing_source','not_current':'not_current','unavailable':'provider_unavailable'}

def from_result(result):
    reason=result.get('reason','');metadata=result.get('plan',{}).get('metadata',{})
    if reason in {'request_model_budget_exhausted','request_deadline_exhausted'}:return 'budget_exhausted'
    if reason in {'unsupported_operation','requested_operator_not_supported_by_reader'}:return 'unsupported_operation'
    if reason.startswith(('invalid_compiled','source_receipt_')) or reason=='invalid_or_cross_category_fact':return 'invalid_plan'
    if reason in {'model_transport_failure','model_plan_missing','model_protocol_failure','model_invalid_choice','model_duplicate_item','model_identity_mismatch','model_admission_unavailable'}:return 'model_unavailable'
    if metadata.get('authority_conflict'):return 'conflict'
    return PLAN.get(result.get('status'),'missing_source')

def aggregate(states,has_claims=False):
    states=list(states)
    if not states:return 'missing_source'
    if len(set(states))==1:return states[0]
    if has_claims:return 'partial'
    for state in ['missing_input','budget_exhausted','model_unavailable','provider_unavailable','conflict','invalid_plan','unsupported_operation','not_current']:
        if state in states:return state
    return 'missing_source'

def from_public(artifact):
    response=artifact.get('response_type')
    if response=='retry':return 'not_current'
    if (artifact.get('query_plan') or {}).get('time_required'):return 'missing_input'
    return {'answer':'supported','list':'supported','partial_answer':'partial','unconfirmed':'missing_source','clarification':'missing_input',
            'not_current':'not_current','live_unavailable':'provider_unavailable','unavailable':'provider_unavailable'}.get(response,'missing_source')
