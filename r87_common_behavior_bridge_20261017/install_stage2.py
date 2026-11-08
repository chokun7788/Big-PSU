"""Hash-guarded promotion; preserve the first promotion and its evidence."""
import difflib,hashlib,json,shutil
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=json.loads((B/'INSTALLATION.json').read_text(encoding='utf8'))
for name,sha in old['installed_files'].items():assert digest(S/name)==sha,'Changed since first promotion: '+name
assert digest(S/'data/knowledge/common.sqlite')==old['database_sha256']
files=[p.relative_to(B/'candidate').as_posix() for p in (B/'candidate').rglob('*.py')]
for name in files:
 if name not in old['installed_files']:assert not (S/name).exists(),'New file collision: '+name
results=[]
for name in ['candidate_release/SUMMARY.json','competition_fixture_release/SUMMARY.json']:
 r=json.loads((B/'verification'/name).read_text(encoding='utf8'));assert r['count']==r['passed'] and not r.get('model_failures'),name
 results.append({'suite':name,'count':r['count'],'passed':r['passed'],'real_model_inference':r.get('real_llm_generation_verified',False)})
inventory={p.relative_to(S).as_posix():digest(p) for folder in ['app','web_chat','data/rules'] for p in (S/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts}
patch=[]
for name in files:
 a=(B/'before_stage2'/name).read_text(encoding='utf8') if (B/'before_stage2'/name).exists() else ''
 z=(B/'candidate'/name).read_text(encoding='utf8');compile(z,str(S/name),'exec')
 patch.extend(difflib.unified_diff(a.splitlines(keepends=True),z.splitlines(keepends=True),fromfile='before_stage2/'+name,tofile='after_stage2/'+name))
with (B/'CHANGESET_2.patch').open('x',encoding='utf8') as f:f.write(''.join(patch))
with (B/'SOURCE_INVENTORY_BEFORE_2.json').open('x',encoding='utf8') as f:json.dump(inventory,f,indent=2)
for name in files:shutil.copy2(B/'candidate'/name,S/name)
assert all(digest(S/name)==sha for name,sha in inventory.items() if name not in files)
result={**old,'installed_at_utc':datetime.now(timezone.utc).isoformat(),'installed_files':{name:digest(S/name) for name in files},'before_files':{name:old['installed_files'].get(name) for name in files},'other_application_ui_routing_files_unchanged':len([name for name in inventory if name not in files]),'stage':2,'tests':results,'database_unchanged':digest(S/'data/knowledge/common.sqlite')==old['database_sha256']}
with (B/'INSTALLATION_2.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False))
