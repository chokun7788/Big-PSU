"""Bound the independent review to the requested action and local task scope."""
import ast,hashlib,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R/'revision02_system';S=R/'revision03_system'
assert json.loads((R/'guard01/TEST_COMPLETE.json').read_text('utf8'))['complete']
assert not S.exists()
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
freeze=json.loads((R/'guard01/RUN_FREEZE.json').read_text('utf8'));assert all(sha(Path(p))==h for p,h in freeze.items())
shutil.copytree(OLD,S,ignore=shutil.ignore_patterns('__pycache__','*.pyc','*.log','*-wal','*-shm'));D=S/'app/knowledge/common/domain_flow'
p=D/'meaning_review.py';x=p.read_text('utf8')
old="elif re.search(r'คืออะไร|\\bwhat is\\b|\\bwhat are\\b',q) and index.bind('C03',q) and not competing:"
new="elif re.search(r'คืออะไร|\\bwhat is\\b|\\bwhat are\\b',q) and index.bind('C03',q) and not competing and not re.search(r'ปุ่ม|\\b(?:buttons?|controls?)\\b',q):"
assert old in x;x=x.replace(old,new)
x=x.replace("and not re.search(r'psu\\s*(?:id|account)|รหัส|บัญชี',q):", "and re.search(r'\\b(?:visitor|studio|check.in|arrival|service)\\b',q) and not re.search(r'(?:psu|steam|riot|discord|game|account|api)\\s*(?:id|identifier|account)|รหัส|บัญชี',q):")
old="for task in result.tasks:\n        child_event="
new="""for task in result.tasks:
        # A source-quoted target can still belong to a DIFFERENT need. Keep
        # cross-need targets only with an explicit anaphoric relation.
        if task.target and task.target not in task.quote and not re.search(r'\\b(?:it|its|same|that|those)\\b|เดียวกัน|เครื่องนั้น|เกมนั้น',task.quote,re.I):
            audits.append({'basis':'unrelated_cross_task_target_removed','source_target':task.target,'task_quote':task.quote,'business_facts_added':False})
            task.target=''
        child_event="""
assert old in x;x=x.replace(old,new);ast.parse(x);p.write_text(x,'utf8')
p=D/'vocabulary.py';x=p.read_text('utf8')
x=x.replace("r'เช็คอิน.*(?:เอกสาร|บัตร)|เช็กอิน.*(?:เอกสาร|บัตร)|แสดงหลักฐาน|check.in.*(?:document|card)|documents.*check.in|\\b(?:what|which)\\s+(?:id|identification|documents?)\\b|\\b(?:id|identification|passport|documents?).{0,35}(?:need|bring|show|present)\\b'", "r'เช็คอิน.*(?:เอกสาร|บัตร)|เช็กอิน.*(?:เอกสาร|บัตร)|แสดงหลักฐาน|check.in.*(?:document|card)|documents.*check.in|\\b(?:what|which)\\s+(?:id|identification|documents?)\\b(?=.{0,120}\\b(?:studio|visitor|check.in|arrival|service)\\b)|\\b(?:id|identification|passport|documents?).{0,35}(?:need|bring|show|present)\\b(?=.{0,120}\\b(?:studio|visitor|check.in|arrival|service)\\b)'")
ast.parse(x);p.write_text(x,'utf8')
assert all(sha(Path(p))==h for p,h in freeze.items())
assert sha(OLD/'data/knowledge/common.sqlite')==sha(S/'data/knowledge/common.sqlite')
(R/'REVISION03_BUILD.json').write_text(json.dumps({'parent_run_frozen_files_unchanged':True,'same_database':True,'same_adapter':True,'new_training':False,'changes':['explicit controls before broad what-is equipment definition','remove cross-task targets without explicit anaphora','scope identification-document recovery to studio/check-in context'],'fresh_heldout_accuracy_claim':False,'production_installed':False},indent=2),'utf8')
print('revision03 built; no frozen parent, facts or adapter changed')
