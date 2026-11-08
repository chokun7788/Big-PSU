import json,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent
with sqlite3.connect((R/'revision04_system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as c:
 for rid,payload in c.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0'):
  row=json.loads(payload)
  if row['kind']=='control_set':print(json.dumps({'id':rid,'coverage':row['fields'].get('source_coverage'),'entries':len(row['fields'].get('bindings',{}).get('value') or [])},ensure_ascii=False))
