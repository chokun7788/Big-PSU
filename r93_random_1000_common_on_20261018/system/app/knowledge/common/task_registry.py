"""Data readiness per reusable task. Contains no studio facts or record IDs.

This reports supplied fields/relationships, not intent accuracy or publication
approval. The store's schema/evidence/approval checks remain authoritative.
"""
from .registry import CATALOG,value,aware

VERSION='common_task_readiness_v1'

def clarification_options(kinds,locale):
 """User tasks, rather than raw database field captions."""
 if kinds & {'zone','service','resource','equipment_model'}:
  return ['รายการเกม','อุปกรณ์และสเปก','ราคา','สถานะจอง'] if locale=='th' else ['games','equipment and specifications','prices','booking availability']
 if kinds & {'game','game_service','game_mode','control_set'}:
  return ['เกมเกี่ยวกับอะไร','วิธีเล่น','ปุ่มควบคุม','บริการที่มีเกมนี้'] if locale=='th' else ['game overview','how to play','controls','services offering this game']
 if kinds & {'competition','competition_rule'}:
  return ['ภาพรวมกติกา','กติกาทั้งหมด','กฎเฉพาะเรื่อง'] if locale=='th' else ['rules overview','all rules','a specific rule topic']
 return []
# task key, owner-facing caption, required local fields, optional related kind
TASKS={
 'center':[('center_identity','ชื่อและหน่วยงานผู้ดูแล',['name','operator'],None),('directions','ที่ตั้งและแผนที่',['address','map_url'],None)],
 'contact':[('contact','ช่องทางติดต่อและเรื่องที่ติดต่อได้',['channel','value','purpose'],None)],
 'facility':[('facility_location','ตำแหน่งสิ่งอำนวยความสะดวก',['name','location'],None),('facility_conditions','เงื่อนไขใช้สิ่งอำนวยความสะดวก',['usage_conditions'],None)],
 'zone':[('zone_overview','ภาพรวมโซน',['name','description'],None),('zone_equipment','รายการอุปกรณ์ในโซน',['name'],'zone_equipment')],
 'equipment_model':[('equipment_name','รายการอุปกรณ์',['name','device_type'],None),('equipment_specs','สเปกอุปกรณ์',['specifications'],None)],
 'resource':[('resource_details','ข้อมูลเครื่องและสถานะพร้อมใช้งาน',['name','zone_id','operational_status'],None),('resource_equipment','อุปกรณ์ของเครื่อง',['equipment_model_ids'],None)],
 'service':[('service_session','เวลาเล่นและเวลาที่กันเครื่อง',['name','resource_ids','session_minutes','occupancy_minutes'],None),('service_capacity','จำนวนคนของบริการ',['capacity_min','capacity_max'],None)],
 'game':[('game_overview','เกมเกี่ยวกับอะไร',['title','summary'],None),('game_genre','แนวเกม',['title','genre'],None),('game_how_to_play','วิธีเล่น',['title','how_to_play'],None),('game_controls','ปุ่มควบคุม',['title'],'control_set'),('game_offerings','บริการที่มีเกมนี้',['title'],'game_service')],
 'game_service':[('game_service','เกมที่ให้บริการและบริการที่เกี่ยวข้อง',['game_id','service_id','offered'],None),('installed_resources','เครื่องที่ติดตั้งเกม',['installed_resource_ids'],None)],
 'game_mode':[('game_players','จำนวนคนเล่นในโหมด',['game_id','mode_name','platform','players_min','players_max'],None),('game_network','การเล่นออนไลน์และโหมดที่ศูนย์รองรับ',['network_requirement','studio_supported'],None)],
 'control_set':[('game_controls','ปุ่มควบคุมตามชุดที่ระบุ',['game_id','platform','input_device','preset','bindings'],None)],
 'audience':[('audience_eligibility','คุณสมบัติกลุ่มผู้ใช้',['name','eligibility'],None),('audience_proofs','หลักฐานของกลุ่มผู้ใช้',['required_proofs'],None)],
 'rate':[('fee_quote','ราคาตามกลุ่มและหน่วย',['service_id','audience_id','amount_minor','currency','unit','duration_minutes','calculation_rule'],None)],
 'rental_package':[('rental_quote','ราคาเหมาตามโซน กลุ่ม และแพ็กเกจ',['zone_ids','audience_id','period_label','amount_minor','currency'],None),('rental_duration','จำนวนชั่วโมงของแพ็กเกจ',['duration_minutes'],None),('rental_terms','เงื่อนไขราคาเหมา',['terms'],None)],
 'schedule':[('opening_hours','ช่วงเปิดบริการ',['timezone','zone_ids','weekday','open_periods'],None),('bookable_hours','ช่วงที่จองได้',['timezone','zone_ids','weekday','bookable_periods'],None),('maintenance','ช่วงบำรุงรักษา',['maintenance_periods'],None)],
 'closure':[('special_closure','วันปิดหรือเปลี่ยนเวลาเฉพาะวัน',['local_date','zone_ids','state','reason'],None),('closure_booking_resolution','จัดการรายการจองเมื่อปิดพิเศษ',['resolution_policy_id'],None)],
 'policy':[('policy_decision','ข้อกำหนดและเงื่อนไข',['topic','subject','decision','conditions_all','details'],None),('policy_exceptions','ข้อยกเว้น',['exceptions'],None),('policy_consequence','ผลเมื่อฝ่าฝืน',['consequence'],None)],
 'procedure':[('procedure_steps','ขั้นตอนและเงื่อนไขก่อนเริ่ม',['topic','preconditions','steps'],None),('procedure_documents','เอกสารที่ใช้',['required_documents'],None),('procedure_deadline','กำหนดเวลา',['deadline_minutes'],None)],
 'competition':[('competition_identity','รายการและฉบับกติกา',['game_id','event_name','rulebook_release','coverage'],None),('competition_rules','ข้อกติกาในเล่ม',['event_name'],'competition_rule')],
 'competition_rule':[('competition_clause','ข้อกติกาและขอบเขต',['competition_id','section_number','facet','heading','text','completeness'],None)],
 'news':[('news_content','ข่าวและรายละเอียด',['title','body'],None),('event_dates','วันจัดกิจกรรม',['event_start','event_end'],None)],
 'person':[('person_public_details','ชื่อและบทบาทที่อนุญาตให้เผยแพร่',['display_name','role','public_scope'],None)],
 'faq':[('faq_content','คำตอบของหัวข้อ',['question','answer','topic'],None)],
 'live_binding':[('live_mapping','การผูกบริการกับระบบสถานะสด',['service_id','provider','external_resource_key','physical_pool_key','status_mapping','timezone','freshness_policy'],None)]
}

