import re

CASES=[
 ('en-identity','en',[('I attached incorrect proof of identity. How do I fix it?','identity_correction')]),
 ('th-identity','th',[('ส่งหลักฐานยืนยันตัวตนผิด ต้องแก้ยังไง','identity_correction')]),
 ('en-passport','en',[('I uploaded the wrong passport document. How do I correct it?','identity_correction')]),
 ('th-student-id','th',[('แนบรูปบัตรนักศึกษาผิด ต้องแก้ยังไง','identity_correction')]),
 ('en-amount','en',[('The payment amount was incorrect. How do I fix it?','wrong_amount')]),
 ('en-amount-order','en',[('The amount I paid was wrong. How can I correct it?','wrong_amount')]),
 ('th-amount','th',[('ยอดเงินที่โอนผิด ต้องแก้ยังไง','wrong_amount')]),
 ('th-amount-order','th',[('ผมชำระจำนวนเงินผิด ต้องแก้ยังไง','wrong_amount')]),
 ('en-proof','en',[('I attached incorrect proof of payment. How do I fix it?','pending'),('yes','slip')]),
 ('th-proof','th',[('แนบหลักฐานชำระเงินผิด ต้องแก้ยังไง','pending'),('ใช่','slip')]),
 ('th-alias-collision','th',[('ผมอัปโหลดรูปหลักฐานโอนเงินผิด ต้องแก้ยังไง','pending'),('ใช่ครับ','slip')]),
 ('en-proof-typo','en',[('I uploded the wrong payment attachement. How can I correct it?','pending'),('yes','slip')]),
 ('en-personal','en',[('Can I bring my own input peripheral?','pending'),('keyboard','personal')]),
 ('th-personal','th',[('ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม','pending'),('ใช่ แต่เป็นเมาส์ของผม','personal')]),
 ('th-rental-pc','th',[('เหมา PC เต็มวัน หน่วยงานภายนอกราคาเท่าไหร่','rental_pc_external_full_day')]),
 ('en-rental-pc','en',[('Full-day PC zone rental for an external organization price','rental_pc_external_full_day')]),
 ('th-rental-vr','th',[('เหมา VR ครึ่งวัน หน่วยงานภายในราคาเท่าไหร่','rental_vr_internal_half_day')]),
 ('en-rental-ps5','en',[('How much is half-day PS5 zone rental for an internal organization?','rental_ps5_internal_half_day')]),
 ('th-rental-all','th',[('เหมาทุกโซนเต็มวันหน่วยงานภายนอกราคาเท่าไหร่','rental_all_zones_external_full_day')]),
 ('en-rental-all','en',[('Full-day all zones rental for external organizations price','rental_all_zones_external_full_day')]),
]
PRICES={'rental_pc_external_full_day':4000,'rental_vr_internal_half_day':1500,'rental_ps5_internal_half_day':500,'rental_all_zones_external_full_day':12000}

def check(body,expect):
 p=(body.get('decision_artifact') or {}).get('query_plan') or {};state=body.get('common_read_state') or {};a=body.get('answer','');errors=[]
 ids=set(p.get('record_ids',[]))|{x['record_id'] for x in p.get('response_projection',[]) if x.get('fields') and x.get('record_id')}
 if not body.get('validation_ok') or not a.strip():errors.append('validation_or_empty')
 if expect=='pending' and not state.get('profile_confirmation'):errors.append('missing_topic_confirmation')
 if expect=='personal' and ('migrated_owner_claim_personal_keyboard_mouse' not in ids or not any(s in a for s in ['ไม่อนุญาต','not allowed'])):errors.append('missing_personal_rule')
 if expect=='slip' and ('procedure_wrong_slip' not in ids or 'facebook.com/psuesportsphuket' not in a):errors.append('missing_slip_procedure')
 if expect in {'identity_correction','wrong_amount'}:
  if state.get('profile_confirmation') or 'procedure_wrong_slip' in ids:errors.append('wrong_slip_menu_or_source')
  if p.get('unconfirmed_topic')!=expect:errors.append('not_specific_unconfirmed_need')
  if p.get('source_answer_confirmed') is True:errors.append('invented_correction_policy')
 if expect in PRICES:
  projected={x['record_id'] for x in p.get('response_projection',[]) if 'amount_minor' in x.get('fields',[])}
  actual={rid for rid in ids if rid.startswith('rental_')}
  if actual!={expect} and projected!={expect}:errors.append('wrong_package_scope')
  if not re.search(r'(?<!\d)'+str(PRICES[expect])+r'(?!\d)',a.replace(',','')):errors.append('missing_source_price')
 return errors
