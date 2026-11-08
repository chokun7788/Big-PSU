import json,sys,copy
from pathlib import Path
B=Path(__file__).resolve().parent;S=B.parent/'r78_web_session_check_20261016/system';sys.path.insert(0,str(S))
import app.knowledge.common as pkg
pkg.__path__.insert(0,str(B/'candidate/app/knowledge/common'))
from app.knowledge.common.open_day import status_question,classify
checks=[]
def check(n,v):checks.append({'case':n,'passed':bool(v)})
for q in ['วันนี้เปิดกี่โมง','วันนี้เปิดไหมแล้วปิดกี่โมง','วันนี้ตอน 10:00 เปิดไหม','ตอนนี้เปิดไหม','Is the studio open right now?','วันนี้เปิดไหมถ้าฝนตก','วันนี้ PC เปิดไหม','วันนี้เปิดไหมและมีเกมอะไรบ้าง','Is the studio open today and what are the prices?','วันหยุดราชการเปิดไหม']:
 check('No day-status shortcut: '+q,not status_question(q))
def field(s,v):return {'status':s,'value':v}
def record(op,bp,state=None):return {'fields':{'open_periods':op,'bookable_periods':bp,'state':field('known' if state else 'unknown',state)}}
periods=[{'start':'09:00','end':'12:00'}]
check('No booking slots alone cannot prove closed',classify(record(field('unknown',None),field('known',[])))[0] is None)
check('Known empty opening periods prove closed',classify(record(field('known',[]),field('known',[])))[0]=='closed')
check('Positive service period supports day opening without guessing exact hours',classify(record(field('conflicted',None),field('known',periods)))[0]=='open')
check('Closed state and positive periods are a conflict',classify(record(field('unknown',None),field('known',periods),'closed'))[0] is None)
check('No service periods means unresolved opening conflict stays unknown',classify(record(field('conflicted',None),field('known',[])))[0] is None)
r={'count':len(checks),'passed':sum(x['passed'] for x in checks),'checks':checks}
with (B/'STATUS_GUARDS.json').open('x',encoding='utf8') as f:json.dump(r,f,ensure_ascii=False,indent=2)
print(json.dumps(r,ensure_ascii=False));raise SystemExit(any(not x['passed'] for x in checks))
