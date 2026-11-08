import sys,json,sqlite3,zlib,collections
from pathlib import Path
B=Path(__file__).resolve().parent;tag=sys.argv[1];output=B/('PAIRED_BASELINE_'+tag+'.json')
if output.exists():raise FileExistsError(output)
c=sqlite3.connect((B.parent/'r65_detailed_failure_analysis_20261014/evidence.sqlite').as_uri()+'?mode=ro',uri=True)
summary={};samples=[]
for flag,oldarm in [('off','common_offline'),('llm','common_llm')]:
 rows=[json.loads(x) for x in (B/('MATRIX_'+tag+'_'+flag+'.jsonl')).read_text(encoding='utf-8').splitlines()];counts=collections.Counter();locales=collections.defaultdict(collections.Counter)
 for r in rows:
  raw=c.execute('SELECT raw FROM results WHERE arm=? AND key=?',(oldarm,r['key'])).fetchone()
  if raw is None:counts['unpaired']+=1;continue
  old=json.loads(zlib.decompress(raw[0]));counts['paired_requests']+=1
  oldgrades=old.get('grades',[])
  oldby={g.get('file','')+':'+str(g.get('id','')):g for g in oldgrades}
  for i,g in enumerate(r['grades']):
   # R64 and R66 preserve grader order for the frozen original jobs.
   if i>=len(oldgrades):counts['unpaired_grades']+=1;continue
   og=oldgrades[i];loc=locales[r['effective_locale']];counts['paired_grades']+=1;loc['grades']+=1
   for key,passed in [('baseline_strict_pass',og.get('passed',False)),('candidate_strict_pass',g['passed'])]:counts[key]+=bool(passed);loc[key]+=bool(passed)
   if bool(og.get('passed'))!=bool(g['passed']):
    status='strict_repaired' if g['passed'] else 'strict_regressed';counts[status]+=1;samples.append({'arm':flag,'key':r['key'],'question':r['question'],'file':g.get('file'),'change':status,'old_failures':og.get('failures'),'new_failures':g.get('failures'),'old_answer':(old.get('result') or {}).get('answer'),'new_answer':(r.get('result') or {}).get('answer')})
 summary[flag]={'counts':dict(counts),'locales':{k:dict(v) for k,v in locales.items()}}
output.write_text(json.dumps({'scope':'same selected common requests only; no legacy calls','summary':summary,'strict_score_changes':samples},ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(summary,ensure_ascii=False,indent=2))
