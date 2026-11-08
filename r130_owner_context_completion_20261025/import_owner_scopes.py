"""Curate new draft cards. Never revise/approve the inherited 824 records."""
import copy,hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.domain_flow.source_decisions import digest
ORIGIN=B/'r107_owner_questions_20261020/owner_update_50'
original=json.loads((ORIGIN/'SOURCE_OWNER_50.json').read_text('utf8'))
prefill=json.loads((ORIGIN/'PREFILL_PAYLOAD.json').read_text('utf8'))
later=json.loads((B/'r109_owner_answers_20261020/SOURCE_STATE.json').read_text('utf8'))
store=CommonStore(R/'system/data/knowledge/common.sqlite')
with store.connect() as c:
 before=store.heads(c);approvals=[tuple(x) for x in c.execute('SELECT * FROM cc_approvals ORDER BY record_id,version')]
 old_hashes={k:digest(v) for k,v in before.items() if not k.startswith('r130_owner_')}
items={i['number']:i for i in original['source_items']}
cards=[]
def card(n,cat,th,en,all_patterns=(),none=(),partial=False,limits=(),claim='policy',numbers=False):
 cards.append(dict(number=n,category=cat,answer={'th':th,'en':en},all=list(all_patterns),none=list(none),partial=partial,limits=list(limits),claim_class=claim,numbers_allowed=numbers))

card(12,'C04',
 'สำหรับมา 2 คน เจ้าของแนะนำเกมดังนี้\n\n**PS5**\n- SF6\n- Tekken 8\n- Naruto\n- FC24\n\n**Nintendo Switch**\n- It Takes Two\n- Luigi’s Mansion 3\n- Mario Kart 8 Deluxe\n- Mario Party Superstars\n- Moving Out 2\n- New Super Mario Bros. U Deluxe\n- Nintendo Switch Sports\n- Overcooked!\n- Overcooked! 2\n- Super Mario Odyssey\n- Super Smash Bros Ultimate\n\nรายการนี้เป็นคำแนะนำจากเจ้าของ ยังไม่ยืนยันโหมดเล่นพร้อมกันของแต่ละเกมหรือรุ่นของชื่อย่อ SF6/Naruto ส่วน PC เจ้าของให้ตรวจรายการอีกครั้ง จึงยังไม่ยืนยันว่าเล่นสองคนได้ทุกเกมครับ',
 'For a visit by two people, the owner recommends:\n\n**PS5**\n- SF6\n- Tekken 8\n- Naruto\n- FC24\n\n**Nintendo Switch**\n- It Takes Two\n- Luigi’s Mansion 3\n- Mario Kart 8 Deluxe\n- Mario Party Superstars\n- Moving Out 2\n- New Super Mario Bros. U Deluxe\n- Nintendo Switch Sports\n- Overcooked!\n- Overcooked! 2\n- Super Mario Odyssey\n- Super Smash Bros Ultimate\n\nThese are owner recommendations, not verified simultaneous-player modes or resolved editions for SF6/Naruto. The PC list still needs checking; this does not confirm every PC game supports two players.',
 [r'2\s*(?:คน|people|players)',r'เล่น|เกม|play|games?',r'อะไร|ไหน|แนะนำ|what|which|recommend'],
 [r'แบ่งจอ|พร้อมกัน|co.?op|split.?screen|local|online|ออนไลน์|ออฟไลน์|ทุกเกม|all games|กี่จอย|เปรียบ|เทียบ'],True,
 ['recommendations_not_modes','pc_inventory_unconfirmed','abbreviated_editions_not_inferred'],claim='group_recommendation',numbers=True)
