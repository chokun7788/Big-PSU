"""Compile a source-backed experimental read model, with isolated fixtures."""
import hashlib,json,re,sqlite3
from datetime import date,timedelta
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent
def read(path):return json.loads((B/path).read_text('utf8'))
def loc(v):
 if isinstance(v,dict) and ('th' in v or 'en' in v):return {'th':v.get('th') or '', 'en':v.get('en') or ''}
 if isinstance(v,list):return {l:'; '.join(loc(x)[l] for x in v) for l in ['th','en']}
 if isinstance(v,dict):return {l:'; '.join(k+': '+loc(x)[l] for k,x in v.items()) for l in ['th','en']}
 return {'th':str(v),'en':str(v)}
db=B/'r106_complete_flow_20261020/system/data/knowledge/common.sqlite';c=sqlite3.connect('file:'+db.as_posix()+'?mode=ro',uri=True)
records={rid:json.loads(p) for rid,p in c.execute('select h.record_id,r.payload from cc_heads h join cc_revisions r on h.record_id=r.record_id and h.head=r.version where h.withdrawn=0')}
def val(r,k):return r['fields'].get(k,{}).get('value') if r['fields'].get(k,{}).get('status')=='known' else None
def title(r):
 for k in ['title','name','display_name','event_name','subject','question']:
  if val(r,k):return loc(val(r,k))
 return {'th':r['record_id'],'en':r['record_id']}
facts=[]
def add(cat,rid,facet,subject,label,value,refs,aliases=None,**extra):
 if not refs:return
 l=loc(value)
 if not l['th'] and not l['en']:return
 if not l['en']:l['en']=l['th'];extra['english_translation_missing']=True
 if not l['th']:l['th']=l['en']
 fid=f'{cat}:{rid}:{facet}'
 if any(x['id']==fid for x in facts):return
 facts.append({'id':fid,'category':cat,'record_id':rid,'facet':facet,'subject':subject,'label':dict(zip(['th','en'],label)),'value':l,'aliases':list(dict.fromkeys([*subject.values(),*(aliases or [])])),'evidence_refs':refs,'fixture':False,**extra})
def field(cat,r,k,label,**extra):
 f=r['fields'].get(k,{})
 if f.get('status')=='known' and f.get('value') is not None:add(cat,r['record_id'],k,title(r),label,f['value'],f.get('evidence_refs'),sum(r.get('aliases',{}).values(),[]),**extra)
