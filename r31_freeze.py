import json,hashlib
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r31_report_path.txt').read_text().strip())
with (r/'app_freeze_final_A.json').open('x',encoding='utf-8') as out:json.dump({f.relative_to(p).as_posix():hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'app').rglob('*.py')},out,indent=2)
print('Final A application frozen for complete regression and package parity.')
