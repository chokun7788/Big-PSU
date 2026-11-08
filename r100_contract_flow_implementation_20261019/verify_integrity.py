"""Read-only source integrity audit; output belongs only to this candidate."""
from pathlib import Path
import hashlib,json,sys
R=Path(__file__).resolve().parent;B=R.parent/'r98_flow_v2_implementation_20261019';baseline=json.loads((R/'BASELINE_MANIFEST.json').read_text('utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
changed_baseline=[p for p,h in baseline.items() if sha(B/'system'/p)!=h]
changed_candidate=[p for p,h in baseline.items() if sha(R/'system'/p)!=h]
files={p.relative_to(R/'system').as_posix():sha(p) for p in (R/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
tag=sys.argv[1] if len(sys.argv)>1 else 'final_on04'
freeze=json.loads((R/tag/'SOURCE_BEFORE.json').read_text('utf8'))
report={'baseline':'R98 final frozen source','baseline_files_verified':len(baseline),'r98_unchanged':not changed_baseline,'r98_changed_paths':changed_baseline,'candidate_changed_paths':changed_candidate,'candidate_added_paths':sorted(set(files)-set(baseline)),'candidate_database_unchanged':sha(R/'system/data/knowledge/common.sqlite')==baseline['data/knowledge/common.sqlite'],'final_runtime_unchanged':files==freeze,'source_or_approval_writes_to_real_database':False,'production_install_performed':False}
(R/'INTEGRITY_FINAL.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');(R/'FINAL_SOURCE_MANIFEST.json').write_text(json.dumps(files,indent=2),'utf8');print(json.dumps(report,ensure_ascii=False))
if changed_baseline or not report['candidate_database_unchanged'] or not report['final_runtime_unchanged']:raise SystemExit(1)
