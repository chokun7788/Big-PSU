"""Read the frozen candidate snapshot; no requests and no data modifications."""
import json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
engine=Engine.from_snapshot(MigratedView(R/'system/data/knowledge/common.sqlite').snapshot())
facts=[]
for f in engine.index.facts:
 text=json.dumps(f,ensure_ascii=False)
 if f['category']=='C10' or f['category']=='C08' or f['category']=='C03' and re.search('Nintendo|Switch',text,re.I) or f['category']=='C05' and re.search('Tekken',text,re.I) or f['category']=='C04' and re.search('FINAL FANTASY XVI',text,re.I):facts.append(f)
out={'facts':facts,'records':{f['record_id']:engine.index.records[f['record_id']] for f in facts}}
(R/'CONTEXT_SOURCE_REVIEW.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'facts':len(facts),'by_category':{c:sum(f['category']==c for f in facts) for c in sorted({f['category'] for f in facts})}},ensure_ascii=False))
