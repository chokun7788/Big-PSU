import difflib,json,random,time
from pathlib import Path
import harness
random.seed(6313);harness.init('common',False)
from app.knowledge.common import answer
pairs=[]
for label in ['Counter-Strike 2','สวัสดี','Cockpit #01','กฎการแข่งขัน Arena of Valor','Nintendo Switch (1-4 Persons)','นานเปนไคแเสทำอะไรไดเทั่ง']:
 for _ in range(100):
  chars=list(label)
  for i in range(random.randrange(1,5)):
   at=random.randrange(len(chars));op=random.randrange(3)
   if op==0:chars.insert(at,chars[at])
   elif op==1:chars.pop(at)
   else:chars[at]=random.choice('abcdefghijklmnopqrstuvwxyzกขคงาจนมสวดี')
  pairs.append((label,''.join(chars)))
failed=[];start=time.perf_counter()
for a,b in pairs:
 old=difflib.SequenceMatcher(None,a,b).ratio();new=answer.SequenceMatcher(None,a,b).ratio()
 if (old>=.88)!=(new>=.88) or old>=.88 and old!=new:failed.append({'a':a,'b':b,'old':old,'new':new})
r={'pairs':len(pairs),'failed':failed,'threshold':.88,'passing_scores_identical':not failed,'reason':'stdlib quick_ratio upper bound; excluded scores never enter named candidate set','production_code_modified':False,'evaluation_latency_not_production_benchmark':True}
(harness.B/'PRUNING_EQUIVALENCE.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(r,ensure_ascii=False))
