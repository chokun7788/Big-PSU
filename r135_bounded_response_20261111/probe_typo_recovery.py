import json,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
view=MigratedView(R/'system/data/knowledge/verified_sources.sqlite');snap=view.snapshot()
class Pinned:
 path=view.path
 def snapshot(self):return snap
 def still_current(self,s):return True
 def connect(self,**kw):return view.connect(**kw)
reader=CommonAnswerer(Pinned());out=R/('typo_probe_'+str(time.time_ns()));out.mkdir();rows=[]
for q in ['มีเกมอะไรบ้าง','มีเกสอะไรบ้าง','มีเกอะไรบ้าง','มีเกมมอะไรบ้าง','มีเกมอะไรบ้างง','มีอะไรบ้าง','PC นักศึกษา PSU ราคเท่าไหร่']:
 with patch('urllib.request.urlopen',side_effect=AssertionError('No HTTP/model')):r=reader.answer(q,locale='th',planner=None)
 a=r.decision_artifact or {};rows.append({'q':q,'answer':r.answer,'artifact':a,'hits':r.hits})
 print(json.dumps({'q':q,'answer':r.answer[:240],'mode':r.mode,'hit_count':len(r.hits),'recovery':a.get('intent_edit_recovery',{}).get('status'),'contract':a.get('execution_contract',{}).get('path')},ensure_ascii=False),flush=True)
 (out/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print('OUTPUT',out)
