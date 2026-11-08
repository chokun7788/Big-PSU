import sys,re
from pathlib import Path
import r41_probe as probe
BASE=Path(__file__).resolve().parent;probe.OUT=Path((BASE/'r43_current_path.txt').read_text())
def cases():
 rows=[dict(id='en-week-'+str(i),locale='en',turns=[q],kind='week') for i,q in enumerate([
  'What are the studio opening hours?','When is the studio open?','What is your opening timetable?',
  'Please list opening hours for every day.','What is the service schedule?','What days are available?',
  'What are the opening times?','Give me the complete opening schedule.'])]
 for q,name,kind in [('Monday opening hours','Monday','monday'),('Friday opening hours','Friday','friday'),
  ('Saturday opening hours','Saturday','weekend'),('Sunday opening hours','Sunday','weekend'),
  ('Monday morning opening hours','Monday','maintenance'),('Friday afternoon opening hours','Friday','maintenance')]:
  rows.append(dict(id='en-'+kind+'-'+name,locale='en',turns=[q],kind=kind,name=name))
 rows.append(dict(id='en-regular-date',locale='en',turns=['What are the opening hours on 2026-10-05?'],kind='date'))
 rows.append(dict(id='en-all-week-after-price',locale='en',turns=['PC prices for external users','Please list opening hours for every day.'],kind='week'))
 rows.append(dict(id='en-price-duration-after-price',locale='en',turns=['PC prices for external users','all services 2 hours'],kind='fee_duration'))
 return rows
def grade(c,rs):
 b=rs[-1]['response'];a=b.get('answer','');checks=dict(transport=all(r['status']==200 and r['response'].get('ok') is True for r in rs),
  validated=b.get('validation_ok') is True,not_timeout=b.get('timed_out') is not True,category=b.get('route_category')==('service_fee' if c['kind']=='fee_duration' else 'schedule'))
 if c['kind']=='week':
  checks.update(all_days=all(n+':' in a for n in ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')),
   lunch='12:00-13:00' in a,not_live='not live device availability' in a,closure_override='special closures override' in a)
  for day,must in [('Monday',['09:00-12:00 is maintenance','13:00-16:00 is open']),('Friday',['09:00-12:00 is open','13:00-16:00 is maintenance'])]:
   line=next((s for s in a.splitlines() if day+':' in s),'');checks[day+'_windows']=all(s in line for s in must)
 elif c['kind']=='fee_duration':
  tasks=(b.get('request_plan') or {}).get('tasks',[])
  checks['duration_and_targets']=bool(tasks) and tasks[0]['filters']['duration_minutes']==120 and len(tasks[0]['targets'])==5
  checks['all_services_in_output']=all(n in a for n in ('PC','PlayStation 5','Nintendo Switch','Cockpit','VR'))
 elif c['kind']=='weekend':checks['no_regular_service']='no regular service period' in a and 'Tuesday:' not in a
 elif c['kind']=='maintenance':checks['no_play']='maintenance' in a and 'not a regular play session' in a
 elif c['kind']=='date':checks['date_kept']='05/10/2026' in a and '13:00-16:00 is open' in a
 else:
  checks['day_kept']=c['name']+':' in a;checks['no_other_weekdays']='Tuesday:' not in a
  checks['windows']='09:00-12:00' in a and '13:00-16:00' in a and 'maintenance' in a
 return dict(id=c['id'],passed=all(checks.values()),checks=checks,mode=b.get('mode'),answer=a,records=rs)
probe.cases=cases;probe.grade=grade
if __name__=='__main__':probe.run(sys.argv[1],sys.argv[2])
