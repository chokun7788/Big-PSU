"""Create research-only schemas/forms/examples. Never writes the actual project."""
from pathlib import Path
import json, hashlib, csv
from datetime import datetime, timezone
OUT=Path(__file__).resolve().parent
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
VERSION='studio-content-3.0-design'
def dump(path,value):
    p=OUT/path; p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def obj(properties): return {'type':'object','properties':properties,'required':list(properties),'additionalProperties':False}
S={'type':'string','minLength':1}; B={'type':'boolean'}; N={'type':'integer','minimum':0}
POS={'type':'integer','minimum':1}; STRINGS={'type':'array','items':S,'uniqueItems':True}
TEXT=dict(obj({'th':{'type':['string','null']},'en':{'type':['string','null']}}),anyOf=[{'properties':{'th':S}},{'properties':{'en':S}}])
def enum(*values): return {'type':'string','enum':list(values)}
def ar(value): return {'type':'array','items':value}
PERIOD=obj({'start':{'type':'string','pattern':r'^([01][0-9]|2[0-3]):[0-5][0-9]$'},'end':{'type':'string','pattern':r'^([01][0-9]|2[0-3]):[0-5][0-9]$'}})
CONDITION=obj({'field':S,'operator':enum('eq','in','gte','lte'),'value':{'type':['string','integer','boolean','array']}})
INPUT=obj({'buttons':STRINGS,'gesture':enum('press','hold','release','double_press','simultaneous','sequence','move'),'action':TEXT,'context':TEXT})
# Every entry describes one semantic field, not one wording of a question.
# tuple: key, value schema, owner label/meaning, publish-core, reference target.
REG={
'center':('ข้อมูลศูนย์',[
 ('name',TEXT,'ชื่อศูนย์อย่างเป็นทางการ',1,None),('operator',TEXT,'หน่วยงานเจ้าของ/ผู้ดำเนินการ',1,None),('description',TEXT,'ศูนย์ทำอะไร/ขอบเขตบริการ',0,None),('address',TEXT,'ที่อยู่เต็ม',0,None),('building',S,'อาคาร',0,None),('floor',S,'ชั้น',0,None),('map_url',S,'ลิงก์แผนที่',0,None),('timezone',enum('Asia/Bangkok'),'เขตเวลา',1,None)]),
'contact':('ติดต่อ',[
 ('channel',enum('facebook','email','phone','website','onsite'),'ประเภทช่องทาง',1,None),('value',S,'URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย',1,None),('purpose',TEXT,'ติดต่อเรื่องอะไรได้บ้าง',1,None),('office_hours',TEXT,'เวลาตอบของช่องทางนี้',0,None)]),
'facility':('สิ่งอำนวยความสะดวก',[
 ('name',TEXT,'เช่น ที่จอดรถ/ที่นั่งพัก',1,None),('location',TEXT,'อยู่บริเวณไหน',1,None),('usage_conditions',TEXT,'เงื่อนไขใช้บริการ',0,None),('accessibility',TEXT,'การเข้าถึง/รถเข็น หากยังไม่มีข้อมูลให้ unknown',0,None)]),
'zone':('โซนบริการ',[
 ('name',TEXT,'PC/PS5/Switch/Cockpit/VR เป็นชื่อรายการ',1,None),('description',TEXT,'โซนนี้ใช้ทำอะไร',0,None),('location',TEXT,'ตำแหน่งในศูนย์',0,None),('room_seats',N,'จำนวนที่นั่งในพื้นที่ ไม่ใช่จำนวนคนเล่นพร้อมกัน',0,None)]),
'equipment_model':('รุ่นและสเปกอุปกรณ์',[
 ('name',TEXT,'ชื่อรุ่นอุปกรณ์',1,None),('device_type',enum('pc','console','vr','wheel','display','peripheral','furniture'),'ประเภทอุปกรณ์',1,None),('specifications',ar(obj({'key':S,'value':S,'unit':{'type':['string','null']}})),'สเปกทีละค่า พร้อมหน่วย/รุ่น',0,None),('usage',TEXT,'วิธีใช้อุปกรณ์/ข้อควรทราบจากแหล่งข้อมูล',0,None)]),
'resource':('เครื่องหรือทรัพยากรจริง',[
 ('name',TEXT,'ชื่อเครื่อง เช่น PC #01',1,None),('zone_id',S,'โซนที่เครื่องตั้งอยู่',1,'zone'),('equipment_model_ids',STRINGS,'รุ่นอุปกรณ์ที่ประกอบในเครื่องนี้',0,'equipment_model'),('capacity_persons',POS,'จำนวนคนเล่นพร้อมกันของเครื่อง ไม่ใช่ห้อง',0,None),('physical_pool_key',S,'รหัสทรัพยากรร่วม เช่น VR 30/60 นาทีใช้เครื่องเดียวกัน',1,None),('operational_status',enum('in_service','out_of_service','retired'),'พร้อมให้บริการทางกายภาพ ไม่ใช่สถานะจอง',1,None)]),
'service':('รายการที่เลือกในระบบจอง',[
 ('name',TEXT,'ชื่อบริการตามหน้า WordPress',1,None),('resource_ids',STRINGS,'เครื่องจริงที่บริการใช้',1,'resource'),('platform',S,'แพลตฟอร์มของบริการ',1,None),('session_minutes',POS,'ระยะเวลาเล่นของบริการ',1,None),('occupancy_minutes',POS,'เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60',1,None),('capacity_min',POS,'ผู้เล่นขั้นต่ำ',0,None),('capacity_max',POS,'ผู้เล่นสูงสุดตามบริการ',0,None),('booking_product_key',S,'รหัสผลิตภัณฑ์/API จาก WordPress ไม่ใช่เดาจากชื่อ',0,None)]),
'game':('ข้อมูลเกม',[
 ('title',TEXT,'ชื่อเกมอย่างเป็นทางการ',1,None),('edition',S,'ภาค/edition ให้ตรง หากต้นทางไม่มีให้ unknown',0,None),('genre',TEXT,'แนวเกม',0,None),('summary',TEXT,'เกมเกี่ยวกับอะไร',0,None),('how_to_play',TEXT,'เป้าหมาย/วงจรการเล่นโดยสรุป',0,None),('publisher_url',S,'แหล่งจากผู้พัฒนาเกม',0,None),('supported_platforms',STRINGS,'แพลตฟอร์มที่ตัวเกมรองรับ ไม่แปลว่าศูนย์มีให้เล่น',0,None),('age_rating',TEXT,'เรตเกมจากต้นทาง ไม่ใช่นโยบายรับเด็กของศูนย์',0,None)]),
'game_service':('เกมที่ศูนย์มีให้เล่นจริง',[
 ('game_id',S,'เลือกเกมจากทะเบียนเกม',1,'game'),('service_id',S,'เลือกบริการจากทะเบียนการจอง',1,'service'),('offered',B,'ศูนย์ยืนยันมี/ไม่มีเกมนี้ในบริการนี้',1,None),('installed_resource_ids',STRINGS,'ถ้ายืนยันเฉพาะเครื่อง ให้ระบุเครื่อง ห้ามอนุมานทั้งโซน',0,'resource'),('game_version',S,'เวอร์ชันเกมที่ติดตั้ง ถ้าไม่ทราบให้ unknown',0,None),('account_policy_id',S,'นโยบายบัญชีของศูนย์',0,'policy')]),
'game_mode':('รูปแบบเล่นและเล่นกับเพื่อน',[
 ('game_id',S,'เกมที่อ้างถึง',1,'game'),('mode_name',TEXT,'เช่น local co-op/online multiplayer',1,None),('platform',S,'แพลตฟอร์มของโหมดนี้',1,None),('players_min',POS,'จำนวนผู้เล่นขั้นต่ำของโหมด',0,None),('players_max',POS,'สูงสุดของโหมดเกม ไม่ใช่ความจุบริการ',0,None),('network_requirement',TEXT,'ออนไลน์/อินเทอร์เน็ต/บัญชีที่ต้องใช้',0,None),('studio_supported',B,'ศูนย์รองรับโหมดนี้จริงหรือยังไม่ยืนยัน',0,None)]),
'control_set':('วิธีเล่นและปุ่ม',[
 ('game_id',S,'เกม/edition ที่ตรงกัน',1,'game'),('platform',S,'PC/PS5/Nintendo Switch/VR',1,None),('input_device',enum('keyboard_mouse','gamepad','racing_wheel','vr_motion'),'ชนิดอุปกรณ์ควบคุม',1,None),('preset',S,'default/custom profile ชื่อชุดปุ่ม',1,None),('game_version',S,'เวอร์ชันที่ตรวจชุดปุ่มนี้',0,None),('bindings',ar(INPUT),'ปุ่ม + กด/ค้าง/กดพร้อมกัน/ลำดับ + action + context; ทุกรายการต้องมีหลักฐานชุดเดียวกัน มิฉะนั้นแยก record',1,None),('limitations',TEXT,'ข้อจำกัดหรือปุ่มที่ยังไม่ยืนยัน',0,None)]),
'audience':('กลุ่มผู้ใช้',[
 ('name',TEXT,'ชื่อกลุ่ม เช่น บุคคลทั่วไป/หน่วยงานภายนอก',1,None),('eligibility',TEXT,'ใครอยู่ในกลุ่มนี้ ตามนโยบายจริง',1,None),('required_proofs',STRINGS,'หลักฐานสิทธิ์ หากไม่มีข้อมูลให้ unknown',0,None)]),
'rate':('ราคาต่อบริการ',[
 ('service_id',S,'บริการตามระบบจอง',1,'service'),('audience_id',S,'กลุ่มผู้ใช้',1,'audience'),('amount_minor',N,'จำนวนสตางค์: 70 บาท = 7000; 0 คือฟรีเมื่อยืนยันจริง',1,None),('currency',enum('THB'),'สกุลเงิน',1,None),('unit',enum('per_session','per_hour','per_person','per_group'),'คิดต่ออะไร',1,None),('duration_minutes',POS,'ช่วงเวลาที่ราคานี้ครอบคลุม',1,None),('persons_min',POS,'ช่วงผู้ใช้ขั้นต่ำ',0,None),('persons_max',POS,'ช่วงผู้ใช้สูงสุด',0,None),('calculation_rule',enum('fixed','linear','no_extrapolation'),'อนุญาตคูณเวลาได้หรือคิดตายตัว ต้องมีหลักฐาน',1,None),('tax_note',TEXT,'ภาษี/เงื่อนไข ถ้ายังไม่ระบุห้ามคิดรวมเอง',0,None)]),
'rental_package':('ราคาเหมาโซน/ห้อง',[
 ('name',TEXT,'ชื่อแพ็กเกจ',1,None),('zone_ids',STRINGS,'โซนที่รวมในแพ็กเกจ',1,'zone'),('audience_id',S,'หน่วยงานภายใน/ภายนอก ไม่ใช่กลุ่มราคาบุคคล',1,'audience'),('period_label',enum('half_day','full_day','custom'),'ครึ่งวัน/เต็มวันเป็นชื่อแพ็กเกจ',1,None),('duration_minutes',POS,'จำนวนจริงของนาที ต้องรอยืนยัน ไม่เดาว่า 4/8 ชั่วโมง',0,None),('amount_minor',N,'ราคาเป็นสตางค์',1,None),('currency',enum('THB'),'สกุลเงิน',1,None),('equipment_included',TEXT,'จำนวนเครื่อง/อุปกรณ์ที่รวม',0,None),('room_seats',N,'จำนวนที่นั่งพื้นที่ตามชีต ไม่ใช่ผู้เล่นเครื่อง',0,None),('terms',TEXT,'เช่น ค่าเจ้าหน้าที่นอกเวลา',0,None)]),
'schedule':('ตารางบริการ',[
 ('timezone',enum('Asia/Bangkok'),'เขตเวลา',1,None),('zone_ids',STRINGS,'ขอบเขตโซน; [] ที่ known หมายถึงทุกโซนตามประกาศ',1,'zone'),('weekday',{'type':'integer','minimum':0,'maximum':6},'ISO weekday ในสเปกนี้ 0=จันทร์ ต้องแปลงจากต้นทางชัดเจน',1,None),('open_periods',ar(PERIOD),'ช่วงเปิดพื้นที่',1,None),('bookable_periods',ar(PERIOD),'ช่วงที่จอง/เล่นได้ แยกจากเปิดพื้นที่',1,None),('maintenance_periods',ar(PERIOD),'ช่วง maintenance',0,None),('reason',TEXT,'เหตุผล/ประกาศของตาราง',0,None)]),
'closure':('วันปิด/ข้อยกเว้น',[
 ('local_date',{'type':'string','format':'date'},'วันที่ ISO ค.ศ. ตามเวลาไทย',1,None),('zone_ids',STRINGS,'โซนที่ได้รับผล; [] = ทุกโซนเมื่อยืนยัน',1,'zone'),('state',enum('closed','modified_hours','open_override'),'ประเภทข้อยกเว้น',1,None),('open_periods',ar(PERIOD),'เวลาใหม่ กรณี modified/open override',0,None),('bookable_periods',ar(PERIOD),'เวลาที่จองได้ในวันที่ยกเว้น',0,None),('reason',TEXT,'เหตุผลปิด/เปิดพิเศษ',1,None),('resolution_policy_id',S,'นโยบายจัดการรายการจองเดิม หากไม่มีให้ unknown',0,'policy')]),
'policy':('นโยบายและกฎศูนย์',[
 ('topic',S,'หัวข้อเชิงความหมาย เช่น personal_peripherals',1,None),('subject',TEXT,'สิ่งที่กฎใช้กับ เช่น คีย์บอร์ด/เมาส์ส่วนตัว',1,None),('decision',enum('allowed','prohibited','required','conditional'),'อนุญาต/ห้าม/จำเป็น/มีเงื่อนไข',1,None),('conditions_all',ar(CONDITION),'เงื่อนไขที่ต้องครบ เช่น booking_paid=true; ไม่มีเงื่อนไขต้องยืนยันจริง',1,None),('exceptions',TEXT,'ข้อยกเว้น หากต้นทางไม่ได้ระบุให้ unknown',0,None),('consequence',TEXT,'ผลเมื่อผิดกฎ/ค่าปรับ ห้ามเติมเอง',0,None),('details',TEXT,'ข้อความกฎพร้อมเงื่อนไขจากต้นทาง',1,None),('procedure_id',S,'ขั้นตอนปฏิบัติที่เกี่ยวข้อง',0,'procedure')]),
'procedure':('ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา',[
 ('topic',S,'เรื่องที่ขั้นตอนนี้ใช้กับ',1,None),('preconditions',ar(CONDITION),'สถานการณ์ก่อนทำ เช่น จองผิดเครื่อง',1,None),('steps',ar(obj({'order':POS,'instruction':TEXT,'contact_id':{'type':['string','null']}})),'ลำดับจริง; contact_id ตรวจ FK ด้วย semantic validator ใน production',1,None),('required_documents',STRINGS,'หลักฐาน/รายการที่ต้องเตรียม',0,None),('deadline_minutes',N,'กำหนดเวลา ถ้าไม่ทราบอย่าเติม',0,None),('outcome',TEXT,'หลังทำแล้วได้อะไร ขอบเขตสิ่งที่ยืนยัน',0,None)]),
'competition':('รายการแข่งขันและฉบับกติกา',[
 ('game_id',S,'เกมที่แข่งขัน',1,'game'),('event_name',TEXT,'ชื่อรายการ+ปี+ประเภทให้ตรง',1,None),('division',TEXT,'เช่น ทีมชาย/ทีมผสม ถ้าไม่ระบุให้ unknown',0,None),('rulebook_release',S,'ฉบับและเวอร์ชันกติกา',1,None),('competition_dates',STRINGS,'วันที่การแข่งขันจากต้นทาง',0,None),('coverage',enum('complete','partial','conflicted'),'ความครบของเอกสาร ตรวจจากสารบัญและต้นทาง ไม่ใช่มี JSON แล้วครบ',1,None),('supersedes_id',S,'ฉบับก่อนหน้าถ้าทราบ',0,'competition')]),
'competition_rule':('ข้อกติกาการแข่งขัน',[
 ('competition_id',S,'ฉบับรายการที่กฎเป็นของมัน',1,'competition'),('section_number',S,'เลขข้อเดิม เช่น 6.1.5',1,None),('facet',enum('identity','eligibility_registration','roster_composition','competition_format','match_configuration','pre_match_on_site','in_match_operations','fair_play_conduct','penalty_matrix','protest_dispute','references_change_history','game_specific'),'หมวดกฎ',1,None),('heading',TEXT,'หัวข้อข้อกติกา',1,None),('text',TEXT,'ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ',1,None),('depends_on_ids',STRINGS,'ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม',0,'competition_rule'),('completeness',enum('complete','truncated','conflicted'),'สถานะความสมบูรณ์ของข้อนี้',1,None)]),
'news':('ข่าว/กิจกรรม/ประกาศ/โปรโมชัน',[
 ('title',TEXT,'หัวข้อประกาศ',1,None),('body',TEXT,'รายละเอียด',1,None),('event_start',{'type':'string','format':'date-time'},'เวลาเริ่มกิจกรรม',0,None),('event_end',{'type':'string','format':'date-time'},'เวลาจบกิจกรรม',0,None),('audience_ids',STRINGS,'ผู้เข้าร่วม/กลุ่มสิทธิ์',0,'audience'),('contact_id',S,'ช่องทางเกี่ยวกับกิจกรรม',0,'contact'),('registration_url',S,'ลิงก์สมัคร ถ้ามี',0,None)]),
'person':('บุคลากร/ทีมที่เปิดเผยได้',[
 ('display_name',TEXT,'ชื่อที่อนุญาตให้เผยแพร่',1,None),('role',TEXT,'ตำแหน่ง/หน้าที่',1,None),('team',TEXT,'ทีม/หน่วยงาน',0,None),('public_contact_id',S,'ช่องทางงานที่อนุญาตเผยแพร่',0,'contact'),('public_scope',TEXT,'รายละเอียดที่เผยแพร่ได้ ไม่ใส่ข้อมูลลูกค้าหรือสลิป',1,None)]),
'faq':('คำถามเสริมและเอกสารทั่วไปของศูนย์',[
 ('question',TEXT,'คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase',1,None),('answer',TEXT,'คำตอบพร้อมหลักฐานของศูนย์',1,None),('related_ids',STRINGS,'รายการที่เกี่ยวข้อง หากใช้ต้อง resolve ข้าม kind',0,'*'),('topic',S,'หัวข้อเชิงความหมาย',1,None),('scope_note',TEXT,'ขอบเขตและข้อจำกัด ไม่ใช้ FAQ override ราคาหรือสถานะสด',0,None)]),
'live_binding':('การเชื่อมสถานะสด',[
 ('service_id',S,'บริการของศูนย์',1,'service'),('provider',enum('wordpress_booking'),'ผู้ให้ข้อมูลสด',1,None),('external_resource_key',S,'รหัสที่ API ใช้จริง',1,None),('physical_pool_key',S,'ทรัพยากรร่วม ต้องตรง resource ที่ service ใช้',1,None),('status_mapping',ar(obj({'raw':S,'normalized':enum('free','occupied','unavailable','unknown')})),'ความหมายสถานะจาก API ต้องมี fixture ที่รู้ผล',1,None),('timezone',enum('Asia/Bangkok'),'เขตเวลาของการแปลงข้อมูล',1,None),('freshness_policy',TEXT,'นโยบาย cache/TTL ที่อนุมัติ',1,None)])}

