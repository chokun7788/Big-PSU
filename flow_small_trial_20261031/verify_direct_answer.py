"""Focused direct-answer ordering against isolated source; no HTTP or model."""
import copy,json,os,sqlite3,sys,time
from pathlib import Path
from unittest.mock import patch
W=Path(__file__).resolve().parent;sys.path.insert(0,str(W/'system'))
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
o=W/('direct_answer_check_'+str(time.time_ns()));o.mkdir()
src=sqlite3.connect((W/'system/data/knowledge/trial.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
dst=sqlite3.connect(o/'source.sqlite');src.backup(dst);dst.close();src.close()
os.environ['PSU_CONVERSATION_STATE_PATH']=str(o/'sessions.sqlite')
v=DraftSnapshotView(CommonStore(o/'source.sqlite'))
qs=['ยกเลิกการจองยังไง อะ ช่วยแนบแหล่งข้อมูลด้วย','How do I cancel my booking?','ยกเลิกการจองอย่างไร และราคา PC เท่าไหร่','ต้องยกเลิกการจองล่วงหน้ากี่ชั่วโมง','How do I book a PC?']
rows=[]
for q in qs:
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):
  x=CommonAnswerer(v).answer(q,locale='auto',at='2026-10-16T12:00:00+07:00',planner=None)
 rows.append({'question':q,'answer':x.answer if x else None,'artifact':x.decision_artifact if x else None})
(o/'DETAILS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
checks={'thai_cancel_direct_first':rows[0]['answer'].startswith('ขั้นตอนการยกเลิกการจองยังไม่ยืนยัน'),
 'english_cancel_direct_first':rows[1]['answer'].startswith('The cancellation procedure is not confirmed'),
 'compound_price_preserved':('ขั้นตอนการยกเลิกการจองยังไม่ยืนยัน' in rows[2]['answer'] and bool(rows[2]['artifact'].get('domain_flow',{}).get('typed_claims'))),
 'deadline_no_wrong_procedure_notice':'ขั้นตอนการยกเลิกการจองยังไม่ยืนยัน' not in rows[3]['answer'],
 'booking_no_wrong_cancel_notice':'cancellation procedure is not confirmed' not in rows[4]['answer'].lower()}
record=copy.deepcopy(v.snapshot()['release']['records']['procedure_change_time'])
record['fields']['topic']['value']='cancel_booking'
record['fields']['name']['value']={'th':'วิธียกเลิกการจอง','en':'Cancel a booking'}
record['fields']['preconditions']['value']=[]
record['fields']['steps']['value']=[{'order':1,'contact_id':None,'instruction':{'th':'ทดสอบยกเลิกผ่าน PORTAL.TEST','en':'Cancel using PORTAL.TEST'}}]
record['aliases']={'th':['วิธียกเลิกการจอง'],'en':['Cancel a booking']}
save_owner_record(v.store,record,record['revision'],'isolated-cancel-fixture')
with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):
 x=CommonAnswerer(v).answer('How do I cancel my booking?',locale='auto',at='2026-10-16T12:00:00+07:00',planner=None)
checks['valid_edited_procedure_retained']=bool(x and 'PORTAL.TEST' in x.answer and 'cancellation procedure is not confirmed' not in x.answer.lower())
report={'checks':checks,'all_passed':all(checks.values()),'scope':'source-only copied snapshot, no HTTP/model, no semantic authority or actual transaction'}
(o/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'path':str(o),**report},ensure_ascii=False))
