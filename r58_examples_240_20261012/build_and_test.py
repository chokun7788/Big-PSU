"""DEMO ONLY. Never opens a production database for writing.
Run with the existing r58 bundled Python; all generated files stay beside this script.
"""
import os,sys,json,copy,hashlib,time,collections,statistics,traceback,csv,sqlite3
from pathlib import Path
from datetime import datetime
BASE=Path(__file__).resolve().parent
SYSTEM=BASE.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
sys.path.insert(0,str(SYSTEM))
os.chdir(SYSTEM)
from app.knowledge.common.registry import CATALOG,template,content_hash,value,source_errors
from app.knowledge.common.store import CommonStore
from app.knowledge.common.answer import CommonAnswerer,title
from app.knowledge.records import canonical_json

WARNING='ข้อมูลตัวอย่างแยก ไม่ใช่ข้อมูลบริการ ราคา หรือนโยบายจริงของ PSU / DEMO ONLY — NOT PSU PRODUCTION DATA'
ACTOR='demo-automatic-validator'
AT=datetime.fromisoformat('2026-10-12T15:00:00+07:00')
DB=BASE/'DEMO_ONLY.sqlite'
ORDER=['center','zone','equipment_model','resource','service','game','audience','contact','procedure','policy','facility','game_service','game_mode','control_set','rate','rental_package','schedule','closure','competition','competition_rule','news','person','faq','live_binding']
def L(th,en):return {'th':th,'en':en}
def rid(kind,i):return f'demo_{kind}_{i:02}'
def url(path):return 'https://example.invalid/'+path
def nm(th,en,i):return L(f'ตัวอย่าง {th} {i:02}',f'Demo {en} {i:02}')
def setv(r,key,val):r['fields'][key].update(status='known',value=val,evidence_refs=[],note=WARNING)

# Concise paraphrases from publisher pages, not copied articles. Everything about the
# fictional venue, installation, rates, tournaments and controls is synthetic.
GAMES=[
('Mario Kart 8 Deluxe','Nintendo Switch','เกมแข่งรถ','Kart racing','แข่งขันขับรถบนสนามและใช้ไอเท็ม','Race on tracks and use items','ขับรถเข้าเส้นชัยและเลือกโหมดแข่งหรือแบตเทิล','Drive to the finish and choose racing or battle modes','https://www.nintendo.com/us/store/products/mario-kart-8-deluxe-switch/'),
('Super Smash Bros. Ultimate','Nintendo Switch','เกมต่อสู้','Fighting','ต่อสู้กับตัวละครจากหลายเกมบนเวที','Fight with characters from multiple games on stages','โจมตีคู่แข่งให้หลุดจากเวที','Knock opponents off the stage','https://www.nintendo.com/us/store/products/super-smash-bros-ultimate-switch/'),
('Animal Crossing: New Horizons','Nintendo Switch','จำลองชีวิต','Life simulation','จัดเกาะและใช้ชีวิตกับชาวเกาะ','Develop an island and interact with its residents','ตกปลา ทำสวน ตกแต่ง และสำรวจเกาะ','Fish, garden, decorate and explore the island','https://www.nintendo.com/us/store/products/animal-crossing-new-horizons-switch/'),
('The Legend of Zelda: Breath of the Wild','Nintendo Switch','ผจญภัย','Adventure','สำรวจดินแดนไฮรูลในบทบาทลิงก์','Explore Hyrule as Link','สำรวจโลก ปีนหอคอย และแก้ปริศนาในศาลเจ้า','Explore, climb towers and solve shrine puzzles','https://www.nintendo.com/us/store/products/the-legend-of-zelda-breath-of-the-wild-switch/'),
('Minecraft','PC','สร้างโลกและเอาชีวิตรอด','Building and survival','สร้างสิ่งต่าง ๆ ด้วยบล็อกและสำรวจโลก','Build with blocks and explore a world','เลือก Creative เพื่อสร้างอย่างอิสระ หรือ Survival เพื่อเก็บทรัพยากรและเอาชีวิตรอด','Choose Creative to build freely or Survival to collect resources and survive','https://www.minecraft.net/en-us/article/what-minecraft'),
('VALORANT','PC','ยิงเชิงกลยุทธ์','Tactical shooter','เกมยิงแบบทีม 5 ต่อ 5 ที่มีตัวละครและความสามารถ','A five-versus-five tactical shooter with characters and abilities','เล่นเป็นทีมและใช้ความสามารถของตัวละครประกอบการยิง','Coordinate with teammates and combine character abilities with shooting','https://playvalorant.com/en-us/'),
('Counter-Strike 2','PC','ยิงแข่งขัน','Competitive shooter','เกมยิงแข่งขันที่พัฒนาบนเอนจิน Source 2','A competitive shooter built on the Source 2 engine','เลือกโหมดและเล่นตามเป้าหมายของแผนที่','Select a mode and play its map objectives','https://store.steampowered.com/app/730/CounterStrike2/'),
('Dota 2','PC','วางแผนแบบทีม','Team strategy','เลือกฮีโร่ที่มีความสามารถและไอเท็มหลากหลาย','Choose heroes with varied abilities and items','เริ่มเรียนรู้ผ่านการเล่นร่วมกันสู้บอตหรือทดลองฮีโร่','Learn through cooperative bot matches or hero demos','https://store.steampowered.com/app/570/Dota_2/'),
('Fortnite Battle Royale','PC','แบตเทิลรอยัล','Battle royale','แข่งขันเอาชีวิตรอดบนเกาะที่มีพายุบีบพื้นที่','Compete for survival on an island with a closing storm','หลบพายุและต่อสู้เพื่อเป็นผู้เล่นคนสุดท้าย','Avoid the storm and fight to be the last player standing','https://www.fortnite.com/@epic/battle-royale?lang=en-US'),
('Rocket League','PC','กีฬาและรถยนต์','Vehicular sports','เล่นฟุตบอลสไตล์อาร์เคดด้วยรถยนต์','Play arcade-style soccer with cars','ขับรถเข้าหาลูกบอลและแข่งขันในสนาม','Drive towards the ball and compete on the field','https://www.rocketleague.com/en')]

