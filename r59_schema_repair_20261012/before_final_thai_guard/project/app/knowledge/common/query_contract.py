"""Schema-scoped query attributes. Contains language semantics, never owner facts.

Canonical field/description lookup remains dynamic. Semantic cues are reusable
attributes, not aliases for individual games or canned customer questions.
"""
from __future__ import annotations
import re,unicodedata
from .registry import CATALOG

def normalize(s):
    return re.sub(r'\s+',' ',unicodedata.normalize('NFC',str(s)).casefold().replace('เเ','แ')).strip()

def matches(q,term):
    term=normalize(term)
    if term not in q:return False
    # English substring matches (rate in operating, all in football) are unsafe.
    plural=r's?' if re.search(r'[a-z]{4,}$',term) and not term.endswith('s') else ''
    return bool(re.search((r'(?<![a-z0-9_])' if re.match('[a-z0-9]',term) else '')+re.escape(term)+plural+(r'(?![a-z0-9_])' if re.search('[a-z0-9]$',term) else ''),q))

def broad_request(q):
    q=normalize(q)
    if re.search(r'ไม่(?:ต้อง|เอา|อยาก).{0,12}(?:ทั้งหมด|ทุก|ครบ)|\b(?:not|don.t|do not|without)\b.{0,16}\b(?:all|everything|every)\b',q):return False
    return bool(re.search(r'(?:ข้อมูล|รายละเอียด|information|details).{0,10}(?:ทั้งหมด|ทุกส่วน|ทุกอย่าง|\ball\b|everything)|(?:ทั้งหมด|ทุกส่วน|ทุกอย่าง|\ball\b|everything).{0,10}(?:ข้อมูล|รายละเอียด|information|details)|\beverything\b|^(?:ทั้งหมด|ทุกอย่าง|all)\s*[?!.,]*$|(?:ทุก|all\s+)(?:เกม|เครื่อง|รายการ|หมวด|games|devices|records|categories)\b',q))

def live_request(q):
    q=normalize(q)
    if re.search(r'\bfree\s+(?:to\s+play|of\s+charge|admission)\b|เล่นฟรี|ไม่เสียเงิน',q):return False
    return bool(re.search(r'ว่าง|ถูกจอง|ไม่ว่าง|available\s+(?:now|today|at)|\boccupied\b|\bbooked\b|\bfree\s+(?:now|today|at|slot)\b',q))

def strip_names(q,ids,names):
    q=normalize(q)
    for rid in ids:
        for alias in sorted(names.get(rid,()),key=len,reverse=True):
            a=normalize(alias)
            p=(r'(?<![a-z0-9])' if re.match('[a-z0-9]',a) else '')+re.escape(a)+(r'(?![a-z0-9])' if re.search('[a-z0-9]$',a) else '')
            q=re.sub(p,' ',q)
    return re.sub(r'\s+',' ',q).strip()

def scope_kinds(kinds):
    result=set(kinds or CATALOG)
    if 'game' in result:result.update(('game_mode','game_service','control_set'))
    if 'competition' in result:result.add('competition_rule')
    return result

