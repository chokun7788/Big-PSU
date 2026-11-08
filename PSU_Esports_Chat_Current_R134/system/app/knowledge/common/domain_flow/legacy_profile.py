"""Read source-declared query patterns, never a legacy answer backend."""
import re
from .readers import confirmed,pending

def declared_frame(index,question):
    """Recover a unique explicit source heading, not a bag of answer words."""
    from .scope import norm,contains
    hits=[]
    for f in index.facts:
        profile=f.get('legacy_search') or {}
        if not profile.get('projected_facet'):continue
        for label in (f.get('faq_question') or {}).values():
            if len(norm(label))<6 or re.search(r'\.\*|\(\?:|\\[wsdb]|\|',label):continue
            if contains(question,label):hits.append((len(norm(label)),f))
    if not hits:return None
    top=max(n for n,_ in hits);found=[f for n,f in hits if n==top]
    frames={(f['category'],f['facet']) for f in found}
    if len(frames)!=1:return None
    category,facet=next(iter(frames))
    return category,facet,sorted({f['id'] for f in found})
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
