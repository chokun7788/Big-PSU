"""Canonical linguistic operations proved by current source readers, not stored answers."""
import re
from .scope import norm
from .understanding import Understanding,MeaningTask

def guest_membership_and_id(question):
    return bool(re.search(r'\bmembership\b|(?:ต้อง|สมัคร|เป็น).{0,15}สมาชิก',question,re.I) and re.search(r'\bnational (?:id|identification)\b|บัตรประชาชน',question,re.I) and re.search(r'\b(?:need|require|must)\b|ต้อง|จำเป็น',question,re.I))

def propose(index,question,_split=True):
    from .readers import policy
    q=norm(question);tasks=[]
    from .rule_semantics import explicit_competition
    outside_rule_need=bool(re.search(r'(?:\band\b|และ|แล้ว).{0,60}(?:ราคา|กี่บาท|how much|\b(?:price|cost|fee|payment|booking|refund)\b)|(?:ราคา|how much|\b(?:price|cost)\b).{0,80}(?:\band\b|และ|แล้ว)',q,re.I))
    if explicit_competition(q,index) and not outside_rule_need:
        # Keep the WHOLE event-scoped request, including food and shared context.
        # A pending clause cannot authorize falling back to ordinary studio rules.
        return Understanding([MeaningTask(question,'competition_rules','C13','rule_lookup','rule_clause',canonical_operation='competition.source_clause')],True,'canonical_competition_scope',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if _split:
        from .routing import split_needs
        parts=split_needs(question,index)
        if 1<len(parts)<=4:
            from .meaning_review import review
            from .request_verifier import observe
            from .understanding import DOMAINS
            children=[]
            for part in parts:
                native=propose(index,part,False)
                child=native if native is not None else review(part,index,Understanding(reason='native_compound_part',event={'model_called':False}))
                if child.accepted:children.extend(child.tasks);continue
                observed=observe(index,part)
                if len(observed['needs'])==1 and not observed['uncertain']:
                    need=observed['needs'][0];cat=need['category'];facet=need['facet'];domain=next(d for d,(c,_) in DOMAINS.items() if c==cat)
                    operation='control' if cat=='C05' else 'rule_lookup' if cat=='C13' else 'availability' if cat=='C12' else 'price_calculate' if cat in {'C06','C07'} and facet in {'amount','amount_thb'} else 'list' if facet=='game_catalog' else 'detail'
                    children.append(MeaningTask(part,domain,cat,operation,facet,canonical_operation=need['predicate']))
                else:
                    # An unresolved sibling cannot erase already recognised
                    # task boundaries or turn the whole request into one action.
                    children.append(MeaningTask(part,'general',None,'detail','',ambiguous=True))
            if len(children)<=4:return Understanding(children,True,'canonical_compound_operations',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'},'unresolved_compound_parts':[t.quote for t in children if t.ambiguous]})
            return Understanding(reason='native_compound_requires_wider_planner',event={'model_called':False})
    # A source-bound explicit field lookup can use the predeclared hybrid
    # reader without a model round trip. Predicate text alone never binds an item.
    if re.search(r'ประเภทอุปกรณ์|ชนิดอุปกรณ์|\bdevice type\b',q,re.I) and not re.search(r'ไม่ใช่|\bnot\b|ถ้า|\bif\b',q,re.I):
        bound=index.bind('C03',question)
        models={f['record_id'] for f in bound if index.records.get(f['record_id'],{}).get('kind')=='equipment_model'}
        if len(models)==1:
            return Understanding([MeaningTask(question,'equipment','C03','detail','device_type')],True,'canonical_explicit_equipment_type',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'ใช้งาน(?:ยังไง|อย่างไร)|ใช้ยังไง|ใช้ทำอะไร|\bhow (?:do I |can I |to )?use\b',q,re.I) and not re.search(r'ไม่ใช่|\bnot\b|ถ้า|\bif\b',q,re.I):
        equipment={f['record_id'] for f in index.bind('C03',question) if index.records.get(f['record_id'],{}).get('kind')=='equipment_model'}
        if len(equipment)==1:
            return Understanding([MeaningTask(question,'equipment','C03','detail','usage')],True,'canonical_explicit_equipment_usage',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    from .package_intent import request as package_request
    package=package_request(index,question)
    if package:
        return Understanding([MeaningTask(question,'rental','C07','price_calculate' if facet=='amount_thb' else 'detail',facet,target=package['target'],canonical_operation='rental.named_package_field') for facet in package['facets']],True,'canonical_named_package_fields',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation','predicate_scope':'current_source_package_name_and_local_predicate'}})
    from .control_intent import request as control_request
    control=control_request(index,question)
    if control:
        return Understanding([MeaningTask(question,'game_controls','C05',control['operation'],'input_bindings',canonical_operation='controls.requested_binding')],True,'canonical_named_game_control_predicate',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    from .period_scope import request as period_request
    period=period_request(index,question)
    if period:
        return Understanding([MeaningTask(question,'schedule','C11','list','service_periods',constraints=[{'slot':'time','quote':s['text'],'source_record_id':''} for s in period['spans']],canonical_operation='calendar.named_play_period')],True,'native_named_play_period_scope',{'model_called':False,'meaning_review':{'basis':'native_source_period_operation'},'wire_boundary':'native_only_not_r129_plan_v2'})
    # Membership and identification are distinct predicates. A general
    # visitor-access clause cannot answer either of them by itself.
    if guest_membership_and_id(q):
        return Understanding([MeaningTask(question,'rules','C10','detail','owner_policy',canonical_operation='policy.membership_requirement'),MeaningTask(question,'reservation','C08','detail','owner_policy',canonical_operation='policy.checkin_documents')],True,'canonical_membership_and_checkin_documents',{'model_called':False,'meaning_review':{'basis':'distinct_explicit_predicates'}})
    from .payment_intent import request as payment_request
    payment=payment_request(question)
    if payment:
        return Understanding([MeaningTask(question,'payment','C09','detail','owner_policy',canonical_operation='policy.'+payment)],True,'canonical_payment_proof_or_document_predicate',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    from .policy_scope import topic_clarification
    if topic_clarification(question):
        return Understanding([MeaningTask(question,'rules','C10','detail','owner_policy',ambiguous=True)],True,'policy_topic_missing_predicate',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    # Do not collapse unresolved independent needs into one native shortcut.
    if re.search(r'ปุ่ม|buttons?|controls?',q,re.I) and re.search(r'ราคา|price|cost',q,re.I):return None
    if re.search(r'และ.*(?:ราคา|เปิด)|\band\b.*(?:price|open)|ทั้ง.*และ',q,re.I):return None
    from .controller_catalog import request as controller_request
    controller=controller_request(index,question)
    if controller:
        return Understanding([MeaningTask(question,'games','C04',controller['operation'],'zone' if controller['group_by']=='zone' else 'game_catalog',constraints=[{'slot':'requested_scope','quote':controller['source_span']['text'],'source_record_id':''}],canonical_operation='games.input_device')],True,'canonical_controller_catalog_scope',{'model_called':False,'meaning_review':{'basis':'explicit_input_device_catalog_request'}})
    from app.pipeline.protected_intents import _is_public_access,_asks_open_eligibility,_asks_temporal_access,_asks_offsite_equipment
    offsite=bool(_asks_offsite_equipment(q) or re.search(r'(?:notebook|laptop|โน้ตบุ๊ก|โน้ตบุ๊ค).{0,35}(?:กลับบ้าน|นอกศูนย์|off.?site|home)',q,re.I))
    if offsite:
        return Understanding([MeaningTask(question,'rental','C07','detail','terms')],True,'canonical_offsite_scope',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'ข่าว.*ล่าสุด|ข่าวประชาสัมพันธ์|\bnews\b|announcements?|สถานะการรับสมัคร|วันจัดกิจกรรม|registration.*(?:status|open|closed)|has registration closed',q,re.I):
        facet='status' if re.search(r'สถานะ|status|registration.*(?:open|closed)|has registration closed',q,re.I) else 'registration_url' if re.search(r'ลิงก์สมัคร|ช่องทางลงทะเบียน|ช่องทางสมัคร|สมัคร.*ลิงก์|registration (?:url|link)|where can i register',q,re.I) else 'date' if re.search(r'วัน|when|date',q,re.I) else 'body'
        return Understanding([MeaningTask(question,'news','C14','detail',facet)],True,'canonical_news_source_scope',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    # A specific consent/guardian predicate must survive general access wording.
    if re.search(r'ผู้ปกครอง|เซ็นยินยอม|\b(?:guardian|parental|signed consent)\b',q,re.I):
        return Understanding([MeaningTask(question,'rules','C10','detail','owner_policy',canonical_operation='policy.guardian')],True,'canonical_guardian_before_general_access',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    from .vocabulary import POLICY_INTENTS
    specific_policy=any(intent!='external_visitor' and re.search(pattern,q,re.I) for intent,_,_,pattern in POLICY_INTENTS)
    if (_is_public_access(q) or _asks_open_eligibility(q)) and not specific_policy and not _asks_temporal_access(q) and not re.search(r'ราคา|กี่บาท|\b(?:cost|price|fee)\b|ขั้นตอน|how (?:do|to)|เด็ก|อายุ|\b(?:child|children|minor|age)\b',q,re.I):
        return Understanding([MeaningTask(question,'rules','C10','detail','owner_policy',canonical_operation='policy.external_visitor')],True,'canonical_access_before_person_directory',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    from .player_scope import requested_count
    if re.search(r'\bgames?\b|เกม',q,re.I) and requested_count(index,question) is not None and not re.search(r'ตอนนี้|วันนี้|พรุ่งนี้|ราคา|กี่บาท|ปุ่ม|กติกา|\b(?:now|today|tomorrow|cost|price|fee|controls?|buttons?|rules?)\b|20\d\d-\d\d-\d\d|\d{1,2}:\d{2}',q,re.I):
        from .dialogue_task import mentions
        return Understanding([MeaningTask(question,'games','C04','detail' if mentions(index,question,{'game'}) else 'list','players_max')],True,'canonical_game_player_range',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'\b(?:which|what) games?\b|มีเกมอะไร|เกมอะไร.*(?:โซน|เล่น)',q,re.I) and not re.search(r'ตอนนี้|วันนี้|พรุ่งนี้|\b(?:now|today|tomorrow|players?|people|together|genre|controls?|buttons?|mode)\b|กี่คน|\d+\s*คน|20\d\d-\d\d-\d\d|\d{1,2}:\d{2}',q,re.I):
        return Understanding([MeaningTask(question,'games','C04','list','game_catalog')],True,'canonical_static_catalog',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'มีอุปกรณ์อะไร|อุปกรณ์.*(?:ทั้งหมด|บ้าง)|equipment list|list.*equipment|what equipment|which devices',q,re.I) and not re.search(r'อนุญาต|นำ.*มา|ยืม|เช่า|เสีย|หาย|พัง|\b(?:bring|allowed|borrow|rent|permission|rules?|price|cost|broken)\b',q,re.I):
        return Understanding([MeaningTask(question,'equipment','C03','list','name')],True,'canonical_recorded_equipment_inventory',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if index.bind('C03',q) and re.search(r'กี่|จำนวน|how many|listed service capacity|service participant range',q,re.I):
        from .vocabulary import FACETS
        field=next((f for f in ['controllers','room_seats','service_capacity','capacity_persons','quantity'] if re.search(FACETS[f],q,re.I)),None)
        if field:return Understanding([MeaningTask(question,'equipment','C03','count',field)],True,'canonical_equipment_dimension',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    from .precision import game_presence
    presence=game_presence(index,q)
    if presence is not None and (presence.ids or presence.reason=='requested_resource_offering_not_confirmed'):
        return Understanding([MeaningTask(question,'games','C04','availability',presence.facets[0] if presence.facets else 'studio_services')],True,'canonical_game_resource_scope',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    # Act on explicit predicates before treating a mentioned object as inventory.
    from .vocabulary import POLICY_INTENTS
    for intent,cat,_,pattern in POLICY_INTENTS:
        if intent not in {'equipment_compensation','customer_cancel','studio_cancel','booking_steps','logout_data'} or not re.search(pattern,q,re.I):continue
        source=policy(index,cat,q,forced_intent=intent)
        if source is not None:
            domain='reservation' if cat=='C08' else 'rules'
            return Understanding([MeaningTask(question,domain,cat,'detail','owner_policy',canonical_operation='policy.'+intent)],True,'canonical_action_before_entity',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    from .contact_scope import CHANNELS
    channel_query=any(re.search(p,q,re.I) for p in CHANNELS.values())
    if channel_query and re.search(r'ติดต่อ|เบอร์|อีเมล|อีเมล์|\b(?:contact|phone|telephone|e-?mail|facebook|website)\b',q,re.I) and not re.search(r'สลิป|คืนเงิน|จ่าย|สมัคร|\b(?:slip|refund|pay|registration|send|submit|use)\b',q,re.I):
        facet='office_hours' if re.search(r'เวลาติดต่อ|office hours|contact hours',q,re.I) else 'value'
        return Understanding([MeaningTask(question,'contact','C01','detail',facet)],True,'canonical_contact_channel',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    center_named=bool(re.search(r'ศูนย์|สตูดิโอ|\bstudio\b',q,re.I))
    from .calendar_sets import weekly_requested
    if weekly_requested(q) and re.search(r'\breservations?\b|\bbook(?:ing|able)?\b|จอง',q,re.I) and not re.search(r'ว่าง|ราคา|ค่าบริการ|ลงทะเบียน|แข่งขัน|แข่ง|\b(?:vacan\w*|available|price|cost|fee|register|registration|tournament|competition)\b|20\d\d-\d\d-\d\d',q,re.I):
        return Understanding([MeaningTask(question,'schedule','C11','list','bookable_periods',canonical_operation='calendar.weekly_bookable_periods')],True,'canonical_weekly_reservation_calendar',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    bare_center_location=bool(re.fullmatch(r'(?:อยู่)?(?:อาคาร|ตึก)(?:อะไร|ไหน|ใด)[\s,?]*(?:ชั้น(?:อะไร|ไหน|ใด))?[?\s]*|(?:อยู่)?ชั้น(?:อะไร|ไหน|ใด)[?\s]*',q,re.I))
    if re.search(r'อาคาร|ตึก|ชั้น|\b(?:building|floor)\b',q,re.I) and (center_named or bare_center_location) and not re.search(r'เกม|game|equipment|อุปกรณ์|บุคลากร|\bperson\b',q,re.I):
        facet='building' if re.search(r'อาคาร|ตึก|\bbuilding\b',q,re.I) else 'floor'
        return Understanding([MeaningTask(question,'contact','C01','detail',facet)],True,'canonical_center_field',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'จอง|book|reserve|บริการ|service',q,re.I) and re.search(r'จันทร์|อังคาร|พุธ|พฤหัส|ศุกร์|เสาร์|อาทิตย์|\b(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b',q,re.I) and not re.search(r'ว่าง|occupied|\bfree\b|ตอนนี้|20\d\d-\d\d-\d\d',q,re.I):
        return Understanding([MeaningTask(question,'schedule','C11','detail','bookable_periods')],True,'canonical_bookable_calendar',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
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
        if devices and re.search(r'อยู่ไหน|อยู่ที่ไหน|อยู่(?:โซน|ซน)ไหน|ที่ตั้ง|which zone|where|location|located',q,re.I):
            return Understanding([MeaningTask(question,'equipment','C03','detail','location')],True,'canonical_equipment_location',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'\bwhat (?:id|documents?|identification)\b',q,re.I) and re.search(r'visitor|arrival|check.in|studio',q,re.I):
        return Understanding([MeaningTask(question,'reservation','C08','detail','owner_policy',canonical_operation='policy.checkin_documents')],True,'canonical_checkin_documents',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'ถ่าย(?:รูป|ภาพ|วิดีโอ)|อัดวิดีโอ|record(?:ing)?\s+(?:a\s+)?video|film(?:ing)?|screenshots?|capture',q,re.I) and not re.search(r'แข่ง|tournament|competition|price|ราคา',q,re.I):
        return Understanding([MeaningTask(question,'rules','C10','detail','owner_policy',canonical_operation='policy.capture')],True,'canonical_recording_scope',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    for cat,domain in [('C08','reservation'),('C09','payment'),('C10','rules')]:
        p=policy(index,cat,q)
        if p is not None and (p.ids or p.candidates):
            intents=p.metadata.get('policy_intents',[])
            tasks.append(MeaningTask(question,domain,cat,'detail','payer' if cat=='C09' and intents==['payer'] else 'owner_policy',canonical_operation='policy.'+intents[0] if len(intents)==1 else ''))
    if len(tasks)==1:
        return Understanding(tasks,True,'canonical_policy_action',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'เข้าไปเล่น.*เริ่ม|เริ่ม.*(?:ใช้บริการ|เข้าเล่น)|how.*(?:start|begin).*(?:play|visit)',q,re.I):
        return Understanding([MeaningTask(question,'reservation','C08','detail','owner_policy',canonical_operation='policy.booking_steps')],True,'canonical_booking_procedure',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'เหมา|rental|half.day|full.day',q,re.I):
        from .financial import rental_pool
        if rental_pool(index,q):return Understanding([MeaningTask(question,'rental','C07','price_calculate','amount_thb')],True,'canonical_rental_package',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'ราคา|กี่บาท|เตรียมเงิน|price|cost|how much',q,re.I) and not re.search(r'เหมา|rental|damage|ซ่อม|refund|คืนเงิน',q,re.I):
        from .financial import rate_pool,service_scope
        # Recognising a source-named price request is independent from whether
        # the owner has recorded its rate. The executor reports that source gap;
        # it must not erase another recognised need in a compound question.
        if rate_pool(index,q) or service_scope(index,q):return Understanding([MeaningTask(question,'service_fee','C06','compare' if re.search(r'เทียบ|compare|versus',q,re.I) else 'price_calculate','amount')],True,'canonical_financial_operation',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if index.bind('C05',q) and re.search(r'ปุ่ม|\bbuttons?\b|trigger|perform|กด',q,re.I) and not re.search(r'ทั้งหมด|อะไรบ้าง|\ball\b|\blist\b',q,re.I):
        from .source_operations import control_action
        from .control_scope import candidates
        action=control_action(index,q,candidates(index,q))
        if action and action.ids:return Understanding([MeaningTask(question,'game_controls','C05','control','input_bindings')],True,'canonical_source_declared_control_action',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if index.bind('C05',q) and re.search(r'ตีแรง|โจมตีหนัก|heavy attack|กดตรงไหน|กดอะไร',q,re.I):
        return Understanding([MeaningTask(question,'game_controls','C05','control','input_bindings')],True,'canonical_control_action',{'http_attempted':False,'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    if re.search(r'ปุ่ม|\bbuttons?\b|\bcontrols?\b',q,re.I) and not index.bind('C05',q) and not re.search(r'แข่ง|tournament|competition',q,re.I):
        return Understanding([MeaningTask(question,'game_controls','C05','list' if re.search(r'\b(?:buttons|controls|all)\b|ทั้งหมด|อะไรบ้าง',q,re.I) else 'control','input_bindings',ambiguous=True)],True,'canonical_missing_control_game',{'model_called':False,'meaning_review':{'basis':'canonical_source_operation'}})
    return None