THLABEL={k:v['owner_form'] for k,v in CATALOG.items()}
TOPICS=[('เช็กอิน','Check-in'),('บัญชีเกม','Game accounts'),('ต่อเวลา','Time extensions'),('อุปกรณ์ส่วนตัว','Personal equipment'),('ถ่ายภาพ','Photography'),('ติดตั้งโปรแกรม','Software installation'),('เด็กและผู้ปกครอง','Children and guardians'),('อาหารและเครื่องดื่ม','Food and drinks'),('ของหาย','Lost property'),('เลื่อนการจอง','Rescheduling')]
FACILITIES=[('ที่จอดจักรยาน','Bicycle parking'),('ที่นั่งพัก','Rest seats'),('จุดเติมน้ำ','Water station'),('ตู้เก็บของ','Lockers'),('ทางลาด','Access ramp'),('ห้องน้ำ','Restroom'),('พื้นที่ดูการแข่งขัน','Spectator area'),('จุดชาร์จ','Charging station'),('เคาน์เตอร์ช่วยเหลือ','Help desk'),('พื้นที่ซ้อมทีม','Team practice area')]
ALL={};RESEARCH=[]
for i,g in enumerate(GAMES,1):
    RESEARCH.append({'game':g[0],'url':g[-1],'observed_date_bangkok':'2026-10-12','used_fields':['title','genre','summary','how_to_play'],'translated_by':'assistant; not human reviewed','scope':'Publisher descriptions only. No proof PSU offers this game or has these controls.'})

