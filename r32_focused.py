import os,sys,json,time
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(P));os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0';os.environ['PYTHONDONTWRITEBYTECODE']='1'
R=Path((ROOT/'r32_report_path.txt').read_text().strip())
from r31_full_corpus import plain
from app.pipeline.engine import answer_question_pipeline_debug
from app.booking.live_status import _unavailable
cases=[('th','พรุ่งนี้ 13:00 Nintendo Switch (1-4 Persons) วางหรือเปล่า'),('th','PC1 10:00 วางมั้ย'),('th','PC1 วางเครื่องตรงไหน'),('th','ขออ้างอิงกติกา อารีน่สออฟเวเลอร์ ในหัวข้อจำนวผู้เล่นต่อทีม หน่อย'),('en','What are the RoV competition rules for team size?'),('th','ตาม rulebook CS2 คุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน ต้องทำยังไง'),('en','CS2 competition rules: eligibility, roster and registration'),('th','ตามกติกา CS2 ขอบเขตและข้อมูลของรายการ'),('th','กติกา CS2 การตั้งค่าในเกม'),('en','CS2 competition in-game settings'),('th','กติกา CS2 อุปกรณ์ที่ใช้แข่งขัน'),('en','CS2 competition equipment rules'),('en','Wherw can you pay VALORANT'),('en','Where can I pay for my booking?'),('th','Pokémon Champions อยู่โซซนไหน')]
with (R/(sys.argv[1]+'_focused.jsonl')).open('x',encoding='utf-8') as out:
 for loc,q in cases:
  with patch('app.booking.live_status.get_live_booking_status',side_effect=lambda d:_unavailable(d,'controlled offline r32 fixture',error_code='fixture_offline')):
   start=time.perf_counter();r=answer_question_pipeline_debug(q,locale=loc,experimental_allow_llm=False,experimental_rag_fallback=True,global_timeout_sec=20)
  row={'question':q,'locale':loc,'result':plain(r),'elapsed':time.perf_counter()-start};out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush();print(json.dumps({'q':q,'mode':r.mode,'valid':r.validation.ok,'answer':r.answer[:450]},ensure_ascii=False),flush=True)
