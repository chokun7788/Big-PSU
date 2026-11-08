import shutil,json,time
from pathlib import Path
R=Path(__file__).resolve().parent;S=R.parent/'r125_date_context_presentation_20261023/system'
if not (R/'system').exists():shutil.copytree(S,R/'system',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
(R/'LINEAGE.json').write_text(json.dumps({'parent':str(S),'candidate':str(R/'system'),'created':time.time(),'production_installed':False,'source_data_modified':False,'scope':'R127 fourteen defect families plus C01-C14 contracts and end-to-end context'},indent=2),'utf8')
print('Candidate copied')
