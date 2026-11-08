"""Install verified application changes only; refuse stale baselines/collisions."""
import difflib,hashlib,json,os,uuid
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
baseline=json.loads((B/'BASELINE_MANIFEST.json').read_text('utf-8'))
changes=[]
for rel,h in baseline.items():
 if not (S/rel).is_file() or digest(S/rel)!=h:raise RuntimeError('Installed baseline changed: '+rel)
for p in sorted((B/'candidate').rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(B/'candidate').as_posix();target=S/rel
 if target.exists() and digest(target)==digest(p):continue
 if rel not in baseline and target.exists():raise RuntimeError('New file collision: '+rel)
 if target.exists():
  backup=B/'before'/rel
  if not backup.is_file() or digest(backup)!=digest(target):raise RuntimeError('Verified backup missing: '+rel)
 changes.append((rel,p,target))
gates={}
for tag in ['candidate_release','owner_2','existing_fixture','competition_fixture','flow_2','owner_http','live_2']:
 row=json.loads((B/'verification'/tag/'SUMMARY.json').read_text('utf-8'))
 expected=row.get('asserted',row.get('count'))
 if row['passed']!=expected or row.get('failed'):raise RuntimeError('Verification gate failed: '+tag)
 gates[tag]={'passed':row['passed'],'asserted':expected,'full_test':False}
diff=[];installed={};before={}
for rel,p,target in changes:
 old=target.read_text('utf-8').splitlines(True) if target.exists() else []
 diff.extend(difflib.unified_diff(old,p.read_text('utf-8').splitlines(True),fromfile='before/'+rel,tofile='after/'+rel))
 before[rel]=digest(target) if target.exists() else None
 target.parent.mkdir(parents=True,exist_ok=True)
 temporary=target.with_name(target.name+'.r92-'+uuid.uuid4().hex+'.tmp')
 with temporary.open('xb') as f:f.write(p.read_bytes())
 os.replace(temporary,target);installed[rel]=digest(target)
unexpected=[rel for rel,h in baseline.items() if rel not in installed and digest(S/rel)!=h]
result={'installed_files':installed,'before_sha256':before,'verification_gates':gates,
 'database_unchanged':digest(S/'data/knowledge/common.sqlite')==baseline['data/knowledge/common.sqlite'],
 'unexpected_changes':unexpected,'source_snapshot_legacy_modified':False,'full_test_executed':False,
 'target_system':str(S),'draft_profile_preserved':True,'owner_approvals_written_to_real_database':False}
with (B/'INSTALLATION.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
with (B/'CHANGESET.diff').open('x',encoding='utf-8',newline='\n') as f:f.writelines(diff)
print(json.dumps({'installed_files':len(installed),'database_unchanged':result['database_unchanged'],'unexpected_changes':unexpected}))
if unexpected:raise RuntimeError('Unexpected installed changes; see retained manifest')
