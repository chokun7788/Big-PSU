"""Native named play-period lookup; never a bookable-period wire alias.

The retained r129-plan-v2 model cannot emit this facet. This adapter derives
only quoted period/day scope and reads current owner service_slots.
"""
import copy,re
from datetime import date,timedelta
from .projection import value
from .scope import reference_time,validity_allows

PERIODS={'morning':r'\bmorning\b|รอบเช้า|ช่วงเช้า',
         'afternoon':r'\bafternoon\b|รอบบ่าย|ช่วงบ่าย'}
DAY_NAMES={'en':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
           'th':['จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์','อาทิตย์']}

def request(index,question):
    from .named_spans import masked
    q=masked(index,question)
    spans=[{'code':code,'start':m.start(),'end':m.end(),'text':question[m.start():m.end()]}
           for code,pattern in PERIODS.items() for m in re.finditer(pattern,q,re.I)]
    if re.search(r'\b(?:sessions?|slots?|periods?)\b|รอบ|ช่วง',q,re.I):
        names={s.get(k) for r in index.records.values() if r.get('kind')=='schedule'
               for s in value(r,'service_slots') or [] for k in ('code','label') if isinstance(s.get(k),str) and s[k].strip()}
        for name in sorted(names):
            if any(re.search(pattern,name,re.I) for pattern in PERIODS.values()):continue
            boundary=r'(?<![a-z0-9_])' if re.search('[a-z0-9_]',name[:1],re.I) else ''
            end=r'(?![a-z0-9_])' if re.search('[a-z0-9_]',name[-1:],re.I) else ''
            for m in re.finditer(boundary+re.escape(name)+end,q,re.I):
                spans.append({'code':name,'start':m.start(),'end':m.end(),'text':question[m.start():m.end()]})
    if not spans or not re.search(r'\b(?:what time|when|hours?|times?)\b|กี่โมง|เวลา|ช่วงไหน',q,re.I):return None
    explicit_play_time=bool(re.search(r'\bwhen\b[^?.;]{0,55}\bplay\b|\bplay\b[^?.;]{0,40}\b(?:when|what time)\b|(?:กี่โมง|เวลา|ช่วงไหน).{0,35}เล่น|เล่น.{0,35}(?:กี่โมง|เวลา|ช่วงไหน)',q,re.I))
    if not explicit_play_time and not re.search(r'\b(?:sessions?|slots?|periods?)\b|รอบ|ช่วง',q,re.I):return None
    # These predicates have different authorities. A named period mention
    # cannot make them a timetable request.
    if re.search(r'ราคา|กี่บาท|จอง|ว่าง|อาคาร|ตึก|ติดต่อ|ลงทะเบียน|\b(?:price|cost|fee|pay|book|booking|bookable|reserve|vacan\w*|available|building|occupied|rules?|registration|deadline|contact|office|tournament|compare|versus|longer|shorter)\b',q,re.I):return None
    return {'periods':list(dict.fromkeys(s['code'] for s in sorted(spans,key=lambda s:s['start']))),
            'spans':sorted(spans,key=lambda s:s['start'])}

def day_scope(question,at):
    from .calendar_sets import requested_weekdays
    from .service_calendar import WEEKDAYS
    clock=reference_time(at);dates=re.findall(r'(?<!\d)20\d\d-\d\d-\d\d(?!\d)',question)
    relative=[m[0].lower() for m in re.finditer(r'\btoday\b|\btomorrow\b|วันนี้|พรุ่งนี้',question,re.I)]
    if len(set(dates))>1 or len(set(relative))>1 or dates and relative:raise ValueError('named_period_requires_one_date')
    target=date.fromisoformat(dates[0]) if dates else (clock.date()+timedelta(days=int(relative[0] in {'tomorrow','พรุ่งนี้'}))) if relative else None
    if not target and re.search(r'(?<!\d)(?:20\d\d|25\d\d)(?!\d)',question):raise ValueError('named_period_year_scope_requires_date')
    weekdays=requested_weekdays(question)
    if target:
        if any(re.search(p,question,re.I) for p in WEEKDAYS) and set(weekdays)!={target.weekday()}:raise ValueError('named_period_date_weekday_conflict')
        clock=clock.replace(year=target.year,month=target.month,day=target.day)
        weekdays=[target.weekday()]
    return {'requested_weekdays':weekdays,'local_date':target.isoformat() if target else None,
            'scope_clock':clock.isoformat(),'date_basis':'explicit_date' if dates else 'reference_clock_relative_date' if relative else 'recorded_weekday_set'}

