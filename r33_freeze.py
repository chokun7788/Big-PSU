import json,hashlib,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path((ROOT/'r33_report_path.txt').read_text().strip())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest={f.relative_to(P).as_posix():sha(f) for folder in ['app','web_chat'] for f in (P/folder).rglob('*') if f.is_file() and '__pycache__' not in f.parts and f.suffix!='.pyc'}
before=json.loads((R/'before_manifest.json').read_text());protected=json.loads((R/'protected_manifest.json').read_text());assert all(sha(P/k)==v for k,v in protected.items())
changed=[k for k in manifest if manifest[k]!=before.get(k)]
data=dict(runtime_version='2026.10.02-usable-task-frames-r33',manifest=manifest,changed_runtime=changed,protected_unchanged=len(protected),note='Full r33 candidate_D execution uses the frozen D runtime; subsequent replay/deployment must name its runtime manifest explicitly.')
with (R/(sys.argv[1]+'_runtime_freeze.json')).open('x',encoding='utf-8') as out:json.dump(data,out,ensure_ascii=False,indent=2)
package=P/(sys.argv[2] if len(sys.argv)>2 else 'owner_local_delivery_20261002_source_content_reliability_r32_candidate6/PSU_Esports_Chatbot_Local');assert all(sha(package/k)==v for k,v in manifest.items())
print(json.dumps({'changed_runtime':changed,'protected_unchanged':len(protected),'package_runtime_hashes_match':len(manifest)},ensure_ascii=False))
