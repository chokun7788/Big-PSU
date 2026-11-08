"""Stage reviewed family moves on an amended v3 cohort; not optimizer authorization."""
import argparse,json,time
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import Artifacts,prepare_dataset,file_sha,digest
from app.knowledge.common.domain_flow.semantic_family_plan import apply_reviewed_family_moves
W=R/'training_review_workbench_1793037663397671000'
a=argparse.ArgumentParser();a.add_argument('cohort');args=a.parse_args();S=(W/args.cohort).resolve();assert S.parent==W.resolve() and S.name.startswith('protocol_v3_admission_')
read=lambda p:json.loads(p.read_text(encoding='utf8'));rows=lambda p:[json.loads(s) for s in p.read_text(encoding='utf8').splitlines() if s.strip()]
summary=read(S/'SUMMARY.json');assert summary['manual_round'].startswith('review_round_014_candidate_')
files=[S/'EXAMPLES.jsonl',S/'REVIEWS.jsonl',S/'RUNTIME_CONTRACT.json',S/'SUMMARY.json']
family=[W/'semantic_amendments_round014'/n for n in ['FAMILY_PSU_PRICE_BOOKING_104_133_134_135.json','FAMILY_EN_PRICE_BOOKING_141_282.json','FAMILY_BOOKING_DAYS_137_280.json']];files+=family
pins={str(p):file_sha(p) for p in files}; refs=[{'path':str(p.resolve()),'sha256':file_sha(p)} for p in family]
art=Artifacts(R.parent);examples=rows(files[0]);reviews=rows(files[1]);planned,moves=apply_reviewed_family_moves(examples,refs,art)
assert len(moves)==5 and len({x['question_key'] for x in moves})==5
bykey={m['question_key']:m for m in moves}
for x in planned:
 if x['question_key'] in bykey:x['annotation_provenance']['semantic_family_move_ref']=bykey[x['question_key']]['family_review_ref']
O=W/('family_cohort_candidate_'+str(time.time_ns()));O.mkdir()
for n,v in [('EXAMPLES.jsonl',planned),('REVIEWS.jsonl',reviews)]: (O/n).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in v),encoding='utf8')
runtime=read(files[2]);source=read(W/'SOURCE_REF.json');inventory=read(W/'INVENTORY.json')
report=prepare_dataset(O/'bundle',planned,reviews,art,source,runtime,expected_keys=inventory['question_keys'],known_exposed=inventory['known_exposed_question_keys'])
assert all(file_sha(Path(p))==h for p,h in pins.items())
eligible=sum(x['eligible'] for x in report['rows']);expected=summary['eligible'];assert eligible==expected,(eligible,expected,[x for x in report['rows'] if not x['eligible'] and x.get('adjudication_status')!='quarantined'])
result={'input_cohort':str(S),'input_sha256':pins,'moves':moves,'eligible':eligible,'eligible_split_counts':report['eligible_split_counts'],'dataset_gate_ready':report['ready_for_optimization'],'dataset_gate_is_optimizer_authorization':False,'family_audit_complete':False,'metrics_and_model_evaluation_complete':False,'optimizer_started':False,'old_artifacts_unchanged':True}
(O/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps({'path':str(O),**result},ensure_ascii=False))
