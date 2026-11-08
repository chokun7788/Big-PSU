from pathlib import Path
import json,hashlib
root=Path(__file__).parent;report=Path((root/'r30_report_path.txt').read_text().strip())
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
with (report/'app_freeze_C.json').open('x',encoding='utf-8') as f:json.dump({str(v.relative_to(p)):hashlib.sha256(v.read_bytes()).hexdigest() for v in (p/'app').rglob('*.py')},f,indent=2)
for old,new in [('r29_start_web.ps1','r30_start_web.ps1'),('r29_stop_owned_web.ps1','r30_stop_owned_web.ps1')]:
    path=root/new;assert not path.exists();path.write_text((root/old).read_text(encoding='utf-8').replace('r29_ready_','r30_ready_').replace('r29_report_path.txt','r30_report_path.txt'),encoding='utf-8')
print('Saved freeze and separate web launch helpers.')
