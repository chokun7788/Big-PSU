import hashlib,json
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r52_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
old=json.loads((OUT/'before_hashes.json').read_text(encoding='utf-8'))
changed=[];missing=[]
for name,digest in old.items():
    p=ROOT/name
    if not p.exists():missing.append(name)
    elif hashlib.sha256(p.read_bytes()).hexdigest()!=digest:changed.append(name)
data=[n for n in old if n.startswith(('data/','booking_dashboard/'))]
new=[]
for folder in ('app','web_chat','tests'):
    for p in (ROOT/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.relative_to(ROOT).as_posix() not in old:
            new.append(p.relative_to(ROOT).as_posix())
candidate=OUT/'candidate_r52_5/PSU_Esports_Chatbot_Local'
candidate_diffs=[]
for folder in ('app','web_chat','tests'):
    for p in (ROOT/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc':
            other=candidate/p.relative_to(ROOT)
            if not other.exists() or p.read_bytes()!=other.read_bytes():candidate_diffs.append(p.relative_to(ROOT).as_posix())
result=dict(compared_files=len(old),changed=changed,missing=missing,new_source_files=new,
            owner_data_compared=len(data),owner_data_changed=[n for n in changed if n in data],
            source_candidate_differences=candidate_diffs,
            old_logs_hash_verified=False,old_logs_note='Initial snapshot excluded logs; tests write new output/candidate log folders. No claim of whole old-log hash verification.',
            git_status_verified=False,git_note=(OUT/'git_status_before.txt').read_text(encoding='utf-8'))
with (OUT/'preservation_audit.json').open('x',encoding='utf-8') as s:json.dump(result,s,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False,indent=2))
