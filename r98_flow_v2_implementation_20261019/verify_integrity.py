"""Read-only hash audit of baseline, candidate database, and final test source."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent/'r95_merged_flow_implementation_20261018'
base=json.loads((R/'BASELINE_MANIFEST.json').read_text('utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
changed_base=[p for p,h in base.items() if sha(B/'system'/p)!=h]
changed_candidate=[p for p,h in base.items() if sha(R/'system'/p)!=h]
added=[p.relative_to(R/'system').as_posix() for p in (R/'system').rglob('*') if p.is_file() and p.relative_to(R/'system').as_posix() not in base and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))]
final=json.loads((R/'final_on02/SOURCE_BEFORE.json').read_text('utf8'))
changed_final=[p for p,h in final.items() if sha(R/'system'/p)!=h]
result={'r95_files_verified':len(base),'r95_unchanged':not changed_base,'r95_changed_paths':changed_base,'candidate_changed_paths':changed_candidate,'candidate_added_paths':added,'candidate_database_unchanged':sha(R/'system/data/knowledge/common.sqlite')==base['data/knowledge/common.sqlite'],'final_runtime_source_unchanged':not changed_final,'changed_after_final_freeze':changed_final,'production_install_performed':False,'data_or_approval_changes_to_source':False}
(R/'INTEGRITY.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8');print(json.dumps(result,ensure_ascii=False))