def field_schema(value_schema,description):
    refs=ar(obj({'source_id':S,'locator':S}))
    return {'description':description,'oneOf':[
      obj({'status':{'const':'known'},'value':value_schema,'evidence_refs':dict(refs,minItems=1),'note':{'type':'string'}}),
      obj({'status':enum('unknown','not_applicable'),'value':{'type':'null'},'evidence_refs':dict(refs,maxItems=0),'note':S}),
      obj({'status':{'const':'conflicted'},'value':{'type':'null'},'evidence_refs':dict(refs,minItems=2),'note':S})]}

def unknown(): return {'status':'unknown','value':None,'evidence_refs':[],'note':'ยังไม่มีข้อมูลยืนยันสำหรับช่องนี้'}
def known(value,sid,loc): return {'status':'known','value':value,'evidence_refs':[{'source_id':sid,'locator':loc}],'note':''}

DATE={'type':['string','null'],'format':'date-time'}
COMMON={
 'schema_version':{'const':VERSION},'record_id':{'type':'string','pattern':r'^[a-z][a-z0-9_:-]{2,99}$'},
 'kind':S,'branch_id':{'const':'psu_phuket'},'revision':POS,
 'lifecycle':enum('draft','in_review','approved','published','withdrawn','archived'),
 'validity':obj({'state':enum('known','unknown'),'effective_from':DATE,'effective_until':DATE}),
 'localization':obj({'source_language':enum('th','en','mixed'),'en_status':enum('missing','draft','agent_translated','reviewed','stale'),'source_revision_hash':{'type':['string','null']}}),
 'aliases':obj({'th':STRINGS,'en':STRINGS}),
 'review':obj({'actor_id':{'type':['string','null']},'reviewed_at':DATE,'revision_sha256':{'type':['string','null']}})
}
catalog=[]
for kind,(label,fields) in REG.items():
    properties=dict(COMMON); properties['kind']={'const':kind}
    properties['fields']=obj({key:field_schema(s,label2) for key,s,label2,core,ref in fields})
    schema=dict(obj(properties),**{'$schema':'https://json-schema.org/draft/2020-12/schema','title':label+' — research design','description':'Research prototype; not loadable by current application.'})
    dump(f'schemas/{kind}.schema.json',schema)
    template={'schema_version':VERSION,'record_id':'draft_'+kind+'_001','kind':kind,'branch_id':'psu_phuket','revision':1,'lifecycle':'draft','validity':{'state':'unknown','effective_from':None,'effective_until':None},'localization':{'source_language':'th','en_status':'missing','source_revision_hash':None},'aliases':{'th':[],'en':[]},'review':{'actor_id':None,'reviewed_at':None,'revision_sha256':None},'fields':{key:unknown() for key,*_ in fields}}
    dump(f'templates/{kind}.draft.json',template)
    catalog.append({'kind':kind,'owner_form':label,'fields':[{'key':key,'meaning_th':desc,'publish_core':bool(core),'reference_kind':ref,'value_schema':s} for key,s,desc,core,ref in fields]})
