import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
reader=CommonAnswerer(MigratedView(R/'system/data/knowledge/common.sqlite'))
e=Engine.from_snapshot(reader.store.snapshot())
for f in e.index.facts:
 if any(s in json.dumps(f,ensure_ascii=False).casefold() for s in sys.argv[1:]):
  print(json.dumps(f,ensure_ascii=False))
for rid,r in e.index.records.items():
 if any(s in rid.casefold() for s in sys.argv[1:]):
  print('RECORD',json.dumps(r,ensure_ascii=False))
  for ref in r.get('fields',{}).get('answer',{}).get('evidence_refs',[]):
   print('SOURCE',json.dumps(reader.store.snapshot()['release']['sources'].get(ref['source_id']),ensure_ascii=False))
