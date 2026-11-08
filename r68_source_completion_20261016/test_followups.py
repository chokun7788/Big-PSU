import sys,json
from datetime import datetime
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B),str(B/'system')]
from harness import configure,test_temp,equivalent_name_pruning
test_temp('followups');configure('common',False,db=B/'candidate06.sqlite');equivalent_name_pruning()
from app.knowledge.common.store import CommonStore
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.dialogue import state_from_answer
a=CommonAnswerer(CommonStore(B/'candidate06.sqlite'));cases=[
 ('PC มีหมายเหตุอะไรบ้าง','แล้ว PS5 ล่ะ','th',['PlayStation 5 #01 และ #02 ใช้รายการเกมเดียวกัน'],['PC #03']),
 ('ขอปุ่มควบคุม Mario Kart 8 Deluxe บน Nintendo Switch','แล้วปุ่ม B ล่ะ','th',['เบรก'],['A | เร่งเครื่อง']),
 ('List all controls for eFootball on PlayStation / PS5.','What does R2 do?','en',['Dash'],['Low Pass']),
 ('ขอปุ่มควบคุม Overcooked! 2 บน PlayStation / PS5','แล้วปุ่ม Circle ทำอะไร','th',['พุ่งตัว'],['ปุ่ม: เพิ่ม']),
 ('บุคคลทั่วไปเล่น PC 2 ชั่วโมงกี่บาท','ถ้าเป็นศิษย์เก่าล่ะ','th',['50.00'],['140.00']),
 ('PC for 2 hours, general adult price?','What about alumni?','en',['50.00'],['140.00'])]
out=[]
for first,second,lang,required,forbidden in cases:
 try:
  r=a.answer(first,locale=lang,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'));history=[{'role':'user','content':first},{'role':'assistant','content':r.answer,'common_read_state':state_from_answer(r)}]
  s=a.answer(second,locale=lang,history=history,at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'));text=s.answer if s else '';errs=[]
  if s is None:errs.append('no_answer')
  if s is not None and not s.validation.ok:errs.append('validation_rejected')
  for x in required:
   if x.casefold() not in text.casefold():errs.append('missing:'+x)
  for x in forbidden:
   if x.casefold() in text.casefold():errs.append('forbidden:'+x)
  out.append({'first':first,'second':second,'first_answer':r.answer,'second_answer':text,'errors':errs,'state':state_from_answer(s) if s else None})
 except Exception as e:out.append({'first':first,'second':second,'errors':[repr(e)]})
(B/'FOLLOWUPS_final03.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(out,ensure_ascii=False)[:9000])
