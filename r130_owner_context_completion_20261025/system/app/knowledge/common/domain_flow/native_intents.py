"""Canonical linguistic operations proved by current source readers, not stored answers."""
import re
from .scope import norm
from .understanding import Understanding,MeaningTask

def propose(index,question,_split=True):
    from .readers import policy
    q=norm(question);tasks=[]
    if _split:
        parts=[s.strip(' ,') for s in re.split(r'\s+(?:and|ans|adn)\s+(?=(?:what|how|which|can|is|when)\b)',question,flags=re.I)]
        if 1<len(parts)<=4:
            from .meaning_review import review
            children=[]
            for part in parts:
                native=propose(index,part,False)
                child=native if native is not None else review(part,index,Understanding(reason='native_compound_part',event={'model_called':False}))
                if not child.accepted:break
                children.extend(child.tasks)
            else:return Understanding(children,True,'canonical_compound_operations',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    # Do not collapse unresolved independent needs into one native shortcut.
    if re.search(r'ปุ่ม|buttons?|controls?',q,re.I) and re.search(r'ราคา|price|cost',q,re.I):return None
    if re.search(r'และ.*(?:ราคา|เปิด)|\band\b.*(?:price|open)|ทั้ง.*และ',q,re.I):return None
    if re.search(r'มีอะไร.*(?:เลือกเล่น|ให้เล่น)',q,re.I):
        return Understanding([MeaningTask(question,'games','C04','list','game_catalog')],True,'canonical_game_catalog',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'20\d\d-\d\d-\d\d',q) and re.search(r'เปิด|ปิด|เล่น.*ช่วง|\bopen\b|\bclosed\b',q,re.I) and not re.search(r'ว่าง|available|ราคา|price|วิธีจอง|how.*book',q,re.I):
        return Understanding([MeaningTask(question,'schedule','C11','detail','open_periods')],True,'canonical_dated_service',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'what days.*open|which days.*open|เวลาเปิด.*วัน|ตาราง.*(?:เปิด|บริการ)',q,re.I):
        return Understanding([MeaningTask(question,'schedule','C11','list','open_periods')],True,'canonical_regular_calendar',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'maintenance|บำรุงรักษา',q,re.I) and not re.search(r'ราคา|cost|repair|ค่าซ่อม',q,re.I):
        return Understanding([MeaningTask(question,'schedule','C11','detail','maintenance_periods')],True,'canonical_maintenance_periods',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'แข่ง|กติกา|tourn[a-z]*|competition|rulebook|\bruls?\b',q,re.I):
        from .readers import rules_reader
        from .scope import reference_time
        source=rules_reader(index,q,reference_time())
        if source.ids:
            return Understanding([MeaningTask(question,'competition_rules','C13','rule_lookup','rule_clause',canonical_operation='competition.source_clause')],True,'canonical_source_rule_clause',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    unknown=re.fullmatch(r'do you have\s+(.+?)[?!.]*',q,re.I)
    if unknown and not any(index.bind(cat,q) for cat in index.bycat):
        target=unknown[1].rstrip('?!.')
        return Understanding([MeaningTask(question,'equipment','C03','detail','name',target=target)],True,'canonical_unknown_inventory_target',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'แข่ง|กติกา|tournament|competition|rulebook',q,re.I) and re.search(r'ลงโทษ|penalt|punishment|sanction',q,re.I):
        return Understanding([MeaningTask(question,'competition_rules','C13','rule_lookup','rule_clause')],True,'canonical_rule_family',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'เกม.*(?:พร้อมกัน|เล่นด้วยกัน|เล่นได้|เล่นกับเพื่อน)|games?.*(?:players|people|together)',q,re.I) and re.search(r'\d+\s*(?:คน|players|people)|กี่คน|how many players',q,re.I):
        return Understanding([MeaningTask(question,'games','C04','list' if not index.bind('C04',q) else 'detail','players_max')],True,'canonical_game_mode',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'มีอุปกรณ์อะไร|อุปกรณ์.*บ้าง|มีของอะไร.*(?:เตรียม|ให้ใช้)|มีอะไรให้ใช้|what equipment|which devices',q,re.I):
        return Understanding([MeaningTask(question,'equipment','C03','list','name')],True,'canonical_inventory',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if not any(index.bind(cat,q) for cat in ['C03','C04']) and re.fullmatch(r'(?:แล้ว)?(?:อันนั้น|อันนี้|มัน)(?:ล่ะ)?[?! ]*|(?:what about|how about)\s+(?:it|that|this)(?: one)?[?! .]*',q,re.I):
        return Understanding([MeaningTask(question,'games','C04','detail','summary',ambiguous=True)],True,'unresolved_reference',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if not re.search(r'ราคา|cost|price|fee|ปุ่ม|controls|games?|tournament|แข่งขัน',q,re.I):
        from .dialogue_task import mentions
        people=mentions(index,q,{'person'})
        if people and re.search(r'ตำแหน่ง|หน้าที่|\brole\b|\bposition\b',q,re.I):
            return Understanding([MeaningTask(question,'members','C02','role_lookup','role')],True,'canonical_person_role',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
        devices=mentions(index,q,{'equipment_model'})
        if devices and re.search(r'อยู่ไหน|อยู่ที่ไหน|อยู่โซนไหน|ที่ตั้ง|which zone|where|location|located',q,re.I):
            return Understanding([MeaningTask(question,'equipment','C03','detail','location')],True,'canonical_equipment_location',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'\bwhat (?:id|documents?|identification)\b',q,re.I) and re.search(r'visitor|arrival|check.in|studio',q,re.I):
        return Understanding([MeaningTask(question,'reservation','C08','detail','owner_policy',canonical_operation='policy.checkin_documents')],True,'canonical_checkin_documents',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'ถ่าย(?:รูป|ภาพ|วิดีโอ)|อัดวิดีโอ|record(?:ing)?\s+(?:a\s+)?video|film(?:ing)?|screenshots?|capture',q,re.I) and not re.search(r'แข่ง|tournament|competition|price|ราคา',q,re.I):
        return Understanding([MeaningTask(question,'rules','C10','detail','owner_policy',canonical_operation='policy.capture')],True,'canonical_recording_scope',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    for cat,domain in [('C08','reservation'),('C09','payment'),('C10','rules')]:
        p=policy(index,cat,q)
        if p is not None and (p.ids or p.candidates):
            intents=p.metadata.get('policy_intents',[])
            tasks.append(MeaningTask(question,domain,cat,'detail','owner_policy',canonical_operation='policy.'+intents[0] if len(intents)==1 else ''))
    if len(tasks)==1:
        return Understanding(tasks,True,'canonical_policy_action',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'เข้าไปเล่น.*เริ่ม|เริ่ม.*(?:ใช้บริการ|เข้าเล่น)|how.*(?:start|begin).*(?:play|visit)',q,re.I):
        return Understanding([MeaningTask(question,'reservation','C08','detail','owner_policy',canonical_operation='policy.booking_steps')],True,'canonical_booking_procedure',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'เหมา|rental|half.day|full.day',q,re.I):
        from .financial import rental_pool
        if rental_pool(index,q):return Understanding([MeaningTask(question,'rental','C07','price_calculate','amount_thb')],True,'canonical_rental_package',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'ราคา|กี่บาท|เตรียมเงิน|price|cost|how much',q,re.I) and not re.search(r'เหมา|rental|damage|ซ่อม|refund|คืนเงิน',q,re.I):
        from .financial import rate_pool
        if rate_pool(index,q):return Understanding([MeaningTask(question,'service_fee','C06','compare' if re.search(r'เทียบ|compare|versus',q,re.I) else 'price_calculate','amount')],True,'canonical_financial_operation',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if index.bind('C05',q) and re.search(r'ตีแรง|โจมตีหนัก|heavy attack|กดตรงไหน|กดอะไร',q,re.I):
        return Understanding([MeaningTask(question,'game_controls','C05','control','input_bindings')],True,'canonical_control_action',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'ปุ่ม|\bbuttons?\b|\bcontrols?\b',q,re.I) and not index.bind('C05',q) and not re.search(r'แข่ง|tournament|competition',q,re.I):
        return Understanding([MeaningTask(question,'game_controls','C05','control','input_bindings',ambiguous=True)],True,'canonical_missing_control_game',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    return None