def create(kind,i):
    r=template(kind);r['record_id']=rid(kind,i)
    r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2028-01-01T00:00:00+07:00'}
    r['localization']={'source_language':'mixed','en_status':'agent_translated','source_revision_hash':None}
    aliases=nm(THLABEL[kind],kind.replace('_',' '),i);r['aliases']={'th':[aliases['th']],'en':[aliases['en']]}
    for f in r['fields'].values():f['note']=WARNING
    g=GAMES[i-1];platform=g[1];topic=TOPICS[i-1];cap=4 if platform=='Nintendo Switch' else 1
    data={
      'center':{'name':nm('ศูนย์ Coral Lab','Coral Lab center',i),'operator':L('ผู้ประกอบการสมมุติ Coral Lab','Fictional Coral Lab operator'),'description':L(f'สาขาจำลอง {i:02} สำหรับฝึกกรอกข้อมูล ไม่ใช่ศูนย์จริง',f'Fictional branch {i:02} for form demonstrations, not a real venue'),'address':L(f'อาคารตัวอย่าง {i:02} ถนนสมมุติ จังหวัดสมมุติ',f'Example building {i:02}, fictional road, fictional province'),'building':f'Demo building {i:02}','floor':str(i),'map_url':url(f'map/{i:02}'),'timezone':'Asia/Bangkok'},
      'zone':{'name':nm('โซนฝึก '+g[0],g[0]+' practice zone',i),'description':L(f'โซนสมมุติสำหรับ {g[0]}',f'Fictional zone for {g[0]}'),'location':L(f'ห้องจำลอง C{i:02}',f'Demo room C{i:02}'),'room_seats':cap*2+i},
      'equipment_model':{'name':nm('เครื่องรุ่น LabStation','LabStation model',i),'device_type':'console' if platform=='Nintendo Switch' else 'pc','specifications':[{'key':'demo_memory','value':str(8+i*4),'unit':'GB'},{'key':'demo_storage','value':str(256+i*128),'unit':'GB'}],'usage':L('สเปกสมมุติสำหรับทดสอบ ไม่ใช่สเปกสินค้าจริง','Fictional specifications for testing, not real product specifications')},
      'resource':{'name':nm('เครื่อง Coral Station','Coral Station',i),'zone_id':rid('zone',i),'equipment_model_ids':[rid('equipment_model',i)],'capacity_persons':cap,'physical_pool_key':f'demo_pool_{i:02}','operational_status':'out_of_service' if i==10 else 'in_service'},
      'service':{'name':nm('บริการฝึก '+g[0],g[0]+' practice service',i),'resource_ids':[rid('resource',i)],'platform':platform,'session_minutes':30 if i==5 else 60,'occupancy_minutes':60,'capacity_min':1,'capacity_max':cap,'booking_product_key':f'demo_product_{i:02}'},
      'game':{'title':L('ตัวอย่าง '+g[0],'Demo '+g[0]),'edition':f'DEMO data edition {i:02}; not a verified game build','genre':L(g[2],g[3]),'summary':L(g[4]+' (ข้อมูลเกมสำหรับตัวอย่าง ไม่ยืนยันว่าศูนย์มีให้เล่น)',g[5]+' (example game description, not proof of availability at PSU)'),'how_to_play':L(g[6],g[7]),'publisher_url':g[-1],'supported_platforms':[platform]},
      'audience':{'name':nm('กลุ่มผู้ใช้ '+topic[0],topic[1]+' audience',i),'eligibility':L(f'กลุ่มผู้ใช้จำลอง {i:02} ตามเงื่อนไขตัวอย่าง',f'Fictional audience {i:02} under sample eligibility'),'required_proofs':[f'DEMO group voucher {i:02}']},
      'contact':{'channel':'email','value':f'demo{i:02}@example.invalid','purpose':L('ช่องทางสมมุติสำหรับ '+topic[0],'Fictional contact for '+topic[1]),'office_hours':L(f'ช่วงช่วยเหลือสมมุติ {8+i%3}:00–18:00',f'Example help hours {8+i%3}:00–18:00')},
      'procedure':{'topic':f'DEMO {topic[1]}','preconditions':[{'field':'demo_environment','operator':'eq','value':True}],'steps':[{'order':1,'instruction':L(f'เลือกหัวข้อ {topic[0]} ในหน้าตัวอย่าง',f'Select {topic[1]} on the demo page'),'contact_id':None},{'order':2,'instruction':L(f'แจ้งรหัสตัวอย่าง C{i:02} กับเจ้าหน้าที่สมมุติ',f'Provide sample code C{i:02} to the fictional operator'),'contact_id':rid('contact',i)}],'required_documents':[f'DEMO voucher C{i:02}'],'deadline_minutes':5+i,'outcome':L('ได้รับผลการดำเนินการสมมุติ '+topic[0],'Receive a fictional outcome for '+topic[1])},
      'policy':{'topic':f'DEMO policy {topic[1]}','subject':nm('นโยบาย '+topic[0],topic[1]+' policy',i),'decision':['allowed','prohibited','required','conditional'][i%4],'conditions_all':[{'field':'demo_environment','operator':'eq','value':True}],'exceptions':L('ข้อยกเว้นสมมุติ: ใช้เฉพาะกิจกรรมทดสอบที่ระบุ','Fictional exception: only the specified test activity'),'consequence':L(f'ผลสมมุติ: ส่งต่อผู้ดูแลตัวอย่าง C{i:02}',f'Fictional consequence: refer to demo operator C{i:02}'),'details':L(f'กฎสมมุติเรื่อง {topic[0]} ไม่ใช่นโยบาย PSU ให้ทำตามขั้นตอนตัวอย่าง C{i:02}',f'Fictional rule for {topic[1]}, not PSU policy; follow sample procedure C{i:02}'),'procedure_id':rid('procedure',i)},
      'facility':{'name':nm(FACILITIES[i-1][0],FACILITIES[i-1][1],i),'location':L(f'พื้นที่จำลอง F{i:02}',f'Fictional area F{i:02}'),'usage_conditions':L('เงื่อนไขสมมุติ: ใช้ระหว่างรอบสาธิตเท่านั้น','Fictional condition: use only during the demo session'),'accessibility':L('รายละเอียดการเข้าถึงสมมุติ ต้องตรวจสถานที่จริงแยก','Fictional accessibility details; real venue assessment is separate')},
      'game_service':{'game_id':rid('game',i),'service_id':rid('service',i),'offered':i!=10,'installed_resource_ids':[rid('resource',i)],'game_version':f'DEMO configured build {i:02}; not current official version','account_policy_id':rid('policy',i)},
      'game_mode':{'game_id':rid('game',i),'mode_name':nm('รอบฝึกสมมุติ '+g[0],g[0]+' fictional practice mode',i),'platform':platform,'players_min':1,'players_max':cap,'network_requirement':L('ค่าตั้งทดสอบ: เครือข่ายจำลอง ไม่ยืนยันโหมดจริง','Test configuration: simulated network, not an actual game mode claim'),'studio_supported':i!=10},
      'control_set':{'game_id':rid('game',i),'platform':platform,'input_device':'gamepad' if platform=='Nintendo Switch' else 'keyboard_mouse','preset':f'DEMO_CUSTOM_{i:02}','game_version':f'DEMO input fixture {i:02}','bindings':[{'buttons':[f'DEMO_KEY_{i:02}'],'gesture':'press','action':L(f'คำสั่งทดสอบ {i:02}',f'Test action {i:02}'),'context':L('ปุ่มสมมุติสำหรับทดสอบ ไม่ใช่ปุ่มมาตรฐานของเกม','Synthetic test input, not the game default control')}],'limitations':L('ชุดปุ่มตัวอย่าง ไม่ใช้เป็นคู่มือเล่นเกมจริง','Example bindings; not an actual game controls guide')},
      'rate':{'service_id':rid('service',i),'audience_id':rid('audience',i),'amount_minor':2500+i*500,'currency':'THB','unit':'per_session','duration_minutes':30 if i==5 else 60,'persons_min':1,'persons_max':cap,'calculation_rule':'no_extrapolation','tax_note':L('ราคาและภาษีสมมุติ ไม่ใช่ราคาศูนย์และห้ามใช้เรียกเก็บเงินจริง','Fictional pricing and tax; not a PSU price or payment instruction')},
      'rental_package':{'name':nm('แพ็กเกจเหมา Coral','Coral rental package',i),'zone_ids':[rid('zone',i)],'audience_id':rid('audience',i),'period_label':'half_day' if i%2 else 'full_day','duration_minutes':180 if i%2 else 360,'amount_minor':100000+i*25000,'currency':'THB','equipment_included':L(f'เครื่องจำลอง Coral Station {i:02}',f'Fictional Coral Station {i:02}'),'room_seats':cap*2+i,'terms':L('เงื่อนไขราคาสมมุติสำหรับสาธิต ไม่ใช่ข้อเสนอขายจริง','Synthetic rental terms for demonstrations, not a real sales offer')},
      'schedule':{'timezone':'Asia/Bangkok','zone_ids':[rid('zone',i)],'weekday':(i-1)%7,'open_periods':[{'start':'09:00','end':'18:00'}],'bookable_periods':[{'start':'09:00','end':'12:00'},{'start':'13:00','end':'18:00'}],'maintenance_periods':[{'start':'12:00','end':'13:00'}],'reason':L(f'ตารางสมมุติของโซน C{i:02} เว้นช่วงบำรุงรักษา','Fictional schedule for zone C%02d with a maintenance break'%i)},
      'closure':{'local_date':f'2026-11-{i:02}','zone_ids':[rid('zone',i)],'state':'closed' if i%2 else 'modified_hours','open_periods':[] if i%2 else [{'start':'13:00','end':'17:00'}],'bookable_periods':[] if i%2 else [{'start':'13:00','end':'17:00'}],'reason':L(f'ประกาศปิดสมมุติ C{i:02} เพื่อทดสอบเท่านั้น',f'Fictional closure C{i:02} for tests only'),'resolution_policy_id':rid('policy',i)},
      'competition':{'game_id':rid('game',i),'event_name':nm('การแข่งขัน Coral '+g[0],'Coral '+g[0]+' tournament',i),'division':L('รุ่นทดสอบสมมุติ ไม่ใช่รายการแข่งขันจริง','Fictional test division, not a real tournament'),'rulebook_release':f'DEMO_RULEBOOK_{i:02}','competition_dates':[f'2026-11-{i+10:02}'],'coverage':'partial'},
      'competition_rule':{'competition_id':rid('competition',i),'section_number':str(i),'facet':['identity','eligibility_registration','roster_composition','competition_format','match_configuration','pre_match_on_site','in_match_operations','fair_play_conduct','penalty_matrix','protest_dispute'][i-1],'heading':nm('ข้อกติกาทดสอบ '+topic[0],topic[1]+' test rule',i),'text':L(f'กติกาสมมุติหัวข้อ {topic[0]}: แจ้งผู้ดูแลตัวอย่างก่อนเริ่มรอบ {i:02}; ไม่ใช่กฎทางการของเกมหรือ PSU',f'Fictional rule for {topic[1]}: notify the demo operator before round {i:02}; not an official game or PSU rule'),'depends_on_ids':[],'completeness':'complete'},
      'news':{'title':nm('ประกาศรอบสาธิต '+topic[0],topic[1]+' demo announcement',i),'body':L(f'ประกาศสมมุติ: เปิดรอบฝึก C{i:02} ไม่มีการรับสมัครหรือชำระเงินจริง',f'Fictional announcement: practice C{i:02}, no actual registration or payment'),'event_start':f'2026-11-{i:02}T09:00:00+07:00','event_end':f'2026-11-{i:02}T11:00:00+07:00','audience_ids':[rid('audience',i)],'contact_id':rid('contact',i),'registration_url':url(f'demo-registration/{i:02}')},
      'person':{'display_name':nm('ผู้ดูแล Coral','Coral operator',i),'role':L('ผู้ดูแลสมมุติเรื่อง '+topic[0],'Fictional operator for '+topic[1]),'team':L(f'ทีมตัวอย่าง T{i:02}',f'Demo team T{i:02}'),'public_contact_id':rid('contact',i),'public_scope':L('ตัวตนสมมุติ ไม่มีข้อมูลส่วนบุคคลของคนจริง','Fictional identity; no real personal data')},
      'faq':{'question':nm('คำถาม '+topic[0],topic[1]+' question',i),'answer':L(f'คำตอบสมมุติ: เรื่อง {topic[0]} ให้ใช้ขั้นตอน C{i:02} และติดต่อช่องทางตัวอย่าง',f'Fictional answer: for {topic[1]}, use procedure C{i:02} and the demo contact'),'related_ids':[rid('procedure',i),rid('policy',i)],'topic':f'DEMO_FAQ_{i:02}','scope_note':L('ใช้ทดสอบเท่านั้น ห้ามอ้างเป็นคำตอบของศูนย์จริง','Testing only; do not present as the actual center answer')},
      'live_binding':{'service_id':rid('service',i),'provider':'wordpress_booking','external_resource_key':f'DEMO_EXTERNAL_{i:02}','physical_pool_key':f'demo_pool_{i:02}','status_mapping':[{'raw':f'DEMO_FREE_{i:02}','normalized':'free'},{'raw':f'DEMO_BOOKED_{i:02}','normalized':'occupied'}],'timezone':'Asia/Bangkok','freshness_policy':L('การจับคู่สถานะสมมุติ ไม่เรียก WordPress และไม่ยืนยันสถานะสด','Synthetic status mapping; no WordPress call or live availability claim')}
    }[kind]
    for key,val in data.items():setv(r,key,val)
    if kind=='competition':r['fields']['supersedes_id'].update(status='not_applicable',value=None,evidence_refs=[],note='ไม่มีรายการก่อนหน้าในชุดตัวอย่าง / No prior event in this demo')
    # Real age ratings have not been researched; keep unknown, do not invent a rating.
    if kind=='game':r['fields']['age_rating']['note']='ยังไม่ได้ค้นเรตอายุ แยกจากกฎผู้ใช้ของร้าน / Age rating not researched'
    return r

