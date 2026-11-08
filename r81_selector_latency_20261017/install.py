"""Promote only reviewed candidate files; refuse an unexpected source change."""
import difflib,hashlib,json,shutil
from datetime import datetime,timezone
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((B/'BASELINE_MANIFEST.json').read_text(encoding='utf8'))
required=['candidate_4/RESULTS.json','qualified_1/RESULTS.json','rephrase_1/RESULTS.json','open_day_1/SUMMARY.json']
results=[]
for name in required:
    result=json.loads((B/'verification'/name).read_text(encoding='utf8'))
    assert result['count']==result['passed'],name
    results.append({'suite':name,'count':result['count'],'passed':result['passed']})
qa=json.loads((B/'HELPER_QA.json').read_text(encoding='utf8'));assert qa['count']==qa['passed']
for name,expected in manifest.items():assert digest(S/name)==expected,'Installed file changed since backup: '+name
files=['app/knowledge/common/entity_search.py','app/knowledge/common/answer.py']
# Read-only inventory to verify all other application/UI files are preserved.
inventory={p.relative_to(S).as_posix():digest(p) for folder in ('app','web_chat') for p in (S/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts}
patch=[]
for name in files:
    a=(B/'before'/name).read_text(encoding='utf8');z=(B/'candidate'/name).read_text(encoding='utf8')
    compile(z,str(S/name),'exec')
    patch.extend(difflib.unified_diff(a.splitlines(keepends=True),z.splitlines(keepends=True),fromfile='before/'+name,tofile='after/'+name))
with (B/'CHANGESET.patch').open('x',encoding='utf8') as f:f.write(''.join(patch))
with (B/'SOURCE_INVENTORY_BEFORE.json').open('x',encoding='utf8') as f:json.dump(inventory,f,indent=2)
for name in files:shutil.copy2(B/'candidate'/name,S/name)
installed={name:digest(S/name) for name in files}
unchanged=[name for name,expected in inventory.items() if name not in files and digest(S/name)==expected]
assert len(unchanged)==len(inventory)-len(files)
assert all(digest(S/name)==value for name,value in manifest.items() if name not in files)
result={'installed_at_utc':datetime.now(timezone.utc).isoformat(),'installation':str(S),'installed_files':installed,'before_files':{name:manifest[name] for name in files},'other_application_ui_files_unchanged':len(unchanged),'r80_open_day_unchanged':True,'database_unchanged':True,'database_sha256':digest(S/'data/knowledge/common.sqlite'),'llm_configuration_changed':False,'tests':results,'related_checks_total':sum(r['count'] for r in results),'real_http_verified_after_patch':False,'restart_required':True,'network_limitation':'Assistant tool loopback denied with WinError 10013; user-launched live helper prepared, not executed by assistant.'}
with (B/'INSTALLATION.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False))
