"""Conservative interpretation-only edits; owner names and raw input stay intact."""
import re
from .query_contract import normalize

def canonical(question,records,names):
    import unicodedata
    q=re.sub(r'\s+',' ',unicodedata.normalize('NFC',str(question)).replace('เเ','แ')).strip();protected={};i=0
    aliases=sorted({normalize(a) for aa in names.values() for a in aa if len(normalize(a))>=2},key=len,reverse=True)
    for alias in aliases:
        pattern=(r'(?<![a-z0-9])' if re.match('[a-z0-9]',alias) else '')+re.escape(alias)+(r'(?![a-z0-9])' if re.search('[a-z0-9]$',alias) else '')
        def hide(m):
            nonlocal i
            key='\ue000'+str(i)+'\ue001';i+=1;protected[key]=m.group();return key
        q=re.sub(pattern,hide,q,flags=re.I)
    q=re.sub(r'^(?:(?:ขอถามหน่อย|ขอสอบถาม|ขอถาม|ช่วยตอบ|รบกวน)\s*)+','',q)
    q=re.sub(r'^(?:could you help me with this|please tell me|please explain)\s*:?\s*','',q,flags=re.I)
    q=re.sub(r'\s*(?:ตอบสั้น\s*ๆ|ขอแบบสั้น\s*ๆ|please be brief)[.!?\s]*$','',q,flags=re.I)
    q=re.sub(r'\s*(?:ครับ|ค่ะ|คะ)[.!?\s]*$','',q)
    # A concrete duplicate-vowel error channel, restricted to intent vocabulary.
    q=q.replace('ราาคา','ราคา').replace('กฏ','กฎ')
    from .schema_language import recover_schema_language
    def recover(m):
        token=m.group();base=token[:-1] if token.casefold().endswith('s') else token
        target,edits=recover_schema_language(base,set(r['kind'] for r in records.values()))
        if not edits:return token
        a=base.casefold();b=target.casefold();diff=[i for i in range(min(len(a),len(b))) if a[i]!=b[i]]
        transposed=len(a)==len(b) and len(diff)==2 and diff[1]==diff[0]+1 and a[diff[0]]==b[diff[1]] and a[diff[1]]==b[diff[0]]
        duplicated=len(a)==len(b)+1 and any(a[:i]+a[i+1:]==b and i>0 and a[i]==a[i-1] for i in range(len(a)))
        return target+('s' if len(base)<len(token) else '') if transposed or duplicated else token
    q=re.sub(r'[A-Za-z]+',recover,q)
    for key,original in protected.items():q=q.replace(key,original)
    return q.strip(' .!?')
