"""Source-derived behavioral cases; raw answers and real model audits retained."""
import os,sys,json,time,hashlib
from pathlib import Path
from datetime import datetime
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B),str(B/'system')]
enabled=sys.argv[1]=='1';tag=sys.argv[2]
from harness import configure,test_temp,equivalent_name_pruning
test_temp(tag);configure('common',enabled);equivalent_name_pruning()
from app.knowledge.common.store import CommonStore
from app.knowledge.common.answer import CommonAnswerer,title
from app.knowledge.common.registry import value
from app.knowledge.common.planner import plan_fields
from migrate_ids import stable
store=CommonStore(B/'common.sqlite');a=CommonAnswerer(store)
with store.connect() as c:records=store.heads(c)
cases=[]
def case(q,lang,required=(),forbidden=(),label='source_content',method=None):cases.append({'question':q,'locale':lang,'required':list(required),'forbidden':list(forbidden),'label':label,'method':method})
for p in sorted((B/'source_snapshot/data/content').rglob('*.json')):
 x=json.loads(p.read_text('utf-8-sig'));kind=x.get('kind');rid=stable(x.get('content_id',''))
 if kind=='control_map':
  g=x['facts']['game'];platform=x['facts']['platform'];rows=x['locales']['th']['fields']['controls']
  en=value(records[rid],'bindings')
  case(f'ขอปุ่มควบคุมทั้งหมดของ {g} บน {platform}','th',[rows[0]['button'],rows[-1]['button'],rows[-1]['action_th']],label='controls_all')
  case(f'List all controls for {g} on {platform}.','en',[rows[0]['button'],rows[-1]['button'],en[-1]['action']['en']],label='controls_all')
 elif kind=='service_availability':
  label=x['facts']['service_label'];th='\n'.join(x['locales']['th']['fields']['notes']);en=value(records[rid],'notes')['en']
  case(f'{label} มีหมายเหตุอะไรบ้าง','th',[th],label='service_notes')
  case(f'What are the service notes for {label}?','en',[en],label='service_notes')
 elif kind=='member' and x['locales']['th']['fields'].get('affiliation'):
  name=x['locales']['th']['fields']['name'];aff=value(records[rid],'affiliation')
  case(f'{name} สังกัดอะไร','th',[aff['th']],label='affiliation')
  case(f'What is the affiliation of {name}?','en',[aff['en']],label='affiliation')
  if x['facts'].get('period'):
   case(f'{name} วาระช่วงไหน','th',[x['facts']['period']],label='historical_period')
   case(f'What is the tenure of {name}?','en',[x['facts']['period']],label='historical_period')
case('Mario Kart 8 Deluxe ปุ่มเร่งเครื่องกดอะไร','th',['A | เร่งเครื่อง','กดค้าง'],['B | เบรก'],'specific_control')
case('What does A do in Moving Out 2 on Nintendo Switch?','en',['Jump'],['Shield'],'specific_control')
case('What time is the afternoon session? I need the official answer.','en',['13:00','16:00','Friday','Maintenance'],label='previous_timeout')
case('รอบบ่ายคือกี่โมง','th',['13:00','16:00','วันศุกร์'],label='session_definition')
case('พกอาหารจากข้างนอกเข้าไปได้ไหม','th',['พื้นที่ที่กำหนด','ยังไม่ได้ระบุ'],label='previous_timeout')
case('May I bring outside food?','en',['designated areas','does not separately confirm'],label='outside_food_boundary')
case('General Adult PC 2 ชั่วโมง กี่บาท','th',['140.00','70.00','ยังไม่ระบุ'],['150.00'],label='recovered_price')
case('What is the General Adult PC price for 2 hours?','en',['140.00','70.00','not specified'],['150.00'],label='recovered_price')
case('PS5 มีเกมอะไรบ้าง','th',['17','God of War'],['Animal Crossing'],'offered_catalog')
case('PC มีเกมอะไรบ้าง','th',['6','Counter-Strike'],['Mario Kart'],'offered_catalog')
case('TEKKEN 8 การแก้ข้อพิพาททำยังไง','th',['กรรมการ','สิ้นสุด'],['competition_dates'],'rule_scope')
case('Under CS2 tournament rules, which language must protests use and who may file a protest within how many minutes?','en',['15','Thai','captain'],['starting money'],'rule_scope')
# Sources that never reached the old canonical export are tested separately.
raw_recovery=json.loads((B/'RAW_RECOVERY.json').read_text('utf8'))
for item in raw_recovery['control_groups']:
 if not item['record_id'].startswith('recovered_controls_'):continue
 r=records[item['record_id']];rows=value(r,'bindings')
 for lang in ('th','en'):
  q=f"{item['game']} บน {item['platform']} มีปุ่มอะไรบ้าง" if lang=='th' else f"List all controls for {item['game']} on {item['platform']}."
  if rows:case(q,lang,[(rows[0]['button_label'])[lang],rows[-1]['action'][lang]],label='recovered_controls')
  else:case(q,lang,[],['Cross |','A |','Triangle |'],label='unavailable_mapping')