# Language descriptions/cues are attributed to field meaning, scoped by kind.
# Adding a new record needs no changes here; unseen fields can use canonical
# names/descriptions or the bounded semantic planner.
CUES={
 'how_to_play':['วิธีเล่น','เล่นยังไง','เล่นอย่างไร','เป้าหมาย','ต้องทำอะไรเพื่อเล่น','how to play','how do i play','do to play','instructions','gameplay'],
 'genre':['แนวเกม','ประเภทเกม','genre','kind of game'],
 'summary':['เกี่ยวกับอะไร','เนื้อเรื่อง','game about','summary','synopsis'],
 'supported_platforms':['แพลตฟอร์ม','เครื่องไหน','อุปกรณ์ไหน','เล่นที่ไหน','supported platforms','available on','where can i play'],
 'platform':['แพลตฟอร์ม','เครื่องประเภท','platform'],
 'bindings':['ปุ่ม','ควบคุม','กดอะไร','กดตรงไหน','controls','buttons','jump','กระโดด','input bindings'],
 'specifications':['สเปก','specifications','specs','hardware'],
 'device_type':['ประเภทอุปกรณ์','อุปกรณ์ประเภท','device type'],
 'operational_status':['ยังใช้งาน','พร้อมให้บริการ','operational status','in service','out of service','working'],
 'session_minutes':['หนึ่งรอบ','เวลาเล่น','ได้เวลาเล่น','ระยะเวลาเล่น','session','play duration','how long can i play'],
 'occupancy_minutes':['กินช่องจอง','กันช่อง','กันทรัพยากร','booking occupancy','occupancy'],
 'required_proofs':['หลักฐาน','เอกสาร','proof','documents'],
 'eligibility':['ใครใช้สิทธิ์','คุณสมบัติ','ใครอยู่','qualifies','eligible','eligibility'],
 'value':['ติดต่อ','ช่องทาง','เบอร์','contact','reach the operator','reach them','phone','email'],
 'office_hours':['ติดต่อได้ช่วง','เวลาตอบ','office hours','contact hours'],
 'details':['กฎ','กฏ','ข้อกำหนด','นโยบาย','policy','rules','requirements'],
 'conditions_all':['เงื่อนไข','conditions','requirements'],
 'decision':['อนุญาต','ห้ามไหม','allowed','permission','permitted'],
 'exceptions':['ข้อยกเว้น','exceptions'],
 'consequence':['ผลเมื่อ','ค่าปรับ','consequence','penalty'],
 'steps':['ขั้นตอน','ทำยังไง','procedure','steps','walk me through'],
 'required_documents':['เอกสาร','หลักฐาน','documents','proof'],
 'accessibility':['ความช่วยเหลือ','รถเข็น','เข้าถึง','accessibility','wheelchair'],
 'offered':['มีให้เล่น','มีเกมนี้','offered','offer this game'],
 'game_version':['ติดตั้งรุ่น','เวอร์ชันเกม','game version','build','installed version'],
 'amount_minor':['ราคา','ค่าบริการ','กี่บาท','price','cost','fee','how much','เหมาเท่าไหร่','เล่นฟรี','free to play','free of charge'],
 'duration_minutes':['กี่นาที','ระยะเวลา','duration','minutes','how long'],
 'equipment_included':['รวมอุปกรณ์','อุปกรณ์ที่รวม','equipment included','which equipment'],
 'bookable_periods':['ช่วงจอง','เวลาจอง','จองช่วง','เวลาที่จอง','ช่วงเวลาไหนที่จอง','booking hours','bookable','time periods can i book'],
 'open_periods':['เวลาเปิด','เปิดกี่โมง','เปิดช่วง','opening hours','opening periods','opening','open hours'],
 'maintenance_periods':['บำรุงรักษา','ซ่อมบำรุง','maintenance'],
 'state':['เปิดหรือปิด','เปิดปิด','ปิดไหม','closed','open or closed','opening status'],
 'reason':['เพราะอะไร','เหตุผล','why','reason'],
 'rulebook_release':['กติกาฉบับ','กฎเวอร์ชัน','rulebook release','version of the rules'],
 'competition_dates':['แข่งวัน','competition dates','tournament dates'],
 'text':['เนื้อหา','ข้อความกติกา','กำหนดอะไร','rule say','rule require','text of this rule','rule text'],
 'completeness':['ข้อมูลครบ','สมบูรณ์','content complete','completeness'],
 'body':['ประกาศว่า','ประกาศอะไร','ข่าวนี้แจ้ง','announcement say','announced','information is in','body'],
 'event_start':['เริ่ม','เริ่มจบ','start','begin'],
 'event_end':['จบ','สิ้นสุด','end','finish'],
 'role':['รับผิดชอบ','ช่วยเรื่องไหน','role','handle','responsibilities'],
 'public_contact_id':['ติดต่อ','public contact','contact'],
 'answer':['คำตอบ','ตอบคำถาม','answer','respond'],
 'scope_note':['กรณีไหน','ขอบเขต','scope','limitations'],
 'status_mapping':['จับคู่สถานะ','แปลงเป็นสถานะ','status mapping','statuses mapped','statuses translated'],
 'freshness_policy':['เก็บข้อมูลนาน','อายุข้อมูล','freshness','cache','ttl'],
 'building':['ตึก','อาคาร','building','tower'],
 'floor':['ชั้น','floor'],
 'map_url':['แผนที่','map'],
 'age_rating':['เรตเกม','อายุเกม','age rating','age restriction'],
 'edition':['ภาค','edition'],
}

