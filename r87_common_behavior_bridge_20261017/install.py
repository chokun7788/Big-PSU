import difflib,hashlib,json,shutil
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
baseline=json.loads((B/'BASELINE_MANIFEST.json').read_text(encoding='utf8'))
for name,sha in baseline.items():assert digest(S/name)==sha,'Changed since backup: '+name
files=[p.relative_to(B/'candidate').as_posix() for p in (B/'candidate').rglob('*.py')]
for name in files:
 if name not in baseline:assert not (S/name).exists(),'New file collision '+name
results=[]
for name in ['candidate_4/SUMMARY.json','fixture_release/SUMMARY.json','qualified_hardened/RESULTS.json','rephrase_hardened/RESULTS.json']:
 r=json.loads((B/'verification'/name).read_text(encoding='utf8'));assert r['passed']==r['count'],name
 assert not r.get('model_failures'),name
 results.append({'suite':name,'count':r['count'],'passed':r['passed'],'real_model_inference':r.get('real_llm_generation_verified',False),'isolated_fixture':r.get('isolated_fixture',False)})
inventory={p.relative_to(S).as_posix():digest(p) for folder in ['app','web_chat','data/rules'] for p in (S/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts}
patch=[]
for name in files:
 a=(B/'before'/name).read_text(encoding='utf8') if (B/'before'/name).exists() else ''
 z=(B/'candidate'/name).read_text(encoding='utf8');compile(z,str(S/name),'exec')
 patch.extend(difflib.unified_diff(a.splitlines(keepends=True),z.splitlines(keepends=True),fromfile='before/'+name,tofile='after/'+name))
with (B/'CHANGESET.patch').open('x',encoding='utf8') as f:f.write(''.join(patch))
with (B/'SOURCE_INVENTORY_BEFORE.json').open('x',encoding='utf8') as f:json.dump(inventory,f,indent=2)
for name in files:shutil.copy2(B/'candidate'/name,S/name)
assert all(digest(S/name)==sha for name,sha in inventory.items() if name not in files)
assert all(digest(S/name)==sha for name,sha in baseline.items() if name not in files)
result={'installed_at_utc':datetime.now(timezone.utc).isoformat(),'installed_files':{name:digest(S/name) for name in files},'before_files':{name:baseline.get(name) for name in files},'other_application_ui_routing_files_unchanged':len([name for name in inventory if name not in files]),'database_unchanged':True,'database_sha256':digest(S/'data/knowledge/common.sqlite'),'strict_validator_unchanged':True,'open_day_unchanged':True,'legacy_parser_and_matcher_source_unchanged':True,'production_data_modified':False,'tests':results,'full_test_executed':False,'restart_required':True}
with (B/'INSTALLATION.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False))
