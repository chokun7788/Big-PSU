from pathlib import Path
import json,shutil
from package_r62 import B,SYSTEM,OUT,tree
for root in OUT.iterdir():
 if not root.is_dir():continue
 tree(SYSTEM/'app',root/'app');tree(SYSTEM/'web_chat',root/'web_chat');tree(SYSTEM/'docs',root/'docs')
 for p in SYSTEM.iterdir():
  if p.is_file() and (p.suffix in {'.ps1','.cmd','.md'} or p.name=='Model-Manifest-Check.py'):shutil.copy2(p,root/p.name)
 for ext in ['.md','.json']:shutil.copy2(B.parent/('r61_implementation_20261013/OWNER_REVIEW_PACKET'+ext),root/('OWNER_REVIEW_PENDING'+ext))
 (root/'README_TH.md').write_text('# PSU Esports Chatbot r62\n\nอ่าน START_HERE_TH.md ของโฟลเดอร์นี้ก่อน จากนั้น PRODUCTION_OPERATION_TH.md และ OWNER_CONTENT_GUIDE_TH.md\n\nแบบ With Models รวมโมเดลแล้ว แบบ Download Models ให้เปิด Setup-Local-Models.cmd ให้เสร็จก่อนเปิดแชท\n\nเปิดแชท: Open-PSU-Esports-Background.cmd\nเปิดเพิ่ม/แก้ข้อมูล: Open-Owner-Content.cmd\n\nชุดนี้ใช้ Windows 64-bit ในเครื่องที่รัน การเปิดเว็บสาธารณะยังต้องจัดโฮสต์และสิทธิ์ผู้ดูแล ดูขอบเขตและผลทดสอบใน docs/common_content_r62_20261013/RESULTS_TH.md\n\nไม่รวมข้อมูลทดลองและประวัติแชทของเครื่องพัฒนา ไม่อนุมัติร่างข้อเท็จจริงแทนเจ้าของ\n',encoding='utf-8')
 p=root/'START_HERE_TH.md';s=p.read_text(encoding='utf-8')
 s=s.replace('2. เปิด Open-PSU-Esports-Background.cmd แล้วรอระบบตรวจความพร้อมก่อนเปิดเว็บ\n3. แบบ With_Models มีโมเดลแล้ว แบบ Download_Models ต้องเปิด Setup-Local-Models.cmd พร้อมอินเทอร์เน็ตครั้งแรก',
 '2. ถ้าเลือก Download_Models เปิด Setup-Local-Models.cmd พร้อมอินเทอร์เน็ตให้เสร็จก่อน (ดาวน์โหลดครั้งแรก)\n3. เปิด Open-PSU-Esports-Background.cmd แล้วรอระบบตรวจความพร้อมก่อนเปิดเว็บ; With_Models มีโมเดลพร้อมแล้ว')
 s+='\nแนะนำให้แตกไปที่โฟลเดอร์สั้น เช่น Downloads/PSU_Chatbot และเลือกใช้งานเพียงหนึ่งแบบบนเครื่องเดียวกัน\n'
 p.write_text(s,encoding='utf-8')
 # Transferable folders get the relative Python binding, never developer paths.
 m=json.loads((root/'package_manifest.json').read_text(encoding='utf-8'));m['latest_verification']='r62_completion_20261013/FINAL_VERIFICATION.json';m['local_runtime_features']+=['schema_scoped_unnamed_faq_selection','draft_only_schema_context_translation','related_model_and_procedure_reads','regular_rental_budget_separation']
 (root/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
print('Final application, guides and owner review packet included in both variants.')
