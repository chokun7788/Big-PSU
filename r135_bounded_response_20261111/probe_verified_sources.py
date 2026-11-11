import json,time
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.web_api.server import _source_list

view=MigratedView(R/'system/data/knowledge/verified_sources.sqlite');snap=view.snapshot()
class Pinned:
 path=view.path
 def snapshot(self):return snap
 def still_current(self,s):return True
 def connect(self,**kw):return view.connect(**kw)
reader=CommonAnswerer(Pinned());out=R/('verified_source_probe_'+str(time.time_ns()));out.mkdir();rows=[]
for q,lang in [('จองได้สูงสุดกี่รอบ','th'),('How many sessions can I book in one booking?','en'),('จองได้สูงสุดกี่ session และต้องจ่ายภายในกี่นาที','th'),('โรงแรมอันดามันจองได้สูงสุดกี่รอบ','th'),('How many sessions can I book at Andaman Hotel?','en'),('PC นักศึกษา PSU ราคาเท่าไหร่ แล้วจองได้สูงสุดกี่รอบ','th')]:
 result=reader.answer(q,locale=lang,planner=None)
 rows.append({'question':q,'answer':result.answer,'mode':result.mode,'sources':_source_list(result.hits),'artifact':result.decision_artifact})
 print(json.dumps({'question':q,'answer':result.answer[:1000],'sources':_source_list(result.hits)},ensure_ascii=False),flush=True)
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print('OUTPUT',out)
