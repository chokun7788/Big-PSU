"""Need-level routing using task meanings and entities from the current data."""
import re
from .scope import norm,contains
from .vocabulary import POLICY_INTENTS,FACETS,matches

def split_needs(question,index=None):
    protected=[]
    if index is not None:
        for labels in index.subject_labels.values():
            for label in labels:
                if len(label)>2 and contains(question,label):
                    for m in re.finditer(re.escape(label),norm(question)):protected.append(m.span())
    q=norm(question) if protected else question
    cut_pattern=r'\s+and also\s+|แล้วขอ|[;\n]+|\s+แล้วก็\s+|\s+และ(?:ขอ|อยากรู้)\s*'
    cuts=[m for m in re.finditer(cut_pattern,q,re.I) if not any(a<=m.start()<b for a,b in protected)]
    parts=[];start=0
    for m in cuts:parts.append(q[start:m.start()]);start=m.end()
    parts.append(q[start:])
    if len(parts)==1:
        # Split a conjunction only when it starts a distinct task, not inside
        # a name, condition or a coordinated object such as keyboard and mouse.
        parts=re.split(r'\s+แล้ว(?=(?:ราคา|จอง|เปิด|ปิด|มีเกม|ต้อง))|\s+and\s+(?=(?:how (?:much|do i book)|what games|is .*open))',question,flags=re.I)
    combined=[]
    for p in parts:
        p=p.strip(' ,?')
        if not p:continue
        # A separated qualifier still constrains the preceding task. Dropping
        # it could quote a price for an audience the user explicitly denied.
        qualifier=re.match(r'^(?:i am\b|we are\b|i(?:\x27m|’m)\b|we(?:\x27re|’re)\b|for (?:a |an |the )?\d|ฉัน(?:เป็น|ไม่ใช่)|ผม(?:เป็น|ไม่ใช่)|เรา(?:เป็น|ไม่ใช่)|ไม่ใช่|สำหรับ)',p,re.I)
        if combined and qualifier:combined[-1]+=' '+p
        else:combined.append(p)
    return combined

