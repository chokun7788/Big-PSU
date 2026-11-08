"""Reuse legacy live selection/window/rendering with current common bindings.

No stored occupancy, startup fetch, sample fallback, or model-generated facts.
"""
import time,re
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
    raw_window=live.requested_time_window(need.query,observation)
    day_wide=day!=at.date().isoformat() and not (raw_window and raw_window.explicit) and not re.search(r'ตอนนี้|ขณะนี้|เวลานี้|\b(?:now|currently)\b',need.query,re.I)
    windows={resource.resource_id:live._slot_window_for_resources(members,raw_window) for _,members in groups for resource in members}
    selected={resource.resource_id:resource for _,members in groups for resource in members}
    bykey={value(b,'external_resource_key'):b for b in bindings}
    invalid=set(selected)-set(bykey);rows=[];receipts=[]
    # A provider subset cannot stand in for an explicitly named station set.
    # Keep missing selections distinct from zero availability or transport.
    missing_resources=[]
    for family,members in groups:
        numbers=live._requested_resource_numbers(need.query,family)
        present={n for n in numbers if any(re.search(rf'#0?{n}(?!\d)',live.normalize_text(r.resource_name)) for r in members)}
        missing_resources.extend((family,n) for n in sorted(numbers-present))
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
        source_fresh=reason is None
        normalized=mapping.get(resource.status,'unknown')
        if normalized=='unknown':reason=reason or 'unmapped_provider_status'
        from .live_window_receipt import build as window_receipt
        window=windows.get(key,raw_window)
        scope=window_receipt(observation,resource,window,raw_window,day_wide,mapping,live._historical_window(observation,window) if window else False)
        if not reason and not scope['decision']['verified']:reason=scope['decision']['reason']
        if not reason:normalized=scope['decision']['normalized_status']
        from .pinned_live_calendar import conflict as calendar_conflict
        calendar=calendar_conflict(snap,b,scope) if not reason else None
        if calendar:reason='recorded_calendar_conflict'
        rows.append({'binding_id':b['record_id'],'provider':value(b,'provider'),'resource_key':key,'physical_pool_key':value(b,'physical_pool_key'),
            'provider_status':resource.status,'normalized_status':normalized,'available_now':resource.available_now,'capacity':resource.capacity,
            'observed_at':observation.generated_at,'observed_at_timezone':value(b,'timezone'),'target_date':day,'freshness_checked_at':checked.isoformat(),
            'request_clock_elapsed_seconds':elapsed,'age_seconds':age,'max_age_seconds':ttl,'freshness_checked':source_fresh,
            'freshness_clock_basis':'provider_wall_clock',
            'slot_coverage':[{'start':slot['start'],'end':slot['end'],'raw_status':slot['status'],'available_count':slot['available_count'],'booked_count':slot['booked_count'],'no_show_count':slot['no_show_count']} for slot in scope['payload']['resource']['slots']],
            'window_receipt':scope,'calendar_crosscheck':calendar,'status':'live_unavailable' if reason else 'supported','reason':reason,
            'window_contract':'verified_requested_window_against_current_request_provider_snapshot'})
        if not reason:
            for key2,f in b['fields'].items():
                if f['status']=='known':receipts.append({'record_id':b['record_id'],'field':key2,'status':'known','evidence_refs':f['evidence_refs']})
    reason=next((r['reason'] for r in rows if r['reason']),None)
    if invalid:
        reason='selected_provider_resources_not_bound'
        for row in rows:row.update(status='live_unavailable',reason=reason)
    if missing_resources:
        reason='requested_provider_resources_not_found'
        for row in rows:row.update(status='live_unavailable',reason=reason)
    if not observation.ok:reason=observation.error_code or 'provider_unavailable'
    response='answer'
    if reason:
        # Reuse the old unavailable renderer too, preserving the cause rather
        # than treating a failed/old observation as an empty booking list.
        rejected=replace(observation,ok=False,error_code=reason,error=reason)
        body=live.render_live_booking_answer(need.query,rejected,lang);response='live_unavailable'
        scope_gap=reason in {'slot_coverage_incomplete','unmapped_provider_slot_status','overlapping_provider_slots','malformed_provider_window_payload','inconsistent_provider_slot_availability','requested_time_window_unresolved'}
        configuration_gap=reason in {'selected_provider_resources_not_bound','requested_provider_resources_not_found','unmapped_provider_status','binding_not_effective'} or scope_gap
        if observation.ok:
            if reason=='recorded_calendar_conflict':
                body=('ข้อมูลช่วงจองจากระบบขัดกับประกาศหรือตารางจองที่มีผลของศูนย์ จึงยังยืนยันสถานะช่วงนี้ไม่ได้ กรุณาตรวจสอบกับศูนย์ครับ' if lang=='th' else 'The provider booking window conflicts with a current studio closure or booking timetable. This period remains unconfirmed; please check with the studio.')
                response='partial_answer'
            elif configuration_gap:
                body=('ดึงข้อมูลระบบจองได้ แต่ข้อมูลช่วงเวลาหรือการจับคู่บริการยังยืนยันไม่ครบ จึงยังบอกว่าว่างหรือถูกจองไม่ได้ครับ' if lang=='th' else 'Booking data was received, but its requested window or service mapping is incomplete. Neither free nor occupied status can be confirmed.')
                response='unconfirmed'
            else:
                body=('ดึงข้อมูลระบบจองได้ แต่วันหรือเวลาอัปเดตของข้อมูลไม่ผ่านการตรวจ จึงยังยืนยันเครื่องว่างไม่ได้ครับ' if lang=='th' else 'Booking data was received, but its requested date or update time failed verification. Availability remains unconfirmed.')
            body+='\n'+('แหล่งข้อมูล: ' if lang=='th' else 'Source: ')+live.BOOKING_SOURCE_URL
            unresolved=[selected[r['resource_key']].resource_name for r in rows if r.get('reason') and r['resource_key'] in selected]
            if unresolved:body+='\n'+('ยังยืนยันไม่ได้: ' if lang=='th' else 'Still unconfirmed: ')+', '.join(unresolved)
        valid_keys={r['resource_key'] for r in rows if not r.get('reason')}
        if observation.ok and valid_keys and not invalid and not missing_resources:
            subset=replace(observation,resources=tuple(r for r in observation.resources if r.resource_id in valid_keys))
            shown=live.render_live_booking_answer(need.query+(' ตารางจอง' if day_wide else ''),subset,lang,calendar_check=lambda *_:None)
            body=('เฉพาะเครื่องที่ตรวจข้อมูลครบ:\n' if lang=='th' else 'Verified resource subset only:\n')+shown+'\n\n'+body;response='partial_answer'
        else:receipts=[]
    else:
        render_query=need.query
        # A future/past date without a time asks about that day's slots. Do
        # not silently apply the current wall-clock hour to the other date.
        if day_wide:render_query+=' ตารางจอง'
        body=live.render_live_booking_answer(render_query,observation,lang,calendar_check=lambda *_:None)
    if not selected and observation.ok:
        # The old renderer owns a specific unknown-target clarification. Do
        # not label that as verified occupancy of an empty selected set.
        response='unconfirmed';receipts=[]
    plan={'record_ids':[bykey[k]['record_id'] for k in selected if k in bykey],'requested_fields':[],
        'method':'r124_legacy_live_on_demand','selected_external_resource_ids':list(selected),'target_date':day,
        'legacy_selector':'_resource_groups_for_query','legacy_renderer':'render_live_booking_answer',
        'static_availability_inferred':False,'provider_read_on_demand':True,'live_observations':rows,
        'date_without_time_scope':'day_slots' if not reason and day_wide else 'requested_window',
        'request_clock_elapsed_seconds':elapsed,'unbound_selected_ids':sorted(invalid)}
    result=reader.finish(snap,started,body,[],plan,receipts,response=response)
    result.decision_artifact['live_booking']={'status':'partial' if response=='partial_answer' else 'unavailable' if reason else 'confirmed' if selected else 'unconfirmed',
        'observations':rows,'provider_scope_reads':1,'reason':reason,'source':observation.source,
        'transport':observation.transport,'generated_at':observation.generated_at,'cache_reused':observation.cached or observation.request_reused,
        'provider_payload_ok':observation.ok,'mapping_confirmed':not invalid and not any(r.get('reason')=='unmapped_provider_status' for r in rows),
        'selection_and_rendering':'existing_legacy_functions','semantic_correctness_verified':False}
    return result
