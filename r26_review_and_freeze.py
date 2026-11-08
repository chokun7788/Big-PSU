import hashlib,json,subprocess,sys
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
root=Path(__file__).parent;report=Path((root/'r26_report_path.txt').read_text(encoding='utf-8').strip())
files=['app/core/intent_cue_recovery.py','app/pipeline/engine.py','app/pipeline/retrieval.py','app/pipeline/competition_presentation.py','app/pipeline/competition_fast_route.py','tests/test_competition_content_speed_r26_20261001.py']
manifest={}
for relative in files:
 path=project/relative;dest=report/'after'/relative;dest.parent.mkdir(parents=True,exist_ok=True)
 with dest.open('xb') as f:f.write(path.read_bytes())
 manifest[relative]=hashlib.sha256(path.read_bytes()).hexdigest()
with (report/'code_freeze.json').open('x',encoding='utf-8') as f:json.dump(manifest,f,indent=2)
original=json.loads((report/'before_manifest.json').read_text(encoding='utf-8'))
protected={p:{'before':h,'after':hashlib.sha256((project/p).read_bytes()).hexdigest()} for p,h in original.items() if p.startswith('data/') or p.startswith('booking_dashboard/')}
assert all(v['before']==v['after'] for v in protected.values())
with (report/'protected_data_verification.json').open('x',encoding='utf-8') as f:json.dump(protected,f,indent=2)
pkg=project/'owner_local_delivery_20261001_competition_content_speed_r26_final/PSU_Esports_Chatbot_Local'
pkg_match={p:hashlib.sha256((pkg/p).read_bytes()).hexdigest()==h for p,h in manifest.items() if p.startswith('app/')}
assert all(pkg_match.values())
with (report/'package_code_verification.json').open('x',encoding='utf-8') as f:json.dump(pkg_match,f,indent=2)
with (report/'git_status_after.txt').open('x',encoding='utf-8') as f:f.write(subprocess.run(['git','status','--short'],cwd=project,capture_output=True,text=True,encoding='utf-8').stdout)
review=(root/'r25_source_presence_review.py').read_text(encoding='utf-8').replace('r25_report_path.txt','r26_report_path.txt')
with (root/'r26_source_presence_review.py').open('x',encoding='utf-8') as f:f.write(review)
print(json.dumps({'code_files':len(manifest),'protected_files':len(protected),'package_matches':pkg_match}))
