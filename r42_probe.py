import sys,json,re
from pathlib import Path
import r41_probe as probe
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r42_current_path.txt').read_text(encoding='utf-8'))
probe.OUT=OUT
def cases():
    rows=[]
    for lang in ('th','en'):
        en=lang=='en';shift='VALORANT controls' if en else 'VALORANT มีปุ่มอะไรบ้าง'
        for topic,initial,resume,category in [
            ('schedule','What are the studio opening hours?' if en else 'เวลาเปิดปิดศูนย์คือกี่โมง','back to the opening hours' if en else 'กลับไปเรื่องเวลาเปิดปิด','schedule'),
            ('booking','How many days ahead can I book?' if en else 'จองล่วงหน้าได้กี่วัน','back to the booking process' if en else 'กลับไปเรื่องวิธีจอง','reservation'),
            ('members','How many member groups are there?' if en else 'สมาชิกมีกี่กลุ่ม','back to the member list' if en else 'กลับไปเรื่องรายชื่อสมาชิก','overview'),
            ('equipment','What equipment is available in PC?' if en else 'PC มีอุปกรณ์อะไรบ้าง','back to the equipment' if en else 'กลับไปเรื่องอุปกรณ์','equipment'),
            ('details','What is Beat Saber?' if en else 'Beat Saber คืออะไร','back to the game details' if en else 'กลับไปเรื่องรายละเอียดเกม','games'),
            ('contact','How can I contact the studio?' if en else 'ติดต่อศูนย์ทางไหน','back to the contact details' if en else 'กลับไปเรื่องช่องทางติดต่อ','contact')]:
            rows.append(dict(id=lang+'-resume-'+topic,locale=lang,turns=[initial,shift,resume],kind='resume_equivalent',expected_category=category))
        rows.append(dict(id=lang+'-new-schedule-condition',locale=lang,turns=['What are the studio opening hours?' if en else 'เวลาเปิดปิดศูนย์คือกี่โมง',shift,'back to the opening hours tomorrow' if en else 'กลับไปเรื่องเวลาเปิดปิดของพรุ่งนี้'],kind='clarification'))
        rows.append(dict(id=lang+'-resume-members-no-history',locale=lang,turns=['back to the member list' if en else 'กลับไปเรื่องรายชื่อสมาชิก'],kind='clarification'))
    return rows

def grade(case,records):
    if case['kind']!='resume_equivalent':return oldgrade(case,records)
    first,last=records[0]['response'],records[-1]['response']
    checks={'transport':all(r['status']==200 and r['response'].get('ok') for r in records),
        'initial_category':first.get('route_category')==case['expected_category'],
        'retained_category':last.get('route_category')==first.get('route_category'),
        'retained_operation':last.get('route_intent')==first.get('route_intent'),
        'retained_answer':last.get('answer')==first.get('answer'),
        'context_used':last.get('context_resolution',{}).get('used_context') is True,
        'target_oracle_has_answer':bool(first.get('answer')) and 'no_answer' not in first.get('mode','')}
    if case['id'].endswith('booking'):
        checks['maximum_lead_gap']='booking_maximum_lead_unconfirmed' in first.get('mode','') and 'booking_maximum_lead_unconfirmed' in last.get('mode','')
    if case['id'].endswith('members'):
        checks['group_count_not_headcount']=bool(re.search(r'3\s+groups|3\s+หมวด',first.get('answer',''),re.I)) and bool(re.search(r'3\s+groups|3\s+หมวด',last.get('answer',''),re.I))
    return dict(id=case['id'],passed=all(checks.values()),checks=checks,mode=last.get('mode'),answer=last.get('answer'),records=records)
oldgrade=probe.grade;probe.cases=cases;probe.grade=grade
if __name__=='__main__':probe.run(sys.argv[1],sys.argv[2])
