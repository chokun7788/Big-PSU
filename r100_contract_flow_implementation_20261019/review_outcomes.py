"""Inspect changed outcome checks separately from literal/content checks."""
import gzip,json
from pathlib import Path
R=Path(__file__).resolve().parent
def load(folder):
 out={}
 for p in folder.glob('RESULTS_*.jsonl.gz'):
  with gzip.open(p,'rt',encoding='utf8') as f:
   for l in f:
    r=json.loads(l);out[r['key']]=r
 return out
old=load(R.parent/'r98_flow_v2_implementation_20261019/subset02');new=load(R/'subset05');changes=[]
for key,row in new.items():
 before={(g['file'],g['row'],g['variant']):g for g in old[key]['grades']}
 for g in row['grades']:
  b=before[(g['file'],g['row'],g['variant'])];bf=b.get('partitions',{}).get('outcome',[]);nf=g.get('partitions',{}).get('outcome',[])
  if bf!=nf:changes.append({'question':row['question'],'locale':row['requested_locale'],'grade_id':g.get('id'),'before':bf,'after':nf,'old_mode':old[key]['result']['mode'],'new_mode':row['result']['mode'],'new_answer':row['result']['answer']})
(R/'subset05/OUTCOME_CHANGES.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),'utf8')
for r in changes:print(json.dumps({k:v for k,v in r.items() if k!='new_answer'},ensure_ascii=False))
