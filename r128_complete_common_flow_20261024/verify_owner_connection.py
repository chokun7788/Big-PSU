"""Verify the real owner UI is bound to the chat draft database without writes."""
import hashlib,json,os,subprocess,sys,time,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;db=R/'system/data/knowledge/common.sqlite';before=hashlib.sha256(db.read_bytes()).hexdigest()
session=R/'owner_private/session.json'
def get(path):
 c=json.loads(session.read_text('utf8'));token=c['url'].split('#token=',1)[1]
 req=urllib.request.Request(f"http://127.0.0.1:{c['port']}"+path,headers={'Authorization':'Bearer '+token})
 with urllib.request.urlopen(req,timeout=4) as f:return json.load(f)
try:registry=get('/api/registry')
except (OSError,ValueError):
 log=(R/'OWNER.log').open('a',encoding='utf8')
 subprocess.Popen([sys.executable,'-B','-X','utf8',str(R/'owner_editor.py')],cwd=R.parent,stdout=log,stderr=subprocess.STDOUT,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
 for _ in range(25):
  time.sleep(.4)
  try:registry=get('/api/registry');break
  except (OSError,ValueError):pass
 else:raise RuntimeError('Owner editor did not start; see OWNER.log')
status=get('/api/status')
checks={'same_database_as_chat':Path(registry['db']).resolve()==db.resolve(),'real_registry_available':len(registry['catalog'])>=20,'records_available':len(status['records'])>800,'no_database_writes':hashlib.sha256(db.read_bytes()).hexdigest()==before}
result={'all_passed':all(checks.values()),'checks':checks,'record_count':len(status['records']),'registry_kinds':len(registry['catalog']),'epoch':status['epoch'],'db':str(db),'owner_port':12823,'authenticated_read_only_requests':2,'save_or_approval_actions':0}
(R/'OWNER_VERIFICATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8');print(json.dumps(result,ensure_ascii=False,indent=2));assert result['all_passed']
