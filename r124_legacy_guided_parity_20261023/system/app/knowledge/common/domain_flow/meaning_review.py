"""Independent legacy intent frames check explicit purpose, not answer values.

Use narrow supported frames to stop a model from silently reinterpreting an
explicit controls/tournament/live/role request as a generic game description.
Current source readers still resolve all identities, evidence and permissions.
"""
import re,json
from .scope import norm,requested_resources

def review(question,index,result):
    if index is None:return result
    if result.reason=='meaning_model_identity_mismatch':return result
    from .routing import split_needs
    # Never collapse multiple needs into a single recovered frame.
    if len(result.tasks)>1 or len(split_needs(question,index))>1:return result
    try:raw_tasks=json.loads(result.event.get('raw_content','{}')).get('tasks',[])
    except (ValueError,TypeError,AttributeError):raw_tasks=[]
    if len(raw_tasks)>1:
        from .understanding import style_only_quote
        factual=[t for t in raw_tasks if isinstance(t,dict) and not (style_only_quote(str(t.get('quote',''))) and t.get('domain')=='general' and not t.get('target') and not t.get('constraints')) and not re.fullmatch(r'(?:please |กรุณา|ขอ|ช่วย|ข้อมูลที่ยืนยันได้|ตอบสั้น.?|answer briefly|verify|check|official answer|ครับ|ค่ะ|หน่อย|\s|[?!.,:])+',str(t.get('quote','')),re.I)]
        if len(factual)>1:return result
    from app.pipeline.router import _looks_like_game_control_query,_looks_like_competition_rule_query
    from .understanding import MeaningTask,Understanding
    q=norm(question);frame=None;basis=None
    competing=re.search(r'ราคา|กี่บาท|นำ.*มา|เอา.*มา|ค่าซ่อม|ค่าปรับ|how much|\b(?:cost|price|fee|bring|repair)\b',q)
    competition_rule=bool(re.search(r'ลงแข่ง|แข่งขัน|\b(?:match|competition|tournament)\b',q) and re.search(r'อนุญาต|ห้าม|กฎ|กติกา|\b(?:allowed|permitted|banned|remap|rules?|policy)\b',q))
    from .precision import equipment
    from .distilled_policy import requested_frame
    taught_frame=requested_frame(question,index)
    from app.pipeline.protected_intents import _food_facet,_asks_personal_power
    if _food_facet(q)=='food_bring_permission' or _asks_personal_power(q):
        from .readers import policy
        if policy(index,'C10',q) is not None:
            frame=('rules','C10','detail','owner_policy');basis='legacy_protected_intent_current_native_policy'
    elif re.search(r'\b(?:what|which)\s+(?:id|identification|documents?)\b|\b(?:id|identification|passport|documents?).{0,35}(?:need|bring|show|present)\b',q) and re.search(r'\b(?:visitor|studio|check.in|arrival|service)\b',q) and not re.search(r'(?:psu|steam|riot|discord|game|account|api)\s*(?:id|identifier|account)|รหัส|บัญชี',q):
        from .readers import policy
        if policy(index,'C08',q) is not None:
            frame=('reservation','C08','detail','owner_policy');basis='identification_documents_requested_before_visitor_eligibility'
    elif taught_frame is not None:
        frame=taught_frame;basis='distilled_price_operation_with_current_native_rate_relation'
    elif index.bind('C04',q) and re.search(r'\b(?:what|which)\b.{0,45}\bbook\b.{0,20}\b(?:play|paly)\b',q) and not competing:
        frame=('games','C04','availability','studio_services');basis='source_bound_game_to_bookable_service_relation'
    elif re.search(r'หลายโซน|มากกว่าหนึ่งโซน|multiple zones|more than one zone',q) and re.search(r'เกม|\bgames?\b',q) and not competing:
        frame=('games','C04','list','zone');basis='explicit_set_predicate_over_current_game_zone_relations'
    elif re.search(r'คืออะไร|\bwhat is\b|\bwhat are\b',q) and index.bind('C03',q) and not competing and not re.search(r'ปุ่ม|\b(?:buttons?|controls?)\b',q):
        frame=('equipment','C03','detail','usage');basis='source_equipment_definition_before_name_echo'
    elif re.search(r'\b(?:gpu|cpu|ram)\b|การ์ดจอ|แรม',q) and re.search(r'\b(?:model|inside|specifications?|specs?)\b|รุ่น|สเปก',q) and equipment(index,q) is not None and not competing:
        frame=('equipment','C03','detail','specifications');basis='explicit_hardware_component_with_typed_device'
    elif _looks_like_game_control_query(q) and re.search(r'ปุ่ม|\b(?:buttons?|controls?)\b',q) and not competing and not competition_rule and index.bind('C05',q):
        frame=('game_controls','C05','list' if re.search(r'ทั้งหมด|อะไรบ้าง|อะไรมั่ง|\b(?:all|buttons|controls)\b',q) else 'control','input_bindings')
        basis='legacy_control_frame_and_current_source_target'
    elif ((_looks_like_competition_rule_query(q) or competition_rule) and re.search(r'ลงแข่ง|แข่งขัน|รายการแข่ง|\b(?:match|competition|tournament)\b',q) or
          re.search(r'กติกา|rulebook|tournament rules',q) and re.search(r'\bmap\s*pool\b|แผนที่ในการแข่งขัน',q)) and not re.search(r'อาหาร|เครื่องดื่ม|สูบบุหรี่|กฎศูนย์|\b(?:smoking|food|drinks|studio rules)\b',q):
        frame=('competition_rules','C13','rule_lookup','rule_clause');basis='legacy_competition_frame_with_explicit_context'
    elif requested_resources(q) and re.search(r'ว่าง|available|\bfree\b|ถูกจอง',q) and re.search(r'วันนี้|พรุ่งนี้|\d{1,2}(?::\d\d|\s*(?:am|pm))|20\d\d[-/]',q) and not competing:
        frame=('live','C12','availability','live_status');basis='dated_named_resource_availability'
    elif index.bind('C04',q) and re.search(r'คือเกมอะไร|เป็นเกมอะไร|\bwhat (?:is|kind of game)\b',q) and not competing and not re.search(r'แนวเกม|ประเภท|กี่คน|วิธี|\b(?:genre|players|controls|how to)\b',q):
        frame=('games','C04','detail','summary');basis='current_game_and_definition_request'
    elif index.bind('C04',q) and re.search(r'โซนไหน|ที่โซนใด|which studio zone|which zone.*(?:has|offer)|what zone',q) and not competing:
        frame=('games','C04','detail','zone');basis='current_game_and_explicit_zone_request'
    elif re.search(r'กี่เกม|how many (?:distinct )?games|number of games',q) and not competing and not re.search(r'แข่ง|รอบชิง|finals?|tournament|match|competition',q):
        frame=('games','C04','count','game_catalog');basis='explicit_catalog_count_request'
    elif re.search(r'ยกเลิก.*จอง|cancel.{0,20}(?:booking|reservation)',q) and not re.search(r'เหมา|rental|refund|คืนเงิน|การแข่งขัน|tournament',q):
        from .readers import policy
        cancellation=policy(index,'C08',q)
        if cancellation and (cancellation.metadata.get('policy_intents') or cancellation.candidates):
            frame=('reservation','C08','detail','owner_policy');basis='explicit_booking_cancellation_action'
    elif re.search(r'เช็[คก]อิน|check.in|จอง.*(?:ทำยังไง|อย่างไร|ยังไง)|how (?:can|do|should) (?:i|we) (?:book|reserve)',q) and not re.search(r'แข่ง|tournament|match|competition|luggage|สัมภาระ',q):
        from .readers import policy
        procedure=policy(index,'C08',q)
        if procedure is not None:
            frame=('reservation','C08','detail','owner_policy');basis='booking_action_before_game_context'
    elif re.search(r'ตำแหน่ง|หน้าที่|\b(?:position|role)\b',q) and re.search(r'ใคร|ชื่อ|\b(?:who|what position|what role|mr\.?|ms\.?|mrs\.?)\b',q):
        frame=('members','C02','role_lookup','role');basis='explicit_personnel_role_request'
    if frame is None:return result
    prior=result.tasks[0] if result.accepted and result.tasks else None
    if prior and (prior.category,prior.operation,prior.facet)==frame[1:]:return result
    task=MeaningTask(question,*frame[:2],frame[2],frame[3],target=prior.target if prior else '',
                     constraints=prior.constraints if prior else [],ambiguous=False)
    revised=Understanding([task],True,'independent_context_frame',result.event)
    revised.event['meaning_review']={'basis':basis,'model_plan_accepted':result.accepted,'model_reason':result.reason,
        'prior_tasks':[t.as_dict() for t in result.tasks],'business_facts_added':False}
    return revised


