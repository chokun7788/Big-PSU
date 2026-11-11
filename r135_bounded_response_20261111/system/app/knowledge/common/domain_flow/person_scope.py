"""Public recorded personnel profiles; a past role is not a current role."""
import re
from datetime import datetime,timedelta
from .projection import value
from .scope import reference_time,requested_years,validity_allows


def check(record,question,at,period_only=False):
    public=record.get('fields',{}).get('public_scope',{})
    if public.get('status')!='known' or re.search(r'private|internal|not public|ภายใน|ห้ามเผยแพร่',str(value(record,'public_scope') or ''),re.I):return {'allowed':False,'reason':'person_public_scope_not_confirmed'}
    valid=record.get('validity') or {};date_match=re.search(r'20\d\d-\d\d-\d\d',question);years=requested_years(question)
    if date_match:
        try:
            day=datetime.fromisoformat(date_match[0]).replace(tzinfo=at.tzinfo);intervals=[(day,day+timedelta(days=1))]
        except ValueError:return {'allowed':False,'reason':'invalid_profile_date'}
    elif years:intervals=[(at.replace(year=y,month=1,day=1,hour=0,minute=0,second=0,microsecond=0),at.replace(year=y+1,month=1,day=1,hour=0,minute=0,second=0,microsecond=0)) for y in sorted(years)]
    else:intervals=[]
    if valid.get('state')=='known':
        start=reference_time(valid['effective_from']) if valid.get('effective_from') else None;end=reference_time(valid['effective_until']) if valid.get('effective_until') else None
        if intervals:
            if not any((end is None or a<end) and (start is None or start<b) for a,b in intervals):return {'allowed':False,'reason':'profile_not_effective_for_requested_period'}
        elif not period_only and validity_allows(record,at) is False:return {'allowed':False,'reason':'profile_not_current'}
        return {'allowed':True,'state':'recorded_effective_interval','validity':valid,'requested_intervals':[(a.isoformat(),b.isoformat()) for a,b in intervals],'requested_interval_fully_covered':all((start is None or start<=a) and (end is None or b<=end) for a,b in intervals),'current_role_claimed':not intervals and not period_only}
    return {'allowed':True,'state':'effective_period_unknown','validity':valid,'current_role_claimed':False}
