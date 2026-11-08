"""Read source-declared query patterns, never a legacy answer backend."""
import re
from .readers import confirmed,pending
def plan(index,category,question):
    hits=[]
    for f in index.bycat[category]:
        profile=f.get('legacy_search') or {}
        for pattern in profile.get('patterns',[]):
            if not isinstance(pattern,str) or len(pattern)>600:continue
            try:match=re.search(pattern,question,re.I)
            except re.error:continue
            if match:hits.append((profile.get('priority',0),len(match[0]),f));break
    if not hits:return None
    top=max((a,b) for a,b,_ in hits);selected=list({f['id']:f for a,b,f in hits if (a,b)==top}.values())
    # Distinct decisions remain scoped candidates. Do not concatenate their
    # policy text or claim the highest lexical score proves equivalence.
    signatures={f['value']['th'] for f in selected}
    if len(signatures)==1:
        result=confirmed(category,[selected[0]],'declared_legacy_query_profile',matched_profile_fact_ids=[f['id'] for f in selected]);result.locked=True;return result
    return pending(category,selected,'source_query_profiles_need_disambiguation')
