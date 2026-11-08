"""Data-driven live bindings; missing/stale/unknown is never free or closed."""
import time,re
from .registry import value,aware
from .flow_context import CURRENT

def answer(reader,need,snap,at,lang):
    records={k:r for k,r in snap['release']['records'].items() if k not in snap.get('withdrawn',[])}
    roots=set(need.record_ids);services={k for k in roots if k in records and records[k]['kind']=='service'}
    resources={k for k in roots if k in records and records[k]['kind']=='resource'}
    zones={k for k in roots if k in records and records[k]['kind']=='zone'}
    resources.update(k for k,r in records.items() if r['kind']=='resource' and value(r,'zone_id') in zones)
    services.update(k for k,r in records.items() if r['kind']=='service' and resources.intersection(value(r,'resource_ids') or []))
    services.update(value(r,'service_id') for r in records.values() if r['kind']=='game_service' and value(r,'game_id') in roots and value(r,'offered') is True)
    enumerated_scope=not roots and bool(re.search(r'ทั้งหมด|มีเครื่องไหน|เครื่องไหน|\b(?:all|which|what)\b',need.query,re.I))
    if enumerated_scope:services.update(value(r,'service_id') for r in records.values() if r['kind']=='live_binding')
    bindings=[r for r in records.values() if r['kind']=='live_binding' and (value(r,'service_id') in services or r['record_id'] in roots)]
    if not bindings:return None
    from .answer import effective,title
    from app.booking.live_status import resolve_live_target_date,get_live_booking_status,requested_time_window
    day=resolve_live_target_date(need.query);ctx=CURRENT.get();cache_key=('wordpress_booking',str(day))
    observation=None;blocks=[];receipts=[];observations=[];unavailable=False
    for binding in bindings:
        ttl=value(binding,'freshness_max_age_seconds')
        if not effective(binding,at,records) or type(ttl) is not int or ttl<=0:
            unavailable=True;observations.append({'binding_id':binding['record_id'],'status':'live_unavailable','reason':'freshness_policy_or_binding_not_confirmed'});continue
        if observation is None:
            observation=ctx.live.get(cache_key) if ctx else None
            if observation is None:
                observation=get_live_booking_status(day)
                if ctx:ctx.live[cache_key]=observation
        reason=None
        if not observation.ok:reason=observation.error_code or 'provider_unavailable'
        if observation.date!=str(day):reason=reason or 'observation_date_mismatch'
        try:
            age=(at-aware(observation.generated_at)).total_seconds()
            if age<0 or age>ttl:reason='stale_or_future_observation'
        except (ValueError,TypeError):age=None;reason='missing_observed_at'
        key=value(binding,'external_resource_key');resource=next((r for r in observation.resources if r.resource_id==key),None)
        if resource is None:reason=reason or 'bound_resource_not_in_observation'
        mapping={x['raw']:x['normalized'] for x in value(binding,'status_mapping') or []}
        normalized=mapping.get(resource.status,'unknown') if resource else 'unknown'
        window=requested_time_window(need.query,observation);slot_rows=[]
        if str(day)!=at.date().isoformat() and (window is None or not window.explicit):reason=reason or 'time_required'
        if resource and window and window.explicit:
            slots=sorted((s for s in resource.slots if s.start<(window.end or '24:00') and s.end>window.start),key=lambda s:s.start)
            if not window.end:slots=[s for s in slots if s.start<=window.start<s.end][:1]
            cursor=window.start;states=[]
            for slot in slots:
                mapped=mapping.get(slot.status,'unknown')
                if slot.start>cursor:reason=reason or 'incomplete_slot_coverage'
                cursor=max(cursor,slot.end);states.append(mapped)
                if mapped=='free' and slot.available_count<=0:reason=reason or 'conflicting_slot_count'
                slot_rows.append({'start':slot.start,'end':slot.end,'raw_status':slot.status,'normalized_status':mapped,'available_count':slot.available_count})
            if not slots or window.end and cursor<window.end:reason=reason or 'incomplete_slot_coverage'
            if 'unknown' in states:reason=reason or 'unmapped_slot_status'
            normalized='free' if states and all(s=='free' for s in states) else 'unavailable' if 'unavailable' in states else 'occupied' if 'occupied' in states else 'unknown'
        if normalized=='unknown':reason=reason or 'unmapped_provider_status'
        row={'binding_id':binding['record_id'],'provider':value(binding,'provider'),'resource_key':key,'physical_pool_key':value(binding,'physical_pool_key'),
          'observed_at':observation.generated_at,'target_date':str(day),'age_seconds':age,'max_age_seconds':ttl,
          'provider_status':resource.status if resource else None,'normalized_status':normalized,'freshness_checked':reason is None,
          'requested_window':window.label if window else None,'slot_coverage':slot_rows,
          'status':'live_unavailable' if reason else 'supported','reason':reason}
        observations.append(row)
        if reason:unavailable=True;continue
        name=title(records[value(binding,'service_id')],lang)
        status={'free':('ว่าง','available'),'occupied':('ไม่ว่าง','occupied'),'unavailable':('ไม่พร้อมใช้','unavailable')}[normalized][lang=='en']
        blocks.append(name+(': '+window.label+' — ' if window and window.explicit else ': ')+status+' ('+observation.generated_at+')')
        for field in ('service_id','provider','external_resource_key','physical_pool_key','status_mapping','timezone','freshness_policy','freshness_max_age_seconds'):
            f=binding['fields'].get(field,{})
            if f.get('status')=='known':receipts.append({'record_id':binding['record_id'],'field':field,'status':'known','evidence_refs':f.get('evidence_refs',[])})
    if unavailable:blocks.append('บางรายการยังตรวจสถานะสดที่ยืนยันได้ไม่ได้ครับ' if lang=='th' else 'Live availability cannot currently be confirmed for some selected items.')
    plan={'record_ids':[r['record_id'] for r in bindings],'requested_fields':[],'method':'r101_common_live_binding','live_observations':observations,'static_availability_inferred':False}
    if enumerated_scope:plan['set_receipt']={'scope':'all_declared_live_bindings','member_ids':[r['record_id'] for r in bindings],'total_members':len(bindings),'returned_members_count':len(observations),'release_id':snap['active']}
    needs_time=any(r.get('reason')=='time_required' for r in observations)
    if needs_time:
        plan.update(time_required=True,pending_selection={'candidate_ids':list(services),'slot':'time'})
        blocks.append('ต้องการตรวจช่วงเวลากี่โมงครับ?' if lang=='th' else 'Which time or time range should I check?')
    result=reader.finish(snap,time.perf_counter(),'\n'.join(blocks),[],plan,receipts,response='clarification' if needs_time else 'partial_answer' if blocks and any(r['status']=='supported' for r in observations) and unavailable else 'live_unavailable' if unavailable else 'answer')
    result.decision_artifact['live_booking']={'status':'unavailable' if unavailable else 'confirmed','observations':observations,'provider_scope_reads':1 if observation else 0}
    return result
