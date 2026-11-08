import shutil,json,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OLD=Path((BASE/'r55_current_path.txt').read_text())/'candidate_7/PSU_Esports_Chatbot_Local'
NEW=OUT/('candidate_'+sys.argv[1])/'PSU_Esports_Chatbot_Local'
shutil.copytree(OLD,NEW,ignore=shutil.ignore_patterns('__pycache__','logs','state','*.pyc','chat_logs'))
for folder in ('app','tests','web_chat'):
    shutil.copytree(ROOT/folder,NEW/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
m=json.loads((NEW/'package_manifest.json').read_text(encoding='utf-8'));m.update(runtime_version='2026.10.10-service-r56.'+sys.argv[1],parent_runtime_version='2026.10.10-service-r55.7')
(NEW/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/('candidate_'+sys.argv[1]+'.txt')).write_text(str(NEW),encoding='utf-8');print(NEW)
