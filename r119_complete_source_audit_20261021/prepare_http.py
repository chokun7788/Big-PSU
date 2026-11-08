import json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r118_precision_readers_20261021'
for n in ['SELECTED_JOBS.jsonl','SELECTION_MANIFEST.json','SAMPLE_ALLOCATION.json','BASELINE_CHECK_V2.json','BASELINE_SCORED_V2.jsonl','SAVED_R115_RESULTS.jsonl','serve_frozen.py','evaluation.py','reference_grader.py','retained_literal.py']:
 assert not (R/n).exists();shutil.copy2(P/n,R/n)
shutil.copy2(R/'PROTECTED_INPUTS.json',R/'REFERENCE_HASHES.json')
src=(P/'run_http02.py').read_text('utf8').replace("OUT=R/'http02'","OUT=R/'http01'")
src=src.replace("'run_http.py','run_http02.py'","'run_http.py'")
src=src.replace('R118 context-first candidate','R119 complete source migration candidate').replace('r118-context-regression','r119-migration-regression').replace('R118-context-first','R119-complete-migration').replace('r118-http01-','r119-http01-')
(R/'run_http.py').write_text(src,'utf8')
print('Prepared exact retained 48 requests; no new benchmark text.')
