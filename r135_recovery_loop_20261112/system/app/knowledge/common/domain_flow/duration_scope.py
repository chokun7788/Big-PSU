"""Retain adjacent repeated scalar durations as unresolved raw input."""
import re
from .named_spans import masked
TOKEN=re.compile(r'(?P<number>(?<![\d.])\d+(?:\.\d+)?|(?<![a-z])(?:one|two|three|four|five|six|seven|eight|nine|ten|a|an))\s*(?P<unit>ชั่วโมง|นาที|hours?|hrs?|minutes?)(?![a-z])',re.I)
WORDS={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'a':1,'an':1}
def repeated_duration(index,question):
    text=masked(index,question);hits=list(TOKEN.finditer(text))
    def number(m):return WORDS[m['number'].lower()] if m['number'].lower() in WORDS else float(m['number'])
    def unit(m):return 'hours' if m['unit'].lower() in {'ชั่วโมง','hour','hours','hr','hrs'} else 'minutes'
    for a,b in zip(hits,hits[1:]):
        if not text[a.end():b.start()].strip() and number(a)==number(b) and unit(a)==unit(b):
            return {'reason':'adjacent_repeated_duration_requires_clarification','source_span':{'start':a.start(),'end':b.end(),'text':question[a.start():b.end()]},'normalization_applied':False}
    return None

def guard(index,category,question,meaning=None):
    if category not in {'C06','C07'}:return None
    proof=repeated_duration(index,meaning.quote if meaning is not None else question)
    if not proof:return None
    from .readers import blocked
    result=blocked(category,proof['reason'],'missing_input');result.locked=True
    result.metadata.update(duration_ambiguity=proof,context_clarification={'th':'ระยะเวลาถูกระบุซ้ำ ต้องการระยะเวลาเดียวหรือรวมหลายรอบครับ? กรุณายืนยันระยะเวลารวมก่อนคำนวณราคา','en':'The duration is repeated. Do you mean one duration or multiple sessions? Please confirm the intended total before I calculate a price.'})
    return result