def filejson(name,x):
    path=BASE/name
    if path.exists():raise RuntimeError('Preserve existing artifact: '+str(path))
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')

def production_digest():
    # Only the delivered package is readable in the sandbox; the real ROOT check is
    # done separately with explicit system permissions and saved in its own receipt.
    db=BASE.parent/'r58_common_content_20261010/ready_package/PSU_Esports_Chatbot_Local/data/knowledge/approved.sqlite'
    c=sqlite3.connect('file:'+db.as_posix()+'?mode=ro',uri=True)
    try:return hashlib.sha256('\n'.join(c.iterdump()).encode()).hexdigest()
    finally:c.close()

def build():
    if DB.exists():raise RuntimeError('Refuse to overwrite existing demo DB')
    baseline=production_digest();store=CommonStore(DB);store.initialize(allow_demo=True)
    saved=[]
    for kind in ORDER:
        for i in range(1,11):
            r=create(kind,i);ALL[r['record_id']]=copy.deepcopy(r)
            snapshot=canonical_json({'warning':WARNING,'kind':kind,'record_id':r['record_id'],'values':{k:f['value'] for k,f in r['fields'].items() if f['status']=='known'}})
            sid='fixture_source_'+r['record_id']
            source={'source_id':sid,'kind':'fixture','path':str(BASE/'records'/kind/(r['record_id']+'.json')),'sha256':hashlib.sha256(snapshot.encode()).hexdigest(),'authority_for':[kind],'observed_at':'2026-10-12T00:00:00+07:00','trust':'synthetic','public_url':None}
            store.add_source(source,snapshot,actor=ACTOR)
            for k,f in r['fields'].items():
                if f['status']=='known':f['evidence_refs']=[{'source_id':sid,'locator':'/values/'+k}]
            x=store.save(r,actor=ACTOR,expected_version=0,change_note=WARNING)
            store.approve(x['record_id'],x['version'],x['hash'],actor=ACTOR);saved.append(x['record_id'])
            filejson('records/'+kind+'/'+r['record_id']+'.json',store.get(r['record_id'])['record'])
        print('created '+kind+': 10',flush=True)
    release=store.publish(saved,actor=ACTOR,expected_active='',request_key='demo-240-first-release')
    rejected=source_errors(source,snapshot,demo=False)
    if not any('Fixture source' in x for x in rejected):raise AssertionError('Production synthetic source guard missing')
    filejson('RESEARCH_SOURCES.json',RESEARCH)
    filejson('MANIFEST.json',{'warning':WARNING,'records':240,'per_kind':{k:10 for k in ORDER},'field_count_per_10':sum(len(s['fields']) for s in CATALOG.values())*10,'db':str(DB),'active_demo_release':release,'demo_database':True,'sources':'all fixture/synthetic, including curated public game descriptions','translations':'agent_translated; no human sign-off','production_fixture_guard':rejected,'package_db_unchanged_after_import':baseline==production_digest(),'production_package_logical_hash':baseline,'research_date_bangkok':'2026-10-12'})
    return store

