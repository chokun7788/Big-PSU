import json,statistics,sys,time,urllib.request
from pathlib import Path
report=Path(Path(__file__).with_name('r26_report_path.txt').read_text(encoding='utf-8').strip())
base='http://127.0.0.1:'+sys.argv[1];run=sys.argv[2]
health=json.load(urllib.request.urlopen(base+'/health',timeout=2))
queries=[
 ('rov-original','สอบถามหน่อยครับ กติกา RoV เรื่องการหลุดจากเกมหรือการเชื่อมต่อ ว่าอย่างไร ครับ','rov_blueket_2025_men'),
 ('tekken-original','สอบถามหน่อยครับ ขออ้างอิงกติกา เทคเค่น 8 ในหัวข้อการตั้งค่าในเกม หน่อย ครับ','tekken8_psu_esports'),
 ('rov-preface','ขอสอบถามหน่อยนะครับ กติกา RoV เรื่องการหลุดจากเกมหรือการเชื่อมต่อ ว่าอย่างไร ครับ','rov_blueket_2025_men'),
 ('tekken-preface','ขอสอบถามหน่อยนะครับ ขออ้างอิงกติกา เทคเค่น 8 ในหัวข้อการตั้งค่าในเกม หน่อย ครับ','tekken8_psu_esports'),
]
records=[]
for repetition in range(3):
 for key,question,game in queries:
  payload={'question':question,'locale':'th','recent_history':[],'experimental_allow_llm':True,'experimental_rag_fallback':True,'debug':True}
  started=time.perf_counter()
  response=json.load(urllib.request.urlopen(urllib.request.Request(base+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'}),timeout=25))
  trace=response.get('trace') or response.get('debug',{}).get('trace') or []
  llm=any(t.get('stage')=='universal_intent' and t.get('metadata',{}).get('llm_attempted') for t in trace)
  skipped=any(t.get('decision')=='skipped_exact_competition_facet' for t in trace)
  failures=[]
  if response.get('route_category')!='competition_rules':failures.append('wrong category')
  if not response.get('sources') or any(game not in s.get('url','') for s in response['sources']):failures.append('wrong source')
  if key.startswith('tekken') and '60 วินาที' not in response['answer']:failures.append('settings content missing')
  if key.startswith('rov') and ('5 ครั้ง' not in response['answer'] or '1 นาที' not in response['answer']):failures.append('disconnect quota missing')
  record={'case':key,'repetition':repetition,'elapsed_sec':round(time.perf_counter()-started,4),'llm_intent_attempted':llm,'exact_facet_route_skipped':skipped,'failures':failures,'response':response}
  records.append(record)
  print(json.dumps({k:v for k,v in record.items() if k!='response'},ensure_ascii=False),flush=True)
summary={'runtime':health['runtime'],'total':len(records),'passed':sum(not r['failures'] for r in records),'median_sec':statistics.median(r['elapsed_sec'] for r in records),'max_sec':max(r['elapsed_sec'] for r in records),'llm_intent_attempts':sum(r['llm_intent_attempted'] for r in records),'route_skips':sum(r['exact_facet_route_skipped'] for r in records),'cases':records}
with (report/(run+'_speed.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in summary.items() if k!='cases'},ensure_ascii=False))
