import hashlib,json,os,re,sys
from pathlib import Path
PROJECT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
REPORT=Path(Path(__file__).with_name('r28_report_path.txt').read_text(encoding='utf-8').strip())
sys.path.insert(0,str(PROJECT));os.environ['PSU_BILINGUAL_EN_ENABLED']='1'
from app.knowledge.localization import approved_localization
BOOKS={'cs2':'cs2_psu_phuket_2026','rov':'rov_blueket_2025_men','tekken8':'tekken8_psu_esports','valorant':'valorant_psu_phuket_2026'}
# Questions, source locations and clause constraints are declared before runtime changes.
SPECS=[
('cs2-format','cs2','20','กติกา CS2 รูปแบบทัวร์นาเมนต์แข่งแบบคัดออกยังไง','What elimination format is used in the CS2 tournament?',r'Single Elimination',r'Single Elimination'),
('cs2-mode','cs2','23','กติกา CS2 ใช้โหมดการแข่งขันอะไร','Which competitive mode is used under CS2 tournament rules?',r'Competitive',r'Competitive'),
('cs2-bracket','cs2','15','กติกา CS2 ประกาศสายล่วงหน้ากี่วันและมาสายเป็นยังไง','Under CS2 tournament rules, when is the bracket announced and what happens if a team is late?',r'สายการแข่งขัน',r'bracket'),
('cs2-bugs','cs2','37','กติกา CS2 ใช้บัคแผนที่หรือ Engine ได้ไหม','Under CS2 tournament rules, may players use map or engine bugs?',r'ห้ามใช้บัค',r'bugs'),
('cs2-streams','cs2','38','กติกา CS2 ดูสตรีมสดระหว่างแข่งได้ไหม','Under CS2 tournament rules, may players watch live streams during the match?',r'ห้ามผู้เล่นดูสตรีม',r'live streams'),
('cs2-gear-quality','cs2','42','กติกา CS2 ใครรับผิดชอบคุณภาพอุปกรณ์ของผู้เล่น','Under CS2 tournament rules, who is responsible for the quality and readiness of personal equipment?',r'รับผิดชอบ',r'responsible'),
('cs2-custom-settings','cs2','45','กติกา CS2 ปรับ Brightness Resolution Crosshair ได้ไหมและปรับที่ไหน','Under CS2 tournament rules, may I change Brightness, Resolution and Crosshair, and where?',r'Brightness',r'Brightness'),
('cs2-macros','cs2','46','กติกา CS2 ใช้สคริปต์หรือมาโครได้ไหม','Under CS2 tournament rules, are scripts or macros allowed?',r'สคริปต์',r'scripts'),
('cs2-install','cs2','47','กติกา CS2 ติดตั้งโปรแกรมเองได้ไหม','Under CS2 tournament rules, may players install software on the supplied computers?',r'ติดตั้งโปรแกรม',r'install'),
('cs2-prep','cs2','50','กติกา CS2 ในช่วงเตรียมตัวมีผู้เล่นได้กี่คน','Under CS2 tournament rules, how many players may be in the match preparation area?',r'เตรียมตัว',r'preparation'),
('cs2-drinks','cs2','53','กติกา CS2 ในพื้นที่แข่งอนุญาตอาหารเครื่องดื่มอะไรบ้าง','Under CS2 tournament rules, what food and drinks are permitted in the competition area?',r'น้ำดื่ม',r'drinking water'),
('cs2-authority','cs2','57','กติกา CS2 คำตัดสินใครถือเป็นที่สุดและผู้จัดเปลี่ยนกฎได้ไหม','Under CS2 tournament rules, whose decisions are final and may organizers amend the rules?',r'อำนาจตัดสิน',r'final'),
('valorant-macros','valorant','01','กติกา VALORANT มาโครทั้งซอฟต์แวร์และฮาร์ดแวร์ใช้ได้ไหม','Under VALORANT tournament rules, are software or hardware macros allowed?',r'ห้ามใช้มาโคร',r'macros.*prohibited'),
('valorant-prep','valorant','02','กติกา VALORANT ช่วง Match Prep มีผู้เล่นได้กี่คน','Under VALORANT tournament rules, how many players are allowed in the match preparation area?',r'จำนวนบุคลากร',r'No more than 6'),
('valorant-drinks','valorant','02','กติกา VALORANT กินดื่มอะไรได้ในพื้นที่แข่ง','Under VALORANT tournament rules, what food and beverages are permitted in the competition area?',r'อาหารและเครื่องดื่ม',r'drinking water'),
('valorant-regular-timeout','valorant','06','กติกา VALORANT Tactical Timeout รอบปกติได้กี่ครั้งและกี่วินาที','Under VALORANT tournament rules, how many Tactical Timeouts are allowed in regulation and how long is each?',r'ขอได้ 2 ครั้ง',r'2 requests'),
('valorant-technical-reason','valorant','07','กติกา VALORANT Technical Pause ใช้เมื่อมีปัญหาอะไร','Under VALORANT tournament rules, which problems qualify for a Technical Pause?',r'ใช้เมื่อมีปัญหา',r'Used when'),
('valorant-outside','valorant','09','กติกา VALORANT ใช้สกิลนอกขอบแผนที่เพื่อหาข้อมูลได้ไหม','Under VALORANT tournament rules, may abilities be used outside map boundaries for information?',r'ห้ามใช้สกิล|ข้อยกเว้นพิเศษ.*KAY/O',r'Abilities.*not|Special exception:.*KAY/O'),
('valorant-cypher','valorant','09','กติกา VALORANT กล้อง Cypher วางทะลุ Texture ให้มองไม่เห็นได้ไหม','Under VALORANT tournament rules, may Cypher cameras be invisible or indestructible through map textures?',r'ห้ามวางกล้อง Cypher',r'Cypher cameras'),
('valorant-boost','valorant','09','กติกา VALORANT ต่อตัวเพื่อนให้กระโดดสูงกว่าปกติได้ไหม','Under VALORANT tournament rules, may teammates boost a player above normal jump height?',r'การกระโดดต่อตัว',r'Using teammates to.*(?:jump|boost)'),
('tekken-custom','tekken8','03','กติกา Tekken 8 ปรับชุดทรงผมเอฟเฟกต์ตัวละครได้ไหม','Under Tekken 8 tournament rules, may character outfits, hairstyles and effects be customized?',r'ห้าม ปรับแต่งตัวละคร',r'customization'),
('tekken-glitch','tekken8','03','กติกา Tekken 8 ใช้ Bug หรือ Glitch สร้างความได้เปรียบได้ไหม','Under Tekken 8 tournament rules, may bugs or glitches be used for an advantage?',r'ห้ามใช้ Bug',r'Bug or Glitch|Bugs? or glitches?'),
('tekken-dispute','tekken8','08','กติกา Tekken 8 ถ้ามีข้อพิพาทต้องแจ้งใครและคำตัดสินใครเป็นที่สุด','Under Tekken 8 tournament rules, who must be notified of problems and whose dispute decision is final?',r'แจ้งผู้จัด|ข้อโต้แย้ง',r'notify|disputes|objections'),
('rov-side','rov','06','กติกา RoV เกมแรกใครอยู่สีฟ้าและเกมต่อไปใครเลือกฝั่ง','Under RoV tournament rules, which team is blue in game one and who chooses the side in later games?',r'เกมแรก ทีม',r'first match'),
('rov-late','rov','06','กติกา RoV เริ่มแข่งช้าเกิน 15 นาทีเป็นยังไง','Under RoV tournament rules, what happens if a team starts more than 15 minutes late?',r'ช้าเกิน',r'15 minutes'),
('rov-runes','rov','06','กติกา RoV ใส่รูนและระบบพลังเสริมได้ไหม','Under RoV tournament rules, are runes and enhancement systems allowed?',r'ใส่รูน',r'runes'),
('rov-global','rov','06','กติกา RoV ใช้การแบนและเลือกฮีโร่แบบไหน','Under RoV tournament rules, what hero ban and pick system is used?',r'Global Ban/Pick',r'Global Ban/Pick'),
('rov-force-majeure','rov','06_c02','กติกา RoV เน็ตล่มทั้งบริเวณหรือเซิร์ฟเวอร์ล่มต้องทำยังไงและใครตัดสินให้แข่งใหม่','Under RoV tournament rules, who decides on a rematch after an area-wide ISP or game server failure?',r'เหตุสุดวิสัย',r'force majeure'),
]
# Composite expected coverage is the union of independent source assertions.
PAIRS=[
('cs2-macro-install','cs2-macros','cs2-install','กติกา CS2 ใช้มาโครได้ไหม แล้วติดตั้งโปรแกรมเองได้ไหม','Under CS2 tournament rules, are macros allowed and may I install software?'),
('cs2-custom-macro','cs2-custom-settings','cs2-macros','กติกา CS2 ปรับ Brightness Resolution Crosshair ที่ไหน แล้วใช้สคริปต์หรือมาโครได้ไหม','Under CS2 tournament rules, where may Brightness, Resolution and Crosshair be changed, and are scripts or macros allowed?'),
('cs2-prep-drinks','cs2-prep','cs2-drinks','กติกา CS2 ช่วงเตรียมตัวมีผู้เล่นได้กี่คนและในพื้นที่แข่งกินดื่มอะไรได้บ้าง','Under CS2 tournament rules, how many players may prepare and what food or drinks are permitted?'),
('cs2-bug-stream','cs2-bugs','cs2-streams','กติกา CS2 ใช้บัคแผนที่ได้ไหม แล้วดูสตรีมสดระหว่างแข่งได้ไหม','Under CS2 tournament rules, may I use map bugs and watch live streams during a match?'),
('cs2-format-mode','cs2-format','cs2-mode','กติกา CS2 ใช้รูปแบบคัดออกอะไรและโหมดการแข่งขันอะไร','Under CS2 tournament rules, what elimination format and competitive mode are used?'),
('cs2-bracket-authority','cs2-bracket','cs2-authority','กติกา CS2 สายประกาศเมื่อไหร่ มาสายเป็นยังไง และคำตัดสินใครเป็นที่สุด','Under CS2 tournament rules, when is the bracket announced, what happens for lateness and whose decisions are final?'),
('valorant-macro-drinks','valorant-macros','valorant-drinks','กติกา VALORANT ใช้มาโครได้ไหมและกินดื่มอะไรได้ในพื้นที่แข่ง','Under VALORANT tournament rules, are macros permitted and what food or beverages are allowed?'),
('valorant-cypher-outside','valorant-cypher','valorant-outside','กติกา VALORANT กล้อง Cypher วางทะลุ Texture ได้ไหมและใช้สกิลนอกขอบแผนที่ได้ไหม','Under VALORANT tournament rules, may Cypher cameras clip through map textures and may abilities be used outside map boundaries?'),
('valorant-prep-timeout','valorant-prep','valorant-regular-timeout','กติกา VALORANT Match Prep มีได้กี่คน และ Tactical Timeout รอบปกติได้กี่ครั้งกี่วินาที','Under VALORANT tournament rules, how many players may be in match preparation and how many regulation Tactical Timeouts are allowed with what duration?'),
('tekken-custom-glitch','tekken-custom','tekken-glitch','กติกา Tekken 8 ปรับชุดทรงผมตัวละครได้ไหม แล้วใช้ Bug Glitch ได้ไหม','Under Tekken 8 tournament rules, may character outfits be customized and may bugs or glitches be used?'),
('rov-side-global','rov-side','rov-global','กติกา RoV เกมแรกใครอยู่สีฟ้าและเกมต่อไปใครเลือกฝั่ง แล้วแบนเลือกฮีโร่แบบไหน','Under RoV tournament rules, which team is blue in game one, who chooses later sides and what hero ban/pick system is used?'),
('rov-runes-late','rov-runes','rov-late','กติกา RoV ใช้รูนได้ไหม แล้วเริ่มช้าเกิน 15 นาทีเป็นยังไง','Under RoV tournament rules, are runes allowed and what happens for a start more than 15 minutes late?'),
]

