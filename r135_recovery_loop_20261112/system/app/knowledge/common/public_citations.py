"""Public website corroboration; never substitutes for internal claim verification.

Entries are manually reviewed, pinned to record + evidence + exact output text.
An owner edit, withdrawal, changed source or new wording requires review again.
No network access, homepage guessing, approval changes or answer fallback here.
"""
import hashlib
import json
import re
from pathlib import Path

REGISTRY = Path(__file__).resolve().parents[3] / 'data/knowledge/verified_web_citations.json'


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                                     separators=(',', ':')).encode()).hexdigest()


def text_digest(value):
    return hashlib.sha256(str(value).encode()).hexdigest()


def corroboration(hit, snapshot, entries):
    record = snapshot.get('release', {}).get('records', {}).get(hit.get('record_id'))
    if not record:
        return None
    for entry in entries:
        if (entry['record_id'] != hit.get('record_id') or entry['field'] != hit.get('field')
                or entry['record_sha256'] != digest(record)
                or text_digest(hit.get('text', '')) not in entry['text_sha256']):
            continue
        identity = {k: hit.get(k) for k in ('source_id', 'snapshot_sha256', 'locator')}
        if identity not in entry['evidence']:
            continue
        pair = snapshot.get('source_pairs', {}).get(hit.get('source_id'))
        if not pair or hashlib.sha256(pair[1].encode()).hexdigest() != identity['snapshot_sha256']:
            continue
        return entry
    return None


def apply(answer, hits, snapshot, entries=None):
    if entries is None:
        try:
            entries = json.loads(REGISTRY.read_text(encoding='utf-8'))['entries']
        except (OSError, ValueError, KeyError, TypeError):
            entries = []
    result = []
    allowed = set()
    for hit in hits:
        entry = corroboration(hit, snapshot, entries)
        metadata = {**hit.get('metadata', {}), 'public_citation_status':
                    'website_corroborated' if entry else 'not_verified',
                    'internal_evidence_retained': True}
        item = {**hit, 'source_url': '', 'metadata': metadata}
        # Prevent an old URL in metadata from bypassing this policy.
        metadata.pop('source_url', None)
        metadata.pop('url', None)
        if entry:
            item.update(source_url=entry['url'], title=entry['title'])
            metadata.update(website_checked_at=entry['checked_at'],
                            website_access=entry['access'],
                            website_section=entry['section'],
                            website_scope='corroboration as observed; not publication or currentness approval')
            allowed.add(hit.get('citation_label'))
        result.append(item)
    # Keep internal hits/receipts intact; remove only unsupported public markers.
    answer = re.sub(r'\[(S\d+)\]', lambda m: m[0] if m[1] in allowed else '', answer)
    return answer, result