def plan(index,question,at):
    from .readers import blocked
    from .calendar_sets import weekly_plan
    from .service_calendar import applies,requested_zones
    req=request(index,question)
    if req is None:return None
    try:scope=day_scope(question,at)
    except ValueError as exc:return hold(str(exc),'missing_input')
    # Do not quietly discard extra clock, conditional, comparison or annual
    # scopes that this finite adapter cannot yet project.
    if re.search(r'\d{1,2}:\d{2}|\b(?:if|unless|except|not|now|currently|before|after|in\s+20\d\d)\b|ถ้า|หาก|ยกเว้น|ตอนนี้|ก่อน|หลัง|ปี\s*\d',question,re.I):
        return hold('named_period_additional_scope_requires_review','missing_input')
    clock=reference_time(scope['scope_clock']);zones=requested_zones(index,question)
    if scope['local_date']:
        special=[r for r in index.records.values() if r.get('kind')=='closure' and value(r,'local_date')==scope['local_date'] and applies(r,zones) is not False and validity_allows(r,clock) is not False]
        # A physical-hours exception cannot be silently relabelled as a named
        # service slot. Keep the dated exception explicit and unfulfilled.
        if special:return hold('named_period_dated_exception_requires_service_scope_review','missing_source')
    result=weekly_plan(index,'service_periods',question,clock,'native_named_play_periods',play_service=True,days=scope['requested_weekdays'])
    if not result.ids:return result
    rows=[]
    for fid in result.ids:
        fact=index.byid[fid];record=index.records[fact['record_id']]
        rows.append({'fact_id':fid,'record_id':record['record_id'],'record_revision':record['revision'],
            'weekday':value(record,'weekday'),'service_closed':value(record,'service_closed'),
            'slots':[copy.deepcopy(s) for s in value(record,'service_slots') if any(slot_matches(s,key) for key in req['periods'])],
            'unidentified_periods':any(not any(str(s.get(k) or '').strip() for k in ('code','label')) for s in value(record,'service_slots'))})
    receipt={'version':'native-service-period-v1','wire_boundary':'native_only_not_r129_plan_v2',
             'request':req,'scope':scope,'rows':rows,
             'missing_weekdays':result.metadata['weekly_missing_weekdays'],
             'conflicting_weekdays':result.metadata['weekly_conflicting_weekdays']}
    result.metadata['named_period_receipt']=receipt
    result.metadata['named_period_answer']={lang:render(receipt,lang) for lang in ('th','en')}
    result.metadata['named_period_limits']=list(result.metadata['calendar_source_limits'])
    if any(row['unidentified_periods'] for row in rows):
        result.metadata['named_period_limits'].append('named_period_identity_unconfirmed');result.status='partial'
    return result

