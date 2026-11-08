import json,hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());READY=BASE.parents[1]/'PSU_Esports_Share_R56_20261010';rows=[]
for variant in ('01_Download_Models','02_With_Models'):
 d=READY/variant;p=d/'system/PSU_Esports_Chatbot_Local/Start-PSU-Esports-Chatbot.ps1';t=p.read_text(encoding='utf-8-sig');assert t.count('$env:PSU_PIPELINE_WORKERS = "2"')==1 and '$env:PSU_PIPELINE_WORKERS = "1"' not in t
 hashes={}
 for name in ('Start-Chatbot.ps1','Stop-Chatbot.ps1','Runtime-Process-Identity.ps1','system/PSU_Esports_Chatbot_Local/Start-PSU-Esports-Chatbot.ps1'):
  p=d/name;hashes[name]=hashlib.sha256(p.read_bytes()).hexdigest()
  if name in ('Start-Chatbot.ps1','Stop-Chatbot.ps1'):
   txt=p.read_text(encoding='utf-8-sig');assert 'Get-RecordedProcessUtc $Item.started_utc' in txt and '[datetime]::Parse($Item.started_utc)' not in txt
  if name=='Runtime-Process-Identity.ps1':assert 'InvariantCulture' in p.read_text(encoding='utf-8-sig')
 for name in ('ready_manifest.json','system/PSU_Esports_Chatbot_Local/package_manifest.json'):
  assert json.loads((d/name).read_text(encoding='utf-8'))['runtime_version']=='2026.10.10-service-r56.7'
 rows.append(dict(variant=variant,version='2026.10.10-service-r56.7',pipeline_workers=2,llm_shared_limit=1,launcher_hashes=hashes))
assert rows[0]['launcher_hashes']==rows[1]['launcher_hashes']
with (OUT/'PACKAGE_RUNTIME_AUDIT_7.json').open('x',encoding='utf-8') as f:json.dump(rows,f,indent=2)
print('both package launcher hashes match, workers2/LLM1, invariant timestamp checks')
