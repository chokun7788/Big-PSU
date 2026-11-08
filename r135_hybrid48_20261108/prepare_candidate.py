"""Create the isolated hybrid candidate; never write to either parent tree."""
import ast, collections, hashlib, json, os, pathlib, shutil, sqlite3, textwrap
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parent
PARENT = REPO / 'r135_complete_flow_audit_20261026'
LEGACY = REPO / 'PSU_Esports_Chat_Current_R134'

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name, value):
    p = ROOT / name; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf8')

if (ROOT / 'BASELINE_MANIFEST.json').exists():
    raise SystemExit('Candidate already prepared; preserve its evidence.')
shutil.copytree(PARENT / 'system', ROOT / 'system', ignore=shutil.ignore_patterns('data', '__pycache__', '*.pyc', '*.log'))
db = ROOT / 'system/data/knowledge/common.sqlite'; db.parent.mkdir(parents=True)
with sqlite3.connect((PARENT / 'system/data/knowledge/common.sqlite').resolve().as_uri() + '?mode=ro', uri=True) as source:
    with sqlite3.connect(db) as dest: source.backup(dest)
shutil.copytree(PARENT / 'spec', ROOT / 'spec')
for pattern in ('verify*.py', 'verification_support.py'):
    for p in PARENT.glob(pattern): shutil.copy2(p, ROOT / p.name)
shutil.copy2(PARENT / 'paired_eval5_groups_20261107/ITEMS.jsonl', ROOT / 'PAIRED_REVIEW_INPUT.jsonl')
evaldir = ROOT / 'evaluation'; evaldir.mkdir()
for name in ['SELECTED_5_PERCENT_v2.jsonl', 'SELECTION_MANIFEST_v2.json', 'score_results.py', 'run_eval.py']:
    shutil.copy2(REPO / 'r135_eval5_20261107' / name, evaldir / name)
old = LEGACY / 'system/app/knowledge/common/domain_flow/engine.py'
tree = ast.parse(old.read_text(encoding='utf8'))
cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'Engine')
method = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == 'plan')
lines = old.read_text(encoding='utf8').splitlines()
body = textwrap.dedent('\n'.join(lines[method.lineno-1:method.end_lineno]))
body = body.replace('def plan(self,', 'def plan(engine,', 1).replace('self.', 'engine.')
target = ROOT / 'system/app/knowledge/common/domain_flow/r134_reader.py'
target.write_text('"""R134 plan algorithm, shared R135 index/helpers/renderer/verifier.\nNot an independent R134 runtime or an authority bypass.\n"""\nfrom .scope import reference_time\nfrom .readers import read,blocked\n\n' + body + '\n', encoding='utf8')
status = json.loads((PARENT / 'STATUS.json').read_text(encoding='utf-8-sig'))
ledger = json.loads((PARENT / 'COMPLETION_LEDGER.json').read_text(encoding='utf-8-sig'))
chosen = set(status['requirement_specific_review_ids']); rows = []
for number, row in enumerate(ledger['requirements'], 1):
    rid = row['id']
    rows.append({**row, 'original_position': number, 'historical_48': rid in chosen,
        'hybrid_role': 'retained_model_training_deferred' if rid in {'PHASE-07','PHASE-08','PHASE-09','PHASE-10'} or rid in {'FLOW-23','FLOW-24','FLOW-25','FLOW-26'} else 'runtime_or_acceptance_dependency',
        'hybrid_acceptance': 'pending', 'original_requirement_closed': False})
write('REQUIREMENT_MAP.json', {'count':76,'historical_48_count':len(chosen),'rows':rows,'scope':'mapping, not completion'})
files = []
for p in sorted((ROOT / 'system').rglob('*')):
    if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.sqlite','-wal','-shm'}:
        files.append({'path':p.relative_to(ROOT).as_posix(),'sha256':digest(p)})
write('BASELINE_MANIFEST.json', {'created_at':datetime.now().astimezone().isoformat(),
    'parent':str(PARENT),'legacy':str(LEGACY),'files':files,'source_backup_method':'SQLite online backup includes committed WAL',
    'source_copy_sha256':digest(db),'legacy_plan_file_sha256':digest(old),
    'historical_48_ids':sorted(chosen),'parent_owner_live_frozen_modified':False,
    'model':'existing retained model only','python':str(pathlib.Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe')})
write('STATUS.json', {'phase':'prepared','complete':False,'installed':False,'full_r135':'preserved; development paused while hybrid is active','evaluation_started':False,'critical_acceptance':'pending'})
print(json.dumps({'candidate':str(ROOT),'files':len(files),'requirements':len(rows),'historical_48':len(chosen)}))
