"""A named rental package owns its local field predicate, not its zone's stock.

Names come from the current source. This bounded interpreter does not resolve
arbitrary comparisons, conditions, missing names or unrelated sibling needs.
"""
import re
from .financial import _labels

FIELDS = {
    'amount_thb': r'กี่บาท|ราคา|จ่าย.*เท่าไหร่|\b(?:price|cost|fee)\b|how much(?!\s+(?:time|long))',
    'duration_minutes': r'กี่นาที|นานเท่าไหร่|นานเท่าไร|ระยะเวลา|\b(?:duration|minutes)\b|how long',
    'equipment_included': r'รวมเครื่องอะไร|อุปกรณ์อะไร|อุปกรณ์.*รวม|รวม.*อุปกรณ์|\b(?:equipment|devices)\b.*\b(?:include|included|come|provided)\b|what.*\b(?:include|included)\b',
    'room_seats': r'ที่นั่ง|นั่งได้กี่คน|\b(?:seats|seating)\b',
}


def mentions(index, question):
    hits = []
    for rid, record in index.records.items():
        if record.get('kind') != 'rental_package':
            continue
        for label in _labels(record):
            if not isinstance(label, str) or len(label.strip()) < 3:
                continue
            pattern = r'\s+'.join(re.escape(p) for p in label.split())
            if label[0].isascii() and label[0].isalnum():
                pattern = r'(?<![a-z0-9])' + pattern
            if label[-1].isascii() and label[-1].isalnum():
                pattern += r'(?![a-z0-9])'
            hits.extend({'record_id': rid, 'start': m.start(), 'end': m.end(), 'text': m[0]}
                        for m in re.finditer(pattern, question, re.I))
    return [h for h in hits if not any(o['start'] <= h['start'] and h['end'] <= o['end']
                and o['end']-o['start'] > h['end']-h['start'] for o in hits)]


def request(index, question):
    hits = mentions(index, question)
    if len({h['record_id'] for h in hits}) != 1:
        return None
    chars = list(question)
    for hit in hits:
        chars[hit['start']:hit['end']] = ' ' * (hit['end']-hit['start'])
    predicate = ''.join(chars)
    # A real additional object/predicate must reach the wider planner. The
    # native caller splits explicit sibling clauses before using this helper.
    if re.search(r'ปุ่ม|เกมอะไร|มีเกม|สเปก|เปิดกี่|ว่าง|คืนเงิน|ใบเสร็จ|\b(?:games?|buttons?|controls?|specs?|available|refund|receipt)\b', predicate, re.I):
        return None
    facets = [f for f, pattern in FIELDS.items() if re.search(pattern, predicate, re.I)]
    if not facets:
        return None
    return {'record_id': hits[0]['record_id'], 'target': hits[0]['text'],
            'source_spans': hits, 'facets': facets, 'predicate': predicate}


def price_scenario(index, question):
    """A sole hypothetical unit-price question, without an extra eligibility if."""
    asked=request(index,question)
    if not asked or asked['facets']!=['amount_thb']:return None
    hits=asked['source_spans']
    if len(hits)!=1:return None
    hit=hits[0];before=question[:hit['start']]
    prefix=re.search(r'(?:ถ้า(?:จะ)?เช่า|หาก(?:จะ)?เช่า|\bif\s+(?:(?:i|we)\s+)?(?:rent|hire))\s*$',before,re.I)
    if prefix is None:return None
    from .understanding import style_only_quote
    framing=before[:prefix.start()]
    framing=re.sub(r'ว่า\s*$','',framing)
    if framing.strip() and not style_only_quote(framing):return None
    tail=question[hit['end']:].strip(' ,?!.')
    if not re.fullmatch(r'(?:ต้อง)?จ่ายกี่บาท|ราคาเท่า(?:ไหร่|ไร)|how much(?: (?:does it cost|is it|would it cost))?',tail,re.I):return None
    return {**asked,'scenario_span':{'start':prefix.start(),'end':hit['end'],'text':question[prefix.start():hit['end']]},'unit_count':1,'permission_or_booking_confirmed':False}
