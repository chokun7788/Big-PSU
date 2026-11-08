import difflib,hashlib,json,shutil
from datetime import datetime,timezone
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
manifest=json.loads((B/'BASELINE_MANIFEST_ROUND_2.json').read_text(encoding='utf8'))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for name,sha in manifest.items():assert digest(S/name)==sha,'Source changed since backup: '+name
new='app/knowledge/common/correction_scope.py';assert not (S/new).exists()
files=[p.relative_to(B/'candidate').as_posix() for p in (B/'candidate').rglob('*.py')]
results=[]
for name in ['unit_2/UNIT_RESULTS.json','qualified_final/RESULTS.json','rephrase_final/RESULTS.json','candidate_2/SUMMARY.json']:
 r=json.loads((B/'verification'/name).read_text(encoding='utf8'));assert r['passed']==r['count'],name
 assert not r.get('model_failures'),name
 results.append({'suite':name,'count':r['count'],'passed':r['passed']})
inventory={p.relative_to(S).as_posix():digest(p) for folder in ('app','web_chat') for p in (S/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts}
patch=[]
for name in files:
 a=(B/'before'/name).read_text(encoding='utf8') if (B/'before'/name).exists() else ''
 z=(B/'candidate'/name).read_text(encoding='utf8');compile(z,str(S/name),'exec')
 patch.extend(difflib.unified_diff(a.splitlines(keepends=True),z.splitlines(keepends=True),fromfile='before/'+name,tofile='after/'+name))
with (B/'CHANGESET.patch').open('x',encoding='utf8') as f:f.write(''.join(patch))
with (B/'SOURCE_INVENTORY_BEFORE.json').open('x',encoding='utf8') as f:json.dump(inventory,f,indent=2)
for name in files:shutil.copy2(B/'candidate'/name,S/name)
assert all(digest(S/name)==sha for name,sha in inventory.items() if name not in files)
assert all(digest(S/name)==sha for name,sha in manifest.items() if name not in files)
result={'installed_at_utc':datetime.now(timezone.utc).isoformat(),'installed_files':{name:digest(S/name) for name in files},'before_files':{name:manifest.get(name) for name in files},'other_application_ui_files_unchanged':len([n for n in inventory if n not in files]),'database_sha256':digest(S/'data/knowledge/common.sqlite'),'database_unchanged':True,'strict_semantic_validator_unchanged':True,'r80_open_day_module_unchanged':True,'tests':results,'full_test_executed':False,'full_test_held_until_user_request':True,'restart_required':True}
with (B/'INSTALLATION.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False))
