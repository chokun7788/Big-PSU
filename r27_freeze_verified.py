import hashlib,json
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path(Path(__file__).with_name('r27_report_path.txt').read_text(encoding='utf-8').strip())
manifest=json.loads((report/'final_code_manifest.json').read_text(encoding='utf-8'))
verified={}
for relative in manifest:
    source=project/relative;data=source.read_bytes()
    target=report/'verified_code'/relative;target.parent.mkdir(parents=True,exist_ok=True)
    with target.open('xb') as f:f.write(data)
    verified[relative]=hashlib.sha256(data).hexdigest()
with (report/'verified_code_manifest.json').open('x',encoding='utf-8') as f:json.dump(verified,f,indent=2)
protected=json.loads((report/'protected_manifest.json').read_text(encoding='utf-8'))
checks={relative:{'before':sha,'after':hashlib.sha256((project/relative).read_bytes()).hexdigest()} for relative,sha in protected.items()}
assert all(row['before']==row['after'] for row in checks.values()),checks
with (report/'protected_verification.json').open('x',encoding='utf-8') as f:json.dump(checks,f,indent=2)
package=project/'owner_local_delivery_20261001_competition_contract_r27_verified/PSU_Esports_Chatbot_Local'
checks={relative:{'source':verified[relative],'package':hashlib.sha256((package/relative).read_bytes()).hexdigest()} for relative in manifest if relative.startswith('app/')}
assert all(row['source']==row['package'] for row in checks.values()),checks
assert not (package/'data/eval').exists()
with (report/'verified_package_code_checks.json').open('x',encoding='utf-8') as f:json.dump({'code':checks,'eval_corpora_in_package':False},f,indent=2)
print(json.dumps({'protected_files_unchanged':len(protected),'runtime_files_match':len(checks),'code_snapshots':len(verified)}))
