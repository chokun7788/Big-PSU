"""Bounded booking/payment action scope, independent of planner/delivered metadata."""
import re
from .vocabulary import POLICY_INTENTS

def topic_clarification(question):
    """A food/drink + area fragment does not supply a carry/consume predicate."""
    if not re.search(r'อาหาร|เครื่องดื่ม|ขวดน้ำ|\b(?:food|drinks?|beverages?)\b',question,re.I):return None
    if not re.search(r'พื้นที่|บริเวณ|\b(?:areas?|spaces?|zones?)\b',question,re.I):return None
    if re.search(r'กิน|(?<!เครื่อง)ดื่ม|รับประทาน|(?:นำ|เอา|ถือ).{0,30}(?:เข้า|มา)|กฎ|นโยบาย|อนุญาต|ห้าม|ได้ไหม|ได้หรือไม่|ที่ไหน|ตรงไหน|พื้นที่ไหน|พื้นที่ใด|\b(?:consume|eat|bring|carry|where|can|may|allowed|rules?|policy|facilities)\b',question,re.I):return None
    return {'th':'ต้องการทราบเรื่องนำอาหารหรือเครื่องดื่มเข้า พื้นที่รับประทาน หรือสิ่งอำนวยความสะดวกด้านใดครับ?',
            'en':'Do you mean bringing food or drinks inside, designated consumption areas, or a particular facility?'}

def requested_actions(question,category):
    names={intent for intent,cat,_,pattern in POLICY_INTENTS if cat==category and re.search(pattern,question,re.I)}
    rejected=bool(re.search(r'(?:ไม่ต้องการ|ไม่อยาก|ไม่ได้ถาม|ไม่ถาม).{0,15}ยกเลิก|(?:not asking|do not want|don.t want).{0,20}cancel',question,re.I))
    customer=bool(re.search(r'\b(?:can|may|how|when|do)\s+(?:i|we)\b.{0,20}\bcancel|(?:ผม|ฉัน|เรา|ผู้ใช้).{0,20}ยกเลิก',question,re.I))
    if rejected:names-={'customer_cancel','studio_cancel'}
    if customer:names.discard('studio_cancel')
    if 'studio_cancel' in names:names.discard('customer_cancel')
    if len(names)>1:names.discard('booking_steps')
    if 'checkin_documents' in names:names={'checkin_documents'}
    if 'rain_reschedule' in names:names-={'late_notice','change_paid_booking'}
    if 'correct_booking_name' in names:names.discard('change_paid_booking')
    if 'change_time' in names:names.discard('change_paid_booking')
    if category=='C09' and len(names)>1:names.discard('refund')
    if category=='C10':
        from app.pipeline.protected_intents import _food_facet,_asks_personal_power
        if _food_facet(question)=='food_bring_permission':names.add('food_bring');names.discard('food_consumption')
        if _asks_personal_power(question):names.add('personal_power');names.discard('personal_accessories')
        if 'game_failure_switch' in names:names.discard('change_service')
    return names

def source_actions(fact,category):
    declared=fact.get('policy_intent','')
    actions={intent for intent,cat,pattern,_ in POLICY_INTENTS if cat==category and (declared==intent or declared.endswith('.'+intent) or any(re.search(pattern,s,re.I) for s in [*fact['subject'].values(),' '.join(fact['subject'].values())]))}
    if fact.get('service_policy_claim') in {'food_bring','personal_power'}:actions.add(fact['service_policy_claim'])
    return actions

def contradicts_customer_actor(steps):
    # Explicit staff-as-canceller is incompatible with a general customer procedure.
    # This is a bounded contradiction check, not semantic entailment proof.
    for step in steps if isinstance(steps,list) else []:
        instruction=step.get('instruction',{}) if isinstance(step,dict) else {}
        for text in instruction.values() if isinstance(instruction,dict) else []:
            if isinstance(text,str) and re.search(r'(?:staff|employees?|the studio|administrators?)\s+(?:will\s+|can\s+|may\s+)?cancels?\b|(?:เจ้าหน้าที่|พนักงาน|ทางศูนย์)\s*(?:จะ|สามารถ)?\s*ยกเลิก',text,re.I):return True
    return False

def check(index,task,fact,question):
    wanted=requested_actions(question,task.category);actual=source_actions(fact,task.category)
    record=index.records[fact['record_id']]
    if task.category=='C08' and record.get('kind')=='procedure':
        fields=record.get('fields',{}); topic=fields.get('topic',{});pre=fields.get('preconditions',{});steps=fields.get('steps',{})
        if topic.get('status')=='known' and topic.get('value') in {'cancel_booking','cancel_reservation','booking_cancellation'} and pre.get('status') in {'known','not_applicable'} and not pre.get('value') and steps.get('status')=='known' and steps.get('value') and not contradicts_customer_actor(steps.get('value')):actual.add('customer_cancel')
    keys=['topic','name'] if record['kind']=='procedure' else ['topic','subject'] if record['kind']=='policy' else ['question','intent_key','topic','scope_note','legacy_search']
    refs=[ref for key in keys for ref in record.get('fields',{}).get(key,{}).get('evidence_refs',[])]
    return {'requested_actions':sorted(wanted),'source_actions':sorted(actual),'verified':not wanted or bool(wanted&actual),'source_scope_refs':refs,'basis':'actual_question_action_and_source_declared_scope_recomputed','semantic_entailment_verified':False}

