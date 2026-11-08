import sqlite3,json,hashlib,sys
from pathlib import Path
B=Path(__file__).resolve().parent;target=B/('common_before_'+sys.argv[1]+'.sqlite')
if target.exists():raise FileExistsError(target)
with sqlite3.connect((B/'common.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(target) as dst:src.backup(dst)
(target.with_suffix('.manifest.json')).write_text(json.dumps({'path':str(target),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'reason':'Candidate backup only; production database untouched'},indent=2),encoding='utf-8')
