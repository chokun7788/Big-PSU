"""Canonical task/predicate vocabulary. No owner identities or business values."""
import re
from .task_contracts import TASKS
from .query_contract import normalize,live_request

ALIASES={'players':'game_players','controls':'game_controls','rules':'competition_rules','booking':'procedure','checkin':'procedure','calendar':'schedule','games':'game_at_studio','location':'center_location','equipment':'equipment_list'}
PREDICATES={'game_players':'game_player_count','game_overview':'game_summary','game_how_to_play':'game_how_to_play','game_controls':'input_bindings','game_at_studio':'offered_game_location','center_location':'center_location','procedure':'booking_steps','price':'current_rate','rental':'rental_package','live_status':'live_resource_available','schedule':'service_schedule','policy':'policy_applicability','competition_rules':'rule_clause','equipment_list':'equipment_in_scope'}

def canonical(task):
    task=ALIASES.get(task,task)
    return task if task in TASKS else 'unresolved'

def infer(question,records=None,ids=None):
    q=normalize(question)
    from .query_scope import operation
    if live_request(q):task='live_status'
    elif re.search(r'ราคา|ค่าบริการ|กี่บาท|\b(?:prices?|cost|fees?|rates?|how much|budget)\b',q):task='rental' if re.search(r'เหมา|ครึ่งวัน|เต็มวัน|\b(?:rental|half.day|full.day)\b',q) else 'price'
    elif re.search(r'อยู่(?:ตรง|ที่)?ไหน|ที่อยู่|\b(?:where is|address|location)\b',q):task='center_location'
    elif re.search(r'กี่คน|\b(?:how many players|player count)\b',q):task='game_players'
    elif re.search(r'คือเกมอะไร|เป็นเกมอะไร|\b(?:what is|what kind of game|game overview)\b',q):task='game_overview'
    else:task=canonical(operation(q))
    op=operation(q)
    if task=='game_overview' and op in {'policy','booking','checkin','rules','rental','price','calendar'}:task=canonical(op)
    if re.search(r'เล่นได้ที่ไหน|อยู่โซนไหน|\bwhere can (?:i|you) play\b|\bwhich (?:studio )?zone\b',q):task='game_at_studio'
    # The same booking verb has different predicates. This changes routing
    # metadata, not source facts or provider availability.
    timetable=bool(re.search(r'วันและเวลา|วันไหน|วันใด|\b(?:days?|monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b',q) and re.search(r'จอง|ให้บริการ|\b(?:book|booking|slots?|service)\b',q) and re.search(r'เวลา|ช่วงเช้า|ช่วงบ่าย|\b(?:morning|afternoon|slots?|times?)\b',q))
    timetable=timetable or bool(re.search(r'จอง.{0,12}(?:ได้ช่วงไหน|ได้เวลาไหน|ได้กี่โมง)|\b(?:what|which)\s+(?:times?|hours?|periods?)\b.{0,25}\b(?:book|booking|reserve)\b|\bbook\b.{0,20}\b(?:what|which)\s+(?:times?|hours?|periods?)\b',q))
    if timetable:task='schedule'
    if re.search(r'ปิดกี่โมง|เปิดถึงกี่โมง|\bwhat time (?:do you|does the studio) close\b|\bhow late (?:are you|is the studio) open\b',q):task='schedule'
    kinds={records[k]['kind'] for k in ids or [] if records and k in records}
    if task=='center_location' and 'equipment_model' in kinds and 'center' not in kinds:task='equipment_location'
    if 'game' in kinds and re.search(r'ต้องจอง(?:อะไร|เครื่องไหน)|\b(?:what|which)\b.{0,28}\bbook\b.{0,20}\bplay\b',q):task='game_at_studio'
    if task=='game_overview' and kinds and 'game' not in kinds:
        task='equipment_explain' if kinds&{'equipment_model','resource','service'} else 'center_overview' if 'center' in kinds else 'unresolved'
    booking_required=bool(re.search(r'โดยไม่จอง|ไม่.{0,8}จอง|ต้องจอง(?:ก่อนไหม|ก่อน|ไหม|มั้ย|ล่วงหน้า)|เดินเข้าไป|\bwithout\b.{0,14}\bbook\w*|\b(?:walk.in|booking required|must book|need to book)\b',q))
    if booking_required and task not in {'price','rental','schedule','live_status'}:task='policy'
    predicate=PREDICATES.get(task,task)
    if booking_required and task=='policy':predicate='booking_required'
    if task=='schedule':
        if re.search(r'เปิดไหม|ปิดไหม|\b(?:open today|open tomorrow|open on|are you open)\b',q):predicate='access_open'
        elif re.search(r'ปิดกี่โมง|เปิดถึงกี่โมง|\b(?:close|how late)\b',q):predicate='closing_time'
        elif timetable or re.search(r'ช่วงจอง|\bbookable\b',q):predicate='bookable_period'
    if task=='policy':
        if re.search(r'นำ|เอา.{0,15}มา|\bbring\b',q):predicate='bring_permission'
        elif re.search(r'รับประทาน|กิน|ดื่ม|\b(?:eat|drink|consume)\b',q):predicate='consumption_permission'
    return {'task':canonical(task),'predicate':predicate,'contract_version':'common_intent_contract_v1'}
