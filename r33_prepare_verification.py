import json
from pathlib import Path
ROOT=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path((ROOT/'r33_report_path.txt').read_text().strip());OLD=Path((ROOT/'r32_report_path.txt').read_text().strip())
cases=[]
def add(id,question,locale,groups,forbidden=(),mode=None):
    cases.append(dict(id=id,question=question,locale=locale,groups=groups,forbidden=forbidden,mode=mode))
add('TH-fee-calc','บุคคลทั่วไปเล่น PS5 3 ชั่วโมงเสีบกี่าท','th',[['450'],['3 session'],['150'],['PlayStation']])
add('TH-price-noise','Mario Party Superstars รคาเท่าๆหร่','th',[['Nintendo Switch'],['บาท'],['ราคา'],['กลุ่ม']])
add('TH-food-boundary','เอาอสหารเข้าไดไหม','th',[['อาหาร'],['เฉพาะพื้นที่'],['กำหนด']])
add('TH-member-role','นายปัณณวิชญ์ หนูเรือง มีตไแหน่งอไร','th',[['นายปัณณวิชญ์ หนูเรือง'],['เลขานุการ'],['PSU Phuket Esports Club']])
add('TH-compound-price-control','Tekken 8 ราคาเท่าไหร่แล้วมีป่มอะไรบ้าง','th',[['คำถามที่ 1'],['คำถามที่ 2'],['บาท'],['ปุ่ม'],['1','2','Square','Triangle']])
add('TH-compound-book-schedule','Cockpit จองนังไงแล้วเปิวันไหนบ้าง','th',[['คำถามที่ 1'],['คำถามที่ 2'],['จอง'],['09:00'],['13:00'],['Maintenance','maintenance']])
add('TH-game-book','ถ้าจะเล่น Resident Evil 4 ต้องจอวอะไร','th',[['PlayStation 5'],['VR'],['แนบสลิป'],['สถานะว่าง']])
add('TH-game-existence','มั Counter-Strike 2 ไหม','th',[['Counter-Strike 2'],['PC']])
add('TH-slip-boundary','ต้องแนบสลิไปหม','th',[['แนบสลิป'],['Student ID'],['อีเมล']])
add('TH-hour-boundary','เปืดกี่โง','th',[['09:00-12:00'],['13:00-16:00'],['maintenance']])
add('TH-genre','PUBG เป็นเกมนแวไหน','th',[['Battle Royale'],['เอาชีวิตรอด']])
add('TH-unsupported-game','Roblox เล่นได้ไม','th',[['ยังไม่พบ Roblox'],['สอบถามเจ้าหน้าที่']],mode='pipeline:games_known_unsupported')
add('TH-loss-vs-damage','ทำอุปกรณ์เสยหาย รับผิดชอบ','th',[['100–500','100-500'],['500–2,000','500-2,000'],['เต็มจำนวน']])
add('TH-peripheral-gap','เอาคีย์บอร์ตดัวเองมาใช้ได้ไหม','th',[['ยังไม่พบ'],['นโยบาย'],['เจ้าหน้าที่']],forbidden=['อนุญาตให้','ใช้ได้ครับ'])
add('TH-delivery-gap','ส่งเครื่องงเกมไปบ้าน','th',[['ยังไม่พบ'],['ส่งเครื่องเกมไปที่บ้าน']],forbidden=['42 เกม'])
add('TH-comparison','PC กับ VR อันไหนพงกว่า','th',[['PC'],['70'],['25'],['VR'],['190'],['525'],['375'],['1,050'],['กลุ่มผู้ใช้']])
add('EN-comparison','Whih is more expensivw, PC or VR','en',[['PC'],['70'],['25'],['VR'],['190'],['525'],['375'],['1,050'],['user group']])
add('EN-group-count','How many categories are memmbers divided into','en',[['3 groups'],['25 member records'],['7 records'],['5 records'],['13 records']])
add('EN-name-gap','What possition does Mr. Imaginary Person hold','en',[['could not verify'],['Imaginary Person'],['exact name']],forbidden=['member directory:\n','University President ('])
add('EN-rule-singular','What are the studio rule','en',[['Food','food'],['designated areas'],['prohibited'],['noise'],['Return equipment']])
add('EN-rule-typos','What are the stduio ryles','en',[['Food','food'],['designated areas'],['prohibited'],['noise']])
add('EN-controls-article','What does teh R2 button do in Gran Turismo 7 on PS5','en',[['R2'],['Accelerate'],['secondary'],['not been checked']])
add('EN-equipment','What is a gamimg moue','en',[['Gaming Mouse'],['PC Zone']])
add('EN-double-modifier','Does the PC Zone have hamin monitors','en',[['Gaming Monitor'],['PC Zone']])
add('EN-unknown-game','Can I use an unknown gamr called Example Quest','en',[['could not find Example Quest'],['will not substitute']],forbidden=['VALORANT controls'])
add('EN-overnight','Do you offer vernight accommodation','en',[['could not find verified'],['overnight'],['should not be assumed']])
add('EN-weekday-plural','Is it opn on Sundays','en',[['Sunday'],['no regular service period']])
add('EN-booking-no-target','Can I biok his','en',[['Which service'],['date and time']],forbidden=['Booking steps:'])
add('EN-ambiguous-pay','Wherw can you pay VALORANT','en',[['Do you mean'],['play VALORANT'],['service fee']],mode='pipeline:game_pay_or_play_clarification')
add('EN-contact','How can I cotnact the studuo','en',[['psuesportspkt@gmail.com'],['+66 7627 6004'],['+66 7627 6045']])
add('EN-book-days','How to book VR and what days are availablee','en',[['Question 1'],['Question 2'],['Upload the payment slip'],['Monday-Friday']])
add('TH-negation-retained','ขอข้อมูลเรื่องคำพูดไม่หมาัสม','th',[['ห้าม'],['ดูหมิ่น'],['เสียดสี']])
with (R/'R33_INDEPENDENT_USAGE_ORACLE.json').open('x',encoding='utf-8') as f:json.dump(dict(cases=cases,evidence='Assistant assertions traced to recorded fee/member/rule/game records; not owner-approved; real occupancy excluded'),f,ensure_ascii=False,indent=2)
for name in ['r32_start_web.ps1','r32_stop_owned_web.ps1','r32_positive_http.py','r32_partial_http.py','r32_year_http.py','r32_queue_diagnostic.js','r32_freeze.py']:
    s=(ROOT/name).read_text(encoding='utf-8').replace('r32_report_path.txt','r33_report_path.txt').replace('2026.10.02-source-content-reliability-r32','2026.10.02-usable-task-frames-r33').replace('r32_ready_','r33_ready_')
    if name.endswith('_http.py'):
        # Read the preserved source fixtures from r32; write only into r33.
        s=s.replace("R/'R32_POSITIVE_SOURCE_ORACLE.json'", "Path((ROOT/'r32_report_path.txt').read_text().strip())/'R32_POSITIVE_SOURCE_ORACLE.json'")
    (ROOT/name.replace('r32_','r33_')).write_text(s,encoding='utf-8')
