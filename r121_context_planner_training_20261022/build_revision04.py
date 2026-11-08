"""Fix two observed reader failures without inventing permission or subsets."""
import ast,hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R/'revision03_system';S=R/'revision04_system'
assert json.loads((R/'priority01/TEST_COMPLETE.json').read_text('utf8'))['complete'];assert not S.exists()
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
frozen=json.loads((R/'priority01/RUN_FREEZE.json').read_text('utf8'));assert all(sha(Path(p))==h for p,h in frozen.items())
shutil.copytree(OLD,S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'));D=S/'app/knowledge/common/domain_flow'
p=D/'vocabulary.py';x=p.read_text('utf8')
x+="\n# Match a requested consumption action, never add a new business permission.\nPOLICY_INTENTS.append(('food_consumption','C10',r'อาหาร.*เครื่องดื่ม|food.*drinks?',r'(?:อาหาร|เครื่องดื่ม).{0,30}(?:กิน|รับประทาน|บริโภค)|(?:กิน|รับประทาน|บริโภค).{0,20}(?:อาหาร|เครื่องดื่ม)|(?:can|may|must).{0,20}(?:eat|drink)|(?:eat|eating).{0,25}(?:area|desk|designated)'))\n"
ast.parse(x);p.write_text(x,'utf8')
p=D/'readers.py';x=p.read_text('utf8');needle="for intent,domain,source_pattern,question_pattern in POLICY_INTENTS:\n        if domain==cat"
replacement="""for intent,domain,source_pattern,question_pattern in POLICY_INTENTS:
        if intent=='food_consumption' and matches(r'นำ.*เข้า|ถือ.*เข้า|เอา.*เข้า|\\bbring\\b|ไม่ได้ถาม|ไม่ใช่ถาม|not.{0,15}ask',q):continue
        if domain==cat"""
assert needle in x;x=x.replace(needle,replacement);ast.parse(x);p.write_text(x,'utf8')
p=D/'meaning_reader.py';x=p.read_text('utf8')
needle="return confirmed(cat,pool,'complete_source_binding_set',complete_set=True,member_count=len(pool),operator='list')"
replacement="""result=confirmed(cat,pool,'complete_source_binding_set',complete_set=True,member_count=len(pool),operator='list')
            requested=re.search(r'\\b(?:the|all)\\s+(\\d+)\\s+buttons?\\b|(?:จำนวน|ทั้งหมด|ขอ)\\s*(\\d+)\\s*ปุ่ม',question,re.I)
            if requested:
                count=int(next(s for s in requested.groups() if s is not None))
                if count!=len(pool):
                    result.status='partial';result.reason='requested_control_subset_not_identified'
                    result.metadata['requested_binding_count']=count;result.metadata['recorded_binding_entries']=len(pool)
                    result.metadata['complete_set']=False
            return result"""
assert needle in x;x=x.replace(needle,replacement);ast.parse(x);p.write_text(x,'utf8')
p=D/'engine.py';x=p.read_text('utf8');needle="if plan.metadata.get('unanswered_buttons'):"
replacement="""if plan.metadata.get('requested_binding_count') is not None:
            wanted=plan.metadata['requested_binding_count'];recorded=plan.metadata['recorded_binding_entries']
            blocks.insert(0,(f'แหล่งข้อมูลมี {recorded} รายการควบคุม แต่ยังไม่ระบุว่าชุด {wanted} ปุ่มที่ถามคือรายการใด ด้านล่างเป็นรายการที่ยืนยันได้ โปรดระบุกลุ่มปุ่มที่ต้องการ' if lang=='th' else f'The source records {recorded} control entries but does not identify the requested subset of {wanted} buttons. Known entries are listed below; please specify the button group.'))
        if plan.metadata.get('unanswered_buttons'):"""
assert needle in x;x=x.replace(needle,replacement);ast.parse(x);p.write_text(x,'utf8')
assert all(sha(Path(p))==h for p,h in frozen.items());assert sha(OLD/'data/knowledge/common.sqlite')==sha(S/'data/knowledge/common.sqlite')
(R/'REVISION04_BUILD.json').write_text(json.dumps({'parent_frozen_files_unchanged':True,'same_database':True,'same_adapter':True,'changes':['consumption question maps to existing consumption policy','bring/negated-topic queries excluded from consumption recovery','explicit requested control-entry subset differs from recorded entries -> partial and clarification'],'new_business_answers':False,'production_installed':False,'fresh_heldout_accuracy_claim':False},indent=2),'utf8')
print('revision04 built; permission, source data and adapter unchanged')
