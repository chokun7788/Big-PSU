import json,hashlib,difflib,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');N=sys.argv[1] if len(sys.argv)>1 else '5';SUFFIX='' if N=='5' else '_'+N;CAND=Path((OUT/('candidate_'+N+'.txt')).read_text());READY=BASE.parents[1]/'PSU_Esports_Share_R56_20261010'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
before=json.loads((OUT/'hashes_before.json').read_text(encoding='utf-8'));owner=json.loads((OUT/'owner_hashes_before.json').read_text(encoding='utf-8'));changed=[];missing=[];patch=[]
for name,oldsha in before.items():
 p=ROOT/name
 if not p.exists():missing.append(name);continue
 if sha(p)!=oldsha:
  changed.append(name);a=(OUT/'before'/name).read_text(encoding='utf-8').splitlines(True);b=p.read_text(encoding='utf-8').splitlines(True);patch.extend(difflib.unified_diff(a,b,fromfile='before/'+name,tofile='after/'+name))
source={str(p.relative_to(ROOT)):sha(p) for f in ('app','web_chat','tests','tools') for p in (ROOT/f).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix in ('.py','.js','.html','.css')}
new=sorted(k for k in source if k not in before and (k.startswith('app\\') or k.startswith('web_chat\\') or 'r56' in k or k.endswith('inspect_chat_storage.py')))
owner_changed=[k for k,v in owner.items() if not (ROOT/k).exists() or sha(ROOT/k)!=v]
candidate_mismatch=[k for k,v in source.items() if k.startswith(('app\\','web_chat\\')) and (not (CAND/k).exists() or sha(CAND/k)!=v)]
package_checks=[]
for variant in ('01_Download_Models','02_With_Models'):
 app=READY/variant/'system/PSU_Esports_Chatbot_Local'
 # Add the read-only diagnostic into newly built distribution only.
 import shutil
 shutil.copyfile(ROOT/'tools/inspect_chat_storage.py',app/'tools/inspect_chat_storage.py')
 mismatch=[k for k,v in source.items() if k.startswith(('app\\','web_chat\\')) and (not (app/k).exists() or sha(app/k)!=v)]
 owner_mismatch=[k for k,v in owner.items() if not (app/k).exists() or sha(app/k)!=v]
 # Runtime data files are copied from the actual project, not just 38 owner fields.
 dirs=json.loads((app/'package_manifest.json').read_text(encoding='utf-8'))['included_data_directories'];data_mismatch=[];data_count=0
 for folder in dirs:
  for p in (ROOT/'data'/folder).rglob('*'):
   if not p.is_file() or '__pycache__' in p.parts:continue
   data_count+=1;k=p.relative_to(ROOT);target=app/k
   if not target.exists() or sha(p)!=sha(target):data_mismatch.append(str(k))
 package_checks.append(dict(variant=variant,source_mismatches=mismatch,owner_mismatches=owner_mismatch,runtime_data_files=data_count,runtime_data_mismatches=data_mismatch))
audit=dict(existing_snapshots=len(before),changed_existing=changed,added_relevant=new,missing_previous_source_files=missing,owner_files=len(owner),owner_changes=owner_changed,candidate_mismatches=candidate_mismatch,package_checks=package_checks,git_status='unavailable: ancestor workdir metadata error; no reset or cleanup',logs='No original log deletion/truncation; original log files were not part of the source hash snapshot')
with (OUT/('PRESERVATION_AND_PACKAGE_AUDIT'+SUFFIX+'.json')).open('x',encoding='utf-8') as f:json.dump(audit,f,ensure_ascii=False,indent=2)
with (OUT/('source_changes'+SUFFIX+'.patch')).open('x',encoding='utf-8') as f:f.write(''.join(patch))
with (OUT/('source_hashes_final'+SUFFIX+'.json')).open('x',encoding='utf-8') as f:json.dump(source,f,indent=2)
print('changed',len(changed),'owner_changed',owner_changed,'candidate',candidate_mismatch,'package',[(c['variant'],len(c['source_mismatches']),len(c['runtime_data_mismatches'])) for c in package_checks]);assert not missing and not owner_changed and not candidate_mismatch and all(not c['source_mismatches'] and not c['owner_mismatches'] and not c['runtime_data_mismatches'] for c in package_checks)
