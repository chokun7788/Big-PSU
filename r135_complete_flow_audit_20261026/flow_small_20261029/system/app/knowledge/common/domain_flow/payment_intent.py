"""Document availability and additional-proof predicates, not payment values."""
import re


def predicate_text(question):
    # ราคา inside ใบเสนอราคา is part of a document noun. Keep raw offsets so
    # a separate price clause outside that noun can still be observed.
    return re.sub(r'ใบเสนอราคา', lambda m: ' ' * len(m[0]), question)


def request(question):
    from .policy_scope import requested_actions
    text=predicate_text(question)
    if re.search(r'กี่บาท|เท่าไหร่|เท่าไร|ราคา|\b(?:price|cost|fee)\b|how much',text,re.I):
        return None
    actions=requested_actions(question,'C09')
    if actions=={'documents'} and re.search(r'ขอ|ออก|ได้ไหม|ได้หรือไม่|\b(?:can|may|issue|obtain|get|provide)\b',question,re.I):
        return 'documents'
    if actions=={'underpayment'} and re.search(r'หลักฐาน|สลิป|อย่างไร|ยังไง|\b(?:how|proof|evidence|slip)\b',question,re.I):
        return 'underpayment'
    return None
