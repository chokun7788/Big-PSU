"""Entity and applicability checks precede retrieval and model selection."""
import re,unicodedata,calendar
from functools import lru_cache
from datetime import datetime
from zoneinfo import ZoneInfo

BANGKOK=ZoneInfo('Asia/Bangkok')
THAI_DIGITS=str.maketrans('๐๑๒๓๔๕๖๗๘๙','0123456789')

def norm(value):
    return _norm_text(str(value))

@lru_cache(maxsize=32768)
def _norm_text(value):
    s=re.sub(r'\s+',' ',unicodedata.normalize('NFC',value).translate(THAI_DIGITS).casefold()).strip()
    return re.sub(r'\bplaystation\s*5\b','ps5',s)

def contains(text,label):
    q=norm(text);s=norm(label)
    if len(s)<2:return False
    # Almost every label is absent. Avoid compiling thousands of escaped
    # regular expressions while routing newly added FAQ records.
    if s not in q:return False
    ascii_word=lambda ch:'a'<=ch<='z' or '0'<=ch<='9'
    pos=q.find(s)
    while pos>=0:
        end=pos+len(s)
        if (not ascii_word(s[0]) or pos==0 or not ascii_word(q[pos-1])) and (not ascii_word(s[-1]) or end==len(q) or not ascii_word(q[end])):return True
        pos=q.find(s,pos+1)
    return False

def entity_contains(text,label):
    """Short aliases cannot bind inside a recognized action/component word.

    Thai has no mandatory spaces. Preserve ordinary compound device names,
    while giving a longer lexical operation precedence over its noun substring.
    """
    q=norm(text);s=norm(label)
    if not contains(q,s):return False
    if len(s)>2 or not re.fullmatch(r'[\u0e00-\u0e7f]+',s):return True
    lexical=[m.span() for m in re.finditer(r'จอง|การ์ดจอ',q)]
    return any(not any(a<=m.start() and m.end()<=b and b-a>len(s) for a,b in lexical) for m in re.finditer(re.escape(s),q))

def years(text):
    # Four-digit source years are protected; game editions such as Tekken 8
    # and price/session numbers are not rewritten into years.
    out=set()
    for y in re.findall(r'(?<!\d)((?:20|21|25|26)\d{2})(?!\d)',norm(text)):
        n=int(y);out.add(n-543 if n>=2500 else n)
    return out

def requested_years(text):
    q=norm(text)
    pattern=r'(?:ปี(?:\s*พ\.?ศ\.?)?\s*|\b(?:year|in|for|during)\s+)((?:20|21|25|26)\d{2})(?!\d)'
    return years(' '.join(re.findall(pattern,q)))

def reference_time(value=None):
    if isinstance(value,str):value=datetime.fromisoformat(value.replace('Z','+00:00'))
    if value is None:return datetime.now(BANGKOK)
    if value.tzinfo is None:raise ValueError('Reference time must include timezone')
    return value.astimezone(BANGKOK)

def in_year(at,year):
    return at.replace(year=year,day=min(at.day,calendar.monthrange(year,at.month)[1]))

def matching_subjects(facts,question):
    mentions={s for f in facts for s in f['subject'].values() if s and contains(question,s)}
    mentions={s for s in mentions if not any(norm(s)!=norm(t) and contains(t,s) for t in mentions)}
    return [f for f in facts if any(s in mentions for s in f['subject'].values())]

def requested_resources(question):
    # Applied only in live reader: these identifiers must bind exactly.
    return set(re.findall(r'(?<![a-z0-9])(?:pc\s*#?\s*\d+|[a-z][a-z_-]*station\s*#?\s*\d+|ps[45]\s*#\s*\d+|[a-z][a-z0-9_-]*\s*#\s*\d+)(?![a-z0-9])',norm(question)))

def canonical_resource(value):
    # Platform digits (PS5) belong to the family; leading zeroes belong to
    # the station number. PS5 #01 and PS5 #1 must name the same resource.
    match=re.fullmatch(r'(ps[45]|pc|cockpit|switch|vr)\s*#?\s*0*(\d+)',norm(value))
    if match:return match[1]+str(int(match[2]))
    s=re.sub(r'[\s#_-]+','',norm(value))
    return re.sub(r'(?<=[a-z])0+(\d+)$',lambda m:str(int(m[0])),s)

def resource_scope(facts,question):
    explicit=requested_resources(question)
    if not explicit:return None
    chosen=[]
    for f in facts:
        labels=list(f['subject'].values())+f.get('entity_aliases',[])
        bound={canonical_resource(s.split(' / ')[0]) for s in labels}
        if any(canonical_resource(x) in bound for x in explicit):chosen.append(f)
    return chosen

def validity_allows(fact,at):
    valid=fact.get('business_effective_period') or fact.get('validity')
    if not valid or valid.get('state')=='unknown':return None
    for key,op in [('effective_from','start'),('effective_until','end')]:
        raw=valid.get(key)
        if raw:
            t=reference_time(raw)
            if op=='start' and at<t:return False
            if op=='end' and at>=t:return False
    return True

def requested_minutes(question):
    q=norm(question)
    compound=re.search(r'(?<!\d)(\d+(?:\.\d+)?)\s*(?:ชั่วโมง|hours?|hrs?)\s*(?:and\s*)?(\d+(?:\.\d+)?)\s*(?:นาที|minutes?)',q,re.I)
    if compound and not re.search(r'ต่อรอบ|รอบละ|per session|each session|เทียบ|compare|different|หรือ|\bor\b',q,re.I):return float(compound[1])*60+float(compound[2])
    m=re.search(r'(?<!\d)(\d+(?:\.\d+)?)\s*(นาที|ชั่วโมง|minutes?|hours?|hrs?)\b',q)
    if m is None:m=re.search(r'(?<!\d)(\d+(?:\.\d+)?)\s*(นาที|ชั่วโมง)',q)
    if not m:
        if re.search(r'อย่างน้อย|ไม่เกิน|น้อยกว่า|มากกว่า|\b(?:at least|less than|more than|up to|under|over)\b',q):return None
        words={'one and a half':1.5,'half an':.5,'half a':.5,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'a':1,'an':1}
        names='|'.join(re.escape(s) for s in sorted(words,key=len,reverse=True))
        verbal=re.search(r'(?<![a-z])('+names+r')\s+(hours?|hrs?|minutes?)\b',q)
        if not verbal:return None
        n=words[verbal[1]];return n*60 if verbal[2] in {'hour','hours','hr','hrs'} else n
    number=float(m[1]);return number*60 if m[2] in {'ชั่วโมง','hour','hours','hr','hrs'} else number

def event_years(index,text):
    """A year inside an explicit game title is an edition, not an event year."""
    from .projection import title
    q=norm(text)
    if not years(q):return set()
    labels=getattr(index,'_game_edition_year_labels',None)
    if labels is None:
        labels={norm(s) for r in index.records.values() if r['kind']=='game' for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])] if years(s)}
        labels=sorted(labels,key=len,reverse=True);index._game_edition_year_labels=labels
    for s in labels:
        if len(s)>2 and not s.isdigit() and contains(q,s):q=q.replace(s,' ')
    return years(q)