def local_booking_reference(question):
    # A local wrong-date/time/name booking situation supplies a booking referent,
    # without inventing an unnamed game/machine/service target for "it".
    return bool(re.search(r'wrong date|booking time|name.{0,20}(?:booking|reservation)|จองผิดวัน|เปลี่ยนเวลาจอง|ชื่อ.*(?:รายการจอง|จอง)',question,re.I)) and bool(requested_actions(question,'C08')) and not re.search(r'same (?:service|game)|that (?:machine|game)|เครื่องนั้น|เกมนั้น|บริการเดิม',question,re.I)

def requested_reference(index,question,at):
    """Resolve a bounded scalar policy date/time without choosing one of many."""
    from .scope import reference_time,requested_years
    from .temporal import parse,MONTHS
    from .named_spans import masked
    from .dialogue_task import normalize_numbers
    from app.calendar.service_calendar import resolve_date_from_text,THAI_MONTHS
    from datetime import date,timedelta
    at=reference_time(at);text=normalize_numbers(masked(index,question));day=None;error=None
    english='|'.join(re.escape(s) for s in sorted(MONTHS,key=len,reverse=True));thai='|'.join(re.escape(s) for s in sorted(THAI_MONTHS,key=len,reverse=True))
    patterns=[r'(?<!\d)\d{4}-\d{1,2}-\d{1,2}(?!\d)',r'\b(?:'+english+r')\.?\s+\d{1,2}(?:st|nd|rd|th)?(?:,?\s+(?:20|21|25|26)\d{2})?\b',r'\b\d{1,2}(?:st|nd|rd|th)?\s+(?:'+english+r')\.?(?:\s+(?:20|21|25|26)\d{2})?\b',r'(?:วันที่\s*)?\d{1,2}\s*(?:'+thai+r')(?:\s*\d{2,4})?',r'\b\d{1,2}[/-]\d{1,2}(?:[/-]\d{2,4})?\b',r'วันนี้|พรุ่งนี้|มะรืน(?:นี้)?|เมื่อวาน(?:นี้)?|\b(?:day after tomorrow|today|tomorrow|yesterday)\b',r'\b(?:next|this)\s+(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b']
    spans=[];days=set()
    offsets={'today':0,'วันนี้':0,'tomorrow':1,'พรุ่งนี้':1,'yesterday':-1,'เมื่อวาน':-1,'เมื่อวานนี้':-1,'มะรืน':2,'มะรืนนี้':2,'day after tomorrow':2}
    for pattern in patterns:
        for match in re.finditer(pattern,text,re.I):
            if any(a<=match.start() and match.end()<=b for a,b in spans):continue
            spans.append(match.span());literal=match[0];resolved=None
            if literal.casefold() in offsets:resolved=at.date()+timedelta(days=offsets[literal.casefold()])
            elif re.fullmatch(patterns[0],literal):
                try:
                    year,month,number=map(int,literal.split('-'));resolved=date(year-543 if year>=2400 else year,month,number)
                except ValueError:pass
            else:
                resolved,_=parse(literal,at.date())
                if resolved is None:
                    candidate=resolve_date_from_text(literal,today=at.date());resolved=candidate.target_date if candidate else None
            if resolved is None:error='invalid_policy_reference_date'
            else:days.add(resolved)
    if len(days)>1:error='multiple_policy_dates_require_separate_roles'
    elif days:day=next(iter(days))
    if not spans:
        day,basis=parse(text,at.date())
        if basis=='invalid':error='invalid_policy_reference_date'
        if day is None and error is None:
            resolved=resolve_date_from_text(text,today=at.date())
            if resolved:day=resolved.target_date
        if day is None and error is None and requested_years(text):error='policy_year_requires_specific_date'
    ref=at.replace(year=day.year,month=day.month,day=day.day) if day else at
    times=set(re.findall(r'(?<!\d)\d{1,2}:\d{2}(?!\d)',text))
    if len(times)>1:error='multiple_policy_times_require_separate_roles'
    elif times:
        try:
            hour,minute=map(int,next(iter(times)).split(':'));ref=ref.replace(hour=hour,minute=minute,second=0,microsecond=0)
        except ValueError:error='invalid_policy_reference_time'
    return ref,error

def applicability(index,fact,question,at):
    from .scope import validity_allows
    ref,error=requested_reference(index,question,at)
    allowed=validity_allows(fact,ref);record=index.records[fact['record_id']]
    return {'fact_id':fact['id'],'record_id':record['record_id'],'record_revision':record['revision'],'requested_reference_time':ref.isoformat(),'recorded_validity':record['validity'],'allowed':allowed is not False and error is None,'state':'input_scope_unresolved' if error else 'outside_recorded_interval' if allowed is False else 'validity_interval_unconfirmed' if allowed is None else 'within_recorded_interval','error':error}

def procedure_limits(record):
    return [key for key in ['preconditions','required_documents','deadline_minutes','outcome'] if record.get('fields',{}).get(key,{}).get('status') not in {'known','not_applicable'}] if record.get('kind')=='procedure' else []
