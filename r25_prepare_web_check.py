from pathlib import Path
old = Path(__file__).with_name('r24_web_check.py').read_text(encoding='utf-8')
new = old.replace('r24_report_path.txt','r25_report_path.txt').replace('2026.10.01-competition-r24','2026.10.01-competition-format-r25').replace("session='r24-web-'", "session='r25-web-'")
new = new.replace("history=[];records=[];session=", """cases.extend([
 ('th-technical-communication','th','VALORANT technical pause สื่อสารได้ไหม','valorant_psu_phuket_2026','focused'),
 ('en-technical-communication','en','Can players communicate during a VALORANT technical pause?','valorant_psu_phuket_2026','focused'),
 ('th-cs2-table','th','ขอตารางบทลงโทษ CS2','cs2_psu_phuket_2026','focused'),
 ('en-cs2-table','en','Show the CS2 penalty table','cs2_psu_phuket_2026','focused'),
 ('th-tekken-settings','th','Tekken 8 การตั้งค่าเกมเป็นยังไง','tekken8_psu_esports','focused'),
 ('en-tekken-settings','en','What are the Tekken 8 in-game settings?','tekken8_psu_esports','focused'),
 ('en-rov-ipad','en','Can I use a tablet or iPad in the RoV tournament?','rov_blueket_2025_men','focused'),
 ('en-cs2-team','en','How many players are in a CS2 team?','cs2_psu_phuket_2026','focused'),
 ('th-technical-duration','th','VALORANT technical pause ได้กี่นาที','valorant_psu_phuket_2026','focused'),
 ('en-technical-duration','en','How long is a VALORANT technical pause?','valorant_psu_phuket_2026','focused'),
])
history=[];records=[];session=""")
new = new.replace("    if elapsed>20:errors.append('too slow')", """    first=answer.splitlines()[0] if answer else ''
    if kind=='focused' and key not in ('th-technical-duration','en-technical-duration') and not first.startswith('Answer:' if locale=='en' else 'คำตอบ:'):errors.append('first line is not a direct answer')
    if key.endswith('technical-communication'):
        required=('ห้าม','สื่อสาร','เว้นแต่ได้รับอนุญาต') if locale=='th' else ('may not communicate','unless permitted')
        if any(term not in first for term in required):errors.append('missing communication prohibition/exception in first line')
        if any(term in answer for term in ('60','Overtime','Tactical','Major Bug','10 นาที','10 minutes')):errors.append('wrong pause subtype details')
        if answer.casefold().count('สื่อสาร' if locale=='th' else 'communicate')!=1:errors.append('duplicate communication rule')
    if key.endswith('technical-duration') and any(term in answer for term in ('60','2 timeouts','10 minutes','10 นาที','Tactical')):errors.append('unsupported technical duration borrowed from another pause type')
    if key.endswith('cs2-table'):
        table=[line for line in answer.splitlines() if line.startswith('|')][2:]
        if len(table)!=9:errors.append('not nine complete table pairs')
        expected='| การหมิ่นศาสนา | แบนถาวร |' if locale=='th' else '| Offensive religious remarks | Permanent ban |'
        if not table or table[-1]!=expected:errors.append('missing/mismatched final penalty')
    if key.endswith('tekken-settings'):
        if '3' not in first or ('60 วินาที' if locale=='th' else '60 seconds') not in answer:errors.append('missing settings values')
    if key=='en-rov-ipad' and ('may not be used' not in first or 'disqualification' not in first):errors.append('not direct iPad prohibition')
    if key=='en-cs2-team' and '5 players' not in first:errors.append('missing first-line team size')
    if elapsed>20:errors.append('too slow')""")
target = Path(__file__).with_name('r25_web_check.py')
with target.open('x',encoding='utf-8') as handle:handle.write(new)
