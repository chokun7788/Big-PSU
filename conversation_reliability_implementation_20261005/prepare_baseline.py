import shutil
from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
HERE=Path(__file__).resolve().parent
BASE=HERE/'baseline_runtime'
BASE.mkdir(exist_ok=True)
shutil.copytree(ROOT/'app',BASE/'app',dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
for p in (HERE/'before/app').rglob('*.py'):
    shutil.copy2(p,BASE/'app'/p.relative_to(HERE/'before/app'))
shutil.copytree(ROOT/'tests',BASE/'tests',dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
print(BASE)