_single_need_review=review
def review(question,index,result):
    # Review each explicit need independently; never merge a compound query
    # into one recovered frame. No additional model calls or business answers.
    if not result.accepted or len(result.tasks)<=1:return _single_need_review(question,index,result)
    from .understanding import Understanding
    revised=[];audits=[]
    for task in result.tasks:
        # A source-quoted target can still belong to a DIFFERENT need. Keep
        # cross-need targets only with an explicit anaphoric relation.
        if task.target and task.target not in task.quote and not re.search(r'\b(?:it|its|same|that|those)\b|เดียวกัน|เครื่องนั้น|เกมนั้น',task.quote,re.I):
            audits.append({'basis':'unrelated_cross_task_target_removed','source_target':task.target,'task_quote':task.quote,'business_facts_added':False})
            task.target=''
        child_event={'raw_content':json.dumps({'tasks':[task.as_dict()]},ensure_ascii=False)}
        child=Understanding([task],True,result.reason,child_event)
        checked=_single_need_review(task.quote,index,child)
        if len(checked.tasks)==1:
            revised.append(checked.tasks[0])
            if checked.event.get('meaning_review'):audits.append(checked.event['meaning_review'])
        else:revised.append(task)
    result.tasks=revised
    if audits:result.event['independent_subtask_reviews']=audits
    return result
