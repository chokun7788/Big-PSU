import json,hashlib,sqlite3
from pathlib import Path
p=Path(__file__).resolve().parent
f=p/'FINAL_OWNER_EDIT_RECEIPT.json'
r=json.loads(f.read_text(encoding='utf-8'));checks={};counts={}
for db,old in r['production_database_after'].items():
    c=sqlite3.connect('file:'+Path(db).as_posix()+'?mode=ro',uri=True)
    checks[db]=hashlib.sha256('\n'.join(c.iterdump()).encode()).hexdigest()==old
    counts[db]={'records':c.execute('select count(*) from cc_heads').fetchone()[0],'releases':c.execute('select count(*) from cc_releases').fetchone()[0]}
    c.close()
r.update(final_database_unchanged=checks,final_database_counts=counts,actual_owner_edit_and_history_read=True,actual_owner_port=8097)
f.write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'unchanged':all(checks.values()),'counts':counts}))
if not all(checks.values()):raise SystemExit('Database changed; inspect concurrent writer')
