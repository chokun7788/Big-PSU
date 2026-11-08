import json
from pathlib import Path
root=Path(__file__).parent
report=Path((root/'r28_report_path.txt').read_text(encoding='utf-8').strip())
old=Path((root/'r27_report_path.txt').read_text(encoding='utf-8').strip())
for name in ['content_contract_fixture_v2.json','new_questions_fixture_128.json']:
    with (report/name).open('x',encoding='utf-8') as f:f.write((old/name).read_text(encoding='utf-8'))
for src,dest in [('r27_fixture.py','r28_contract_fixture.py'),('r27_r26_content_check.py','r28_old80.py'),('r27_new_questions.py','r28_old128.py')]:
    text=(root/src).read_text(encoding='utf-8').replace('r27_report_path.txt','r28_report_path.txt').replace('from r27_fixture import','from r28_contract_fixture import')
    with (root/dest).open('x',encoding='utf-8') as f:f.write(text)
print('Prepared unchanged regression fixtures and separate runners.')
