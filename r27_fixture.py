"""Independent literal-clause contracts, not runtime-generated expected answers."""
import hashlib, json, re
from pathlib import Path

PROJECT = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
REPORT = Path(Path(__file__).with_name('r27_report_path.txt').read_text(encoding='utf-8').strip())
BOOKS = {'cs2':'cs2_psu_phuket_2026','rov':'rov_blueket_2025_men','tekken8':'tekken8_psu_esports','valorant':'valorant_psu_phuket_2026'}
# game, section, detail, TH question, EN question, TH source regex, EN source regex
SPECS = [
('cs2','04','scope','กติกา CS2 ฉบับนี้ใช้กับใครบ้าง','Who does the CS2 rulebook apply to?','ขอบเขตการบังคับใช้','Scope of Application'),
('cs2','05','version','กติกา CS2 ใช้เวอร์ชันเกมอะไร','Which game version do the CS2 tournament rules use?','เวอร์ชันของเกม','latest version'),
('cs2','06','language','กติกา CS2 ใช้ภาษาอะไรในการประท้วง','Which language must CS2 tournament protests use?','ภาษา ภาษาทางการ','Language:'),
('cs2','09','discord','กติกา CS2 ต้องใช้ Discord ไหน','Which Discord server must CS2 tournament participants use?','เซิร์ฟเวอร์ Discord','Communication:'),
('cs2','11','roster-change','กติกา CS2 เปลี่ยนสมาชิกทีมระหว่างแข่งได้ไหม','Can CS2 tournament teams change members during the event?','เปลี่ยนแปลงสมาชิก','No team member'),
('cs2','12','late-register','กติกา CS2 ลงทะเบียนผู้เล่นหลังปิดรับสมัครได้ไหม','Can CS2 players register after tournament registration closes?','ไม่อนุญาตให้ลงทะเบียน','Registration of players'),
('cs2','13','withdraw','กติกา CS2 ถ้าสมาชิกถอนตัวจะเกิดอะไร','What happens if a CS2 tournament team member withdraws?','ถอนตัว','If any member withdraws'),
('cs2','14','one-team','กติกา CS2 ผู้เล่นลงได้กี่ทีม','How many teams may a CS2 tournament player represent?','ทีมเดียวเท่านั้น','only one team'),
('cs2','17','eligibility','กติกา CS2 คุณสมบัติผู้สมัครคืออะไร','Who is eligible to register for the CS2 tournament?','เปิดรับเฉพาะ','General eligibility'),
('cs2','21','bo3','กติกา CS2 รอบรองและรอบชิงแข่ง BO อะไร','What series format applies to CS2 tournament semifinals and finals?','รอบรองชนะเลิศ','Semifinals and finals'),
('cs2','24','timer','กติกา CS2 เวลาต่อรอบและ Freeze time เท่าไร','What are round time and Freeze time in the CS2 tournament?','เวลาต่อรอบ','Round time'),
('cs2','25','money-bomb','กติกา CS2 เงินเริ่มต้นและเวลาระเบิดเท่าไร','What are starting money and bomb time in the CS2 tournament?','เงินเริ่มต้น','Initial money'),
('cs2','26','rounds','กติกา CS2 จำนวนรอบสูงสุดและชนะที่กี่รอบ','What are the maximum rounds and winning threshold in the CS2 tournament?','จำนวนรอบสูงสุด','Maximum of'),
('cs2','27','overtime','กติกา CS2 ต่อเวลามีกี่รอบและเงินเท่าไร','What are the CS2 tournament overtime rounds and starting money?','การต่อเวลา','Overtime:'),
('cs2','29','maps','กติกา CS2 ใช้แผนที่อะไรบ้าง','Which maps are in the CS2 tournament map pool?','ANCIENT','ANCIENT'),
('cs2','31','mapban','กติกา CS2 เลือกแผนที่ใช้เว็บอะไร','Which website is used for CS2 tournament map selection?','MAPBAN','MAPBAN'),
('cs2','32','side','กติกา CS2 เลือกฝั่งอย่างไร','How are sides selected in the CS2 tournament?','ดวลมีด','knife round'),
('cs2','33','technical','กติกา CS2 technical pause ได้กี่ครั้งกี่นาที','How many technical pauses and minutes per pause are allowed in the CS2 tournament?','ทางเทคนิค','Technical game pauses'),
('cs2','34','tactical','กติกา CS2 เวลานอกได้กี่ครั้งและใช้ช่วงไหน','How many tactical timeouts are allowed and when can they be used in the CS2 tournament?','การขอเวลานอก','Tactical timeouts'),
('cs2','36','conduct','กติกา CS2 มารยาทผู้เล่นห้ามอะไรบ้าง','What player conduct does the CS2 tournament prohibit?','มารยาทผู้เล่น','Player conduct'),
('cs2','41','own-gear','กติกา CS2 นำอุปกรณ์ของตัวเองอะไรมาได้บ้าง','What personal equipment may players bring to the CS2 tournament?','นำคีย์บอร์ด','Players may bring'),
('cs2','43','provided','กติกา CS2 ผู้จัดเตรียมอุปกรณ์อะไรให้','What equipment do CS2 tournament organizers provide?','ผู้จัดจะจัดเตรียม','organizers will prepare'),
('cs2','48','social-exception','กติกา CS2 เข้าโซเชียลบนเครื่องแข่งได้ไหม','Can players access social media on CS2 tournament computers?','ห้ามเข้าโซเชียล','must not access'),
('cs2','51','devices','กติกา CS2 นำโทรศัพท์เข้าเขตแข่งได้ไหม','Can players bring phones into the CS2 tournament area?','ห้ามนำโทรศัพท์','Mobile phones'),
('cs2','52','notes','กติกา CS2 ใครนำโน้ตเข้าแข่งได้และต้องส่งให้ใคร','Who may bring notes into the CS2 tournament area and who receives them?','ผู้เล่นห้ามนำโน้ต','Players are not allowed'),
('cs2','58','protest','กติกา CS2 ใครยื่นประท้วงได้ภายในกี่นาที','Who may file a CS2 tournament protest and within how many minutes?','การประท้วง ต้อง','Protests must'),
('rov','05','format','กติกา RoV รูปแบบการแข่งขันเป็นอย่างไร','What is the RoV tournament format?','แข่งแบบออฟไลน์|แข่ง Best','Offline Mode|Each round played'),
('rov','06:01','heroes','กติกา RoV ต้องมีฮีโร่อย่างน้อยกี่ตัว','How many heroes must a RoV tournament participant own?','4\.2\.1','4\.2\.1'),
('rov','06:01','skin','กติกา RoV ใช้สกินอะไรได้บ้าง','Which skins may be used in the RoV tournament?','4\.2\.5','4\.2\.5'),
('rov','06:01','disconnect-quota','กติกา RoV หลุดเกมหยุดได้กี่ครั้งกี่นาที','How many pauses and minutes are allowed for a disconnect in the RoV tournament?','4\.3\.1','4\.3\.1'),
('rov','06:02','rematch','กติกา RoV ขอเริ่มเกมใหม่ก่อนและหลัง First Blood ได้ไหม','Can RoV tournament players request a restart before or after First Blood?','4\.3\.[34]','4\.3\.[34]'),
('rov','06:02','break','กติกา RoV เวลาพักระหว่างเกมกี่นาที','How long is the break between games in the RoV tournament?','4\.4\.3','4\.4\.3'),
('rov','06:03','long-pause','กติกา RoV หยุดเกิน 10 นาทีกรรมการทำอย่างไร','What may staff do if a RoV tournament pause exceeds 10 minutes?','4\.5\.2','4\.5\.2'),
('rov','06:04','overheat','กติกา RoV เครื่องร้อนหยุดได้กี่นาทีและเงื่อนไขอะไร','How long may staff pause for device overheating in the RoV tournament and under what condition?','4\.6\.1\.1','4\.6\.1\.1'),
('rov','07','ipad','กติกา RoV ใช้ Tablet หรือ iPad ได้ไหม','Can I use a tablet or iPad in the RoV tournament?','5\.3','5\.3'),
('tekken8','02','equipment','กติกา Tekken 8 ใช้เครื่องอะไร','What console is used in the Tekken 8 tournament?','ใช้เครื่องเกม','PlayStation 5 console'),
('tekken8','02','decider','กติกา Tekken 8 เสมอ 1-1 ทำอย่างไร','What happens at a 1-1 tie in the Tekken 8 tournament?','หากเสมอกัน','If tied'),
('tekken8','03','dlc','กติกา Tekken 8 ใช้ตัวละคร DLC ได้ไหม','Are DLC characters allowed in the Tekken 8 tournament?','สามารถเลือก ตัวละคร','Any character'),
('tekken8','03','assist','กติกา Tekken 8 ใช้ปุ่ม Assist ได้ไหม','Are Assist buttons permitted in the Tekken 8 tournament?','อนุญาตให้ใช้ ปุ่ม','Assist buttons'),
('tekken8','04','settings','กติกา Tekken 8 การตั้งค่าเกมเป็นอย่างไร','What are the Tekken 8 tournament in-game settings?','จำนวนรอบต่อเกม|เวลาแข่งขันต่อรอบ|Advantage|Stage','Rounds per game|Time per round|Advantage|Stage'),
('tekken8','05','conduct','กติกา Tekken 8 มารยาทและพฤติกรรมต้องเป็นอย่างไร','What conduct and etiquette do Tekken 8 tournament players follow?','ห้ามแสดงพฤติกรรม|ผู้เข้าแข่งขันต้องให้เกียรติ','Unsportsmanlike|Competitors must respect'),
('tekken8','06','officials','กติกา Tekken 8 กรรมการเปลี่ยนคำตัดสินได้ไหม','Can Tekken 8 tournament referees reconsider their decisions?','กรรมการสามารถพิจารณา','Referees may reconsider'),
('valorant','01','socd','กติกา VALORANT ใช้ Snap Tap หรือ SOCD ได้ไหม','Do VALORANT tournament rules allow Snap Tap or SOCD?','อนุญาตให้ใช้เทคโนโลยี|เทคโนโลยีคีย์บอร์ด.*Snap','Allowed keyboard technology'),
('valorant','02','notes','กติกา VALORANT ใครนำโน้ตเข้าแข่งได้','Who may bring notes into the VALORANT tournament area?','เอกสารและโน้ต','Documents and notes'),
('valorant','03','checkin','กติกา VALORANT รายงานตัวก่อนแข่งกี่นาที','How early must VALORANT tournament teams arrive at the venue?','เวลาการรายงานตัว','Check-in:'),
('valorant','03','new-content','กติกา VALORANT เอเจนท์ใหม่และแผนที่ใหม่ห้ามกี่สัปดาห์','How long are new agents and new maps restricted in the VALORANT tournament?','เอเจนท์ใหม่|แผนที่ใหม่','New agents may|New maps may'),
('valorant','03','settings','กติกา VALORANT การตั้งค่าเลือด ศพ FPS และ Latency เป็นอย่างไร','What do VALORANT tournament rules require for Blood, Bodies, FPS and Latency displays?','ผู้เล่นต้อง ปิด|ห้ามแสดงกราฟ','Turn OFF Blood'),
('valorant','04','forfeit-score','กติกา VALORANT ปรับแพ้บันทึกคะแนนเท่าไร','What score is recorded for a forfeited map in the VALORANT tournament?','การปรับแพ้ \(Forfeiture','If a forfeit'),
('valorant','06','overtime-timeout','กติกา VALORANT Tactical Timeout ช่วงต่อเวลาทบโควตาไหม','Do regulation Tactical Timeout quotas carry into VALORANT tournament overtime?','เมื่อเข้าสู่ช่วงต่อเวลา','In Overtime'),
('valorant','08','emergency','กติกา VALORANT emergency pause ได้กี่ครั้งกี่นาที','What are the request and time limits for a VALORANT emergency pause?','ขอได้ 1 ครั้ง|รวมเวลาทั้งหมด','One request|Total emergency'),
('valorant','08','rollback','กติกา VALORANT ย้อนรอบก่อนและหลังทำดาเมจได้ไหม','Can officials roll back a VALORANT tournament round before or after damage is dealt?','หากเกิดบั๊กก่อน|หากมีการทำดาเมจ','If a bug occurs before|If damage has'),
('valorant','09','kayo','กติกา VALORANT ZERO/POINT ของ KAY/O มีข้อยกเว้นอะไร','What exception applies to KAY/O ZERO/POINT under VALORANT tournament rules?','ข้อยกเว้นพิเศษ','Special exception:'),
]

