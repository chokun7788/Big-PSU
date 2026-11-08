import copy,json,os,sqlite3,sys,time
from pathlib import Path
from unittest.mock import patch
W=Path(__file__).resolve().parent;R=W.parent;sys.path.insert(0,str(W/'system'))
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.owner_server import save_owner_record
O=W/('booking_compound_controls_'+str(time.time_ns()));O.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'sessions.sqlite')
a=sqlite3.connect((R/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True);b=sqlite3.connect(O/'source.sqlite');a.backup(b);a.close();b.close();store=CommonStore(O/'source.sqlite');view=DraftSnapshotView(store);details=[];checks={}
def run(q,source=None):
 with patch('urllib.request.urlopen',side_effect=AssertionError('HTTP forbidden')):r=CommonAnswerer(source or view).answer(q,locale='auto',at='2026-10-29T17:45:00+07:00',planner=None)
 details.append({'question':q,'answer':r.answer if r else None,'artifact':r.decision_artifact if r else None});return r
def answer(q,source=None):
 r=run(q,source);return r.answer if r else ''

for label,q in [('th','ราคา PC เท่าไหร่และจองอย่างไร'),('en','How much does PC cost and how do I book it?'),('address','ศูนย์ตั้งอยู่ที่ไหน และจอง PC อย่างไร')]:
 r=run(q);a=r.answer if r else '';art=r.decision_artifact if r else {};rows=art.get('need_results',[]);claims=[c for n in rows for c in n.get('claim_packets',[])]
 booking=[c for c in claims if c.get('record_id')=='migrated_faq_curated_booking_steps'];checks[label+'_booking_claim']=bool(booking)
 checks[label+'_validity_notice']=('ช่วงที่ขั้นตอนการจองมีผลยังไม่ยืนยัน' in a) if label!='en' else ('effective period' in a.lower() and 'unconfirmed' in a.lower())
 checks[label+'_other_task_claim']=any(c.get('record_id','').startswith('rate_recovered_pc_') for c in claims) if label!='address' else any(c.get('record_id')=='center_psu_phuket' and c.get('facet')=='address' for c in claims)
report={'checks':checks,'all_passed':all(checks.values()),'scope':'three compound source-only requests; actual copied draft, no HTTP/model; claims plus disclosure checks, not semantic or source authority proof'}
(O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),encoding='utf8');(O/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(json.dumps({'path':str(O),**report}))
