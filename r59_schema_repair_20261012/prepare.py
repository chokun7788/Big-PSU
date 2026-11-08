from pathlib import Path
import hashlib,json,shutil,subprocess,sqlite3
B=Path(__file__).resolve().parent
BASE=B.parent
SYSTEM=BASE/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
PACK=BASE/'r58_common_content_20261010/ready_package/PSU_Esports_Chatbot_Local'
ROOT=Path('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data')
FILES=['app/knowledge/common/answer.py','app/knowledge/common/planner.py','app/knowledge/common/catalog.json','app/knowledge/common/owner_server.py','app/pipeline/engine.py']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dbhash(p):
    with sqlite3.connect('file:'+p.as_posix()+'?mode=ro',uri=True) as c:return hashlib.sha256('\n'.join(c.iterdump()).encode()).hexdigest()
if __name__=='__main__':
    snapshots={}
    for label,root in [('candidate',SYSTEM),('package',PACK),('project',ROOT)]:
        snapshots[label]={}
        for name in FILES:
            src=root/name;dest=B/'before'/label/name;dest.parent.mkdir(parents=True,exist_ok=True)
            if dest.exists():raise RuntimeError('Backup already exists')
            shutil.copy2(src,dest);snapshots[label][name]=sha(src)
    subprocess.run(['git','-C',str(ROOT),'status','--porcelain=v1','-uall'],stdout=(B/'GIT_STATUS_BEFORE.txt').open('x',encoding='utf-8'),check=True)
    dbs=[ROOT/'data/knowledge/approved.sqlite',PACK/'data/knowledge/approved.sqlite',BASE/'r58_examples_20sets_20261012/DEMO_720_ONLY.sqlite',BASE/'r58_examples_240_20261012/DEMO_ONLY.sqlite']
    receipt={'source_hashes':snapshots,'database_logical_hashes':{str(p):dbhash(p) for p in dbs},'no_policy_or_owner_record_edits':True}
    (B/'BEFORE_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(receipt,indent=2))
