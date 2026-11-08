"""Distinguish gaming equipment use from an independent game question."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('gaming_pc_usage_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);a.close();b.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(source or view).answer(q,locale='en',at='2026-10-16T12:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
q='What is the Gaming PC used for? Could you check this for me?';r=run(q);needs=r.decision_artifact.get('understanding',{}).get('event',{}).get('independent_request_observations',{}).get('needs',[]) if r else []
checks['equipment_usage_without_spurious_game_need']=bool(r and 'usage' in r.answer.lower() and not any(n['category']=='C04' for n in needs) and 'No confirmed source' not in r.answer)
r=run("What is the Gaming PC used for and also what kind of game is Luigi's Mansion 3?");checks['independent_game_question_preserved']=bool(r and 'gaming computers' in r.answer.lower() and 'action puzzle' in r.answer.lower())
rid='equipment_gaming_pc';record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['usage']['value']['en']+=' Controlled equipment source revision.';save_owner_record(store,record,record['revision'],'isolated-pc-usage-control');r=run(q);checks['actual_owner_edit_visible']=bool(r and 'Controlled equipment source revision' in r.answer)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['usage']['value']['en']='Forged equipment usage.';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
r=run(q,Forged());checks['unattested_usage_not_delivered']=r is None or 'Forged equipment usage' not in r.answer
report={'checks':checks,'all_passed':all(checks.values()),'http_or_inference':False,'owner_data_modified':False,'current_hardware_or_game_availability_proven':False};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n',encoding='utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps({'path':str(O),'checks':checks}));assert report['all_passed']
