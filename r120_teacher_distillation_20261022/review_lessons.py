"""Record semantic review of teacher-to-native task mappings, not facts."""
import copy,json,re
from pathlib import Path
R=Path(__file__).resolve().parent
data=json.loads((R/'TEACHER_LESSONS.json').read_text('utf8'));(R/'TEACHER_LESSONS_PRE_REVIEW.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),'utf8')
decisions=[];keep=[]
for e in data['examples']:
 q=e['question'];t=e['plan']['tasks'][0];before=copy.deepcopy(t);reason=None
 if re.search(r'แล้วจองยังไง',q):reason='quarantined_compound_teacher_label_drops_booking_need'
 elif re.search(r'1 hour or 2 hours',q):reason='quarantined_alternative_duration_not_a_single_scalar_plan'
 elif '1a8ef7b8'==e['id'][:8]:reason='quarantined_teacher_contact_map_route_for_explicit_cs2_rulebook_request'
 if reason:decisions.append({'key':e['id'],'decision':reason,'question':q,'original_plan':before});continue
 if re.search(r'Who is.*intern|ตำแหน่ง|\brole\b',q,re.I) and t['domain']=='contact':t.update(domain='members',facet='role',operation='role_lookup')
 if t['domain']=='equipment':
  if re.search(r'คืออะไร|what is',q,re.I):t['facet']='usage'
  if re.search(r'มีอุปกรณ์อะไรบ้าง',q):t['operation']='list'
 if re.search(r'how do i pay',q,re.I):t.update(domain='payment',facet='owner_policy',operation='detail')
 if re.search(r'คนภายนอก.*ได้ไหม|public visitor.*membership',q,re.I):t.update(domain='rules',facet='owner_policy',operation='detail')
 if re.search(r'เปิดจองวันไหน|afternoon session',q,re.I):t.update(domain='schedule',facet='bookable_periods',operation='detail')
 if re.search(r'ถ้าจะเล่น.*ต้องจองอะไร',q):t.update(domain='games',facet='studio_services',operation='detail')
 if re.search(r'รอบละกี่นาที',q):t.update(domain='service_fee',facet='duration_minutes',operation='detail')
 if t['domain']=='game_controls' and re.search(r'มีอะไรบ้าง|ทั้งหมด|\ball\b',q,re.I):t['operation']='list'
 e['reviewed_native_mapping']=True;keep.append(e)
 if t!=before:decisions.append({'key':e['id'],'decision':'mapped_legacy_task_to_native_domain_and_requested_field','question':q,'before':before,'after':copy.deepcopy(t)})
data['examples']=keep;data['semantic_mapping_review']='teacher route/mode plus request predicate reviewed; teacher business facts still excluded'
(R/'TEACHER_LESSONS.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),'utf8')
(R/'TEACHER_MAPPING_REVIEW.json').write_text(json.dumps({'teacher_runs':64,'accepted_examples':len(keep),'quarantined':64-len(keep),'decisions':decisions,'weights_changed':False},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'accepted_examples':len(keep),'quarantined':64-len(keep),'review_decisions':len(decisions)}))
