"""Read-only source discovery through public Common; no model or HTTP."""
import argparse,json,os,sqlite3,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.answer import CommonAnswerer
parser=argparse.ArgumentParser();parser.add_argument('--rows',nargs='+',type=int,default=[155,158,160,164,168,171,173,174]);parser.add_argument('--locale',choices=['th','en','auto']);parser.add_argument('--resume',help='Existing discovery directory; reuse only its isolated source copy and skip saved rows.');args=parser.parse_args()
O=(R/args.resume).resolve() if args.resume else R/('saved_clause_discovery_'+str(time.time_ns()))
if args.resume:
 assert O.parent==R.resolve() and O.name.startswith('saved_clause_discovery_') and (O/'source_copy.sqlite').is_file()
else:
 O.mkdir();source=(R/'system/data/knowledge/common.sqlite').resolve();s=sqlite3.connect(source.as_uri()+'?mode=ro',uri=True);d=sqlite3.connect(O/'source_copy.sqlite');s.backup(d);d.close();s.close()
os.environ['PSU_CONVERSATION_STATE_PATH']=str(O/'isolated_conversation.sqlite');view=DraftSnapshotView(CommonStore(O/'source_copy.sqlite'))
W=R/'training_review_workbench_1793037663397671000';examples=[json.loads(x) for x in (W/'review_round_008/EXAMPLES.jsonl').read_text('utf8').splitlines()];lookup={x['annotation_provenance']['historical_review_ref']['line']-1:x for x in examples};details=json.loads((O/'DETAILS.json').read_text('utf8')) if args.resume else [];summaries=json.loads((O/'SUMMARY.json').read_text('utf8')) if args.resume else []
assert len({d['row'] for d in details})==len(details)
for i in args.rows:
 if any(d['row']==i for d in details):continue
 q=lookup[i]['raw_question'];locale=args.locale or ('en' if i in [155,171,174] else 'th')
 with patch('urllib.request.urlopen',side_effect=AssertionError('actual HTTP forbidden in source discovery')):
  r=CommonAnswerer(view).answer(q,locale=locale,at='2026-10-27T10:00:00+07:00',planner=None)
 a=r.decision_artifact if r is not None else {};answer=r.answer if r is not None else None;c=a.get('execution_contract',{});tasks=c.get('request_plan',{}).get('tasks',[]);summary={'row':i,'question':q,'answer':answer,'source_dispatch_returned_none':r is None,'tasks':[{'category':t.get('category'),'quote':t.get('source_span',{}).get('text'),'operation':t.get('operation'),'field':t.get('field'),'ambiguities':t.get('ambiguities')} for t in tasks],'execution_contract_keys':list(c)}
 details.append({'row':i,'question':q,'answer':answer,'artifact':a,'source_dispatch_returned_none':r is None});summaries.append(summary)
 (O/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n','utf8');(O/'SUMMARY.json').write_text(json.dumps(summaries,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps({'output':str(O),'summary':summaries,'actual_HTTP_or_model_calls':0,'original_source_modified':False,'discovery_only_no_acceptance_claim':True},ensure_ascii=False))
