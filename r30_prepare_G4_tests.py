import json,hashlib
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip())
f=p/'app/pipeline/protected_intents.py';before=f.read_bytes();dest=r/'before_G4c/app/pipeline/protected_intents.py';dest.parent.mkdir(parents=True,exist_ok=True)
with dest.open('xb') as out:out.write(before)
s=before.decode('utf-8');old=r'\b(?:pc|ps5|vr|cockpit|nintendo|equipment|station)\b';new=r'\b(?:pc|ps5|vr|cockpit|nintendo|equipment|station)(?:\s*#?\s*\d+)?\b';assert s.count(old)==1;f.write_text(s.replace(old,new),encoding='utf-8',newline='\n')
t=p/'tests/test_r30_remaining_source_contracts.py';s=t.read_text(encoding='utf-8');old="'Is PC1 free on Friday afternoon?'";assert s.count(old)==1;t.write_text(s.replace(old,old+",'PC1 จองได้ช่วงไหนที่ว่างวันศุกร์ช่วงบ่าย','Which PC1 booking slots are available on Friday afternoon?'"),encoding='utf-8',newline='\n')
cases=[]
def add(loc,q,yes=(),no=(),source='',group='source_G4',mode_prefix=None):
    cases.append(dict(id='G4-'+str(len(cases)+1).zfill(3),locale=loc,question=q,must_contain=list(yes),must_not_contain=list(no),required_source=source,group=group,outcome=None,mode_prefix=mode_prefix))
for loc,questions,yes,no in [
 ('th',['CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม','การแข่งขัน CS2 ใช้เวอร์ชันอะไรบนแพลตฟอร์มไหนและแก้ตัวเกมได้ไหม'],['Steam','ไม่ได้รับอนุญาต'],['ส่งเสียงดัง']),
 ('en',['Which platform does CS2 use, and are unauthorized game client modifications allowed?','CS2 tournament: which platform and can we modify the game client?'],['Steam','Unauthorized modifications'],['noise']),
 ('th',['CS2 ปิดรับสมัครแล้วเพิ่มเพื่อนเข้า roster ได้ปะ','CS2 หลังปิดรับสมัครยังลงทะเบียนผู้เล่นเพิ่มได้ไหม'],['หลังจากปิดรับสมัคร'],['ผู้เล่น 5 คน']),
 ('en',['CS2 registration is closed; can we add a teammate to the roster?','Can we register more CS2 players after registration has closed?'],['not permitted after'],['5 players']),
 ('th',['RoV ใช้สกินพิเศษได้หรือเปล่า','แข่ง RoV เลือกสกินอื่นนอกจาก Default ได้ไหม'],['สกิน Default'],['42 เกม']),
 ('en',['Can we use special skins in RoV?','Are non-Default skins allowed in the RoV tournament?'],['only Default skins'],['Verified game catalog'])]:
    for q in questions:add(loc,q,yes,no,'competition_rules_rov' if 'RoV' in q else 'competition_rules_cs2')
for loc,q,yes in [('th','เทคเคนแต่ละเกมแข่งกี่รอบ',['Tekken 8','จำนวนรอบต่อเกม (Round): 3','ตามเอกสาร']),('en','How many rounds per game in Tekken?',['recorded Tekken 8 rulebook','3 rounds per game']),('th','Tekken 8 เกมละแข่งกี่รอบ',['จำนวนรอบต่อเกม (Round): 3']),('en','How many rounds per game in Tekken 8?',['3 rounds per game'])]:add(loc,q,yes,source='competition_rules_tekken8')
for loc,q in [('en','Tekken 7 tournament rules'),('en','Tekken VII tournament rules'),('en','Tekken v7 tournament rules'),('en','Tekken version VII tournament rules'),('th','เทคเคนภาค 7 กฎแข่ง')]:add(loc,q,no=['จำนวนรอบต่อเกม','3 rounds per game'],group='edition_negative',mode_prefix='pipeline:competition_target_clarification')
for loc,q,yes in [('th','วันศุกร์ช่วงบ่ายจองได้หรือเป็นเวลาปิดดูแลเครื่อง',['Maintenance 13:00-16:00','วันปิดพิเศษ']),('en','Can we book on Friday afternoon, or is it maintenance?',['Friday: open 09:00-12:00; maintenance 13:00-16:00','Special closures'])]:add(loc,q,yes,group='weekly_policy',mode_prefix='pipeline:protected_booking_window')
for loc,q in [('th','PC1 จองได้ช่วงไหนที่ว่างวันศุกร์ช่วงบ่าย'),('en','Which PC1 booking slots are available on Friday afternoon?'),('th','วันนี้บ่าย3 PC1 ว่างไหม'),('en','Is PC1 free today at 15:00?')]:add(loc,q,group='live_required',mode_prefix='pipeline:live_booking_status_unavailable')
with (r/'focused_fixture_G4_source.json').open('x',encoding='utf-8') as out:json.dump({'scope':'source-derived full-pipeline contracts; live-required requests use unavailable fixture, no real occupancy oracle','cases':cases},out,ensure_ascii=False,indent=2)
with (r/'app_freeze_G4c.json').open('x',encoding='utf-8') as out:json.dump({str(f.relative_to(p)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'app').rglob('*.py')},out,indent=2)
for old,new in [('r30_extra_G3.py','r30_extra_G4.py'),('r30_extra_analyze_G3.py','r30_extra_analyze_G4.py'),('r30_build_G3_analysis.py','r30_build_G4_analysis.py')]:
    with Path(new).open('x',encoding='utf-8') as out:out.write(Path(old).read_text(encoding='utf-8').replace('G3','G4'))
s=Path('r30_http_G3.py').read_text(encoding='utf-8').replace('G3','G4')
s=s.replace("tasks=[('focused79'","tasks=[('source_G4',json.loads((r/'focused_fixture_G4_source.json').read_text(encoding='utf-8'))['cases']),('focused79'")
s=s.replace("'competition_G43','mixed_title8'","'competition_G43','mixed_title8','source_G4'")
s=s.replace("if not response['valid']:errors.append('validation_rejected')","if not response['valid']:errors.append('validation_rejected')\n                    if c.get('mode_prefix') and not response['mode'].startswith(c['mode_prefix']):errors.append('mode_contract:'+response['mode'])")
# Mixed title fixture remains G3-named because it is unchanged evidence.
s=s.replace('mixed_title_fixture_G4.json','mixed_title_fixture_G3.json')
with Path('r30_http_G4.py').open('x',encoding='utf-8') as out:out.write(s)
print(json.dumps({'new_focus_cases':len(cases),'resource_id_boundary_fixed':True}))
