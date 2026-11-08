import collections,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
e=Engine.from_snapshot(MigratedView(R/'system/data/knowledge/common.sqlite').snapshot())
rows=[]
for f in e.index.facts:
 if 'temp_suspension' in f['record_id'] or f['category']=='C13' and 'valorant' in f['record_id']:
  r=e.index.records[f['record_id']]
  rows.append({'fact_id':f['id'],'category':f['category'],'facet':f['facet'],'label':f['label'],'subject':f['subject'],'legacy_search':f.get('legacy_search'),'native_kind':r['kind'],'native_facet':r['fields'].get('facet'),'native_facets':r['fields'].get('facets')})
(R/'NATIVE_READER_INSPECTION.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8')
print('FACTS',len(e.index.facts));print(json.dumps([r for r in rows if 'temp_suspension' in r['fact_id']],ensure_ascii=False));print('PENALTY',json.dumps([r for r in rows if 'penalt' in str(r).lower() or 'บทลงโทษ' in str(r)],ensure_ascii=False)[:5000])