description_map={r['locator']:r['record_id'] for r in json.loads((B/'RAW_RECOVERY_LINEAGE.json').read_text('utf8')) if r['field']=='official_description'}
raw=[json.loads(s) for s in (B/'source_snapshot/data/curated/our_games_scraped_details.jsonl').read_text('utf-8-sig').splitlines() if s.strip()]
for i,x in enumerate(raw):
 r=records[description_map['/'+str(i)]];d=value(r,'official_description')
 case(x['game']+' คำบรรยายต้นฉบับ','th',[d['th']],label='recovered_description')
 case('What is the official description of '+x['game']+'?','en',[d['en']],label='recovered_description')
out=B/('BEHAVIOR_'+tag+'.jsonl');fail=[];audits=[];times=[]
dbhash=hashlib.sha256((B/'common.sqlite').read_bytes()).hexdigest()
with out.open('x',encoding='utf8') as f:
 for i,c in enumerate(cases,1):
  start=time.perf_counter();trace=[]
  try:
   planner=(lambda q,rs,ids:plan_fields(q,rs,ids,diagnostic=trace.append)) if enabled else None
   r=a.answer(c['question'],locale=c['locale'],at=datetime.fromisoformat('2026-10-14T12:00:00+07:00'),planner=planner)
   text=r.answer if r else '';errors=[]
   if r is None:errors.append('no_answer')
   if r and not r.validation.ok:errors.append('validation_rejected')
   for s in c['required']:
    if s and s.casefold() not in text.casefold():errors.append('missing:'+s)
   for s in c['forbidden']:
    if s.casefold() in text.casefold():errors.append('forbidden:'+s)
   row={'case':c,'answer':text,'errors':errors,'trace':r.decision_artifact if r else None,'model_audits':trace,'elapsed':time.perf_counter()-start}
  except Exception as e:row={'case':c,'errors':['exception:'+repr(e)],'elapsed':time.perf_counter()-start,'model_audits':trace}
  f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush();times.append(row['elapsed']);audits+=trace
  if row['errors']:fail.append({'question':c['question'],'errors':row['errors']})
  if i%20==0:print(json.dumps({'done':i,'total':len(cases),'failed':len(fail),'llm_enabled':enabled}),flush=True)
summary={'tag':tag,'llm_enabled':enabled,'cases':len(cases),'passed':len(cases)-len(fail),'failed':len(fail),'failures':fail,'model_audits':audits,'max_seconds':max(times),'database_unchanged':dbhash==hashlib.sha256((B/'common.sqlite').read_bytes()).hexdigest(),'scope':'common direct reader; not HTTP or load test'}
(B/('BEHAVIOR_'+tag+'_SUMMARY.json')).write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in summary.items() if k!='model_audits'},ensure_ascii=False),flush=True)
