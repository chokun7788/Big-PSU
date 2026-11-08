"""Reviewed retained questions only. No teacher answer text enters labels."""
import collections,copy,hashlib,json,re,unicodedata
from pathlib import Path
from manual_annotations import GOLD,TEST,VALIDATION,COMPOUNDS,EXTRA_TRAIN
from context_contract import validate,messages
R=Path(__file__).resolve().parent;P=R.parent;OLD=P/'r120_teacher_distillation_20261022'
load=lambda n:json.loads((R/n).read_text('utf8'))
jobs=list(map(json.loads,(R/'ALL_RETAINED_JOBS.jsonl').open(encoding='utf8')));bykey={j['key']:j for j in jobs};families=load('FAMILY_GROUPS.json');fresh=load('FRESH_CANDIDATES.json');aliases=load('SOURCE_ENTITY_ALIASES.json')
allsets={'train':[],'validation':[],'test':[]};review=[];excluded=[]
def norm(q):return re.sub(r'\s+',' ',unicodedata.normalize('NFC',q).casefold()).strip()
def signature(q):
 s=norm(q)
 for pattern in [r'please (?:answer from|use) verified studio information[: ,]*',r'could you please help me w+ith this[: ,]*',r'(?:please tell me|please explain|i am planning a visit and (?:need to|would like to) know)[: ,]*',r'could you check this (?:using verified information|for me)[: ,]*',r'(?:ขอสอบถามหน่อยครับ|ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย|รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ|ขอข้อมูลที่ยืนยันได้หน่อยครับ|กำลังวางแผน(?:จะ)?ไปใช้บริการ|เลย(?:อยากทราบว่า|ขอถามว่า)|พอดีอยากรู้ว่า)[: ,]*',r'(?:please answer briefly|please use verified information|i need the official answer|please keep the answer concise|ขอรายละเอียดแบบสั้น ๆ|ขอสรุปให้เข้าใจง่าย)[.?! ]*']:
  s=re.sub(pattern,'',s,flags=re.I)
 return re.sub(r'[^a-z0-9\u0e00-\u0e7f]','',s)
def spans(q,kind):
 matches=[]
 for a in aliases:
  if a['kind'] not in kind:continue
  for s in a['aliases']:
   edge1=r'(?<![a-z0-9])' if re.match('[a-z0-9]',s,re.I) else ''
   edge2=r'(?![a-z0-9])' if re.search('[a-z0-9]$',s,re.I) else ''
   for m in re.finditer(edge1+re.escape(s)+edge2,q,re.I):matches.append((m.start(),m.end(),q[m.start():m.end()],a['id']))
 longest=[x for x in matches if not any(y[0]<=x[0] and x[1]<=y[1] and y[1]-y[0]>x[1]-x[0] for y in matches)]
 return list({(a,b,s):rid for a,b,s,rid in longest}.keys())
def constraints(q,domain):
 patterns=[
 ('duration',r'(?:one and a half|half an?|one|two|three|four|five|six|a|an|\d+(?:\.\d+)?)\s*(?:hours?|hrs?|minutes?)\b|(?:\d+(?:\.\d+)?|หนึ่ง|สอง|สาม|ครึ่ง)\s*(?:ชั่วโมง|นาที)'),
 ('persons',r'\b\d+\s*(?:people|persons?|players?)\b|\d+\s*คน'),
 ('sessions',r'\b\d+\s*sessions?\b|\d+\s*รอบ'),
 ('event' if domain=='competition_rules' else 'date',r'20\d\d(?:[-/]\d\d[-/]\d\d)?|(?:next\s+)?(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)|today|tomorrow|วันนี้|พรุ่งนี้|(?:วัน)?(?:จันทร์|อังคาร|พุธ|พฤหัสบดี|ศุกร์|เสาร์|อาทิตย์)'),
 ('time',r'(?<!\d)\d{1,2}:\d{2}(?!\d)|\b\d{1,2}\s*(?:am|pm)\b|ตอนนี้|right now|ช่วงบ่าย|ตอนบ่าย|ช่วงเช้า|ตอนเช้า'),
 ('platform',r'PlayStation(?:\s*/\s*PS5|\s*5)?|\bPS5\b|\bPC\b|Nintendo Switch'),
 ('negation',r'ไม่มีรหัส\s*PSU|ไม่ใช่(?:นักศึกษา)?\s*PSU|ไม่ได้ถามเรื่อง(?:กิน|ดื่ม)|\bnonstudents\b|\bnot (?:asking(?: about)? (?:eating|drinking)|drink it)\b|\bwithout\s+booking\b|\bnot(?: an?| a)?\s+PSU(?:\s+(?:student|staff))?\b'),
 ('requested_scope',r'\ball(?: the)? buttons\b|\b\d+ buttons\b|ปุ่มทั้งหมด|ทั้งหมด|หลายโซน|more than one zone|multiple zones')]
 if domain in {'service_fee','rental','rules'}:patterns += [('audience',r'PSU\s+(?:Student(?:\s+and\s+Staff)?|Staff|Alumni)|General\s+(?:Adult|Student)|นักศึกษา\s*PSU|นักศึกษา(?:ต่างมหาลัย|ต่างมหาวิทยาลัย)|บุคคลทั่วไป|คนทั่วไป|คนนอก|ภายนอก|ภายใน|\badult\b|\boutsider\b|\btourist\b|student from another university|general visitor')]
 found=[]
 for slot,p in patterns:
  for m in re.finditer(p,q,re.I):
   if m[0]:found.append({'slot':slot,'quote':m[0],'source_record_id':''})
 if domain in {'reservation','service_fee','rental','games','live'}:
  ss=spans(q,{'service','zone'})
  for a,b,s in ss[:2]:found.append({'slot':'service','quote':s,'source_record_id':''})
 if domain=='competition_rules':
  m=re.search(r'(?:I am preparing|กำลังจะลงแข่ง|หำลังจะลงแข่ง|เตรียมแข่ง)[^.?!]*',q,re.I)
  if m:found.insert(0,{'slot':'condition','quote':m[0],'source_record_id':''})
 if domain in {'rules','reservation','payment'}:
  m=re.search(r'(?:\bif\b|ถ้า|หาก)[^.?!]*',q,re.I)
  if m:found.insert(0,{'slot':'condition','quote':m[0],'source_record_id':''})
 seen=set();out=[]
 for c in found:
  k=(c['slot'],c['quote'])
  if k not in seen:out.append(c);seen.add(k)
 return out[:12]
