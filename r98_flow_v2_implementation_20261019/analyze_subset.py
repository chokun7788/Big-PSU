"""Same retained R95 questions/checker, separated literal/protocol/transport metrics."""
from pathlib import Path
import collections,gzip,hashlib,json,statistics,sys
R=Path(__file__).resolve().parent;B=R.parent/'r95_merged_flow_implementation_20261018'
tag=sys.argv[1] if len(sys.argv)>1 else 'subset01';freeze=sys.argv[2] if len(sys.argv)>2 else 'final_on01'
def rows(folder):
 for path in folder.glob('RESULTS_*.jsonl.gz'):
  with gzip.open(path,'rt',encoding='utf8') as f:
   for line in f:yield json.loads(line)
current={r['key']:r for r in rows(R/tag)};old={r['key']:r for r in rows(B/'full01') if r['key'] in current}
def metric(data):
 counts=collections.Counter();partitions=collections.Counter();locales=collections.defaultdict(collections.Counter)
 for r in data.values():
  counts['requests']+=1;counts['exceptions']+=bool(r.get('exception'));counts['empty_answers']+=not bool(r.get('result',{}).get('answer'))
  for c in r.get('observed_model_http_calls',[]):counts['model_http_attempts']+=1;counts['model_response_opened']+=bool(c.get('transport_ok'))
  for g in r['grades']:
   counts['grades']+=1;counts['strict_passed']+=bool(g['passed'])
   for key,vals in g.get('partitions',{}).items():partitions[key]+=len(vals)
   if g.get('positive_text_contract'):
    failed=bool(g.get('partitions',{}).get('content'));counts['positive_grades']+=1;counts['positive_literal_passed']+=not failed
    locales[r['requested_locale']]['positive_grades']+=1;locales[r['requested_locale']]['positive_literal_passed']+=not failed
 return {'totals':dict(counts),'failure_partitions':dict(partitions),'locale':{k:dict(v) for k,v in locales.items()}}
def gp(r):return {(g['file'],g['row'],g['variant']):g for g in r.get('grades',[])}
changes=[]
for key,r in current.items():
 if key not in old:continue
 before=gp(old[key]);after=gp(r);improved=[];regressed=[]
 for gkey,g in after.items():
  b=before.get(gkey)
  if b and g.get('positive_text_contract'):
   bfail=bool(b.get('partitions',{}).get('content'));afail=bool(g.get('partitions',{}).get('content'))
   if bfail and not afail:improved.append(gkey)
   if afail and not bfail:regressed.append(gkey)
 if improved or regressed:changes.append({'key':key,'question':r['question'],'locale':r['requested_locale'],'improved_positive_grades':improved,'regressed_positive_grades':regressed,'old_answer':old[key]['result'].get('answer'),'new_answer':r['result'].get('answer'),'new_artifact':r['result'].get('decision_artifact')})
source=json.loads((R/freeze/'SOURCE_BEFORE.json').read_text('utf8'))
changed=[p for p,h in source.items() if not (R/'system'/p).is_file() or hashlib.sha256((R/'system'/p).read_bytes()).hexdigest()!=h]
report={'requests_expected':len((R/'FOCUSED_JOBS.jsonl').read_text('utf8').splitlines()),'current_requests':len(current),'retained_matched_requests':len(old),'source_unchanged_from_focused_freeze':not changed,'changed_source_paths':changed,'r95_retained':metric(old),'r98_candidate':metric(current),'changes':changes,'limits':['Development subset selected by domain/locale; not a full-corpus accuracy estimate.','Literal/clause mismatch requires content review; strict scores also include protocol requirements.','R95 was retained, not rerun; model transport can differ.','Booking is controlled unavailable; live availability correctness is not tested.']}
(R/tag/'COMPARISON.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps({k:v for k,v in report.items() if k!='changes'},ensure_ascii=False))
