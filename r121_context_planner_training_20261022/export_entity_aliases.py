import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parent/'r120_teacher_distillation_20261022/system'))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.projection import title
e=Engine.from_snapshot(MigratedView(R.parent/'r120_teacher_distillation_20261022/system/data/knowledge/common.sqlite').snapshot())
out=[]
for rid,r in e.index.records.items():
 if r['kind'] not in {'game','equipment_model','service','person','zone','audience','event'}:continue
 labels=[*title(r).values(),*sum(r.get('aliases',{}).values(),[])]
 out.append({'id':rid,'kind':r['kind'],'aliases':sorted({s for s in labels if s and len(s)>=2},key=len,reverse=True)})
(R/'SOURCE_ENTITY_ALIASES.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'alias_records':len(out),'facts_or_answers_exported':False}))