for r in records.values():
 kind=r['kind']
 if kind=='center':
  for k,t,e in [('address','ที่อยู่','address'),('building','อาคาร','building'),('floor','ชั้น','floor'),('map_url','แผนที่','map link'),('description','ข้อมูลศูนย์','studio overview'),('operator','ผู้ดำเนินการ','operator')]:field('C01',r,k,(t,e))
 if kind=='contact':
  for k,t,e in [('value','ช่องทางติดต่อ','contact information'),('office_hours','เวลาติดต่อ','contact hours')]:field('C01',r,k,(t,e))
 if kind=='facility':
  for k,t,e in [('location','ที่ตั้ง','location'),('usage_conditions','วิธีใช้','usage conditions')]:field('C01',r,k,(t,e))
 if kind=='person':
  for k,t,e in [('display_name','ชื่อ','name'),('role','หน้าที่และตำแหน่ง','role'),('team','ทีม','team')]:field('C02',r,k,(t,e),public_scope_basis='Owner R108 group_people confirms existing names/roles; no private contacts included')
 if kind=='equipment_model':
  for k,t,e in [('device_type','ชนิดอุปกรณ์','device type'),('specifications','สเปก','specifications'),('usage','การใช้งาน','usage')]:field('C03',r,k,(t,e))
  for si,s in enumerate(val(r,'specifications') or []):
   if isinstance(s,dict) and s.get('key') in ['zone','quantity']:
    add('C03',r['record_id'],'location' if s['key']=='zone' else 'quantity',title(r),('ที่ตั้ง' if s['key']=='zone' else 'จำนวนเครื่อง','location' if s['key']=='zone' else 'quantity'),s['value'],r['fields']['specifications']['evidence_refs'])
 if kind=='resource':
  field('C03',r,'capacity_persons',('จำนวนคนเล่นพร้อมกัน','simultaneous player capacity'))
  zid=val(r,'zone_id')
  if zid in records:add('C03',r['record_id'],'location',title(r),('ที่ตั้ง','location'),title(records[zid]),r['fields']['zone_id']['evidence_refs'])
 if kind=='zone':field('C03',r,'room_seats',('จำนวนที่นั่งห้อง','room seats'))
 if kind=='game':
  for k,t,e in [('summary','คำอธิบายเกม','game overview'),('how_to_play','วิธีเล่น','how to play'),('genre','แนวเกม','genre'),('supported_platforms','แพลตฟอร์มที่เกมรองรับ','supported platforms')]:field('C04',r,k,(t,e))
  offers=[x for x in records.values() if x['kind']=='game_service' and val(x,'game_id')==r['record_id'] and val(x,'offered') is True]
  if offers:
   labels={l:list(dict.fromkeys(title(records[val(x,'service_id')])[l] for x in offers if val(x,'service_id') in records)) for l in ['th','en']}
   add('C04',r['record_id'],'studio_services',title(r),('บริการที่มีเกมนี้','studio services offering this game'),{l:'; '.join(v) for l,v in labels.items()},[{'source_id':x['record_id'],'locator':'/fields/offered','path_kind':'common_relation'} for x in offers],sum(r.get('aliases',{}).values(),[]))
 if kind=='control_set':
  g=records.get(val(r,'game_id'));sub=title(g) if g else title(r);platform=val(r,'platform') or ''
  sub={l:s+' / '+platform for l,s in sub.items()}
  for i,b in enumerate(val(r,'bindings') or []):
   action=loc(b.get('action') or '');button=loc(b.get('button_label') or b.get('buttons') or '')
   value={l:button[l]+(' — '+loc(b.get('notes'))[l] if b.get('notes') and loc(b.get('notes'))[l] not in ['', 'None'] else '') for l in ['th','en']}
   add('C05',r['record_id'],f'binding_{i}',sub,(action['th'],action['en']),value,r['fields']['bindings']['evidence_refs'],action.values(),platform=platform,source_index=i)
 if kind=='rate':
  service=records.get(val(r,'service_id'));group=records.get(val(r,'audience_id'))
  if not service or not group:continue
  sub={l:title(service)[l]+' / '+title(group)[l] for l in ['th','en']}
  amount=val(r,'amount_minor')/100
  add('C06',r['record_id'],'amount',sub,('ค่าบริการต่อคนต่อรอบ','price per person per session'),{'th':f'{amount:g} บาทต่อคนต่อรอบ','en':f'{amount:g} THB per person per session'},r['fields']['amount_minor']['evidence_refs'],numeric=amount,calculation='integer_sessions_per_person',confirmation_ref='owner108:group_rates + owner108:Q049',business_effective_period=r['validity'])
  field('C06',r,'duration_minutes',('นาทีต่อรอบ','minutes per session'))
 if kind=='schedule':
  days={'th':['จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์','อาทิตย์'],'en':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']};day=val(r,'weekday');sub={l:days[l][day] for l in days}
  for k,t,e in [('bookable_periods','ช่วงจองเล่น','bookable periods'),('maintenance_periods','ช่วงบำรุงรักษา','maintenance periods')]:
   value=val(r,k)
   if value is not None:
    x='; '.join(a['start']+'–'+a['end'] for a in value) or 'ไม่มี / None'
    add('C11',r['record_id'],k,sub,(t,e),x,r['fields'][k]['evidence_refs'])
 if kind=='closure':
  for k,t,e in [('local_date','วันที่ปิดพิเศษ','exception date'),('reason','เหตุผล','reason')]:field('C11',r,k,(t,e))

# Studio offering lists are complete sets within this snapshot, not top-K.
for s in [r for r in records.values() if r['kind']=='service']:
 offers=[x for x in records.values() if x['kind']=='game_service' and val(x,'service_id')==s['record_id'] and val(x,'offered') is True]
 if offers:
  names={l:list(dict.fromkeys(title(records[val(x,'game_id')])[l] for x in offers if val(x,'game_id') in records)) for l in ['th','en']}
  add('C04',s['record_id'],'game_catalog',title(s),('รายชื่อเกมทั้งหมด','all offered games'),{l:'; '.join(v) for l,v in names.items()},[{'source_id':x['record_id'],'locator':'/fields/game_id','path_kind':'common_relation'} for x in offers],complete_set=True)

rent=read('r109_owner_answers_20261020/RENTAL_PACKAGES_RECONCILED.json')
for i,p in enumerate(rent['packages']):
 sub={'th':p['zone_name']+' / '+('ภายใน' if p['audience']=='internal' else 'ภายนอก')+' / '+('ครึ่งวัน' if p['period_label']=='half_day' else 'เต็มวัน'),'en':p['zone_name']+' / '+p['audience']+' / '+p['period_label'].replace('_',' ')}
 for k,t,e in [('amount_thb','ราคาแพ็กเกจ','package price'),('duration_minutes','ระยะเวลาเป็นนาที','duration in minutes'),('equipment_included','อุปกรณ์ที่รวม','included equipment'),('room_seats','ที่นั่งห้อง','room seats')]:
  refs=[{'source_id':'r109:rental','locator':p['locator'],'source_path':rent['source_path']}]
  if k=='duration_minutes':refs=[p['duration_evidence']]
  v=p[k];value={'th':f'{v} บาทต่อแพ็กเกจ','en':f'{v} THB per package'} if k=='amount_thb' else v
  add('C07','package_'+str(i),k,sub,(t,e),value,refs,numeric=v if isinstance(v,(int,float)) else None)

# Translate only the owner's supplied meaning. Do not add missing policies.
translations={
'Q001':'Wait in the central area. You cannot start playing before your booked time.',
'Q003':'You may book the next session through the normal process if it is available and within service hours.',
'Q004':'No refund is given for the original booking when changing services; cancel and book again as previously stated.',
'Q005':'Booking details cannot be edited. Cancel through email at least 1 hour before the session, then book again and attach the original payment slip.',
'Q008':'You must notify the studio if you cannot arrive in time.',
'Q009':'Contact the Facebook page with the payment slip and booking evidence.',
'Q010':'The studio contacts the Gmail email address used to register. The handling of money is not specified by this answer.',
'Q011':'Cancel through email at least 1 hour in advance, then book again using the original payment slip.',
'Q014':'Contact the Facebook page with the slip and booking evidence. Overpaid funds are kept for a future session; they are not refunded.',
'Q015':'For an additional payment, contact the Facebook page with the slip and booking evidence.',
'Q016':'Payment must be made in full.',
'Q017':'Payment checking normally takes about 30 minutes. Contact the Facebook page if the status has not changed.',
'Q018':'Tax invoices cannot be issued. The earlier answer also says quotations and receipts cannot be issued.',
'Q019':'Contact the Facebook page with the payment slip and booking evidence. This does not establish a refund entitlement or processing deadline.',
'Q020':'A studio Steam account is provided for use at the studio. You may also use your own Steam account.',
'Q022':'The owner says users are logged out and login data is not kept. This is not an independently verified security guarantee.',
'Q025':'If a game update takes more than 5 minutes, additional play time is provided. The exact extension is not specified.',
'Q026':'A different machine may be used if the game cannot run for a reason other than updating. This is separate from the no-switching rule during updates.',
'Q027':'Ask the studio supervisor to confirm the game version.',
'Q028':'Network or other system problems follow the same fault-handling principle; notify staff for inspection.',
'Q029':'You do not pay compensation when equipment fails by itself without the player causing the damage. The amount is not specified.',
'Q030':'Notify staff to replace a faulty peripheral.',
'Q032':'Parental supervision is recommended. Signed consent alone is allowed, with the guardian name used for verification. No minimum age is established here.',
'Q033':'In-game screenshots and video capture are allowed; delete them when finished. This does not confirm filming people or the premises.',
'Q034':'The earlier answer permits game streaming; the latest answer says there is no zone restriction. It does not grant permission to install software.',
'Q037':'External visitors may use all general studio services. Tournament eligibility is separate.',
'Q040':'Public-holiday opening follows studio announcements on the Facebook page.',
'Q041':'Contact the Facebook page to discuss out-of-hours rentals or events. A single price for all times is not guaranteed.',
'Q043':'You may sit and watch your friend play. A maximum number of spectators is not specified.',
'Q044':'Personal accessories may be used. The earlier keyboard and mouse answer requires notifying staff.',
'Q045':'The owner says the rental start can be discussed; normal half-day and full-day periods are clarified in the later answers.',
'Q047':'For a venue or zone rental, contact the Facebook page.',
'Q048':'Contact the Facebook page about rental terms. Cancellation and refund conditions are not independently specified.',
'Q049':'Hourly service fees are charged per person. This does not make whole-zone rental prices per person.',
'Q050':'The quoted price table includes tax. The source note about out-of-hours staff compensation remains separate.',
}
topic_en={'Q001':'arrival waiting','Q003':'extend session','Q004':'change service','Q005':'change paid booking','Q008':'late arrival notice','Q009':'rain reschedule','Q010':'studio closes after booking','Q011':'correct booking name','Q014':'overpayment','Q015':'underpayment additional slip','Q016':'full payment','Q017':'payment verification','Q018':'tax invoice and receipt','Q019':'payment problem contact','Q020':'Steam account','Q022':'logout and login data','Q025':'game update compensation','Q026':'game fails to run change machine','Q027':'confirm installed version','Q028':'network fault','Q029':'equipment damage compensation','Q030':'faulty peripheral','Q032':'guardian consent','Q033':'game capture','Q034':'game streaming','Q037':'external visitors','Q040':'public holiday opening','Q041':'out of hours rental','Q043':'spectators','Q044':'personal accessories','Q045':'rental start time','Q047':'rental contact','Q048':'rental cancellation terms','Q049':'per person billing','Q050':'tax included'}
owner=read('r109_owner_answers_20261020/MERGED_SERVICE_STATEMENTS.json')['statements']
booking={'Q001','Q003','Q004','Q005','Q008','Q009','Q010','Q011','Q043'};payment={'Q014','Q015','Q016','Q017','Q018','Q019'}
for x in owner:
 key=x['source_question_id']
 if key not in translations:continue
 cat='C08' if key in booking else 'C09' if key in payment else 'C11' if key=='Q040' else 'C07' if key in {'Q041','Q045','Q047','Q048'} else 'C06' if key in {'Q049','Q050'} else 'C10'
 add(cat,key,'owner_policy',{'th':x['topic'],'en':topic_en[key]},('เงื่อนไขและวิธีปฏิบัติ','conditions and procedure'),{'th':x['answer_th'],'en':translations[key]},[{'source_id':x['id'],'locator':'/answer_th','source_path':'r109_owner_answers_20261020/MERGED_SERVICE_STATEMENTS.json'}],aliases=[x['source_text'] or '',topic_en[key]],owner_confirmed=True)
for x in owner:
 key=x['source_question_id'];ref=[{'source_id':x['id'],'locator':'/answer_th'}]
 if key=='R108_PS5_CONTROLLERS':add('C03',key,'controllers',{'th':'PS5','en':'PS5'},('จอยต่อเครื่อง','controllers per console'),{'th':'2 จอยต่อเครื่อง','en':'2 controllers per console'},ref,numeric=2)
 if key=='R108_PAYER':add('C09',key,'payer',{'th':'ผู้โอนเงิน','en':'payment sender'},('ผู้มีสิทธิ์โอน','eligible payer'),{'th':x['answer_th'],'en':'The payment sender must have a name in the booking.'},ref)
 if key=='R108_OPEN_16_18':add('C11',key,'weekday_closing',{'th':'จันทร์ถึงศุกร์ 16:00–18:00','en':'Monday to Friday 16:00–18:00'},('สถานะเปิดปิด','opening status'),{'th':'ปิดแล้ว','en':'Closed'},ref)
 if key=='R108_MIXED_RATE':add('C06',key,'mixed_audience',{'th':'ผู้เล่นต่างกลุ่ม','en':'mixed audience players'},('การคิดราคาต่างกลุ่ม','mixed audience pricing'),{'th':x['answer_th'],'en':'Each player pays the rate for their own audience group.'},ref)

# Read current rule source clauses, retain textual holds and owner decisions.
docs=read('r109_owner_answers_20261020/TOURNAMENT_SOURCE_UNITS_RECONCILED.json')['documents']
for d in docs:
 heading='';event=d['units'][0]['text']
 for u in d['units']:
  t=u.get('candidate_text') or u['text'];resolution=u.get('owner_resolution') or {}
  if u.get('usage')=='superseded_for_pause_permission' or resolution.get('status')=='deferred_no_test' or u.get('quality_hold'):continue
  if len(t)<42:heading=t;continue
  if d['game']=='valorant' and u.get('language')=='en':continue
  # Explicit source section text is a reference excerpt, not a claim that the entire book is complete.
  section=re.match(r'^(\d+(?:\.\d+)+)',t)
  label=(section.group(1)+' '+heading if section else heading).strip() or 'กฎการแข่งขัน'
  add('C13',f"{d['game']}_{u['paragraph']}",'rule_clause',{'th':event,'en':{'cs2':'PSU Phuket CS2 2026 Tournament','valorant':'PSU Phuket VALORANT 2026 Tournament','rov':'Blueket Games 2025 RoV men','tekken':'PSU Esports Tekken 8 event'}[d['game']]},(label,label),{'th':t,'en':t},[{'source_id':u['source_id'],'locator':u['locator'],'source_sha256':d['sha256']}],english_translation_missing=True,rule_source_excerpt=True,section_number=section.group(1) if section else None)

# Isolated controlled providers and news: never inserted into the common DB.
resources=[r for r in records.values() if r['kind']=='resource']
for i,r in enumerate(resources):
 for j,state in enumerate(['available','booked','unavailable','stale']):
  sub={l:title(r)[l]+f' / 2026-10-21 {9+j:02}:00' for l in ['th','en']}
  add('C12',r['record_id']+'_'+str(j),'live_status',sub,('สถานะว่างสด','live availability'),{'th':{'available':'ว่าง','booked':'ถูกจอง','unavailable':'ตรวจสถานะไม่ได้','stale':'ข้อมูลเก่า ยืนยันสถานะไม่ได้'}[state],'en':{'available':'Available','booked':'Booked','unavailable':'Provider unavailable; occupancy is not confirmed','stale':'Stale data; occupancy is not confirmed'}[state]},[{'source_id':'fixture:live_provider','locator':r['record_id']+'/'+str(j)}],provider_state=state,fixture=True)
for i in range(1,13):
 sub={'th':f'กิจกรรมจำลองทดสอบ {i:02}','en':f'Synthetic test event {i:02}'}
 for facet,label,value in [('description',('รายละเอียดกิจกรรม','event details'),{'th':f'กิจกรรมจำลอง {i:02} สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง','en':f'Synthetic event {i:02} for testing news reading; not an actual studio announcement'}),('date',('วันที่จัด','event date'),str(date(2026,10,21)+timedelta(days=i))),('registration',('ช่องทางสมัคร','registration link'),f'https://example.invalid/test-registration/{i:02}'),('status',('สถานะรับสมัคร','registration status'),{'th':'เปิดรับสมัคร' if i%2 else 'ปิดรับสมัครแล้ว','en':'Registration open' if i%2 else 'Registration closed'})]:
  add('C14','fixture_event_'+str(i),facet,sub,label,value,[{'source_id':'fixture:news','locator':str(i)+'/'+facet}],fixture=True)

assert all(x['evidence_refs'] for x in facts)
assert all(any(f['category']==f'C{i:02}' for f in facts) for i in range(1,15))
path=R/'COMMON_READ_MODEL.json'
if path.exists():raise SystemExit('Read model already frozen; refuse overwrite')
path.write_text(json.dumps({'schema':'r113-experimental-read-model-1','records':records,'facts':facts,'runtime_installation':'isolated experimental adapters only','not_production_common_schema':True,'news_fixture_only':True,'live_fixture_only':True,'source_database_sha256':hashlib.sha256(db.read_bytes()).hexdigest()},ensure_ascii=False,indent=2),'utf8')
manifest={'source_database':str(db),'sha256':hashlib.sha256(db.read_bytes()).hexdigest(),'facts':len(facts),'categories':{f'C{i:02}':sum(x['category']==f'C{i:02}' for x in facts) for i in range(1,15)},'fixture_categories':['C12','C14'],'source_records':len(records),'production_changed':False,'schema_note':'Compiled candidate view with source-backed owner overlays, not an installation into R78 or frozen R106'}
(R/'DATA_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf8');print(json.dumps(manifest,ensure_ascii=False))
