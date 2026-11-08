from pathlib import Path
import json, sys, time, urllib.request, uuid

report = Path(Path(__file__).with_name('r22_report_path.txt').read_text(encoding='utf-8'))
port = int(sys.argv[1])
run = sys.argv[2]
base = f'http://127.0.0.1:{port}'
health = json.load(urllib.request.urlopen(base+'/health', timeout=5))
assert health['runtime']['version'] == '2026.10.01-on-demand-booking-r22', health['runtime']
assert health['runtime']['booking'] == {'enabled':True,'fetch_mode':'wordpress','cache_seconds':0.0,'dashboard_required':False,'read_only':True}
cases = [
 ('original-th','th','ตนนี้ pc ว่างให้เล่นไหม',True,['PC #01','PC #10']),
 ('typo-en','en','Is cockpik available now?',True,['Cockpit']),
 ('slots-th','th','วันนี้มีช่วงไหนให้จองบ้าง',True,['09:00-10:00','12:00-13:00','15:00-16:00']),
 ('slots-en','en','What PC slots can I book tomorrow?',True,['09:00-10:00','12:00-13:00','PC Zone']),
 ('procedure-th','th','จอง PC ยังไง',False,[]),
 ('price-en','en','How much does PC cost?',False,[]),
]
records=[]
for key,locale,query,live,required in cases:
 payload={'question':query,'locale':locale,'client_session_id':'r22-'+uuid.uuid4().hex,'recent_history':[],'experimental_allow_llm':True,'experimental_rag_fallback':True,'debug':True}
 request=urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode('utf-8'),{'Content-Type':'application/json; charset=utf-8'})
 started=time.perf_counter()
 response=json.load(urllib.request.urlopen(request,timeout=25))
 elapsed=round(time.perf_counter()-started,4)
 trace=response.get('trace',[])
 live_events=[t for t in trace if t['stage']=='live_booking_status']
 failure=[]
 if live:
  if response.get('mode')!='pipeline:live_booking_status_fast_path':failure.append('wrong live mode')
  if not live_events:failure.append('missing live trace')
  elif live_events[-1]['metadata'].get('transport')!='wordpress' or live_events[-1]['metadata'].get('cached') is not False:failure.append('not fresh direct WordPress')
 elif live_events:failure.append('static question fetched live slots')
 for term in required:
  if term not in response.get('answer',''):failure.append('missing '+term)
 if elapsed>20:failure.append('latency exceeds target')
 records.append({'case':key,'question':query,'locale':locale,'http_wall_sec':elapsed,'failures':failure,'response':response})
 print(json.dumps({'case':key,'mode':response.get('mode'),'wall_sec':elapsed,'failures':failure,'booking_trace':live_events,'answer':response.get('answer','')[:800]},ensure_ascii=False))
result={'health':health,'cases':records,'passed':sum(not r['failures'] for r in records),'total':len(records)}
(report/f'http_{run}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
if result['passed'] != result['total']:sys.exit(1)
