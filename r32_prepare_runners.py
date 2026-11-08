from pathlib import Path
import json,shutil
ROOT=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path((ROOT/'r32_report_path.txt').read_text().strip());OLD=Path((ROOT/'r31_report_path.txt').read_text().strip())
for name in ['r31_full_corpus.py','r31_full.py','r31_extra.py','r31_smoke_all.py','r31_http_B.py','r31_idle_concurrency.py','r31_start_web.ps1','r31_stop_owned_web.ps1']:
 s=(ROOT/name).read_text(encoding='utf-8-sig').replace('r31_report_path.txt','r32_report_path.txt').replace('r31_full_corpus','r32_full_corpus').replace('r31_ready_','r32_ready_').replace('2026.10.02-question-target-content-r31','2026.10.02-source-content-reliability-r32')
 if name=='r31_extra.py':s=s.replace('R31_EXTRA_EXTRA','R32_EXTRA')
 with (ROOT/name.replace('r31_','r32_')).open('x',encoding='utf-8') as out:out.write(s)
for name in ['extra_corpus_inventory.json','compound_pause_fixture_B.json','focused_fixture.json','focused_fixture_G6_source.json','focused_fixture_v2.json','focused_fixture_G_new_v2.json','mixed_title_fixture_G3.json']:
 shutil.copy2(OLD/name,R/name)
print('isolated r32 runners ready, historical fixtures copied unchanged')
