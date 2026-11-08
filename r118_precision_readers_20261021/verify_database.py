import hashlib,json,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent
paths=[R.parent/'r117_context_understanding_20261021/system/data/knowledge/common.sqlite',R/'system/data/knowledge/common.sqlite']
databases=[sqlite3.connect(p.resolve().as_uri()+'?mode=ro',uri=True) for p in paths]
schemas=[c.execute("SELECT type,name,tbl_name,sql FROM sqlite_master ORDER BY type,name").fetchall() for c in databases]
assert schemas[0]==schemas[1]
tables=[x[0] for x in databases[0].execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
checks=[]
for table in tables:
 query='SELECT * FROM "'+table.replace('"','""')+'"'
 records=[sorted(map(repr,c.execute(query).fetchall())) for c in databases]
 checks.append({'table':table,'before_rows':len(records[0]),'after_rows':len(records[1]),'equal':records[0]==records[1],
 'before_logical_sha256':hashlib.sha256('\n'.join(records[0]).encode()).hexdigest(),
 'after_logical_sha256':hashlib.sha256('\n'.join(records[1]).encode()).hexdigest()})
out={'schema_equal':True,'all_tables_and_rows_equal':all(c['equal'] for c in checks),'checks':checks,
 'file_hash_equal':hashlib.sha256(paths[0].read_bytes()).hexdigest()==hashlib.sha256(paths[1].read_bytes()).hexdigest(),
 'basis':'SQLite backup can change file header/layout. Compare schema and all typed row representations through read-only connections; no logical fields excluded.'}
(R/'DATABASE_EQUIVALENCE.json').write_text(json.dumps(out,indent=2),'utf8')
print(json.dumps({'schema_equal':True,'tables':len(checks),'all_equal':out['all_tables_and_rows_equal'],'file_hash_equal':out['file_hash_equal'],'differences':[c['table'] for c in checks if not c['equal']]}))
assert out['all_tables_and_rows_equal']
