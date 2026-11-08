"""Create an isolated repair candidate with a consistent source DB backup."""
import hashlib,json,shutil,sqlite3,time
from pathlib import Path
B=Path(__file__).resolve().parent
P=B/'r130_owner_context_completion_20261025'
R=B/'r132_flow_repairs_20261025'
assert not R.exists(),'Do not overwrite a repair candidate'
R.mkdir()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
freeze=json.loads((P/'EXECUTION_FREEZE_R130.json').read_text('utf8'))
changed=[p for p,h in freeze.items() if sha(p)!=h]
assert not changed,changed
shutil.copytree(P/'system',R/'system',ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm','common.sqlite'))
with sqlite3.connect((P/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as source:
 with sqlite3.connect(R/'system/data/knowledge/common.sqlite') as target:source.backup(target)
shutil.copytree(P/'spec',R/'spec')
for name in ['REQUIREMENTS_TRACEABILITY.json','REQUIREMENTS.json','FULL_JOBS.jsonl']:
 if (P/name).exists():shutil.copy2(P/name,R/('PARENT_'+name))
status={'phase':'implement_proven_flow_repairs','complete':False,'parent_candidate':str(P),'source_data_changes':0,'weights_changed':False,'production_installed':False,'user_authorization':'Proceed autonomously with proven improvements and complete all Flow requirements; no repeated permission requests','requirements_scope':76,'categories_scope':14,'created_at':time.time()}
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),'utf8')
(R/'PARENT_FREEZE.json').write_text(json.dumps(freeze,indent=2),'utf8')
(R/'SOURCE_DATABASE_LINEAGE.json').write_text(json.dumps({'method':'SQLite read-only backup including committed WAL contents','source':str(P/'system/data/knowledge/common.sqlite'),'target':str(R/'system/data/knowledge/common.sqlite'),'source_logical_digest':json.loads((P/'SOURCE_SNAPSHOT_BEFORE.json').read_text('utf8'))['sha256'],'records_and_approvals_not_edited':True},indent=2),'utf8')
print(json.dumps({'candidate':str(R),'parent_frozen_files_verified':len(freeze),'source_consistent_backup':True}))
