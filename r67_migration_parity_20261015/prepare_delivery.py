"""Prepare reviewable guarded changes; no writes outside this workspace."""
import hashlib,json,shutil,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent;old=B.parent/'r66_common_repair_20261014/system';root=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
changes=[];conflicts=[]
for p in sorted((B/'system/app').rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts:continue
 rel=p.relative_to(B/'system');before=sha(old/rel);after=sha(p)
 if before==after:continue
 actual=sha(root/rel)
 item={'path':rel.as_posix(),'expected_old_sha256':before,'actual_root_sha256':actual,'new_sha256':after}
 changes.append(item)
 if actual!=before:conflicts.append(item)
 if actual is not None:
  dst=B/'DELIVERY/before'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/rel,dst)
with sqlite3.connect((B/'common.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(B/'DELIVERY/candidate.sqlite') as dst:src.backup(dst)
protected=[]
for rel in ['data/knowledge/approved.sqlite','data/knowledge/migration_r63_20261013/review/approved.sqlite','data/knowledge/migration_r66_20261015/candidate.sqlite']:
 p=root/rel
 if p.is_file():protected.append({'path':rel,'sha256':sha(p)})
result={'root':str(root),'candidate_target':'data/knowledge/migration_r67_20261016/candidate.sqlite','candidate_sha256':sha(B/'DELIVERY/candidate.sqlite'),'changes':changes,'conflicts':conflicts,'protected_databases':protected,'applied':False,'reason':'Workspace-only prepared delivery; separate filesystem grant required before project writes'}
(B/'DELIVERY/PLAN.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'changed_files':len(changes),'conflicts':conflicts,'candidate_sha256':result['candidate_sha256'],'protected_databases':len(protected)},ensure_ascii=False))
