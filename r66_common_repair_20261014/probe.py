import os,sys,json,time
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B),str(B/'system')]
from harness import configure,offline_booking,test_temp
test_temp('probe');configure('common',False);offline_booking()
from app.knowledge.common.store import CommonStore
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.registry import value
a=CommonAnswerer(CommonStore(B/'common.sqlite'))
queries=[
 ('Counter-Strike 2 แข่งจริง กฎเกี่ยวกับแผนที่และการเลือกแผนที่ เป็นแบบไหน','th'),
 ('TEKKEN 8 การแก้ข้อพิพาททำยังไง','th'),
 ('What are the dispute rules for TEKKEN 8?','en'),
 ('Mario Kart 8 Deluxe ปุ่มเร่งเครื่องกดอะไร','th'),
 ('What buttons accelerate in Mario Kart 8 Deluxe?','en'),
 ('What is the price of Counter-Strike 2?','en'),
 ('General Adult เล่น PC 30 นาที เสียกี่บาท','th'),
 ('PS5 มีเกมอะไรบ้าง','th'), ('PC มีเกมอะไรบ้าง','th'),
 ('กฎตอนแข่ง rov มีอะไรบ้าง','th'),
 ('How do I book a PC?','en'),('PC สเปกอะไร','th'),
 ('cockpik ว่างไหม','th'),('สวัาดี','th'),
]
out=[]
for q,lang in queries:
 start=time.perf_counter()
 try:
  r=a.answer(q,locale=lang)
  row={'question':q,'locale':lang,'elapsed':time.perf_counter()-start,'result':None if r is None else {'answer':r.answer,'mode':r.mode,'validation':r.validation.ok,'artifact':r.decision_artifact}}
 except Exception as e:row={'question':q,'exception':repr(e)}
 out.append(row);print(json.dumps({**row,'result':None if not row.get('result') else {**row['result'],'answer':row['result']['answer'][:1100],'artifact':{k:row['result']['artifact'].get(k) for k in ('coverage_errors','query_plan')}}},ensure_ascii=False),flush=True)
(B/('PROBE_'+str(len(list(B.glob('PROBE_*.json')))+1).zfill(2)+'.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
