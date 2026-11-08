import sys,json,time,uuid
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r42_current_path.txt').read_text(encoding='utf-8'))
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(ROOT))
from app.pipeline.protected_intents import is_maximum_booking_lead_query
questions=['How far ahead must I book?','How many days in advance can I cancel my booking?','จองได้สูงสุดกี่เครื่อง','ต้องจองล่วงหน้ากี่วัน','จองล่วงหน้าได้สูงสุดกี่วัน','What is the maximum advance booking limit?']
rows=[dict(question=q,matched=is_maximum_booking_lead_query(q),expected=i>=4) for i,q in enumerate(questions)]
with (OUT/(sys.argv[1]+'_'+uuid.uuid4().hex[:6]+'.json')).open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
for row in rows:print(row)
