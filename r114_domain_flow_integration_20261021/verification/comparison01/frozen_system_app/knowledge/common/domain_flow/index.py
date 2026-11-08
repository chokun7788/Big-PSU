"""Request-local evidence index. Reads content only, never test workloads."""
import collections,math,re
from .scope import norm,contains,matching_subjects

def tokens(text):
    s=norm(text);words=re.findall(r'[a-z0-9]+|[\u0e00-\u0e7f]+',s)
    return set(words+['~'+s[i:i+3] for i in range(max(0,len(s)-2)) if ' ' not in s[i:i+3]])

class FactIndex:
    def __init__(self,data):
        self.records=data.get('records',{});self.facts=data['facts'];self.byid={f['id']:f for f in self.facts}
        if len(self.byid)!=len(self.facts):raise ValueError('Duplicate fact identities')
        self.bycat=collections.defaultdict(list);self.byrecord=collections.defaultdict(list)
        self.ftokens={};self.subjects=collections.defaultdict(list)
        self.subject_labels=collections.defaultdict(lambda:collections.defaultdict(list))
        self.entity_labels=collections.defaultdict(lambda:collections.defaultdict(list))
        for f in self.facts:
            self.bycat[f['category']].append(f);self.byrecord[f['record_id']].append(f)
            self.ftokens[f['id']]=tokens(' '.join([*f['subject'].values(),*f['label'].values(),*f.get('aliases',[]),*f['value'].values()]))
            for s in set(norm(x) for x in f['subject'].values() if x):self.subject_labels[f['category']][s].append(f)
            aliases=f.get('entity_aliases',[])
            if not aliases:aliases=sum(self.records.get(f['record_id'],{}).get('aliases',{}).values(),[])
            record=self.records.get(f['record_id'],{})
            if record.get('kind')=='service':
                from .projection import value
                platform=value(record,'platform')
                if platform:aliases=[*aliases,platform]
            for s in set(norm(x) for x in aliases if x):self.entity_labels[f['category']][s].append(f)

    def rank(self,cat,question,pool=None,limit=12):
        qt=tokens(question);ranked=[]
        for f in self.bycat[cat] if pool is None else pool:
            ft=self.ftokens[f['id']];score=len(qt&ft)/math.sqrt(max(1,len(qt))*max(1,len(ft)))
            if any(contains(question,s) for s in f['subject'].values()):score+=1
            if any(len(s)>2 and contains(question,s) for s in f['label'].values()):score+=.8
            ranked.append((score,f))
        return sorted(ranked,key=lambda x:(-x[0],x[1]['id']))[:limit]

    def bind(self,cat,question):
        q=norm(question);labels=self.subject_labels[cat]
        mentions=[s for s in labels if len(s)>=2 and s in q and contains(q,s)]
        mentions=[s for s in mentions if not any(s!=other and s in other for other in mentions)]
        if mentions:return list({f['id']:f for s in mentions for f in labels[s]}.values())
        # Only entity aliases may bind a target. Generic field/action aliases
        # must never silently change the requested entity.
        aliases=self.entity_labels[cat];matches=[s for s in aliases if len(s)>=2 and s in q and contains(q,s)]
        if not matches:return []
        top=max(map(len,matches))
        return list({f['id']:f for s in matches if len(s)==top for f in aliases[s]}.values())
