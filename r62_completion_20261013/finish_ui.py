from pathlib import Path
R=Path(__file__).resolve().parent.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
p=R/'app/knowledge/common/ui/owner.js';s=p.read_text(encoding='utf-8')
old="async function task(fn){document.querySelectorAll('button').forEach(b=>b.disabled=true);try{await fn();}catch(e){message(userError(e.message),true);}finally{document.querySelectorAll('button').forEach(b=>b.disabled=false);}}"
new="async function task(fn){let controls=Array.from(document.querySelectorAll('button,input,select,textarea')).map(e=>[e,e.disabled]);controls.forEach(([e])=>e.disabled=true);try{await fn();}catch(e){message(userError(e.message),true);}finally{controls.forEach(([e,was])=>{if(e.isConnected)e.disabled=was;});}}"
assert old in s;s=s.replace(old,new,1);p.write_text(s,encoding='utf-8')
p=R/'PRODUCTION_OPERATION_TH.md';s=p.read_text(encoding='utf-8')
s=s.replace('3. ดับเบิลคลิก Open-Owner-Content.cmd', '3. ถ้าเป็นแบบ Download Models ให้เปิด Setup-Local-Models.cmd ให้จบก่อนเปิดแชทหรือหน้าผู้ดูแล\n4. ดับเบิลคลิก Open-Owner-Content.cmd',1)
s+='\n## อังกฤษสำหรับข้อมูลใหม่\n\nกรอกไทย → กดช่วยแปลไทยเป็นอังกฤษ (ร่าง) → ตรวจคำแปล → บันทึก → อนุมัติ → เผยแพร่ ปุ่มนี้แปลเฉพาะช่องข้อความไทย/อังกฤษตาม schema และไม่บันทึกเอง ตัวเลข วันที่ ลิงก์ และรหัสไม่ได้ให้โมเดลเปลี่ยน หากยังไม่ได้ตรวจความหมาย คงสถานะแปลโดยระบบ ไม่ใช้ผลทดสอบภาษาอังกฤษเดิมเป็นการรับรองข้อความใหม่ทุกฉบับ\n\n## ตารางจองต้นทางกับข้อมูลกลาง\n\nการแก้ราคา เวลา หรือวันปิดในฐานความรู้ ไม่ใช่การเขียนแก้ WordPress หรือยกเลิกการจองของลูกค้า เมื่อเปลี่ยนการให้บริการจริง เจ้าของต้องปรับระบบจองต้นทางให้ตรงกันด้วย ส่วน live_binding ในฟอร์มเป็นข้อมูลการเชื่อม ไม่ได้สร้าง adapter สำหรับ API ใหม่อัตโนมัติ แพ็กเกจนี้ยังไม่ได้รับรองการซิงก์ตารางกลางที่แก้ใหม่เข้ากับทุกหน้า WordPress\n'
p.write_text(s,encoding='utf-8')
