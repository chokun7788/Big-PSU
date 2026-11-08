"""Isolate the retained R114 candidate and freeze the existing 1,400 questions."""
import hashlib,json,shutil,sqlite3,os
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;source=B/'r114_domain_flow_integration_20261021'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ext(p):return '\\\\?\\'+str(p.resolve()) if os.name=='nt' else str(p)
if (R/'system').exists():raise SystemExit('Refusing to overwrite an existing candidate')
files=[p for p in (source/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.log'} and not p.name.endswith(('-wal','-shm'))]
before={str(p.resolve()):sha(p) for p in files}
shutil.copytree(ext(source/'system'),ext(R/'system'),ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.sqlite-wal','*.sqlite-shm','owner-session.json'))
db=R/'system/data/knowledge/common.sqlite'
with sqlite3.connect((source/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as a,sqlite3.connect(db) as b:a.backup(b)
q=B/'r113_multi_flow_benchmark_20261021/EFFECTIVE_QUESTIONS_1400.jsonl'
(R/'EXISTING_QUESTIONS_1400.jsonl').write_bytes(q.read_bytes())
jobs=[json.loads(s) for s in q.read_text('utf8').splitlines()]
assert len(jobs)==len({j['id'] for j in jobs})==1400
assert len({j['reference_time'] for j in jobs})==1
assert not any('หน่วยโทษ' in j['question'] for j in jobs)
before[str(q.resolve())]=sha(q)
for p in [B/'r109_owner_answers_20261020/MERGED_SERVICE_STATEMENTS.json',B/'r109_owner_answers_20261020/OWNER_CLARIFICATIONS.json',B/'r113_multi_flow_benchmark_20261021/COMMON_READ_MODEL.json',source/'CANDIDATE_DATA_IMPORT.json']:
    before[str(p.resolve())]=sha(p)
(R/'REFERENCE_HASHES.json').write_text(json.dumps(before,indent=2),'utf8')
(R/'QUESTION_MANIFEST.json').write_text(json.dumps({'questions':1400,'new_questions_added':0,'source_path':str(q.resolve()),'sha256':sha(q),'copy_sha256':sha(R/'EXISTING_QUESTIONS_1400.jsonl'),'reference_time':jobs[0]['reference_time'],'category_hints_sent_to_chat':False},indent=2),'utf8')
(R/'STATUS.json').write_text(json.dumps({'phase':'source_review_and_native_expectation_alignment','steps_requested':[1,2,3],'candidate_only':True,'new_questions_added':0,'production_installed':False},indent=2),'utf8')
assert all(sha(Path(p))==h for p,h in before.items())
print(json.dumps({'isolated_candidate':str((R/'system').resolve()),'reference_files':len(before),'existing_questions':1400,'new_questions':0}))
