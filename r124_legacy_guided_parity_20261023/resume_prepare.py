"""Resume the owned staging copy using Windows extended-length paths."""
import hashlib,json,shutil,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';T=R/'teacher';L=Path('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data')
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm','owner-session.json')
freeze={}
for name in ('app','data','booking_dashboard'):
 for p in (L/name).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.log'} and not p.name.endswith(('-wal','-shm')):freeze[str(p.resolve())]=sha(p)
 shutil.copytree('\\\\?\\'+str((L/name).resolve()),'\\\\?\\'+str((T/name).resolve()),dirs_exist_ok=True,ignore=ignore)
(R/'TEACHER_FREEZE.json').write_text(json.dumps(freeze,indent=2),'utf8')
with sqlite3.connect((S/'data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as c:
 records={rid:json.loads(payload) for rid,payload in c.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0')}
 sources={sid:json.loads(payload) for sid,payload in c.execute('SELECT source_id,snapshot FROM cc_sources')}
rows=[]
for rid,r in records.items():
 if r['kind']!='schedule':continue
 item={'record_id':rid,'fields':{k:v for k,v in r['fields'].items() if k in {'weekday','open_periods','bookable_periods','maintenance_periods','service_slots','zone_ids','legacy_context'}},'evidence':{}}
 for key,f in item['fields'].items():
  if key=='legacy_context':continue
  for ref in f.get('evidence_refs',[]):item['evidence'][ref['source_id']]=sources.get(ref['source_id'])
 rows.append(item)
(R/'CALENDAR_SOURCE_CONFLICTS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8')
(R/'STATUS.json').write_text(json.dumps({'status':'implementing_legacy_guided_parity','candidate':str(S),'teacher':str(T),'method':'run same retained questions on legacy and common; compare plans/tools/source traces; improve common adapters continuously','full_test_started':False,'production_installed':False},indent=2),'utf8')
assert all(sha(Path(p))==h for p,h in json.loads((R/'PARENT_FREEZE.json').read_text('utf8')).items())
print('Isolated candidate/teacher ready; original candidate source hashes unchanged')