dump('FIELD_CATALOG.json',catalog)
source_schema=obj({'source_id':S,'kind':enum('owner_chat','owner_document','official_page','publisher_document','derived_curated','secondary','fixture'),'path':S,'sha256':{'type':'string','pattern':'^[0-9a-f]{64}$'},'authority_for':STRINGS,'observed_at':{'type':'string','format':'date-time'},'trust':enum('owner_confirmed','official','internal_verified','legacy_unreviewed','secondary_unverified','synthetic'),'public_url':{'type':['string','null']}})
dump('schemas/source.schema.json',dict(source_schema,**{'$schema':'https://json-schema.org/draft/2020-12/schema'}))

# Draft imports of actual supplied facts. The values retain source meaning;
# no owner approval, current validity, or runtime publication is fabricated.
sources=[]
def src(sid,relative,authority,trust='owner_confirmed'):
 p=ROOT/relative
 sources.append({'source_id':sid,'kind':'owner_document' if trust=='owner_confirmed' else 'derived_curated','path':relative,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'authority_for':authority,'observed_at':datetime.now(timezone.utc).isoformat(),'trust':trust,'public_url':None})
src('owner_answers','data/curated/user_service_facts_20261008.json',['center','contact','policy','procedure'])
src('game_profile_source','data/curated/game_item_details.jsonl',['game'],'legacy_unreviewed')
src('rental_workbook','data/curated/zone_rental_fees_20261006.json',['rental_package','audience','zone'])
def record(kind,rid):
 t=json.loads((OUT/f'templates/{kind}.draft.json').read_text(encoding='utf-8'));t['record_id']=rid;return t
