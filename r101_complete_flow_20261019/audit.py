"""Freeze working source and verify immutable inputs. No approval/data writes."""
import ast,hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent/'r100_contract_flow_implementation_20261019'
baseline=json.loads((R/'BASELINE_MANIFEST.json').read_text('utf8'))
def manifest(folder):return {p.relative_to(folder).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
frozen=json.loads((B/'FINAL_SOURCE_MANIFEST.json').read_text('utf8'))
bad=[p for p,h in frozen.items() if not (B/'system'/p).is_file() or hashlib.sha256((B/'system'/p).read_bytes()).hexdigest()!=h]
current=manifest(R/'system');changed=[p for p,h in baseline.items() if current.get(p)!=h];added=[p for p in current if p not in baseline]
errors=[]
for p in (R/'system/app').rglob('*.py'):
 try:ast.parse(p.read_text('utf8'),filename=str(p))
 except (SyntaxError,UnicodeDecodeError) as exc:errors.append(str(exc))
report={'baseline_r100_unchanged':not bad,'baseline_changed_files':bad,'candidate_changed_files':changed,'candidate_added_files':added,
 'candidate_database_unchanged':current['data/knowledge/common.sqlite']==baseline['data/knowledge/common.sqlite'],
 'syntax_errors':errors,'full_test_executed':False,'production_installed':False,'real_approvals_created':False}
if '--freeze' in sys.argv:
 path=R/'FINAL_SOURCE_MANIFEST.json'
 if path.exists():raise SystemExit('Refusing to overwrite freeze')
 path.write_text(json.dumps(current,indent=2),'utf8')
if (R/'FINAL_SOURCE_MANIFEST.json').exists():report['frozen_candidate_unchanged']=current==json.loads((R/'FINAL_SOURCE_MANIFEST.json').read_text('utf8'))
(R/'INTEGRITY.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(report,ensure_ascii=False));sys.exit(bool(bad or errors or not report['candidate_database_unchanged'] or report.get('frozen_candidate_unchanged') is False))
