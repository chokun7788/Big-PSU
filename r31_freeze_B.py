import json,hashlib
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r31_report_path.txt').read_text().strip())
freeze={f.relative_to(p).as_posix():hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'app').rglob('*.py')}
with (r/'app_freeze_final_B.json').open('x',encoding='utf-8') as out:json.dump(freeze,out,indent=2)
for label,rel in [('grader_v2','tools/eval_contract_v2.py'),('r31_tests','tests/test_competition_reliability_r31.py')]:
    with (r/(label+'_final_B.sha256')).open('x',encoding='utf-8') as out:out.write(hashlib.sha256((p/rel).read_bytes()).hexdigest())