def target(q,domain):
 kinds={'games':{'game'},'game_controls':{'game'},'competition_rules':{'game'},'equipment':{'equipment_model'},'service_fee':{'service','game'},'rental':{'zone'},'members':{'person'}}.get(domain,set())
 found=spans(q,kinds)
 unique=list(dict.fromkeys(s for a,b,s in found))
 if len(unique)==1 and len(unique[0])<=120:return unique[0]
 return ''
def task(q,domain,op,facet,ambiguous=False,whole=None):
 whole=whole or q
 return {'quote':q,'domain':domain,'operation':op,'facet':facet,'target':target(q,domain),
 'constraints':constraints(whole,domain),'ambiguous':bool(ambiguous)}
def make(q,spec,index=None):
 if spec[0]=='multiple':ts=[task(span,d,op,f,whole=q) for span,d,op,f in COMPOUNDS[index]]
 else:ts=[task(q,*spec[1:4],ambiguous=len(spec)>4 and spec[4])]
 contexts=list(dict.fromkeys(c['quote'] for t in ts for c in t['constraints']))[:12]
 return {'focus':spec[0],'context_quotes':contexts,'tasks':ts}
def add(split,j,plan,source,group=None):
 ok,why=validate(plan,j['question']);assert ok,(j['question'],why,plan)
 x={'key':j['key'],'question':j['question'],'locale':j.get('locale','auto'),'family':group or families[j['key']],
 'label':plan,'label_source':source,'messages':messages(j['question'])+[{'role':'assistant','content':json.dumps(plan,ensure_ascii=False,separators=(',',':'))}]}
 allsets[split].append(x);review.append({'split':split,'key':x['key'],'question':x['question'],'label':plan,'label_source':source})
for i,spec in TEST.items():
 j=bykey[fresh[i]['key']];add('test',j,make(j['question'],spec,i),'manual_review_fresh_family')
for i,spec in VALIDATION.items():
 j=bykey[fresh[i]['key']];add('validation',j,make(j['question'],spec,i),'manual_review_fresh_family')
for prefix,spec in GOLD.items():
 j=next(j for j in jobs if j['key'].startswith(prefix));add('train',j,make(j['question'],spec),'manual_review_r120_context_failure_and_regression')
for i,spec in EXTRA_TRAIN.items():
 j=bykey[fresh[i]['key']];add('train',j,make(j['question'],spec,i),'manual_review_retained_contrast')