def clauses(text):
    return [x.strip().lstrip('*•·- ').strip() for x in re.split(r'\n|\s+\*\s+|\s+(?=\d+(?:\.\d+)+\.?\s*[^\W\d_])', text) if x.strip()]

def norm(text):
    text = re.sub(r'^(?:\d+(?:\.\d+)+[.)]?|\d+[.)])\s*', '', text.strip())
    return re.sub(r'\s+', ' ', text.casefold()).strip()

def build():
    import sys
    sys.path.insert(0,str(PROJECT))
    from app.knowledge.localization import approved_localization
    source={r['id']:r for r in (json.loads(x) for x in (PROJECT/'data/competition_rules/competition_rule_chunks.jsonl').read_text(encoding='utf-8').splitlines())}
    cases=[]
    for game,section,detail,th,en,thpat,enpat in SPECS:
        sec,_,chunk=section.partition(':');chunk=chunk or '01'
        source_id=f'competition_rules_{BOOKS[game]}_s{sec}_c{chunk}'
        row=source[source_id]
        for locale,q,pattern in [('th',th,thpat),('en',en,enpat)]:
            text=row['text'] if locale=='th' else approved_localization(row,'text') or ''
            required=[line for line in clauses(text) if re.search(pattern,line,re.I)]
            assert required,(source_id,locale,pattern)
            variants=[q, ('สอบถามหน่อยครับ '+q+' หน่อย') if locale=='th' else ('Hello, could you help? '+q), q.replace('กติกา','กติกกา',1) if locale=='th' else q.replace('tournament','tournamment',1).replace('rules','ruls',1)]
            for index,question in enumerate(variants):
                cases.append(dict(id=f'R27-{game}-{detail}-{locale}-{index}',anchor=f'{game}-{detail}-{locale}',locale=locale,game=game,question=question,required_clauses=required,source_id=source_id,source_sha256=hashlib.sha256(row['text'].encode()).hexdigest(),status='answer',first_clause=True,mutation=['clean','wrapper','task_typo'][index],review='assistant source-clause contract; not organizer approved'))
    for locale in ('th','en'):
        for detail,q,mode in ([('age','กติกา Tekken 8 อายุขั้นต่ำเท่าไร','no_answer'),('technical-duration','VALORANT technical pause ได้กี่นาที','no_answer'),('no-game','กติกาแข่งขันมีอะไรบ้าง','clarification'),('unknown','กติกา Free Fire มีอะไรบ้าง','no_answer')] if locale=='th' else [('age','What is the Tekken 8 tournament minimum age?','no_answer'),('technical-duration','How long is a VALORANT technical pause?','no_answer'),('no-game','What are the tournament rules?','clarification'),('unknown','What are the Free Fire tournament rules?','no_answer')]):
            cases.append(dict(id=f'R27-safe-{detail}-{locale}',anchor=f'safe-{detail}-{locale}',locale=locale,question=q,status=mode,required_clauses=[],first_clause=False,mutation='control'))
    return cases

