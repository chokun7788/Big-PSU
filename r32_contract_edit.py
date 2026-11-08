from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(rel,old,new):
 p=P/rel;s=p.read_text(encoding='utf-8');assert old in s,rel;p.write_text(s.replace(old,new,1),encoding='utf-8')
edit('app/pipeline/competition_request_contract.py',"    if game_id!='cs2':return ()\n    result=[]",'''    result=list(expanded_requirements(query,game_id))
    if game_id!='cs2':return tuple(result)''')
extra=r'''
# Query requirements are evaluated before retrieval; they do not depend on the
# renderer's chosen rows or its first detected facet. Patterns locate source
# clauses, not values supplied by the program.
def expanded_requirements(query,game_id):
    result=[]
    def add(name,pattern):
        if name not in {n for n,_ in result}:result.append((name,pattern))
    if game_id=='cs2':
        info=bool(re.search(r'ข้อมูลของรายการ|ข้อมูลรายการ|event information|event identity',query,re.I))
        if info or re.search(r'ขอบเขต|rulebook scope',query,re.I):add('scope',r'ขอบเขตการบังคับใช้|Scope of Application')
        if info:
            add('version',r'เวอร์ชันของเกม|latest version.*Steam')
            add('language',r'ภาษาทางการ|official language')
            add('event_duration_venue',r'การแข่งขันจะแข่งขันทั้งหมด 1 วัน|(?:competition|tournament).{0,55}(?:1 day|one day)')
            add('discord',r'เซิร์ฟเวอร์ Discord|Discord server')
        if re.search(r'คุณสมบัติ|\beligibility\b',query,re.I):add('eligibility',r'เปิดรับเฉพาะ|General eligibility')
        if re.search(r'รายชื่อผู้เล่น|\broster\b',query,re.I) and not re.search(r'กำหนดส่ง|deadline|substitutes?|สำรอง',query,re.I):add('roster',r'องค์ประกอบทีม.*ผู้เล่น|Team composition.*players')
        if re.search(r'การลงทะเบียน|\bregistration\b',query,re.I) and not re.search(r'กำหนดส่ง|วันที่|deadline|fee|ค่าสมัคร',query,re.I):add('registration',r'ไม่อนุญาตให้ลงทะเบียน|Registration of players is not permitted')
        if re.search(r'การตั้งค่า(?:ใน)?เกม|in.game settings|match settings',query,re.I):
            add('competitive_mode',r'โหมด Competitive|Competitive mode')
            add('round_time',r'เวลาต่อรอบ.*Freeze time|Round time.*Freeze time')
            add('money_bomb',r'เงินเริ่มต้น.*เวลาของระเบิด|Initial money.*Bomb time')
            add('rounds',r'จำนวนรอบสูงสุด|Maximum of \d+ rounds')
            add('overtime',r'การต่อเวลา|Overtime:.*rounds')
        if re.search(r'อุปกรณ์ที่ใช้แข่งขัน|(?:competition equipment|equipment rules|equipment and devices)',query,re.I):
            add('own_equipment',r'นำคีย์บอร์ด.*มาเองได้|Players may bring|Self-provided equipment:')
            add('provided_equipment',r'ผู้จัดจะจัดเตรียม|organizers? (?:will )?(?:prepare|provide)')
            add('equipment_readiness',r'รับผิดชอบต่อคุณภาพ|responsible for.*(?:quality|readiness)')
    if game_id=='rov' and re.search(r'จำนวนผู้เล่น|ผู้เล่นกี่คน|ทีมละกี่คน|team size|how many players|number of players',query,re.I) and not re.search(r'สำรอง|substitutes?|registered roster',query,re.I):
        add('rov_in_match_team_size',r'การแข่งขัน 5v5|5v5.*Tournament Mode|Tournament Mode.*5v5')
    return tuple(result)
'''
p=P/'app/pipeline/competition_request_contract.py';s=p.read_text();p.write_text(s+extra,encoding='utf-8')
edit('app/pipeline/competition_detail.py',"    if not concepts:\n        return None",'''    from app.pipeline.competition_request_contract import request_requirements
    requirements=request_requirements(query,target.targets[0].game_id)
    if not concepts and not requirements:
        return None''')
edit('app/pipeline/competition_detail.py','    selected = list(dict.fromkeys(selected))', '''    # Independent requested propositions supplement the extraction taxonomy.
    # Every requested clause must be supported; missing evidence must never
    # fall back to a different topic from the same game.
    for name, pattern in requirements:
        matches=[]
        for row in rows:
            text=approved_localization(row,'text') if locale=='en' else str(row.get('text') or '')
            clauses=[line for line in source_clause_lines(text or '') if re.search(pattern,line,re.I)]
            if clauses:matches.append((row,clauses))
        if not matches:
            note=("I could not find complete verified source clauses for every requested topic. Please specify the unresolved topic or ask the organizer." if locale=='en' else "ยังไม่พบข้อกฎที่ยืนยันได้ครบทุกประเด็นที่ถามครับ กรุณาระบุประเด็นที่ยังขาดหรือสอบถามผู้จัด")
            return CompetitionDetail(note,(),tuple(n for n,_ in requirements),'no_answer',('requested_source_missing:'+name,))
        row, clauses=max(matches,key=lambda pair:len(pair[1]))
        selected.extend(clauses)
        if row not in used:used.append(row)
    selected = list(dict.fromkeys(selected))''')
edit('app/pipeline/competition_detail.py','            return None\n        # A settings section', '''            note=("I could not find complete verified source clauses for every requested topic." if locale=='en' else "ยังไม่พบข้อกฎที่ยืนยันได้ครบทุกประเด็นที่ถามครับ")
            return CompetitionDetail(note,(),tuple(c.name for c in concepts),'no_answer',('requested_source_missing:'+concept.name,))
        # A settings section''')
edit('app/pipeline/competition_detail.py','    return CompetitionDetail(answer,tuple(used),tuple(c.name for c in concepts))', '''    if any(name=='rov_in_match_team_size' for name,_ in requirements):
        note=("The source specifies 5v5 play (five players per side). This does not verify the registered roster size or substitute allowance." if locale=='en' else "ข้อนี้ระบุการแข่งขันแบบ 5v5 (ฝ่ายละ 5 คนในเกม) ไม่ได้ยืนยันจำนวนรายชื่อที่ลงทะเบียนหรือโควตาตัวสำรองครับ")
        answer+='\\n'+note
    names=tuple(dict.fromkeys([c.name for c in concepts]+[n for n,_ in requirements]))
    return CompetitionDetail(answer,tuple(used),names)''')
print('expanded query content contracts and source extraction')
