from pathlib import Path
import hashlib,json,shutil
B=Path(__file__).resolve().parent
roots={'candidate':B.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local','project':Path('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data'),'package':B.parent/'r58_common_content_20261010/ready_package/PSU_Esports_Chatbot_Local'}
extra={k:{} for k in roots}
for label,root in roots.items():
 p=root/'OWNER_CONTENT_GUIDE_TH.md'
 if p.exists():
  dst=B/'before'/label/p.name;dst.parent.mkdir(parents=True,exist_ok=True)
  if dst.exists():raise RuntimeError('Already backed up guide')
  shutil.copy2(p,dst);extra[label][p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'EXTRA2_BEFORE.json').write_text(json.dumps(extra,indent=2),encoding='utf-8')
p=roots['candidate']/'OWNER_CONTENT_GUIDE_TH.md';s=p.read_text(encoding='utf-8')
s=s.replace('ชุดกรอกข้อมูลกลางและแชท r58','ชุดกรอกข้อมูลกลางและแชท r62',1)
old='เครื่องนี้มี Ollama และโมเดลเดิมอยู่แล้ว ชุดนี้แนบ Python 3.12 x64 และ validator ไว้ ไม่ต้องติดตั้ง pip สำหรับแบบฟอร์ม ข้อมูลโมเดล Ollama ไม่ถูกคัดลอกเพิ่ม การเอาไปเครื่องอื่นยังต้องมี Ollama และดาวน์โหลดโมเดลผ่าน Setup-Local-Models.cmd ไม่ใช่แพ็กเกจแนบโมเดลทั้งหมด'
new='แพ็กเกจส่งต่อ r62 ทั้งสองแบบรวม Python 3.12 x64, validator และตัวรัน Ollama แล้ว แบบ With Models รวมโมเดลที่ตรวจไว้ด้วย แบบ Download Models ดาวน์โหลดครั้งแรกผ่าน Setup-Local-Models.cmd แต่ละแพ็กเกจใช้คลังโมเดลของตนเอง ไม่ต้องติดตั้ง pip หรือ Ollama แยก อ่าน START_HERE_TH.md และ PRODUCTION_OPERATION_TH.md ของชุดที่เลือกใช้ ชุด source ในโปรเจกต์เดิมยังใช้การติดตั้ง Ollama เดิมได้'
assert old in s;s=s.replace(old,new)
s=s.replace('ทดสอบ “<ชื่อเกม>', 'เลือกทดสอบร่างสำหรับข้อมูลที่บันทึกแต่ยังไม่เผยแพร่ หรือทดสอบฉบับเผยแพร่ตามปกติ: “<ชื่อเกม>',1)
p.write_text(s,encoding='utf-8')
