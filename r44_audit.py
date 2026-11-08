import json,hashlib,difflib,subprocess
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r44_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');RELEASE=Path((OUT/'release_r44_2_path.txt').read_text())
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before=json.loads((OUT/'before_manifest.json').read_text());changed=[r for r,v in before.items() if (ROOT/r).is_file() and h(ROOT/r)!=v];missing=[r for r in before if not (ROOT/r).is_file()]
allowed=['app/core/source_registry.py','app/session/conversation_plan.py','app/session/task_memory.py','app/web_api/server.py','app/pipeline/engine.py','app/pipeline/validator.py']
new=['app/pipeline/zone_rental.py','tests/test_zone_rental_r44.py','data/curated/zone_rental_fees_20261006.json','data/sources/zone_rental_fees_20261006.xlsx']
protected=[r for r in before if r.startswith('data/curated/')]+['booking_dashboard/center_schedule.json','app/calculator/service_fee.py','data/competition_rules/competition_rule_chunks.jsonl','data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl']
parity={p.relative_to(ROOT).as_posix():(RELEASE/p.relative_to(ROOT)).is_file() and h(p)==h(RELEASE/p.relative_to(ROOT)) for folder in ('app','web_chat','data/curated') for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts}
frozen=json.loads((OUT/'release_r44_2_hashes.json').read_text())
original=Path(r'D:\Download New\ค่าบริการครึ่งวันและเต็มวัน PSU Esports Studio - Phuket (1).xlsx');expected=json.loads((OUT/'WORKBOOK_EXTRACTION.json').read_text(encoding='utf-8'))['sha256']
result=dict(changed=changed,new_files=new,missing=missing,unexpected_changes=sorted(set(changed)-set(allowed)),protected_unchanged={r:h(ROOT/r)==before[r] for r in protected},source_release_parity=parity,frozen_unchanged={r:(RELEASE/r).is_file() and h(RELEASE/r)==v for r,v in frozen.items()},workbook_hashes={str(p):h(p)==expected for p in (original,OUT/original.name,ROOT/'data/sources/zone_rental_fees_20261006.xlsx',RELEASE/'data/sources/zone_rental_fees_20261006.xlsx')})
diff=[]
for r in changed+[n for n in new if not n.endswith('.xlsx')]:
    old=(OUT/'before'/r).read_text(encoding='utf-8-sig').splitlines(True) if (OUT/'before'/r).is_file() else []
    diff.extend(difflib.unified_diff(old,(ROOT/r).read_text(encoding='utf-8-sig').splitlines(True),fromfile='before/'+r,tofile='after/'+r))
with (OUT/'SOURCE_CHANGE_R44_FINAL.diff').open('x',encoding='utf-8') as f:f.writelines(diff)
result['git']=[]
for label,args in [('status',['status','--short']),('diff_check',['diff','--check'])]:
    p=subprocess.run(['git','-c','safe.directory='+ROOT.parent.as_posix(),'-C',str(ROOT),*args],capture_output=True,text=True,encoding='utf-8',errors='replace')
    filename=f'GIT_{label}_R44.txt'
    with (OUT/filename).open('x',encoding='utf-8') as f:f.write(p.stdout+p.stderr)
    result['git'].append(dict(check=label,returncode=p.returncode,evidence=filename))
with (OUT/'SOURCE_AUDIT_R44_FINAL.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print('changed',changed,'parity',len(parity),sum(parity.values()),'protected',all(result['protected_unchanged'].values()),'xlsx',all(result['workbook_hashes'].values()),'frozen',all(result['frozen_unchanged'].values()),'git',result['git'])
assert not missing and not result['unexpected_changes'] and all(result['protected_unchanged'].values()) and all(parity.values()) and all(result['workbook_hashes'].values()) and all(result['frozen_unchanged'].values()) and all(g['returncode']==0 for g in result['git'])
