import json,hashlib,sys
from pathlib import Path
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');report=Path((root/'r28_report_path.txt').read_text(encoding='utf-8').strip())
package=project/'owner_local_delivery_20261002_competition_composition_r28_guard_verified/PSU_Esports_Chatbot_Local'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
protected=json.loads((report/'protected_manifest.json').read_text(encoding='utf-8'))
checks={p:sha(project/p)==s for p,s in protected.items()};assert all(checks.values()),checks
unit=json.loads((report/'candidate_G_unit.json').read_text(encoding='utf-8'));assert unit['success'] and unit['tests']==154
for name,n in [('verified_http280_summary.json',280),('verified_http320_summary.json',320),('verified_http_resolution12_summary.json',12)]:
    s=json.loads((report/name).read_text(encoding='utf-8'));assert s['total']==s['passed']==n,(name,s)
reg=json.loads((report/'http_guard_verified_regression.json').read_text(encoding='utf-8'));assert reg['total']==reg['passed']==36
matches={str(p.relative_to(project)).replace('\\','/'):sha(p)==sha(package/p.relative_to(project)) for p in (project/'app').rglob('*.py')};assert all(matches.values())
assert sha(project/'booking_dashboard/center_schedule.json')==sha(package/'booking_dashboard/center_schedule.json')
assert not (package/'data/eval').exists()
data={'protected_files_unchanged':checks,'all_app_python_matches_package':matches,'package_has_no_eval':True,'unit_passed':154,'http_sequential_passed':648,'runtime_version':reg['health']['runtime']['version'],'package':str(package)}
with (report/'release_preflight_verified.json').open('x',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in data.items() if k not in ('all_app_python_matches_package','protected_files_unchanged')},ensure_ascii=False))
