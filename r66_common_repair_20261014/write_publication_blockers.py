import json,collections
from pathlib import Path
B=Path(__file__).resolve().parent;p=B/'PUBLICATION_BLOCKERS_TH.md';assert not p.exists()
source=sorted(B.glob('RELEASE_AUDIT_*.json'))[-1];d=json.loads(source.read_text(encoding='utf-8'));counts=collections.Counter();missing=collections.Counter()
for r in d['publication_blockers']:
 for e in r['publication_blockers']:
  counts[e]+=1
  if 'required before publication' in e:missing[e.split(':')[0]]+=1
lines=['# ข้อที่ยังปิดการเผยแพร่ร่าง Format กลาง','','อ้างอิง '+source.name+'; candidate '+str(d['candidate_records'])+' records; blocked '+str(d['records_blocked_from_publication'])+'; active release ว่าง ข้อมูลยังอยู่ครบ มิใช่ถูกลบเมื่อไม่ผ่าน gate','','## ต้องแยกงานเทคนิคกับ facts ที่ยังไม่ทราบ','','- source needs factual review: เป็น trust state ของแหล่งที่ย้ายมา ไม่ได้แปลว่าทุกข้อพิสูจน์แล้วว่าผิด ต้องยืนยันเอกสาร/แหล่งฉบับที่จะใช้งาน ไม่สร้าง owner attestation แทนเจ้าของ','- Time-sensitive content requires confirmed validity: วันที่ได้รับไฟล์ไม่ใช่วันเริ่มใช้ ต้องมีช่วงมีผลของอัตรา/บริการ/รายการที่ไวต่อเวลา','- required before publication: ข้อมูลย้ายมายังไม่ครบ core schema บางช่องเป็น metadata ที่เสนอจาก source ได้ เช่น facet/excerpt completeness; บางช่องเช่น gesture/context ห้ามเดา ต้องเก็บเป็น partial จนมีหลักฐานพอ','- การอ่าน draft ใน eval/Owner preview ได้ ไม่เท่ากับ publish gate ผ่าน; อย่าเปิด evaluation override ในเว็บ production เพื่อหลบ gate','','## Core fields ที่ยังขาด (นับ records ที่พบ)','','| Field | Records |','|---|---:|']
lines += ['| '+k+' | '+str(v)+' |' for k,v in missing.most_common()]
lines += ['','## สาเหตุทั้งหมดและจำนวน (หลายสาเหตุใน record เดียวได้)','','| Reason | Occurrences |','|---|---:|']
lines += ['| '+k.replace('|','/')+' | '+str(v)+' |' for k,v in counts.most_common()]
lines+=['','## ราย record','','ข้อมูลนี้เป็นรายการที่ต้องจัดการก่อน release ไม่ใช่สิ่งที่ส่งไปเป็นคำตอบให้ผู้ใช้ทุกครั้ง','']
for x in d['publication_blockers']:
 lines+=['### '+x['record_id']+' — '+x['kind'],'']+['- '+e for e in x['publication_blockers']]+['']
p.write_text('\n'.join(lines)+'\n',encoding='utf-8');print(json.dumps({'records_blocked':len(d['publication_blockers']),'missing_core_fields':dict(missing),'path':str(p)},ensure_ascii=False))
