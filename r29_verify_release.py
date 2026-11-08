import json,hashlib,sys,subprocess
from pathlib import Path
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');report=Path((root/'r29_report_path.txt').read_text(encoding='utf-8').strip())
package=project/'owner_local_delivery_20261002_input_context_r29_verified/PSU_Esports_Chatbot_Local'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protected=json.loads((report/'protected_manifest.json').read_text(encoding='utf-8'));checks={name:sha(project/name)==value for name,value in protected.items()};assert all(checks.values()),checks
audit=json.loads((report/'change_audit.json').read_text(encoding='utf-8'));assert all(audit['snapshots_verified'].values())
unit=json.loads((report/'candidate_D_unit.json').read_text(encoding='utf-8'));assert unit['success'] and unit['tests']==168
guard=json.loads((report/'candidate_C_guard_regression4283.json').read_text(encoding='utf-8'))['summary'];assert guard['controls_passed']==100 and guard['newly_blocked']==0
pipeline=json.loads((report/'pipeline31_C_summary.json').read_text(encoding='utf-8'));assert pipeline['legacy_noisy_passed']==31
http=[]
for name,count in [('http_noise36_B_summary.json',36),('http_composition280_summary.json',280),('http_contract320_summary.json',320),('http_resolution12_summary.json',12)]:
    data=json.loads((report/name).read_text(encoding='utf-8'));assert data['total']==data['passed']==count,(name,data);http.append({'report':name,'passed':count})
data=json.loads((report/'http_old36.json').read_text(encoding='utf-8'));assert data['total']==data['passed']==36;http.append({'report':'http_old36.json','passed':36})
matches={str(p.relative_to(project)).replace('\\','/'):sha(p)==sha(package/p.relative_to(project)) for p in (project/'app').rglob('*.py')};assert all(matches.values())
assert sha(project/'booking_dashboard/center_schedule.json')==sha(package/'booking_dashboard/center_schedule.json')
assert not (package/'data/eval').exists()
result={'protected_files_unchanged':checks,'snapshots_verified':audit['snapshots_verified'],'changed_production_files':audit['changed'],
        'all_app_python_matches_package':matches,'package_excludes_eval':True,'unit_passed':168,'guard_controls_passed':100,
        'guard_regression_total':4283,'guard_newly_blocked':0,'guard_no_longer_blocked':31,
        'direct_legacy_noisy_passed':31,'direct_clean_noisy_identical':29,'http_sequential':http,'http_total_passed':sum(r['passed'] for r in http),
        'http_noise_static_checks':29,'http_noise_real_booking_path_only':2,'http_noise_intentional_layout_controls':5,
        'real_booking_ground_truth_verified':False,'owner_policy_approval':False,
        'known_semantic_issues_retained':['multi_duration_price','focused_controls_overselection','booking_required_resource_vs_steps','safe_unknown_explanation_vs_missing_translation'],
        'runtime_version':'2026.10.02-input-context-r29-verified','package':str(package)}
with (report/'release_preflight_verified.json').open('x',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=project,capture_output=True,text=True,encoding='utf-8',check=True).stdout
with (report/'git_status_after.txt').open('x',encoding='utf-8') as f:f.write(status)
print(json.dumps({k:result[k] for k in ('unit_passed','guard_controls_passed','guard_regression_total','guard_newly_blocked','http_total_passed','package','known_semantic_issues_retained')},ensure_ascii=False))
