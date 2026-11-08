import json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;OLD=Path((BASE/'r56_current_path.txt').read_text());OUT=Path((BASE/'r57_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');CAND=OUT/'candidate_1/PSU_Esports_Chatbot_Local';VERSION='2026.10.10-service-r57.1'
old=Path((OLD/'candidate_7.txt').read_text());shutil.copytree(old,CAND,ignore=shutil.ignore_patterns('__pycache__','logs','state','*.pyc','chat_logs'))
for folder in ('app','tests','web_chat'):shutil.copytree(ROOT/folder,CAND/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
p=CAND/'package_manifest.json';m=json.loads(p.read_text());m['runtime_version']=VERSION;m['parent_runtime_version']='2026.10.10-service-r56.7';p.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8');(OUT/'candidate_1.txt').write_text(str(CAND))
for name in ('r56_units.py','r56_targeted_web.py','r56_web_all.py'):
 s=(BASE/name).read_text(encoding='utf-8').replace('r56_current_path.txt','r57_current_path.txt').replace("('2026.10.10-service-r55.','2026.10.10-service-r56.')","('2026.10.10-service-r57.',)")
 s=s.replace("startswith('2026.10.10-service-r56.')","startswith('2026.10.10-service-r57.')")
 (BASE/name.replace('r56_','r57_')).write_text(s,encoding='utf-8')
shutil.copy2(OLD/'answer_contracts_v2.json',OUT/'answer_contracts_v2.json')
# Preserve r56 launcher corrections and historical reports in the newly made packages.
READY=BASE.parents[1]/'PSU_Esports_Share_R56_20261010'
for variant in ('01_Download_Models','02_With_Models'):
 d=READY/variant;app=d/'system/PSU_Esports_Chatbot_Local'
 for name in ('app/pipeline/engine.py','app/pipeline/experimental_fallback.py'):
  target=app/name;backup=OUT/'package_before'/variant/name;backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(target,backup);shutil.copy2(ROOT/name,target)
 for name in (d/'ready_manifest.json',app/'package_manifest.json'):
  m=json.loads(name.read_text(encoding='utf-8'));m['runtime_version']=VERSION;m['source_revision']='r57.1';name.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
 p=d/'README_R56_TH.md';t=p.read_text(encoding='utf-8');shutil.copy2(p,OUT/(variant+'_README_before.md'));t=t.replace('2026.10.10-service-r56.7',VERSION).replace('# PSU Esports Chatbot r56','# PSU Esports Chatbot r57').replace('`R56_REVISION7_CHECKS.json`','`R57_SCOPE_CHECKS.json`');t+='\nขอบเขตรุ่น r57: ตอบเฉพาะข้อมูลศูนย์ที่มี ไม่ตอบคำถามชีวิตประจำวันหรือสร้างบทความทั่วไป แม้ข้อความจะมีคำว่าเกม\n';p.write_text(t,encoding='utf-8')
print(CAND)
