import json, hashlib, shutil
from pathlib import Path
OUT=Path(__file__).resolve().parent
BASE=OUT.parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OLD=BASE/'r57_studio_scope_20261010_174001/candidate_4/PSU_Esports_Chatbot_Local'
CAND=OUT/'system/PSU_Esports_Chatbot_Local'
RESEARCH=BASE/'canonical_format_research_20261010_180226'
if CAND.exists(): raise SystemExit('refuse to overwrite candidate')
shutil.copytree(OLD,CAND,ignore=shutil.ignore_patterns('__pycache__','*.pyc','logs','state','chat_logs'))
for name in ('app','tests','web_chat','tools'):
    shutil.copytree(ROOT/name,CAND/name,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
before={}
for folder in ('app','tests','web_chat','tools','data','booking_dashboard'):
    for p in (ROOT/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and not any(x in p.parts for x in ('logs','chat_logs','ground_truth','vector','eval','state')):
            before[p.relative_to(ROOT).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'source_hashes_before.json').write_text(json.dumps(before,indent=2),encoding='utf-8')
dst=CAND/'app/knowledge/common'
dst.mkdir()
(dst/'__init__.py').write_text('',encoding='utf-8')
shutil.copytree(OUT/'vendor',CAND/'app/knowledge/common/vendor',ignore=shutil.ignore_patterns('__pycache__','*.pyc','bin'))
shutil.copytree(RESEARCH/'schemas',dst/'schemas')
shutil.copytree(RESEARCH/'templates',dst/'templates')
catalog=json.loads((RESEARCH/'FIELD_CATALOG.json').read_text(encoding='utf-8'))
(dst/'catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2),encoding='utf-8')
for p in (dst/'schemas').glob('*.json'):
    s=p.read_text(encoding='utf-8').replace('studio-content-3.0-design','studio-content-3.0')
    p.write_text(s,encoding='utf-8')
for p in (dst/'templates').glob('*.json'):
    s=p.read_text(encoding='utf-8').replace('studio-content-3.0-design','studio-content-3.0')
    p.write_text(s,encoding='utf-8')
backup=OUT/'before/app/pipeline';backup.mkdir(parents=True)
shutil.copy2(ROOT/'app/pipeline/engine.py',backup/'engine.py')
m=json.loads((CAND/'package_manifest.json').read_text(encoding='utf-8'))
m['parent_runtime_version']=m.get('runtime_version');m['runtime_version']='2026.10.10-common-r58.1'
(CAND/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'candidate_path.txt').write_text(str(CAND),encoding='utf-8')
print(CAND)
