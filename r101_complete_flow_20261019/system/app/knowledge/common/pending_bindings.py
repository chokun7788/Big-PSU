"""Bind explicit pending selections. Store references/constraints, not facts."""
import re
from .followup_scope import delivered_state
from .query_contract import normalize

def bind(question,history,records,names):
    state=delivered_state(history) or {};p=state.get('price_scope_request')
    q=normalize(question).strip(' ?!.,')
    if re.search(r'เปลี่ยนเรื่อง|ไม่ใช่|\b(?:new topic|instead|not that)\b',q):return None
    if isinstance(state.get('request_contract'),dict) and state['request_contract'].get('domain')=='rental':
        from .rental_bridge import parse,catalog,zone_selection,group_selection,_periods
        contract=parse(question,history,records)
        if contract and contract.get('context_used') and contract.get('action')=='read':
            _,zones,groups,labels=catalog(records)
            explicit_zones,_=zone_selection(q,zones,labels);explicit_groups=group_selection(q,groups,records);explicit_periods=_periods(q)
            requests=[]
            for row in contract['requests']:
                requests.append({key:{'values':vals,'origin':'current_user' if explicit else 'delivered_state','source_span':question if explicit else None} for key,vals,explicit in [('zones',row['zones'],explicit_zones),('audiences',row['audiences'],explicit_groups),('periods',row['periods'],explicit_periods)]})
            return {'version':1,'action':'rental_selection','task':'rental','predicate':'rental_package','slots':{'requests':requests,'task':{'value':'rental','origin':'delivered_state','binding_reason':'same_pending_rental_task'}},'business_values_from_history':False}
    if not isinstance(p,dict) or p.get('version')!=1 or state.get('profile_confirmation_closed'):return None
    services=sorted(k for k,r in records.items() if r['kind']=='service')
    if q in {'ทั้งหมด','ทุกอัน','ทุกบริการ','all','all services','all of them','everything'}:
        selected=services;basis='explicit_all';roots=[]
    else:
        choices=p.get('candidate_service_ids',[])
        if not isinstance(choices,list) or len(choices)>500:return None
        number=re.fullmatch(r'(?:อันที่|รายการที่|ข้อ|number|option|#)\s*(\d+)',q)
        words={'อันแรก':1,'first':1,'the first':1,'อันที่สอง':2,'second':2,'the second':2,'อันที่สาม':3,'third':3,'the third':3}
        index=int(number[1]) if number else words.get(q)
        if index:
            if not 1<=index<=len(choices):return {'action':'invalid_selection','slot':'service','task':'price','reason':'option_out_of_range','slots':{}}
            target=choices[index-1]
            if target not in records or records[target]['kind']!='service':return {'action':'invalid_selection','slot':'service','task':'price','reason':'selected_record_withdrawn','slots':{}}
            selected=[target];roots=[target];basis='explicit_ordinal'
        else:
            roots=[k for k,r in records.items() if r['kind'] in {'service','resource','zone'} and any(normalize(a)==q for a in names.get(k,[]))]
            if not roots:return None
            from .relations import related_rates
            from .registry import value
            selected=sorted({k for k in roots if records[k]['kind']=='service'}|{value(rate,'service_id') for k in roots for rate in related_rates(records,records[k]) if value(rate,'service_id') in services})
            if not selected:return None
            basis='explicit_name'
    audiences=p.get('audience_ids',[])
    audiences=[k for k in audiences if isinstance(k,str) and k in records and records[k]['kind']=='audience'] if isinstance(audiences,list) else []
    slots={'service':{'record_ids':selected,'origin':'current_user','source_span':question,'binding_reason':basis},
           'task':{'value':'price','origin':'delivered_state','binding_reason':'same_pending_price_task'}}
    if audiences:slots['audience']={'record_ids':audiences,'origin':'delivered_state','binding_reason':'same_pending_price_task'}
    duration=p.get('duration_quote')
    if isinstance(duration,str) and duration:slots['duration']={'quote':duration,'origin':'delivered_state','binding_reason':'same_pending_price_task'}
    return {'version':1,'action':'price_selection','task':'price','predicate':'current_rate','service_ids':selected,'root_ids':roots,'audience_ids':audiences,'slots':slots,'selection_basis':basis,'source_state_release':state.get('release_id'),'business_values_from_history':False}
