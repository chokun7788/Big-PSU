"""Exact stick labels and named-game controller-use source controls."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.control_intent import request
O=R/('stick_controller_predicates_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close()
store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);original=view.snapshot();checks={};details=[]
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-27T10:00:00+07:00',planner=None)
 assert r is not None,q
 tasks=r.decision_artifact['execution_contract']['request_plan']['tasks'];details.append({'question':q,'answer':r.answer,'artifact':r.decision_artifact});return r,tasks
left='ในเกม Super Mario Odyssey บน Nintendo Switch ปุ่ม L (Left Stick) ใช้ทำอะไร'
r,t=run(left);checks['left_stick_exact_binding']=len(t)==1 and t[0]['category']=='C05' and 'เคลื่อนที่' in r.answer and 'L (Left Stick)' in r.answer
checks['left_stick_source_limits_retained']='แหล่งรอง' in r.answer and 'เวอร์ชันเกม' in r.answer
r,t=run('What does the L (Left Stick) button do in Super Mario Odyssey on Nintendo Switch?');checks['english_full_label_precedes_single_letter']='Move and run Mario' in r.answer and len(t)==1
r,t=run('ในเกม Super Mario Odyssey บน Nintendo Switch ปุ่ม L ใช้ทำอะไร');checks['bare_L_does_not_invent_stick_binding']='บังคับทิศทางการเดิน' not in r.answer
r,t=run('ในเกม Super Mario Odyssey บน Nintendo Switch ปุ่ม R3 (Click Right Stick) ใช้ทำอะไร');checks['R3_distinct_from_left_stick']='มุมมองบุคคลที่หนึ่ง' in r.answer and 'บังคับทิศทางการเดิน' not in r.answer
fort='Fortnite ใช้จอยยังไง';r,t=run(fort);checks['controller_use_not_game_catalog']=len(t)==1 and t[0]['category']=='C05' and 'Options' in r.answer and 'Marvel' not in r.answer
checks['partial_layout_caveat_retained']='ยังไม่มีผังปุ่มครบชุด' in r.answer and 'PlayStation / PS5' in r.answer
idx=Engine.from_snapshot(original).index
for i,q in enumerate(['เกมไหนใช้จอยได้บ้าง','Fortnite รองรับจอยไหม','What equipment is in PC Zone?','How much does Fortnite cost?','Fortnite tournament controller remaps allowed?']):checks['independent_predicate_not_control_'+str(i)]=request(idx,q) is None
checks['english_controller_use_recognized']=request(idx,'How do I use a controller in Fortnite?') is not None
class Missing:
 path=view.path
 def snapshot(self):
  s=copy.deepcopy(original);s['release']['records'].pop('controls_ps5_fortnite');s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
r,t=run(fort,Missing());checks['withdrawn_layout_no_catalog_or_constants']=len(t)==1 and t[0]['category']=='C05' and 'Options' not in r.answer and 'Marvel' not in r.answer
record=copy.deepcopy(original['release']['records']['controls_nintendo_super_mario_odyssey']);binding=next(b for b in record['fields']['bindings']['value'] if b['buttons']==['L (Left Stick)']);binding['action']={'th':'ทิศทางจากแหล่งที่แก้จริง','en':'Controlled edited stick action'};binding['notes']={'th':None,'en':None};save_owner_record(store,record,record['revision'],'isolated-stick-source-control')
r,t=run(left);checks['attested_source_change_controls_answer']='ทิศทางจากแหล่งที่แก้จริง' in r.answer and 'บังคับทิศทางการเดิน' not in r.answer
report={'all_passed':all(checks.values()),'checks':checks,'actual_HTTP_or_model_inferences':0,'actual_owner_or_frozen_source_modified':False,'whole_category_or_model_semantics_accepted':False}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
