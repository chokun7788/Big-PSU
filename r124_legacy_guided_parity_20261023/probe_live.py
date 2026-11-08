"""On-demand connection probe; persist only public service/slot aggregates."""
import json,sys,time,urllib.request,csv,io,os
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S))
from app.calendar.service_calendar import today_bangkok
from app.booking.live_status import get_live_booking_status,reset_live_booking_cache
from booking_dashboard import server as dashboard
day=today_bangkok().isoformat();results={};catalog=[]
for mode in ('wordpress','dashboard'):
 os.environ['PSU_LIVE_BOOKING_FETCH_MODE']=mode;reset_live_booking_cache();start=time.monotonic()
 snap=get_live_booking_status(day)
 results[mode]={'snapshot':snap.as_public_dict(),'elapsed_sec':time.monotonic()-start}
 try:
  with urllib.request.urlopen(dashboard.SERVICES_CSV_URL,timeout=8) as f:
   raw=f.read(2000000).decode('utf-8-sig')
  catalog=[{k:str(v) for k,v in row.items() if k.lower() in {'id','name','duration'}} for row in csv.DictReader(io.StringIO(raw))]
 except Exception as exc:results[mode]['catalog_fetch_error']=type(exc).__name__+': '+str(exc)
 if catalog:break
(R/'LIVE_CONNECTION_PROBE.json').write_text(json.dumps({'date':day,'results':results,'catalog':catalog,'personal_booking_data_saved':False},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'date':day,'transports':{k:{'ok':v['snapshot']['ok'],'error_code':v['snapshot'].get('error_code'),'resource_count':len(v['snapshot']['resources'])} for k,v in results.items()},'catalog_entries':len(catalog)},ensure_ascii=False,indent=2))
