"""Concise day-level opening status from calendar fields, never live occupancy."""
import calendar,re
from datetime import datetime,time
from zoneinfo import ZoneInfo
from .registry import value
from .query_contract import normalize

def status_question(question):
    q=normalize(question)
    intent=bool(re.search(r'(?:เปิด|ปิด|หยุด).{0,12}(?:ไหม|มั้ย|หรือเปล่า|หรือไม่|รึเปล่า)',q) or (re.search(r'\b(?:open|closed)\b',q) and (re.match(r'^(?:is|are|will)\b',q) or q.endswith('?'))))
    if not intent:return False
    # Remove only understood date/framing language. Times, extra needs and
    # unknown conditions must retain their normal, more detailed handling.
    rest=re.sub(r'(?<!\d)\d{4}-\d{1,2}-\d{1,2}(?!\d)|(?<!\d)\d{1,2}/\d{1,2}(?:/\d{2,4})?(?!\d)',' ',q)
    rest=re.sub(r'วันนี้|พรุ่งนี้|มะรืนนี้|วันที่|วัน(?:จันทร์|อังคาร|พุธ|พฤหัสบดี|ศุกร์|เสาร์|อาทิตย์)',' ',rest)
    rest=re.sub(r'เปิดให้บริการ|ปิดให้บริการ|เปิดบริการ|ปิดบริการ|ให้บริการ|เปิด|ปิด|หยุด|ไหม|มั้ย|หรือเปล่า|หรือไม่|รึเปล่า|ศูนย์อีสปอร์ต|ศูนย์|สตูดิโอ|ร้าน|ที่นี่|ครับ|ค่ะ|คะ|หน่อย',' ',rest)
    rest=re.sub(r'\b(?:is|are|will|be|you|it|the|studio|cent(?:er|re)|venue|open|closed|today|tomorrow|on|please|monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b',' ',rest)
    return not re.sub(r'[\s?!.,]+','',rest)

def classify(record):
    f=record['fields'];opens=f.get('open_periods',{});book=f.get('bookable_periods',{});state=value(record,'state')
    has_slots=book.get('status')=='known' and bool(book.get('value'))
    if state=='closed':
        if has_slots or opens.get('status')=='known' and opens.get('value'):return None,[],'contradictory_calendar_fields'
        return 'closed',['state'],'explicit_closed_state'
    if opens.get('status')=='known' and isinstance(opens.get('value'),list):
        if not opens['value'] and has_slots:return None,[],'contradictory_calendar_fields'
        return ('open' if opens['value'] else 'closed'),['open_periods'],'known_open_periods'
    if has_slots:
        # At least one confirmed service period proves service is offered that
        # day. It does not establish exact area hours or "open right now".
        return 'open',['bookable_periods'],'has_confirmed_service_period'
    return None,[],'no_confirmed_day_status'

def answer(reader,snap,started,question,lang,at,records):
    if not status_question(question):return None
    from .query_scope import calendar_ids
    _,day=calendar_ids(question,records,at)
    if day is None:return None
    from .answer import effective,title,text
    from app.calendar.service_calendar import thai_month_name
    zone=ZoneInfo('Asia/Bangkok');date_at=datetime.combine(day,time.min,tzinfo=zone)
    # Known zone-specific exceptions cannot close the entire center.
    def branch_scope(r):return not (r['fields'].get('zone_ids',{}).get('status')=='known' and value(r,'zone_ids'))
    selected=[r for r in records.values() if r['kind']=='closure' and value(r,'local_date')==day.isoformat() and branch_scope(r)]
    scope='special_date'
    if not selected:
        selected=[r for r in records.values() if r['kind']=='schedule' and value(r,'weekday')==day.weekday() and branch_scope(r)];scope='weekly'
    observations=[];outcomes=[];hits=[];obligations=[]
    for r in selected:
        result,keys,reason=classify(r) if effective(r,date_at,records) else (None,[],'record_not_effective_at_target_date')
        if any(not r['fields'][key].get('evidence_refs') for key in keys):result=None;keys=[];reason='missing_evidence'
        outcomes.append(result);observations.append({'record_id':r['record_id'],'status':result,'basis':reason,'zone_scope_status':r['fields'].get('zone_ids',{}).get('status','unknown')})
        if result is None:continue
        for key in keys:
            field=r['fields'][key];obligations.append({'record_id':r['record_id'],'field':key,'status':'known','evidence_refs':field['evidence_refs']})
            for ref in field['evidence_refs']:
                src=snap['release']['sources'].get(ref['source_id'])
                if src is None:return None
                marker='S'+str(len(hits)+1)
                hits.append({'id':r['record_id']+':'+key+':'+marker,'record_id':r['record_id'],'field':key,'title':title(r,lang),'text':text(field['value'],lang),'source_id':ref['source_id'],'snapshot_sha256':src['sha256'],'locator':ref['locator'],'citation_label':marker,'source_url':src.get('public_url') or ''})
    status=outcomes[0] if outcomes and None not in outcomes and len(set(outcomes))==1 else None
    today=day==at.astimezone(zone).date() and bool(re.search(r'วันนี้|\btoday\b',normalize(question)))
    if lang=='th':
        prefix=('วันนี้วันที่ ' if today else 'วันที่ ')+str(day.day)+' '+thai_month_name(day.month)+' '+str(day.year+543)
        body=prefix+(' เปิดให้บริการครับ' if status=='open' else ' ไม่เปิดให้บริการครับ' if status=='closed' else ' ยังยืนยันสถานะเปิด–ปิดไม่ได้ครับ')
    else:
        prefix=('Today, ' if today else 'On ')+f'{day.day} {calendar.month_name[day.month]} {day.year}'
        body=prefix+(', the studio is open.' if status=='open' else ', the studio is closed.' if status=='closed' else ', the opening status is not confirmed.')
    if status is None:hits=[];obligations=[]
    plan={'record_ids':[r['record_id'] for r in selected],'requested_fields':list(dict.fromkeys(o['field'] for o in obligations)),
          'operation':'calendar','method':'common_calendar_open_status','day_status':status or 'unconfirmed','target_date':day.isoformat(),
          'calendar_scope':scope,'calendar_status_sources':observations,'day_level_only':True,'live_availability_asserted':False,
          'source_answer_confirmed':status is not None,'response_projection':[{'record_id':r['record_id'],'fields':{o['field']:'day_status_basis' for o in obligations if o['record_id']==r['record_id']}} for r in selected]}
    return reader.finish(snap,started,body,hits,plan,obligations,response='answer' if status else 'unconfirmed')
