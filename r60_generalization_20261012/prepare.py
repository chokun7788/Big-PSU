from pathlib import Path
import json,shutil,hashlib,sqlite3,subprocess
B=Path(__file__).resolve().parent;BASE=B.parent
SYSTEM=BASE/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
PACK=BASE/'r58_common_content_20261010/ready_package/PSU_Esports_Chatbot_Local'
ROOT=Path('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data')
FILES=['app/knowledge/common/answer.py','app/knowledge/common/planner.py','app/knowledge/common/query_contract.py','app/knowledge/common/catalog.json','app/knowledge/common/store.py','app/pipeline/engine.py']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dbhash(p):
    with sqlite3.connect('file:'+p.as_posix()+'?mode=ro',uri=True) as c:return hashlib.sha256('\n'.join(c.iterdump()).encode()).hexdigest()
if __name__=='__main__':
    result={'files':{},'dbs':{}}
    for label,root in [('candidate',SYSTEM),('project',ROOT),('package',PACK)]:
        result['files'][label]={}
        for name in FILES:
            dest=B/'before'/label/name;dest.parent.mkdir(parents=True,exist_ok=True)
            if dest.exists():raise RuntimeError('Backup exists')
            shutil.copy2(root/name,dest);result['files'][label][name]=sha(root/name)
        result['dbs'][str(root/'data/knowledge/approved.sqlite')]=dbhash(root/'data/knowledge/approved.sqlite')
    result['dbs'][str(BASE/'r58_examples_20sets_20261012/DEMO_720_ONLY.sqlite')]=dbhash(BASE/'r58_examples_20sets_20261012/DEMO_720_ONLY.sqlite')
    with (B/'BEFORE.json').open('x',encoding='utf-8') as f:json.dump(result,f,indent=2)
    subprocess.run(['git','-C',str(ROOT),'status','--porcelain=v1','-uall'],stdout=(B/'GIT_BEFORE.txt').open('x',encoding='utf-8'),check=True)
    print('Backed up all three copies; owner databases unchanged')
