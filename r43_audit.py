import sys,json,hashlib,difflib,subprocess,uuid
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r43_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');RELEASE=Path((OUT/'release_r43_3_path.txt').read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before=json.loads((OUT/'before_manifest.json').read_text());missing=[r for r in before if not (ROOT/r).is_file()];changed=[r for r,h in before.items() if (ROOT/r).is_file() and digest(ROOT/r)!=h]
allowed={'app/web_api/server.py','app/pipeline/bilingual_english.py','app/session/conversation_plan.py',*[f'deployment_templates/{n}' for n in ('Open-PSU-Esports-Background.ps1','Open-PSU-Esports-Chatbot.ps1','Start-PSU-Esports-Chatbot.ps1','README_TH.md')]}
new=['deployment_templates/Runtime-Readiness.ps1','tests/test_runtime_readiness_r43.py','tests/test_schedule_completeness_r43.py']
protected=['booking_dashboard/center_schedule.json','data/curated/service_policy_answers.json','data/competition_rules/competition_rule_chunks.jsonl','data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl','app/calculator/service_fee.py']
parity={p.relative_to(ROOT).as_posix():(RELEASE/p.relative_to(ROOT)).is_file() and digest(p)==digest(RELEASE/p.relative_to(ROOT)) for folder in ('app','web_chat') for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts}
deployment={n:(RELEASE/n).is_file() and digest(ROOT/'deployment_templates'/n)==digest(RELEASE/n) for n in ('Runtime-Readiness.ps1','Open-PSU-Esports-Background.ps1','Open-PSU-Esports-Chatbot.ps1','Start-PSU-Esports-Chatbot.ps1','README_TH.md')}
knowledge={p.relative_to(ROOT).as_posix():(RELEASE/p.relative_to(ROOT)).is_file() and digest(p)==digest(RELEASE/p.relative_to(ROOT)) for folder in ('data/curated','data/competition_rules') for p in (ROOT/folder).glob('*') if p.is_file() and p.suffix in ('.json','.jsonl')}
frozen=json.loads((OUT/'release_r43_3_hashes.json').read_text());immutable={r:(RELEASE/r).is_file() and digest(RELEASE/r)==h for r,h in frozen.items()}
diff=[]
for r in changed+new:
 old=(OUT/'before'/r).read_text(encoding='utf-8-sig').splitlines(True) if (OUT/'before'/r).is_file() else []
 diff.extend(difflib.unified_diff(old,(ROOT/r).read_text(encoding='utf-8-sig').splitlines(True),fromfile='before/'+r,tofile='after/'+r))
with (OUT/'SOURCE_CHANGE_R43_FINAL.diff').open('x',encoding='utf-8') as f:f.writelines(diff)
git=[]
for label,args in [('status',['status','--short']),('diff_check',['diff','--check'])]:
 p=subprocess.run(['git','-c','safe.directory='+ROOT.parent.as_posix(),'-C',str(ROOT),*args],capture_output=True,text=True,encoding='utf-8',errors='replace')
 file=f'git_{label}_verified.txt'
 with (OUT/file).open('x',encoding='utf-8') as f:f.write(p.stdout+p.stderr)
 git.append(dict(check=label,returncode=p.returncode,evidence=file))
result=dict(before_files=len(before),changed=changed,new_files=new,missing_before_files=missing,unexpected_changes=sorted(set(changed)-allowed),protected_unchanged={r:digest(ROOT/r)==before[r] for r in protected},app_web_parity=parity,deployment_parity=deployment,knowledge_parity=knowledge,frozen_bytes_unchanged=immutable,git=git)
with (OUT/'SOURCE_AUDIT_R43_FINAL.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print('changed',changed,'new',new,'parity',len(parity),sum(parity.values()),'knowledge',len(knowledge),sum(knowledge.values()),'deployment',deployment,'immutable',all(immutable.values()),'protected',result['protected_unchanged'],'git',git)
assert not missing and not result['unexpected_changes'] and all(result['protected_unchanged'].values()) and all(parity.values()) and all(knowledge.values()) and all(deployment.values()) and all(immutable.values()) and all(g['returncode']==0 for g in git)
