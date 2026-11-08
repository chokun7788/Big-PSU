"""Resolve dates with the existing Bangkok calendar before model inference.

Delivered pending state carries only the user's day/query, never answer facts.
"""
import re
from datetime import date
from .scope import norm

def service_date_question(q):
    return bool(re.search(r'เปิด|ปิด|ว่าง|เข้าไปเล่น.*ช่วงไหน|\b(?:open|closed|available|free)\b',q,re.I)) and not re.search(r'เปิดเกม|ปิดเกม|launch|ราคา|กี่บาท|ขั้นตอน|วิธีจอง|\b(?:price|cost|how much|install)\b',q,re.I)

def _year(s,base):
    n=int(s) if s else base
    return n-543 if n>=2400 else 2000+n if n<100 else n

def _month_reply(q,base):
    from app.calendar.service_calendar import THAI_MONTHS,resolve_month_from_text
    clean=re.sub(r'^(?:หมายถึง|เอา|เดือน|in\s+)|(?:ครับ|ค่ะ|คะ|นะ|please|[?!.,])+$','',norm(q),flags=re.I).strip()
    if re.fullmatch(r'\d{1,2}(?:[/\s]+\d{2,4})?',clean):
        parts=re.split(r'[/\s]+',clean);month=int(parts[0])
        return (_year(parts[1] if len(parts)>1 else None,base.year),month) if 1<=month<=12 else None
    month_pattern='|'.join(re.escape(x) for x in sorted(THAI_MONTHS,key=len,reverse=True))
    from .temporal import MONTHS
    english=re.fullmatch(r'('+'|'.join(MONTHS)+r')\.?(?:\s+(20\d{2}))?',clean,re.I)
    if english:return (int(english[2]) if english[2] else base.year,MONTHS[english[1].lower()])
    if not re.fullmatch(r'(?:เดือน)?(?:นี้|หน้า|ที่แล้ว)|(?:'+month_pattern+r')(?:\s*(?:พ\.?ศ\.?\s*)?\d{2,4})?',clean):return None
    helper=re.sub(r'\s*พ\.?ศ\.?\s*(?=\d{4})',' ',clean)
    resolved=resolve_month_from_text('เดือน'+helper if helper in {'นี้','หน้า','ที่แล้ว'} else helper,today=base)
    return (resolved.year,resolved.month) if resolved else None

def resolve(question,at,history=None):
    from app.calendar.service_calendar import resolve_date_from_text,THAI_MONTHS
    q=norm(question);base=at.date();source=question;pending=None
    if history:
        from ..followup_scope import delivered_state
        state=delivered_state(history) or {};pending=state.get('date_pending')
        if isinstance(pending,dict) and pending.get('version')==1:
            month=_month_reply(q,base)
            if month:
                try:target=date(*month,int(pending['day']))
                except (ValueError,TypeError,KeyError):return {'status':'clarification','reason':'invalid_day_for_month','prompt':{'th':'วันที่นี้ไม่มีในเดือนที่ระบุครับ ต้องการวันที่เท่าไร?','en':'That day does not exist in the specified month. Which date do you mean?'},'pending':pending}
                source=pending['query'];q=norm(source)
                return _resolved(source,target,'delivered_month_reply',base)
            if re.fullmatch(r'(?:เดือน\s*)?\d{1,2}(?:ครับ|ค่ะ)?',q):
                return {'status':'clarification','reason':'invalid_month_reply','pending':pending,'prompt':{'th':'กรุณาระบุเดือนตั้งแต่ 1 ถึง 12 ครับ','en':'Please specify a month from 1 to 12.'}}
    if not service_date_question(q):return None
    from .temporal import parse as parse_extra
    target,basis=parse_extra(q,base)
    if target is not None:return _resolved(question,target,basis,base)
    if basis=='invalid':return {'status':'clarification','reason':'invalid_explicit_date','prompt':{'th':'วันที่ระบุไม่ถูกต้องครับ กรุณาระบุวัน เดือน และปีอีกครั้ง','en':'That date is invalid. Please specify the day, month and year again.'}}
    # Existing date helper supports Thai month aliases, ISO, slash dates,
    # relative days and Buddhist years. A year prefix is spelling, not a fact.
    helper_q=re.sub(r'\s*(?:พ\.?ศ\.?|ค\.?ศ\.?)\s*(?=\d{4})',' ',q)
    # A clock range contains "00-16", which the retained date parser may
    # mistake for a numeric date before reading the explicit Thai month.
    helper_q=re.sub(r'(?<![\d:])\d{1,2}:\d{2}\s*(?:-|–|to|until|ถึง)\s*\d{1,2}:\d{2}(?![\d:])',' ',helper_q,flags=re.I)
    resolved=resolve_date_from_text(helper_q,today=base)
    if resolved:return _resolved(question,resolved.target_date,'existing_calendar_'+resolved.reason,base)
    # Explicit invalid dates must not degrade into a weekday/default-today read.
    months='|'.join(re.escape(x) for x in THAI_MONTHS)
    if re.search(r'\d{4}-\d{1,2}-\d{1,2}|\d{1,2}[/]\d{1,2}|\d{1,2}\s*(?:'+months+')',q):
        return {'status':'clarification','reason':'invalid_explicit_date','prompt':{'th':'วันที่ระบุไม่ถูกต้องครับ กรุณาระบุวัน เดือน และปีอีกครั้ง','en':'That date is invalid. Please specify the day, month and year again.'}}
    bare=re.search(r'(?:วันที่\s*|\bon\s+(?:the\s+)?)(\d{1,2})(?:st|nd|rd|th)?(?!\d)',q)
    if not bare:bare=re.search(r'^\s*(\d{1,2})(?!\d)\s*(?:ศูนย์|เปิด|ปิด|ว่าง|studio|cent(?:er|re))',q)
    if not bare:return None
    day=int(bare[1]);state={'version':1,'day':day,'query':question,'reference_date':base.isoformat(),'facts_in_state':False}
    if not 1<=day<=31:return {'status':'clarification','reason':'invalid_day','prompt':{'th':'กรุณาระบุวันที่ตั้งแต่ 1 ถึง 31 ครับ','en':'Please specify a day from 1 to 31.'}}
    if day<base.day:
        return {'status':'clarification','reason':'past_day_requires_month','pending':state,'prompt':{'th':f'วันที่ {day} ของเดือนไหนครับ?','en':f'Which month do you mean for day {day}?'}}
    try:target=date(base.year,base.month,day)
    except ValueError:return {'status':'clarification','reason':'day_not_in_current_month','pending':state,'prompt':{'th':f'เดือนนี้ไม่มีวันที่ {day} ครับ หมายถึงเดือนไหน?','en':f'This month has no day {day}. Which month do you mean?'}}
    return _resolved(question,target,'current_month_non_past_day',base)

def _resolved(source,target,basis,base):
    # The ISO target is appended to the user's original scope; no game,
    # resource, requested time, negation or other constraint is discarded.
    return {'status':'resolved','query':source+' '+target.isoformat(),'target_date':target.isoformat(),'basis':basis,'reference_date':base.isoformat(),'source_query':source}
