import json, hashlib, shutil, subprocess, datetime, uuid
from pathlib import Path
W=Path(__file__).parent
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
R=P/'reports'/('r35_conversation_context_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]);R.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=Path((W/'r34_report_path.txt').read_text().strip())
protected=json.loads((old/'protected_manifest.json').read_text())
assert all(sha(P/k)==v for k,v in protected.items())
manifest={}
for folder in ('app','tests','tools','web_chat','deployment_templates'):
 for f in (P/folder).rglob('*'):
  if not f.is_file() or '__pycache__' in f.parts or f.suffix=='.pyc':continue
  k=f.relative_to(P).as_posix();manifest[k]=sha(f);dest=R/'before'/k;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(f,dest)
for name,data in [('before_manifest.json',manifest),('protected_manifest.json',protected)]:
 with (R/name).open('x',encoding='utf-8') as out:json.dump(data,out,indent=2)
with (R/'git_status_before.txt').open('x',encoding='utf-8') as out:out.write(subprocess.run(['git','status','--short'],cwd=P,capture_output=True,text=True,encoding='utf-8').stdout)
with (W/'r35_report_path.txt').open('x',encoding='utf-8') as out:out.write(str(R))
for name in ('r34_unit_all.py','r34_start_web.ps1','r34_stop_owned_web.ps1'):
 with (W/name.replace('r34','r35')).open('x',encoding='utf-8') as out:out.write((W/name).read_text(encoding='utf-8').replace('r34','r35'))
with (R/'FLOW_INITIAL_TH.md').open('x',encoding='utf-8') as out:out.write('''# Flow r35 — ประวัติคำถามต่อเนื่อง
1. เก็บบทสนทนาจริงและ debug; ตรวจเว็บส่ง history และ server ได้รับกี่ข้อความ
2. ทำ baseline ลำดับเดิมกับ HTTP และ context resolver โดยไม่ดึงสถานะจองจริง
3. รองรับคำตอบชื่อเกมหลังคำถามชี้แจงกติกา โดยรักษาคำถาม/หัวข้อ/ปีเดิม ไม่เปลี่ยนเป็นข้อมูลเกมทั่วไป
4. คำถามกติกาที่ไม่มีชื่อเกมใช้เป้าหมายชัดเจนจากคู่บทสนทนาล่าสุดเท่านั้น ไม่เลือกจากรายการตัวอย่างของบอท
5. ทดสอบไทย/อังกฤษ คำผิดชื่อเกมที่ตัวตรวจเดิมรองรับ เปลี่ยนเรื่อง หลายชื่อ ไม่มี history และข้อมูลเก่า
6. รัน regression ของบริบทและ unit เดิม สร้าง package ใหม่ ทดสอบ HTTP และ UI ก่อนเปิดตัวแก้ที่8090
7. แยกการผ่านอัตโนมัติจากการยืนยันนโยบายโดยเจ้าของ เก็บ code/log/Gold เดิมทั้งหมด
''')
print(json.dumps({'report':str(R),'snapshots':len(manifest),'protected':len(protected)},ensure_ascii=False))
