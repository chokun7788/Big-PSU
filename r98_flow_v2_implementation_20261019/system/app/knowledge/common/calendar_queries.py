"""Closing-time interpretation using typed calendar evidence, not word leftovers."""
import re,time
from datetime import datetime,time as daytime
from zoneinfo import ZoneInfo
from dataclasses import replace
from .query_contract import normalize
from .registry import value

def answer(reader,question,snap,records,lang,at):
    from .query_scope import calendar_ids
    q=normalize(question).strip(' ?!.,')
    days=['จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์','อาทิตย์']
    en=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    rest=re.sub(r'วันนี้|พรุ่งนี้|วัน(?:จันทร์|อังคาร|พุธ|พฤหัสบดี|ศุกร์|เสาร์|อาทิตย์)|\b(?:today|tomorrow|on|'+ '|'.join(en)+r')\b',' ',q)
    rest=re.sub(r'ครับ|ค่ะ|คะ|หน่อย','',rest).strip()
    closing=bool(re.fullmatch(r'(?:ตอนเย็น)?\s*(?:เปิดถึงกี่โมง|ปิดกี่โมง)(?:ตอนเย็น)?|what time (?:do you|does the studio) close|how late (?:are you|is the studio) open',rest))
    # Asking which days/time periods are bookable is a timetable task, not
    # the steps for making a booking. Never use a regular FAQ for a live date.
    regular=bool(re.search(r'\b(?:days?|monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b|วันและเวลา|วันไหน|วันใด',q) and re.search(r'\b(?:book|booking|slots?|service)\b|จอง|ให้บริการ',q) and re.search(r'\b(?:morning|afternoon|slots?|times?)\b|วันและเวลา|ช่วงเช้า|ช่วงบ่าย|เวลา',q))
    regular=regular and not bool(re.search(r'วันนี้|พรุ่งนี้|มะรืน|\b(?:today|tomorrow|now|available|free|cancel|change|pay|refund)\b|\d{4}[-/]\d|\d{1,2}[/.-]\d{1,2}|ยกเลิก|เปลี่ยน|จ่าย|ว่าง',q))
    if not closing and not regular:return None
    ids,target=calendar_ids(question,records,at)
    if target is None or regular:ids=[k for k,r in records.items() if r['kind']=='schedule' and r['fields']['zone_ids']['status']=='known' and value(r,'zone_ids')==[]]
    if not ids and (target is None or regular):
        # Some migrations retain the weekly timetable only in a sourced FAQ.
        # A complete closing-time frame can read that FAQ without treating
        # the temporal word "evening" as an unhandled new business condition.
        from .answer import named
        from .query_scope import derived_names
        ns=derived_names(snap['release']['names'],records)
        candidates,_=named(question,{k:ns.get(k,[]) for k,r in records.items() if r['kind']=='faq'},allow_fuzzy=False)
        selected=[k for k in candidates if re.search(r'เวลาเปิด|เวลาให้บริการ|เปิด.?ปิด|บริการถึง|เปิดถึง|ปิดกี่|opening hours|service hours|schedule|closing',str(value(records[k],'question') or {}),re.I)]
        if regular:
            selected=[k for k,r in records.items() if r['kind']=='faq' and (value(r,'intent_key')=='service_schedule' or re.search(r'ตารางเวลาให้บริการ|weekly service (?:hours|schedule)|regular service timetable',str(value(r,'question') or {}),re.I))]
        if len(selected)==1:
            plan={'record_ids':selected,'scope_ids':selected,'requested_fields':['answer'],'operation':'calendar','all_fields':False,'platform':None,'method':'r98_sourced_timetable_faq','unresolved_clauses':[],'task_binding':{'frame':'weekly_bookable_timetable' if regular else 'closing_time','temporal_scope':'regular_timetable_not_live','source_authority_inferred':False}}
            return reader.execute_task(question,snap=snap,at=at,lang=lang,plan=plan)
    if not ids:return None
    # A broad question cannot silently adopt a zone-specific closing time.
    ids=[k for k in ids if records[k]['fields']['zone_ids']['status']=='known' and value(records[k],'zone_ids')==[]]
    if not ids:return None
    at_read=datetime.combine(target,daytime.min,tzinfo=ZoneInfo('Asia/Bangkok')) if target else at
    plan={'record_ids':ids,'scope_ids':ids,'requested_fields':['open_periods','bookable_periods'],'operation':'calendar','all_fields':False,'method':'r98_closing_time_read','platform':None,'unresolved_clauses':[],'target_date':target.isoformat() if target else None}
    r=reader.execute_task(question,snap=snap,at=at_read,lang=lang,plan=plan)
    if regular:return r
    from .answer import effective
    lines=[]
    for rid in ids:
        record=records[rid];wd=value(record,'weekday');caption=target.isoformat() if target else (('วัน'+days[wd]) if lang=='th' else en[wd].title()) if isinstance(wd,int) and 0<=wd<7 else rid
        open_f=record['fields']['open_periods'];book_f=record['fields']['bookable_periods']
        if not effective(record,at_read,records):label='ข้อมูลไม่อยู่ในช่วงมีผล' if lang=='th' else 'source is not effective'
        elif value(record,'state')=='closed':label='ปิดตามประกาศ' if lang=='th' else 'closed by explicit notice'
        elif open_f['status']=='known' and open_f['evidence_refs']:
            label=(('เปิดถึง ' if lang=='th' else 'Open until ')+max(p['end'] for p in open_f['value'])) if open_f['value'] else ('ไม่มีช่วงเปิดในตารางที่ยืนยัน' if lang=='th' else 'No opening period is recorded (confirmed)')
        elif book_f['status']=='known' and book_f['evidence_refs'] and book_f['value']:
            label=('ช่วงจองสิ้นสุด ' if lang=='th' else 'Bookable periods end at ')+max(p['end'] for p in book_f['value'])+(' (ยังไม่ยืนยันเวลาปิดเข้าศูนย์)' if lang=='th' else ' (physical closing time is not confirmed)')
        else:label='ยังไม่ยืนยันเวลาปิด' if lang=='th' else 'Closing time is not confirmed'
        labels=[h['citation_label'] for h in r.hits if h.get('record_id')==rid]
        lines.append('• '+caption+': '+label+' '+''.join('['+x+']' for x in labels))
    if r.decision_artifact.get('response_type')=='retry':return r
    return replace(r,answer=('ตารางเวลาที่บันทึกไว้\n' if lang=='th' else 'Recorded service schedule\n')+'\n'.join(lines))