records=[]
c=record('center','center_psu_phuket');f=c['fields'];
for key,value,loc in [('name',{'th':'PSU Esports Studio - Phuket','en':'PSU Esports Studio - Phuket'},'/claims/university'),('operator',{'th':'มหาวิทยาลัยสงขลานครินทร์','en':'Prince of Songkla University'},'/claims/university'),('building','5','/claims/location'),('floor','1','/claims/location'),('map_url','https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5','/claims/map')]:f[key]=known(value,'owner_answers',loc)
records.append(c)
g=record('game','game_valorant');row=json.loads((ROOT/'data/curated/game_item_details.jsonl').read_text(encoding='utf-8').splitlines()[0]);
for key,value in [('title',{'th':row['game'],'en':row['game']}),('genre',{'th':row['genre'],'en':None}),('summary',{'th':row['summary_th'],'en':None}),('how_to_play',{'th':row['how_to_play_th'],'en':None})]:g['fields'][key]=known(value,'game_profile_source','id=game_detail_valorant/'+key)
records.append(g)
pol=record('policy','policy_personal_keyboard_mouse');
for key,value in [('topic','personal_keyboard_mouse'),('subject',{'th':'คีย์บอร์ดหรือเมาส์ส่วนตัว','en':'Personal keyboard or mouse'}),('decision','prohibited'),('details',{'th':'ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้','en':None})]:pol['fields'][key]=known(value,'owner_answers','/claims/personal_keyboard_mouse')
# Do not claim the unanswered controller case, exceptions, or universal applicability.
records.append(pol)
a=record('audience','audience_external_org');a['fields']['name']=known({'th':'หน่วยงานภายนอก','en':'External organizations'},'rental_workbook','/customer_groups/external');records.append(a)
z=record('zone','zone_pc');z['fields']['name']=known({'th':'PC Zone','en':'PC Zone'},'rental_workbook','/rows/5/label');records.append(z)
rent=record('rental_package','rental_pc_external_full_day');
for key,value,loc in [('name',{'th':'เหมา PC Zone เต็มวัน หน่วยงานภายนอก','en':None},'/rows/5/label + /rows/5/prices_thb/external/full_day'),('zone_ids',['zone_pc'],'/rows/5/id'),('audience_id','audience_external_org','/customer_groups/external'),('period_label','full_day','/rows/5/prices_thb/external/full_day'),('amount_minor',400000,'/rows/5/prices_thb/external/full_day (THB x 100)'),('currency','THB','/currency'),('room_seats',43,'/rows/5/seats'),('equipment_included',{'th':'PC 10 เครื่อง','en':None},'/rows/5/equipment_th')]:rent['fields'][key]=known(value,'rental_workbook',loc)
records.append(rent)
dump('examples/actual_source_drafts.bundle.json',{'schema_version':VERSION,'sources':sources,'records':records,'note':'Draft mapping examples only. No policy/date/English review was invented.'})
form=['# คู่มือช่องกรอกข้อมูลทุกหมวด','', 'สถานะ: แบบออกแบบ 3.0 ยังไม่เชื่อมเว็บใช้งานจริง; templates เป็น draft ที่กรอกไม่ครบได้ แต่ยัง Publish ไม่ได้', '', 'เจ้าของกรอกชื่อ/ค่าจริงและแหล่งข้อมูลผ่านฟอร์ม ชื่อ key และ record_id ให้ระบบสร้าง/เลือก ไม่จำเป็นต้องพิมพ์ JSON เอง', '', 'ช่องที่ยังไม่ทราบเลือก unknown; ห้ามกรอก 0/false/ไม่มีแทน unknown. ช่องอ้างอิงใช้ dropdown จากทะเบียนเดียวกัน', '', 'publish_core = จำเป็นก่อนเผยแพร่ความสามารถหลักของ record; ช่องอื่นยังตอบเป็น partial ได้ แต่ไม่ถือว่าข้อมูลครบทุก facet', '']
for cat in catalog:
 form+=['## '+cat['owner_form']+' (`'+cat['kind']+'`)','', '| ช่อง | ความหมายที่เจ้าของกรอก | ต้องทราบก่อนเผยแพร่แกนหลัก | เชื่อมกับ |','|---|---|---|---|']
 for f in cat['fields']:form.append(f"| `{f['key']}` | {f['meaning_th']} | {'ใช่' if f['publish_core'] else 'ตามข้อมูลที่มี'} | {f['reference_kind'] or '—'} |")
 form+=['', f"ไฟล์ตั้งต้น: `templates/{cat['kind']}.draft.json`; ข้อกำหนดชนิดข้อมูล: `schemas/{cat['kind']}.schema.json`",'']
(OUT/'OWNER_FIELD_GUIDE_TH.md').write_text('\n'.join(form)+'\n',encoding='utf-8')
print(json.dumps({'record_types':len(REG),'semantic_fields':sum(len(f) for _,f in REG.values()),'templates':len(REG),'draft_examples':len(records)},ensure_ascii=False))
