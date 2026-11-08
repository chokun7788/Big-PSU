"""Protect explicit Arabic-number editions using aliases of the recorded catalog.

Only numbers immediately attached to a known game stem are checked. Durations,
event years, station numbers and the rest of the user's sentence are untouched.
"""
from functools import lru_cache
import re
from app.core.normalization import normalize_text
from app.pipeline.entity_resolver import _game_resolver_index

@lru_cache(maxsize=2)
def _numbered_stems(catalog_version):
    groups={}
    for row in _game_resolver_index().rows_by_id.values():
        for alias in [row['title'],*row.get('aliases',())]:
            text=normalize_text(alias)
            match=re.match(r'^([^\d]+?)(\d+)(?:\D.*)?$',text)
            if not match:
                continue
            stem=match[1].rstrip()
            if len(re.sub(r'\W','',stem))<2:
                continue
            groups.setdefault(stem,set()).add(match[2])
    return tuple((stem,frozenset(versions)) for stem,versions in sorted(groups.items(),key=lambda p:len(p[0]),reverse=True))

def unsupported_numbered_game(query):
    if not re.search(r'\d',query):
        return None
    q=normalize_text(query)
    index=_game_resolver_index()
    confirmed_spans=[]
    for stem,versions in _numbered_stems(index.catalog_version):
        pattern=r'(?<![a-z0-9])'+re.escape(stem).replace(r'\ ',r'\s+')+r'\s*(\d+)(?![a-z0-9])'
        for match in re.finditer(pattern,q):
            if any(start <= match.start() and match.end() <= end for start,end in confirmed_spans):
                continue
            if match[1] not in versions:
                return {'requested_title':match[0].strip(),'requested_version':match[1],
                        'known_stem':stem,'recorded_versions':sorted(versions),'catalog_version':index.catalog_version}
            confirmed_spans.append(match.span())
    return None
