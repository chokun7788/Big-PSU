"""Separate v3 cohort: preserve prior reviews, individually readmit row191."""
import argparse,copy,json,time
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import *
from app.knowledge.common.domain_flow import graph_protocol_v3 as v3
W=R/'training_review_workbench_1793037663397671000'
parser=argparse.ArgumentParser();parser.add_argument('--round',default='review_round_012');args=parser.parse_args()
S=(W/args.round).resolve();assert S.parent==W.resolve() and S.name.startswith('review_round_')
O=W/('protocol_v3_admission_'+str(time.time_ns()));O.mkdir()
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(x) for x in p.read_text('utf8').splitlines() if x.strip()]
def write(name,value):
 p=O/name;p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in value) if name.endswith('.jsonl') else json.dumps(value,ensure_ascii=False,indent=2)+'\n','utf8');return p
def ref(p,**kw):return {'path':str(p.resolve()),'sha256':file_sha(p),**kw}
source_ref=read(W/'SOURCE_REF.json');source=read(W/'SOURCE_SNAPSHOT.json');identity=digest(source_identity(source))
examples=rows(S/'EXAMPLES.jsonl');prior_reviews=rows(S/'REVIEWS.jsonl');prior={r['question_key']:(i,r) for i,r in enumerate(prior_reviews,1)};reviews=[];migration_count=0
pinned={str(p):file_sha(p) for p in [S/'EXAMPLES.jsonl',S/'REVIEWS.jsonl',W/'review_round_010/ADJUDICATION_191.json']}
tokenizer=Path('D:/CodexTraining/psu-r121-20261022/model/tokenizer_config.json');runtime=runtime_contract(read(tokenizer),chat_template=tokenizer.with_name('chat_template.jinja').read_text('utf8'),model_profile=read(W/'DECLARED_MODEL_PROFILE.json'),wire_version=v3.VERSION);write('RUNTIME_CONTRACT.json',runtime)
for line,original in enumerate(examples,1):
 x=copy.deepcopy(original);x['contract_version']=v3.VERSION;x['plan_label']['version']=v3.VERSION
 saved_split=Path(original['annotation_provenance']['origin_ref']['path']).stem
 x['split']='train' if saved_split=='train' else 'development'
 x['annotation_provenance']['runtime_contract_sha256']=digest(runtime)
 row=x['annotation_provenance']['historical_review_ref']['line']-1
 old=prior.get(x['question_key'])
 if old and old[1]['adjudication_status']=='quarantined' and row not in {191,267}:
  # A protocol version cannot decide an unresolved user predicate. Preserve
  # the original proposal and its actual individual quarantine byte-for-byte
  # as excluded forensic material, including the original v2 wire and packing.
  examples[line-1]=copy.deepcopy(original);reviews.append(copy.deepcopy(old[1]));continue
 if row in {191,267} and old and old[1]['adjudication_status']=='quarantined':
  assert x['raw_question']==({191:'Please tell me: What time is the afternoon session',267:'Please answer from verified studio information: Please tell me: When can I play on Monday afternoon'}[row])
  q=x['raw_question'];x['plan_label']={'version':v3.VERSION,'focus':'service_periods','context_quotes':[],
   'tasks':[{'id':'t1','quote':q,'domain':'schedule','operation':'list','facet':'service_periods','target':'',
             'constraints':[{'slot':'time','quote':'afternoon','source_record_id':'','scope':'local'}],'ambiguous':False}],
   'shared_bindings':[]}
  if row==267:x['plan_label']['tasks'][0]['constraints'].insert(0,{'slot':'date','quote':'Monday','source_record_id':'','scope':'local'})
  assert v3.parse(json.dumps(x['plan_label']),q).accepted
  who={'id':'Codex-primary-agent-R135-source-adjudication','kind':'agent'}
  ids=['migrated_schedule_'+str(day) for day in (range(7) if row==191 else [0])]
  reasons=[
   'One named afternoon play-session time need; Please tell me is style. No booking operation or live occupancy is requested.',
   'Explicit v3 schedule/list/service_periods represents the recorded play-period source field. Friday afternoon maintenance exists while its booking window is absent, so bookable_periods was a different semantic target.',
   'afternoon is the exact local period/time quote. No person, amount, service identifier, weekday, date, clock or authority is invented.',
   'No history or weekday/date is supplied. The native source executor retains every recorded weekday and its applicability caveats; no fictional date or broadcast binding enters the target.',
   'There is no negation or contradictory period in the raw request. Unknown source validity and weekday states are source limitations, not linguistic ambiguity.',
   'Pinned seven migrated_schedule records distinguish service_slots from physical opening and bookable fields; actual v3/native source execution binds current record revisions and preserves Friday maintenance and empty weekend schedules.',
   'Target contains language operations and raw afternoon quote only. No13:00/16:00 clock, weekday answer, maintenance verdict, booking guarantee or business permission is taught.']
  if row==267:reasons=[
   'One question asks when play is possible on Monday afternoon; repeated verified/polite introductions are framing, not separate tasks.',
   'Explicit v3 schedule/list/service_periods represents play-service timing. open_periods asks physical opening and bookable_periods asks reservation windows, so neither is an equivalent v2 substitute.',
   'Monday and afternoon are exact local date/time quotes. No clock times, calendar date, service identifier or live state is invented.',
   'The question supplies a weekday but no specific date or dialogue history. Both constraints belong to this one task; no shared context or fictional history is added.',
   'There is no negation or competing period. Unknown owner applicability and dated exceptions remain source limitations, not permission to assert current play access.',
   'Individually read migrated_schedule_0 revision4 has morning maintenance, afternoon open service_slots, a distinct afternoon bookable window and unknown physical open_periods. This explicitly supports the service-period facet distinction, not a present-day access guarantee.',
   'The target contains only raw Monday/afternoon quotes and the language operation. It teaches no13:00/16:00 answer, permission, maintenance verdict, booking result or authority assertion.']
  issues=[{'scope':'answer_source','reason':'Service-period effective intervals/resource applicability and physical opening conflicts remain independent source limitations.','handling':'Keep per-day states, source revision/field and applicability caveats; do not infer live availability, physical access or booking windows.'}]
  evidence={'question_key':x['question_key'],'example_sha256':example_sha(x),'adjudication_status':'corrected','reviewer':who,'source_identity_sha256':identity,
   'criteria':{k:{'status':'passed','reason':reason,'raw_quotes':[q],'source_record_ids':ids if k=='source_version_alignment' else []} for k,reason in zip(CRITERIA,reasons)},
   'unresolved_issues':issues,'historical_review_row':row,'prior_label':original['plan_label'],'reviewed_label':x['plan_label'],
   'prior_quarantined_review_ref':ref(S/'REVIEWS.jsonl',line=old[0]),'source_field_evidence':{rid:{'revision':source['release']['records'][rid]['revision'],'record_sha256':digest(source['release']['records'][rid])} for rid in ids},
   'review_scope':'Individual v3 language-target readmission only; no actual model learning or business-answer acceptance.'}
  p=write('V3_ADJUDICATION_'+str(row)+'.json',evidence)
  reviews.append({'version':VERSION,'question_key':x['question_key'],'example_sha256':example_sha(x),'adjudication_status':'corrected','reviewer':who,'review_method':'individual_source_adjudication','source_version':source_ref,'adjudication_ref':ref(p),'teacher_status':'not_applicable','teacher_trace_refs':[],'unresolved_issues':issues})
 elif old and old[1]['adjudication_status'] in {'accepted','corrected'}:
  record={'kind':'structural_wire_version_migration','from_version':WIRE_VERSION,'to_version':v3.VERSION,
          'original_example_ref':ref(S/'EXAMPLES.jsonl',line=line),'original_review_ref':ref(S/'REVIEWS.jsonl',line=old[0]),
          'original_example_sha256':example_sha(original),'migrated_example_sha256':example_sha(x)}
  p=write('MIGRATION_'+str(row).zfill(3)+'.json',record);x['annotation_provenance']['wire_migration_ref']=ref(p)
  reviews.append(copy.deepcopy(old[1]));migration_count+=1
 # Unreviewed proposals are inventoried, never promoted by a version change.
 x['messages']=v3.messages(x['raw_question'])+[{'role':'assistant','content':json.dumps(x['plan_label'],ensure_ascii=False,separators=(',',':'))}]
 examples[line-1]=x
