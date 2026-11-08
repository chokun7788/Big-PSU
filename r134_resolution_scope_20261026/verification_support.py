"""Read-only pinned source snapshot for repair verification, never runtime gold."""
import json,sqlite3,sys
from pathlib import Path
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'system'))
def snapshot():
 c=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
 c.row_factory=sqlite3.Row;c.execute('BEGIN')
 records={x['record_id']:json.loads(x['payload']) for x in c.execute('SELECT r.* FROM cc_revisions r JOIN cc_heads h USING(record_id) WHERE r.version=h.head AND h.withdrawn=0')}
 pairs={x['source_id']:(json.loads(x['payload']),x['snapshot']) for x in c.execute('SELECT * FROM cc_sources')}
 meta=dict(c.execute('SELECT key,value FROM cc_meta'))
 out={'active':'migration-preview-r69','epoch':int(meta['epoch']),'release':{'records':records,'sources':{k:v[0] for k,v in pairs.items()}},'source_pairs':pairs,'withdrawn':[x[0] for x in c.execute('SELECT record_id FROM cc_heads WHERE withdrawn=1')],'evaluation_draft_only':True,'allow_demo':False}
 c.close();return out
def index():
 from app.knowledge.common.domain_flow.index import FactIndex
 from app.knowledge.common.domain_flow.projection import compile_snapshot
 return FactIndex(compile_snapshot(snapshot()))
