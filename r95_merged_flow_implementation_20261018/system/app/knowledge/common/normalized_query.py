"""Shared discourse normalization with an auditable mapping to original input."""
from dataclasses import dataclass, asdict
import re, unicodedata
from difflib import SequenceMatcher
from app.core.typo_similarity import osa_distance

@dataclass
class NormalizedQuery:
    raw: str
    text: str
    offsets: list
    edits: list
    protected: list

    def public(self):
        return asdict(self)

def normalize_query(raw):
    raw = str(raw)
    text = unicodedata.normalize('NFC', raw).casefold()
    offsets = [0] * len(text)
    for tag, a, b, c, d in SequenceMatcher(None, raw, text).get_opcodes():
        for i in range(c, d): offsets[i] = min(a + i-c, max(a, b-1))
    edits = []
    def sub(pattern, replacement, reason, flags=0):
        nonlocal text, offsets
        matches = list(re.finditer(pattern, text, flags))
        for m in reversed(matches):
            start = offsets[m.start()] if m.start() < len(offsets) else len(raw)
            end = offsets[m.end()-1]+1 if m.end() else start
            rep = replacement(m) if callable(replacement) else replacement
            if rep == m.group(): continue
            edits.append({'reason':reason,'raw_start':start,'raw_end':end,'observed':m.group(),'replacement':rep})
            text = text[:m.start()] + rep + text[m.end():]
            offsets = offsets[:m.start()] + [start]*len(rep) + offsets[m.end():]
    sub('เเ', 'แ', 'thai_vowel_composition')
    sub(r'\s+', ' ', 'whitespace')
    # Framing is removed only at the edges, not when it qualifies a request.
    prefixes = [
        r'^\s*(?:i (?:am |was )?planning (?:a |my )?visit and (?:i )?(?:would like|want) to know|please answer from verified studio information)\s*[:：]\s*',
        r'^\s*(?:(?:could|can|would) you (?:please )?help me (?:with this|understand this)|(?:i would|i.d) like to (?:ask|know))\s*[:：]\s*',
        r'^\s*(?:ช่วยตอบจากข้อมูลที่ยืนยันได้(?:หน่อย)?|ขอสอบถาม(?:หน่อย)?(?:ครับ|ค่ะ)?|สอบถาม(?:หน่อย)?(?:ครับ|ค่ะ)?)\s*[:：]?\s*',
    ]
    for _ in range(3):
        before = text
        for pattern in prefixes: sub(pattern, '', 'discourse_prefix')
        if before == text: break
    colon=text.find(':')
    if 15<=colon<=90:
        prefix=text[:colon].strip()
        for target in ('please answer from verified studio information','i am planning a visit and would like to know'):
            if osa_distance(prefix,target)==1:
                sub('^'+re.escape(text[:colon+1])+r'\s*','','bounded_discourse_prefix_edit')
                break
    # A bounded typo in a long polite prefix must not poison an exact entity.
    for prefix in ('ขอสอบถามหน่อยครับ', 'ขอสอบถามหน่อยค่ะ', 'ขอสอบถามหน่อย'):
        observed = text[:len(prefix)]
        if len(observed) == len(prefix) and observed != prefix and osa_distance(observed, prefix) == 1:
            sub('^'+re.escape(observed), '', 'bounded_polite_prefix_edit')
            break
    for pattern in [r'\s*[?.!,]*\s*(?:could you check this for me|please use verified information|please answer using verified information)\s*[?.!,]*\s*$']:
        sub(pattern, '', 'discourse_suffix')
    sub(r'^\s+|\s+$', '', 'edge_whitespace')
    protected = []
    for m in re.finditer(r'\d+(?:[:./-]\d+)*|ไม่|ห้าม|ยกเว้น|เฉพาะ|ก่อน|หลัง|\b(?:not|no|never|except|unless|only|before|after|without)\b', raw, re.I):
        protected.append({'text':m.group(),'start':m.start(),'end':m.end()})
    return NormalizedQuery(raw, text or raw, offsets if text else list(range(len(raw))), edits, protected)
