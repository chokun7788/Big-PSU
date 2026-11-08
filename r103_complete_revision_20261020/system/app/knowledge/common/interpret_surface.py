"""Conservative interpretation-only edits; owner names and raw input stay intact."""
import re
from .query_contract import normalize

def canonical(question,records,names):
    q=normalize(question);protected={};i=0
    aliases=sorted({normalize(a) for aa in names.values() for a in aa if len(normalize(a))>=2},key=len,reverse=True)
    for alias in aliases:
        pattern=(r'(?<![a-z0-9])' if re.match('[a-z0-9]',alias) else '')+re.escape(alias)+(r'(?![a-z0-9])' if re.search('[a-z0-9]$',alias) else '')
        def hide(m):
            nonlocal i
            key='\ue000'+str(i)+'\ue001';i+=1;protected[key]=m.group();return key
        q=re.sub(pattern,hide,q)
    q=re.sub(r'^(?:(?:ขอถามหน่อย|ขอสอบถาม|ขอถาม|ช่วยตอบ|รบกวน)\s*)+','',q)
    q=re.sub(r'^(?:could you help me with this|please tell me|please explain|explain the procedure for)\s*:?\s*','',q)
    q=re.sub(r'\s*(?:ตอบสั้น\s*ๆ|ขอแบบสั้น\s*ๆ|please be brief)[.!?\s]*$','',q)
    q=re.sub(r'\s*(?:ครับ|ค่ะ|คะ)[.!?\s]*$','',q)
    # A concrete duplicate-vowel error channel, restricted to intent vocabulary.
    q=q.replace('ราาคา','ราคา').replace('กฏ','กฎ')
    from .schema_language import recover_schema_language
    q,_=recover_schema_language(q,set(r['kind'] for r in records.values()))
    for key,original in protected.items():q=q.replace(key,original)
    return q.strip(' .!?')
