"""Source-backed integration corrections; preserve the completed experiment."""
import hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R/'system';S=R/'revision02_system'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
assert not S.exists()
before={str(p.resolve()):sha(p) for p in OLD.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.log'} and not p.name.endswith(('-wal','-shm'))}
shutil.copytree(OLD,S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'));D=S/'app/knowledge/common/domain_flow'
p=D/'understanding.py';x=p.read_text('utf8')
x=x.replace("result=parse(content,question,audience_ids);event['schema_ok']=result.accepted", "result=parse(content,question,audience_ids);event.update(result.event);event['schema_ok']=result.accepted")
x=x.replace("valid,reason=validate(value,question)\n    if not valid:return Understanding(reason='r121_'+reason)\n    return _native_parse(content,question,audience_ids)", """from .source_quote_binding import rebind
    value,repairs=rebind(value,question)
    valid,reason=validate(value,question)
    if not valid:return Understanding(reason='r121_'+reason)
    result=_native_parse(json.dumps(value,ensure_ascii=False),question,audience_ids)
    if repairs:result.event['source_quote_repairs']=repairs
    return result""")
p.write_text(x,'utf8')
p=D/'vocabulary.py';x=p.read_text('utf8')
x=x.replace("r'บุคคลภายนอก|คนนอก.*บริการ|external visitor|general studio services'", "r'บุคคลภายนอก|คนนอก.*บริการ|external visitor|general studio services|(?:ไม่ใช่|ไม่ได้เป็น).{0,18}นักศึกษา.{0,8}(?:psu|มอ).{0,22}(?:เข้า|เล่น|บริการ)|(?:non[- ]psu|not (?:a |an )?psu student).{0,40}(?:use|play|enter|access)'")
old="r'เช็คอิน.*(?:เอกสาร|บัตร)|เช็กอิน.*(?:เอกสาร|บัตร)|แสดงหลักฐาน|check.in.*(?:document|card)|documents.*check.in'"
new="r'เช็คอิน.*(?:เอกสาร|บัตร)|เช็กอิน.*(?:เอกสาร|บัตร)|แสดงหลักฐาน|check.in.*(?:document|card)|documents.*check.in|\\b(?:what|which)\\s+(?:id|identification|documents?)\\b|\\b(?:id|identification|passport|documents?).{0,35}(?:need|bring|show|present)\\b'"
assert old in x;x=x.replace(old,new);p.write_text(x,'utf8')
p=D/'meaning_review.py';x=p.read_text('utf8')
old="if taught_frame is not None:\n        frame=taught_frame;basis='distilled_price_operation_with_current_native_rate_relation'"
new="""if re.search(r'\\b(?:what|which)\\s+(?:id|identification|documents?)\\b|\\b(?:id|identification|passport|documents?).{0,35}(?:need|bring|show|present)\\b',q) and not re.search(r'psu\\s*(?:id|account)|รหัส|บัญชี',q):
        from .readers import policy
        if policy(index,'C08',q) is not None:
            frame=('reservation','C08','detail','owner_policy');basis='identification_documents_requested_before_visitor_eligibility'
    elif taught_frame is not None:
        frame=taught_frame;basis='distilled_price_operation_with_current_native_rate_relation'
    elif index.bind('C04',q) and re.search(r'\\b(?:what|which)\\b.{0,45}\\bbook\\b.{0,20}\\b(?:play|paly)\\b',q) and not competing:
        frame=('games','C04','availability','studio_services');basis='source_bound_game_to_bookable_service_relation'"""
assert old in x;x=x.replace(old,new)
x+='''

_single_need_review=review
def review(question,index,result):
    # Review each explicit need independently; never merge a compound query
    # into one recovered frame. No additional model calls or business answers.
    if not result.accepted or len(result.tasks)<=1:return _single_need_review(question,index,result)
    from .understanding import Understanding
    revised=[];audits=[]
    for task in result.tasks:
        child_event={'raw_content':json.dumps({'tasks':[task.as_dict()]},ensure_ascii=False)}
        child=Understanding([task],True,result.reason,child_event)
        checked=_single_need_review(task.quote,index,child)
        if len(checked.tasks)==1:
            revised.append(checked.tasks[0])
            if checked.event.get('meaning_review'):audits.append(checked.event['meaning_review'])
        else:revised.append(task)
    result.tasks=revised
    if audits:result.event['independent_subtask_reviews']=audits
    return result
'''
p.write_text(x,'utf8')
assert all(sha(Path(p))==h for p,h in before.items())
assert sha(OLD/'data/knowledge/common.sqlite')==sha(S/'data/knowledge/common.sqlite')
(R/'REVISION02_BUILD.json').write_text(json.dumps({'parent_files':before,'parent_unchanged':True,'same_native_database':True,'same_trained_adapter':True,'additional_model_training':False,'changes':['uniquely source-bound case repair','independent review per compound need','identify requested documents before visitor eligibility','recognize non-PSU visitor eligibility paraphrase','game-to-service relation before rental packages'],'evaluation_status':'posthoc development checks required; not fresh held-out accuracy','production_installed':False},ensure_ascii=False,indent=2),'utf8')
print('revision02 built; parent and native database unchanged')
