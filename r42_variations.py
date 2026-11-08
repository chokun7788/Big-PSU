import sys,re
import r41_probe as probe
from pathlib import Path
BASE=Path(__file__).resolve().parent
probe.OUT=Path((BASE/'r42_current_path.txt').read_text(encoding='utf-8'))
oldgrade=probe.grade

def cases():
    rows=[]
    for lang in ('th','en'):
        en=lang=='en';shift='VALORANT controls' if en else 'VALORANT มีปุ่มอะไรบ้าง'
        for topic,query,resume,cat,required in [
            ('schedule','What are the studio opening hours?' if en else 'เวลาเปิดปิดศูนย์คือกี่โมง','please go back to the earlier service hours' if en else 'กลับไปเรื่องเวลาบริการเดิมครับ','schedule',[]),
            ('members','How many member groups are there?' if en else 'สมาชิกมีกี่กลุ่ม','return to the previous members please' if en else 'กลับไปรายชื่อสมาชิกเมื่อกี้ค่ะ','overview',['3 groups'] if en else ['3 หมวด']),
            ('contact','How can I contact the studio?' if en else 'ติดต่อศูนย์ทางไหน','please return to the earlier contact information' if en else 'กลับไปเรื่องข้อมูลติดต่อเดิมครับ','contact',[])]:
            rows.append(dict(id=lang+'-paraphrase-'+topic,locale=lang,turns=[query,shift,resume],kind='equivalent',expected_category=cat,required=required))
        rows.append(dict(id=lang+'-compound-schedule-resume',locale=lang,
            turns=['What are the studio opening hours and what are the Friday opening hours?' if en else 'เวลาเปิดปิดศูนย์คือกี่โมง และ วันศุกร์ศูนย์เปิดกี่โมง',shift,'return to the opening hours' if en else 'กลับไปเรื่องเวลาเปิดปิด'],kind='compound_schedule'))
        rows.append(dict(id=lang+'-partial-controls-resume',locale=lang,
            turns=['Show me the game controls' if en else 'ขอดูปุ่มควบคุมเกม','VALORANT and Minecraft' if en else 'VALORANT กับ มายคราฟต์','PC prices for external users' if en else 'ราคา PC ของบุคคลภายนอก','return to the controls' if en else 'กลับไปเรื่องปุ่มเดิม'],kind='partial',required=['VALORANT','W']))
        rows.append(dict(id=lang+'-mixed-resume-scope',locale=lang,
            turns=['What are the studio opening hours?' if en else 'เวลาเปิดปิดศูนย์คือกี่โมง','How many member groups are there?' if en else 'สมาชิกมีกี่กลุ่ม','back to the opening hours and members' if en else 'กลับไปเรื่องเวลาเปิดปิดกับสมาชิก'],kind='clarification'))
    return rows

def grade(c,rs):
    if c['kind'] not in ('equivalent','compound_schedule'):return oldgrade(c,rs)
    a,b=rs[0]['response'],rs[-1]['response'];contract=b.get('task_contract') or {}
    checks=dict(transport=all(r['status']==200 and r['response'].get('ok') for r in rs),
        context_used=b.get('context_resolution',{}).get('used_context') is True,
        same_answer=a.get('answer')==b.get('answer'),
        required_content=all(x.casefold() in b.get('answer','').casefold() for x in c.get('required',[])))
    if c['kind']=='equivalent':
        checks['category']=a.get('route_category')==b.get('route_category')==c['expected_category']
    else:
        checks['two_children']=len(contract.get('tasks',[]))==2 and len((a.get('task_contract') or {}).get('tasks',[]))==2
        checks['schedule_children']=all(t.get('category')=='schedule' for t in contract.get('tasks',[]))
        checks['all_executed']=contract.get('expected_task_ids')==contract.get('executed_task_ids')
    return dict(id=c['id'],passed=all(checks.values()),checks=checks,mode=b.get('mode'),answer=b.get('answer'),records=rs)

probe.cases=cases;probe.grade=grade
if __name__=='__main__':probe.run(sys.argv[1],sys.argv[2])
