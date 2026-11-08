import json,sqlite3,sys
from pathlib import Path
R=Path(__file__).resolve().parent;db=R/'revision03_system/data/knowledge/common.sqlite'
with sqlite3.connect(db.resolve().as_uri()+'?mode=ro',uri=True) as c:
 for rid,payload in c.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0'):
  row=json.loads(payload)
  if any(s.casefold() in rid.casefold() for s in sys.argv[1:]):print(json.dumps(row,ensure_ascii=False))
