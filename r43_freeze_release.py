import json,shutil,hashlib,sys
from datetime import datetime,timezone
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r43_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OLD=Path((BASE/'r42_current_path.txt').read_text())/'release_r42_4/PSU_Esports_Chatbot_Local'
minor=sys.argv[1] if len(sys.argv)>1 else '1'
NEW=OUT/f'release_r43_{minor}/PSU_Esports_Chatbot_Local'
assert not NEW.exists()
shutil.copytree(OLD,NEW,ignore=shutil.ignore_patterns('logs','__pycache__','.git','*.pyc'))
for folder in ('app','web_chat'):shutil.copytree(ROOT/folder,NEW/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
names=('Runtime-Readiness.ps1','Open-PSU-Esports-Background.ps1','Open-PSU-Esports-Chatbot.ps1','Start-PSU-Esports-Chatbot.ps1','README_TH.md')
for name in names:shutil.copy2(ROOT/'deployment_templates'/name,NEW/name)
manifest=json.loads((NEW/'package_manifest.json').read_text(encoding='utf-8-sig'))
manifest.update(runtime_version=f'2026.10.06-readiness-schedule-r43.{minor}',built_at=datetime.now(timezone.utc).isoformat(),parent_runtime_version='2026.10.06-domain-resume-r42.4',release_scope='Local machine candidate; explicit verified Python binding; existing Ollama models, no bundled model weights.',python_runtime=dict(path=r'C:\Users\Chokhun\Documents\Codex\PSU Esports Chatbot Ready 20261003\runtime\python\python.exe',scope='local-machine'))
manifest['local_runtime_features']+=['verified_interpreter_chain','startup_answer_oracle','complete_english_regular_week']
(NEW/'package_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (OUT/f'release_r43_{minor}_path.txt').open('x',encoding='utf-8') as f:f.write(str(NEW))
with (OUT/f'release_r43_{minor}_hashes.json').open('x',encoding='utf-8') as f:json.dump({p.relative_to(NEW).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in NEW.rglob('*') if p.is_file()},f,indent=2)
print(NEW)
