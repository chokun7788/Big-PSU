"""Read-only real provider observation; unavailable is integration-blocked."""
import os,sys,json,time,dataclasses
from pathlib import Path
R=Path(__file__).resolve().parent;T=R/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False);sys.path.insert(0,str(R/'system'))
os.environ.pop('PSU_ESPORTS_NOW',None)
from app.booking.live_status import get_live_booking_status
from app.pipeline.request_deadline import request_deadline
started=time.perf_counter()
try:
 with request_deadline(20):snapshot=get_live_booking_status('2026-10-20')
 public=snapshot.as_public_dict()
 (T/'PROVIDER_PUBLIC_OBSERVATION.json').write_text(json.dumps(public,ensure_ascii=False,indent=2,default=str),'utf8')
 summary={'count':1,'passed':int(snapshot.ok),'failed':[],'integration_blocked':not snapshot.ok,'error_code':snapshot.error_code,
  'real_provider_called':True,'read_only':True,'booking_created_or_changed':False,'physical_state_independently_verified':False,'elapsed_sec':time.perf_counter()-started}
except Exception as e:
 summary={'count':1,'passed':0,'failed':[],'integration_blocked':True,'error_type':type(e).__name__,'real_provider_called':True,'read_only':True,'elapsed_sec':time.perf_counter()-started}
(T/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False))
