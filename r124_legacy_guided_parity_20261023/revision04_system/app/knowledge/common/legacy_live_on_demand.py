"""Reuse legacy live selection/window/rendering with current common bindings.

No stored occupancy, startup fetch, sample fallback, or model-generated facts.
"""
import time
from datetime import timedelta,datetime
from dataclasses import replace
from zoneinfo import ZoneInfo
from .registry import value,aware
from .flow_context import CURRENT

def observed_time(text,timezone):
    # The existing Dashboard serializes its Asia/Bangkok clock without an
    # offset. Attach the declared provider timezone, never the host locale.
    stamp=datetime.fromisoformat(text.replace('Z','+00:00'))
    return stamp.replace(tzinfo=ZoneInfo(timezone)) if stamp.tzinfo is None else stamp

def freshness_now():
    # A requested historical/future booking date is not the age of the HTTP
    # observation. Keep provider freshness independent of semantic date clocks.
    return datetime.now(ZoneInfo('Asia/Bangkok'))

def answer(reader,need,snap,at,lang,bindings):
    from app.booking import live_status as live
    from .answer import effective
    started=time.perf_counter();records=snap['release']['records'];ctx=CURRENT.get()
    day=live.resolve_live_target_date(need.query,reference_date=at.astimezone(ZoneInfo('Asia/Bangkok')).date())
    cache_key=('wordpress_booking',day)
    observation=ctx.live.get(cache_key) if ctx else None
    if observation is None:
        observation=live.get_live_booking_status(day)
        if ctx:ctx.live[cache_key]=observation
    anchor=next((e['monotonic_value'] for e in reversed(ctx.events) if e.get('stage')=='R124_reference_clock' and e.get('reference_time')==at.isoformat()),started) if ctx else started
    checked=freshness_now()
    elapsed=time.perf_counter()-anchor;groups=live._resource_groups_for_query(observation,need.query)
    selected={resource.resource_id:resource for _,members in groups for resource in members}
    bykey={value(b,'external_resource_key'):b for b in bindings}
    invalid=set(selected)-set(bykey);rows=[];receipts=[]
    # Rendering is scoped to the selected family/station by the same old
    # selector. Every returned provider member must have a pinned binding.
    for key,resource in selected.items():
        b=bykey.get(key)
        if not b:continue
        ttl=value(b,'freshness_max_age_seconds');mapping={x['raw']:x['normalized'] for x in value(b,'status_mapping') or []}
        try:age=(checked-observed_time(observation.generated_at,value(b,'timezone'))).total_seconds()
        except (ValueError,TypeError,AttributeError):age=None
        reason=None
        if not observation.ok:reason=observation.error_code or 'provider_unavailable'
        elif observation.date!=day:reason='observation_date_mismatch'
        elif not effective(b,checked,records):reason='binding_not_effective'
        elif type(ttl) is not int or age is None or not 0<=age<=ttl:reason='stale_or_future_observation'
        normalized=mapping.get(resource.status,'unknown')
        if normalized=='unknown':reason=reason or 'unmapped_provider_status'
        rows.append({'binding_id':b['record_id'],'provider':value(b,'provider'),'resource_key':key,'physical_pool_key':value(b,'physical_pool_key'),
            'provider_status':resource.status,'normalized_status':normalized,'available_now':resource.available_now,'capacity':resource.capacity,
            'observed_at':observation.generated_at,'observed_at_timezone':value(b,'timezone'),'target_date':day,'freshness_checked_at':checked.isoformat(),
            'request_clock_elapsed_seconds':elapsed,'age_seconds':age,'max_age_seconds':ttl,'freshness_checked':reason is None,
            'freshness_clock_basis':'provider_wall_clock',
            'slot_coverage':[],'status':'live_unavailable' if reason else 'supported','reason':reason,
            'window_contract':'legacy_requested_time_window_and_contiguous_slot_renderer'})
        if not reason:
            for key2,f in b['fields'].items():
                if f['status']=='known':receipts.append({'record_id':b['record_id'],'field':key2,'status':'known','evidence_refs':f['evidence_refs']})
    reason=next((r['reason'] for r in rows if r['reason']),None)
    if invalid:reason='selected_provider_resources_not_bound'
    if not observation.ok:reason=observation.error_code or 'provider_unavailable'
    response='answer'
    if reason:
        # Reuse the old unavailable renderer too, preserving the cause rather
        # than treating a failed/old observation as an empty booking list.
        rejected=replace(observation,ok=False,error_code=reason,error=reason)
        body=live.render_live_booking_answer(need.query,rejected,lang);response='live_unavailable';receipts=[]
        configuration_gap=reason in {'selected_provider_resources_not_bound','unmapped_provider_status','binding_not_effective'}
        if observation.ok:
            if configuration_gap:
                body=('ดึงข้อมูลระบบจองได้ แต่การจับคู่บริการหรือสถานะที่ถามยังตรวจยืนยันไม่ได้ จึงยังบอกว่าเครื่องว่างไม่ได้ครับ' if lang=='th' else 'Booking data was received, but the requested service or status mapping is not confirmed. I cannot confirm availability.')
                response='unconfirmed'
            else:
                body=('ดึงข้อมูลระบบจองได้ แต่วันหรือเวลาอัปเดตของข้อมูลไม่ผ่านการตรวจ จึงยังยืนยันเครื่องว่างไม่ได้ครับ' if lang=='th' else 'Booking data was received, but its requested date or update time failed verification. Availability remains unconfirmed.')
            body+='\n'+('แหล่งข้อมูล: ' if lang=='th' else 'Source: ')+live.BOOKING_SOURCE_URL
    else:body=live.render_live_booking_answer(need.query,observation,lang)
    if not selected and observation.ok:
        # The old renderer owns a specific unknown-target clarification. Do
        # not label that as verified occupancy of an empty selected set.
        response='unconfirmed';receipts=[]
    plan={'record_ids':[bykey[k]['record_id'] for k in selected if k in bykey],'requested_fields':[],
        'method':'r124_legacy_live_on_demand','selected_external_resource_ids':list(selected),'target_date':day,
        'legacy_selector':'_resource_groups_for_query','legacy_renderer':'render_live_booking_answer',
        'static_availability_inferred':False,'provider_read_on_demand':True,'live_observations':rows,
        'request_clock_elapsed_seconds':elapsed,'unbound_selected_ids':sorted(invalid)}
    result=reader.finish(snap,started,body,[],plan,receipts,response=response)
    result.decision_artifact['live_booking']={'status':'unavailable' if reason else 'confirmed' if selected else 'unconfirmed',
        'observations':rows,'provider_scope_reads':1,'reason':reason,'source':observation.source,
        'transport':observation.transport,'generated_at':observation.generated_at,'cache_reused':observation.cached or observation.request_reused,
        'provider_payload_ok':observation.ok,'mapping_confirmed':not invalid and not any(r.get('reason')=='unmapped_provider_status' for r in rows),
        'selection_and_rendering':'existing_legacy_functions','semantic_correctness_verified':False}
    return result