# Natural requests authored separately from router terms; misses are reported as
# misses. No planner oracle or extra query aliases are injected to force a pass.
PRIMARY={
 'center':('address','อยู่ตรงไหน','Where is it located?'), 'contact':('value','ติดต่อทางไหน','How can I contact them?'),
 'facility':('location','อยู่ตรงไหนในร้าน','Where in the venue is it?'), 'zone':('room_seats','มีที่นั่งกี่ที่','How many seats are there?'),
 'equipment_model':('specifications','สเปกมีอะไรบ้าง','What are the specifications?'), 'resource':('capacity_persons','เล่นพร้อมกันได้กี่คน','How many people can play at once?'),
 'service':('session_minutes','หนึ่งรอบเล่นได้กี่นาที','How many minutes does a session last?'), 'game':('how_to_play','เล่นยังไง','How do I play it?'),
 'game_service':('offered','มีให้เล่นหรือยัง','Is this game offered?'), 'game_mode':('players_max','เล่นพร้อมกันได้กี่คน','How many people can play together?'),
 'control_set':('bindings','ปุ่มอะไรบ้าง','What are the controls?'), 'audience':('required_proofs','ต้องใช้หลักฐานอะไร','What proof is required?'),
 'rate':('amount_minor','ราคาเท่าไหร่','How much does it cost?'), 'rental_package':('amount_minor','เหมาเท่าไหร่','How much is the rental?'),
 'schedule':('bookable_periods','จองช่วงไหนได้บ้าง','What are the booking hours?'), 'closure':('state','วันนั้นปิดไหม','Is it closed on that date?'),
 'policy':('details','กฎเป็นยังไง','What are the rules?'), 'procedure':('steps','ต้องทำยังไงบ้าง','What steps should I follow?'),
 'competition':('rulebook_release','ใช้กติกาฉบับไหน','Which rulebook release applies?'), 'competition_rule':('text','ข้อนี้กำหนดอะไร','What does this rule require?'),
 'news':('body','ประกาศว่าอะไร','What does the announcement say?'), 'person':('role','รับผิดชอบอะไร','What is their role?'),
 'faq':('answer','คำตอบคืออะไร','What is the answer?'), 'live_binding':('status_mapping','จับคู่สถานะยังไง','How are statuses mapped?')}

