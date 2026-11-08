import faulthandler,json,os,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
os.environ.update(PSU_LOCAL_LLM_ASSIST_ENABLED='0',PSU_ESPORTS_NOW='2026-10-21T12:00:00+07:00')
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.store import CommonStore
from app.knowledge.common.answer import CommonAnswerer
from app.pipeline.request_deadline import request_deadline
faulthandler.dump_traceback_later(20,repeat=True)
a=CommonAnswerer(DraftSnapshotView(CommonStore(R/'system/data/knowledge/common.sqlite')))
questions=sys.argv[1:] or ['วันนี้เปิดไหม','PS5 มีกี่จอย','โอนขาดไป ต้องส่งสลิปเพิ่มยังไง','เปลี่ยนเวลาจองได้ไหม','PC99 ตอนนี้ว่างไหม','Nintendo Switch มีเกมอะไรบ้าง','ต้องจองก่อนไหม']
for q in questions:
    print('START '+q,flush=True);started=time.perf_counter()
    with request_deadline(12):x=a.answer(q,locale='th')
    print(json.dumps({'q':q,'a':x.answer[:1600] if x else None,'validation':x.validation.ok if x else None,'domain':x.decision_artifact.get('domain_flow',{}).get('path') if x else None,'seconds':round(time.perf_counter()-started,3)},ensure_ascii=False),flush=True)
faulthandler.cancel_dump_traceback_later()
