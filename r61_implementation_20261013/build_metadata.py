from pathlib import Path
import json,sys,copy
B=Path(__file__).resolve().parent;S=B.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
sys.path.insert(0,str(S));from app.knowledge.common.registry import CATALOG
p=S/'app/knowledge/common/schema_descriptions.json';s=json.loads(p.read_text(encoding='utf-8'))
s['kinds']={kind:{f['key']:{**copy.deepcopy(s['fields'].get(f['key'],{})),'description_th':f['meaning_th']} for f in spec['fields']} for kind,spec in CATALOG.items()}
overrides={('game_service','game_version'):('เวอร์ชันเกมที่ติดตั้งในบริการนี้','Game build installed for this venue service, not the version used to verify a control guide.'),('control_set','game_version'):('เวอร์ชันเกมที่ใช้ตรวจชุดปุ่มนี้','Game build against which this particular control preset was verified, not the installed service build.'),('zone','room_seats'):('จำนวนที่นั่งในพื้นที่','Seating capacity of the room; not the simultaneous players of a game.'),('resource','capacity_persons'):('จำนวนคนใช้เครื่องพร้อมกัน','People who can use this particular resource simultaneously; not total room seating.')}
for (kind,key),(th,en) in overrides.items():s['kinds'][kind][key].update(description_th=th,description_en=en)
s['version']=4;p.write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8')
profiles={'version':1,'purpose':'Presentation semantics only; no owner facts','kinds':{},'labels':{}}
def ctx(kind,when,include):profiles['kinds'].setdefault(kind,{'context':[]})['context'].append({'when':when,'include':include})
ctx('rate',['amount_minor','unit','duration_minutes'],['service_id','audience_id','currency','unit','duration_minutes','calculation_rule','tax_note'])
ctx('rental_package',['amount_minor'],['audience_id','currency','period_label','duration_minutes','terms'])
ctx('rental_package',['equipment_included'],['zone_ids'])
ctx('policy',['decision','exceptions','details'],['decision','conditions_all','exceptions','details'])
ctx('game_mode',['players_min','players_max','network_requirement','studio_supported'],['mode_name','platform'])
ctx('control_set',['bindings','game_version'],['platform','input_device','preset'])
ctx('competition_rule',['text'],['heading','section_number','completeness'])
ctx('schedule',['open_periods','bookable_periods','maintenance_periods'],['timezone','weekday','zone_ids'])
ctx('closure',['state','open_periods','bookable_periods'],['local_date','zone_ids'])
labels={'service':{'session_minutes':('เวลาเล่น (นาที)','Play time (minutes)'),'occupancy_minutes':('เวลาที่ล็อกเครื่อง (นาที)','Reserved time (minutes)')},'rate':{'amount_minor':('ราคา','Price'),'unit':('หน่วยคิดราคา','Billing unit'),'calculation_rule':('วิธีคิดราคา','Calculation rule')},'rental_package':{'amount_minor':('ราคาแพ็กเกจ','Package price'),'equipment_included':('อุปกรณ์ที่รวม','Included equipment'),'room_seats':('ที่นั่งในพื้นที่','Room seats'),'duration_minutes':('ระยะเวลา (นาที)','Duration (minutes)')},'schedule':{'open_periods':('เวลาเปิดพื้นที่','Opening periods'),'bookable_periods':('ช่วงที่จองได้','Bookable periods'),'maintenance_periods':('ช่วงบำรุงรักษา','Maintenance periods'),'zone_ids':('โซนที่ใช้ตารางนี้','Applicable zones')},'closure':{'zone_ids':('โซนที่ได้รับผล','Affected zones'),'state':('สถานะตามประกาศ','Notice status')},'game_service':{'game_version':('เวอร์ชันที่ติดตั้ง','Installed game version')},'control_set':{'game_version':('เวอร์ชันที่ตรวจชุดปุ่ม','Version used to verify controls')},'contact':{'value':('ช่องทางติดต่อ','Contact'),'office_hours':('เวลาที่ช่องทางนี้ตอบ','Contact response hours')}}
for kind,fs in labels.items():profiles['labels'][kind]={key:{'th':th,'en':en} for key,(th,en) in fs.items()}
with (S/'app/knowledge/common/answer_profiles.json').open('x',encoding='utf-8') as f:json.dump(profiles,f,ensure_ascii=False,indent=2)
print('155 kind-qualified slots and presentation profiles created')
