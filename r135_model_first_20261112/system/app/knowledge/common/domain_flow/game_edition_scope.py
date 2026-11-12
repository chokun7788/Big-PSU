"""Bounded source-derived numeric game-edition checks, not fuzzy name repair.

Only families attested by a source label ending in a numeric token are covered.
Person/time/currency quantities immediately following a family are not editions.
Opaque versions, Roman numerals and arbitrary sequel semantics are not inferred.
"""
import re
from .projection import title
from .scope import norm

def request(index,question):
    families={}
    for rid,record in index.records.items():
        if record.get('kind')!='game':continue
        labels=[*title(record).values(),*sum(record.get('aliases',{}).values(),[])]
        for label in labels:
            if not isinstance(label,str):continue
            match=re.fullmatch(r'(.+?\D)\s+(\d{1,4})',norm(label))
            if match:
                stem=match[1].strip();edition=match[2]
                families.setdefault(stem,{}).setdefault(edition,set()).add(rid)
    q=norm(question);requests=[];allowed=set();unresolved=False
    for stem,editions in families.items():
        pattern=(r'(?<![a-z0-9])' if stem[0].isascii() else '')+re.escape(stem)+r'\s*(\d{1,4})(?!\d)(?!\s*(?:คน|ชั่วโมง|นาที|บาท|people\b|persons?\b|players?\b|hours?\b|minutes?\b|baht\b))'
        asked={m[1] for m in re.finditer(pattern,q,re.I)}
        if not asked:continue
        requests.append({'source_family':stem,'requested_editions':sorted(asked)})
        if len(asked)!=1 or not asked<=editions.keys():unresolved=True
        for version in asked:allowed.update(editions.get(version,set()))
    return {'applicable':bool(requests),'requests':requests,'allowed_game_ids':sorted(allowed),'unresolved':unresolved,'basis':'explicit_numeric_family_from_current_game_source_labels'}

def allows(index,question,game_id):
    scope=request(index,question)
    return not scope['applicable'] or not scope['unresolved'] and game_id in scope['allowed_game_ids']
