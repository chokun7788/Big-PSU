import json,hashlib,subprocess
from pathlib import Path
W=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path((W/'r34_report_path.txt').read_text().strip());package=P/'owner_local_delivery_20261003_source_task_boundaries_r34_finalI/PSU_Esports_Chatbot_Local'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before=json.loads((R/'before_manifest.json').read_text());owner=json.loads((R/'protected_manifest.json').read_text())
assert all(sha(P/k)==v for k,v in owner.items())
existing_tests={k:v for k,v in before.items() if k.startswith('tests/')};assert all(sha(P/k)==v for k,v in existing_tests.items())
runtime={f.relative_to(P).as_posix():sha(f) for folder in ['app','web_chat'] for f in (P/folder).rglob('*') if f.is_file() and '__pycache__' not in f.parts and f.suffix!='.pyc'}
assert all(sha(package/k)==v for k,v in runtime.items())
changes=[k for k,v in runtime.items() if before.get(k)!=v]
with (R/'FINAL_I_RUNTIME_FREEZE.json').open('x',encoding='utf-8') as f:json.dump(dict(version='2026.10.03-source-task-boundaries-r34',package=str(package),manifest=runtime,changed_runtime=changes,owner_Gold_unchanged=len(owner),existing_tests_unchanged=len(existing_tests),package_hashes_match=len(runtime)),f,ensure_ascii=False,indent=2)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=P,capture_output=True,text=True,encoding='utf-8',check=True).stdout
with (R/'git_status_after_finalI.txt').open('x',encoding='utf-8') as f:f.write(status)
print(dict(changed_runtime=changes,owner_Gold_unchanged=len(owner),existing_tests_unchanged=len(existing_tests),package_hashes_match=len(runtime)))

h=json.loads((R/'FINAL_H_RUNTIME_FREEZE.json').read_text());diff=[k for k,v in runtime.items() if h['manifest'].get(k)!=v];assert diff==['app/pipeline/engine.py'];print(dict(H_to_I_runtime_diff=diff))
