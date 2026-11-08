"""Calendar arithmetic only. No business opening or occupancy facts."""
import re
from datetime import date,timedelta
from .dialogue_task import normalize_numbers
MONTHS={name:i for i,names in enumerate([('january','jan'),('february','feb'),('march','mar'),('april','apr'),('may',),('june','jun'),('july','jul'),('august','aug'),('september','sep','sept'),('october','oct'),('november','nov'),('december','dec')],1) for name in names}
WEEKDAYS=[('จันทร์','monday'),('อังคาร','tuesday'),('พุธ','wednesday'),('พฤหัสบดี','thursday'),('ศุกร์','friday'),('เสาร์','saturday'),('อาทิตย์','sunday')]
def parse(q,today):
    q=normalize_numbers(q).lower();monthpat='|'.join(sorted(MONTHS,key=len,reverse=True))
    m=re.search(r'\b('+monthpat+r')\.?\s+(\d{1,2})(?:st|nd|rd|th)?(?:,?\s+(20\d{2}|25\d{2}))?\b',q)
    if m:month,day,year=MONTHS[m[1]],int(m[2]),int(m[3]) if m[3] else today.year
    else:
        m=re.search(r'\b(\d{1,2})(?:st|nd|rd|th)?\s+('+monthpat+r')\.?(?:\s+(20\d{2}|25\d{2}))?\b',q)
        if m:day,month,year=int(m[1]),MONTHS[m[2]],int(m[3]) if m[3] else today.year
    if m:
        try:return date(year-543 if year>2400 else year,month,day),'english_month'
        except ValueError:return None,'invalid'
    m=re.search(r'อีก\s*(\d+)\s*วัน|\bin\s+(\d+)\s+days?\b|\b(\d+)\s+days?\s+from\s+(?:now|today)\b',q)
    if m:return today+timedelta(days=int(next(s for s in m.groups() if s is not None))),'relative_day_count'
    for i,names in enumerate(WEEKDAYS):
        if not any(re.search(re.escape(name),q) for name in names):continue
        if not re.search(r'หน้า|\bnext\b|ที่จะถึง|\bthis\b',q):continue
        distance=(i-today.weekday())%7
        if distance==0 and re.search(r'หน้า|\bnext\b',q):distance=7
        return today+timedelta(days=distance),'relative_weekday'
    return None,None
