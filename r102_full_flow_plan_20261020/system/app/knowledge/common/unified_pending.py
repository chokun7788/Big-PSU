from .selection_surface import canonical as selection_surface
"""Generic delivered selections for any registered task; intent only, no facts."""
import re
from .query_contract import normalize
from .followup_scope import delivered_state

def resolve(question,history,records,names):
    state=delivered_state(history) or {};pending=state.get('flow_pending')
    # Edition/price/event adapters preserve additional qualified source spans.
    # They own their slots; a generic selector must not preempt their repair.
    if any(state.get(k) for k in ('pending_target','price_scope_request','r98_pending_context','pending_competition_scope','profile_confirmation','request_contract')):return None
    if not isinstance(pending,dict) or pending.get('version')!=1:return None
    from .task_contracts import TASKS
    if pending.get('task') not in TASKS:return None
    ids=pending.get('candidate_ids')
    if not isinstance(ids,list) or len(ids)>100 or any(not isinstance(k,str) for k in ids):return None
    if pending.get('slot')=='time':
        from app.booking.live_status import requested_time_window,LiveBookingSnapshot
        blank=LiveBookingSnapshot(False,'','','','',False,'',(),())
        window=requested_time_window(question,blank)
        if window and window.explicit and all(k in records for k in ids):
            return {'task':pending['task'],'predicate':pending.get('predicate','live_resource_available'),
              'record_ids':ids,'query':pending['query']+' '+question,'source_span':question,
              'slots':{'task':{'value':pending['task'],'origin':'delivered_state'},'time':{'value':window.label,'origin':'current_user','quote':question}},'invalid':False}
        return None
    q=selection_surface(question)
    ordinal=re.fullmatch(r'(?:option\s*|อันที่\s*|ข้อ\s*)(\d+)',q)
    if ordinal:
        index=int(ordinal[1])-1
        selected=ids[index:index+1] if 0<=index<len(ids) else []
    elif q in {'all','all of them','everything','ทั้งหมด','ทุกอัน'}:
        if pending.get('allow_all') is False:return {'invalid':True,'reason':'single_subject_required'}
        selected=list(ids)
    else:
        eligible=ids if not pending.get('subject_kind') else [k for k,r in records.items() if r['kind']==pending['subject_kind']]
        selected=[rid for rid in eligible if any(normalize(a)==q for a in names.get(rid,[]))]
    if not selected:return None
    if any(k not in records for k in selected):return {'invalid':True,'reason':'selected_record_withdrawn'}
    selected_query=pending['query'];root_ids=[]
    if pending.get('subject_kind')=='audience':
        from .answer import title
        root_ids=pending.get('scope_root_ids',[])
        if any(k not in records for k in root_ids):return {'invalid':True,'reason':'selected_scope_withdrawn'}
        selected_query+=' for '+', '.join(title(records[k],'en') for k in selected)
    return {'task':pending['task'],'predicate':pending.get('predicate',pending['task']),
      'record_ids':list(dict.fromkeys(root_ids+selected)),'query':selected_query,'source_span':question,
      'slots':{'task':{'value':pending['task'],'origin':'delivered_state'},
       'subject':{'value':selected,'origin':'current_user','quote':question}},'invalid':False}

def create(plan,artifact):
    if len(plan.get('needs',[]))!=1:return None
    need=plan['needs'][0];qp=artifact.get('query_plan') or {}
    # Only actual displayed selections are eligible. Never turn a retrieval
    # shortlist or hidden database IDs into conversation options.
    pending=qp.get('pending_selection') or {}
    ids=pending.get('candidate_ids') or pending.get('record_ids')
    if not ids:return None
    return {'version':1,'task':need['task'],'predicate':need.get('predicate'),
      'query':need['query'],'candidate_ids':ids,'scope_root_ids':pending.get('scope_root_ids',need.get('record_ids',[])),'slot':pending.get('slot'),'subject_kind':pending.get('subject_kind'),'allow_all':pending.get('allow_all',True),'facts_in_state':False}