def check(case,response):
    answer=response.get('answer') or ''; mode=response.get('mode') or ''; failures=[]
    from tools.run_competition_rules_rag_ground_truth import actual_status
    if actual_status(answer,mode)!=case['status']: failures.append('outcome_mismatch')
    if response.get('category')!='competition_rules': failures.append('route_mismatch')
    body=answer.split('แหล่งข้อมูล:')[0].split('Source:')[0]
    body=re.sub(r'\s+',' ',body.casefold())
    for clause in case['required_clauses']:
        if norm(clause) not in body: failures.append('missing_complete_clause:'+clause)
    if case['first_clause']:
        first=norm(answer.splitlines()[0].removeprefix('คำตอบ: ').removeprefix('Answer: '))
        if not any(first and (norm(c).startswith(first) or first.startswith(norm(c))) for c in case['required_clauses']): failures.append('first_line_off_topic')
        hits=response.get('hits') or []
        if not hits or any(BOOKS[case['game']] not in str(h.get('id',''))+str(h.get('url','')) for h in hits): failures.append('wrong_game_evidence')
    if not response.get('valid',True): failures.append('validation_rejected')
    return failures

if __name__=='__main__':
    cases=build()
    with (REPORT/'content_contract_fixture_v2.json').open('x',encoding='utf-8') as f: json.dump({'cases':cases,'anchors':len(SPECS)*2+8,'scope':'literal clause completeness, first line, source game and safe outcomes; not universal semantic equivalence','revision':'split optional trailing outline dot, preserve initial cardinal quantities'},f,ensure_ascii=False,indent=2)
    print(len(cases))
