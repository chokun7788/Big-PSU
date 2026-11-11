"""Validate recorded play-service intervals without inferring business hours."""
import re


def covers(periods,start,end=None):
    """Contiguous union; an adjacent boundary is not a closure gap."""
    if end is None:return any(a<=start<b for a,b in periods)
    if end<=start:return False
    cursor=start
    for a,b in sorted(periods):
        if b<=cursor:continue
        if a>cursor:return False
        cursor=max(cursor,b)
        if cursor>=end:return True
    return False


def errors(slots,closed=None):
    if slots is None:return []
    if not isinstance(slots,list):return ['service_slots: array required']
    issues=[];ordered=[]
    for slot in slots:
        if not isinstance(slot,dict):issues.append('service_slots: object required');continue
        start,end=slot.get('start'),slot.get('end')
        clock=lambda x:isinstance(x,str) and bool(re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d',x))
        if not clock(start) or not (clock(end) or end=='24:00'):issues.append('service_slots: invalid time');continue
        if start>=end:issues.append('service_slots: inverted interval')
        if slot.get('state') not in {'open','closed','maintenance'}:issues.append('service_slots: unsupported state')
        if closed is True and slot.get('state')=='open':issues.append('service_slots: open interval on declared closed day')
        ordered.append(slot)
    ordered.sort(key=lambda x:x['start'])
    if any(a['end']>b['start'] for a,b in zip(ordered,ordered[1:])):issues.append('service_slots: overlapping intervals')
    return list(dict.fromkeys(issues))
