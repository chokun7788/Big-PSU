import hashlib,json
from r27_fixture import PROJECT,REPORT
files=['app/pipeline/engine.py','app/pipeline/competition_detail.py','app/core/intent_cue_recovery.py','tools/competition_content_grader_r27.py','tools/run_competition_contract_r27.py','tests/test_competition_contract_r27_20261001.py']
manifest={}
for relative in files:
    dest=REPORT/'ready_code'/relative;dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('xb') as f:f.write((PROJECT/relative).read_bytes())
    manifest[relative]=hashlib.sha256((PROJECT/relative).read_bytes()).hexdigest()
for old,new in [('content_contract_fixture_v2.json','competition_content_contract_r27_320_20261001.json'),('new_questions_fixture_128.json','competition_new_questions_r27_128_20261001.json')]:
    with (PROJECT/'data/eval'/new).open('xb') as f:f.write((REPORT/old).read_bytes())
with (REPORT/'ready_code_manifest.json').open('x',encoding='utf-8') as f:json.dump(manifest,f,indent=2)
print(json.dumps(manifest,indent=2))
