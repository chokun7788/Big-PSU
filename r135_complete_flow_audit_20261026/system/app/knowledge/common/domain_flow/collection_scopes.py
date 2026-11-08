"""Source-set identities for registered list operations, independent of output."""
import re
from .projection import value,title
from .scope import contains,event_years,norm

def inventory_zones(index,question):
    from .dialogue_task import platforms
    ps=set(platforms(index,question))
    zones={rid for rid,r in index.records.items() if r['kind']=='zone' and any(contains(question,s) for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])])}
    if not zones:zones={rid for rid,r in index.records.items() if r['kind']=='zone' and ps&set(platforms(index,' '.join([*title(r).values(),*sum(r.get('aliases',{}).values(),[])])))}
    return zones

def equipment_zones(index,record):
    rows=[x for x in value(record,'specifications') or [] if isinstance(x,dict) and x.get('key')=='zone']
    locations={norm(x.get('value','')) for x in rows}
    if len(locations)!=1:return None
    labels={}
    for rid,r in index.records.items():
        if r['kind']=='zone':
            for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])]:
                if s:labels.setdefault(norm(s),set()).add(rid)
    text=next(iter(locations));parts=[text] if text in labels else [norm(s) for s in text.split('/')]
    if any(len(labels.get(part,set()))!=1 for part in parts):return None
    return set().union(*(labels[part] for part in parts))

def inventory(index,question):
    pool=[f for f in index.bycat['C03'] if f['facet']=='name'];zones=inventory_zones(index,question)
    if not zones:return [] if re.search(r'โซน|\bzone\b',question,re.I) else pool
    return [f for f in pool if zones&(equipment_zones(index,index.records[f['record_id']]) or set())]

def inventory_refs(index,question,facts):
    zones=inventory_zones(index,question);result=[]
    for f in facts:
        r=index.records[f['record_id']]
        for zid in sorted(zones&(equipment_zones(index,r) or set())):
            z=index.records[zid]
            refs=[*r['fields']['specifications'].get('evidence_refs',[]),*z['fields'].get('name',{}).get('evidence_refs',[])]
            result.append({'equipment_record_id':r['record_id'],'equipment_revision':r.get('revision'),'zone_record_id':zid,'zone_revision':z.get('revision'),'evidence_refs':refs})
    return result

def rules(index,question):
    bound=index.bind('C13',question)
    games={rid for rid,r in index.records.items() if r['kind']=='game' and any(contains(question,s) for s in [*title(r).values(),*sum(r.get('aliases',{}).values(),[])])}
    pool=bound or index.bycat['C13'] if games else bound
    if games:pool=[f for f in pool if f.get('game_id') in games]
    asked=event_years(index,question)
    from .scope import rule_source_years
    if asked:pool=[f for f in pool if asked<=rule_source_years(index,f)]
    from .scope import rule_edition_events
    editions=rule_edition_events(index,question,pool)
    if editions is not None:pool=[f for f in pool if f.get('event_id') in editions]
    events={f.get('event_id') for f in pool if f.get('event_id')}
    if len(events)!=1:return []
    return [f for f in pool if f['facet']=='rule_clause']

def policies(index,question):
    # Exact source target binds a policy collection; otherwise list the recorded
    # source collection, not an inferred permission for a named service/person.
    bound=index.bind('C10',question)
    pool=bound or index.bycat['C10']
    return [f for f in pool if f['facet']=='owner_policy']

def expected(index,task,question):
    if task.category=='C03' and task.facet=='name':return inventory(index,question)
    if task.category=='C13' and task.facet=='rule_clause':return rules(index,question)
    if task.category=='C10' and task.facet=='owner_policy':return policies(index,question)
    return None
