import copy,json,os,sqlite3,sys,time
from pathlib import Path
from unittest.mock import patch
W=Path(__file__).resolve().parent;R=W.parent;sys.path.insert(0,str(W/'system'))
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=W/('address_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);a.close();b.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-29T17:45:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
def answer(q,source=None):
 r=run(q,source);return r.answer if r else ''
a=answer('ศูนย์ตั้งอยู่ที่ไหน');checks['center_address']=bool('อาคาร 5' in a and 'ชั้น 1' in a)
a=answer('ราคา PC เท่าไหร่');checks['price_not_replaced']=bool('บาท' in a and 'อาคาร 5' not in a)
a=answer('ศูนย์ตั้งอยู่ที่ไหน และราคา PC เท่าไหร่');checks['compound_retains_both']=bool('อาคาร 5' in a and 'บาท' in a)
a=answer('Where is the studio contact email address?');checks['email_not_physical_address']=bool('@' in a and 'Building 5' not in a)
a=answer('What is the studio email address and also what is its physical address?');checks['email_and_physical_address']=bool('@' in a and 'Building 5' in a)
rid='center_psu_phuket';record=copy.deepcopy(view.snapshot()['release']['records'][rid]);record['fields']['address']['value']['th']='ที่อยู่ทดลอง CONTROLLED ADDRESS';save_owner_record(store,record,record['revision'],'isolated-address-control')
a=answer('ศูนย์ตั้งอยู่ที่ไหน');checks['actual_owner_edit']=bool('CONTROLLED ADDRESS' in a)
class Forged:
 path=view.path
 def connect(self):return store.connect()
 def snapshot(self):
  s=copy.deepcopy(view.snapshot());s['release']['records'][rid]['fields']['address']['value']['th']='FORGED ADDRESS';s['epoch']+=10000;return s
 def still_current(self,s):return s==self.snapshot()
a=answer('ศูนย์ตั้งอยู่ที่ไหน',Forged());checks['forged_snapshot_not_delivered']='FORGED ADDRESS' not in a
report={'checks':checks,'all_passed':all(checks.values()),'http_or_model':False,'source_edit':'isolated copy only','semantic_or_publication_authority_verified':False}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n',encoding='utf8');(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps({'path':str(O),**report},ensure_ascii=False))
