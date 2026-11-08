"""Request-local evidence index. Reads content only, never test workloads."""
import collections,math,re,copy
from .scope import norm,contains,entity_contains,matching_subjects

def tokens(text):
    s=norm(text);words=re.findall(r'[a-z0-9]+|[\u0e00-\u0e7f]+',s)
    return set(words+['~'+s[i:i+3] for i in range(max(0,len(s)-2)) if ' ' not in s[i:i+3]])

class FactIndex:
    def __init__(self,data):
        self.records=data.get('records',{});self.sources=data.get('sources',{});self.facts=copy.deepcopy(data['facts'])
        self.source_pairs=data.get('source_pairs',{})
        from .projection import attach_rule_scope
        attach_rule_scope(self.facts,self.records)
        from .source_decisions import current_corrections,entries
        self.source_corrections=current_corrections(self)
        replaced={p['record_id'] for p in self.source_corrections}
        from .projection import value
        declared={rid for rid,r in self.records.items() if (value(r,'legacy_search') or {}).get('source_decision')}
        verified={r['record_id'] for r,d in entries(self)}
        self.invalid_source_decisions=declared-verified
        self.facts=[f for f in self.facts if f['record_id'] not in replaced|self.invalid_source_decisions]
        self.byid={f['id']:f for f in self.facts}
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

    def record_mentions(self,question):
        # Native identifiers are opaque entity labels, never a bag of words.
        mentions=[rid for rid in self.byrecord if contains(question,rid)]
        return [rid for rid in mentions if not any(rid!=other and rid in other for other in mentions)]

    def rank(self,cat,question,pool=None,limit=12):
        qt=tokens(question);ranked=[]
        for f in self.bycat[cat] if pool is None else pool:
            ft=self.ftokens[f['id']];score=len(qt&ft)/math.sqrt(max(1,len(qt))*max(1,len(ft)))
            if any(contains(question,s) for s in f['subject'].values()):score+=1
            if any(len(s)>2 and contains(question,s) for s in f['label'].values()):score+=.8
            ranked.append((score,f))
        return sorted(ranked,key=lambda x:(-x[0],x[1]['id']))[:limit]

    def bind(self,cat,question):
        explicit=[f for rid in self.record_mentions(question) for f in self.byrecord[rid] if f['category']==cat]
        if explicit:return explicit
        q=norm(question);labels=self.subject_labels[cat]
        mentions=[s for s in labels if len(s)>=2 and s in q and entity_contains(q,s)]
        mentions=[s for s in mentions if not any(s!=other and s in other for other in mentions)]
        if mentions:return list({f['id']:f for s in mentions for f in labels[s]}.values())
        # Only entity aliases may bind a target. Generic field/action aliases
        # must never silently change the requested entity.
        aliases=self.entity_labels[cat];matches=[s for s in aliases if len(s)>=2 and s in q and entity_contains(q,s)]
        if not matches:
            if cat=='C02':return self.person_spelling(question)
            return []
        spans=[(m.start(),m.end(),s) for s in matches for m in re.finditer(re.escape(s),q)]
        chosen={s for a,b,s in spans if not any(c<=a and b<=d and d-c>b-a for c,d,_ in spans)}
        return list({f['id']:f for s in sorted(chosen) for f in aliases[s]}.values())

    def person_spelling(self,question):
        """Unique full-name spelling recovery with an exact source surname."""
        def distance(a,b):
            previous=list(range(len(b)+1))
            for i,ca in enumerate(a,1):
                current=[i]
                for j,cb in enumerate(b,1):current.append(min(current[-1]+1,previous[j]+1,previous[j-1]+(ca!=cb)))
                previous=current
            return previous[-1]
        words=re.findall(r'[a-z]+',norm(question));found=set()
        for label,fs in self.entity_labels['C02'].items():
            parts=re.findall(r'[a-z]+',label)
            if parts and parts[0] in {'mr','mrs','ms','miss','dr','prof','professor'}:parts=parts[1:]
            if len(parts)!=2 or len(parts[-1])<5:continue
            for i,w in enumerate(words):
                if i and w==parts[-1] and len(parts[0])>=5 and distance(words[i-1],parts[0])<=2:
                    found.update(f['record_id'] for f in fs)
        if len(found)!=1:return []
        return [f for f in self.byrecord[next(iter(found))] if f['category']=='C02']
