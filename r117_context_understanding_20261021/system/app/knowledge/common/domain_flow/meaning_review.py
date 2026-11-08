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
        factual=[t for t in raw_tasks if isinstance(t,dict) and not re.fullmatch(r'(?:please |กรุณา|ขอ|ช่วย|ข้อมูลที่ยืนยันได้|ตอบสั้น.?|answer briefly|verify|check|official answer|ครับ|ค่ะ|หน่อย|\s|[?!.,:])+',str(t.get('quote','')),re.I)]
        if len(factual)>1:return result
    from app.pipeline.router import _looks_like_game_control_query,_looks_like_competition_rule_query
    from .understanding import MeaningTask,Understanding
    q=norm(question);frame=None;basis=None
    competing=re.search(r'ราคา|กี่บาท|นำ.*มา|เอา.*มา|ค่าซ่อม|ค่าปรับ|how much|\b(?:cost|price|fee|bring|repair)\b',q)
    competition_rule=bool(re.search(r'ลงแข่ง|แข่งขัน|\b(?:match|competition|tournament)\b',q) and re.search(r'อนุญาต|ห้าม|กฎ|กติกา|\b(?:allowed|permitted|banned|remap|rules?|policy)\b',q))
    if _looks_like_game_control_query(q) and re.search(r'ปุ่ม|\b(?:buttons?|controls?)\b',q) and not competing and not competition_rule and index.bind('C05',q):
        frame=('game_controls','C05','list' if re.search(r'ทั้งหมด|อะไรบ้าง|อะไรมั่ง|\b(?:all|buttons|controls)\b',q) else 'control','input_bindings')
        basis='legacy_control_frame_and_current_source_target'
    elif (_looks_like_competition_rule_query(q) or competition_rule) and re.search(r'ลงแข่ง|แข่งขัน|รายการแข่ง|\b(?:match|competition|tournament)\b',q) and not re.search(r'อาหาร|เครื่องดื่ม|สูบบุหรี่|กฎศูนย์|\b(?:smoking|food|drinks|studio rules)\b',q):
        frame=('competition_rules','C13','rule_lookup','rule_clause');basis='legacy_competition_frame_with_explicit_context'
    elif requested_resources(q) and re.search(r'ว่าง|available|\bfree\b|ถูกจอง',q) and re.search(r'วันนี้|พรุ่งนี้|\d{1,2}(?::\d\d|\s*(?:am|pm))|20\d\d[-/]',q) and not competing:
        frame=('live','C12','availability','live_status');basis='dated_named_resource_availability'
    elif index.bind('C04',q) and re.search(r'คือเกมอะไร|เป็นเกมอะไร|\bwhat (?:is|kind of game)\b',q) and not competing and not re.search(r'แนวเกม|ประเภท|กี่คน|วิธี|\b(?:genre|players|controls|how to)\b',q):
        frame=('games','C04','detail','summary');basis='current_game_and_definition_request'
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
