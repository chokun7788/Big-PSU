import json,hashlib
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path(Path(__file__).with_name('r26_report_path.txt').read_text(encoding='utf-8').strip())
relative='web_chat/app.js';dest=report/'before'/relative;dest.parent.mkdir(parents=True,exist_ok=True)
with dest.open('xb') as f:f.write((project/relative).read_bytes())
with (report/'ui_before_manifest.json').open('x',encoding='utf-8') as f:json.dump({relative:hashlib.sha256((project/relative).read_bytes()).hexdigest()},f,indent=2)
