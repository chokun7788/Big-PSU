"""Create a new audit candidate without changing R67 or the actual project."""
import hashlib,json,shutil,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent
S=B/'r67_migration_parity_20261015'
O=B/'r68_source_completion_20261016'
R=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
O.mkdir(exist_ok=False)
shutil.copytree(S/'system',O/'system',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
for n in ['harness.py','migrate_ids.py']:
 shutil.copy2(S/n,O/n)
for n in ['before.sqlite','common.sqlite']:
 with sqlite3.connect((S/'common.sqlite').as_uri()+'?mode=ro',uri=True) as c,sqlite3.connect(O/n) as d:c.backup(d)
paths={x['path'] for x in json.loads((S/'SOURCE_MANIFEST.json').read_text('utf8'))}
# Include all source/business files, including source text missed by earlier lists.
for folder in ['curated','rules','content','sources','competition_rules','calendar']:
 paths.update(p.relative_to(R).as_posix() for p in (R/'data'/folder).rglob('*') if p.is_file())
manifest=[]
for rel in sorted(paths):
 p=R/rel
 if not p.is_file():continue
 data=p.read_bytes();t=O/'source_snapshot'/rel;t.parent.mkdir(parents=True,exist_ok=True);t.write_bytes(data)
 manifest.append({'path':rel,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
(O/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'workspace':str(O),'snapshot_files':len(manifest),'extra_files':len(set(x['path'] for x in manifest)-set(x['path'] for x in json.loads((S/'SOURCE_MANIFEST.json').read_text('utf8'))))}))
