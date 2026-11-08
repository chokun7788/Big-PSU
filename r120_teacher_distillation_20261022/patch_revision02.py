"""Source-backed corrections after the first completed retained pilot."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';D=S/'app/knowledge/common/domain_flow'
assert all(json.loads((R/n/'TEST_COMPLETE.json').read_text('utf8'))['complete'] for n in ['student01','regression01'])
shutil.copytree(S,R/'revision01_system',ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
changes=[]
def edit(name,old,new):
 p=D/name;s=p.read_text('utf8');assert s.count(old)==1,(name,s.count(old));p.write_text(s.replace(old,new),'utf8');changes.append({'file':name,'before':hashlib.sha256(s.encode()).hexdigest(),'after':hashlib.sha256(p.read_bytes()).hexdigest()})
edit('precision.py',"    role_labels=lambda f:[*f['value'].values(),*(value(index.records[f['record_id']],'role_aliases') or [])]", """    def role_labels(f):
        source=[*f['value'].values(),*(value(index.records[f['record_id']],'role_aliases') or [])]
        # A role may follow a source description such as 'student: Developer'.
        # Use exact source substrings, never names or inferred qualifications.
        headings={'role','position','student','intern','internship','ตำแหน่ง','หน้าที่'}
        parts=[s.strip() for label in source for s in re.split(r'[;:]',label) if len(s.strip())>=4 and norm(s) not in headings]
        return list(dict.fromkeys(source+parts))""")
edit('meaning_review.py',"    elif re.search(r'\\b(?:gpu|cpu|ram)\\b|การ์ดจอ|แรม',q)","""    elif re.search(r'หลายโซน|มากกว่าหนึ่งโซน|multiple zones|more than one zone',q) and re.search(r'เกม|\\bgames?\\b',q) and not competing:
        frame=('games','C04','list','zone');basis='explicit_set_predicate_over_current_game_zone_relations'
    elif re.search(r'\\b(?:gpu|cpu|ram)\\b|การ์ดจอ|แรม',q)""")
edit('engine.py',"        asked=event_years(self.index,question) if category=='C13' else requested_years(question)","""        if category=='C10' and re.search(r'อาหาร|เครื่องดื่ม|\\b(?:food|drinks?|beverages?)\\b',question,re.I) and re.search(r'นำ|เอา.*เข้า|\\bbring\\b',question,re.I):
            # Consumption does not establish permission to bring an item.
            consumption=any(re.search(r'บริโภค|รับประทาน|กิน|\\b(?:consum\\w*|eat\\w*)\\b',' '.join(f['value'].values()),re.I) for f in selected)
            if consumption:
                plan.status='partial';plan.metadata['consumption_not_bring_permission']=True
        asked=event_years(self.index,question) if category=='C13' else requested_years(question)""")
edit('engine.py',"        if category=='C02' and selected:\n            blocks.insert", """        if plan.metadata.get('consumption_not_bring_permission'):
            blocks.insert(0,'ข้อมูลด้านล่างยืนยันเฉพาะการบริโภคในบริเวณที่กำหนด ยังไม่ยืนยันสิทธิ์นำอาหารหรือเครื่องดื่มเข้าศูนย์แยกต่างหาก' if lang=='th' else 'The following source confirms consumption in designated areas. It does not separately confirm permission to bring food or drinks into the studio.')
        if category=='C02' and selected:
            blocks.insert""")
for src,dst,oldout,newout in [('run_student.py','run_student02.py','student01','student02'),('run_regression.py','run_regression02.py','regression01','regression02')]:
 s=(R/src).read_text('utf8').replace("OUT=R/'"+oldout+"'","OUT=R/'"+newout+"'")
 s=s.replace("'run_student.py']","'run_student.py','run_student02.py']") if src=='run_student.py' else s.replace("'run_regression.py']","'run_regression.py','run_regression02.py']")
 (R/dst).write_text(s,'utf8')
(R/'REVISION02_CHANGES.json').write_text(json.dumps({'reason':'Confirmed first-pilot semantic regressions; evaluation cohort is now reused development data','changes':changes,'teacher_examples_unchanged':True,'native_data_unchanged':True},ensure_ascii=False,indent=2),'utf8')
print('Prepared revision02; first pilot outputs retained; no new questions.')
