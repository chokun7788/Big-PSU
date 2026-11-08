import copy,json,os,sqlite3,sys,time
from pathlib import Path
from unittest.mock import patch
W=Path(__file__).resolve().parent;R=W.parent;sys.path.insert(0,str(W/'system'))
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=W/('booking_validity_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);a.close();b.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-29T17:45:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
def answer(q,source=None):
 r=run(q,source);return r.answer if r else ''
q='จอง PC อย่างไร'
a=answer(q);checks['unknown_th_disclosed']='ช่วงที่ขั้นตอนการจองมีผลยังไม่ยืนยัน' in a
b=answer('How do I book PC?');checks['unknown_en_disclosed']='effective period' in b.lower() and 'unconfirmed' in b.lower()
rid='migrated_faq_curated_booking_steps';record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2026-12-31T23:59:59+07:00'};save_owner_record(store,record,record['revision'],'isolated-booking-validity')
a=answer(q);checks['valid_interval_no_false_notice']='ขั้นตอนการจอง' in a and 'ช่วงที่ขั้นตอนการจองมีผลยังไม่ยืนยัน' not in a
record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['validity']['effective_until']='2026-02-01T00:00:00+07:00';save_owner_record(store,record,record['revision'],'isolated-expired-booking')
a=answer(q);checks['expired_steps_not_presented']='แนบสลิป' not in a
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['answer']['value']['th']='FORGED BOOKING';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
a=answer(q,Forged());checks['forged_snapshot_not_delivered']='FORGED BOOKING' not in a
report={'checks':checks,'all_passed':all(checks.values()),'http_or_model':False,'source_edit':'isolated copy only','semantic_or_publication_authority_verified':False}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n',encoding='utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps({'path':str(O),**report},ensure_ascii=False))
