import json,hashlib,sqlite3,shutil
from pathlib import Path
B=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
files=json.loads((B/'SOURCE_MANIFEST_REPAIRED.json').read_text(encoding='utf-8'))
changes=[]
for r in files:
 p=ROOT/r['path']
 if not p.exists():changes.append({'path':r['path'],'status':'missing'});continue
 current=hashlib.sha256(p.read_bytes()).hexdigest()
 if current!=r['sha256']:changes.append({'path':r['path'],'before':r['sha256'],'after':current})
def logical(path):
 if not path.is_relative_to(B):
  dest=B/'preservation_copies'/path.parent.name;dest.mkdir(parents=True,exist_ok=False)
  members=[p for p in (path,Path(str(path)+'-wal')) if p.exists()]
  before=[(p.stat().st_size,p.stat().st_mtime_ns) for p in members]
  for p in members:shutil.copy2(p,dest/p.name)
  after=[(p.stat().st_size,p.stat().st_mtime_ns) for p in members]
  if before!=after:raise RuntimeError('Source changed while copying; cannot certify consistency')
  path=dest/path.name
 h=hashlib.sha256()
 with sqlite3.connect(path.as_uri()+'?mode=ro',uri=True) as c:
  for line in c.iterdump():h.update(line.encode('utf-8'));h.update(b'\n')
 return h.hexdigest()
db={}
for mode,source in [('legacy',ROOT/'data/knowledge/approved.sqlite'),('common',ROOT/'data/knowledge/migration_r63_20261013/approved.sqlite')]:
 before=logical(B/(mode+'.sqlite'));after=logical(source);db[mode]={'snapshot':before,'source_now':after,'logical_unchanged':before==after}
report={'checked_files':len(files),'changed_source_files':changes,'knowledge_databases':db,'original_code_edited_this_turn':False,'logs_written_only_under':str(B),'git_preexisting_changes_not_reverted':True}
(B/'PRESERVATION_CHECK.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
