from pathlib import Path
import json
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip());f=p/'docs/130_full_improvement_r30_flow_20261002.md'
assert (r/'final_G3_all_summary.json').exists()
with (r/'flow_before_revision4.md').open('xb') as out:out.write(f.read_bytes())
s=f.read_text(encoding='utf-8').replace('ฉบับทบทวน 3','ฉบับทบทวน 4').replace('2026.10.02-full-improvement-r30-G2','2026.10.02-full-improvement-r30-G3').replace('หลัง G2','หลัง G3').replace('ทุกโมดูล 411 ข้อ','ทุกโมดูล 414 ข้อ')
s=s.replace('| P2 | EN fallback', '| P1 | ชื่อเกมอังกฤษมีคำ The/of/It จนภาษาไทยถูกนับเป็น EN | แยก multiword names/aliases ของเกมที่ยังอยู่ใน catalog ออกจากหลักฐานภาษา เฉพาะ mixed input; ไม่แก้ข้อความผู้ใช้ | คำถามไทยใช้ TH; ประโยค EN จริงและ language toggle ยังใช้ EN; เก็บ detected=mixed |\n| P2 | EN fallback')
s=s.replace('G 37 → G2 43 การนับนี้เป็นรอบทดสอบจริง ไม่แต่งจำนวน loop','G 37 (รวม assertion body/bodies ที่ผิด 3 ข้อ) → G2/G3 43 ตาม fixture v2; กรณี mixed title เพิ่มอีก 8 ตรวจภาษาเฉพาะ การนับนี้เป็นรอบทดสอบจริง ไม่แต่งจำนวน loop')
s=s.replace('รุ่น G2 ใช้ locale binding','รุ่น G2/G3 ใช้ locale binding')
s=s.replace('79 + 43 + 280 + 320 + 128 = 850 เคส','79 + 43 + 8 + 280 + 320 + 128 = 858 เคส (8 เคสเพิ่มตรวจภาษา มีข้อจำกัดเรื่อง content oracle)')
s=s.replace('candidate คะแนนต่ำมีผลผิด จึงเพิ่ม classified direction gate','candidate คะแนนต่ำมีผลผิด จึงเพิ่ม classified direction gate และพบ game-title function words จึงแยกชื่อจาก source ก่อนนับภาษา')
s += '''
## 7. ผลทบทวนรอบท้ายและข้อจำกัดที่เพิ่มจากการทดสอบจริง

- Full sweep ทดสอบทุก input ชุดหลักครบใน F, G2, G3 เก็บผลทั้งสามรุ่น; A/B ที่หยุดกลางคันไม่ใช้เป็นผลครบชุด
- HTTP grader รุ่น G2 เข้าใจ `input_guard_layout_retype` เป็น answer หนึ่งกรณี แก้เฉพาะตัวประเมิน และเก็บ raw/rescore แยก; รุ่น G3 ตรวจ guard mode/flag โดยตรง
- Runtime guard 500: 498/500 การบล็อกตาม policy ถูก; KIA-0337/KIA-0355 มี layout ผิดปนชื่อเกมอังกฤษ แต่ detector มอง repeat และให้ต่อ จึงตอบข้อมูลเกมแทนคำถาม มีชื่อเกมไม่ได้พิสูจน์ operation ถูก ต้องพัฒนาการตรวจ span รอบชื่อเกม/บริบทคำถามและตรวจ false positives ก่อนปรับ threshold
- Native detector 500 ใช้ corpus/threshold ต่างจาก production จึงไม่ใช้คะแนน 500/500 มาแทนความถูกต้องของ runtime หรือคำตอบจริง ทั้ง calibration และ test ถูกใช้ทบทวนคุณลักษณะมาก่อน ไม่ใช่ independent holdout
- บางการทดสอบพร้อมกัน 10 session ได้ 503 ขณะเครื่องมีโหลด; isolated G2 ผ่าน 10/10 ภายหลัง worker profile มีหนึ่ง worker และ queue wait 3 วินาที ต้องวัด idle/under-load ทั้งสองและอ่าน error body ก่อนระบุสาเหตุ ไม่เหมารวมว่าทุก 503 มาจาก WordPress หรือภาษา
- รายงานนี้ยังยืนยันข้อผิดจริงสี่ตัวอย่างในกติกา implicit/หลายประเด็น และจำนวนข้อไม่ผ่านราย corpus ไม่สรุปคะแนน route/validation ว่าเป็น answer accuracy
'''
f.write_text(s,encoding='utf-8',newline='\n')
with (r/'flow_revision4_final.md').open('x',encoding='utf-8') as out:out.write(s)
print(str(f))
