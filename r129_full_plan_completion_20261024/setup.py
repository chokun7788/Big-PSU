"""Freeze the original full plan and create an isolated implementation candidate."""
import hashlib,json,re,shutil,time
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;P=ROOT/'r128_complete_common_flow_20261024'
if not (R/'system').exists():shutil.copytree(P/'system',R/'system',ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
spec=R/'spec';spec.mkdir(exist_ok=True);requirements=[]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for filename,prefix in [('FLOW_MAIN_TH.md','FLOW'),('DATA_CONTRACTS_TH.md','CONTRACT'),('IMPLEMENTATION_EVALUATION_TH.md','PHASE')]:
 src=ROOT/'r123_plan_distillation_architecture_20261023'/filename;dst=spec/filename
 if not dst.exists():shutil.copy2(src,dst)
 assert digest(src)==digest(dst)
 text=src.read_text('utf8');sections=list(re.finditer(r'^#{2,3} (.+)$',text,re.M))
 for n,m in enumerate(sections):
  title=m[1];body=text[m.end():sections[n+1].start() if n+1<len(sections) else len(text)].strip()
  if not body:continue
  rid=f'{prefix}-{n+1:02}'
  requirements.append({'id':rid,'title':title,'source':filename,'line':text[:m.start()].count('\n')+1,'text':body,'sha256':hashlib.sha256(body.encode()).hexdigest(),'status':'pending','implementation':[],'acceptance_evidence':[]})
  if prefix=='FLOW' and title.startswith('5.'):
   for line in body.splitlines():
    if re.match(r'\| C\d\d ',line):
     cat=line.split('|')[1].strip().split()[0]
     requirements.append({'id':cat,'title':line.split('|')[1].strip(),'source':filename,'text':line,'status':'pending','implementation':[],'acceptance_evidence':[]})
ledger=R/'REQUIREMENTS.json'
if not ledger.exists():ledger.write_text(json.dumps({'scope':'original R123 full runtime/data/training/evaluation plan P0-P8; R128 improvements retained','scope_may_not_be_narrowed':True,'original_plan_files':{n:digest(spec/n) for n in ['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md']},'requirements':requirements},ensure_ascii=False,indent=2),'utf8')
protected=json.loads((P/'DELIVERY_FREEZE.json').read_text('utf8'));bad=[n for n,h in protected.items() if digest(P/n)!=h];assert not bad,bad
(R/'PARENT_FREEZE.json').write_text(json.dumps({str((P/n).resolve()):h for n,h in protected.items()},indent=2),'utf8')
(R/'LINEAGE.json').write_text(json.dumps({'parent':str(P/'system'),'candidate':str(R/'system'),'created':time.time(),'full_plan':'R123 P0-P8 + R00-R12 + C01-C14','parent_source_unchanged':True,'source_data_modified':False,'approvals_modified':False,'production_installed':False},ensure_ascii=False,indent=2),'utf8')
(R/'STATUS.json').write_text(json.dumps({'phase':'full_plan_implementation','complete':False,'requirements':len(requirements),'runtime_activated':False,'new_training_complete':False,'three_arm_comparison_complete':False,'full_test_complete':False},indent=2),'utf8')
print(json.dumps({'candidate':str(R/'system'),'requirements':len(requirements),'original_plan_frozen':True,'R128_unchanged':True},ensure_ascii=False))
