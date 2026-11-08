"""Individual post-migration field review of the18 existing C11 questions."""
import json,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import digest,source_identity,file_sha
W=R/'training_review_workbench_1793037663397671000';A=sorted(W.glob('protocol_v3_admission_*'))[-1]
def read(p):return json.loads(p.read_text('utf8'))
xs=[json.loads(x) for x in (A/'EXAMPLES.jsonl').read_text('utf8').splitlines()];reviews={json.loads(x)['question_key'] for x in (A/'REVIEWS.jsonl').read_text('utf8').splitlines()}
# Expectations/reasons are individual human-language judgments written after
# reading these questions and the pinned calendar fields, not auto labels.
notes={
2:('bookable_periods','availability','The literal question asks whether booking is possible during maintenance. A booking predicate is distinct from asking maintenance dates or play-session start/end times.'),
7:('open_periods','availability','Friday-afternoon closed-state confirmation asks broad opening, not the named-session timetable. Physical opening conflict and known play maintenance must stay source-qualified.'),
15:('open_periods','detail','Will the studio be open tomorrow is a broad future opening request; visit planning is framing. No named play period, booking window or vacancy is requested.'),
32:('maintenance_periods','list','Maintenance คือช่วงไหน requests the recorded maintenance-period set without a weekday. It is not the full named play-session timetable or an opening guarantee.'),
34:('open_periods','detail','Tuesday studio-opening time is explicit. Preserve the typo/framing and weekday while keeping physical/source-play scope distinct at execution.'),
41:('maintenance_periods','detail','Friday maintenance information requests maintenance scope, not booking or a universal session time. The stated weekday is local.'),
52:('open_periods','availability','Is the studio open now requests current opening state. It does not ask which machines are vacant; the source clock and opening-field conflict remain reader obligations.'),
55:('open_periods','availability','Monday morning open-or-closed is a state question rather than a named-session start/end request. Maintenance alone cannot prove physical building closure.'),
66:('open_periods','availability','Friday afternoon open asks the broad opening predicate. Preserve weekday/period and disclose physical-opening status separately from recorded play maintenance.'),
68:('open_periods','availability','Open on Sundays is a recurring weekday-opening question, not a booking or live-occupancy predicate. Recorded empty periods/currentness remain source-qualified.'),
137:('bookable_periods','detail','How to book VR supplies booking context for what days are available. The second need retains regular bookable-day scope and shared VR, without asserting current machine vacancies.'),
158:('open_periods','availability','Today open asks broad dated opening state. No session name or booking-window predicate is supplied; source and date applicability must not be invented.'),
159:('closing_time','detail','ปิดกี่โมง asks closing time. No day is supplied, so source/date clarification or a qualified recorded schedule remains necessary; do not relabel it as booking or a named play session.'),
174:('open_periods','availability','Will the studio be opem tomorrow retains the literal typo and tomorrow scope. Meaning is an opening-state request, not a named play-period time.'),
182:('open_periods','detail','The wording explicitly asks Wednesday opening hours. Verified-information framing does not make conflicted physical hours known or turn them into service periods.'),
184:('bookable_periods','list','เปิดจองวันไหนและช่วงเวลาไหน explicitly requests the complete recorded booking-day/time tuples. A named play-period facet would lose its booking predicate.'),
191:('service_periods','list','What time is the afternoon session explicitly requests a named play-service period without a booking predicate. Friday afternoon maintenance versus absent booking window is the source counterexample requiring a new v3 semantic label.'),
197:('open_periods','detail','Monday opening time remains the broad opening facet. No session word or booking predicate appears; its source-field conflict cannot be normalized away.')}
observed={x['annotation_provenance']['historical_review_ref']['line']-1:x for x in xs if x['question_key'] in reviews and any(t['domain']=='schedule' for t in x['plan_label']['tasks'])};assert set(observed)==set(notes)
source=read(W/'SOURCE_SNAPSHOT.json');records=[]
for i,(facet,operation,reason) in notes.items():
 x=observed[i];tasks=[t for t in x['plan_label']['tasks'] if t['domain']=='schedule'];assert len(tasks)==1 and (tasks[0]['facet'],tasks[0]['operation'])==(facet,operation)
 records.append({'original_row':i,'question_key':x['question_key'],'raw_question':x['raw_question'],'schedule_task':tasks[0],'reason':reason,'label_changed_by_this_audit':False,'source_business_answer_accuracy_claimed':False})
result={'reviewed_at':time.time(),'cohort':str(A.relative_to(R)),'cohort_examples_sha256':file_sha(A/'EXAMPLES.jsonl'),'source_identity_sha256':digest(source_identity(source)),
 'review_scope':'Current18 C11 language labels against the explicit service-period/booking/opening/maintenance/closing distinction. No new training labels or205-question review-count inflation.',
 'records':records,'new_semantic_review_records_created':0,'only_new_v3_semantic_correction_already_recorded':191,
 'source_caveats':['Physical opening conflicts and effective interval/resource scope remain source obligations.','Booking-context available days do not establish live vacancy.','No native/source execution or parser pass proves a model learned v3.'],
 'all_C11_language_semantics_for_arbitrary_questions_verified':False,'actual_model_generation_or_optimization':False,'complete':False}
p=R/('C11_V3_FACET_REAUDIT_'+str(time.time_ns())+'.json');p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(p),'existing_C11_questions_read':len(records),'new_unique_question_reviews':0,'label_changes':0}))
