"""Bounded damage-scenario retrieval; source wording remains conditional."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('damage_condition_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite');a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);b.close();a.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP/model forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-27T10:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
q1='Please use verified studio information: What am I responsible for if the Cockpit wheel breaks?';q2='ถ้าทำเครื่อง Nintendo Switch ตกจะมีค่าปรับไหม'
a=run(q1);checks['wheel_policy_retrieved_with_applicability_unresolved']=bool(a and 'migrated_faq_rule_damage_responsibility' in json.dumps(a.decision_artifact) and 'unverified' in a.answer.lower() and 'without the player causing' in a.answer)
b=run(q2);checks['drop_policy_retrieved_without_asserting_fixed_fine']=bool(b and 'migrated_faq_rule_damage_responsibility' in json.dumps(b.decision_artifact) and ('ยืนยัน' in b.answer or 'เงื่อนไข' in b.answer))
c=run('What games are available on Nintendo Switch?');checks['catalog_not_damage_policy']=bool(c and '100-500 THB' not in c.answer and 'ค่าปรับ' not in c.answer)
d=run('What if the wheel breaks by itself without any user action?');checks['no_invented_user_cause']=d is None or 'you caused' not in d.answer.lower()
rid='migrated_faq_rule_damage_responsibility';record=copy.deepcopy(view.snapshot()['release']['records'][rid]);field=record['fields']['answer']['value'];field['th']+=' เงื่อนไขทดสอบแหล่งข้อมูล';field['en']+=' Controlled source condition.';save_owner_record(store,record,record['revision'],'isolated-damage-source-control');e=run(q2);checks['edited_source_visible']=bool(e and ('เงื่อนไขทดสอบแหล่งข้อมูล' in e.answer or 'Controlled source condition' in e.answer))
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['answer']['value']['th']='ค่าปรับปลอมแน่นอน';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
f=run(q2,Forged());checks['unattested_source_not_delivered']=f is None or 'ค่าปรับปลอมแน่นอน' not in f.answer
report={'all_passed':all(checks.values()),'checks':checks,'actual_http_or_model_calls':0,'actual_owner_frozen_data_modified':False,'full_damage_authority_or_condition_resolved':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':checks},ensure_ascii=False));assert report['all_passed']