def expected_leaves(v,lang,records,key):
    if key.endswith('_id') or key.endswith('_ids'):
        return [title(records[x],lang) for x in (v if isinstance(v,list) else [v]) if x in records]
    if key=='amount_minor':return [f'{v//100:,}.{v%100:02d} THB']
    if type(v) is bool:return [('Yes' if v else 'No') if lang=='en' else ('มี/ใช่' if v else 'ไม่มี/ไม่ใช่')]
    if isinstance(v,dict):
        if set(v)=={'th','en'}:return [v.get(lang)] if v.get(lang) else []
        return [z for nested_key,x in v.items() for z in expected_leaves(x,lang,records,nested_key)]
    if isinstance(v,list):return [z for x in v for z in expected_leaves(x,lang,records,'nested')]
    if v is None:return []
    return [str(v)]

def score(result,case,records):
    if result is None:return False,['no_common_answer']
    art=result.decision_artifact or {};obs=art.get('obligations',[]);why=[]
    if art.get('response_type') not in ('answer','list'):why.append('response_'+str(art.get('response_type')))
    record=records[case['rid']]
    for key in case['expected_fields']:
        f=record['fields'][key]
        matches=[o for o in obs if o.get('record_id')==case['rid'] and o.get('field')==key]
        if not matches:why.append('missing_field:'+key);continue
        if matches[0]['status']!=f['status']:why.append('wrong_status:'+key)
        if f['status']=='known':
            missing=[x for x in expected_leaves(f['value'],case['lang'],records,key) if x and x not in result.answer]
            if missing:why.append('missing_content:'+key+':'+repr(missing[:3]))
            if not any(h.get('source_id') in {e['source_id'] for e in f['evidence_refs']} and h.get('locator')=='/values/'+key for h in result.hits):why.append('missing_evidence:'+key)
        else:
            want=('Not applicable' if f['status']=='not_applicable' else 'Not yet confirmed') if case['lang']=='en' else ('ไม่เกี่ยวข้อง' if f['status']=='not_applicable' else 'ยังไม่มีข้อมูลยืนยัน')
            if want not in result.answer:why.append('missing_unknown_wording:'+key)
    return not why,why

