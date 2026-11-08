import hashlib,json
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path(Path(__file__).with_name('r26_report_path.txt').read_text(encoding='utf-8').strip())
files=['app/core/intent_cue_recovery.py','app/pipeline/engine.py','app/pipeline/retrieval.py','app/pipeline/competition_presentation.py','app/pipeline/competition_fast_route.py','app/pipeline/competition_taxonomy.py','web_chat/app.js','tests/test_competition_content_speed_r26_20261001.py']
manifest={}
pkg=project/'owner_local_delivery_20261001_competition_content_speed_r26_ready/PSU_Esports_Chatbot_Local'
for relative in files:
 path=project/relative;dest=report/'ready_code'/relative;dest.parent.mkdir(parents=True,exist_ok=True)
 with dest.open('xb') as f:f.write(path.read_bytes())
 manifest[relative]=hashlib.sha256(path.read_bytes()).hexdigest()
 if not relative.startswith('tests/'):
  assert hashlib.sha256((pkg/relative).read_bytes()).hexdigest()==manifest[relative],relative
with (report/'ready_code_manifest.json').open('x',encoding='utf-8') as f:json.dump(manifest,f,indent=2)
print('ready code snapshot: 8 files, package runtime matches: 7')
