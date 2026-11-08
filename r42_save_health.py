import json,sys,time,uuid,urllib.request
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r42_current_path.txt').read_text(encoding='utf-8'))
with urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=8) as r:health=json.load(r)
file=OUT/(sys.argv[1]+'_'+time.strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]+'.json')
with file.open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
print(file.name,json.dumps({k:health.get(k) for k in ('warmup','llm_preflight')},ensure_ascii=False))
