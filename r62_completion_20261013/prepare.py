from pathlib import Path
import json,shutil,hashlib,sqlite3,subprocess
B=Path(__file__).resolve().parent;BASE=B.parent
SYSTEM=BASE/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
PACK=BASE/'r58_common_content_20261010/ready_package/PSU_Esports_Chatbot_Local'
ROOT=Path('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dbhash(p):
 with sqlite3.connect('file:'+p.as_posix()+'?mode=ro',uri=True) as c:return hashlib.sha256('\n'.join(c.iterdump()).encode()).hexdigest()
if __name__=='__main__':
 result={'files':{},'dbs':{}}
 names=[str(p.relative_to(SYSTEM)).replace('\\','/') for p in (SYSTEM/'app/knowledge/common').glob('*') if p.suffix in {'.py','.json'}]
 names+=['app/pipeline/engine.py','app/web_api/server.py','app/knowledge/local_models.py','app/knowledge/model_gate.py','package_manifest.json','Start-PSU-Esports-Chatbot.ps1','Open-PSU-Esports-Background.ps1','Runtime-Readiness.ps1','app/pipeline/hybrid_retrieval.py','app/pipeline/retrieval.py','app/pipeline/source_guard.py']
 names+=[str(p.relative_to(SYSTEM)).replace('\\','/') for p in (SYSTEM/'tests').glob('test_common*.py')]
 for label,root in [('candidate',SYSTEM),('project',ROOT),('package',PACK)]:
  result['files'][label]={}
  for name in names:
   if not (root/name).is_file():continue
   dest=B/'before'/label/name;dest.parent.mkdir(parents=True,exist_ok=True)
   if dest.exists():raise RuntimeError('Backup exists')
   shutil.copy2(root/name,dest);result['files'][label][name]=sha(root/name)
  result['dbs'][str(root/'data/knowledge/approved.sqlite')]=dbhash(root/'data/knowledge/approved.sqlite')
 demo=BASE/'r58_examples_20sets_20261012/DEMO_720_ONLY.sqlite';result['dbs'][str(demo)]=dbhash(demo)
 with (B/'BEFORE.json').open('x',encoding='utf-8') as f:json.dump(result,f,indent=2)
 subprocess.run(['git','-C',str(ROOT),'status','--porcelain=v1','-uall'],stdout=(B/'GIT_BEFORE.txt').open('x',encoding='utf-8'),check=True)
 print('Backups and databases recorded')