write('EXAMPLES.jsonl',examples);write('REVIEWS.jsonl',reviews)
inventory=read(W/'INVENTORY.json');report=prepare_dataset(O/'bundle',examples,reviews,Artifacts(R.parent),source_ref,runtime,expected_keys=inventory['question_keys'],known_exposed=inventory['known_exposed_question_keys'])
eligible=sum(d['eligible'] for d in report['rows']);readmissions=sum(1 for row in [191,267] if (O/('V3_ADJUDICATION_'+str(row)+'.json')).exists());quarantined_rows=sorted(x['annotation_provenance']['historical_review_ref']['line']-1 for x in examples if next((r for r in reviews if r['question_key']==x['question_key']),{}).get('adjudication_status')=='quarantined')
assert eligible==migration_count+readmissions and len(reviews)==len(prior_reviews) and sum(d.get('adjudication_status')=='quarantined' and d['inventory_adjudicated'] and not d['eligible'] for d in report['rows'])==len(quarantined_rows),[d for d in report['rows'] if d.get('adjudication_status') and not d['inventory_adjudicated']]
assert all(file_sha(Path(p))==h for p,h in pinned.items())
summary={'wire_version':v3.VERSION,'manual_round':S.name,'all_original_keys':len(examples),'unique_original_questions_individually_reviewed':len(prior_reviews),'existing_individual_reviews_reused_after_version_only_proof':migration_count,'new_protocol_specific_individual_readmissions':readmissions,'eligible':eligible,'quarantined':len(quarantined_rows),'quarantined_original_rows':quarantined_rows,'unreviewed':len(examples)-len(prior_reviews),'eligible_split_counts':report['eligible_split_counts'],'training_ready':report['ready_for_optimization'],'source_identity_sha256':identity,'runtime_contract_sha256':digest(runtime),'old_v2_files_unchanged':True,'old_v2_row191_still_quarantined':True,'other_original_quarantine_proposals_and_reviews_unchanged':True,'actual_model_generation_or_optimization':False,'new_semantic_reviews_claimed_for_version_only_migrations':False,'gateway_default_wire_changed':False,'complete':False}
write('SUMMARY.json',summary);print(json.dumps({'output':str(O),**summary}))
