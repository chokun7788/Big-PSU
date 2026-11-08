import json,re,hashlib,collections,urllib.request
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r50_current_path.txt').read_text());SHARE=Path((OUT/'share_path.txt').read_text());release=Path((OUT/'release_r50_2_path.txt').read_text())
docs=[OUT/n for n in ['FLOW_FINAL_R50.md','REVIEW_LOG_R50.md','REPORT_FINAL_R50.md','FAILURE_DETAILS_R50.md']]
checks={}
for p in docs:
 text=p.read_text(encoding='utf-8');targets=re.findall(r'\]\(<([^>]+)>\)',text)
 checks[p.name]=dict(nonempty=bool(text.strip()),fences_even=text.count('```')%2==0,local_links_exist=all(Path(t).exists() for t in targets if re.match(r'^[A-Za-z]:',t)),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
for name in ['01_Download_Models','02_With_Models']:
 folder=SHARE/name;inner=folder/'system/PSU_Esports_Chatbot_Local';equality=[]
 for d in ['app','web_chat','data']:
  for p in (release/d).rglob('*'):
   if p.is_file() and not {'logs','state','__pycache__'}.intersection(p.relative_to(release).parts):
    target=inner/p.relative_to(release);equality.append(target.is_file() and hashlib.sha256(p.read_bytes()).digest()==hashlib.sha256(target.read_bytes()).digest())
 checks[name]=dict(runtime_equal_files=sum(equality),runtime_total_files=len(equality),all_runtime_equal=all(equality),private_sqlite_absent=not list(folder.rglob('*.sqlite3')),latest_readme='2026.10.09-flow-r50.2' in (folder/'README_TH.md').read_text(encoding='utf-8'),launcher_present=(folder/'Start-Chatbot.cmd').is_file())
health=json.load(urllib.request.urlopen('http://127.0.0.1:8091/health',timeout=8))
checks['server']=dict(ok=health['ok'],runtime_version=health['runtime']['version'],workers_ready=all(w['ready'] and w['alive'] for w in health['pipeline_workers']['workers']))
assert all(c['nonempty'] and c['fences_even'] and c['local_links_exist'] for k,c in checks.items() if k.endswith('.md'))
assert all(checks[n]['all_runtime_equal'] and checks[n]['private_sqlite_absent'] and checks[n]['latest_readme'] and checks[n]['launcher_present'] for n in ['01_Download_Models','02_With_Models'])
assert checks['server']['ok'] and checks['server']['workers_ready'] and checks['server']['runtime_version']=='2026.10.09-flow-r50.2'
with (OUT/'FINAL_DOCUMENT_DELIVERY_AUDIT_R50.json').open('x',encoding='utf-8') as f:json.dump(checks,f,ensure_ascii=False,indent=2)
print(json.dumps({k:{a:b for a,b in v.items() if a!='sha256'} for k,v in checks.items()},ensure_ascii=False))
