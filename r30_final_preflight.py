import json,hashlib,subprocess
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip());package=p/'owner_local_delivery_20261002_full_improvement_r30_G3/PSU_Esports_Chatbot_Local'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
before=json.loads((r/'before_manifest.json').read_text());protected=json.loads((r/'protected_manifest.json').read_text());freeze=json.loads((r/'app_freeze_G3.json').read_text())
protected_changes=[rel for rel,d in protected.items() if not (p/rel).exists() or sha(p/rel)!=d]
snapshot_changes=[rel for rel,d in before.items() if sha(r/'before'/rel)!=d]
changed=[rel for rel,d in before.items() if sha(p/rel)!=d]
original_tests=[rel for rel in changed if rel.startswith('tests/')]
mismatches=[rel for rel,d in freeze.items() if sha(p/rel)!=d or not (package/rel).exists() or sha(package/rel)!=d]
units=json.loads((r/'final_G3_unit_all.json').read_text());http=json.loads((r/'http8091_G3_http_summary.json').read_text());full=json.loads((r/'final_G3_all_summary.json').read_text());extra=json.loads((r/'FINAL_G3_EXTRA_CORPUS_SUMMARY.json').read_text());smokes=json.loads((r/'final_G3_smoke_all.json').read_text());focus=json.loads((r/'final_G3_profile_focused_summary.json').read_text());detail=json.loads((r/'final_G3_competition_G_summary.json').read_text())
expected_unit_failure=len(units['failures'])==1 and units['failures'][0][0].startswith('test_checked_in_locale_files_match_builder') and not units['errors']
pass_gates=not(protected_changes or snapshot_changes or original_tests or mismatches) and expected_unit_failure and all(v['passed']==v['total'] for v in http['by_suite'].values()) and full['unique_requests']==20327 and extra['unique_requests']==970 and focus['passed']==79 and detail['passed']==43 and len(smokes)==85
data={'runtime':'2026.10.02-full-improvement-r30-G3','package':str(package),'protected_total':len(protected),'protected_changes':protected_changes,'original_snapshots':len(before),'snapshot_changes':snapshot_changes,'original_tests_changed':original_tests,'changed_original_production_files':changed,'package_app_mismatch':mismatches,'package_excludes_eval':not (package/'data/eval').exists(),'unit_tests':units['tests'],'expected_preexisting_gold_builder_failure_only':expected_unit_failure,'http':http,'full_unique_requests':full['unique_requests'],'extra_requests':extra['unique_requests'],'smoke_files':len(smokes),'smoke_passed':sum(x['status']=='passed' for x in smokes),'owner_policy_approved':False,'real_booking_oracle_verified':False,'changed_behavior_release_gates_passed':pass_gates,'legacy_oracle_suites_are_not_all_green':True}
with (r/'release_preflight_G3.json').open('x',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,indent=2)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=p,capture_output=True,text=True,encoding='utf-8',check=True).stdout
with (r/'git_status_after_final_G3.txt').open('x',encoding='utf-8') as f:f.write(status)
print(json.dumps({k:v for k,v in data.items() if k not in ['http']},ensure_ascii=False));assert pass_gates
