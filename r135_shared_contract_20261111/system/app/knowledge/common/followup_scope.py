"""Resume typed, delivered scope only. No assistant prose or studio facts."""
import re
from .registry import value
from .query_contract import normalize
from .profile_confirmation import fingerprint

def delivered_state(history):
    for t in reversed((history or [])[-8:]):
        if not isinstance(t,dict) or t.get('role')!='assistant':continue
        if t.get('delivery_status') not in {'server_written','client_acknowledged'}:return None
        s=t.get('common_read_state')
        return s if isinstance(s,dict) and s.get('schema_version')==1 else None
    return None

def delivered_reference(history):
    """Audit reference from the same gated assistant carrier as its state."""
    for turn in reversed((history or [])[-8:]):
        if not isinstance(turn,dict) or turn.get('role')!='assistant':continue
        if turn.get('delivery_status') not in {'server_written','client_acknowledged'}:return None
        ref=turn.get('_server_history_ref')
        if not isinstance(ref,dict) or ref.get('origin')!='server_session_store' or ref.get('response_id')!=turn.get('request_id'):return None
        return {key:ref.get(key) for key in ['session_id','turn_id','response_id','origin','delivery_status']}
    return None

def profile_followup(question,history,records):
    s=delivered_state(history)
    if not s or s.get('profile_confirmation') or s.get('profile_confirmation_closed'):return None
    origin=s.get('profile_read_scope')
    if not isinstance(origin,dict):return None
    q=normalize(question)
    if len(q)>160:return None
    # Explicit follow-up framing; a complete new request uses the normal router.
    start=re.match(r'^(?:and|also|what about|how about)\s+|^(?:แล้ว|ส่วน)',q)
    end=re.search(r'(?:ด้วย(?:ได้ไหม|ได้มั้ย)?|ล่ะ)\s*[?!.,]*$',q)
    if not start and not end:return None
    tail=q[start.end():] if start else q
    tail=re.sub(r'(?:ด้วย(?:ได้ไหม|ได้มั้ย)?|ล่ะ)\s*[?!.,]*$','',tail).strip()
    rid=origin.get('record_id')
    if rid not in records or fingerprint(records[rid])!=origin.get('routing_sha256'):return {'action':'expired'}
    from .qualified_reply import scope_plan
    ids,audit=scope_plan(tail,records[rid],records)
    # No positive subject means e.g. "And when?": preserve its normal field flow.
    from .question_profiles import phrase_match
    if not any(phrase_match(tail,label) for r in records.values() for sub in (value(r,'query_profile') or {}).get('subjects',[]) for label in sub.values() if isinstance(label,str)):return None
    base={'blocked_unqualified_ids':[rid],'qualification':{'qualifier':tail,'original_input':question},'audit':audit}
    if ids and len(ids)==1:return {**base,'action':'qualified_selected','record_id':ids[0],'routing_sha256':fingerprint(records[ids[0]]),'basis':'delivered_declared_profile_followup'}
    if ids and len(ids)>1:audit['reason']='ambiguous_qualified_profiles'
    return {**base,'action':'qualification_unconfirmed'}

def competition_question(question,history,records,names):
    s=delivered_state(history);p=s.get('pending_competition_scope') if s else None
    if not isinstance(p,dict) or p.get('version')!=1:return None
    rid=p.get('record_id')
    if rid not in records or fingerprint(records[rid])!=p.get('routing_sha256'):return {'expired':True}
    q=normalize(question).strip(' ?!.,');games=[k for k,r in records.items() if r['kind']=='game' and any(normalize(a)==q for a in names.get(k,[]))]
    comps=[k for k,r in records.items() if r['kind']=='competition' and (value(r,'game_id') in games or any(normalize(a)==q for a in names.get(k,[])))]
    if not comps:return None
    scope=p.get('scope',{});subjects=scope.get('subjects',[])
    labels=[x.get('en') or x.get('th') for x in subjects]
    owner={'personal':'personal ','studio':'studio-owned '}.get(scope.get('ownership'),'')
    # A sourced rule lookup, not an assertion that ordinary studio policy applies.
    return {'question':question+' tournament rules about '+owner+', '.join(labels),'competition_ids':comps,'inherited_scope':scope}

def priced_services(records):
    return sorted({value(r,'service_id') for r in records.values() if r['kind']=='rate' and value(r,'service_id') in records})

def price_selection(question,history,records,names):
    s=delivered_state(history);p=s.get('price_scope_request') if s else None
    if not isinstance(p,dict) or p.get('version')!=1:return None
    available=priced_services(records);q=normalize(question).strip(' ?!.,')
    if q in {'ทั้งหมด','ทุกอัน','ทุกบริการ','all','all services','all of them','everything'}:roots=available
    else:
        roots=[rid for rid in available if any(normalize(a)==q for a in names.get(rid,[]))]
        # Zone/resource labels may select several service options.
        if not roots:
            from .relations import related_rates
            parents=[r for rid,r in records.items() if r['kind'] in {'zone','resource'} and any(normalize(a)==q for a in names.get(rid,[]))]
            roots=sorted({value(rate,'service_id') for r in parents for rate in related_rates(records,r) if value(rate,'service_id') in available})
    if not roots:return None
    audiences=[rid for rid in p.get('audience_ids',[]) if rid in records and records[rid]['kind']=='audience']
    return {'record_ids':roots+audiences,'query':'price','method':'price_scope_selection'}
