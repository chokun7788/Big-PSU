import sys,json,os,time
from pathlib import Path
from datetime import datetime
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B),str(B/'system')]
from harness import configure,test_temp,equivalent_name_pruning
test_temp('probe');configure('common',False);equivalent_name_pruning()
from app.knowledge.common.store import CommonStore
from app.knowledge.common.answer import CommonAnswerer
a=CommonAnswerer(CommonStore(B/'common.sqlite'))
qs=[('PC มีหมายเหตุอะไรบ้าง','th'),('What are the service notes for Cockpit?','en'),('นายธนชาติ เอ่งฉ้วน สังกัดอะไร','th'),('member_68e4915433f294b7 วาระ','th'),('Mario Kart 8 Deluxe ปุ่ม A ทำอะไร','th'),('What does A do in Mario Kart 8 Deluxe on Nintendo Switch?','en'),('What time is the afternoon session? I need the official answer.','en'),('พกอาหารจากข้างนอกเข้าไปได้ไหม','th')]
with (B/'PROBE_01.jsonl').open('x',encoding='utf8') as out:
 for q,lang in qs:
  st=time.perf_counter()
  try:
   r=a.answer(q,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'))
   row={'q':q,'answer':r.answer if r else None,'plan':r.decision_artifact if r else None,'elapsed':time.perf_counter()-st}
  except Exception as e:row={'q':q,'exception':repr(e)}
  out.write(json.dumps(row,ensure_ascii=False)+'\n');out.flush();print(json.dumps(row,ensure_ascii=False)[:1900],flush=True)
