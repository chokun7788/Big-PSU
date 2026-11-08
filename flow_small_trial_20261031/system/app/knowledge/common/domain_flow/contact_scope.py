"""C01 source subject/channel binding; an unknown unit cannot borrow a neighbor."""
import re
from .projection import value
from .scope import norm

CHANNELS={'email':r'อีเมล|อีเมล์|\be-?mail\b','phone':r'โทรศัพท์|เบอร์|\b(?:phone|telephone)\b',
          'facebook':r'เฟซบุ๊ก|เฟสบุ๊ค|\b(?:facebook|fb)\b','website':r'เว็บไซต์|\bwebsite\b','onsite':r'ติดต่อ.*หน้าเคาน์เตอร์|\bonsite\b'}
KINDS={'operator':{'center'},'description':{'center'},'address':{'center'},'building':{'center'},'floor':{'center'},'map_url':{'center'},'value':{'contact'},'office_hours':{'contact'},'location':{'facility'},'usage_conditions':{'facility'}}

def generic(question):
    question=re.sub(r'\bnumber\b',' ',question,flags=re.I)
    q=norm(question)
    q=re.sub(r'ขอ(?:สอบถาม|สอบถม|ถาม)|หนาอย|หน่อย|อะ(?=\s|$)',' ',q)
    q=re.sub(r'\b(?:what|where|who|which|how|is|are|can|do|does|i|we|you|your|the|a|an|of|for|in|on|to|get|find|please|me|give|show|link|map|address|building|floor|contact|contacts|e?mail|phone|telephone|number|facebook|fb|website|web|page|onsite|office|hours|information|details|description|studio|center|centre|operator|operates|operate|use|usage|conditions|located|it|s)\b',' ',q)
    q=re.sub(r'ขอสอบถาม|ขอข้อมูล|หน่อย|กรุณา|ครับ|ค่ะ|ศูนย์|สตูดิโอ|ผู้ดำเนินการ|ข้อมูลทั่วไป|รายละเอียด|ที่อยู่|แผนที่|ลิงก์|ติดต่อ|ช่องทาง|อีเมล|อีเมล์|โทรศัพท์|เบอร์|เฟซบุ๊ก|เฟสบุ๊ค|เว็บไซต์|เวลาติดต่อ|เวลา|อาคาร|ตึก|ชั้น|ตั้งอยู่ที่ไหน|ตั้งอยู่ที่ใด|ตั้งอยู่|อยู่ที่ไหน|อยู่ที่|อยู่ตรงไหน|อยู่|อะไร|ไหน|ใด|กี่|วิธีใช้|เงื่อนไข|การใช้งาน|ของ|ใน|คือ|เป็น|และ',' ',q)
    return not re.search(r'[\w\u0e00-\u0e7f]',q)

def candidates(index,question,facet):
    bound=index.bind('C01',question)
    is_generic=generic(question)
    if is_generic and facet in {'operator','description','address','building','floor','map_url','location'} and re.search(r'ศูนย์|สตูดิโอ|\b(?:studio|cent(?:er|re))\b',question,re.I):
        return [f for f in index.bycat['C01'] if index.records[f['record_id']]['kind']=='center']
    pool=bound or (index.bycat['C01'] if is_generic else [])
    kinds=KINDS.get(facet)
    if kinds:pool=[f for f in pool if index.records[f['record_id']]['kind'] in kinds|{'faq'}]
    channels={k for k,p in CHANNELS.items() if re.search(p,question,re.I)}
    if channels:
        pool=[f for f in pool if (index.records[f['record_id']]['kind']=='contact' and value(index.records[f['record_id']],'channel') in channels) or (is_generic and index.records[f['record_id']]['kind']=='faq' and f.get('source_declared_contact_field') and f.get('contact_channel') in channels)]
    return pool

def plan(index,question,facet):
    from .readers import confirmed,blocked
    pool=candidates(index,question,facet)
    kinds={index.records[f['record_id']]['kind'] for f in pool}
    if facet=='location' and kinds=={'center'}:facet='address'
    # Existing explicit FAQ source decisions retain their own authority path.
    if kinds=={'faq'} and not any(f.get('source_declared_contact_field') and f['facet']==facet for f in pool):return None
    fields={facet}|({'building','floor'} if facet=='address' else set())
    chosen=[f for f in pool if f['facet'] in fields]
    if not chosen:return blocked('C01','contact_subject_channel_or_field_not_confirmed')
    if len({f['record_id'] for f in chosen if index.records[f['record_id']]['kind']=='center'})>1:return blocked('C01','center_identity_requires_clarification','missing_input')
    return confirmed('C01',chosen,'typed_contact_subject_channel_field',operator='detail')
