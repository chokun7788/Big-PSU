"""Recorded play-service state, distinct from physical building hours/live use."""
import re
from datetime import timedelta,date
from .readers import confirmed,blocked
from .scope import norm,contains
from .projection import value,bilingual
WEEKDAYS=[r'จันทร์|mondays?',r'อังคาร|tuesdays?',r'พุธ|wednesdays?',r'พฤหัส|thursdays?',r'ศุกร์|fridays?',r'เสาร์|saturdays?',r'อาทิตย์|sundays?']
def plan(index,q,at):
    q=norm(q)
    if not re.search(r'เปิด|ปิด|opening|\bopen\b|\bclosed\b',q):return None
    if re.search(r'อาคาร|พื้นที่.*เปิด|physical|building',q):return None
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
    result=confirmed('C11',[selected,*extra],'recorded_play_service_calendar',calendar_service_answer=texts,
                     calendar_service_fact_id=selected['id'],calendar_semantics='play_service_only_not_physical_building_hours_or_live_occupancy',
                     local_date=target.isoformat() if dated else None,weekday=day)
    result.locked=True;return result