# Compare to the actual current r32 baseline, not r31.
s=(ROOT/'r32_compare.py').read_text(encoding='utf-8').replace("R=Path((ROOT/'r32_report_path.txt').read_text().strip());OLD=Path((ROOT/'r31_report_path.txt').read_text().strip())","R=Path((ROOT/'r33_report_path.txt').read_text().strip());OLD=Path((ROOT/'r32_report_path.txt').read_text().strip())").replace("OLD/'final_C_all_results.jsonl'","OLD/'final13_all_results.jsonl'")
(ROOT/'r33_compare.py').write_text(s,encoding='utf-8')
# Regression fixtures are immutable copies, for existing HTTP runner.
for name in ['compound_pause_fixture_B.json','focused_fixture.json','focused_fixture_G6_source.json','focused_fixture_v2.json','focused_fixture_G_new_v2.json','mixed_title_fixture_G3.json']:
    with (R/name).open('xb') as out:out.write((OLD/name).read_bytes())
s=(ROOT/'r32_http_final13.py').read_text(encoding='utf-8').replace('r32_report_path.txt','r33_report_path.txt').replace('2026.10.02-source-content-reliability-r32','2026.10.02-usable-task-frames-r33')
(ROOT/'r33_http_regression.py').write_text(s,encoding='utf-8')
print('prepared 32 source-content usage assertions and preserved HTTP regression fixtures')
