"""Need-level routing using task meanings and entities from the current data."""
import re
from .scope import norm,contains
from .vocabulary import POLICY_INTENTS,FACETS,matches

def split_needs(question):
    parts=re.split(r'\s+and also\s+|แล้วขอ|[;\n]+|\s+แล้วก็\s+|\s+และ(?:ขอ|อยากรู้)\s*',question,flags=re.I)
    if len(parts)==1:
        # Split a conjunction only when it starts a distinct task, not inside
        # a name, condition or a coordinated object such as keyboard and mouse.
        parts=re.split(r'\s+แล้ว(?=(?:ราคา|จอง|เปิด|ปิด|มีเกม|ต้อง))|\s+and\s+(?=(?:how (?:much|do i book)|what games|is .*open))',question,flags=re.I)
    return [p.strip(' ,?') for p in parts if p.strip(' ,?')]

def route(index,question):
    q=norm(question)
    if matches(r'กติกา|การแข่งขัน|รายการแข่ง|\btournament\b|competition|under .+section|according.*rules',q):return 'C13'
    if matches(r'กิจกรรม|ข่าว|โปรโมชัน|ประกาศ|registration|event date|event details|synthetic.*event|news|promotion',q):
        if not matches(r'จองเหมา|เช่าจัดงาน|out.of.hours',q):return 'C14'
    if matches(r'ปุ่ม|กดอะไร|กดตรงไหน|ควบคุม|which input|buttons?|controls?|action binding',q):return 'C05'
    if matches(FACETS['live_status'],q) and not matches(r'รอบถัดไป|จองต่อ|extend|book.*normal process',q):return 'C12'
    if matches(r'ใบเสร็จ|ใบกำกับ|ใบเสนอราคา|สลิป|โอน|ชำระ|payment|paid|payer|receipt|refund|quotation|invoice|overpay|underpay',q):
        if not matches(r'จองผิดวัน|เปลี่ยนวัน|wrong date|change.*booking|change.*service',q):return 'C09'
    if matches(r'เหมา|แพ็กเกจ|rental|package|whole.zone|out.of.hours',q):return 'C07'
    if matches(r'เวลาเปิด|เปิดกี่โมง|ปิดกี่โมง|วันนี้เปิด|วันนี้ปิด|ตอนนี้เปิด|บำรุงรักษา|maintenance|bookable|opening|\bopen\b|\bclosed\b|reserve.*(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)',q):return 'C11'
    if matches(FACETS['amount'],q) or matches(r'นาทีต่อรอบ|คิดเงิน|billing|per person|sessions?$',q):return 'C06'
    for _,cat,_,pattern in POLICY_INTENTS:
        if matches(pattern,q):return cat
    if matches(FACETS['game_catalog'],q) or matches(FACETS['how_to_play'],q) or matches(FACETS['genre'],q):return 'C04'
    if matches(r'เกม.*(?:กี่คน|สองคน|สี่คน|เพื่อน)|เล่นกับเพื่อน|games?.*(?:players|two|four|friends)',q):return 'C04'
    if matches(r'จอง|ยกเลิก|เช็กอิน|เช็คอิน|booking|reserve|cancel|check.in|walk.in',q):return 'C08'
    if matches(r'อนุญาต|นำ.*(?:มา|เข้า)|เอา.*(?:มา|เข้า)|ได้ไหม|อายุ|guardian|allowed|may i|can i bring|permission',q):return 'C10'
    if matches(r'สเปก|กี่จอย|กี่เครื?อง|กี่เครือง|อุปกรณ์|ฮาร์ดแวร์|controllers?|equipment|hardware|specs?|quantity|capacity',q):return 'C03'
    if matches(r'บุคลากร|ตำแหน่ง|ดูแลงาน|รับผิดชอบ|หน้าที่|รายชื่อ|staff|role|responsib|team|personnel',q):return 'C02'
    if matches(r'ศูนย์อยู่|ที่อยู่|ตึก|อาคาร|ชั้น|แผนที่|ที่จอด|ช่องทาง|ติดต่อ|มหาวิทยาลัย|address|map|building|floor|contact|university|studio',q):return 'C01'
    # Protected names can classify questions without requiring a business
    # keyword. Field semantics disambiguate names shared across categories.
    bound=[cat for cat in ['C02','C04','C03','C13','C14','C01'] if index.bind(cat,q)]
    if len(bound)==1:return bound[0]
    if 'C04' in bound and matches(FACETS['summary'],q):return 'C04'
    return bound[0] if bound else None
