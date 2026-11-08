import hashlib,json,os,sys,shutil
from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=Path((Path(__file__).parent/'two_turn_current_path.txt').read_text(encoding='utf-8'))
files=['app/session/context_resolver.py','app/session/conversation_store.py','app/pipeline/bilingual_english.py']
manifest={}
for name in files:
    file=ROOT/name;target=OUT/'before'/name;target.parent.mkdir(parents=True,exist_ok=True)
    with target.open('xb') as f:f.write(file.read_bytes())
    manifest[name]=hashlib.sha256(file.read_bytes()).hexdigest()
(OUT/'before_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
sys.path.insert(0,str(ROOT));os.chdir(ROOT)
from app.pipeline.entity_resolver import resolve_game_entity
for q in ['Tell me about Call of Duty','Call of Duty','Modern Warfare III','Valoant','Mario Kart 8 Deluxe','Beat Saber']:
    r=resolve_game_entity(q,operation='game_detail')
    print(q,r.as_dict())
