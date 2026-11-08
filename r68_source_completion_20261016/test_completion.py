"""Targeted source and read-path checks; not a full benchmark or human review."""
import collections,hashlib,json,os,sys,time,re
from datetime import datetime
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B),str(B/'system')]
enabled=sys.argv[1]=='1';tag=sys.argv[2];db=B/(sys.argv[3] if len(sys.argv)>3 else 'candidate04.sqlite')
from harness import configure,test_temp,equivalent_name_pruning
test_temp(tag);configure('common',enabled,db=db);equivalent_name_pruning()
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,validate,pointer
from app.knowledge.common.answer import CommonAnswerer,title,named
from app.knowledge.common.rendering import enum_text
from app.knowledge.common.planner import plan_fields
from app.knowledge.common.owner_server import preview_answer
store=CommonStore(db);a=CommonAnswerer(store)
with store.connect() as c:rs=store.heads(c);sources=store.sources(c)
def read(rel):
 p=B/'source_snapshot'/rel
 return [json.loads(s) for s in p.read_text('utf-8-sig').splitlines() if s.strip()] if p.suffix=='.jsonl' else json.loads(p.read_text('utf-8-sig'))
cases=[]
def case(q,lang,need,group,forbidden=()):cases.append({'question':q,'locale':lang,'required':need,'group':group,'forbidden':forbidden})
for i,x in enumerate(read('data/sources/our_games_raw.jsonl')):
 norm=lambda s:re.sub(r'[^\w]','',s.casefold())
 r=next(r for r in rs.values() if r['kind']=='game' and norm(x['game']) in [norm(v) for v in (value(r,'title') or {}).values() if v])
 for lang in ('th','en'):
  q=x['game']+' คำบรรยายต้นฉบับ' if lang=='th' else 'What is the official description of '+x['game']+'?'
  expected=x['description'] if ('th' if any('\u0e00'<=c<='\u0e7f' for c in x['description']) else 'en')==lang else value(r,'official_description')[lang]
  case(q,lang,[expected,'2026-07-08'],'full_raw_description')
for x in read('data/curated/game_item_details.jsonl'):
 for lang in ('th','en'):
  q=x['game']+' ขอ venue_zone_ids' if lang=='th' else 'List venue inventory zones for '+x['game']
  case(q,lang,x['zones'],'venue_scope')
for x in read('data/curated/service_game_availability.jsonl'):
 for lang in ('th','en'):
  q=x['service_label']+' วันที่ตรวจรายการ' if lang=='th' else 'When was the inventory verified on '+x['service_label']+'?'
  case(q,lang,[x['last_verified_at']],'inventory_date',('live available','ว่างตอนนี้'))
for r in rs.values():
 if r['kind']=='competition':
  for lang in ('th','en'):case(title(r,lang)+' source_title',lang,[value(r,'source_title')[lang]],'document_identity')
 if r['kind']=='equipment_model':
  for lang in ('th','en'):case(title(r,lang)+' device_type',lang,[enum_text('device_type',value(r,'device_type'),lang) or value(r,'device_type')],'hardware_type')
for rid,th,en,thneed,enneed in [('facility_parking','ที่จอดรถ อยู่ตรงไหน','Parking location',['หน้าตึก 5'],['Building 5']),('facility_rest_seating','ที่นั่งพัก อยู่ตรงไหน','Rest seating location',['โซนกลางห้อง'],['central area']),('contact_studio_facebook','เพจศูนย์อีสปอร์ต ขอข้อมูลทั้งหมด','Studio Facebook page all details',['https://www.facebook.com/psuesportsphuket'],['https://www.facebook.com/psuesportsphuket']),('procedure_change_machine','เปลี่ยนเครื่องที่จองผิด ขอ steps','Change a wrongly booked machine steps',['ยกเลิก','อีเมล','ใหม่'],['Cancel','email','new booking']),('procedure_change_time','เปลี่ยนเวลาจอง ขอ steps','Change the booking time steps',['ยกเลิก','อีเมล','ใหม่'],['Cancel','email','new booking']),('procedure_wrong_slip','แก้การแนบสลิปผิดรูป ขอ steps','Correct an incorrect payment-slip image steps',['สลิป','facebook'],['slip','facebook'])]:
 case(th,'th',thneed,'typed_owner_record');case(en,'en',enneed,'typed_owner_record')
case('ศูนย์อยู่ timezone อะไร','th',['Asia/Bangkok'],'center_scope')
case('What is the studio location timezone?','en',['Asia/Bangkok'],'center_scope')
case('Gaming PC รุ่น MSI MAG Infinite S3 14th สเปกอะไรบ้าง','th',['Intel Core i5-14400','DDR5 32GB','RTX 5060 8GB'],'structured_pc_specs')
case('What are the specifications of Gaming PC รุ่น MSI MAG Infinite S3 14th?','en',['Intel Core i5-14400','DDR5 32GB','RTX 5060 8GB'],'structured_pc_specs')
out=B/('TEST_'+tag+'.jsonl');fail=[];audits=[]
with out.open('x',encoding='utf8') as f:
 for i,c in enumerate(cases,1):
  trace=[];start=time.perf_counter()
  try:
   planner=(lambda q,records,ids:plan_fields(q,records,ids,diagnostic=trace.append)) if enabled else None
   ans=a.answer(c['question'],locale=c['locale'],at=datetime.fromisoformat('2026-10-16T12:00:00+07:00'),planner=planner)
   txt=ans.answer if ans else '';errors=[]
   if not ans:errors.append('no_answer')
   elif not ans.validation.ok:errors.append('validation_rejected')
   for need in c['required']:
    if need.casefold() not in txt.casefold():errors.append('missing:'+need)
   for term in c['forbidden']:
    if term.casefold() in txt.casefold():errors.append('forbidden:'+term)
   row={'case':c,'answer':txt,'errors':errors,'trace':ans.decision_artifact if ans else None,'model_audits':trace,'elapsed':time.perf_counter()-start}
  except Exception as e:row={'case':c,'errors':['exception:'+repr(e)],'model_audits':trace,'elapsed':time.perf_counter()-start}
  f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush();audits+=trace
  if row['errors']:fail.append({'question':c['question'],'errors':row['errors']})
  if i%25==0:print(json.dumps({'done':i,'total':len(cases),'failed':len(fail)}),flush=True)
summary={'cases':len(cases),'passed':len(cases)-len(fail),'failed':len(fail),'failures':fail,'groups':dict(collections.Counter(c['group'] for c in cases)),'llm_flag':enabled,'model_audits':audits,'db':str(db),'scope':'common reader targeted tests, not HTTP or full benchmark; counterpart translations not independently human graded'}
(B/('TEST_'+tag+'_SUMMARY.json')).write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({k:v for k,v in summary.items() if k not in {'failures','model_audits'}},ensure_ascii=False))
