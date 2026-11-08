"""Keep current input, derived execution text and delivered state distinct.

Offset receipts describe literal normalization only, never intent correctness.
The native history gate requires server-sanitized history at its caller boundary.
"""
import copy,hashlib,json
from ..flow_context import CURRENT
from ..normalized_query import normalize_query
from ..followup_scope import delivered_state

VERSION='r123-request-provenance-v1'

def digest(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True).encode()).hexdigest()

def derived_input(question,kind,segments,**detail):
    ctx=CURRENT.get()
    if ctx is not None:
        ctx.event('R123_derived_input',execution_question=question,kind=kind,segments=copy.deepcopy(segments),**detail)

def capture(question,history=None):
    ctx=CURRENT.get();data=ctx.input if ctx is not None else {}
    raw=data.get('raw_question')
    if not isinstance(raw,str):raw=question;origin='direct_engine_or_domain_call'
    else:origin='native_request_context'
    normalized=normalize_query(raw)
    basis='current_raw' if question==raw else 'current_normalized' if question==normalized.text else 'derived_or_unmapped_execution'
    derivation=next((copy.deepcopy(e) for e in reversed(ctx.events) if e.get('stage')=='R123_derived_input' and e.get('execution_question')==question),None) if ctx else None
    if derivation:basis=derivation['kind']
    state=delivered_state(history)
    return {'version':VERSION,'request_id':ctx.request_id if ctx else None,'raw_question':raw,'normalized_question':normalized.text,
        'engine_question':question,'input_origin':origin,'input_basis':basis,'normalization':normalized.public(),
        'derivation':derivation,'history':{'present':bool(history),'native_delivered_state_accepted':state is not None,
            'state_sha256':digest(state) if state is not None else None,'facts_inherited':False,
            'trust_basis':'native_delivered_state_gate_requires_server_sanitized_history','arbitrary_assistant_prose_used':False},
        'whole_question_semantics_verified':False}

def map_span(context,span):
    """Bound a compiled span to current raw text only when offsets are proved.

    Replacements use an enclosing raw range, explicitly not an exact quote.
    Synthetic history/shared queries remain in their original source basis.
    """
    start,end,text=span['start'],span['end'],span['text'];q=context['engine_question']
    if not 0<=start<end<=len(q) or q[start:end]!=text:return {'status':'invalid_execution_span'}
    basis=context['input_basis'];raw=context['raw_question'];norm=context['normalization']
    if basis=='current_raw':return {'status':'exact_current_raw','start':start,'end':end,'text':raw[start:end]}
    if basis!='current_normalized':return {'status':'derived_source_basis','input_basis':basis,'current_raw_span_asserted':False}
    offsets=norm['offsets'][start:end]
    if len(offsets)!=end-start or any(not isinstance(x,int) or not 0<=x<len(raw) for x in offsets):return {'status':'unmapped_normalization'}
    lo,hi=min(offsets),max(offsets)+1
    # Include the complete source range for a replacement (offsets alone only
    # identify the replacement's first character).
    for edit in norm['edits']:
        if edit['replacement'] and any(edit['raw_start']<=x<edit['raw_end'] for x in offsets):
            lo=min(lo,edit['raw_start']);hi=max(hi,edit['raw_end'])
    raw_text=raw[lo:hi]
    status='exact_current_raw' if raw_text==text else 'normalized_raw_range'
    return {'status':status,'start':lo,'end':hi,'text':raw_text,'exact_quote':raw_text==text,'semantic_equivalence_verified':False}

def attach_compiled(contract,context):
    contract['request_context']=context
    plan=contract.get('request_plan') or {}
    if not plan.get('tasks'):return contract
    mapped=[]
    for task in plan['tasks']:
        spans=[('task',task['source_span'])]
        if task.get('target_span'):spans.append(('target',task['target_span']))
        spans.extend((s['id'],s['source_span']) for s in task.get('slots',[]))
        mapped.append({'task_id':task['id'],'spans':[{'kind':kind,'execution_span':s,'raw_mapping':map_span(context,s)} for kind,s in spans]})
    contract['input_span_receipts']=mapped
    return contract
