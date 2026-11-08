import hashlib,json,shutil,uuid
from pathlib import Path
BASE=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=BASE/('r49_service_dialogue_20261008_'+uuid.uuid4().hex[:8]);OUT.mkdir()
(BASE/'r49_current_path.txt').write_text(str(OUT))
manifest={}
for folder in ('app','tests','data/curated','data/rules','web_chat'):
 for p in (ROOT/folder).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:
   rel=p.relative_to(ROOT);dest=OUT/'before'/rel;dest.parent.mkdir(parents=True,exist_ok=True)
   shutil.copy2(p,dest);manifest[rel.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
with (OUT/'before_manifest.json').open('x') as f:json.dump(manifest,f,indent=2)
print(OUT)
