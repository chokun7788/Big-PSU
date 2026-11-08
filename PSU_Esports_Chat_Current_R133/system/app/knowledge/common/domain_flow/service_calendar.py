"""Recorded play-service state, distinct from physical building hours/live use."""
import re
from datetime import timedelta,date
from .readers import confirmed,blocked
from .scope import norm,contains
from .projection import value,bilingual
WEEKDAYS=[r'จันทร์|mondays?',r'อังคาร|tuesdays?',r'พุธ|wednesdays?',r'พฤหัส|thursdays?',r'ศุกร์|fridays?',r'เสาร์|saturdays?',r'อาทิตย์|sundays?']
def plan(index,q,at):
    q=norm(q)
    if not re.search(r'เปิด|ปิด|เข้าไปเล่น.*ช่วงไหน|opening|\bopen\b|\bclosed\b',q):return None
    if re.search(r'อาคาร|พื้นที่.*เปิด|physical|building',q):return None
    # A weekly request has no single weekday to bind. Project every recorded
    # weekday rather than treating an empty booking list as closed service.
    if re.search(r'เปิด.*(?:วันไหน|วันอะไร|กี่วัน)|(?:what|which)\s+days?\b|days?\s+(?:is|are).{0,25}\bopen\b|weekly|ทั้งสัปดาห์',q,re.I):
        fs=[f for f in index.bycat['C11'] if f['facet']=='service_periods']
        grouped={day:[f for f in fs if f.get('weekday')==day] for day in range(7)}
        if any(len(v)!=1 for v in grouped.values()):return blocked('C11','weekly_calendar_missing_or_conflicting_weekday')
        selected=[grouped[day][0] for day in range(7)]
        result=confirmed('C11',selected,'recorded_weekly_play_service_calendar',
            calendar_semantics='play_service_only_not_physical_building_hours_or_live_occupancy',
            calendar_source_limits=['recorded_play_service_only','resource_applicability_unconfirmed','effective_period_unknown'],
            requested_resource_context=q,complete_set=True,weekday_count=7)
        result.status='partial';result.locked=True
        return result
    days=[i for i,p in enumerate(WEEKDAYS) if re.search(p,q,re.I)]
    target=None;dated=False
    explicit=re.search(r'(?<!\d)(20\d\d-\d\d-\d\d)(?!\d)',q)
    if explicit:
        try:target=date.fromisoformat(explicit[1]);dated=True
        except ValueError:return blocked('C11','invalid_calendar_date','missing_input')
    elif re.search(r'วันนี้|ตอนนี้|\btoday\b|\bnow\b',q):target=at.date();dated=True
    elif re.search(r'พรุ่งนี้|\btomorrow\b',q):target=at.date()+timedelta(days=1);dated=True
    if target:days=[target.weekday()]
    if len(days)!=1:return None
    day=days[0];fs=[f for f in index.bycat['C11'] if f['facet']=='service_periods' and f.get('weekday')==day]
    if len(fs)!=1:return None
    selected=fs[0];slots=selected['service_slots'];period=None
    if re.search(r'เช้า|\bmorning\b',q):period='morning'
    elif re.search(r'บ่าย|\bafternoon\b',q):period='afternoon'
    scoped=[s for s in slots if not period or s.get('code')==period]
    now_asked=bool(re.search(r'ตอนนี้|\bright now\b|\bnow\b',q))
    if now_asked:
        clock=at.strftime('%H:%M');scoped=[s for s in scoped if s['start']<=clock<s['end']]
    closure=None
    if dated:
        closure=next((r for r in index.records.values() if r['kind']=='closure' and value(r,'local_date')==target.isoformat() and value(r,'state')=='closed'),None)
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
    result=confirmed('C11',[selected,*extra],'recorded_play_service_calendar',calendar_service_answer=texts,customer_calendar_answer=customer,
                     calendar_service_fact_id=selected['id'],calendar_semantics='play_service_only_not_physical_building_hours_or_live_occupancy',
                     local_date=target.isoformat() if dated else None,weekday=day)
    result.locked=True;return result
