"""Explicit requested output and controller constraints, without guessed facts."""
import re
from .projection import value

def device(index,question):
    from .named_spans import masked
    q=masked(index,question)
    pad=bool(re.search(r'จอย|เกมแพด|\b(?:controller|gamepad)\b',q,re.I))
    keys=bool(re.search(r'คีย์บอร์ด|เมาส์|\b(?:keyboard|mouse)\b',q,re.I))
    return 'ambiguous' if pad and keys else 'controller' if pad else 'keyboard' if keys else None

def allows(index,question,fact):
    requested=device(index,question)
    if requested is None:return True
    if requested=='ambiguous':return False
    source=value(index.records.get(fact['record_id'],{}),'input_device')
    if not isinstance(source,str):return False
    return bool(re.search(r'จอย|เกมแพด|controller|gamepad',source,re.I)) if requested=='controller' else bool(re.search(r'keyboard|mouse|คีย์บอร์ด|เมาส์',source,re.I))
