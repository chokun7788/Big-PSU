"""Start only this experiment's model server, hidden, with new output logs."""
import json,os,socket,subprocess,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r123_contract_execution_20261023';TRAIN=R.parent/'r121_context_planner_training_20261022'
for source,target in [(OLD/'serve_planner.py',R/'serve_model.py'),(TRAIN/'context_contract.py',R/'context_contract.py')]:
 if not target.exists():target.write_bytes(source.read_bytes())
port=12421
with socket.socket() as sock:sock.bind(('127.0.0.1',port))
tag=str(time.time_ns());log=(R/('MODEL_'+tag+'.log')).open('x',encoding='utf8')
proc=subprocess.Popen(['D:/CodexTraining/psu-r121-20261022/venv/Scripts/python.exe','-B','-X','utf8',str(R/'serve_model.py'),'--port',str(port),'--output-name','inference_'+tag],
 cwd=R,env=os.environ.copy(),stdout=log,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
(R/'MODEL_PROCESS.json').write_text(json.dumps({'launcher_pid':proc.pid,'port':port,'log':log.name,'inference_output':'inference_'+tag,'base_profile':'psu-r121-base:latest','trained_profile':'psu-r121-trained:latest'},indent=2),'utf8')
print('Started isolated model loader; log '+log.name)
