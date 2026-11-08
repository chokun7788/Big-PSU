import sqlite3,json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent
status=json.loads((B/'FINAL_final07/STATUS.json').read_text(encoding='utf-8'));assert status.get('complete') and status.get('code_unchanged')
backup=B/'common_before_pc_recovery.sqlite'
if backup.exists():raise FileExistsError(backup)
with sqlite3.connect((B/'common.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(backup) as dst:src.backup(dst)
with sqlite3.connect((B/'common_pc_candidate.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(B/'common.sqlite') as dst:src.backup(dst)
(B/'PC_CANDIDATE_SWITCH.json').write_text(json.dumps({'previous_candidate_backup':str(backup),'previous_sha256':hashlib.sha256(backup.read_bytes()).hexdigest(),'new_candidate_sha256':hashlib.sha256((B/'common.sqlite').read_bytes()).hexdigest(),'production_database_modified':False},indent=2),encoding='utf-8')
