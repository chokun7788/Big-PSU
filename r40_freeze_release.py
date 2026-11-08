import json, shutil, hashlib, sys
from datetime import datetime, timezone
from pathlib import Path
BASE=Path(__file__).resolve().parent
OUT=Path((BASE/'r40_current_path.txt').read_text(encoding='utf-8'))
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OLD=BASE/'two_turn_choices_20261005_000041/release_r39_3/PSU_Esports_Chatbot_Local'
minor=int(sys.argv[1]) if len(sys.argv)>1 else 1
NEW=OUT/f'release_r40_{minor}/PSU_Esports_Chatbot_Local'
assert not NEW.exists(), 'Never replace an existing release.'
shutil.copytree(OLD,NEW,ignore=shutil.ignore_patterns('logs','__pycache__','.git','*.pyc'))
for folder in ('app','web_chat'):
    shutil.copytree(ROOT/folder,NEW/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
for name in ('Open-PSU-Esports-Background.ps1','Start-PSU-Esports-Chatbot.ps1','README_TH.md','LOCAL_OPERATION_AND_DATA_POLICY_TH.md'):
    shutil.copy2(ROOT/'deployment_templates'/name,NEW/name)
manifest=json.loads((NEW/'package_manifest.json').read_text(encoding='utf-8-sig'))
manifest.update(runtime_version=f'2026.10.06-targeted-flow-r40.{minor}',built_at=datetime.now(timezone.utc).isoformat(),
                release_scope='Targeted dialogue fixes; local-machine test release. Model weights excluded.',
                parent_runtime_version='2026.10.06-two-turn-r39.3')
manifest['local_runtime_features']+=['typed_multi_target_dialogue_selection','roman_edition_guard','per_child_named_game_guard']
(NEW/'package_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
hashes={p.relative_to(NEW).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in NEW.rglob('*') if p.is_file()}
with (OUT/f'release_r40_{minor}_hashes.json').open('x',encoding='utf-8') as f:json.dump(hashes,f,indent=2)
with (OUT/('release_path.txt' if minor==1 else f'release_r40_{minor}_path.txt')).open('x',encoding='utf-8') as f:f.write(str(NEW))
print(str(NEW), len(hashes), sum(p.stat().st_size for p in NEW.rglob('*') if p.is_file()))
