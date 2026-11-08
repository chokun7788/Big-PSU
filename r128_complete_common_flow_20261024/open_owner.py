import json,os,subprocess,sys,time,urllib.request,webbrowser
from pathlib import Path
R=Path(__file__).resolve().parent;session=R/'owner_private/session.json'
if session.exists():
 c=json.loads(session.read_text('utf8'))
 try:
  req=urllib.request.Request(f"http://127.0.0.1:{c['port']}/api/registry",headers={'Authorization':'Bearer '+c['url'].split('#token=',1)[1]})
  with urllib.request.urlopen(req,timeout=2) as f:json.load(f)
  webbrowser.open(c['url']);print('Opened R128 owner editor');raise SystemExit()
 except OSError:pass
log=(R/'OWNER.log').open('a',encoding='utf8');subprocess.Popen([sys.executable,'-B','-X','utf8',str(R/'owner_editor.py'),'--open'],cwd=R.parent,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0),env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
print('Starting R128 owner editor')
