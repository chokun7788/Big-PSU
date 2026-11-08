"""End-to-end delivered state, current clock, formatting and measured latency."""
import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;config=json.loads((R/'LIVE_API_PROCESS.json').read_text('utf8'));OUT=Path(config['output']);rows=[];sessions={}
for attempt in range(30):
 try:
  with urllib.request.urlopen(config['url']+'/health',timeout=2) as response:health=json.load(response)
  break
 except OSError:
  if attempt==29:raise
  time.sleep(1)
assert health['runtime']['profile']=='r125-date-context-live'
with urllib.request.urlopen(config['url']+'/api/calendar',timeout=5) as response:calendar=json.load(response)
(OUT/'CALENDAR_API.json').write_text(json.dumps(calendar,ensure_ascii=False,indent=2),'utf8')
work=[('date26','วันที่ 26 ตุลาเปิดไหม'),('date27','วันที่27เปิดไหม'),('bare27','27ศูนย์เปิดไหม'),('month','วันที่15เปิดไหม'),('month','เดือน11'),('live_month','วันที่15ว่างไหม'),('live_month','พฤศจิกายน'),('live_month','PC2'),('unscoped','วันนี้มีตารางว่างรึเปล่า'),('games','มีเกมอะไรมั่ง'),('price','บุคคลทั่วไป เล่น PC 1 ชั่วโมง เสียกี่บาท'),('controls','God of War Ragnarök ปุ่มทั้งหมดมีอะไรบ้าง'),('equipment','Nintendo Switch OLED คืออะไร')]
for group,q in work:
 session=sessions.setdefault(group,{'id':'r125-'+uuid.uuid4().hex,'last':None})
 payload={'question':q,'locale':'th','debug':True,'experimental_rag_fallback':True,'client_session_id':session['id'],'client_turn_id':'turn-'+uuid.uuid4().hex,'last_seen_response_id':session['last']}
 before=time.perf_counter();req=urllib.request.Request(config['url']+'/api/chat',json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=120) as response:body=json.load(response)
 elapsed=time.perf_counter()-before;session['last']=body['request_id']
 rows.append({'group':group,'question':q,'wall_sec':elapsed,'response':body})
 (OUT/'API_RESULTS.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'question':q,'elapsed':elapsed,'answer':body['answer'][:180]},ensure_ascii=False),flush=True)
by={r['question']:r for r in rows}
def text(q):return by[q]['response']['answer']
checks={'all_13_http_requests_succeeded':len(rows)==13,
 'explicit_oct26_answered_monday':all(s in text('วันที่ 26 ตุลาเปิดไหม') for s in ['วันจันทร์ที่ 26 ตุลาคม','13:00–16:00']),
 'current_month_day27':all(s in text('วันที่27เปิดไหม') for s in ['27 ตุลาคม','เปิดให้บริการ']),
 'leading_day_not_live_unsupported':'27 ตุลาคม' in text('27ศูนย์เปิดไหม') and 'unsupported' not in text('27ศูนย์เปิดไหม'),
 'past_day_asks_month':'เดือนไหน' in text('วันที่15เปิดไหม'),
 'month_reply_uses_day15':'15 พฤศจิกายน' in text('เดือน11'),
 'live_day_asks_month_first':'เดือนไหน' in text('วันที่15ว่างไหม'),
 'live_month_reply_asks_only_resource':'เครื่องหรือบริการใด' in text('พฤศจิกายน') and 'วันที่เท่าไร' not in text('พฤศจิกายน'),
 'resource_reply_keeps_resolved_date':bool(by['PC2']['response'].get('decision_artifact',{}).get('live_booking')) and '2026-11-15' in text('PC2'),
 'unscoped_live_no_date_reask':'เครื่องหรือบริการใด' in text('วันนี้มีตารางว่างรึเปล่า'),
 'game_catalog_has_bullets':'\n- ' in text('มีเกมอะไรมั่ง'),
 'control_subject_once':text('God of War Ragnarök ปุ่มทั้งหมดมีอะไรบ้าง').count('**God of War Ragnarök / PlayStation / PS5**')==1,
 'price_keeps_70':'70 บาท' in text('บุคคลทั่วไป เล่น PC 1 ชั่วโมง เสียกี่บาท'),
 'equipment_grouped':'**Nintendo Switch OLED**' in text('Nintendo Switch OLED คืออะไร')}
events=[json.loads(s) for s in (OUT/'MODEL_TRANSPORT.jsonl').read_text('utf8').splitlines()] if (OUT/'MODEL_TRANSPORT.jsonl').exists() else []
generation=[e for e in events if '/api/chat' in e['url'] or '/api/generate' in e['url']]
checks['no_generation_for_clear_retained_requests']=not generation
summary={'all_passed':all(checks.values()),'checks':checks,'requests':len(rows),'model_generation_calls':len(generation),'calendar_api':calendar,'latencies':[{k:r[k] for k in ['question','wall_sec']} for r in rows],'output':str(OUT),'full_test':False}
(OUT/'API_VERIFICATION.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False,indent=2));assert summary['all_passed']
