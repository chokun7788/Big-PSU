import sys
import r41_probe as probe
from pathlib import Path
BASE=Path(__file__).resolve().parent;probe.OUT=Path((BASE/'r42_current_path.txt').read_text(encoding='utf-8'))
def cases():
    rows=[]
    for lang in ('th','en'):
        en=lang=='en'
        for topic,q,mode,content in [
            ('minimum','How far ahead must I book?' if en else 'ต้องจองล่วงหน้ากี่วัน',None,'1 hour' if en else '1 ชั่วโมง'),
            ('cancellation','How many days in advance can I cancel my booking?' if en else 'ต้องยกเลิกจองล่วงหน้ากี่วัน',None,'1 hour' if en else '1 ชั่วโมง'),
            ('maximum-days','How many days ahead can I book?' if en else 'จองล่วงหน้าได้สูงสุดกี่วัน','booking_maximum_lead_unconfirmed',None),
            ('maximum-devices','What is the maximum number of devices I can book?' if en else 'จองได้สูงสุดกี่เครื่อง','booking_maximum_resources_unconfirmed',None),
            ('maximum-sessions','How many sessions can I book?' if en else 'จองได้สูงสุดกี่ session',None,'3'),
            ('payment','How many minutes do I have to pay after booking?' if en else 'หลังจองต้องจ่ายภายในกี่นาที',None,'10'),
            ('checkin','How early can I check in?' if en else 'เช็คอินล่วงหน้าได้กี่นาที',None,'30')]:
            rows.append(dict(id=lang+'-policy-'+topic,locale=lang,turns=[q],topic=topic,expected_mode=mode,required=content))
    return rows
def grade(c,rs):
    b=rs[-1]['response'];contract=b.get('task_contract') or {}
    checks=dict(transport=rs[-1]['status']==200 and b.get('ok') is True,category=b.get('route_category')=='reservation',
        not_weekly_window='protected_booking_window' not in b.get('mode',''))
    if c['expected_mode']:
        checks['specific_gap']=c['expected_mode'] in b.get('mode','');checks['missing_outcome']=contract.get('status')=='missing'
    else:
        checks['quantity']=c['required'].casefold() in b.get('answer','').casefold()
        checks['not_general_steps']=b.get('route_intent')!='booking_steps'
        if c['topic']=='maximum-sessions':checks['session_unit']='session' in b.get('answer','').casefold()
        if c['topic']=='payment':checks['payment_clause']='pay' in b.get('answer','').casefold() if c['locale']=='en' else ('ชำระ' in b.get('answer','') or 'จ่าย' in b.get('answer',''))
        if c['topic']=='checkin':checks['checkin_clause']='check' in b.get('answer','').casefold() if c['locale']=='en' else ('เช็คอิน' in b.get('answer','') or 'เช็กอิน' in b.get('answer',''))
    return dict(id=c['id'],passed=all(checks.values()),checks=checks,mode=b.get('mode'),answer=b.get('answer'),records=rs)
probe.cases=cases;probe.grade=grade
if __name__=='__main__':probe.run(sys.argv[1],sys.argv[2])
