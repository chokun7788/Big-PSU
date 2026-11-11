"""Recorded play-service state, distinct from physical building hours/live use."""
import re
from datetime import timedelta,date
from .readers import confirmed,blocked
from .scope import norm,contains
from .projection import value,bilingual
def explicit_window(question):
    match=re.search(r'(?<!\d)(\d{1,2}):(\d{2})(?:\s*[-–]\s*(\d{1,2}):(\d{2}))?(?!\d)',question)
    if not match:return None
    start=f'{int(match[1]):02}:{match[2]}';end=f'{int(match[3]):02}:{match[4]}' if match[3] is not None else None
    from ..live_window_receipt import minutes
    a=minutes(start);b=minutes(end,True) if end else None
    if b is not None and b<=a:raise ValueError('calendar_window_requires_increasing_same_day_times')
    return {'start':start,'end':end,'source_quote':match[0]}

def covers(slots,start,end=None):
    if end is None:return any(s['state']=='open' and s['start']<=start<s['end'] for s in slots)
    cursor=start
    for slot in sorted((s for s in slots if s['state']=='open' and s['start']<end and s['end']>start),key=lambda s:s['start']):
        if slot['start']>cursor:return False
        cursor=max(cursor,slot['end'])
    return cursor>=end

def overlaps(slot,start,end=None):
    return slot['start']<end and slot['end']>start if end else slot['start']<=start<slot['end']
WEEKDAYS=[r'จันทร์|mondays?',r'อังคาร|tuesdays?',r'พุธ|wednesdays?',r'พฤหัส(?:บดี)?|thursdays?',r'ศุกร์|fridays?',r'เสาร์|saturdays?',r'อาทิตย์|sundays?']

def requested_zones(index,q):
    from .projection import title
    matches=[]
    for rid,r in index.records.items():
        if r.get('kind') not in {'zone','resource','service'}:continue
        lengths=[len(norm(s)) for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])] if contains(q,s)]
        if lengths:matches.append((max(lengths),rid,r))
    zones=set()
    for _,rid,r in matches:
        z=[rid] if r['kind']=='zone' else value(r,'zone_ids') or ([value(r,'zone_id')] if value(r,'zone_id') else [])
        zones.update(z)
    return zones

def applies(record,zones):
    field=record.get('fields',{}).get('zone_ids',{})
    if field.get('status')!='known':return None
    scope=field.get('value')
    if scope==[]:return True
    if zones:return zones<=set(scope or [])
    return None

def invalid_source(issues):
    result=blocked('C11','recorded_service_calendar_invalid')
    result.metadata.update(source_validation_issues=issues,execution_notice={'th':'ตารางบริการที่บันทึกไว้ยังมีช่วงเวลาที่ไม่ชัดเจนหรือซ้อนกัน จึงยังยืนยันเวลาให้บริการไม่ได้ครับ','en':'The recorded service timetable contains invalid or overlapping periods, so service hours cannot be confirmed.'})
    return result
