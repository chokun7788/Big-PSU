"""Create an isolated CUDA training environment on D:, leaving existing Python intact."""
import json,os,subprocess,sys,time,traceback
from pathlib import Path
R=Path(__file__).resolve().parent
ASSETS=Path('D:/CodexTraining/psu-r121-20261022');VENV=ASSETS/'venv'
ASSETS.mkdir(parents=True,exist_ok=True)
for name in ['tmp','pip-cache','model']:(ASSETS/name).mkdir(exist_ok=True)
env=os.environ.copy();env.update(TEMP=str(ASSETS/'tmp'),TMP=str(ASSETS/'tmp'),PIP_CACHE_DIR=str(ASSETS/'pip-cache'),PYTHONDONTWRITEBYTECODE='1')
def status(phase,**kw):(R/'SETUP_STATUS.json').write_text(json.dumps({'phase':phase,'updated_at':time.time(),**kw},indent=2),'utf8')
def run(args,phase):
 status(phase,command=args)
 with (R/'SETUP.log').open('a',encoding='utf8') as f:
  f.write('\n'+phase+'\n');f.flush();subprocess.run(args,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
try:
 if not (VENV/'Scripts/python.exe').exists():run([sys.executable,'-m','venv',str(VENV)],'create_isolated_venv')
 py=str(VENV/'Scripts/python.exe')
 run([py,'-m','pip','install','--disable-pip-version-check','torch==2.7.1','--index-url','https://download.pytorch.org/whl/cu128'],'install_cuda_pytorch')
 run([py,'-m','pip','install','--disable-pip-version-check','transformers==4.56.2','peft==0.17.1','bitsandbytes==0.48.1','accelerate==1.10.1','safetensors>=0.4.3','psutil','huggingface_hub==0.35.3'],'install_pinned_training_dependencies')
 run([py,'-m','pip','freeze'],'freeze_environment')
 status('complete',complete=True,python=py,assets=str(ASSETS))
except BaseException as exc:status('failed',complete=False,error=repr(exc),traceback=traceback.format_exc());raise
