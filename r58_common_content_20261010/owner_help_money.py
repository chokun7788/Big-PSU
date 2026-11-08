from pathlib import Path
import json
OUT=Path(__file__).resolve().parent
plan=json.loads((OUT/'owner_help_latest.json').read_text(encoding='utf-8'));RUN=Path(plan['run']);stage=Path(plan['stage'])
js=(stage/'owner.js').read_text(encoding='utf-8')
js=js.replace('ราคา (กรอกเป็นสตางค์)','ราคา (บาท)')
js=js.replace('กรอกเป็นสตางค์: 35 บาท = 3500; 4,000 บาท = 400000; ใส่ 0 เฉพาะเมื่อยืนยันว่าฟรี','หน้าเว็บกรอกเป็นบาท เช่น 35 หรือ 35.50 ระบบเก็บเป็นสตางค์ให้เอง; ใส่ 0 เฉพาะเมื่อยืนยันว่าฟรี')
js=js.replace("else if(key==='weekday'&&t==='integer')",r'''else if(key==='amount_minor'&&t==='integer'){let i=node('input');i.type='text';i.inputMode='decimal';i.setAttribute('aria-label','ราคาเป็นบาท');i.placeholder='เช่น 35 หรือ 35.50';i.value=val===null||val===undefined?'':String(Math.floor(val/100))+'.'+String(val%100).padStart(2,'0');let hint=node('small','กรอกบาท ไม่ต้องคูณ 100 เอง; ทศนิยมได้ไม่เกิน 2 ตำแหน่ง');root.append(i,hint);get=()=>{let x=i.value.trim().replace(/,/g,'');if(!/^\d+(\.\d{1,2})?$/.test(x))throw Error('ราคา: กรอกจำนวนบาท เช่น 35 หรือ 35.50 (ไม่เกิน 2 ตำแหน่ง)');let [a,b='']=x.split('.'),n=Number(a)*100+Number(b.padEnd(2,'0'));if(!Number.isSafeInteger(n))throw Error('ราคาเกินขอบเขตที่ระบบรองรับ');return n;};}
 else if(key==='weekday'&&t==='integer')''')
# The monetary example needs to be readable in the same unit as the input.
js=js.replace("exampleView(h.example),node('small'", "(f.key==='amount_minor'?node('p',(h.example/100).toLocaleString('th-TH',{minimumFractionDigits:2,maximumFractionDigits:2})+' บาท — ใส่จำนวนบาทนี้ในช่องราคา'):exampleView(h.example)),node('small'")
(stage/'owner.js').write_text(js,encoding='utf-8')
for base in (OUT/'ready_package/PSU_Esports_Chatbot_Local',OUT/'system/PSU_Esports_Chatbot_Local'):
    p=base/'app/knowledge/common/ui/owner.js';role='ready' if 'ready_package' in str(base) else 'candidate'
    (RUN/(role+'_round2_owner.js')).write_bytes(p.read_bytes());p.write_text(js,encoding='utf-8')
    doc=base/'owner_content_docs/OWNER_EASY_GUIDE_TH.md'
    txt=doc.read_text(encoding='utf-8').replace('ราคาในช่องนี้เป็นสตางค์: 35 บาท → 3500, 35.50 บาท → 3550, 4,000 บาท → 400000;','หน้าเว็บช่องราคา **กรอกเป็นบาทได้เลย** เช่น 35 หรือ 35.50 ระบบแปลงเก็บเป็นสตางค์ให้อัตโนมัติ (JSON สำหรับผู้ดูแลยังเก็บ 35 บาท → 3500, 35.50 บาท → 3550, 4,000 บาท → 400000);')
    txt=txt.replace('กรอกเป็นสตางค์: 35 บาท = 3500; 4,000 บาท = 400000; ใส่ 0 เฉพาะเมื่อยืนยันว่าฟรี','หน้าเว็บกรอกบาท เช่น 35 หรือ 35.50 ระบบแปลงเป็นสตางค์ให้เอง; ใส่ 0 เฉพาะเมื่อยืนยันว่าฟรี (ตัวอย่าง JSON ด้านล่างเป็นหน่วยสตางค์)')
    doc.write_text(txt,encoding='utf-8')
(RUN/'OWNER_EASY_GUIDE_TH.md').write_text(txt,encoding='utf-8')
print('Owner price input now accepts baht; persisted integer minor-unit schema unchanged.')
