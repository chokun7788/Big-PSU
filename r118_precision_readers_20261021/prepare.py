import hashlib,json,shutil,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent; OLD=R.parent/'r117_context_understanding_20261021'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protected={str(p.resolve()):sha(p) for p in (OLD/'system').rglob('*') if p.is_file() and p.suffix not in {'.pyc','.pyo'} and not p.name.endswith(('-wal','-shm'))}
for folder in ['full01','http02','http03','http04']:
 for name in ['RESULTS.jsonl','TEST_COMPLETE.json']:
  p=OLD/folder/name
  if p.exists():protected[str(p.resolve())]=sha(p)
(R/'REFERENCE_HASHES.json').write_text(json.dumps(protected,indent=2),'utf8')
shutil.copytree('\\\\?\\'+str((OLD/'system').resolve()),'\\\\?\\'+str((R/'system').resolve()),ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.pyo','*-wal','*-shm','owner-session.json'))
db=R/'system/data/knowledge/common.sqlite'
with sqlite3.connect((OLD/'system/data/knowledge/common.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(db) as dst:src.backup(dst)
for name in ['serve_frozen.py','evaluation.py','reference_grader.py','retained_literal.py','BASELINE_CHECK_V2.json','BASELINE_SCORED_V2.jsonl','SELECTED_JOBS.jsonl','SELECTION_MANIFEST.json','SAMPLE_ALLOCATION.json','SAVED_R115_RESULTS.jsonl','verify_understanding.py','analyze.py']:
 p=OLD/name
 if p.exists():shutil.copy2(p,R/name)
script=(OLD/'run_http03.py').read_text('utf8').replace("OUT=R/'http03'","OUT=R/'http01'").replace('R117','R118').replace('r117','r118')
# Freeze only actual runner inputs carried into this candidate.
script=script.replace("'run_http02.py','run_http03.py','run_http04.py','SELECTED_JOBS_04.jsonl','SELECTION_MANIFEST_04.json',",'')
script=script.replace("'run_http.py','run_http02.py','run_http03.py',","'run_http.py',")
(R/'run_http.py').write_text(script,'utf8')
print(json.dumps({'protected_files':len(protected),'system_files':sum(p.is_file() for p in (R/'system').rglob('*'))}))
