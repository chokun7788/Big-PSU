"""Bind critical qualifications before semantic execution, without erasing them."""
import re
from datetime import datetime
from .registry import value,aware

def requirements(need,records,targets):
    q=need.query.casefold();missing=[];checks=[]
    def require(condition,reason):
        checks.append({'requirement':reason,'satisfied':bool(condition)})
        if not condition:missing.append(reason)
    if re.search(r'\b(?:children|kids|minor|child)\b|เด็ก|ผู้เยาว์',q):
        require(need.task not in {'game_overview','game_how_to_play','game_players','game_platforms'} or all(value(records[k],'age_rating') is not None for k in need.record_ids if records[k]['kind']=='game'),'age_eligibility_source')
    if re.search(r'\b(?:latest|newest)\b|ล่าสุด',q):
        require(need.task in {'game_version','news'} and all(value(records[k],'game_version') is not None for k in targets),'latest_version_applicability')
    if re.search(r'\b(?:not|without|unless|except|before|after|only)\b|ยกเว้น|เฉพาะ|ห้าม|ไม่ได้|โดยไม่',q):
        require(need.task in {'policy','procedure','faq_content','price','rental','competition_rules','schedule','live_status'},'conditional_task_scope')
    year=re.search(r'(?:\b(?:in|for|during)\b|ในปี|ปี)\s*(20\d{2}|25\d{2})(?!\d)',q)
    if year:
        y=int(year[1]);y=y-543 if y>=2500 else y
        from app.calendar.service_calendar import now_bangkok
        if y!=now_bangkok().year:
            a=datetime.fromisoformat(f'{y}-01-01T00:00:00+07:00');b=datetime.fromisoformat(f'{y+1}-01-01T00:00:00+07:00')
            require(all(records[k]['validity']['state']=='known' and records[k]['validity'].get('effective_from') and aware(records[k]['validity']['effective_from'])<=a and (not records[k]['validity'].get('effective_until') or aware(records[k]['validity']['effective_until'])>=b) for k in targets),'requested_year_applicability')
    if re.search(r'\d+\s*(?:บาท|baht|thb|ชั่วโมง|hours?|minutes?|นาที)',q):
        require(need.task in {'price','rental','service_duration','schedule','live_status'},'quantity_units_task')
    return {'satisfied':not missing,'missing':missing,'checks':checks}
