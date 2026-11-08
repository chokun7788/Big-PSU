"""Read-only source, candidate approval, syntax and frozen-run audit."""
import ast,collections,hashlib,json,sqlite3,sys
from datetime import datetime
from pathlib import Path
R=Path(__file__).resolve().parent;BASE=R.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
reference=json.loads((R/'BASELINE_HASHES.json').read_text('utf8'))
changed=[name for name,h in reference.items() if not (BASE/name).is_file() or sha(BASE/name)!=h]
syntax=[]
for p in (R/'system/app').rglob('*.py'):
    ast.parse(p.read_text('utf-8-sig'),filename=str(p));syntax.append(str(p.relative_to(R)))
sys.path.insert(0,str(R/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
db=R/'system/data/knowledge/common.sqlite'
store=CommonStore(db);draft=DraftSnapshotView(store).snapshot();published=store.snapshot()
with sqlite3.connect(db.resolve().as_uri()+'?mode=ro',uri=True) as c:
    tables=[r[0] for r in c.execute("select name from sqlite_master where type='table'")]
    approvals={t:c.execute('select count(*) from "'+t+'"').fetchone()[0] for t in tables if 'approval' in t}
run=R/'verification'/sys.argv[1];freeze=json.loads((run/'RUN_FREEZE.json').read_text('utf8'))
frozen_changed=[p for p,h in freeze['files'].items() if not Path(p).is_file() or sha(Path(p))!=h]
native_records=draft['release']['records']
result={'audited_at':datetime.now().astimezone().isoformat(),'reference_files':len(reference),'changed_reference_files':changed,
    'reference_scope':'retained R106 app/data and R113 saved source/code/results enumerated before R114 edits',
    'candidate_python_files_parsed':len(syntax),'candidate_records_by_kind':dict(collections.Counter(r['kind'] for r in native_records.values())),
    'candidate_head_records':len(native_records),'active_release':published['active'],'candidate_approval_tables':approvals,
    'frozen_run':run.name,'frozen_files':len(freeze['files']),'changed_frozen_files':frozen_changed,
    'production_installed':False,'R78_modified_by_this_work':False,'R78_prework_hash_baseline_available':False,
    'read_only_audit':True}
target=R/('DELIVERY_AUDIT_'+datetime.now().strftime('%Y%m%d_%H%M%S_%f')+'.json')
target.write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(result,ensure_ascii=False));assert not changed and not frozen_changed
