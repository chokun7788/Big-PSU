"""A named game's recorded offering is distinct from live slot occupancy."""
import re
from .named_spans import masked
def named_game_offering(index,question):
    from .dialogue_task import mentions
    if not mentions(index,question,{'game'}):return False
    text=masked(index,question)
    if re.search(r'ว่าง|ถูกจอง|ตอนนี้|วันนี้|พรุ่งนี้|ปุ่ม|ควบคุม|กติกา|ราคา|กี่บาท|วิธีจอง|\b(?:now|currently|today|tomorrow|occupied|busy|booked|vacant|buttons?|controls?|controller|tournament|rules?|price|cost|fee|free|booking|reserve)\b|20\d\d-\d\d-\d\d|\d{1,2}:\d{2}|\d\s*(?:am|pm)\b',text,re.I):return False
    if re.search(r'จันทร์|อังคาร|พุธ|พฤหัส|ศุกร์|เสาร์|อาทิตย์|\b(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b',text,re.I):return False
    return bool(re.search(r'\b(?:is|are)\s+there\b.*\b(?:available|offered|installed)\b|\b(?:is|are)\b.*\b(?:available|offered|installed)\b|\bdo you (?:have|offer)\b',text,re.I))
