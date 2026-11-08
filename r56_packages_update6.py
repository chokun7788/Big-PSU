import json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');READY=BASE.parents[1]/'PSU_Esports_Share_R56_20261010';records=[]
for variant in ('01_Download_Models','02_With_Models'):
 d=READY/variant;app=d/'system/PSU_Esports_Chatbot_Local'
 for folder in ('app','web_chat'):
  shutil.copytree(ROOT/folder,app/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
 for p in (d/'ready_manifest.json',app/'package_manifest.json'):
  m=json.loads(p.read_text(encoding='utf-8'));m.update(runtime_version='2026.10.10-service-r56.6',source_revision='r56.6');p.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
 p=d/'README_R56_TH.md';t=p.read_text(encoding='utf-8').replace('2026.10.10-service-r56.5','2026.10.10-service-r56.6').replace('`R56_BUILD_CHECKS.json`','`R56_REVISION6_CHECKS.json`');p.write_text(t,encoding='utf-8')
 records.append(dict(variant=variant,runtime='2026.10.10-service-r56.6',copied=['app','web_chat'],original_r50_unchanged=True,previous_build_checks_kept=True))
 (d/'R56_REVISION6_CHECKS.json').write_text(json.dumps(records[-1],indent=2),encoding='utf-8')
with (OUT/'package_revision6.json').open('x',encoding='utf-8') as f:json.dump(records,f,indent=2)
print('updated new packages only; old packages intact')