def plan(index,q,at):
    q=norm(q)
    if not re.search(r'เปิด|ปิด|เข้าไปเล่น.*ช่วงไหน|opening|\bopen\b|\bclosed\b',q):return None
    if re.search(r'อาคาร|พื้นที่.*เปิด|physical|building',q):return None
    # A weekly request has no single weekday to bind. Project every recorded
    # weekday rather than treating an empty booking list as closed service.
    from .calendar_sets import weekly_requested
    if weekly_requested(q):
        from .calendar_sets import weekly_plan
        return weekly_plan(index,'service_periods',q,at,'recorded_weekly_play_service_calendar',play_service=True)
    days=[i for i,p in enumerate(WEEKDAYS) if re.search(p,q,re.I)]
    target=None;dated=False
    explicit=re.search(r'(?<!\d)(20\d\d-\d\d-\d\d)(?!\d)',q)
    if explicit:
        try:target=date.fromisoformat(explicit[1]);dated=True
        except ValueError:return blocked('C11','invalid_calendar_date','missing_input')
    elif re.search(r'วันนี้|ตอนนี้|\btoday\b|\bnow\b',q):target=at.date();dated=True
    elif re.search(r'พรุ่งนี้|\btomorrow\b',q):target=at.date()+timedelta(days=1);dated=True
    try:window=explicit_window(q)
    except ValueError:return blocked('C11','invalid_calendar_time_window','missing_input')
    if target:days=[target.weekday()]
    if len(days)!=1:
        if window:
            result=blocked('C11','calendar_day_required_for_time','missing_input');result.metadata['context_clarification']={'th':'ต้องการตรวจวันหรือวันที่ใดครับ? เวลาให้บริการอาจต่างกันตามวัน','en':'Which day or date should I check? Service hours may differ by day.'};return result
        return None
    day=days[0];zones=requested_zones(index,q)
    fs=[f for f in index.bycat['C11'] if f['facet']=='service_periods' and f.get('weekday')==day and applies(index.records[f['record_id']],zones) is not False]
    if len(fs)!=1:return blocked('C11','calendar_weekday_scope_or_version_unresolved')
    selected=fs[0];slots=selected['service_slots'];period=None
    from ..calendar_slots import errors as calendar_slot_errors
    issues=calendar_slot_errors(slots,selected.get('service_closed'))
    if issues:return invalid_source(issues)
    from .scope import validity_allows
    scope_at=at.replace(year=target.year,month=target.month,day=target.day) if target else at
    if window:scope_at=scope_at.replace(hour=int(window['start'][:2]),minute=int(window['start'][3:]),second=0,microsecond=0)
    if dated and target.year!=at.year and validity_allows(selected,scope_at) is not True:return blocked('C11','calendar_effective_year_not_confirmed','not_current')
    if validity_allows(selected,scope_at) is False:return blocked('C11','calendar_effective_interval_not_current','not_current')
    if window and window['end'] and selected.get('validity',{}).get('effective_until'):
        from ..registry import aware
        end_at=scope_at.replace(hour=0,minute=0)+timedelta(minutes=int(window['end'][:2])*60+int(window['end'][3:]))
        if end_at>aware(selected['validity']['effective_until']):return blocked('C11','calendar_window_exceeds_effective_interval','not_current')
    if re.search(r'เช้า|\bmorning\b',q):period='morning'
    elif re.search(r'บ่าย|\bafternoon\b',q):period='afternoon'
    scoped=[s for s in slots if not period or s.get('code')==period]
    if window:
        start=window['start'];end=window['end']
        if period and not any(overlaps(s,start,end) for s in scoped) and any(s['start']<=start<s['end'] for s in slots):
            result=blocked('C11','calendar_period_and_time_conflict','missing_input');result.metadata['context_clarification']={'th':'ช่วงเช้า/บ่ายกับเวลาที่ระบุตรงกันไม่ชัดเจน ต้องการตรวจช่วงใดครับ?','en':'The named day period and clock time conflict. Which time should I check?'};return result
        scoped=[s for s in scoped if overlaps(s,start,end)]
    now_asked=bool(re.search(r'ตอนนี้|\bright now\b|\bnow\b',q)) and not window
    if now_asked:
        clock=at.strftime('%H:%M');scoped=[s for s in scoped if s['start']<=clock<s['end']]
    closure=None;unconfirmed_closures=[]
    if dated:
        candidates=[r for r in index.records.values() if r['kind']=='closure' and value(r,'local_date')==target.isoformat() and value(r,'state')=='closed' and validity_allows(r,scope_at) is not False]
        closure=next((r for r in candidates if applies(r,zones) is True and validity_allows(r,scope_at) is True),None)
        unconfirmed_closures=[r['record_id'] for r in candidates if applies(r,zones) is None or validity_allows(r,scope_at) is None]
    prefix={'th':('วันที่ '+target.isoformat()+' ' if dated else ''),'en':(target.isoformat()+' ' if dated else '')}
    if closure:
        texts={'th':prefix['th']+'ปิดบริการตามประกาศปิดพิเศษ','en':prefix['en']+'Closed under the recorded special closure.'}
        extra=[f for f in index.bycat['C11'] if f['record_id']==closure['record_id'] and f['facet'] in {'local_date','reason'}]
    elif not scoped:
        texts={'th':prefix['th']+('อยู่นอกช่วงให้บริการเล่นที่บันทึกไว้' if now_asked and slots else 'ปิดบริการเล่นตามตารางประจำ'),
               'en':prefix['en']+('Outside the recorded play-service periods.' if now_asked and slots else 'Closed for play under the regular timetable.')};extra=[]
    elif all(s['state']=='maintenance' for s in scoped):
        times=', '.join(s['start']+'–'+s['end'] for s in scoped)
        texts={'th':prefix['th']+'ไม่เปิดให้บริการเล่นช่วง '+times+' เนื่องจากบำรุงรักษาตามตาราง',
               'en':prefix['en']+'Not open for play during '+times+'; scheduled maintenance.'};extra=[]
    else:
        open_times=', '.join(s['start']+'–'+s['end'] for s in scoped if s['state']=='open')
        maintenance=', '.join(s['start']+'–'+s['end'] for s in scoped if s['state']=='maintenance')
        texts={'th':prefix['th']+'เปิดให้บริการเล่นตามตาราง '+open_times+('; บำรุงรักษา '+maintenance if maintenance else ''),
               'en':prefix['en']+'Open for play under the recorded timetable: '+open_times+('; maintenance '+maintenance if maintenance else '')};extra=[]
    from app.calendar.service_calendar import THAI_WEEKDAYS,thai_month_name
    if dated:
        date_th=f'{THAI_WEEKDAYS[day]}ที่ {target.day} {thai_month_name(target.month)} {target.year+543}'
        date_en=target.strftime('%A, %d %B %Y')
    else:date_th=THAI_WEEKDAYS[day];date_en=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'][day]
    playable=[s for s in scoped if s['state']=='open']
    if closure:
        customer={'th':date_th+' **ปิดให้บริการ** ตามประกาศปิดพิเศษครับ','en':date_en+' — **Closed** under the recorded special closure.'}
    elif playable:
        periods=', '.join(s['start']+'–'+s['end'] for s in playable)
        customer={'th':date_th+' **เปิดให้บริการ** เวลา '+periods+' น. ตามตารางบริการครับ','en':date_en+' — **Open** '+periods+' under the service timetable.'}
    else:
        reason='เนื่องจากเป็นช่วงบำรุงรักษา' if scoped and all(s['state']=='maintenance' for s in scoped) else 'ในเวลานี้' if now_asked else 'ตามตารางบริการ'
        customer={'th':date_th+' **ไม่เปิดให้บริการ**'+(' '+reason)+'ครับ','en':date_en+' — **Closed for play** '+('during scheduled maintenance.' if scoped and all(s['state']=='maintenance' for s in scoped) else 'at this time.' if now_asked else 'under the service timetable.')}
    window_evaluation=None
    if window:
        open_entire=not closure and covers(slots,window['start'],window['end'])
        stamp=window['start']+('–'+window['end'] if window['end'] else '')
        window_evaluation={'requested_window':window,'open_entire_window':open_entire,'source_fact_ids':[selected['id'],*[f['id'] for f in extra]],'source_weekday':day,'source_clock_timezone':'Asia/Bangkok','basis':'contiguous_recorded_open_service_slots_with_special_closure_precedence','live_or_physical_building_status_claimed':False}
        texts={'th':prefix['th']+('เปิดให้บริการเล่นตลอดช่วง ' if window['end'] and open_entire else 'ไม่เปิดให้บริการเล่นตลอดช่วง ' if window['end'] else 'เปิดให้บริการเล่น ณ ' if open_entire else 'ไม่เปิดให้บริการเล่น ณ ')+stamp+' ตามตารางที่บันทึกไว้',
               'en':prefix['en']+('Open for play for the whole period ' if window['end'] and open_entire else 'Not open for play for the whole period ' if window['end'] else 'Open for play at ' if open_entire else 'Closed for play at ')+stamp+' under the recorded timetable.'}
        customer={'th':date_th+' — '+texts['th'],'en':date_en+' — '+texts['en']}
    result=confirmed('C11',[selected,*extra],'recorded_play_service_calendar',calendar_service_answer=texts,customer_calendar_answer=customer,
                     calendar_service_fact_id=selected['id'],calendar_semantics='play_service_only_not_physical_building_hours_or_live_occupancy',
                     local_date=target.isoformat() if dated else None,weekday=day,calendar_window_evaluation=window_evaluation)
    opening=index.records[selected['record_id']].get('fields',{}).get('open_periods',{})
    # A service timetable remains useful, but cannot silently resolve a
    # conflicting/unknown physical opening field in a broad "open?" request.
    explicit_play=bool(re.search(r'บริการเล่น|เข้าไปเล่น|ให้เล่น|for play|play.service|bookable|booking periods|ช่วงจอง',q,re.I))
    opening_status=opening.get('status','unknown')
    if not explicit_play and not closure and opening_status in {'conflicted','unknown'}:
        warning={'th':'ช่วงเวลาเปิดพื้นที่ในต้นทางยังขัดแย้งกัน ยืนยันได้เฉพาะตารางบริการเล่นด้านล่างครับ' if opening_status=='conflicted' else 'ช่วงเวลาเปิดพื้นที่ยังไม่มีข้อมูลยืนยัน ยืนยันได้เฉพาะตารางบริการเล่นด้านล่างครับ',
                 'en':'Physical opening hours conflict in the recorded source. The timetable below confirms play-service periods only.' if opening_status=='conflicted' else 'Physical opening hours are unconfirmed. The timetable below confirms play-service periods only.'}
        for lang in ['th','en']:
            texts[lang]=warning[lang]+'\n'+texts[lang];customer[lang]=warning[lang]+'\n'+customer[lang]
        result.metadata['opening_field_scope_warning']={'record_id':selected['record_id'],'revision':index.records[selected['record_id']]['revision'],'field':'open_periods','status':opening_status,'play_slots_do_not_resolve_opening_field':True}
        result.status='partial'
    limits=[]
    if selected.get('validity',{}).get('state')!='known':limits.append('effective_period_unknown')
    if applies(index.records[selected['record_id']],zones) is None:limits.append('resource_applicability_unconfirmed')
    if unconfirmed_closures:limits.append('special_closure_applicability_unconfirmed');result.metadata['unconfirmed_closure_record_ids']=unconfirmed_closures
    if limits:result.status='partial';result.metadata['calendar_source_limits']=['recorded_play_service_only',*limits]
    result.locked=True;return result
