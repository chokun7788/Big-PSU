import json,sys,os
from pathlib import Path
R=Path(__file__).resolve().parent;S=R.parent/'r125_date_context_presentation_20261023/system';sys.path.insert(0,str(S));os.environ['PSU_KNOWLEDGE_DB']=str(S/'data/knowledge/common.sqlite')
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.meaning_review import review
from app.knowledge.common.domain_flow.understanding import Understanding
engine=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot())
rows=[]
for q in ['Beat Saber คืออะไร','Beat Saber คือเกมอะไร','Tekken 8 คืออะไร','Tekken 8 คือเกมอะไร','PC กับ PS5 มีเกมอะไรบ้าง','PC มีเกมอะไรบ้าง','PS5 มีเกมอะไรบ้าง']:
 row={'question':q,'bindings':{cat:sorted({f['record_id'] for f in engine.index.bind(cat,q)}) for cat in ['C03','C04']},'native_review':review(q,engine.index,Understanding(reason='native_source_frame_before_model',event={'http_attempted':False,'model_called':False})).as_dict()};rows.append(row)
(R/'SOURCE_COUNTERFACTUALS.json').write_text(json.dumps({'read_only':True,'model_calls':0,'cases':rows},ensure_ascii=False,indent=2),'utf8');print(json.dumps(rows,ensure_ascii=False))
