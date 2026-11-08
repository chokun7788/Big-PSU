"""Bind explicit static-fact dates without changing the live observation clock."""
import re
from datetime import datetime,time,timedelta
from zoneinfo import ZoneInfo
def scope(question,at,records,names):
    from .answer import named
    from .query_contract import strip_names
    ids,_=named(question,names,allow_fuzzy=False);text=strip_names(question,ids,names)
    iso=re.search(r'(?<!\d)(20\d{2})-(\d{1,2})-(\d{1,2})(?!\d)',text)
    slash=re.search(r'(?<!\d)(\d{1,2})/(\d{1,2})/((?:20|25)\d{2})(?!\d)',text)
    if not iso and not slash:return None
    try:
        if iso:y,m,d=map(int,iso.groups())
        else:d,m,y=map(int,slash.groups());y=y-543 if y>=2500 else y
        day=datetime(y,m,d,tzinfo=ZoneInfo('Asia/Bangkok'))
        clock=re.findall(r'(?<!\d)([01]?\d|2[0-3]):([0-5]\d)(?!\d)',text)
        explicit=len(clock)==1
        target=day.replace(hour=int(clock[0][0]),minute=int(clock[0][1])) if explicit else day.replace(hour=12)
        return {'target':target,'day_start':day,'day_end':day+timedelta(days=1),'explicit_time':explicit,'source_span':(iso or slash).group()}
    except ValueError:return {'invalid':True}
