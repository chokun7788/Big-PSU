"""Recorded weekday-set scope, independent of a rendered calendar or model."""
import re,copy
from datetime import date
from .scope import reference_time,validity_allows,requested_years,in_year
from .projection import value

def weekly_requested(question):
    return bool(re.search(r'เปิด.*(?:วันไหน|วันอะไร|กี่วัน)|(?:what|which)\s+days?\b|\bwhat\s+are\s+(?:the\s+)?(?:studio\s+)?(?:service\s+)?days?\b|days?\s+(?:is|are).{0,25}\bopen\b|weekly|ทั้งสัปดาห์|ทุกวันในสัปดาห์|ทุกสัปดาห์|รายสัปดาห์',question,re.I))

def requested_weekdays(question):
    from .service_calendar import WEEKDAYS
    hits=sorted((m.start(),m.end(),day) for day,pattern in enumerate(WEEKDAYS) for m in re.finditer(r'(?<![a-z])(?:'+pattern+r')(?![a-z])',question,re.I))
    if not hits:return list(range(7))
    days=[]
    for n,(start,end,day) in enumerate(hits):
        if day not in days:days.append(day)
        if n+1<len(hits) and re.fullmatch(r'\s*(?:to|through|until|ถึง(?:วัน)?|[-–])\s*',question[end:hits[n+1][0]],re.I):
            target=hits[n+1][2];cursor=day if target==day else (day+1)%7
            while cursor!=target:
                if cursor not in days:days.append(cursor)
                cursor=(cursor+1)%7
    return days

def scope_clock(question,at):
    at=reference_time(at)
    match=re.search(r'(?<!\d)(20\d\d-\d\d-\d\d)(?!\d)',question)
    if match:
        day=date.fromisoformat(match[1]);return at.replace(year=day.year,month=day.month,day=day.day)
    years=requested_years(question)
    return in_year(at,next(iter(years))) if len(years)==1 else at

def source_set(index,facet,question,at,days=None):
    from .service_calendar import requested_zones,applies
    zones=requested_zones(index,question);clock=scope_clock(question,at)
    days=requested_weekdays(question) if days is None else days
    all_facts=[f for f in index.bycat['C11'] if f['facet']==facet and index.records.get(f['record_id'],{}).get('kind')=='schedule' and type(value(index.records[f['record_id']],'weekday')) is int and value(index.records[f['record_id']],'weekday') in days]
    scoped=[f for f in all_facts if applies(index.records[f['record_id']],zones) is not False]
    facts=[f for f in scoped if validity_allows(index.records[f['record_id']],clock) is not False]
    return {'facts':facts,'expired_fact_ids':[f['id'] for f in scoped if f not in facts],'scope_clock':clock.isoformat(),'requested_zone_ids':sorted(zones),'requested_weekdays':days}

def describe(index,facts,question):
    from .service_calendar import requested_zones,applies
    zones=requested_zones(index,question);limits=[];periods=[]
    for fact in facts:
        record=index.records[fact['record_id']];validity=record.get('validity') or {}
        if validity.get('state')!='known':limits.append('effective_period_unknown')
        if applies(record,zones) is None:limits.append('resource_applicability_unconfirmed')
        if record.get('fields',{}).get('timezone',{}).get('status')!='known':limits.append('timezone_unconfirmed')
        periods.append({'record_id':record['record_id'],'record_revision':record['revision'],'validity':copy.deepcopy(validity),'zone_ids':copy.deepcopy(value(record,'zone_ids'))})
    return {'limits':sorted(set(limits)),'source_periods':periods}

def weekly_plan(index,facet,question,at,reason,play_service=False,days=None):
    from .readers import confirmed,blocked
    from ..calendar_slots import errors as slot_errors
    try:source=source_set(index,facet,question,at,days)
    except ValueError:return blocked('C11','invalid_calendar_date','missing_input')
    facts=source['facts']
    if not facts:return blocked('C11','weekly_calendar_not_current' if source['expired_fact_ids'] else 'weekly_calendar_missing_source','not_current' if source['expired_fact_ids'] else 'missing_source')
    days=source['requested_weekdays'];groups={day:[f for f in facts if value(index.records[f['record_id']],'weekday')==day] for day in days}
    # Different versions/scopes for one weekday are not a canonical calendar.
    selected=[groups[day][0] for day in days if len(groups[day])==1]
    if not selected:return blocked('C11','weekly_calendar_scope_or_version_unresolved')
    if play_service:
        issues=[issue for f in selected for issue in slot_errors(f.get('service_slots'),f.get('service_closed'))]
        if issues:
            from .service_calendar import invalid_source
            return invalid_source(issues)
    missing=[day for day in days if not groups[day]];conflicted=[day for day in days if len(groups[day])>1]
    description=describe(index,selected,question)
    result=confirmed('C11',selected,reason,operator='list',complete_set=not missing and not conflicted,weekday_count=len(days),
        requested_weekdays=days,weekly_missing_weekdays=missing,weekly_conflicting_weekdays=conflicted,
        calendar_source_limits=description['limits'],calendar_source_periods=description['source_periods'],calendar_scope_clock=source['scope_clock'],
        calendar_collection_basis='all_current_recorded_weekday_fields_for_requested_scope_not_live_or_world_completeness')
    if play_service:result.metadata['calendar_semantics']='play_service_only_not_physical_building_hours_or_live_occupancy'
    if missing or conflicted or description['limits']:result.status='partial'
    result.locked=True
    return result

def verify_metadata(index,task,claims,metadata,question,at):
    if task.facet=='service_periods':
        from .period_scope import verify
        return verify(index,task,claims,metadata,question,at)
    if not weekly_requested(question):return False
    play=metadata.get('calendar_semantics')=='play_service_only_not_physical_building_hours_or_live_occupancy'
    if play:
        from .service_calendar import plan
        expected=plan(index,question,reference_time(at))
    else:expected=weekly_plan(index,task.facet,question,at,'recorded_weekly_calendar_field')
    if not expected or set(expected.ids)!={c.get('fact_id') for c in claims}:return False
    keys=('operator','complete_set','weekday_count','requested_weekdays','weekly_missing_weekdays','weekly_conflicting_weekdays','calendar_source_limits','calendar_source_periods','calendar_scope_clock','calendar_collection_basis','calendar_semantics')
    return all(metadata.get(k)==expected.metadata.get(k) for k in keys)