LOCATION={'center':'address','zone':'location','facility':'location','contact':'value'}
CAPACITY={'zone':'room_seats','resource':'capacity_persons','service':'capacity_max','game_mode':'players_max','game':'players_max','rate':'persons_max','rental_package':'room_seats'}
MINIMUM={'service':'capacity_min','game_mode':'players_min','game':'players_min','rate':'persons_min'}

def resolve_fields(question,kinds=None):
    q=normalize(question);primary=set(kinds or CATALOG);scoped=scope_kinds(primary)
    keys={f['key'] for k in scoped for f in CATALOG[k]['fields']}
    if primary&{'service','audience','zone'}:keys.add('amount_minor')
    cue_keys={f['key'] for k in primary for f in CATALOG[k]['fields']}
    if 'game' in primary:cue_keys.update(f['key'] for k in ('game_mode','game_service','control_set') for f in CATALOG[k]['fields'])
    if 'competition' in primary:cue_keys.update(f['key'] for f in CATALOG['competition_rule']['fields'])
    if primary&{'service','audience','zone'}:cue_keys.add('amount_minor')
    found=[];evidence=[]
    def add(key,reason):
        if key in keys and key not in found:found.append(key);evidence.append({'field':key,'cue':reason,'method':'schema_attribute'})
    # Canonical names and full description labels always stay dynamic/casefolded.
    for kind in sorted(scoped):
        for f in CATALOG[kind]['fields']:
            for label in (f['key'],f['key'].replace('_',' '),f['meaning_th']):
                if matches(q,label):add(f['key'],label);break
    for key,cues in CUES.items():
        if key not in cue_keys:continue
        for cue in cues:
            if key=='open_periods' and cue=='opening' and re.search(r'\bopening\s+status\b',q) and not re.search(r'\bopening\s+(?:hours|periods|times)\b',q):continue
            if matches(q,cue):add(key,cue);break
    if re.search(r'อยู่(?:ตรง|ที่|บริเวณ|จุด|ไหน)|ที่อยู่|เดินไปจุด|ไปที่ไหน|\bwhere\b|\blocation\b|\baddress\b|\blocated\b',q):
        for k in primary:
            if k in LOCATION:add(LOCATION[k],'location query')
    if re.search(r'กี่(?:คน|ที่)|จำนวน(?:คน|ผู้เล่น|ที่นั่ง)|คนเล่น|รองรับ.*คน|how many (?:people|users|players|seats)|(?:maximum|minimum).*(?:users|players|player|people)|seating capacity|player count',q):
        minimal=bool(re.search(r'ขั้นต่ำ|อย่างน้อย|\bminimum\b|\bat least\b',q))
        maximal=bool(re.search(r'สูงสุด|เยอะสุด|มากสุด|\bmaximum\b|\bat most\b',q))
        for k in primary:
            if minimal and k in MINIMUM:add(MINIMUM[k],'minimum participant count')
            if (not minimal or maximal) and k in CAPACITY:add(CAPACITY[k],'participant/seating count')
    if 'service' in primary and re.search(r'กี่นาที|how many minutes|how long',q) and 'occupancy_minutes' not in found:add('session_minutes','play duration')
    if 'contact' in primary and re.search(r'ติดต่อได้ช่วง|ติดต่อได้เวลา|office hours',q):add('office_hours','contact hours')
    if 'competition' in primary and re.search(r'กฎ|กฏ|กติกา|\brules\b',q) and 'rulebook_release' not in found:add('text','competition rule text')
    # Rules of the game and tournament rules are different scopes. The caller
    # performs a competition join only when competition intent is explicit.
    return found,evidence

def unresolved_clauses(q,kinds):
    parts=re.split(r'และ|แล้วก็|\band\b|\balso\b|[;\n]',normalize(q))
    return [p.strip(' ?!.,') for p in parts if p.strip(' ?!.,') and not resolve_fields(p,kinds)[0] and not broad_request(p) and not re.fullmatch(r'(?:please|ครับ|ค่ะ|หน่อย|ขอข้อมูล|tell me)',p.strip())]
