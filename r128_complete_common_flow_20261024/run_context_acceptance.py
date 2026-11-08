"""Actual HTTP checks for count, exclusion, rental and live-window state."""
import json,time,urllib.request,uuid
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'));out=Path(c['output']);rows=[];checks={}
cases={
 'mixed_counts':['นักศึกษา PSU 1 คนกับบุคคลทั่วไป 2 คน เล่น PC 2 ชั่วโมง ราคาเท่าไหร่','แล้วสามชั่วโมงล่ะ','ไม่ใช่ PC เปลี่ยนเป็น PS5 ล่ะ'],
 'rental':['ราคาเหมา PC เต็มวัน หน่วยงานภายใน','แล้วครึ่งวันล่ะ'],
 'live_window':['PC2 วันที่ 27 ตุลาคม 2026 เวลา 15:00-16:00 ว่างไหม','แล้ว PC3 ล่ะ'],
 'topic_after_price':['บุคคลทั่วไปเล่น PC 1 ชั่วโมงราคาเท่าไหร่','PS5 มีปุ่มอะไรบ้าง'],
}
for kind,qs in cases.items():
 session='r128-extra-'+uuid.uuid4().hex;last=''
 for turn,q in enumerate(qs,1):
  request={'question':q,'locale':'th','debug':True,'experimental_rag_fallback':True,'client_session_id':session,'client_turn_id':'turn-'+uuid.uuid4().hex,'last_seen_response_id':last};t=time.perf_counter()
  req=urllib.request.Request(c['url']+'/api/chat',json.dumps(request,ensure_ascii=False).encode(),{'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=195) as f:response=json.load(f)
  row={'kind':kind,'turn':turn,'question':q,'wall_sec':time.perf_counter()-t,'response':response};rows.append(row);last=response.get('request_id','')
  with (out/'CONTEXT_ACCEPTANCE.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
  print(json.dumps({'kind':kind,'turn':turn,'answer':response.get('answer','')[:350],'sec':row['wall_sec']},ensure_ascii=False),flush=True)
def answer(kind,turn):return next(r['response']['answer'] for r in rows if r['kind']==kind and r['turn']==turn)
checks['mixed_two_hours_total_280']='280' in answer('mixed_counts',1)
checks['mixed_three_hours_total_420']='420' in answer('mixed_counts',2)
checks['platform_replacement_keeps_counts_and_duration']='900' in answer('mixed_counts',3) and '**PC /' not in answer('mixed_counts',3)
checks['rental_period_replaced']=answer('rental',1)!=answer('rental',2) and ('ครึ่งวัน' in answer('rental',2) or 'half_day' in answer('rental',2))
checks['live_preserves_date_window']='2026-10-27' in answer('live_window',2) and '15:00-16:00' in answer('live_window',2)
checks['control_topic_not_answered_as_price']='บาท' not in answer('topic_after_price',2)
result={'all_passed':all(checks.values()),'checks':checks,'requests':len(rows),'full_test':False};(out/'CONTEXT_COMPLETE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8');print(json.dumps(result,ensure_ascii=False,indent=2));assert result['all_passed']
