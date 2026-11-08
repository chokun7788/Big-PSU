import json
from pathlib import Path
root=Path(__file__).parent;r=Path((root/'r31_report_path.txt').read_text().strip())
source=(root/'r30_idle_concurrency_G6.py').read_text(encoding='utf-8').replace('r30_report_path.txt','r31_report_path.txt').replace('2026.10.02-full-improvement-r30-G6','2026.10.02-question-target-content-r31')
with (root/'r31_idle_concurrency.py').open('x',encoding='utf-8') as out:out.write(source)
http=(root/'r31_http.py').read_text(encoding='utf-8');start=http.index('tasks=');end=http.index('counts=',start)
tasks="tasks=[('r31_source',json.loads((r/'focused_fixture.json').read_text(encoding='utf-8'))['cases']),('mixed_title8',json.loads((r/'mixed_title_fixture_G3.json').read_text(encoding='utf-8'))['cases'])]\n"
http=http[:start]+tasks+http[end:]
with (root/'r31_postrelease_http.py').open('x',encoding='utf-8') as out:out.write(http)
