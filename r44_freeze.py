import json,shutil,hashlib,sys
from pathlib import Path
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r44_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
old=Path((BASE/'r43_current_path.txt').read_text())/'release_r43_3/PSU_Esports_Chatbot_Local'
minor=sys.argv[1] if len(sys.argv)>1 else '1'
new=OUT/f'release_r44_{minor}/PSU_Esports_Chatbot_Local';assert not new.exists()
shutil.copytree(old,new,ignore=shutil.ignore_patterns('logs','__pycache__','.git','*.pyc'))
for folder in ('app','web_chat'):shutil.copytree(ROOT/folder,new/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
for rel in ('data/curated/zone_rental_fees_20261006.json','data/sources/zone_rental_fees_20261006.xlsx'):
    dest=new/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/rel,dest)
m=json.loads((new/'package_manifest.json').read_text(encoding='utf-8-sig'))
m.update(runtime_version=f'2026.10.06-zone-rental-r44.{minor}',built_at=datetime.now(timezone.utc).isoformat(),parent_runtime_version='2026.10.06-readiness-schedule-r43.3')
m['local_runtime_features']+=['user_workbook_zone_rental','24_cell_bound_rental_rates','organization_rental_dialogue']
(new/'package_manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (OUT/f'release_r44_{minor}_path.txt').open('x',encoding='utf-8') as f:f.write(str(new))
with (OUT/f'release_r44_{minor}_hashes.json').open('x',encoding='utf-8') as f:json.dump({p.relative_to(new).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in new.rglob('*') if p.is_file()},f,indent=2)
print(new)