def _field(record,key,lang):
 field=record.get('fields',{}).get(key,{})
 if field.get('status')!='known' or field.get('value') is None:return field.get('status','unknown')
 v=field['value']
 if isinstance(v,dict) and set(v)=={'th','en'} and not v.get(lang):return 'missing_language'
 return None

def readiness(record,records,*,locale='th',at=None):
 if not isinstance(record,dict) or record.get('kind') not in CATALOG or not isinstance(record.get('fields'),dict):raise ValueError('A record with a registered kind and fields is required')
 from app.calendar.service_calendar import now_bangkok
 at=at or now_bangkok();lang='en' if locale=='en' else 'th';kind=record['kind'];rid=record.get('record_id')
 scope={**records,rid:record} if rid else records
 results=[]
 for task,label,required,related in TASKS[kind]:
  missing=[{'field':key,'reason':reason} for key in required if (reason:=_field(record,key,lang))]
  # Check actual reference existence; do not resolve business relationships
  # from similar display names or invent a new related record.
  for key in required:
   spec=next(f for f in CATALOG[kind]['fields'] if f['key']==key)
   if not spec['reference_kind'] or _field(record,key,lang):continue
   refs=value(record,key);refs=refs if isinstance(refs,list) else [refs]
   for target in refs:
    if target not in scope or scope[target].get('lifecycle')=='withdrawn':missing.append({'field':key,'reason':'missing_reference','record_id':target})
  related_ids=[]
  if related=='zone_equipment':
   for r in records.values():
    if r['kind']=='resource' and value(r,'zone_id')==rid:
     related_ids.extend(x for x in value(r,'equipment_model_ids') or [] if x in records)
   if not related_ids:missing.append({'relation':related,'reason':'no_explicit_resource_equipment_relation'})
  elif related:
   foreign={'control_set':'game_id','game_service':'game_id','competition_rule':'competition_id'}[related]
   related_ids=[key for key,r in records.items() if r['kind']==related and value(r,foreign)==rid]
   if not related_ids:missing.append({'relation':related,'reason':'missing_related_records'})
   elif related=='control_set' and not any(all(_field(records[key],f,lang) is None for f in ['platform','input_device','preset','bindings']) for key in related_ids):missing.append({'relation':related,'reason':'related_records_incomplete'})
  warnings=[];state='needs_data' if missing else 'data_ready'
  if task in {'fee_quote','rental_quote'}:
   validity=record.get('validity',{})
   if validity.get('state')!='known':
    warnings.append('current_price_effective_dates_not_confirmed')
    if not missing:state='needs_effective_dates'
   else:
    start=validity.get('effective_from');end=validity.get('effective_until')
    if start and at<aware(start) or end and at>=aware(end):state='not_current';warnings.append('outside_effective_interval')
  results.append({'task':task,'label_th':label,'status':state,'missing':missing,'warnings':warnings,'related_ids':list(dict.fromkeys(related_ids))})
 core=[f['key'] for f in CATALOG[kind]['fields'] if f['publish_core']]
 return {'version':VERSION,'kind':kind,'record_id':rid,'tasks':results,
  'publish_core_missing':[key for key in core if _field(record,key,lang)],
  'scope':'data readiness only; store validation and runtime interpretation still required',
  'publication_approval_created':False,'runtime_answer_correctness_verified':False}
