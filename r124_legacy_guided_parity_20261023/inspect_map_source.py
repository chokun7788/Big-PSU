import json,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent
with sqlite3.connect((R/'revision04_system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True) as c:
 for rid,payload in c.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0'):
  r=json.loads(payload);f=r.get('fields',{})
  if r.get('kind')=='competition_rule' and 'cs2' in str(f.get('competition_id')) and 20<=int(f.get('section_number',{}).get('value') or 0)<=38:
   print(json.dumps({'id':rid,'section':f.get('section_number',{}).get('value'),'heading':f.get('heading',{}).get('value'),'text':f.get('text',{}).get('value'),'deps':f.get('depends_on_ids',{}).get('value')},ensure_ascii=False))
