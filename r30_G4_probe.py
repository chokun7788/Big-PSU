import sys,os,json
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(p))
os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
from app.pipeline.protected_intents import is_weekly_booking_window_query
from app.pipeline.engine import answer_question_pipeline_debug
from app.booking.live_status import _unavailable
from unittest.mock import patch
for q in ['PC1 จองได้ช่วงไหนที่ว่างวันศุกร์ช่วงบ่าย','Which PC1 booking slots are available on Friday afternoon?','วันศุกร์ช่วงบ่ายจองได้หรือเป็นเวลาปิดดูแลเครื่อง']:
    print(json.dumps({'weekly':is_weekly_booking_window_query(q),'question':q},ensure_ascii=False),flush=True)
queries=[('th','CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม'),('en','Which platform does CS2 use, and are unauthorized game client modifications allowed?'),('th','CS2 ปิดรับสมัครแล้วเพิ่มเพื่อนเข้า roster ได้ปะ'),('en','CS2 registration is closed; can we add a teammate to the roster?'),('th','RoV ใช้สกินพิเศษได้หรือเปล่า'),('en','Can we use special skins in RoV?'),('th','เทคเคนแต่ละเกมแข่งกี่รอบ'),('en','How many rounds per game in Tekken?'),('th','วันศุกร์ช่วงบ่ายจองได้หรือเป็นเวลาปิดดูแลเครื่อง'),('en','Can we book on Friday afternoon, or is it maintenance?'),('en','Tekken VII tournament rules'),('th','เทคเคนภาค 7 กฎแข่ง')]
with patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled fixture; no occupancy oracle',error_code='fixture_offline')):
    for loc,q in queries:
        a=answer_question_pipeline_debug(q,locale=loc,experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
        print(json.dumps({'question':q,'locale':loc,'answer':a.answer,'mode':a.mode,'valid':a.validation.ok},ensure_ascii=False),flush=True)
