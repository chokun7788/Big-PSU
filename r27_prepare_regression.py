from pathlib import Path
from r27_fixture import PROJECT, REPORT
base=Path(__file__).parent
for old,new in [('r26_unit_check.py','r27_unit_check.py'),('r26_content_check.py','r27_r26_content_check.py'),('r26_web_check.py','r27_web_check.py'),('r26_start_web.ps1','r27_start_web.ps1')]:
    text=(base/old).read_text(encoding='utf-8').replace('r26_report_path.txt','r27_report_path.txt').replace("r26_ready_", "r27_ready_")
    if old=='r26_unit_check.py':text=text.replace("names=[", "names=['tests.test_competition_contract_r27_20261001',")
    if old=='r26_web_check.py':text=text.replace('2026.10.01-competition-content-speed-r26','2026.10.01-competition-contract-r27')
    with (base/new).open('x',encoding='utf-8') as f:f.write(text)
for relative in ['app/pipeline/answer_contracts.py']:
    path=REPORT/'before'/relative;path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as f:f.write((PROJECT/relative).read_bytes())
with (REPORT/'flow_initial.md').open('x',encoding='utf-8') as f:f.write((PROJECT/'docs/127_competition_contract_r27_flow_20261001.md').read_text(encoding='utf-8'))