card(13,'C04','มากัน 4 คน เจ้าของแนะนำ Nintendo Switch ครับ เป็นคำแนะนำบริการ ยังไม่ได้ยืนยันโหมดของแต่ละเกม','For four visitors, the owner recommends Nintendo Switch. This service recommendation does not establish each game’s player mode.',[r'4\s*(?:คน|people|players)',r'เลือก|แนะนำ|recommend|choose'],[r'พร้อมกัน|ทุกเกม|split.?screen|co.?op'],limits=['recommendation_not_game_mode'],claim='group_recommendation',numbers=True)
card(14,'C08','มา 4 คนแล้วจองบริการสำหรับ 2 คนเพื่อสลับกันเล่นไม่ได้ครับ','Four visitors cannot book a two-person service and rotate players.',[r'สลับ|rotate|take turns',r'4\s*(?:คน|people|players)',r'2\s*(?:คน|people|players)'],numbers=True)
card(15,'C10','ขอให้ศูนย์ลงเกมเพิ่มได้ โดยศูนย์จะพิจารณาเป็นรายรายการครับ ยังไม่ได้ระบุช่องทาง ค่าใช้จ่าย หรือรับประกันว่าจะเพิ่มทุกเกม','You may ask the studio to add a game; requests are considered individually. The channel and cost are not established, and installation is not guaranteed.',[r'เกม|games?',r'ลงเพิ่ม|เพิ่มเกม|ขอ.*ลง|request.*(?:add|install)|add.*request'],[r'ติดตั้งเอง|ลงเอง|install.*myself|mod|ค่าใช้จ่าย|ช่องทาง|contact|cost'],limits=['request_channel_and_cost_unknown','not_installation_permission'])
card(21,'C08','ถ้ามาไม่ทัน ให้แจ้งผู้จัดการศูนย์ผ่าน Discord ศูนย์อีสปอร์ต หรือเพจศูนย์อีสปอร์ตครับ','If you cannot arrive in time, notify the studio manager through the studio Discord or Facebook page.',[r'ไม่ทัน|มาสาย|ไปสาย|arrive late|running late',r'แจ้งใคร|ติดต่อใคร|notify|contact'],[r'กี่นาที|15|สิบห้า'])
card(25,'C10','ต้องตรวจสาเหตุครับ ถ้าเครื่องขัดข้องโดยไม่ได้เกิดจากผู้ใช้ ให้คิดตามเวลาจริง แต่ถ้าเกิดจากผู้เล่นจะไม่มีการต่อเวลา ให้แจ้งเจ้าหน้าที่ตรวจสอบครับ','The cause must be checked. If the computer fault was not caused by the user, charges follow actual play time. If caused by the player, no extension is provided. Notify staff for inspection.',[r'เครื่องค้าง|เครื่องดับ|ค้างหรือดับ|ขัดข้อง|computer.*(?:crash|fault)|system fault',r'เวลา|คิด|ชดเชย|time|charg|compensat'],[r'รับประกัน|กี่นาที|คืนเงิน|refund'],limits=['cause_requires_staff_check','extension_amount_not_inferred'])
card(26,'C10','หากลืมออกจากบัญชีหลังเล่น ให้แจ้งผู้จัดการศูนย์ผ่าน Discord ศูนย์อีสปอร์ต หรือเพจศูนย์อีสปอร์ตครับ','If you forgot to log out after playing, contact the studio manager through the studio Discord or Facebook page.',[r'ลืม|forgot',r'บัญชี|ออกจากระบบ|log.?out|account',r'ติดต่อ|แจ้ง|ทำยังไง|contact|notify|what.*do'],[r'เก็บข้อมูล|ปลอดภัย|retain|security|password'],limits=['contact_action_not_technical_security_guarantee'])
card(27,'C10','นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ได้ แต่ต้องแจ้งเจ้าหน้าที่ก่อนใช้ครับ ใช้สำหรับบริการศูนย์ทั่วไป ส่วนกฎการแข่งขันต้องตรวจแยกตามรายการ','Personal keyboards and mice may be used, but notify staff before use. This applies to general studio service; tournament equipment rules must be checked separately.',[r'คีย์บอร์ด|เมาส์|keyboard|mouse|mice',r'ตัวเอง|ส่วนตัว|my own|personal|own',r'มาใช้|นำมา|เอามา|ได้ไหม|ได้มั้ย|bring|use|allowed'],[r'ไฟ|power|ราคา|เช่า|rent|แจ้ง.*กี่|how.*notify'],limits=['general_studio_only','not_tournament_rule'])
# The original says notify, without a timing deadline; do not invent one.
cards[-1]['answer']['th']=cards[-1]['answer']['th'].replace('แจ้งเจ้าหน้าที่ก่อนใช้','แจ้งเจ้าหน้าที่')
cards[-1]['answer']['en']=cards[-1]['answer']['en'].replace('notify staff before use','notify staff')
cards[-1]['answer']['th']=cards[-1]['answer']['th'].replace('ต้องแจ้งเจ้าหน้าที่','ต้องแจ้ง')
cards[-1]['answer']['en']=cards[-1]['answer']['en'].replace('but notify staff','with notification required')
card(30,'C10','ผู้ใช้ติดตั้งเกม โปรแกรม หรือ mod เองไม่ได้ครับ หากต้องการเกมเพิ่ม ขอให้ศูนย์พิจารณาเป็นรายรายการได้','Users cannot install games, programs or mods themselves. You may ask the studio to consider adding a game.',[r'ติดตั้ง|ลง|install',r'เอง|myself|ourselves|on my own',r'เกม|โปรแกรม|mod|game|program|software'],[r'ราคา|cost'])
card(32,'C03','จำนวนที่นั่งที่ระบุสำหรับบริการ หมายถึงจำนวนคนที่เล่นพร้อมกันได้ครับ ไม่ใช่จำนวนที่นั่งทั้งหมดในห้อง','The seating count stated for a service means simultaneous players, rather than all physical seats in the room.',[r'ที่นั่ง|seats?|seating',r'หมายถึง|คือจำนวน|เล่นพร้อมกันหรือ|meaning|mean|or.*room'],[r'กี่คน|กี่ที่|how many'],claim='capacity_definition')
card(34,'C10','ไม่ให้ยืมบัญชีของศูนย์ไปใช้นอกศูนย์ครับ บัญชีศูนย์ใช้เล่นเฉพาะที่ศูนย์ โดยมีบัญชี Steam ให้ใช้ หรือใช้ Steam ส่วนตัวก็ได้ ส่วนบัญชีแพลตฟอร์มอื่นยังไม่ยืนยัน','Studio accounts are not lent for use outside the studio. A studio Steam account is available onsite, and you may use your own Steam account. Other platform accounts are not established.',[r'บัญชี|accounts?',r'ยืม|borrow|lend'],[r'psn|nintendo|password|รหัสผ่าน'],limits=['onsite_only','other_platform_accounts_unconfirmed'])
card(35,'C10','ศูนย์อัปเดตเกมทุกวันจันทร์เช้าครับ แต่ตารางอัปเดตไม่ได้ยืนยันว่าเครื่องนี้เป็นเวอร์ชันล่าสุดแล้ว ต้องสอบถามผู้ดูแลเพื่อตรวจเวอร์ชันปัจจุบัน','The studio updates games on Monday mornings. This schedule does not confirm that a particular machine is on the latest version; ask the supervisor to check the current version.',[r'เกม|games?',r'อัปเดต|อัพเดต|update|version|เวอร์ชัน',r'ล่าสุด|แล้วหรือยัง|แล้วหรือ|เมื่อไร|วันไหน|latest|up.to.date|when'],[r'เปลี่ยนเครื่อง|เวลา.*เริ่ม|start.*time|compensat|ชดเชย|กี่นาที'],True,['current_version_requires_live_or_staff_check'],claim='update_schedule_not_live_version')
card(37,'C10','กรณีเกมกำลังอัปเดต เปลี่ยนไปใช้เครื่องอื่นไม่ได้ครับ กฎนี้แยกจากกรณีเปิดเกมไม่ได้ด้วยสาเหตุอื่น','You cannot switch to another machine while the game is updating. This is separate from failure to run for other reasons.',[r'อัปเดต|อัพเดต|updat',r'เปลี่ยน|ย้าย|switch|change',r'เครื่อง|machine|computer|station'],[r'ไม่ใช่.*อัปเดต|not.*updat'])
card(38,'C08','ชื่อจริงและข้อมูลต้องตรงกับบัตรที่ใช้ยืนยันครับ','Your real name and information must match the identification used for verification.',[r'ชื่อจริง|ชื่อ.*ตรง.*บัตร|real name|name.*match',r'บัตร|ตรง|identification|\bid\b|match'],[r'แก้|เปลี่ยนชื่อ|change|correct'])
card(39,'C08','กรอกเบอร์โทรผิดไม่ต้องจองใหม่ครับ แต่อีเมลต้องถูกต้อง คำตอบนี้ยังไม่ได้ระบุวิธีแก้ไขเบอร์ในระบบ','A wrong phone number does not require rebooking, but the email must be correct. The method for editing the phone number is not established.',[r'เบอร์โทร|เบอร์.*ผิด|phone',r'ผิด|wrong|incorrect',r'จองใหม่|rebook'],[r'แก้.*ยังไง|how.*edit'],limits=['editing_method_unknown'])
card(40,'C09','โอนจากบัญชีเพื่อนที่ไม่มีชื่อเป็นผู้เล่นร่วมไม่ได้ครับ ถ้าเพื่อนมีชื่อเป็นผู้เล่นร่วมจึงอยู่ในข้อยกเว้นที่เจ้าของให้ไว้ และคำตอบเพิ่มเติมระบุให้โอนจากคนที่ลงชื่อเพียงคนเดียว','Payment from a friend who is not named as a co-player is not allowed. The owner allows the exception for a named co-player, and the follow-up specifies a single named payer.',[r'บัญชี.*เพื่อน|เพื่อน.*โอน|friend',r'โอน|จ่าย|pay|transfer'],[r'หลายคน.*แบ่ง|split.*payment|คืนเงิน|refund'],limits=['named_payer_only','no_extra_note_procedure_inferred'])
card(42,'C09','โอนขาดต้องโอนเพิ่มครับ ให้ติดต่อเพจ Facebook ศูนย์ พร้อมสลิปโอนเงินและหลักฐานการจองเพื่อตรวจสอบ','An underpayment must be topped up. Contact the studio Facebook page with the transfer slip and booking evidence for verification.',[r'โอนขาด|จ่ายขาด|underpay|paid.*less|short.*payment'],limits=['no_automatic_payment_confirmation'])
card(46,'C09','กรณีขอเลื่อนเป็นวันอื่นแทนการคืนเงิน ทำไม่ได้ครับ ข้อนี้ไม่ใช่กรณีจองผิดวันและชำระแล้ว ซึ่งมีขั้นตอนแก้แยกต่างหาก','Rescheduling to another day instead of receiving a refund is not allowed. A paid booking made for the wrong day is a separate case with its own procedure.',[r'เลื่อน|เปลี่ยนวัน|reschedul|another day',r'แทน.*คืนเงิน|instead.*refund'],limits=['not_paid_wrong_day_case'])
card(48,'C08','ฝนตกหนักจนเดินทางไม่ได้ ขอเปลี่ยนรอบได้แต่ต้องแจ้งล่วงหน้าตามกฎครับ ให้ติดต่อเพจ Facebook พร้อมสลิปและหลักฐานการจอง ยังไม่ได้ระบุระยะเวลาแจ้งล่วงหน้าเป็นตัวเลขสำหรับกรณีนี้','If heavy rain prevents travel, you may request a session change with advance notice under the rules. Contact the Facebook page with the slip and booking evidence. A numeric notice period for this case is not established.',[r'ฝนตก|ฝนหนัก|heavy rain|rainstorm',r'เปลี่ยน|เลื่อน|เดินทางไม่ได้|reschedul|change|cannot travel'],[r'กี่ชั่วโมง|กี่นาที|how many'],limits=['advance_notice_required','numeric_notice_period_not_inferred'])
card(49,'C08','เช็กอินแทนทั้งกลุ่มไม่ได้ครับ ต้องตรวจเป็นรายคน แต่คนที่มาถึงก่อนสามารถเล่นได้','You cannot check in for the whole group. Each person is checked individually, but those who arrive first may play.',[r'เช็กอิน|เช็คอิน|check.?in',r'แทน|ทั้งกลุ่ม|on behalf|whole group'],limits=['individual_checkin'])
card(50,'C01','มีที่นั่งพักตรงโซนกลางห้องครับ','Rest seating is available in the central area of the room.',[r'ที่นั่งพัก|ที่พักนั่ง|rest seating|rest area|waiting seats'],[r'ตอนนี้|ว่าง|จอง|available|free|booking'],claim='static_facility')
card(20,'C08','ยังไม่มีคำตอบยืนยันว่ามาสาย 15 นาทีแล้วยังเล่นได้หรือไม่ครับ หากมาไม่ทันให้แจ้งผู้จัดการศูนย์ผ่าน Discord หรือเพจศูนย์อีสปอร์ต','Whether you can still play after arriving 15 minutes late is not confirmed. If you cannot arrive in time, notify the studio manager through Discord or the Facebook page.',partial=True,limits=['fifteen_minute_admission_not_confirmed'],claim='contact_not_admission_guarantee')
card(47,'C08','กรณีศูนย์ปิดหลังจอง ข้อมูลเพิ่มเติมระบุว่าศูนย์ติดต่อผ่านอีเมล Gmail ที่ใช้สมัครครับ แต่ยังไม่ยืนยันว่าจะคืนเงิน เปลี่ยนรอบ หรือจัดการรายการอย่างไร','For a closure after booking, the follow-up says the studio contacts the Gmail address used to register. Refund, rescheduling and booking disposition are not established.',partial=True,limits=['closure_disposition_unconfirmed'],claim='notification_not_refund_or_reschedule')

