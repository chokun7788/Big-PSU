"""Read every saved label/split/freeze; do not retrain or relabel historical data."""
import json,hashlib,time,collections
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.graph_protocol import messages
S=R.parent/'r129_full_plan_completion_20261024/training_v2';out=R/('saved_training_provenance_'+str(time.time_ns()));out.mkdir()
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(line) for line in p.read_text('utf8').splitlines() if line.strip()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
reviews=rows(S/'ANNOTATION_REVIEW.jsonl');inputs=read(S.parent/'LABELS_REVIEW_INPUT.json');bykey={x['key']:x for x in inputs};datasets={s:rows(S/(s+'.jsonl')) for s in ['train','validation','test']};members={x['key']:(split,x) for split,xs in datasets.items() for x in xs};receipts=[]
for review in reviews:
 key=review['key'];original=bykey[key];entry=members.get(key);issues=[]
 if not review.get('source_version'):issues.append('review_source_version_not_recorded')
 if not review.get('teacher_trace_refs'):issues.append('teacher_trace_refs_not_recorded')
 if not review.get('reviewer') and not review.get('reviewer_id'):issues.append('individual_reviewer_identity_not_recorded')
 if not review.get('adjudication_status'):issues.append('explicit_adjudication_status_not_recorded')
 prompt_equal=None;label_equal=None
 if entry:
  split,row=entry;prompt_equal=row.get('messages',[])[:2]==messages(row['question']);label_equal=row['label']==review['reviewed_label']
  if not prompt_equal:issues.append('saved_training_messages_differ_from_current_inference_messages')
  if not label_equal:issues.append('saved_split_label_differs_from_review_label')
 receipts.append({'key':key,'review_row':review['row'],'question':original['question'],'historical_decision':review['decision'],'split':entry[0] if entry else None,'reviewed_label':review['reviewed_label'],'label_source':original.get('label_source'),'original_family':original.get('family'),'review_family':entry[1].get('review_family') if entry else None,'source_span_receipts':review.get('source_spans',[]),'historical_review_record':{'path':str((S/'ANNOTATION_REVIEW.jsonl').resolve()),'line':review['row']+1,'file_sha256':sha(S/'ANNOTATION_REVIEW.jsonl')},'current_assessment':'review_required' if issues else 'provenance_present_semantic_review_separate','issues':issues,'current_prompt_equal':prompt_equal,'saved_split_label_equals_review':label_equal,'semantic_label_correctness_assessed':False,'historical_training_result_modified':False})
def overlaps(field):
 groups={s:{r.get(field) for r in xs if r.get(field)} for s,xs in datasets.items()}
 return {a+':'+b:sorted(groups[a]&groups[b]) for i,a in enumerate(groups) for b in list(groups)[i+1:]}
freeze=read(S/'DATASET_FREEZE.json');preservation=[{'path':p,'expected_sha256':h,'actual_sha256':sha(Path(p)) if Path(p).is_file() else None} for p,h in freeze.items()]
checks={'every_original_label_has_review_row':len(reviews)==len(inputs)==289 and set(bykey)=={r['key'] for r in reviews},'no_duplicate_review_keys':len({r['key'] for r in reviews})==len(reviews),'no_duplicate_split_keys':len(members)==sum(len(xs) for xs in datasets.values()),'every_accepted_split_label_matches_saved_review':all(r['saved_split_label_equals_review'] is not False for r in receipts),'review_family_never_crosses_splits':not any(overlaps('review_family').values()),'original_family_never_crosses_splits':not any(overlaps('family').values()),'historical_freeze_files_unchanged':all(p['expected_sha256']==p['actual_sha256'] for p in preservation)}
report={'audit_kind':'all_saved_labels_provenance_and_split_integrity_not_semantic_acceptance','checks':checks,'integrity_checks_passed':all(checks.values()),'rows_examined':len(receipts),'historical_decisions':dict(collections.Counter(r['historical_decision'] for r in receipts)),'split_counts':{s:len(v) for s,v in datasets.items()},'issue_counts':dict(collections.Counter(i for r in receipts for i in r['issues'])),'provenance_review_required':sum(r['current_assessment']=='review_required' for r in receipts),'original_family_overlaps':overlaps('family'),'review_family_overlaps':overlaps('review_family'),'freeze_observations':preservation,'fresh_holdout':False,'all_labels_semantically_reviewed_by_this_audit':False,'training_ready':False,'optimizer_started':False,'model_inferences':0,'historical_files_modified':False,'next_work':'Implement fail-closed TrainingExample/ReviewRecord source/teacher/reviewer/adjudication gate; individually review all saved labels against pinned question/context/source. Do not mark generic historical review text semantic proof or reuse mismatched training prompts as current-protocol evidence.'}
(out/'PER_LABEL_AUDIT.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in receipts),'utf8');(out/'REPORT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(out),'rows':report['rows_examined'],'historical_decisions':report['historical_decisions'],'issues':report['issue_counts'],'integrity':checks,'training_ready':False}))
