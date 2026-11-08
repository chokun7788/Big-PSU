import json,hashlib
from pathlib import Path
root=Path(__file__).parent;p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path((root/'r31_report_path.txt').read_text().strip());old=Path((root/'r30_report_path.txt').read_text().strip())
for source,dest in [('r30_unit_all.py','r31_unit_all.py'),('r30_full_corpus.py','r31_full_corpus.py'),('r30_full_G.py','r31_full.py'),('r30_extra_G6.py','r31_extra.py'),('r30_smoke_all.py','r31_smoke_all.py')]:
    text=(root/source).read_text(encoding='utf-8').replace('r30_report_path.txt','r31_report_path.txt').replace('r30_full_corpus','r31_full_corpus').replace('FINAL_G6_','R31_EXTRA_')
    with (root/dest).open('x',encoding='utf-8') as out:out.write(text)
for filename in ['extra_corpus_inventory.json','focused_fixture_G6_source.json','focused_fixture_v2.json','focused_fixture_G_new_v2.json','mixed_title_fixture_G3.json','blocked36_fixture.json']:
    src=old/filename
    if src.exists():
        with (r/filename).open('xb') as out:out.write(src.read_bytes())
http=(root/'r30_http_G6.py').read_text(encoding='utf-8').replace('r30_report_path.txt','r31_report_path.txt').replace('2026.10.02-full-improvement-r30-G6','2026.10.02-question-target-content-r31').replace("'runtime':'r30-G6'","'runtime':'r31'")
http=http.replace("tasks=[","tasks=[('r31_source',json.loads((r/'focused_fixture.json').read_text(encoding='utf-8'))['cases']),",1)
http=http.replace("'source_G6'):","'source_G6','r31_source'):")
with (root/'r31_http.py').open('x',encoding='utf-8') as out:out.write(http)
with (r/'app_freeze_A.json').open('x',encoding='utf-8') as out:json.dump({f.relative_to(p).as_posix():hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'app').rglob('*.py')},out,indent=2)
print('Prepared isolated result runners and first source freeze.')
