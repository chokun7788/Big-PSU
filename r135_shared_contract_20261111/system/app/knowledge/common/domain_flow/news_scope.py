"""Source event identity and publication applicability, separate from status TTL."""
import re
from .projection import title,value
from .scope import years,reference_time,validity_allows

def candidates(index,question):
    bound=index.bind('C14',question)
    asked=years(question)
    if asked:
        def edition(f):
            r=index.records[f['record_id']]
            return years(' '.join(title(r).values())) or years(str(value(r,'event_start') or ''))
        bound=[f for f in bound if asked<=edition(f)]
    return bound

def status_date_observed(question,at):
    at=reference_time(at)
    dates=re.findall(r'20\d\d-\d\d-\d\d',question)
    return not (any(day!=at.date().isoformat() for day in dates) or re.search(r'พรุ่งนี้|เมื่อวาน|สัปดาห์หน้า|สัปดาห์ก่อน|\b(?:tomorrow|yesterday|next week|last week)\b',question,re.I))

def publication(index,fact,question,at):
    record=index.records[fact['record_id']]
    period=record.get('validity')
    active=validity_allows({'validity':period},reference_time(at))
    historical=bool(re.search(r'historical announcement|archived announcement|old announcement|ประกาศเก่า|ข่าวเก่า|ย้อนหลัง',question,re.I)) and not re.search(r'current|latest|ปัจจุบัน|ล่าสุด',question,re.I)
    ended=False
    if period and period.get('state')=='known' and period.get('effective_until'):
        ended=reference_time(period['effective_until'])<=reference_time(at)
    historical=historical and ended and fact['facet']!='status'
    return {'allowed':active is True or historical or active is None and fact['facet']!='status',
            'state':'historical_publication' if historical else 'current_publication' if active is True else 'publication_period_unconfirmed' if active is None else 'publication_not_effective',
            'record_id':fact['record_id'],'validity':period,'clock':reference_time(at).isoformat()}
