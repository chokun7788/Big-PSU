"""Create an isolated migration workspace; never mutate an earlier run or production."""
import hashlib,json,shutil,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent
O=B/'r67_migration_parity_20261015'
R=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
O.mkdir(exist_ok=False)
shutil.copytree(B/'r66_common_repair_20261014/system',O/'system',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
for name in ['harness.py']:
 shutil.copy2(B/'r66_common_repair_20261014'/name,O/name)
src=B/'r66_common_repair_20261014/common.sqlite'
for name in ['before.sqlite','common.sqlite']:
 with sqlite3.connect(src.as_uri()+'?mode=ro',uri=True) as c,sqlite3.connect(O/name) as d:c.backup(d)
manifest=[]
paths={x['path'] for x in json.loads((B/'r66_common_repair_20261014/SOURCE_MANIFEST.json').read_text('utf8'))}
paths.update(p.relative_to(R).as_posix() for p in (R/'data/content').rglob('*.json'))
# Snapshot source inputs used by the first importer, not merely canonical exports.
paths.update(x['path'] for x in json.loads((B/'r63_legacy_migration_20261013/round7/SOURCE_MANIFEST.json').read_text('utf8')))
for rel in sorted(paths):
 p=R/rel
 if not p.is_file():continue
 data=p.read_bytes();t=O/'source_snapshot'/rel;t.parent.mkdir(parents=True,exist_ok=True);t.write_bytes(data)
 manifest.append({'path':rel,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
(O/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'workspace':str(O),'snapshot_files':len(manifest)},ensure_ascii=False))
