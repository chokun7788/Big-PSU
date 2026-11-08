import sys,json,hashlib,difflib,subprocess,uuid
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r42_current_path.txt').read_text(encoding='utf-8'))
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
minor=sys.argv[1] if len(sys.argv)>1 else '3'
RELEASE=Path((OUT/f'release_r42_{minor}_path.txt').read_text(encoding='utf-8'))
before=json.loads((OUT/'before_manifest.json').read_text(encoding='utf-8'))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
missing=[r for r in before if not (ROOT/r).is_file()]
changed=[r for r,h in before.items() if (ROOT/r).is_file() and digest(ROOT/r)!=h]
protected=['booking_dashboard/center_schedule.json','data/curated/service_policy_answers.json','data/competition_rules/competition_rule_chunks.jsonl','data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl','app/calculator/service_fee.py']
parity=[]
for folder in ('app','web_chat'):
    for p in (ROOT/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts:
            rel=p.relative_to(ROOT);parity.append(dict(file=rel.as_posix(),equal=(RELEASE/rel).is_file() and digest(p)==digest(RELEASE/rel)))
diff=[]
for rel in changed:
    if (OUT/'before'/rel).is_file():
        diff.extend(difflib.unified_diff((OUT/'before'/rel).read_text(encoding='utf-8-sig').splitlines(True),(ROOT/rel).read_text(encoding='utf-8-sig').splitlines(True),fromfile='before/'+rel,tofile='after/'+rel))
new=['tests/test_domain_resume_r42.py']
for rel in new:
    diff.extend(difflib.unified_diff([],(ROOT/rel).read_text(encoding='utf-8').splitlines(True),fromfile='/dev/null',tofile='after/'+rel))
with (OUT/f'SOURCE_CHANGE_R42_{minor}.diff').open('x',encoding='utf-8') as f:f.writelines(diff)
git=[]
for label,args in [('status',['status','--short']),('diff_check',['diff','--check'])]:
    r=subprocess.run(['git','-c','safe.directory='+ROOT.parent.as_posix(),'-C',str(ROOT),*args],capture_output=True,text=True,encoding='utf-8',errors='replace')
    filename=f'git_{label}_verified_'+uuid.uuid4().hex[:6]+'.txt'
    with (OUT/filename).open('x',encoding='utf-8') as f:f.write(r.stdout+r.stderr)
    git.append(dict(check=label,returncode=r.returncode,evidence=filename))
allowed={'app/session/task_memory.py','app/session/conversation_store.py','app/pipeline/engine.py','app/web_api/server.py','app/pipeline/protected_intents.py','app/pipeline/closed_query_improvements.py','app/pipeline/bilingual_english.py','app/core/normalization.py','app/booking/live_status.py'}
result=dict(before_files=len(before),changed=changed,new_files=new,missing_before_files=missing,
    unexpected_changes=sorted(set(changed)-allowed),protected_unchanged={r:(ROOT/r).is_file() and digest(ROOT/r)==before[r] for r in protected},
    app_web_parity=parity,git=git,release=str(RELEASE),version=json.loads((RELEASE/'package_manifest.json').read_text(encoding='utf-8'))['runtime_version'])
with (OUT/f'SOURCE_AUDIT_R42_{minor}.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print('changed',len(changed),'new',len(new),'missing',missing,'unexpected',result['unexpected_changes'],'parity',sum(r['equal'] for r in parity),len(parity),'protected',result['protected_unchanged'],'git',git)
assert not missing and not result['unexpected_changes'] and all(result['protected_unchanged'].values()) and all(r['equal'] for r in parity) and all(g['returncode']==0 for g in git)
