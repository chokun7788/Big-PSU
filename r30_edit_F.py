from pathlib import Path
import json,hashlib
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip())
for rel,old,new in [
('app/pipeline/question_frame.py','"ราคา", "กี่บาท", "ค่าบริการ", "คิดเงิน", "คำนวณ", "เสียเงิน", "จ่ายเท่า"','"ราคา", "กี่บาท", "ค่าบริการ", "ค่าเล่น", "คิดเงิน", "คำนวณ", "เสียเงิน", "จ่ายเท่า"'),
('app/core/normalization.py','"ราคา", "ค่าบริการ", "เสียกี่บาท", "กี่บาท", "เท่าไหร่"','"ราคา", "ค่าบริการ", "ค่าเล่น", "เสียกี่บาท", "กี่บาท", "เท่าไหร่"')]:
    f=p/rel;s=f.read_text(encoding='utf-8');assert s.count(old)==1
    dest=r/'before_F'/rel;dest.parent.mkdir(parents=True,exist_ok=True);assert not dest.exists();dest.write_bytes(f.read_bytes());f.write_text(s.replace(old,new),encoding='utf-8')
with (r/'app_freeze_F.json').open('x',encoding='utf-8') as f:json.dump({str(v.relative_to(p)):hashlib.sha256(v.read_bytes()).hexdigest() for v in (p/'app').rglob('*.py')},f,indent=2)
print('Recognize the established Thai fee phrase in routing and answer contract.')
