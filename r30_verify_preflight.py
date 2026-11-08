import json,hashlib,subprocess
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip());package=p/'owner_local_delivery_20261002_full_improvement_r30_F/PSU_Esports_Chatbot_Local'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
before=json.loads((r/'before_manifest.json').read_text());protected=json.loads((r/'protected_manifest.json').read_text());freeze=json.loads((r/'app_freeze_F.json').read_text())
protected_changes=[rel for rel,digest in protected.items() if not (p/rel).exists() or sha(p/rel)!=digest]
snapshot_changes=[rel for rel,digest in before.items() if sha(r/'before'/rel)!=digest]
changed=[rel for rel,digest in before.items() if sha(p/rel)!=digest]
test_original_changes=[rel for rel in changed if rel.startswith('tests/')]
package_mismatch=[rel for rel,digest in freeze.items() if sha(p/rel)!=digest or not (package/rel).exists() or sha(package/rel)!=digest]
units=json.loads((r/'final_F_unit_all.json').read_text());http=json.loads((r/'http8091_F_http_summary.json').read_text());focused=json.loads((r/'candidate_F_profile_focused_summary.json').read_text())
data={'protected_total':len(protected),'protected_changes':protected_changes,'snapshots_total':len(before),'snapshot_changes':snapshot_changes,'changed_production_files':changed,'original_tests_changed':test_original_changes,'package_app_mismatch':package_mismatch,'package_excludes_eval':not (package/'data/eval').exists(),'unit_tests':units['tests'],'unit_failed':len(units['failures']),'unit_errors':len(units['errors']),'focused':focused,'http':http,'owner_policy_approved':False,'real_booking_oracle_verified':False,'package':str(package),'runtime':'2026.10.02-full-improvement-r30-F'}
data['release_changed_behavior_gates_pass']=not(protected_changes or snapshot_changes or test_original_changes or package_mismatch) and focused['passed']==79 and all(x['passed']==x['total'] for x in http['by_suite'].values())
with (r/'release_preflight_F.json').open('x',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,indent=2)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=p,capture_output=True,text=True,encoding='utf-8',check=True).stdout
with (r/'git_status_after_preflight.txt').open('x',encoding='utf-8') as f:f.write(status)
print(json.dumps({k:v for k,v in data.items() if k not in ['http','focused']},ensure_ascii=False))
assert data['release_changed_behavior_gates_pass']
