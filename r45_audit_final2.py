import json,hashlib,difflib,subprocess
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r45_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');RELEASE=Path((OUT/'release_r45_2_path.txt').read_text());PREVIOUS=Path((BASE/'r44_current_path.txt').read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before=json.loads((OUT/'before_manifest.json').read_text());changed=[r for r,v in before.items() if (ROOT/r).is_file() and digest(ROOT/r)!=v];missing=[r for r in before if not (ROOT/r).is_file()]
protected={r:digest(ROOT/r)==v for r,v in before.items() if r.startswith('data/curated/') or r=='app/calculator/service_fee.py'}
parity={p.relative_to(ROOT).as_posix():(RELEASE/p.relative_to(ROOT)).is_file() and digest(p)==digest(RELEASE/p.relative_to(ROOT)) for folder in ('app','web_chat','data/curated') for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts}
expected=json.loads((PREVIOUS/'WORKBOOK_EXTRACTION.json').read_text(encoding='utf-8'))['sha256']
workbooks={str(p):digest(p)==expected for p in (Path(r'D:\Download New\ค่าบริการครึ่งวันและเต็มวัน PSU Esports Studio - Phuket (1).xlsx'),ROOT/'data/sources/zone_rental_fees_20261006.xlsx',RELEASE/'data/sources/zone_rental_fees_20261006.xlsx')}
frozen=json.loads((OUT/'release_r45_2_hashes.json').read_text());immutable=all((RELEASE/r).is_file() and digest(RELEASE/r)==v for r,v in frozen.items())
diff=[]
for r in changed+['tests/test_rental_scope_r45.py']:
    old=(OUT/'before'/r).read_text(encoding='utf-8-sig').splitlines(True) if (OUT/'before'/r).is_file() else []
    diff.extend(difflib.unified_diff(old,(ROOT/r).read_text(encoding='utf-8-sig').splitlines(True),fromfile='before/'+r,tofile='after/'+r))
with (OUT/'SOURCE_CHANGE_R45_2_FINAL.diff').open('x',encoding='utf-8') as f:f.writelines(diff)
git=[]
for label,args in [('status',['status','--short']),('diff_check',['diff','--check'])]:
    p=subprocess.run(['git','-c','safe.directory='+ROOT.parent.as_posix(),'-C',str(ROOT),*args],capture_output=True,text=True,encoding='utf-8',errors='replace')
    file=f'GIT_{label}_R45_2.txt'
    with (OUT/file).open('x',encoding='utf-8') as f:f.write(p.stdout+p.stderr)
    git.append(dict(check=label,returncode=p.returncode,evidence=file))
result=dict(changed=changed,new_files=['tests/test_rental_scope_r45.py'],missing_before_files=missing,protected_unchanged=protected,source_release_parity=parity,workbooks_unchanged=workbooks,frozen_unchanged=immutable,git=git)
with (OUT/'SOURCE_AUDIT_R45_2_FINAL.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print('changed',changed,'parity',len(parity),sum(parity.values()),'protected',all(protected.values()),'workbook',all(workbooks.values()),'immutable',immutable,'git',git)
assert changed==['app/pipeline/zone_rental.py'] and not missing and all(protected.values()) and all(parity.values()) and all(workbooks.values()) and immutable and all(g['returncode']==0 for g in git)

