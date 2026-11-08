"""Preserve api01 and rerun its measurement in the original grader environment."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
freeze=json.loads((R/'api01/RUN_FREEZE.json').read_text('utf8'))
assert all(sha(p)==h for p,h in freeze.items()),'Frozen api01 code/source changed'
x=(R/'run_api_comparison.py').read_text('utf8').replace("OUT=R/'api01'","OUT=R/'api02'")
x=x.replace("'run_api_comparison.py','API_SELECTED_JOBS.jsonl'", "Path(__file__).name,'API_SELECTED_JOBS.jsonl'")
target=R/'run_api_comparison02.py';assert not target.exists();target.write_text(x,'utf8')
(R/'API02_REASON.json').write_text(json.dumps({'previous_run':'api01','previous_complete_requests':0,'previous_model_probe_calls':1,'reason':'D venv grader lacks tzdata; use the original bundled Python environment for grading, same as native API','model_source_weights_inputs_readers_grader_unchanged':True,'original_probe_preserved':True,'new_questions':0},indent=2),'utf8')
print('Prepared api02; api01 frozen files unchanged')
