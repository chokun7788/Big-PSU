"""Actual source scope controls for keyboard definitions, no model or HTTP."""
import copy,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=R/('mechanical_definition_scope_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);a.close();b.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-16T12:00:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
def unknown(r):
 if not r:return True
 return r.decision_artifact.get('query_plan',{}).get('terminal_state') in {'partial','missing_source','missing_input','unsupported'} or any(x.get('terminal_state') in {'partial','missing_source','missing_input','unsupported'} for x in r.decision_artifact.get('need_results',[]))
q='What is a mechanical keyboard? Explain it simply.';r=run(q);checks['definition_unverified_is_not_supported']=unknown(r)
r=run('คีย์บอร์ด mechanical คืออะไรแบบสั้น อธิบายข้อดีข้อเสียสั้น ๆ');checks['thai_definition_and_pros_cons_not_silently_supported']=unknown(r)
r=run('What is the Gaming Keyboard used for?');checks['actual_equipment_usage_preserved']=bool(r and 'Keyboard for controlling games' in r.answer)
rid='equipment_gaming_keyboard';record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['usage']['value']['en']+=' Isolated revised usage only.';save_owner_record(store,record,record['revision'],'isolated-keyboard-definition-control')
r=run(q);checks['usage_edit_does_not_prove_mechanical_definition']=unknown(r)
r=run('What is the Gaming Keyboard used for?');checks['usage_owner_edit_still_delivered']=bool(r and 'Isolated revised usage only' in r.answer)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['usage']['value']['en']='Forged mechanical definition.';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
r=run('What is the Gaming Keyboard used for?',Forged());checks['forged_usage_not_delivered']=r is None or 'Forged mechanical definition.' not in r.answer
result={'checks':checks,'all_passed':all(checks.values()),'http_or_inference':False,'owner_data_modified':False,'scope':'Isolated snapshot only. Does not establish complete definition coverage.'};(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n',encoding='utf8');(O/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps({'path':str(O),**result},ensure_ascii=False));assert result['all_passed']
