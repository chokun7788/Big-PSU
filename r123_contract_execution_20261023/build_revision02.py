"""Strengthen numeric text receipts; preserve the first verified candidate."""
import ast,hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'revision02_system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
runs=sorted(R.glob('verification_*/VERIFICATION.json'));passed=[p for p in runs if json.loads(p.read_text('utf8'))['all_passed']];assert passed
freeze=json.loads((passed[-1].parent/'RUN_FREEZE.json').read_text('utf8'));assert all(sha(Path(p))==h for p,h in freeze.items())
shutil.copytree(R/'system',S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'));D=S/'app/knowledge/common/domain_flow'
p=D/'plan_contract.py';x=p.read_text('utf8').replace("    whole_question_semantics_verified:bool=False", "    whole_question_semantics_verified:bool=False\n    input_basis:str='engine_question_after_native_normalization'\n    raw_request_offset_mapping_implemented:bool=False")
ast.parse(x);p.write_text(x,'utf8')
p=D/'task_execution.py';x=p.read_text('utf8').replace("if category is not None:","if category is not None or history:",1)
x=x.replace("'path':'explicit_category_compatibility'","'path':'trusted_history_compatibility' if history else 'explicit_category_compatibility'")
ast.parse(x);p.write_text(x,'utf8')
x=(R/'verify_foundation.py').read_text('utf8').replace("S=R/'system'","S=R/'revision02_system'")
needle=" checks['forged_reference_rejected']=bool(assess(index,compiled.tasks[0],tampered,snapshot,q)['fatal'])"
replacement=needle+"""
 tampered=copy.deepcopy(result['needs'][0]);tampered['claims'][0]['value']='Free access for everyone regardless of price'
 checks['forged_price_words_rejected']='source_receipt_value_mismatch' in assess(index,compiled.tasks[0],tampered,snapshot,q)['fatal']
 tampered=copy.deepcopy(result['needs'][0]);amount=next(c for c in tampered['claims'] if c['facet']=='amount');amount['numeric']=None
 checks['missing_price_number_rejected']='source_receipt_numeric_missing' in assess(index,compiled.tasks[0],tampered,snapshot,q)['fatal']
"""
assert needle in x;x=x.replace(needle,replacement);ast.parse(x);(R/'verify_foundation02.py').write_text(x,'utf8')
assert all(sha(Path(p))==h for p,h in freeze.items())
(R/'REVISION02_BUILD.json').write_text(json.dumps({'parent_verification':str(passed[-1]),'parent_frozen_unchanged':True,'changes':['verify numeric words as well as amount and source refs','explicitly label engine-normalized input basis','retain history under a marked compatibility path until trusted-history span mapping exists'],'production_installed':False},indent=2),'utf8')
print('Revision02 copied; initial verified source/results preserved')
