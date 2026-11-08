"""Compare provider bookability with current, scoped pinned owner declarations.

Play-service timetables, unknown effective dates and unknown zone scope do not
establish a contradictory booking policy. No global calendar file is consulted.
"""
from datetime import datetime,date,time,timedelta
from zoneinfo import ZoneInfo
from .registry import value,aware

def conflict(snapshot,binding,receipt):
    p=receipt.get('payload',{});window=receipt.get('effective_window')
    if receipt.get('scope_kind') in {'historical_range','day_slots'} or not window or not p.get('center_open'):return None
    day=date.fromisoformat(receipt['target_date']);at=datetime.combine(day,time.fromisoformat(window['start']),tzinfo=ZoneInfo('Asia/Bangkok'))
    records=snapshot['release']['records'];resource=records.get(value(binding,'physical_pool_key'),{});zone=value(resource,'zone_id') if resource else None
    candidates=[]
    for rid,r in records.items():
        if r['kind'] not in {'schedule','closure'} or rid in snapshot.get('withdrawn',[]):continue
        validity=r.get('validity',{})
        if validity.get('state')!='known':continue
        if validity.get('effective_from') and at<aware(validity['effective_from']) or validity.get('effective_until') and at>=aware(validity['effective_until']):continue
        if window.get('end') and validity.get('effective_until'):
            end=window['end'];end_at=datetime.combine(day,time.min,tzinfo=at.tzinfo)+timedelta(minutes=int(end[:2])*60+int(end[3:]))
            if end_at>aware(validity['effective_until']):continue
        if r['fields'].get('zone_ids',{}).get('status')!='known':continue
        zones=value(r,'zone_ids')
        if zones!=[] and (zone is None or zone not in (zones or [])):continue
        if r['kind']=='closure' and value(r,'local_date')==day.isoformat() and value(r,'state')=='closed':
            candidates.append((rid,'state','current_scoped_special_closure'));continue
        if r['kind']=='schedule' and value(r,'weekday')==day.weekday() and r['fields'].get('bookable_periods',{}).get('status')=='known':
            periods=value(r,'bookable_periods') or [];start=window['start'];end=window.get('end')
            from .calendar_slots import covers
            if not covers([(s['start'],s['end']) for s in periods],start,end):candidates.append((rid,'bookable_periods','current_scoped_booking_period_disagrees'))
    if not candidates:return None
    refs=[ref for rid,key,_ in candidates for ref in records[rid]['fields'][key].get('evidence_refs',[])]
    if not refs:return None
    return {'version':'pinned-live-calendar-v1','reason':'recorded_calendar_conflict','record_ids':[rid for rid,_,_ in candidates],'fields':[key for _,key,_ in candidates],'basis':[reason for _,_,reason in candidates],'evidence_refs':refs,'target_date':day.isoformat(),'requested_window':window,'snapshot':{'release_id':snapshot['active'],'epoch':snapshot['epoch']},'authority_winner_selected':False}
