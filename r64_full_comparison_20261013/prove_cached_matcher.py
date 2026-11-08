import ast,difflib,json,random
import harness
harness.init('common',False)
from app.knowledge.common import answer as module
source=(harness.STAGE/'app/knowledge/common/answer.py').read_text(encoding='utf-8')
tree=ast.parse(source);function=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='named')
scope=dict(module.__dict__);scope['SequenceMatcher']=difflib.SequenceMatcher
exec(compile(ast.Module(body=[function],type_ignores=[]),'<original named>','exec'),scope)
names={'a':['Arena of Valor (RoV)','Arena of Valor','RoV'],'b':['Counter-Strike 2','CS2'],'c':['Cockpit #01','Cockpit'],'d':['สวัสดี'],'e':['Nintendo Switch (1-4 Persons)'],'f':['VALORANT','วาโล'],'g':['PC #02']}
queries=['For Arena of Valor, can you verify the rule on competition format?','กฎตอนแข่ง cs2 มีอะไรมั่ง','cockpik ว่างไหม','สวัาดี','PC #03 controls','Nintendo Switch (1-4 Persons) ราคา']
random.seed(644)
for alias in [s for aliases in names.values() for s in aliases]:
 for _ in range(15):
  q=list(alias);i=random.randrange(len(q));q[i]=random.choice('abcdefghijklmnopqrstuvwxyzกขคงาดีส');queries.append(''.join(q)+' controls')
failed=[]
for q in queries:
 old=scope['named'](q,names);new=module.named(q,names)
 if old!=new:failed.append({'query':q,'old':old,'new':new})
report={'queries':len(queries),'failed':failed,'exact_candidate_and_method_equivalence':not failed,'reason':'reuse SequenceMatcher seq2; .88 upper-bound pruning; same loops and numeric protections','production_files_changed':False}
(harness.B/'CACHED_MATCHER_EQUIVALENCE.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(report,ensure_ascii=False))
