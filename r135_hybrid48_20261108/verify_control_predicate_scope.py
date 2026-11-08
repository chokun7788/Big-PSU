"""Retained button/function sources versus unrequested console usage."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.native_intents import propose
from app.knowledge.common.domain_flow.control_intent import request
from app.knowledge.common.domain_flow.request_verifier import observe
O=R/('control_predicate_scope_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close()
store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);original=view.snapshot();checks={};details=[]
def run(q,locale='auto',source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(source or view).answer(q,locale=locale,at='2026-10-27T10:00:00+07:00',planner=None)
 c=r.decision_artifact['execution_contract'];tasks=c['request_plan']['tasks'];details.append({'q':q,'answer':r.answer,'artifact':r.decision_artifact});return r,tasks
cases=[('plus','ในเกม Super Mario Odyssey บน Nintendo Switch ปุ่ม + (Plus) ใช้ทำอะไร','controls_nintendo_super_mario_odyssey','หยุดเกม'),('a','ในเกม Super Smash Bros. Ultimate บน Nintendo Switch ปุ่ม A ใช้ทำอะไร','controls_nintendo_super_smash_bros_ultimate','โจมตี'),('triangle','ในเกม Resident Evil 4 บน PlayStation / PS5 ปุ่ม Triangle ใช้ทำอะไร','controls_ps5_resident_evil_4_remake','คลังไอเทม')]
for name,q,rid,action in cases:
 r,tasks=run(q);checks[name+'_one_requested_controls_task']=len(tasks)==1 and tasks[0]['category']=='C05'
 checks[name+'_actual_binding_and_scope_caveat']=action in r.answer and rid in json.dumps(r.decision_artifact) and 'แหล่งรอง' in r.answer
 checks[name+'_no_unrequested_equipment_usage']='TV 86' not in r.answer and 'ครอบครัว' not in r.answer and not any(t['category']=='C03' for t in tasks)
 e=Engine.from_snapshot(original);seen=observe(e.index,q);checks[name+'_independent_observer_no_console_need']=all(n['category']=='C05' for n in seen['needs']) and bool(seen['needs'])
r,tasks=run('What does the A button do in Super Smash Bros. Ultimate on Nintendo Switch?');checks['english_button_function_same_scope']=len(tasks)==1 and tasks[0]['category']=='C05' and 'Attack' in r.answer
q='What is Nintendo Switch OLED used for?';r,tasks=run(q);checks['real_equipment_usage_preserved']=any(t['category']=='C03' for t in tasks) and 'family' in r.answer and request(e.index,q) is None
q='What does the + (Plus) button do in Super Mario Odyssey on Nintendo Switch; what is Nintendo Switch OLED used for?';r,tasks=run(q);checks['genuine_independent_controls_and_usage_both_retained']={t['category'] for t in tasks}=={'C05','C03'} and 'Pause' in r.answer and 'family' in r.answer
for text in ['What is Nintendo Switch OLED used for?','What equipment is in PC Zone?','Are button remaps allowed in the Tekken8 tournament?','How much is playing Super Mario Odyssey?']:
 checks['other_predicate_not_control_'+str(len(checks))]=request(e.index,text) is None
class MissingControls:
 path=view.path
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'].pop('controls_nintendo_super_mario_odyssey');s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
r,tasks=run(cases[0][1],source=MissingControls());checks['missing_control_source_does_not_become_console_usage']=len(tasks)==1 and tasks[0]['category']=='C05' and 'TV 86' not in r.answer and 'ครอบครัว' not in r.answer
checks['missing_control_source_does_not_invent_binding']='หยุดเกม' not in r.answer
r,tasks=run('ในเกม Super Mario Odyssey บน PS5 ปุ่ม + (Plus) ใช้ทำอะไร');checks['wrong_platform_not_equipment_or_switch_binding']=len(tasks)==1 and tasks[0]['category']=='C05' and 'หยุดเกม' not in r.answer and 'TV 86' not in r.answer
record=copy.deepcopy(original['release']['records']['controls_nintendo_super_mario_odyssey']);binding=next(b for b in record['fields']['bindings']['value'] if '+ (Plus)' in b['buttons']);binding['action']={'th':'การกระทำจากแหล่งควบคุมที่แก้แล้ว','en':'Edited controlled-source action'};binding['notes']={'th':None,'en':None};save_owner_record(store,record,record['revision'],'isolated-source-control')
r,tasks=run(cases[0][1]);checks['actual_owner_source_edit_changes_binding_answer']='การกระทำจากแหล่งควบคุมที่แก้แล้ว' in r.answer and 'หยุดเกม' not in r.answer and len(tasks)==1
report={'all_passed':all(checks.values()),'checks':checks,'actual_HTTP_or_model_inferences':0,'actual_owner_or_frozen_source_modified':False,'control_layout_or_currentness_semantics_fully_accepted':False,'scope':'Native predicate/source controls; final model/source/API category acceptance remains.'}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks),'failed':[k for k,v in checks.items() if not v]}));assert report['all_passed']