def cases(records):
    out=[]
    def add(r,lang,style,q,keys,history=None):out.append({'id':f'{len(out)+1:05}','rid':r['record_id'],'kind':r['kind'],'lang':lang,'style':style,'question':q,'expected_fields':keys,'history':history or []})
    for r in records.values():
        kind=r['kind'];primary,th,en=PRIMARY[kind]
        for lang in ('th','en'):
            name=r['aliases'][lang][0]
            # Query by the authored display alias. Canonical-key tests isolate the
            # schema contract; natural-language tests isolate actual understanding.
            add(r,lang,'all_fields',name+(' ขอข้อมูลทั้งหมดทุกส่วน' if lang=='th' else ' all details'),list(r['fields']))
            for spec in CATALOG[kind]['fields']:
                label=spec['meaning_th'] if lang=='th' else spec['key'].replace('_',' ')
                add(r,lang,'field_contract',name+' '+label,[spec['key']])
            natural=th if lang=='th' else en
            add(r,lang,'natural',name+' '+natural,[primary])
            add(r,lang,'followup',('แล้ว'+natural if lang=='th' else natural),[primary],[{'role':'user','content':name+(' ขอรายละเอียด' if lang=='th' else ' details')}])
            # One extra character inside the label, not a fabricated router alias.
            pos=max(1,len(name)//2);typo=name[:pos]+name[pos]+name[pos:]
            add(r,lang,'name_typo',typo+' '+natural,[primary])
    return out

def run_tests(store):
    records=store.snapshot()['release']['records'];rows=cases(records);filejson('QUESTIONS_EXPECTED.json',rows)
    answerer=CommonAnswerer(store);path=BASE/'ANSWERS_AND_DECISIONS.jsonl'
    if path.exists():raise RuntimeError('Refuse to overwrite answer log')
    summary=collections.defaultdict(lambda:collections.Counter());fail=[];dur=[]
    with path.open('x',encoding='utf-8') as log:
        for n,c in enumerate(rows,1):
            start=time.perf_counter()
            try:
                result=answerer.answer(c['question'],locale=c['lang'],history=c['history'],at=AT)
                ok,reasons=score(result,c,records)
                row={**c,'passed':ok,'reasons':reasons,'answer':result.answer if result else None,'mode':result.mode if result else None,'decision':result.decision_artifact if result else None,'evidence':result.hits if result else [],'exception':None}
            except Exception as exc:
                ok=False;row={**c,'passed':False,'reasons':['exception'],'answer':None,'exception':traceback.format_exc()}
            elapsed=time.perf_counter()-start;row['elapsed_seconds']=elapsed;dur.append(elapsed);log.write(json.dumps(row,ensure_ascii=False)+'\n')
            for dimension in [('overall','all'),('kind',c['kind']),('language',c['lang']),('style',c['style']),('kind_style',c['kind']+'/'+c['style'])]:summary['/'.join(dimension)]['pass' if ok else 'fail']+=1
            if not ok:fail.append(row)
            if n%100==0:log.flush();print(f'queries {n}/{len(rows)}; failures {len(fail)}',flush=True)
    stats={k:dict(v) for k,v in summary.items()};stats['timing']={'median':statistics.median(dur),'p95':sorted(dur)[int(len(dur)*.95)-1],'max':max(dur),'scope':'local schema engine; no LLM, no WordPress, not whole chat latency'}
    filejson('SUMMARY.json',stats);filejson('FAILURES.json',fail)
    with (BASE/'SUMMARY_BY_CATEGORY.csv').open('x',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f);w.writerow(['category','records','pass','fail'])
        for k in ORDER:w.writerow([k,10,summary['kind/'+k]['pass'],summary['kind/'+k]['fail']])
    print(json.dumps({'queries':len(rows),'overall':stats['overall/all'],'timing':stats['timing']},ensure_ascii=False),flush=True)

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='--test-existing':
        if not DB.exists():raise SystemExit('Demo DB missing')
        store=CommonStore(DB)
        if not store.snapshot()['allow_demo']:raise SystemExit('Refuse non-demo DB')
    else:store=build()
    run_tests(store)
