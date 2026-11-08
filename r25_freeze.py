import hashlib,json,shutil
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path(Path(__file__).with_name('r25_report_path.txt').read_text(encoding='utf-8').strip())
files=['app/pipeline/competition_presentation.py','app/pipeline/competition_overview.py','app/pipeline/bilingual_english.py','app/pipeline/retrieval.py','app/pipeline/competition_targets.py','app/pipeline/competition_taxonomy.py','web_chat/app.js','web_chat/styles.css','tests/test_competition_format_r25_20261001.py']
manifest={}
for relative in files:
    path=project/relative
    dest=report/'after'/relative
    dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('xb') as handle:handle.write(path.read_bytes())
    manifest[relative]=hashlib.sha256(path.read_bytes()).hexdigest()
with (report/'final_code_manifest.json').open('x',encoding='utf-8') as handle:json.dump(manifest,handle,indent=2)
protected={key:{'before':value,'after':hashlib.sha256((project/key).read_bytes()).hexdigest()} for key,value in json.loads((report/'before_manifest.json').read_text(encoding='utf-8')).items() if key.startswith(('data/','booking_dashboard/'))}
assert all(item['before']==item['after'] for item in protected.values()),protected
with (report/'protected_data_verification.json').open('x',encoding='utf-8') as handle:json.dump(protected,handle,indent=2)
print(json.dumps({'code_snapshot':len(manifest),'protected_unchanged':len(protected)}))
