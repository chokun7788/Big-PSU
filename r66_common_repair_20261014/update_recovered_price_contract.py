from pathlib import Path
import shutil
B=Path(__file__).resolve().parent;p=B/'test_r66_reader.py';backup=B/'test_r66_reader_before_recovered_pc_source.py'
if backup.exists():raise FileExistsError(backup)
shutil.copy2(p,backup)
text=p.read_text(encoding='utf-8');old="self.assertIn('ราคายืนยัน',r.answer)";assert old in text;text=text.replace(old,"self.assertIn('70.00',r.answer)")
old="self.assertNotIn('150.00',r.answer);self.assertNotIn('140.00',r.answer);self.assertNotEqual(r.decision_artifact['response_type'],'answer')";assert old in text;text=text.replace(old,"self.assertIn('70.00',r.answer);self.assertNotIn('150.00',r.answer);self.assertNotIn('140.00',r.answer);self.assertNotEqual(r.decision_artifact['response_type'],'answer')")
p.write_text(text,encoding='utf-8')
(B/'RECOVERED_PRICE_CONTRACT_CHANGE.md').write_text('# การแก้ oracle หลังพบ source ที่ตกหล่น\n\nR66 รุ่นแรกคาดว่าไม่มีราคา PC ใน Format กลาง ซึ่งจริงเฉพาะร่าง R63 แต่ไม่ครบข้อมูลเดิมทั้งระบบ พบ app/core/source_registry.py ประกาศราคา PC เป็น user_confirmed และ app/calculator/service_fee.py มีราคาและการปัดเต็ม session อยู่แล้ว จึงกู้เป็น 6 draft rates พร้อม SHA/source snapshots ไม่ใช้ตัวเลขจากผลสอบมาเป็น facts\n\nเปลี่ยนเฉพาะ assertion ที่คาดว่าไม่มีราคา เป็นต้องมี 70.00 จาก source เดิม พร้อมยังห้ามราคา 150.00/140.00 ที่ไม่ตรงโจทย์ และยังไม่เรียกข้อมูลที่ไม่ทราบวันมีผลว่า current answer เก็บ test รุ่นก่อนและผลเก่าไว้ ไม่แก้ GT เดิม R64/R65\n',encoding='utf-8')
