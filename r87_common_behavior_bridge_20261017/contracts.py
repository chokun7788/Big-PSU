import importlib.util,re
from pathlib import Path
spec=importlib.util.spec_from_file_location('r84_contracts',Path(__file__).resolve().parent.parent/'r84_correction_scope_rental_20261017/contracts.py')
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
CASES=old.CASES+[
 ('th-rental-followup','th',[('เหมา PC เต็มวันหน่วยงานภายนอกราคาเท่าไหร่','rental_pc_external_full_day'),('แล้วครึ่งวันล่ะ','rental_pc_external_half_day'),('ภายใน','rental_pc_internal_half_day')]),
 ('en-rental-followup','en',[('Full-day PC zone rental for an external organization price','rental_pc_external_full_day'),('What about half-day?','rental_pc_external_half_day'),('internal','rental_pc_internal_half_day')]),
 ('th-rental-compound','th',[('เหมา PC เต็มวันหน่วยงานภายนอก และ VR ครึ่งวันหน่วยงานภายในราคาเท่าไหร่',('packages','rental_pc_external_full_day','rental_vr_internal_half_day'))]),
 ('en-rental-compound','en',[('PC full-day rental for external organizations and VR half-day rental for internal units price',('packages','rental_pc_external_full_day','rental_vr_internal_half_day'))]),
 ('th-rental-detail','th',[('เหมา PC ครึ่งวันหน่วยงานภายนอกราคาเท่าไหร่','rental_pc_external_half_day'),('มีอุปกรณ์อะไรให้บ้าง',('contains','PC 10')),('แล้วจองยังไง',('unknown','rental'))]),
 ('en-rental-detail','en',[('PC half-day rental for external organizations price','rental_pc_external_half_day'),('What equipment is included?',('contains','10 PC')),('How do I book it?',('unknown','rental'))]),
 ('en-rental-hours','en',[('How many hours is a half-day PC zone rental for internal units?',('unknown','minutes'))]),
 ('th-rental-hourly','th',[('เหมา PC รายชั่วโมงเท่าไหร่',('unknown','hourly'))]),
 ('th-rental-unknown','th',[('เหมา PS6 เต็มวันราคาเท่าไหร่',('status','unknown_target'))]),
 ('en-rental-modified','en',[('Rent the whole studio except VR for a full day',('status','custom_package'))]),
 ('th-routing-advance','th',[('ต้องจองล่วงหน้ากี่ชั่วโมง',('intent','booking_advance_time','1'))]),
 ('en-routing-advance','en',[('How far in advance must I reserve?',('intent','booking_advance_time','1'))]),
 ('rules-rov','th',[('ROV สรุปกติกาสั้นๆ',('summary','rov'))]),
 ('rules-cs2','th',[('กติกา CS2 เรื่องการประท้วงและข้อพิพาท ว่าอย่างไร',('protest','th'))]),
 ('rules-rov-en','en',[('Give me a brief overview of RoV competition rules',('summary','rov'))]),
 ('rules-cs2-en','en',[('CS2 competition rules: who can submit a protest and when?',('protest','en'))]),
 ('rules-cs2-mixed','th',[('กติกา CS2 ต้องประท้วงภายในกี่นาที แล้วใช้ภาษาอะไร',('contains','15','ภาษาไทย'))]),
 ('rules-rov-all','th',[('ขอกติกา ROV ทั้งหมดทุกข้อ',('full_rules','rov'))]),
 ('controls-mario','th',[('Mario Party Superstars ปุ่มเล่นบอร์ดและมินิเกมด้วยปุ่มกดอะไร',('contains_any','Button controls','เล่นบอร์ด'))]),
 ('description-animal','th',[('Animal Crossing: New Horizons คือเกมอะไร',('contains_any','เกาะ','island'))]),
 ('equipment-switch','th',[('Nintendo Switch Zone มีอุปกรณ์อะไรบ้าง',('contains_any','OLED','Sofa','โซฟา'))]),
]
PRICES={**old.PRICES,'rental_pc_external_half_day':2000,'rental_pc_internal_half_day':1000}
def check(body,expect):
 if isinstance(expect,str) and expect not in PRICES:return old.check(body,expect)
 p=(body.get('decision_artifact') or {}).get('query_plan') or {};a=body.get('answer','');errors=[]
 if not body.get('validation_ok') or not a.strip():errors.append('validation_or_empty')
 ids={x['record_id'] for x in p.get('response_projection',[]) if 'amount_minor' in x.get('fields',{})}
 if not ids:ids={x for x in p.get('record_ids',[]) if x.startswith('rental_')}
 if isinstance(expect,str):
  if ids!={expect}:errors.append('wrong_package_scope')
  if str(PRICES[expect]) not in a.replace(',',''):errors.append('wrong_or_missing_price')
 elif expect[0]=='packages':
  if ids!=set(expect[1:]):errors.append('mixed_clause_scope')
  if any(str(PRICES[x]) not in a.replace(',','') for x in expect[1:]):errors.append('missing_compound_price')
 elif expect[0]=='contains':
  if not all(s.lower() in a.lower() for s in expect[1:]):errors.append('missing_required_content')
 elif expect[0]=='contains_any':
  if not any(s.lower() in a.lower() for s in expect[1:]):errors.append('missing_substantive_content')
 elif expect[0]=='unknown':
  if not any(s in a.lower() for s in ['ยังไม่มี','ไม่ระบุ','not confirmed','does not confirm']):errors.append('missing_precise_unknown')
  if p.get('legacy_fact_fallback_used'):errors.append('legacy_facts_used')
 elif expect[0]=='status':
  if p.get('bridge_status')!=expect[1]:errors.append('wrong_scope_status')
 elif expect[0]=='intent':
  diagnostics=(body.get('decision_artifact') or {}).get('query_resolution') or []
  # The named source can already answer directly; either route must retain
  # the requested booking fact, never an unrelated generic response.
  if not any(expect[1] in str(x) for x in diagnostics) and not any('advance' in rid for rid in p.get('record_ids',[])):errors.append('wrong_routing_intent')
  if not re.search(r'(?<!\d)'+re.escape(expect[2])+r'\s*(?:ชั่วโมง|hours?)',a,re.I):errors.append('missing_source_duration_not_citation_number')
 elif expect[0]=='domain':
  if 'competition' not in str(p).lower() or 'booking' in str(p.get('record_ids',[])).lower():errors.append('wrong_competition_domain')
 elif expect[0]=='summary':
  if p.get('method')!='common_legacy_clause_overview':errors.append('not_bounded_clause_overview')
  facets={c['facet'] for c in p.get('clause_selection',[])}
  if len(facets)<3:errors.append('insufficient_summary_topic_diversity')
  if len(a)>2400:errors.append('short_summary_too_long')
  if p.get('summary_is_complete') is not False:errors.append('false_summary_completeness')
  if not any(expect[1] in rid.lower() for rid in p.get('scope_ids',[])):errors.append('wrong_rulebook')
 elif expect[0]=='protest':
  required=('15','หลังจากจบแมตช์','กัปตัน','โค้ช') if expect[1]=='th' else ('15','after the match','captain','coach')
  if not all(s.lower() in a.lower() for s in required):errors.append('protest_condition_missing')
  if re.search(r'ภาษาทางการ|การบริหารจัดการ|อำนาจตัดสิน|official language|Judging Authority',a,re.I):errors.append('unrequested_protest_facet_dump')
  if p.get('method')!='common_legacy_proposition_detail':errors.append('missing_proposition_scope')
 elif expect[0]=='full_rules':
  if p.get('method')=='common_legacy_clause_overview' or not p.get('rule_content_all'):errors.append('full_request_truncated_to_summary')
  if len({rid for row in p.get('rule_selection',[]) for rid in row.get('selected_ids',[])})<12:errors.append('missing_full_source_sections')
 return errors
