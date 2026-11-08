"""Isolated development and legacy teacher; previous frozen work unchanged."""
import hashlib,json,shutil,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;P=ROOT/'r123_contract_execution_20261023/revision05_system';S=R/'system'
LEGACY=Path('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data');T=R/'teacher'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
assert not S.exists() and not T.exists()
freeze={str(p.resolve()):sha(p) for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}
(R/'PARENT_FREEZE.json').write_text(json.dumps(freeze,indent=2),'utf8')
ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm','owner-session.json')
shutil.copytree(P,S,ignore=ignore);T.mkdir()
teacher_freeze={}
for name in ('app','data','booking_dashboard'):
 src=LEGACY/name
 for p in src.rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.log'} and not p.name.endswith(('-wal','-shm')):teacher_freeze[str(p.resolve())]=sha(p)
 shutil.copytree(src,T/name,ignore=ignore)
(R/'TEACHER_FREEZE.json').write_text(json.dumps(teacher_freeze,indent=2),'utf8')
db=S/'data/knowledge/common.sqlite'
with sqlite3.connect(db.resolve().as_uri()+'?mode=ro',uri=True) as c:
 records={rid:json.loads(payload) for rid,payload in c.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0')}
 sources={sid:json.loads(payload) for sid,payload in c.execute('SELECT source_id,snapshot FROM cc_sources')}
rows=[]
for rid,r in records.items():
 if r['kind']!='schedule':continue
 item={'record_id':rid,'fields':{k:v for k,v in r['fields'].items() if k in {'weekday','open_periods','bookable_periods','maintenance_periods','service_slots','zone_ids','legacy_context'}},'evidence':{}}
 for key,f in item['fields'].items():
  for ref in f.get('evidence_refs',[]):
   if key=='legacy_context':continue
   item['evidence'][ref['source_id']]=sources.get(ref['source_id'])
 rows.append(item)
(R/'CALENDAR_SOURCE_CONFLICTS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8')
(R/'STATUS.json').write_text(json.dumps({'status':'implementing_legacy_guided_parity','candidate':str(S),'teacher':str(T),'method':'compare same retained questions; trace source/tool/plan; fix common readers and on-demand live adapters','full_test_started':False,'production_installed':False,'prior_data_unchanged':True},indent=2),'utf8')
print(json.dumps({'candidate':str(S),'teacher':str(T),'protected_candidate_files':len(freeze),'protected_legacy_files':len(teacher_freeze),'calendar_source_report':str(R/'CALENDAR_SOURCE_CONFLICTS.json')},ensure_ascii=False))
