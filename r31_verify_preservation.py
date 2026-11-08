import json,hashlib,subprocess
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r31_report_path.txt').read_text().strip());package=p/'owner_local_delivery_20261002_question_target_content_r31_C/PSU_Esports_Chatbot_Local'
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
before=json.loads((r/'before_manifest.json').read_text());protected=json.loads((r/'protected_manifest.json').read_text());freeze=json.loads((r/'app_freeze_final_C.json').read_text())
owner_changes=[rel for rel,d in protected.items() if not (p/rel).exists() or sha(p/rel)!=d]
snapshot_changes=[rel for rel,d in before.items() if not (r/'before'/rel).exists() or sha(r/'before'/rel)!=d]
changes=[rel for rel,d in before.items() if not (p/rel).exists() or sha(p/rel)!=d]
old_test_changes=[rel for rel in changes if rel.startswith('tests/')]
mismatch=[rel for rel,d in freeze.items() if sha(p/rel)!=d or not (package/rel).exists() or sha(package/rel)!=d]
source_records=dict(owner_protected_files=len(protected),owner_changes=owner_changes,snapshots=len(before),snapshot_changes=snapshot_changes,original_tests_changed=old_test_changes,original_app_files_changed=changes,added_app_files=sorted(set(freeze)-set(before)),package_app_mismatch=mismatch,package=str(package),package_excludes_eval=not (package/'data/eval').exists(),real_booking_oracle_verified=False,owner_policy_approved=False,grader_change='Added an existing source-detail answer mode to outcome classification. Exact predecessor reconstructed from the one-line patch and saved separately; not called an original byte snapshot.')
with (r/'preservation_package_C.json').open('x',encoding='utf-8') as out:json.dump(source_records,out,ensure_ascii=False,indent=2)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=p,capture_output=True,text=True,encoding='utf-8',check=True).stdout
with (r/'git_status_after_C.txt').open('x',encoding='utf-8') as out:out.write(status)
print(json.dumps(source_records,ensure_ascii=False),flush=True)
assert not(owner_changes or snapshot_changes or old_test_changes or mismatch)
