"""Transfer teacher answer structure without copying teacher facts."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';D=S/'app/knowledge/common/domain_flow'
assert json.loads((R/'student02/TEST_COMPLETE.json').read_text('utf8'))['complete']
shutil.copytree(S,R/'revision02_system',ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
changes=[]
def edit(name,old,new):
 p=D/name;s=p.read_text('utf8');assert s.count(old)==1,(name,s.count(old));p.write_text(s.replace(old,new),'utf8');changes.append({'file':name,'before':hashlib.sha256(s.encode()).hexdigest(),'after':hashlib.sha256(p.read_bytes()).hexdigest()})
edit('meaning_review.py',"    elif re.search(r'\\b(?:gpu|cpu|ram)\\b|การ์ดจอ|แรม',q)","""    elif re.search(r'คืออะไร|\\bwhat is\\b|\\bwhat are\\b',q) and index.bind('C03',q) and not competing:
        frame=('equipment','C03','detail','usage');basis='source_equipment_definition_before_name_echo'
    elif re.search(r'\\b(?:gpu|cpu|ram)\\b|การ์ดจอ|แรม',q)""")
edit('engine.py',"            blocks.append(f\"{prefix}{f['label'][lang]}: {shown} [S{len(blocks)+1}]\")", """            label=f['label'][lang];citation=f' [S{len(blocks)+1}]'
            if f['facet']=='owner_policy':
                # Teacher-style fact first. Source conditions remain verbatim;
                # technical FAQ/intent identifiers are not customer headings.
                technical=not subject or re.fullmatch(r'[a-z][a-z0-9_.-]+',subject,re.I)
                blocks.append((subject+': ' if not technical else '')+shown+citation)
            elif norm(label)==norm(shown):
                blocks.append(prefix+shown+citation)
            else:blocks.append(f'{prefix}{label}: {shown}'+citation)""")
for src,dst,oldout,newout in [('run_student02.py','run_student03.py','student02','student03'),('run_regression02.py','run_regression03.py','regression02','regression03')]:
 s=(R/src).read_text('utf8').replace("OUT=R/'"+oldout+"'","OUT=R/'"+newout+"'")
 s=s.replace("'run_student02.py']","'run_student02.py','run_student03.py']") if src.startswith('run_student') else s.replace("'run_regression02.py']","'run_regression02.py','run_regression03.py']")
 s=s.replace("candidate':'R120 distilled student'","candidate':'R120 distilled student revision03'").replace("PSU_RUNTIME_PROFILE='r120-student'","PSU_RUNTIME_PROFILE='r120-student-r03'").replace("PSU_RUNTIME_VERSION='R120-distilled-student'","PSU_RUNTIME_VERSION='R120-distilled-student-r03'")
 (R/dst).write_text(s,'utf8')
(R/'REVISION03_CHANGES.json').write_text(json.dumps({'reason':'Teacher-style fact-first response and source-backed equipment definition; no teacher facts transferred','changes':changes,'weights_changed':False,'evaluation_cohort_reused_for_development':True,'native_data_unchanged':True},ensure_ascii=False,indent=2),'utf8')
print('Prepared revision03 answer structure; same retained questions only.')
