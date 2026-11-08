import sys,json,re
from pathlib import Path
import r49_probe as old
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r50_current_path.txt').read_text());old.old.p.OUT=OUT
def cases():
 rows=[]
 for locale in ('th','en'):
  en=locale=='en';parking='Is there parking?' if en else 'มีที่จอดรถไหม';mouse='Can I bring my own keyboard?' if en else 'เอาคีย์บอร์ดส่วนตัวมาได้ไหม';games='What games are available in PC?' if en else 'PC มีเกมอะไรบ้าง'
  rows.extend([
   dict(id=locale+'-roster-cs2',locale=locale,turns=['How many members are in a CS2 team?' if en else 'สมาชิกทีม CS2 ต้องมีกี่คน'],expected=['5','Counter-Strike'],kind='rule_answer'),
   dict(id=locale+'-roster-valo-gap',locale=locale,turns=['How many members are in a VALORANT team?' if en else 'สมาชิกทีม VALORANT ต้องมีกี่คน'],expected=[],kind='rule_gap'),
   dict(id=locale+'-team-timeout',locale=locale,turns=['How many timeouts can a VALORANT team request?' if en else 'VALORANT ทีมขอเวลานอกได้กี่ครั้ง'],expected=['2','60'],kind='rule_answer'),
   dict(id=locale+'-resume-parking',locale=locale,turns=[parking,games,'back to parking' if en else 'กลับไปเรื่องที่จอดรถ'],expected=old.old.CONTENT['parking'][en],kind='resume'),
   dict(id=locale+'-resume-mouse',locale=locale,turns=[mouse,games,'return to my keyboard' if en else 'กลับไปเรื่องคีย์บอร์ดส่วนตัว'],expected=old.old.CONTENT['personal_keyboard_mouse'][en],kind='resume'),
   dict(id=locale+'-resume-gap',locale=locale,turns=['back to parking' if en else 'กลับไปเรื่องที่จอดรถ'],expected=[],kind='clarification'),
   dict(id=locale+'-resume-multi',locale=locale,turns=['Is there parking and can I watch my friends?' if en else 'มีที่จอดรถไหม และนั่งดูเพื่อนได้ไหม',games,'back to parking' if en else 'กลับไปเรื่องที่จอดรถ'],expected=[],kind='clarification'),
   dict(id=locale+'-polite-follow',locale=locale,turns=[parking,'What about motorcycles please?' if en else 'แล้วมอไซค์อะครับ'],expected=old.old.CONTENT['parking'][en],kind='follow'),
   dict(id=locale+'-polite-mouse',locale=locale,turns=[mouse,'What about a mouse please?' if en else 'แล้วเม้าส์อ่ะครับ'],expected=old.old.CONTENT['personal_keyboard_mouse'][en],kind='follow'),
   dict(id=locale+'-double-typo',locale=locale,turns=['Can I make one transferr for multiple bookings and replace a wrong payment sllip image?' if en else 'จอองหลายเครืองโอนครังเดียวได้ปะ และแนบสะลิปผิดรูปแก้ยังไง'],expected=old.old.CONTENT['combined_transfer'][en]+old.old.CONTENT['wrong_slip'][en],kind='facts'),
   dict(id=locale+'-different-date-guard',locale=locale,turns=['Is there parking in Bangkok?' if en else 'ที่จอดรถศูนย์ที่กรุงเทพมีไหม'],expected=[],kind='out_of_scope'),
  ])
 return rows
def grade(c,records):
 b=records[-1]['response'];a=b.get('answer','');checks=dict(transport=all(x['status']==200 and x['response'].get('ok') is True for x in records),content=all(x.casefold() in a.casefold() for x in c['expected']),no_timeout=not any(x['response'].get('timed_out') for x in records),english_no_thai=not re.search('[\u0e00-\u0e7f]',a) if c['locale']=='en' else True)
 if c['kind'] in ('follow','resume'):checks['context_used']=bool((b.get('context_resolution') or {}).get('used_context'))
 if c['kind']=='rule_answer':checks['rule_target']=b.get('route_category')=='competition_rules' and 'no_answer' not in b.get('mode','')
 if c['kind']=='rule_gap':checks['explicit_source_gap']='competition' in b.get('mode','') and ('no_answer' in b.get('mode','') or b.get('task_contract',{}).get('outcome')=='no_answer')
 if c['kind']=='clarification':checks['clarify']=b.get('route_category')=='clarification'
 if c['kind']=='out_of_scope':checks['no_phuket_parking']='Building 5' not in a and 'หน้าตึก 5' not in a
 return dict(id=c['id'],passed=all(checks.values()),checks=checks,answer=a,mode=b.get('mode'),records=records)
if __name__=='__main__':old.old.p.cases=cases;old.old.p.grade=grade;old.old.p.run(sys.argv[1],sys.argv[2])
