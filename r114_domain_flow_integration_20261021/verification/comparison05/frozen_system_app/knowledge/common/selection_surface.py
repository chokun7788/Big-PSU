"""Strip only polite wrappers around a pending selection; keep raw slot spans."""
import re
from .query_contract import normalize
def canonical(question):
    q=normalize(question).strip(' ?!.,')
    q=re.sub(r'^(?:ขอถามหน่อย\s*|ขอเลือก\s*|งั้น\s*|could you help me with this\s*:\s*|please\s+)', '',q,flags=re.I)
    q=re.sub(r'(?:\s*(?:ครับ|ค่ะ|คะ)|\s*ตอบสั้น\s*ๆ|[.;]\s*please be brief[.!]?)+$','',q,flags=re.I)
    return q.strip(' ?!.,')
