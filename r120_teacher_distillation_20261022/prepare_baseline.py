import json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r119_complete_source_audit_20261021'
jobs=list(map(json.loads,(R/'HOLDOUT_JOBS.jsonl').open(encoding='utf8')))
shutil.copy2(R/'HOLDOUT_JOBS.jsonl',R/'SELECTED_JOBS.jsonl');shutil.copy2(R/'PROTECTED_INPUTS.json',R/'REFERENCE_HASHES.json')
(R/'SELECTION_MANIFEST.json').write_text(json.dumps({'requests':len(jobs),'grades':sum(len(j['entries']) for j in jobs),'default_reference_clock':'2026-10-21T12:00:00+07:00','source':'R116 saved questions, source-case-family-separated from teaching','new_questions':0,'selection':'retained evaluation pilot, not Full accuracy'},indent=2),'utf8')
src=(P/'run_http03.py').read_text('utf8').replace("OUT=R/'http03'","OUT=R/'baseline01'")
src=src.replace("==manifest['requests']==48","==manifest['requests']")
src=src.replace(" assert not read(R/'BASELINE_CHECK_V2.json')['r89_literal_definition_mismatch_keys']\n",'')
old="files += [R/n for n in ["
start=src.index(old);end=src.index('\n',start)
src=src[:start]+"files += [R/n for n in ['SELECTED_JOBS.jsonl','SELECTION_MANIFEST.json','SPLIT_MANIFEST.json','serve_frozen.py','evaluation.py','reference_grader.py','retained_literal.py','run_baseline.py']]"+src[end:]
src=src.replace('R119 complete source migration candidate','R120 baseline R119 revision03').replace('r119-migration-regression','r120-baseline').replace('R119-complete-migration','R120-baseline-R119').replace('r119-http01-','r120-baseline-')
(R/'run_baseline.py').write_text(src,'utf8')
print('Prepared',len(jobs),'baseline requests.')
