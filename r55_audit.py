import hashlib,json,difflib,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent
OUT=Path((BASE/'r55_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
LABEL=sys.argv[1] if len(sys.argv)>1 else ''
CAND=OUT/('candidate_'+(sys.argv[2] if len(sys.argv)>2 else '5'))/'PSU_Esports_Chatbot_Local'
def target(name):return OUT/(LABEL+'_'+name if LABEL else name)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
before=json.loads((OUT/'hashes_before.json').read_text())
owners=json.loads((BASE/'r54_shop_cases_20261009_235038/owner_hashes_before.json').read_text())
owner_changes=[k for k,v in owners.items() if digest(ROOT/k)!=v]
changed=[k for k,v in before.items() if digest(ROOT/k)!=v]
new=[str(p.relative_to(ROOT)) for folder in ('app','tests','data/curated','booking_dashboard') for p in (ROOT/folder).rglob('*') if p.is_file() and p.suffix in ('.py','.json','.jsonl','.md') and not any(x in p.parts for x in ('__pycache__','logs','state','.git')) and str(p.relative_to(ROOT)) not in before]
candidate_mismatches=[]
for p in (ROOT/'app').rglob('*.py'):
    if '__pycache__' not in p.parts and digest(p)!=digest(CAND/p.relative_to(ROOT)):candidate_mismatches.append(str(p.relative_to(ROOT)))
result=dict(owner_files_checked=len(owners),owner_changes=owner_changes,baseline_files=len(before),changed=changed,new=new,candidate_app_mismatches=candidate_mismatches)
with target('PRESERVATION_AUDIT.json').open('x',encoding='utf-8') as f:json.dump(result,f,indent=2)
diff=[]
for k in changed+new:
    old=OUT/'before'/k;p=ROOT/k
    diff.extend(difflib.unified_diff(old.read_text(encoding='utf-8').splitlines(True) if old.exists() else [],p.read_text(encoding='utf-8').splitlines(True) if p.exists() else [],fromfile='before/'+k,tofile='after/'+k))
with target('SOURCE_CHANGES.patch').open('x',encoding='utf-8') as f:f.writelines(diff)
with target('hashes_after.json').open('x',encoding='utf-8') as f:json.dump({k:digest(ROOT/k) for k in before.keys()|set(new)},f,indent=2)
print(json.dumps(result,indent=2));assert not owner_changes;assert not candidate_mismatches
