import json,hashlib
from pathlib import Path
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');report=Path((root/'r29_report_path.txt').read_text(encoding='utf-8').strip())
manifest={}
for name in ['app/core/intent_cue_recovery.py','app/pipeline/structured_tools.py']:
    data=(project/name).read_bytes();path=report/'before'/name;path.parent.mkdir(parents=True,exist_ok=True);path.open('xb').write(data);manifest[name]=hashlib.sha256(data).hexdigest()
with (report/'before_downstream_manifest.json').open('x',encoding='utf-8') as f:json.dump(manifest,f,ensure_ascii=False,indent=2)
print(json.dumps(manifest))
