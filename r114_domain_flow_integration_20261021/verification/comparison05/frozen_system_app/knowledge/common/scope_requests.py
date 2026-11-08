"""Exhaustive price scope and trusted short selections over one common snapshot."""
import re,time
from dataclasses import replace
from .registry import value
from .query_contract import normalize,matches,live_request

def answer(reader,question,snap,records,names,lang,history,at):
    from .followup_scope import delivered_state
    from .audience_scope import resolve
    from .answer import named,title
    q=normalize(question);state=delivered_state(history) or {};pending=state.get('price_scope_request') or {}
    from .rental_bridge import parse as rental_contract
    if rental_contract(question,history,records):return None
    from .pending_bindings import bind
    binding=bind(question,history,records,names)
    if binding and binding['action']=='invalid_selection':
        from .answer import title
        services=sorted(k for k,r in records.items() if r['kind']=='service')
        body=('ตัวเลือกนี้เปลี่ยนไปหรือไม่มีอยู่แล้วครับ กรุณาเลือกจากรายการปัจจุบัน: ' if lang=='th' else 'That option is unavailable or changed. Please select from the current list: ')+', '.join(title(records[k],lang) for k in services)
        plan={'record_ids':[],'requested_fields':[],'operation':'price','method':'pending_selection_invalid','pending_binding':binding,'price_scope_request':{**pending,'candidate_service_ids':services}}
        return reader.finish(snap,time.perf_counter(),body,[],plan,[],response='clarification')
    is_price=bool(re.search(r'ราคา|ค่าบริการ|กี่บาท|\b(?:prices?|costs?|fees?|rates?|how much)\b',q))
    all_scope=bool(re.search(r'ทั้งหมด|ทุก(?:บริการ|เครื่อง|อัน)|\b(?:all|every|everything)\b',q)) and not re.search(r'ไม่(?:เอา|ต้อง).{0,12}(?:ทั้งหมด|ทุก)|\b(?:not|without)\b.{0,12}\ball\b',q)
    selector=q.strip(' ?!.,')
    services=sorted(k for k,r in records.items() if r['kind']=='service')
    available_names={k:names.get(k,[]) for k,r in records.items() if r['kind'] in {'zone','resource','service'}}
    root_ids,_=named(question,available_names,allow_fuzzy=False)
    # A named game has its own task/linked-service reader; a missing service
    # selector must not swallow its overview or another independent task.
    game_ids,_=named(question,{k:names.get(k,[]) for k,r in records.items() if r['kind']=='game'},allow_fuzzy=False)
    if game_ids and not root_ids:return None
    if not services:return None
    resume=bool(binding and binding['action']=='price_selection')
    if resume:
        root_ids=binding['root_ids']
        all_scope=binding['selection_basis']=='explicit_all'
    if not (is_price and (all_scope or not root_ids) or resume):return None
    # A set difference is a separate task contract. Keep its established
    # qualifier-aware reader rather than treating "all except X" as "all".
    if re.search(r'ยกเว้น|ไม่เอา|\b(?:except|excluding|without)\b',q):return None
    if live_request(question) or re.search(r'เหมา|ครึ่งวัน|เต็มวัน|\b(?:rental|half.day|full.day|budget|compare|cheaper|difference)\b|งบ|เทียบ|ถูกกว่า|ต่างกัน',q):return None
    if resume:
        # Do not let short selectors inherit a superseded or unrelated task.
        if state.get('profile_confirmation_closed'):return None
        audience_query=str(pending.get('audience_query') or '')
        audience_ids=[k for k in pending.get('audience_ids',[]) if k in records and records[k]['kind']=='audience']
        if not audience_ids:audience_ids,_=resolve(audience_query,records);audience_ids=audience_ids or []
    else:
        audience_query=question;audience_ids,_=resolve(question,records);audience_ids=audience_ids or []
    duration_quotes=re.findall(r'\d+(?:\.\d+)?\s*(?:นาที|ชั่วโมง|minutes?|mins?|hours?|hrs?)',question,re.I)
    duration_quote=duration_quotes[0] if len(duration_quotes)==1 else pending.get('duration_quote','') if resume else ''
    started=time.perf_counter()
    if not root_ids and not all_scope and not resume:
        body=('ต้องการทราบราคาบริการใดครับ: ' if lang=='th' else 'Which service price would you like: ')+', '.join(title(records[k],lang) for k in services)+(' หรือพิมพ์ “ทั้งหมด” เพื่อดูแยกทุกบริการครับ' if lang=='th' else '? Reply “all” to see every service.')
        plan={'record_ids':audience_ids,'requested_fields':['amount_minor'],'operation':'price','method':'r98_pending_service','price_scope_request':{'version':1,'audience_ids':audience_ids,'audience_query':audience_query,'duration_quote':duration_quote,'candidate_service_ids':services,'scope':'all_declared_services'},'source_answer_confirmed':False}
        return reader.finish(snap,started,body,[],plan,[],response='clarification')
    if resume:roots=binding['service_ids']
    elif all_scope and not root_ids:roots=services
    else:
        from .relations import related_rates
        roots=sorted(set(k for k in root_ids if records[k]['kind']=='service')|{value(rate,'service_id') for k in root_ids for rate in related_rates(records,records[k]) if value(rate,'service_id') in records})
    if not roots:return None
    ids=roots+[k for k in audience_ids if k not in roots]
    plan={'record_ids':ids,'scope_ids':list(ids),'requested_fields':['amount_minor'],'operation':'price','all_fields':False,'method':'r98_exhaustive_price_scope','platform':None,'unresolved_clauses':[],
          'audience_selection':{'selected_ids':audience_ids,'user_query':audience_query,'eligibility_assumed':False,'scope_is_alternatives':not bool(audience_ids)},
          'price_scope_request':{'version':1,'audience_ids':audience_ids,'audience_query':audience_query,'duration_quote':duration_quote,'candidate_service_ids':services,'scope':'all_declared_services'},
          'set_receipt':{'release_id':snap['active'],'epoch':snap['epoch'],'predicate':'declared service records in pinned release' if all_scope else 'explicit service/zone/resource selection','member_ids':roots,'total_members':len(roots),'enumeration':'exhaustive_snapshot_scan','retrieval_top_k_used':False,'claims_complete_catalog_outside_this_snapshot':False}}
    billing_query=question+' '+duration_quote if resume else question
    if binding:plan['pending_binding']=binding
    result=reader.execute_task(question,snap=snap,at=at,lang=lang,plan=plan,context={'billing_query':billing_query})
    if result.decision_artifact.get('response_type')=='retry':return result
    # Render the enumerated set compactly; values still require the shared
    # reader's current, source-backed amount obligation.
    from .relations import related_rates
    known={o['record_id'] for o in result.decision_artifact.get('obligations',[]) if o.get('field')=='amount_minor' and o.get('status')=='known' and o.get('evidence_refs')}
    rows=[];missing=[];rates_seen=[]
    header='| บริการ | กลุ่มในตาราง | ราคาปัจจุบัน / สถานะ |\n|---|---|---|' if lang=='th' else '| Service | Recorded audience | Current price / status |\n|---|---|---|'
    def cell(t):return str(t).replace('|','/').replace('\n',' ')
    for sid in roots:
        rates=related_rates(records,records[sid],audiences=audience_ids)
        if not rates:
            rows.append('| '+cell(title(records[sid],lang))+' | — | '+('ยังไม่มีอัตราที่ยืนยัน' if lang=='th' else 'No confirmed rate')+' |');missing.append(sid)
        for rate in rates:
            rid=rate['record_id'];rates_seen.append(rid);aud=records.get(value(rate,'audience_id'))
            if rid in known:
                amount=value(rate,'amount_minor');currency=value(rate,'currency');unit=value(rate,'unit')
                shown=f'{amount//100:,}.{amount%100:02d} {currency} / {unit}'
                duration=value(rate,'duration_minutes')
                if duration is not None:shown+=' ('+str(duration)+(' นาที)' if lang=='th' else ' minutes)')
                from .billing import calculate,render
                calculation=calculate(rate,billing_query)
                if calculation:shown+='; '+render(calculation,lang)
                labels=[h['citation_label'] for h in result.hits if h.get('record_id')==rid and h.get('field')=='amount_minor']
                shown+=' '+''.join('['+label+']' for label in labels)
            else:
                missing.append(sid)
                shown=('ยังไม่ยืนยัน: ไม่มีช่วงมีผลที่ยืนยัน' if lang=='th' else 'Unconfirmed: effective period is unknown') if rate['validity']['state']!='known' else ('ยังไม่ยืนยัน: ไม่อยู่ในช่วงมีผล' if lang=='th' else 'Unconfirmed: rate is not effective')
            rows.append('| '+cell(title(records[sid],lang))+' | '+cell(title(aud,lang) if aud else '—')+' | '+cell(shown)+' |')
    result=replace(result,answer=header+'\n'+'\n'.join(rows))
    plan['set_receipt'].update(rate_ids=rates_seen,members_with_unconfirmed_prices=sorted(set(missing)),returned_members=list(roots),returned_members_count=len(roots))
    if not audience_ids:
        note=('ยังไม่ยืนยันกลุ่มราคาที่ตรงสิทธิของผู้ถาม แสดงอัตรา/สถานะแยกตามกลุ่มที่บันทึกไว้ กรุณาเลือกกลุ่มให้ตรงสิทธิครับ' if lang=='th' else 'Your applicable audience group is not confirmed. The recorded groups are shown separately; select the group matching your eligibility.')
        result=replace(result,answer=note+'\n\n'+result.answer)
    art=dict(result.decision_artifact or {});art['task_flow']={'version':'r98','path':'exhaustive_price_scope','executor':'shared_common_reader'}
    if not known and art.get('response_type')=='clarification':
        art['response_type']='unconfirmed'
        result=replace(result,mode='pipeline:common_unconfirmed',route=replace(result.route,answer_type='unconfirmed'))
    return replace(result,decision_artifact=art)
