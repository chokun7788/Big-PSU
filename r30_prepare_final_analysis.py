from pathlib import Path
root=Path(__file__).parent
s=(root/'r30_build_analysis.py').read_text(encoding='utf-8')
s=s.replace("prefix='VERIFIED_' if run!='final_F' else ''", "prefix='FINAL_G2_'")
s=s.replace("inventory=json.loads((r/'final_F_inventory.json')", "inventory=json.loads((r/'final_G2_inventory.json')")
s=s.replace('final_F_all_results.jsonl','final_G2_all_results.jsonl')
s=s.replace("'6. ขอบที่พบเพิ่ม:","'6. ขอบที่พบเพิ่ม:")
s=s.replace("'', '## หลักฐานก่อน/หลัง'", "'7. กฎ implicit: ผู้เล่นหลัก/เปลี่ยนตัว/ปิดเลือดและศพหลุดไปเกมหรือหัวข้อหน้างาน; ผูก target และ proposition กับข้อ source เดียว พร้อม negative controls ไม่เปลี่ยนตัวละครเป็น roster', '8. Web ingress: layout_direction เป็น candidate ทุกข้อความ แม้ score ต่ำและไม่มี mismatch flag; ให้เฉพาะ decision ที่จำแนกแล้วมีผลต่อภาษา หยุดภาษาไทยถูกโยนไป EN โดย candidate ที่ไม่ผ่าน', '', '## หลักฐานก่อน/หลัง'")
s=s.replace("คู่ 2,000 มีการ rescore V2/overlay โดยไม่แก้ชุด frozen", "คู่ 2,000 มีการ rescore V2/overlay โดยไม่แก้ชุด frozen; native detector 500 เคสใช้ training corpus/threshold ต่างจาก runtime ให้ดู final_G_guard500/summary.json แยกจาก final_G_runtime_guard500_summary.json")
s=s.replace("Detector 500 เคสมี error flags บางกรณี โดยเฉพาะ repeat/combined ผล flag ไม่เท่ากับตอบผิด เพราะเว็บตั้ง repeat_policy เป็น warn_and_continue ต้องทดสอบคำตอบหลัง recovery แยก ตัวเลข detector มาจาก report guard_all_500 ไม่ใช้แทน end-to-end answer accuracy", "Native detector benchmark ตรวจ calibration 100/test 400 พร้อม disclosure ว่าไม่ใช่ untouched holdout; runtime profile ตรวจ 500 เคสด้วย published corpus/fixed thresholds บล็อกตาม policy ถูก 498/500 อีก 2 เคส mixed game title ไม่จับ layout และตอบข้อมูลเกมแทนคำถาม availability ตัวเลขนี้ไม่ใช่ answer accuracy; continued inputs 262 เคสตรวจ validation แต่ยังไม่มี content oracle ครบ")
s=s.replace("สิบคำถามพร้อมกันเคยได้ HTTP 503 ขณะงานทดสอบ API อื่นดึง WordPress อยู่", "สิบคำถามพร้อมกันมี HTTP 503 ทั้งกรณีทดสอบร่วมกับการดึง WordPress และรอบ G2 smoke ขณะ full sweep ใช้เครื่องหนัก")
s=s.replace("จึงเป็นการทดสอบร่วมที่ชนคิว", "worker เดียวมี queue wait 3 วินาที จึงต้องแยกผล under-load จาก idle")
s=s.replace("เป็นเพียงคำใบ้ในการทบทวน", "เป็นเพียงคำใบ้ในการทบทวน")
with (root/'r30_build_final_analysis.py').open('x',encoding='utf-8') as f:f.write(s)