def clauses(text):
    return [x.strip().lstrip('*-• ').strip() for x in re.split(r'\n|\s+\*\s+|\s+(?=\d+(?:\.\d+)+\.?\s*[^\W\d_])',text) if x.strip()]
def build():
    rows={x['id']:x for x in [json.loads(line) for line in (PROJECT/'data/competition_rules/competition_rule_chunks.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]}
    anchors={};cases=[]
    for key,game,section,th,en,thpattern,enpattern in SPECS:
        sid='competition_rules_'+BOOKS[game]+'_s'+(section if '_c' in section else section+'_c01')
        row=rows[sid]
        for locale,question,pattern in [('th',th,thpattern),('en',en,enpattern)]:
            text=row['text'] if locale=='th' else approved_localization(row,'text')
            assert text,(key,locale,'missing localization')
            expected=[x for x in clauses(text) if re.search(pattern,x,re.I)]
            assert expected,(key,locale,pattern,text)
            anchors[key,locale]={'game':game,'question':question,'clauses':expected,'sources':[sid],'source_sha256':{sid:hashlib.sha256(row['text'].encode('utf-8')).hexdigest()},'kind':'single'}
    for key,left,right,th,en in PAIRS:
        for locale,q in [('th',th),('en',en)]:
            a,b=anchors[left,locale],anchors[right,locale]
            assert a['game']==b['game']
            anchors[key,locale]={'game':a['game'],'question':q,'clauses':list(dict.fromkeys(a['clauses']+b['clauses'])),'sources':list(dict.fromkeys(a['sources']+b['sources'])),'source_sha256':dict(a['source_sha256'],**b['source_sha256']),'kind':'composite'}
    for (anchor,locale),spec in anchors.items():
        q=spec['question']
        variants=[('clean',q),('polite','สอบถามหน่อยครับ '+q+' ครับ' if locale=='th' else 'Could you help me? '+q),('task-typo',q.replace('กติกา','กติกกา') if locale=='th' else q.replace('tournament','tournamment').replace('rules','ruls'))]
        for n,(mutation,question) in enumerate(variants):
            cases.append(dict(spec,id=f'R28-{anchor}-{locale}-{n}',anchor=anchor,locale=locale,question=question,mutation=mutation,status='answer'))
    controls=[
        ('no-game','กติกาแข่งขันมีอะไรบ้าง','What are the tournament rules?','clarification',[]),
        ('unsupported','กติกา Dota 2 มีอะไรบ้าง','What are the Dota 2 tournament rules?','no_answer',[]),
        ('age','กติกา Tekken 8 อายุขั้นต่ำกี่ปี','What is the Tekken 8 tournament minimum age?','no_answer',['18 years','อายุ 18']),
        ('age-multi','กติกา CS2 eligibility และ minimum age คืออะไร','What are the CS2 tournament eligibility and minimum age requirements?','no_answer',['minimum age is','อายุขั้นต่ำคือ']),
        ('fee','กติกา CS2 ค่าสมัครกี่บาท','What is the CS2 tournament registration fee?','no_answer',['100 THB','100 บาท']),
        ('fee-multi','กติกา CS2 ใช้สคริปต์ได้ไหมและค่าสมัครกี่บาท','Under CS2 tournament rules, are scripts allowed and what is the registration fee?','safe_unknown_fee',['registration fee is','ค่าสมัครคือ']),
        ('pause-conflict','กติกา Tekken 8 หยุดเกมได้ไหม','May I pause under Tekken 8 tournament rules?','conflict',[]),
        ('clipped-rov','กติกา RoV ข้อ 6.1.5.1 บทลงโทษเต็มว่าอะไร','What is the complete RoV tournament penalty clause 6.1.5.1?','no_answer',[]),
    ]
    for anchor,th,en,status,forbidden in controls:
        for locale,question in [('th',th),('en',en)]:cases.append({'id':f'R28-control-{anchor}-{locale}','anchor':anchor,'locale':locale,'question':question,'mutation':'control','kind':'control','game':'','clauses':[],'sources':[],'source_sha256':{},'status':status,'forbidden':forbidden})
    return {'scope':'Constructed source-frozen development corpus; not organizer approval or all-question accuracy. Includes single, composite and unavailable/conflict controls.','cases':cases,'anchor_count':len(SPECS)+len(PAIRS),'single_anchors':len(SPECS),'composite_anchors':len(PAIRS),'controls':len(controls)*2}

if __name__=='__main__':
    data=build()
    with (REPORT/'composition_fixture_v1.json').open('x',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,indent=2)
    print(json.dumps({k:v for k,v in data.items() if k!='cases'},ensure_ascii=False));print('total',len(data['cases']))
