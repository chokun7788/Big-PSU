"""Apply the HTTP-discovered mixed-scope fix without changing earlier evidence."""
import hashlib,json,os,uuid,shutil
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
first=json.loads((B/'INSTALLATION.json').read_text('utf-8'))
baseline=json.loads((B/'BASELINE_MANIFEST.json').read_text('utf-8'))
for rel,h in {**baseline,**first['installed_files']}.items():
 if sha(S/rel)!=h:raise RuntimeError('Source changed since installation: '+rel)
gate=json.loads((B/'verification/flow_3/SUMMARY.json').read_text('utf-8'))
if gate['count']!=65 or gate['passed']!=65:raise RuntimeError('Mixed-scope verification did not pass')
rel='app/knowledge/common/answer.py';target=S/rel;candidate=B/'candidate'/rel
backup=B/'before_revision_2'/rel;backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(target,backup)
temp=target.with_name(target.name+'.r92-'+uuid.uuid4().hex+'.tmp')
with temp.open('xb') as f:f.write(candidate.read_bytes())
os.replace(temp,target)
result={**first,'installed_files':{**first['installed_files'],rel:sha(target)},
 'revision_2':{'changed_file':rel,'previous_sha256':sha(backup),'gate':'flow_3 65/65','reason':'Preserve the game role when a compound alias also resolves services and controls'},
 'database_unchanged':sha(S/'data/knowledge/common.sqlite')==baseline['data/knowledge/common.sqlite']}
with (B/'INSTALLATION_2.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({'updated_file':rel,'database_unchanged':result['database_unchanged']}))
