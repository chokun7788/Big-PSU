import json
from pathlib import Path
root=Path(__file__).parent;report=Path((root/'r28_report_path.txt').read_text(encoding='utf-8').strip())
data=json.loads((report/'guard_prior_audit.json').read_text(encoding='utf-8'));rows=data['records'];s=data['summary']
lines=['# วิเคราะห์ input guard และเว็บจริง r28','', '## ข้อผิดจริงที่พบเฉพาะเว็บ','',
'คำถามอังกฤษ 3 แบบเรื่องนำอุปกรณ์มาและรับผิดชอบคุณภาพถูกหยุดก่อน routing. ตัวกรองเดิมไม่รู้จัก `its` ซึ่งเป็นสรรพนามอังกฤษ จึงแปลงสมมติฐานเป็น “ระห” แล้วพบใน corpus ไทย: source_quality 0.499681, target_quality 0.601378, target_seen=True. สูตรให้ score ของ span 0.525159 และ score รวม 0.52728 ซึ่งเกิน threshold 0.39. สิ่งนี้ไม่ใช่หลักฐานว่าประโยคอังกฤษเป็นภาษาแป้นผิด แต่ระบบเดิมยอมให้ span เดียวตัดสินทั้งประโยค.',
'','## สิ่งที่แก้และเหตุผล','',
'เพิ่ม closed-class English pronouns/คำหน้าที่ลงใน language prior เดิม. นี่คือคำจริงที่ไม่ควรตีเป็น wrong-layout ไม่มี mapping typo ไปยังคำตอบหรือ alias ของทั้งประโยค. คำว่า its ได้รับ lexical protection; ไม่ปิด guard และไม่เปลี่ยน threshold. Profile ID รวม prior แล้ว เพราะ prior มีผลต่อโมเดล. ชุดคำศัพท์เพิ่มเติม: '+', '.join(s['added_prior_words']),
'',f"ตรวจ guard ก่อน/หลังกับ {s['total']} ข้อ: ถูกหยุดก่อน {s['before_blocked']}, หลัง {s['after_blocked']}; ปลดการหยุด {s['no_longer_blocked']} และเพิ่มการหยุด {s['newly_blocked']}. การตรวจนี้ไม่ใช่การตรวจคำตอบหรือการแปลครบทั้ง 4,283 ข้อ.",
'','## ข้อความผิดแป้นที่ใช้ตรวจ','',
'`g]jo` และ “อยากถามว่า g]jo ได้ไหม” ถูกหยุดทั้งก่อนและหลัง. `l;ylfu` ไม่ถูกหยุดทั้งก่อนและหลัง: score ประมาณ 0.245 ต่ำกว่า 0.39. จึงเอาออกจาก unit ที่เพิ่งเพิ่มซึ่งเดิมสมมติว่าควรถูกหยุด; เก็บ diagnostic ใน audit ให้เห็น ไม่ปรับ threshold ตามข้อนี้ และไม่ได้ทดสอบ end-to-end ของคำทักทายนี้ในรอบนี้. ไม่อ้างว่าตรวจ wrong-layout ได้ทุกกรณี.',
'','## สถานะระบบไม่ว่างระหว่างทดสอบ','',
'final_http280 รอบแรกได้ HTTP 503 สองคำขอแรกเพราะสอง test clients รันพร้อมกันกับคำถาม clarification ที่ใช้เวลาประมาณ 11 วินาที ขณะ backend รับงานทีละคำถามและ queue รอ 3 วินาที. เป็นข้อผิดของวิธีรันทดสอบกับการจำกัด concurrency ที่มีอยู่; เก็บผลเดิมทั้งหมด ไม่แก้ worker ให้ปล่อยงานชนกัน. ชุด verified รันทีละชุดและรายงาน transport แยกจากความถูกของเนื้อหา. ข้อจำกัดผู้ใช้พร้อมกันหลายคนยังมีอยู่ และ retry UI ต้องใช้ retryable/server_busy ตามที่ระบบส่งกลับ.',
'','## สิ่งที่ยังต้องตรวจต่อจากชุดเก่า','',
'เหลือข้อความ 36 ข้อจากชุด multi-error r15 ที่ guard ยังหยุดเหมือนก่อนแก้. ต้องอ่านความหมายกับ mutation ก่อนตัดสินว่า false rejection หรือ input เสียจริง; รอบนี้ไม่ได้ให้คะแนนคำตอบของ 36 ข้อนี้. ลำดับถัดไปควรตรวจ layout_span/source_quality/target_quality/target_seen และบริบทประโยค เพื่อลดการตัดสินทั้งประโยคจาก span เดียวโดยคง wrong-layout controls. ด้านล่างคือรายการจริงที่ยังถูกหยุด (ตัด negative controls ที่ตั้งใจให้หยุดออก).','',
'| ID | ข้อความ | Score | เหตุผล |','|---|---|---|']
pending=[r for r in rows if r['after_blocked'] and r['corpus']!='layout_diagnostic']
assert len(pending)==36
for r in pending:
    lines.append('| '+r['id']+' | '+r['question'].replace('|','\\|').replace('\n',' ')+' | '+str(r['after']['layout_score'])+' | '+r['after']['layout_reason'].replace('|','\\|')+' |')
with (report/'INPUT_GUARD_ANALYSIS_TH.md').open('x',encoding='utf-8') as f:f.write('\n'.join(lines)+'\n')
print(json.dumps({'pending_old_multi_error':len(pending),'newly_blocked':s['newly_blocked'],'new_profile':s['new_profile']},ensure_ascii=False))
