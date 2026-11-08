import os,json,socket,subprocess,time
from pathlib import Path
R=Path(__file__).resolve().parent
with socket.socket() as sock:sock.bind(('127.0.0.1',12421))
name='model_'+str(time.time_ns());log=(R/(name+'.log')).open('x',encoding='utf8')
env=os.environ.copy();env.update(PYTHONDONTWRITEBYTECODE='1',HF_HUB_OFFLINE='1')
p=subprocess.Popen(['D:/CodexTraining/psu-r121-20261022/venv/Scripts/python.exe','-B','-X','utf8',str(R/'serve_model.py'),'--port','12421','--output-name',name],cwd=R.parent,env=env,stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
manifest={'launcher_pid':p.pid,'url':'http://127.0.0.1:12421','output':str(R/name),'log':str(R/(name+'.log')),'weights_changed':False,'protocol':'r128-bounded-context-v1'}
(R/'MODEL_PROCESS.json').write_text(json.dumps(manifest,indent=2),'utf8');print(json.dumps(manifest,indent=2))
