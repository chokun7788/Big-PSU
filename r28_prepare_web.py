from pathlib import Path
root=Path(__file__).parent
for src,dest in [('r27_start_web.ps1','r28_start_web.ps1'),('r27_web_check.py','r28_web_check.py')]:
    text=(root/src).read_text(encoding='utf-8').replace('r27_ready_','r28_ready_').replace('r27_report_path.txt','r28_report_path.txt').replace("=='2026.10.01-competition-contract-r27'","=='2026.10.01-competition-composition-r28'")
    with (root/dest).open('x',encoding='utf-8') as f:f.write(text)
report=Path((root/'r28_report_path.txt').read_text(encoding='utf-8').strip())
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
with (project/'data/eval/competition_composition_r28_280_20261001.json').open('x',encoding='utf-8') as f:f.write((report/'composition_fixture_v3.json').read_text(encoding='utf-8'))
print('Separate web helpers and versioned evaluation fixture created.')
