"""Bilingual audience concepts, bound to audience labels actually in the catalog."""
import re
from .registry import value
from .query_contract import normalize,matches

def resolve(question,records):
    q=normalize(question)
    neg=r'(?:ไม่ใช่|ไม่ได้เป็น|\bnot\s+(?:(?:a|an|the)\s+)?)\s*'
    removed=False
    for r in records.values():
        if r['kind']!='audience':continue
        v=value(r,'name') or {};labels=list(v.values()) if isinstance(v,dict) else [v]
        labels+=r.get('aliases',{}).get('th',[])+r.get('aliases',{}).get('en',[])
        for label in sorted((normalize(x) for x in labels if x),key=len,reverse=True):
            q,n=re.subn(neg+re.escape(label), ' ',q);removed=removed or bool(n)
    q,n=re.subn(neg+r'(?:psu\s+)?(?:general adult|general public|students?|staff|alumni|alumnus|นักศึกษา|นักเรียน|บุคลากร|ศิษย์เก่า|บุคคลทั่วไป|ประชาชนทั่วไป)', ' ',q);removed=removed or bool(n)
    concepts=[]
    if re.search(r'บุคคลทั่วไป|ประชาชนทั่วไป|\bgeneral (?:adult|public)\b',q):concepts.append('general_adult')
    if re.search(r'ศิษย์เก่า|\balumni\b|\balumnus\b|นักเรียน|นักศึกษาทั่วไป|\bgeneral student\b',q):concepts.append('alumni_general_student')
    if re.search(r'\bpsu\s+(?:students?|staff)\b|\b(?:students?|staff)\s+(?:of|at|from)\s+psu\b|(?:นักศึกษา|บุคลากร|เจ้าหน้าที่)\s*(?:ม\.อ\.?|มอ(?:\s|$)|มหาวิทยาลัยสงขลานครินทร์)',q):concepts.append('psu_student_staff')
    selected=[]
    for rid,r in records.items():
        if r['kind']!='audience':continue
        name=value(r,'name') or {};labels=list(name.values()) if isinstance(name,dict) else [name]
        aliases=labels+r.get('aliases',{}).get('th',[])+r.get('aliases',{}).get('en',[])
        literal=any(matches(q,a) for a in aliases if isinstance(a,str) and a)
        source=' '.join(str(a or '') for a in labels).lower()
        semantic=('general_adult' in concepts and bool(re.search(r'general\s+adult|บุคคลทั่วไป',source)) or 'alumni_general_student' in concepts and bool(re.search(r'alumni|ศิษย์เก่า|general\s+student|นักศึกษาทั่วไป',source)) or 'psu_student_staff' in concepts and bool(re.search(r'psu|ม\.?อ\.?',source)) and bool(re.search(r'student|staff|นักศึกษา|บุคลากร',source)))
        if literal or semantic:selected.append(rid)
    return (selected if selected or concepts or removed else None),{'concepts':concepts,'negated_group_removed':removed,'selected_ids':selected,'source':'existing_audience_labels_only'}
