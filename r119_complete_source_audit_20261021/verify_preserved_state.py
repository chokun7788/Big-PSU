"""Check immutable original revisions/sources, approval and withdrawal state."""
import hashlib,json,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent
connect=lambda p:sqlite3.connect(p.resolve().as_uri()+'?mode=ro',uri=True)
old=connect(R.parent/'r118_precision_readers_20261021/system/data/knowledge/common.sqlite');new=connect(R/'system/data/knowledge/common.sqlite')
def table(c,t):
 return c.execute('SELECT * FROM '+t).fetchall()
tables=[n for n, in old.execute("SELECT name FROM sqlite_master WHERE type='table'")]
unchanged={};appendonly={}
for t in tables:
 a=table(old,t);b=table(new,t)
 if t in {'cc_heads','cc_meta'}:continue
 if t in {'cc_revisions','cc_sources','cc_audit'}:
  sa=set(a);sb=set(b);appendonly[t]={'before':len(a),'after':len(b),'original_rows_unchanged':sa<=sb,'new_rows':len(sb-sa)}
 else:unchanged[t]={'before':len(a),'after':len(b),'identical':a==b}
withdraw=lambda c:{rid for rid, in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')}
protected=json.loads((R/'PROTECTED_INPUTS.json').read_text('utf8'))
bad=[p for p,h in protected.items() if hashlib.sha256(Path(p).read_bytes()).hexdigest()!=h]
result={'append_only_tables':appendonly,'unchanged_tables':unchanged,'withdrawn_count':len(withdraw(new)),'withdrawals_unchanged':withdraw(old)==withdraw(new),'protected_original_files':len(protected),'changed_protected_files':bad,'production_installed':False}
result['passed']=not bad and result['withdrawals_unchanged'] and all(v['identical'] for v in unchanged.values()) and all(v['original_rows_unchanged'] for v in appendonly.values())
(R/'PRESERVED_STATE_GATE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(result,ensure_ascii=False));assert result['passed']
