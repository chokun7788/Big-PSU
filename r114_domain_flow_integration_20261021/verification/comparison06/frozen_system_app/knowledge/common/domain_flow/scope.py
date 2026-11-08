"""Entity and applicability checks precede retrieval and model selection."""
import re,unicodedata,calendar
from datetime import datetime
from zoneinfo import ZoneInfo

BANGKOK=ZoneInfo('Asia/Bangkok')
THAI_DIGITS=str.maketrans('๐๑๒๓๔๕๖๗๘๙','0123456789')

def norm(value):
    s=re.sub(r'\s+',' ',unicodedata.normalize('NFC',str(value)).translate(THAI_DIGITS).casefold()).strip()
    return re.sub(r'\bplaystation\s*5\b','ps5',s)

def contains(text,label):
    q=norm(text);s=norm(label)
    if len(s)<2:return False
    # Almost every label is absent. Avoid compiling thousands of escaped
    # regular expressions while routing newly added FAQ records.
    if s not in q:return False
    left=r'(?<![a-z0-9])' if re.match('[a-z0-9]',s) else ''
    right=r'(?![a-z0-9])' if re.search('[a-z0-9]$',s) else ''
    return bool(re.search(left+re.escape(s)+right,q))

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
    return set(re.findall(r'(?<![a-z0-9])(?:pc\s*#?\s*\d+|[a-z][a-z_-]*station\s*#?\s*\d+|ps[45]\s*#\s*\d+)(?![a-z0-9])',norm(question)))

def canonical_resource(value):
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
    m=re.search(r'(?<!\d)(\d+(?:\.\d+)?)\s*(นาที|ชั่วโมง|minutes?|hours?|hrs?)\b',q)
    if m is None:m=re.search(r'(?<!\d)(\d+(?:\.\d+)?)\s*(นาที|ชั่วโมง)',q)
    if not m:return None
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