def infer_focus(t,q):
 d=t['domain'];f=t['facet']
 if d=='service_fee':return 'service_duration' if f=='duration_minutes' else 'price'
 if d=='competition_rules':return 'competition_rules'
 if d=='game_controls':return 'game_controls'
 if d=='equipment':return 'equipment_location' if f=='location' else 'hardware' if f=='specifications' else 'equipment_capacity' if f in {'capacity_persons','service_capacity','room_seats'} else 'equipment_definition' if f=='usage' else 'equipment_inventory'
 if d=='games':return {'zone':'game_location','game_catalog':'game_catalog','studio_services':'game_availability','supported_platforms':'game_platform'}.get(f,'game_description')
 if d=='members':return 'people'
 if d=='contact':return 'location' if f in {'address','building','floor','map_url','location'} else 'identity' if f in {'operator','description'} else 'contact'
 if d=='rules':return 'food_bring' if re.search(r'bring|นำ|เอา.*เข้า',q,re.I) and re.search(r'food|drink|อาหาร|เครื่องดื่ม',q,re.I) else 'food_consume' if re.search(r'food|drink|อาหาร|เครื่องดื่ม',q,re.I) else 'eligibility' if re.search(r'เข้าใช้|สมาชิก|คนภายนอก|คนนอก|ผู้ใช้|visitor|outsider|member',q,re.I) else 'studio_rules'
 if d=='reservation':return 'booking_policy' if re.search(r'cancel|ยกเลิก|check.in|เช็คอิน|ล่วงหน้า|เปลี่ยน|when|กี่',q,re.I) else 'booking_procedure'
 if d=='payment':return 'payment'
 if d=='schedule':return 'maintenance' if f=='maintenance_periods' else 'bookable_periods' if f=='bookable_periods' else 'opening_hours'
 if d=='live':return 'live_status'
 return 'general'
teacher=json.loads((OLD/'TEACHER_LESSONS.json').read_text('utf8'))
for ex in teacher['examples']:
 j=bykey[ex['id']];t=ex['plan']['tasks'][0];spec=(infer_focus(t,j['question']),t['domain'],t['operation'],t['facet'])
 add('train',j,make(j['question'],spec),'r120_reviewed_teacher_behavior_remapped_slots')
# Existing source-derived development questions add rare domains. No answers,
# record IDs, prices or claim values are copied into training targets.
rare=list(map(json.loads,(P/'r113_multi_flow_benchmark_20261021/EFFECTIVE_QUESTIONS_1400.jsonl').open(encoding='utf8')))
counts=collections.Counter()
for j in rare:
 cat=j['category']
 if cat not in {'C07','C09','C14'} or j['stratum']!='single_need' or counts[cat]>=12:continue
 facets={c['facet'] for c in j['expected']['claims']}
 if len(facets)!=1:continue
 facet=next(iter(facets));domain={'C07':'rental','C09':'payment','C14':'news'}[cat]
 op='price_calculate' if facet=='amount_thb' else 'detail'
 focus={'C07':'rental','C09':'payment','C14':'news'}[cat]
 key=hashlib.sha256(('r113:'+j['id']+j['question']).encode()).hexdigest()
 row={'key':key,'question':j['question'],'locale':j['locale']}
 add('train',row,make(j['question'],(focus,domain,op,facet)),'reviewed_r113_existing_question_task_only_fixture' if cat=='C14' else 'reviewed_r113_existing_question_task_only',group='r113:'+j['id'].split('-Q')[0]+':'+str(j['expected']['claims'][0]['record_id']))
 counts[cat]+=1
# No identical normalized core may occur across optimization and held-out sets.
held={signature(x['question']) for s in ['test','validation'] for x in allsets[s]}
kept=[];seen=set()
for x in allsets['train']:
 sig=signature(x['question'])
 if sig in held:excluded.append({'key':x['key'],'reason':'normalized_core_matches_held_out'});continue
 if x['key'] in seen:continue
 seen.add(x['key']);kept.append(x)
allsets['train']=kept
assert not ({x['family'] for x in allsets['train']}&{x['family'] for s in ['validation','test'] for x in allsets[s]})
assert not ({x['family'] for x in allsets['test']}&{x['family'] for x in allsets['validation']})
for name,xs in allsets.items():
 (R/(name+'.jsonl')).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in xs),'utf8')
manifest={'new_questions':0,'business_answer_targets':False,'model_outputs_used_to_label_test':False,'family_overlap':0,'normalized_train_vs_holdout_core_overlap':0,
 'counts':{k:len(v) for k,v in allsets.items()},'domains':{k:dict(collections.Counter(t['domain'] for x in v for t in x['label']['tasks'])) for k,v in allsets.items()},
 'focus':{k:dict(collections.Counter(x['label']['focus'] for x in v)) for k,v in allsets.items()},'excluded':excluded,
 'limitation':'Retained domain development pilot with manually reviewed task labels; semantic near-duplicates with unrelated identifiers may remain. R113 rare-domain questions are source-derived development/fixture questions used for training only; no corresponding real-world accuracy claim.'}
(R/'DATASET_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf8')
(R/'LABEL_REVIEW.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),'utf8')
(R/'DATASET_FREEZE.json').write_text(json.dumps({str((R/n).resolve()):hashlib.sha256((R/n).read_bytes()).hexdigest() for n in ['train.jsonl','validation.jsonl','test.jsonl','manual_annotations.py','context_contract.py','DATASET_MANIFEST.json']},indent=2),'utf8')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