def hold(reason,status):
    from .readers import blocked
    result=blocked('C11',reason,status)
    prompts={
        'named_period_requires_one_date':('ต้องการดูรอบบริการของวันที่ใดครับ กรุณาแยกวันที่หรือวันนี้/พรุ่งนี้ที่ขัดกัน','Which date should the play periods apply to? Please separate conflicting date references.'),
        'named_period_date_weekday_conflict':('วันที่กับวันในสัปดาห์ที่ระบุไม่ตรงกัน ต้องการดูวันใดครับ?','The date and requested weekday scope differ. Which day should I use?'),
        'named_period_year_scope_requires_date':('ต้องการดูรอบบริการของวันที่ใดในปีที่ระบุครับ?','Which date in the stated year should the play periods apply to?'),
        'named_period_additional_scope_requires_review':('ต้องการทราบเวลาเริ่ม–จบของรอบ หรือให้ตรวจเงื่อนไขและช่วงเวลาอื่นที่ระบุครับ?','Do you want the period start/end times, or an assessment of the additional time or condition?'),
        'named_period_dated_exception_requires_service_scope_review':('ต้องตรวจขอบเขตประกาศเฉพาะวันก่อน จึงยังยืนยันรอบบริการเล่นจากตารางประจำไม่ได้ครับ','The dated exception needs a service-scope check before these play periods can be confirmed.')}
    th,en=prompts.get(reason,('วันที่ที่ระบุไม่ถูกต้อง กรุณาระบุวันที่ให้ชัดเจนครับ','Please provide a valid calendar date.'))
    result.metadata['context_clarification']={'th':th,'en':en}
    return result

def slot_matches(slot,key):
    names=[str(slot.get(k) or '') for k in ('code','label')]
    if key in PERIODS:return any(re.search(PERIODS[key],s,re.I) for s in names)
    return any(key.casefold()==s.casefold() for s in names)

def render(receipt,lang):
    en=lang=='en';lines=[]
    for row in receipt['rows']:
        day=DAY_NAMES[lang][row['weekday']]
        parts=[]
        for code in receipt['request']['periods']:
            label=code if en else {'morning':'รอบเช้า','afternoon':'รอบบ่าย'}.get(code,code)
            slots=[s for s in row['slots'] if slot_matches(s,code)]
            text='; '.join(s['start']+'–'+s['end']+' ('+({'open':'open','maintenance':'maintenance','closed':'closed'}.get(s['state'],s['state']) if en else {'open':'เปิดบริการเล่น','maintenance':'บำรุงรักษา','closed':'ปิดบริการ'}.get(s['state'],s['state']))+')' for s in slots)
            if not slots:text=('recorded closed day' if en else 'วันที่บันทึกว่าปิดบริการ') if row['service_closed'] else ('recorded intervals have unconfirmed period identities' if en else 'มีช่วงเวลาที่บันทึกไว้แต่ยังระบุชื่อรอบไม่ได้') if row['unidentified_periods'] else ('period not recorded' if en else 'ไม่มีข้อมูลรอบนี้ที่บันทึกไว้')
            parts.append(label+': '+text)
        lines.append(day+' — '+'; '.join(parts))
    prefix=('Recorded play-service periods; these do not establish booking windows, building hours or live availability.' if en else 'รอบบริการเล่นตามข้อมูลที่บันทึกไว้ ยังไม่ใช้ยืนยันช่วงเปิดจอง เวลาเข้าอาคาร หรือเครื่องว่างแบบสดครับ')
    if receipt['scope']['local_date']:prefix+=(' Date: ' if en else ' วันที่: ')+receipt['scope']['local_date']
    for key,label in [('missing_weekdays','Missing weekday source: ' if en else 'ไม่มีแหล่งข้อมูลของวัน: '),('conflicting_weekdays','Multiple unresolved weekday sources: ' if en else 'มีแหล่งข้อมูลของวันที่ยังเลือกฉบับไม่ได้: ')]:
        if receipt[key]:lines.append(label+', '.join(DAY_NAMES[lang][day] for day in receipt[key]))
    return prefix+'\n'+'\n'.join(lines)

def verify(index,task,claims,metadata,question,at):
    expected=plan(index,question,at)
    if task.facet!='service_periods' or not expected or not expected.ids:return False
    if set(expected.ids)!={c.get('fact_id') for c in claims}:return False
    keys=('named_period_receipt','named_period_answer','named_period_limits','calendar_source_limits','calendar_source_periods',
          'calendar_scope_clock','calendar_collection_basis','calendar_semantics','operator','complete_set',
          'weekday_count','requested_weekdays','weekly_missing_weekdays','weekly_conflicting_weekdays')
    return all(metadata.get(k)==expected.metadata.get(k) for k in keys)
