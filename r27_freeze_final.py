import hashlib,json
from r27_fixture import PROJECT,REPORT
files=['app/pipeline/engine.py','app/pipeline/competition_detail.py','app/core/intent_cue_recovery.py','app/web_api/pipeline_supervisor.py','tools/competition_content_grader_r27.py','tools/run_competition_contract_r27.py','tests/test_competition_contract_r27_20261001.py','tests/test_worker_recycle_r27_20261001.py']
manifest={}
for relative in files:
    dst=REPORT/'final_code'/relative;dst.parent.mkdir(parents=True,exist_ok=True)
    with dst.open('xb') as f:f.write((PROJECT/relative).read_bytes())
    manifest[relative]=hashlib.sha256((PROJECT/relative).read_bytes()).hexdigest()
with (REPORT/'final_code_manifest.json').open('x',encoding='utf-8') as f:json.dump(manifest,f,indent=2)
base=__import__('pathlib').Path(__file__).parent
with (base/'r27_final_web_check.py').open('x',encoding='utf-8') as f:f.write((base/'r27_web_check.py').read_text(encoding='utf-8').replace('2026.10.01-competition-contract-r27','2026.10.01-competition-contract-r27-final'))
