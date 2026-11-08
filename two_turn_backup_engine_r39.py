import shutil,json,hashlib
from pathlib import Path
from two_turn_grader_r39 import OUT
root=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
relative='app/pipeline/engine.py';target=OUT/'before'/relative;target.parent.mkdir(parents=True,exist_ok=True)
with target.open('xb') as stream:stream.write((root/relative).read_bytes())
(OUT/'before_engine_manifest.json').write_text(json.dumps({relative:hashlib.sha256(target.read_bytes()).hexdigest()},indent=2),encoding='utf-8')
print('Engine backed up')
