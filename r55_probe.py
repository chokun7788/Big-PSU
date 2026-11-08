import sys,json,traceback
from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(ROOT))
from app.pipeline.service_query_completion import *
from app.pipeline.user_service_facts import answer_user_service_facts
from app.session.conversation_plan import resolve_request_plan
from app.rules.matcher import RuleMatcher
from app.booking.live_status import _requested_resource_number
from app.pipeline.competition_conversation_signals import is_more_rule_request
for q,l in [('มา4คน เล่นอันไหนดี','th'),('we are 4 ppl what can we play','en'),('อัพสลิปผืด ส่งใหม่ทางไหน','th'),('เพื่อนยังมาไม่ถึง เช็คอินให้ทั้งแก๊งได้ไหม','th'),('ไปถึงต้องเอาบัตรไรไปมั่ง','th'),('which documnts do i bring for checkin','en'),('Is there seating where I can rest while waiting for friends?','en'),('General adult PC for two hours, how much?','en'),('คนทั่วไปมี100บาทเล่นPCได้กี่รอบ','th'),('Nintendo มีเกมไรมั่ง','th'),('Cockpit เล่นเกมอะไร','th'),('ศูนย์มีเกมทั้งหมดกี่เกม','th'),('What are your opening hours?','en'),('How do I shoot and reload in CS2?','en'),('What PC specifications does the studio have?','en'),('PC มีเกมอะไรบ้าง และคนทั่วไปเล่นสองชั่วโมงเท่าไหร่','th')]:
    try:
        p=resolve_request_plan(q,[],locale=l);a=answer_user_service_facts(q,l) or answer_explicit_source_operation(q,l,RuleMatcher.default())
        print(q,'PLAN',p and p.get('resolved_query'),'PARTS',split_service_operations(q),'ANSWER',a and a['answer'][:600],flush=True)
    except Exception:traceback.print_exc()
for q in ('VR 9:00','VR30นาที','VR#1 เวลา09:00','PC10','PC10:00','PC1','VR 9 pm'):
    print(q,_requested_resource_number(q,'vr' if 'VR' in q else 'pc'))
print('MORE',is_more_rule_request('ต่อ เอากฎที่เหลือ'))
