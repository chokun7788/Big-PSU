import difflib,hashlib,json,shutil
from datetime import datetime,timezone
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
required=['candidate_2/RESULTS.json','qualified_final/RESULTS.json','rephrase_1/RESULTS.json','live_candidate_5/SUMMARY.json']
results=[]
for name in required:
 r=json.loads((B/'verification'/name).read_text(encoding='utf8'));assert r['passed']==r['count'],name
 if 'model_failures' in r:assert not r['model_failures'],name
 results.append({'suite':name,'count':r['count'],'passed':r['passed']})
manifest=json.loads((B/'BASELINE_MANIFEST.json').read_text(encoding='utf8'))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for name,value in manifest.items():assert digest(S/name)==value,'Source changed since backup: '+name
files=['app/knowledge/common/entity_search.py','app/knowledge/common/answer.py','app/pipeline/migrated_chat.py']
inventory={p.relative_to(S).as_posix():digest(p) for folder in ('app','web_chat') for p in (S/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts}
patch=[]
for name in files:
 a=(B/'before'/name).read_text(encoding='utf8');z=(B/'candidate'/name).read_text(encoding='utf8');compile(z,str(S/name),'exec')
 patch.extend(difflib.unified_diff(a.splitlines(keepends=True),z.splitlines(keepends=True),fromfile='before/'+name,tofile='after/'+name))
with (B/'CHANGESET.patch').open('x',encoding='utf8') as f:f.write(''.join(patch))
with (B/'SOURCE_INVENTORY_BEFORE.json').open('x',encoding='utf8') as f:json.dump(inventory,f,indent=2)
for name in files:shutil.copy2(B/'candidate'/name,S/name)
assert all(digest(S/name)==value for name,value in inventory.items() if name not in files)
assert all(digest(S/name)==value for name,value in manifest.items() if name not in files)
result={'installed_at_utc':datetime.now(timezone.utc).isoformat(),'installed_files':{name:digest(S/name) for name in files},'before_files':{name:manifest[name] for name in files},'other_application_ui_files_unchanged':len(inventory)-len(files),'strict_semantic_validator_unchanged':True,'r80_open_day_module_unchanged':True,'database_unchanged':True,'database_sha256':digest(S/'data/knowledge/common.sqlite'),'tests':results,'full_test_authorized':False,'full_test_executed':False,'restart_required':True}
with (B/'INSTALLATION.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False))
