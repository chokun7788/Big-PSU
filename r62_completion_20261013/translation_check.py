import sys,json,copy
from pathlib import Path
B=Path(__file__).resolve().parent
sys.path.insert(0,str(B.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'))
from tests.test_common_content_r58 import record
from app.knowledge.common.translation import translate_draft,protected
from app.pipeline.request_deadline import request_deadline
cases=[
 ('policy','details','ห้ามนำเมาส์หรือคีย์บอร์ดส่วนตัวมาใช้'),
 ('news','body','ข้อมูลทดลอง: รอบนี้ราคา60บาท เล่นได้30นาที วันที่ 2026-10-13 ห้ามต่อเวลาเอง ติดต่อ https://example.invalid/help'),
 ('faq','answer','ข้อมูลทดลอง: คนเล่นต้องเป็นคนที่จองหรือมีชื่ออยู่ในรายการจอง ไม่สามารถให้คนอื่นเล่นแทนได้')]
rows=[]
for kind,key,source in cases:
 r=record(kind);r['fields'][key].update(status='known',value={'th':source,'en':''},evidence_refs=[],note='')
 for field in r['fields'].values():
  if field.get('note') is None:field['note']=''
 original=copy.deepcopy(r)
 with request_deadline(35):out=translate_draft(r)
 translated=out['record']['fields'][key]['value']['en']
 # This is a fixture semantic check; it does not certify all future translations.
 ok=r==original and protected(source)==protected(translated) and out['saved'] is False and out['published'] is False and out['record']['localization']['en_status']=='agent_translated' and any(w in translated.casefold() for w in ['not','cannot','prohibited','forbidden','must'])
 rows.append({'kind':kind,'source':source,'english':translated,'passed':ok,'source_unchanged':r==original,'protected_tokens':protected(source),'not_saved_or_published':True})
 print(kind,ok,translated,flush=True)
(B/'TRANSLATION_CHECK.json').write_text(json.dumps({'cases':len(rows),'passed':sum(r['passed'] for r in rows),'results':rows,'human_reviewed':False,'fixture_only':True},ensure_ascii=False,indent=2),encoding='utf-8')
assert all(r['passed'] for r in rows)