out=[]
for c in cards:
 n=c['number'];rid=f'r130_owner_{n:02d}_scoped';item=items[n]
 forms={k:v for k,v in prefill['answers'].items() if n in v.get('source_items',[])}
 evidence=[{'path':str(ORIGIN/'SOURCE_OWNER_50.json'),'sha256':hashlib.sha256((ORIGIN/'SOURCE_OWNER_50.json').read_bytes()).hexdigest(),'pointer':'/source_items/'+str(n-1),'value':item}]
 for k,v in forms.items():
  evidence.append({'path':str(ORIGIN/'PREFILL_PAYLOAD.json'),'sha256':hashlib.sha256((ORIGIN/'PREFILL_PAYLOAD.json').read_bytes()).hexdigest(),'pointer':'/answers/'+k,'value':v})
  if k in later['responses']['answers']:
   evidence.append({'path':str(B/'r109_owner_answers_20261020/SOURCE_STATE.json'),'sha256':hashlib.sha256((B/'r109_owner_answers_20261020/SOURCE_STATE.json').read_bytes()).hexdigest(),'pointer':'/responses/answers/'+k,'value':later['responses']['answers'][k]})
 for other in {20:[21],30:[15],34:[24],46:[45]}.get(n,[]):
  evidence.append({'path':str(ORIGIN/'SOURCE_OWNER_50.json'),'sha256':hashlib.sha256((ORIGIN/'SOURCE_OWNER_50.json').read_bytes()).hexdigest(),'pointer':'/source_items/'+str(other-1),'value':items[other]})
 if n==47:
  # This follow-up has a separate intake question; do not treat the original
  # "I don't understand" as an affirmative closure policy.
  extra=before.get('r114_q010_owner_policy')
  if extra:
   with store.connect() as cx:
    pairs=store.sources(cx)
   evidence.append({'pointer':'/recorded_followup/r114_q010_owner_policy','value':extra,'source_pairs':{ref['source_id']:pairs[ref['source_id']] for ref in extra['fields']['answer'].get('evidence_refs',[])}})
 d={'version':1,'category':c['category'],'scope':'general_studio','claim_class':c['claim_class'],'partial':c['partial'],'limits':c['limits'],'original_evidence':evidence,'question_aliases':[items[11]['question']] if n==12 else [],'match':{'all':c['all'],'none':c['none'],'numbers_allowed':c['numbers_allowed']},'policy_effective_date_not_inferred_from_submission_date':True,'corrections':[]}
 if n==27:
  for oldrid,field in [('migrated_owner_claim_personal_keyboard_mouse','answer'),('policy_personal_keyboard_mouse','decision')]:
   old=before[oldrid]
   d['corrections'].append({'record_id':oldrid,'field':field,'revision':old['revision'],'field_sha256':digest(old['fields'][field]),'correction_kind':'migration_error','owner_source_pointer':'/answers/Q044','owner_correction_quote':prefill['answers']['Q044']['note']})
 profile={'route_category':c['category'],'projected_facet':'group_recommendations' if c['claim_class']=='group_recommendation' else 'owner_policy','source_decision':d}
 mapped={'question':{'th':item['question'],'en':''},'answer':c['answer'],'legacy_search':profile,'topic':'owner_scoped','intent_key':f'owner.scoped_{n:02d}'}
 body=json.dumps({'mapped_fields':mapped,'original_evidence':evidence,'curation':'Faithful scoped owner answers; no approvals or effective dates inferred.'},ensure_ascii=False,sort_keys=True)
 sid=f'r130_owner_scope_{n:02d}_'+hashlib.sha256(body.encode()).hexdigest()[:12];source={'source_id':sid,'kind':'derived_curated','path':str(R/'OWNER50_MAPPING.json')+f'#{n}','sha256':hashlib.sha256(body.encode()).hexdigest(),'authority_for':['faq','policy'],'observed_at':'2026-10-25T12:00:00+07:00','trust':'internal_verified','public_url':None}
 store.add_source(source,body,actor='r130_source_scope_curation')
 record=json.loads((R/'system/app/knowledge/common/templates/faq.draft.json').read_text('utf8'));record['record_id']=rid
 for k,v in mapped.items():record['fields'][k]={'status':'known','value':v,'evidence_refs':[{'source_id':sid,'locator':'/mapped_fields/'+k}],'note':'Source-scoped draft mapping; original intake and approvals unchanged.'}
 if rid not in before or store.get(rid)['record']['fields']!=record['fields']:
  store.save(record,actor='r130_source_scope_curation',expected_version=before[rid]['revision'] if rid in before else 0,change_note='Curate new scoped draft only; inherited records unchanged. No deployment.')
 out.append({'number':n,'record_id':rid,'source_id':sid,'source_sha256':source['sha256'],'decision':d,'answer':c['answer']})
with store.connect() as c:
 after=store.heads(c);assert old_hashes=={k:digest(v) for k,v in after.items() if k in old_hashes}
 assert approvals==[tuple(x) for x in c.execute('SELECT * FROM cc_approvals ORDER BY record_id,version')]
(R/'OWNER50_MAPPING.json').write_text(json.dumps({'appended_draft_cards':len(out),'mappings':out,'original_records_unchanged':True,'original_approvals_unchanged':True,'production_deployed':False},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'appended_draft_cards':len(out),'old_active_records_preserved':len(old_hashes),'old_approvals_preserved':len(approvals)}))