def route(index,question):
    q=norm(question)
    # Polite framing is not an entity or business task ("studio sources" must
    # not route every English question to studio location).
    frame=r'^(?:based on (?:the )?studio sources[:,]?|could you help me with this:|please answer briefly:|i would like to know:|กำลังวางแผนไปใช้บริการ\s*เลยขอถามว่า|ถามจากข้อมูลที่ศูนย์ให้ไว้|ช่วยตอบสั้น\s*ๆ\s*ว่า|ขอสอบถามหน่อยครับ|รบกวนเช็กให้หน่อย|อยากรู้ว่า)\s*'
    while True:
        stripped=re.sub(frame,'',q,flags=re.I)
        if stripped==q:break
        q=stripped
    # A request to check a named machine for a dated booking slot is a live
    # task even if its wording omits the literal word "availability".
    from .scope import requested_resources
    if requested_resources(q) and matches(r'จอง|\bbook(?:ing)?\b|\breserve',q) and matches(r'ได้หรือยัง|ได้ไหม|ได้มั้ย|ถูกจอง|ว่าง|\bcan\b|available|free',q) and matches(r'20\d{2}-\d{2}-\d{2}|\d{1,2}:\d{2}|วันนี้|พรุ่งนี้|\btoday\b|\btomorrow\b',q):
        return 'C12'
    # Bind a complete current record ID before interpreting words embedded in
    # it (e.g. a rate ID can contain "staff" or "availability").
    explicit={f['category'] for rid in index.record_mentions(q) for f in index.byrecord[rid]}
    if len(explicit)==1:return next(iter(explicit))
    from .vocabulary import predicate_domain
    guarded=predicate_domain(q)
    if guarded:return guarded
    strong={cat:max((len(s) for s in labels if len(s)>2 and s in q and contains(q,s)),default=0) for cat,labels in index.subject_labels.items()}
    strongest=max(strong,key=strong.get) if strong and max(strong.values()) else None
    if matches(r'(?:รายการจอง|booking|reservation).{0,35}(?:หมายเลข|เลข|number|\bid\b|#)',q) and matches(r'ยืนยัน|สถานะ|จ่าย.*ยัง|paid|status|confirm|check',q):return 'C12'
    if matches(r'รับประกัน.*เครื่องสำรอง|เครื่องสำรอง.*รับประกัน|guarantee.*backup',q):return 'C08'
    special=[]
    for intent,cat,_,pattern in POLICY_INTENTS:
        if intent=='extend_session' and matches(FACETS['amount'],q):continue
        if intent in {'closure_after_booking','game_failure_switch','rain_reschedule','extend_session','equipment_compensation','logout_data'} and matches(pattern,q):special.append((intent,cat))
    if matches(r'การแข่งขัน|รายการแข่ง|\btournament\b|competition|rulebook|under .+section|according.*rules',q) or matches(r'กติกา',q) and strong.get('C13'):return 'C13'
    if strongest=='C13':return 'C13'
    if matches(r'รายการ(?!จอง)',q) and matches(r'ปี\s*\d{4}|รางวัล|ชนะเลิศ',q):return 'C13'
    if special:return special[0][1]
    if matches(r'ปุ่ม|กดอะไร|กดตรงไหน|ควบคุม|อินพุต|\binputs?\b|buttons?|controls?|action binding',q):return 'C05'
    if matches(FACETS['game_catalog'],q) or matches(FACETS['how_to_play'],q) or matches(FACETS['genre'],q):return 'C04'
    if matches(r'เหมา|เช่า|แพ็กเกจ|rental|package|whole.zone|out.of.hours',q) or strongest=='C07':return 'C07'
    if special:return special[0][1]
    if matches(r'ค่าปรับ|fixed.*fine|damage.*fine',q):return 'C10'
    if strongest=='C01' and matches(r'กิจกรรมอะไร|รายละเอียดของงาน|รายละเอียดกิจกรรม|describe',q) and not matches(r'ข่าว|news|สมัคร|registration',q):return 'C01'
    if matches(r'วันหยุดราชการ|วันธรรมดา.*(?:เปิด|ปิด)|ศูนย์(?:ยัง)?(?:เปิด|ปิด)',q):return 'C11'
    if matches(r'กิจกรรม|ข่าว|โปรโมชัน|ประกาศ|registration|event date|event details|synthetic.*event|news|promotion',q):return 'C14'
    if matches(r'เงินเดือน|salary|ที่อยู่บ้าน|home address|เบอร์มือถือส่วนตัว|private phone',q):return 'C02'
    if matches(r'ประกัน|serial|ซื้อจากร้าน|ซื้อเมื่อวัน',q):return 'C03'
    if matches(r'ใบเสร็จ|ใบกำกับ|ใบเสนอราคา|สลิป|โอน|ชำระ|payment|paid|payer|receipt|refund|quotation|invoice|overpay|underpay',q):
        if not matches(r'จองผิดวัน|เปลี่ยนวัน|wrong date|change.*booking|change.*service',q):return 'C09'
    if matches(r'กี่บาท|ราคา|ค่าบริการ|ค่าเล่น|\bprice\b|\bcost\b|\brate\b|\bfee\b|how much',q):return 'C06'
    if strongest=='C06' and matches(FACETS['duration_minutes'],q):return 'C06'
    if matches(r'ขัดข้อง|เครื่องค้าง|เครื่องดับ|เสียระหว่าง|\bfaulty\b|system fault',q):return 'C10'
    if matches(FACETS['live_status'],q) and not matches(r'รอบถัดไป|จองต่อ|extend|book.*normal process',q):return 'C12'
    if strongest=='C12' and not matches(r'ยกเลิก|เปลี่ยน|cancel|change',q):return 'C12'
    if matches(r'เวลาเปิด|เปิดกี่โมง|ปิดกี่โมง|วันนี้เปิด|วันนี้ปิด|ตอนนี้เปิด|วันปิดพิเศษ|วันหยุดราชการ|บำรุงรักษา|maintenance|bookable|opening|\bopen\b|\bclosed\b|reserve.*(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)',q):return 'C11'
    if strongest=='C11' or matches(FACETS['bookable_periods'],q) and matches(r'วัน|monday|tuesday|wednesday|thursday|friday|saturday|sunday',q):return 'C11'
    for _,cat,_,pattern in POLICY_INTENTS:
        if matches(pattern,q):return cat
    if matches(r'เกม.*(?:กี่คน|สองคน|สี่คน|เพื่อน)|เล่นกับเพื่อน|games?.*(?:players|two|four|friends)',q):return 'C04'
    if strong.get('C02') and (matches(FACETS['role'],q) or matches(FACETS['team'],q) or matches(r'ชื่อ|name|what does|group.+belong|directory',q)):return 'C02'
    if strongest=='C03' and any(matches(FACETS[k],q) for k in ['location','usage','capacity_persons','quantity','specifications','device_type','controllers']):return 'C03'
    if strongest in {'C02','C03','C04','C06','C07','C13','C14'}:return strongest
    if matches(r'จอง|ยกเลิก|เช็กอิน|เช็คอิน|booking|reserve|cancel|check.in|walk.in',q):return 'C08'
    if matches(r'อนุญาต|นำ.*(?:มา|เข้า)|เอา.*(?:มา|เข้า)|ได้ไหม|อายุ|guardian|allowed|may i|can i bring|permission',q):return 'C10'
    if matches(r'สเปก|กี่จอย|กี่เครื?อง|กี่เครือง|อุปกรณ์|ฮาร์ดแวร์|controllers?|equipment|hardware|specs?|quantity|capacity',q):return 'C03'
    if matches(r'บุคลากร|ตำแหน่ง|ดูแลงาน|รับผิดชอบ|หน้าที่|รายชื่อ|staff|role|responsib|team|personnel',q):return 'C02'
    if matches(r'ศูนย์|ที่อยู่|ตึก|อาคาร|ชั้น|แผนที่|ที่จอด|ช่องทาง|ติดต่อ|มหาวิทยาลัย|address|map|building|floor|contact|university|studio',q):return 'C01'
    # Protected names can classify questions without requiring a business
    # keyword. Field semantics disambiguate names shared across categories.
    bound=[cat for cat in ['C02','C04','C03','C13','C14','C01'] if index.bind(cat,q)]
    if len(bound)==1:return bound[0]
    if 'C04' in bound and matches(FACETS['summary'],q):return 'C04'
    return bound[0] if bound else None
