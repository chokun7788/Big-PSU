"""Called LAST by checkpoint_protocol_v3_admission; bounded scope, no closure."""
import hashlib,json,time
from pathlib import Path
from verification_support import R

def read(p):return json.loads(p.read_text('utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n','utf8')
def report(prefix):
 p=sorted(R.glob(prefix+'*/RESULT.json'))[-1];d=read(p);assert d['all_passed'] and all(d['checks'].values()),p
 return {'path':str(p.relative_to(R)),'sha256':sha(p),'checks':len(d['checks']),'passed':True},d
reports={};docs={}
for key,prefix in [('named_package','named_package_scope_'),('payment_predicate','payment_predicate_scope_'),('policy_topic','policy_topic_scope_'),('rental_validity','rental_validity_scope_')]:reports[key],docs[key]=report(prefix)
assert reports['named_package']['checks']>=68 and reports['payment_predicate']['checks']>=16 and reports['policy_topic']['checks']>=17
W=R/'training_review_workbench_1793037663397671000';manual=W/'review_round_012';m=read(manual/'SUMMARY.json');assert (m['individually_adjudicated'],m['accepted'],m['corrected_or_enriched'],m['quarantined'],m['unreviewed'])==(225,65,158,2,64)
base=R/'saved_clause_discovery_1793098997110641700/DETAILS.json';before={d['row']:d for d in read(base)}
completed=[p for p in sorted(R.glob('saved_clause_discovery_*/DETAILS.json')) if {d['row'] for d in read(p)}==set(range(205,225))]
current=completed[-1];assert current!=base;after={d['row']:d for d in read(current)}
audit=R/('ROUND012_SOURCE_SCOPE_REAUDIT_'+str(time.time_ns())+'.json')
records=[]
for row in range(205,225):
 b,a=before[row],after[row];assert b['question']==a['question'];c=a['artifact']['execution_contract'];tasks=c['request_plan']['tasks'];claims=[z for ex in c['executor_results'] for z in ex.get('claims',[])]
 if 208<=row<=219:assert len(tasks)==1 and tasks[0]['category']=='C07' and tasks[0]['operation']!='bounded_compatibility' and bool(claims) and all(z['record_id'].startswith('package_') for z in claims)
 if row==206:assert a['artifact']['response_type']=='clarification' and not claims
 if row in {220,221}:assert len(tasks)==1 and tasks[0]['category']=='C09' and bool(claims)
 if row==210:assert all(r['status']=='structurally_supported' for r in c['verifier_result']['constraint_coverage']['constraints'])
 records.append({'original_row':row,'question':a['question'],'baseline_answer':b['answer'],'candidate_answer':a['answer'],'task_categories':[t['category'] for t in tasks],'claim_source_fields':[(z['record_id'],z['facet']) for z in claims],'manual_adjudication':str((manual/('ADJUDICATION_'+str(row)+'.json')).relative_to(R)),'scope':'Actual native/source answer and label-purpose check; no new unique semantic review or model inference.'})
write(audit,{'baseline':{'path':str(base.relative_to(R)),'sha256':sha(base)},'candidate':{'path':str(current.relative_to(R)),'sha256':sha(current)},'records':records,'controls':reports,'unique_original_reviews':225,'new_unique_reviews_from_this_reaudit':0,'row206_still_quarantined_for_training':True,'actual_model_inferences':0,'whole_flow_complete':False,
 'source_read_notes':{'package_scope':'Organization package audience/full-half day, room seats, duration and included equipment are separate source dimensions. Included all equipment does not prove current full inventory or live capacity.','underpayment':'r114_q015 and actual selected r130_owner_42_scoped both ask underpayment; current source question explicitly says โอนขาด. The typed action matcher now recognizes that actual source actor/purpose. No top-up deadline is established.','documents':'Receipt/quotation/tax-invoice source distinctions and prior-answer version wording remain intact. ราคา inside ใบเสนอราคา is a noun component.','fragment':'Original206 remains unresolved and quarantined in v2/v3; native response requests the missing predicate without supplying an artificial training label.','remaining':'Source policy validity, rental terms/currentness and permission applicability remain separate; bounded source checks do not close model, category, API or installation acceptance.'},
 'test_harness_corrections':'Preserve initial failed reports: the mixed-locale sibling expected English despite Thai auto locale; synthetic source providers reused an epoch or compared mutable whole snapshots and produced retry rather than a valid negative source control. Final controls use real isolated owner writes. The owner writer legitimately refreshes attestation, so authorized edits are positive controls; an independent un-attested snapshot mutation is the negative control. The English seat predicate and embedded platform slots were real candidate gaps and were repaired.'})
specs=[('G119',['C07','FLOW-13','CONTRACT-03','FLOW-17'],'Actual named rental-package questions208-219 gained unrequested C03 inventory/count or C06 per-session price tasks; some package fields fell through bounded compatibility. Native context also inferred a platform from inside an opaque package name. A sole hypothetical package price was treated as an unverified generic condition.','named_package','package_intent.py;financial.py;native_intents.py;readers.py;context_guard.py;request_verifier.py;integration.py'),
 ('G120',['C09','FLOW-13','CONTRACT-03'],'Document availability220 acquired a C06 price obligation from ราคา inside ใบเสนอราคา. Underpayment proof221 took an untyped shortcut; forcing the typed path exposed a real actor/source matcher gap for the attested โอนขาด source heading.','payment_predicate','payment_intent.py;vocabulary.py;native_intents.py;request_verifier.py;integration.py'),
 ('G121',['C10','FLOW-13','CONTRACT-03'],'Original206 drinks/area fragment was rendered as a definite consumption-policy query despite its individually unresolved predicate. Source topic overlap cannot establish whether carrying, consuming or a facility was requested.','policy_topic','policy_scope.py;native_intents.py;engine.py;integration.py;request_verifier.py'),
 ('G122',['C07','CONTRACT-10'],'Re-audit found all selected retained rental packages have unknown effective intervals, but delivery displayed their values as complete answers without disclosing that current applicability was unconfirmed. The missing disclosure/partial state was an implementation gap; unknown owner intervals themselves remain source unknowns and were not fabricated.','rental_validity','engine.py:finish_plan/render')]
gapdoc=read(R/'AUDIT_GAPS.json')
for ident,requirements,finding,key,code in specs:
 entry={'id':ident,'requirements':requirements,'finding':finding,'state':'implemented_component_verification_final_audit_pending','candidate_code':code,'baseline':str(base.relative_to(R)),'source_reaudit':{'path':audit.name,'sha256':sha(audit)},'evidence':reports[key],'remaining':'Arbitrary predicates/conditions/contexts, source currentness, actual model/paired/category/freeze/API/normal activation/final re-audit remain. Original requirements are not finally closed.'}
 gapdoc['gaps']=[g for g in gapdoc['gaps'] if g['id']!=ident]+[entry]
gapdoc.update(complete=False,last_recorded_at=time.time());write(R/'AUDIT_GAPS.json',gapdoc)
criteria={
 'C07':('A full current package name owns its requested source field rather than zone inventory or ordinary play rates.','named_package',['row208_one_local_package_field','row210_only_exact_source_package_claim','row213_independent_observer_no_inventory_or_session_rate','row216_name_component_not_independent_platform_or_service','actual_owner_package_field_edit_changes_answer','unknown_package_seats_not_replaced_with_zone_or_device_capacity','new_owner_package_name_needs_no_training']),
 'C09':('Document nouns and underpayment proof preserve payment purpose, source actor and actual attestation.','payment_predicate',['quotation_noun_does_not_invent_price_obligation','actual_scoped_source_question_actor_alignment','underpayment_proof_has_typed_task_and_receipts','real_document_and_fee_siblings_both_preserved','actual_owner_edit_changes_source_answer_without_training','unattested_answer_mutation_cannot_be_certified','withdrawn_document_source_does_not_restore_constants']),
 'C10':('A drinks/area fragment requests missing-predicate clarification without inferring a business policy from source keywords.','policy_topic',['fragment0_clarifies_without_business_claims','fragment0_observer_does_not_certify_consumption_predicate','explicit_carrying_still_source_bound','owner_source_answer_edit_does_not_determine_fragment_intent','missing_policy_sources_do_not_manufacture_intent']),
 'FLOW-13':('Named package, document and topical-fragment task boundaries retain their local predicate instead of embedded entity/noun words.','named_package',['real_package_and_equipment_siblings_both_preserved','ordinary_play_fee_stays_C06','real_zone_inventory_stays_C03','row213_name_component_not_independent_platform_or_service']),
 'FLOW-17':('A sole hypothetical named-package unit-price scenario requires independently recomputed amount, revision, source and clock; extra eligibility/quantity conditions remain unverified.','named_package',['sole_hypothetical_package_price_scenario_recomputed','scenario_forged_amount_not_verified','scenario_forged_record_not_verified','scenario_forged_revision_not_verified','scenario_forged_clock_not_verified','scenario_forged_no_receipt_not_verified'])}
for p in R.glob('*_REQUIREMENT_REVIEWS.json'):
 doc=read(p);changed=False
 for row in doc['requirements']:
  if row['requirement_id'] not in criteria:continue
  title,key,checks=criteria[row['requirement_id']];assert all(docs[key]['checks'][k] for k in checks)
  row['criteria']=[c for c in row['criteria'] if c.get('iteration')!='round012_source_scope']+[{'criterion':title,'state':'passed_controlled_acceptance','evidence':reports[key]['path'],'evidence_sha256':reports[key]['sha256'],'checks':checks,'iteration':'round012_source_scope','semantic_accuracy_claimed':False}];row['final_revision_api_and_installation_reaudit_pending']=True;changed=True
  if row['requirement_id']=='C07':
   cs=list(docs['rental_validity']['checks']);assert all(docs['rental_validity']['checks'].values())
   row['criteria']=[c for c in row['criteria'] if c.get('iteration')!='round012_rental_currentness']+[{'criterion':'Recorded rental values disclose an unknown effective interval as partial; actual known-current, expired and future source intervals are tested without inventing owner facts.','state':'passed_controlled_acceptance','evidence':reports['rental_validity']['path'],'evidence_sha256':reports['rental_validity']['sha256'],'checks':cs,'iteration':'round012_rental_currentness','semantic_accuracy_claimed':False}]
 if changed:write(p,doc)
ledger=read(R/'COMPLETION_LEDGER.json');identity=[(r['id'],r['text'],r['text_sha256']) for r in ledger['requirements']]
for row in ledger['requirements']:
 for ident,requirements,finding,key,code in specs:
  if row['id'] not in requirements:continue
  if ident not in row['gaps']:row['gaps'].append(ident)
  row['acceptance_evidence']=[e for e in row['acceptance_evidence'] if not isinstance(e,dict) or e.get('iteration')!='round012_'+ident]+[{**reports[key],'iteration':'round012_'+ident,'scope':'bounded native source/task scope; final requirement remains open'}]
assert len(identity)==76 and identity==[(r['id'],r['text'],r['text_sha256']) for r in ledger['requirements']];write(R/'COMPLETION_LEDGER.json',ledger)
allrows=[r for p in R.glob('*_REQUIREMENT_REVIEWS.json') for r in read(p)['requirements']];assert len(allrows)==len({r['requirement_id'] for r in allrows})==48
count=sum(c['state']=='passed_controlled_acceptance' for r in allrows for c in r['criteria'])
status=read(R/'STATUS.json');status.update(last_recorded_at=time.time(),phase='complete_flow_audit_round012_source_scopes_repaired_remaining64_labels_and_final_acceptance_pending',latest_checkpoint_script='checkpoint_protocol_v3_admission.py',latest_round012_source_reaudit={'path':audit.name,'sha256':sha(audit)},latest_source_scope_reports=reports,requirement_specific_controlled_criteria_passed=count,complete=False,whole_flow_complete=False,candidate_installed=False,candidate_frozen=False)
status['last_component_repairs']=list(dict.fromkeys(status['last_component_repairs']+['G119','G120','G121','G122']));write(R/'STATUS.json',status)
header=f'''## Latest checkpoint — round012 source scope re-audit,225 original reviews; full Flow OPEN

Use **checkpoint_protocol_v3_admission.py** LAST. It invokes checkpoint_named_periods and record_round012_scope; never run those or an older recorder afterward. R135 remains mutable/uninstalled, R134 installed, protected model retained, no owner/frozen/model edits, no stop/kill, no actual model inference/optimization or R132 rerun. New source/process/health/code observations are pinned in STATUS.

Round012 individually read rows205–224 against actual source:225 unique reviews=65accepted+158corrected/enriched+2quarantined191/206;223 v2eligible(142train/81development),64unreviewed,next225. Separate v3:224eligible=223 version-only reuse proofs+individual191readmission,142train/82development, original206proposal/review retained exactly as quarantine,64unreviewed/noholdout/noREADY/nooptimizer. Versioning/repacking/source rechecks add no unique reviews. Importer27/current consumer4/v3 controls33 pass; historical281 saved files/final splits and93 stale tags unchanged. Original205/prior adjudications remain immutable.

G119 fixed native full-package field scope, name-inside-platform/service slots and the sole hypothetical unit-price condition with source amount/revision/clock recomputation. {reports['named_package']['path']}68 controls: actual12 raw package questions, independent source edits/new owner name/missing seats, real equipment/ordinary-fee siblings and forged amount/record/revision/clock/receipt negatives. No package inclusion text is expanded into current physical inventory, no permission/booking is confirmed. General eligibility/quantities/conditions still retain their own obligations.

G120 fixed quotation noun creating a price task and underpayment-proof shortcut/actor-source mismatch. {reports['payment_predicate']['path']}16 controls: real document distinctions, typed current owner42 receipts/unknown validity, genuine price sibling, authorized owner edit updates attestation, independent forged snapshot rejected, withdrawn source does not restore constants. G121 {reports['policy_topic']['path']}17 controls now requests the missing predicate for original206 and bounded drinks/area fragments; explicit carrying/consumption/policy/facility questions survive. Native clarification does not manufacture a training target:206 stays quarantined in both cohorts.

G122: retained package effective intervals are unknown. Delivery now explicitly discloses the interval/current applicability limit and remains partial; {reports['rental_validity']['path']}6 actual isolated owner-source controls verify Thai/English, nonprice fields, known-current, expired and future intervals. No real owner interval or permission was supplied to force a pass. Package terms and eligibility remain separate source obligations.

{audit.name} preserves before/after full Q/A for all20 original rows plus locators, source-purpose notes and test-harness corrections. It is bounded source/native evidence, not actual model or whole-category semantic acceptance. Original76 IDs/text/hash/14categories/spec3files unchanged;48 requirement-specific reviews/{count} bounded criteria, none finally closed. G115dated closure/changed-hours mapping, other context transforms, semantic families/eight strata/metrics/protocol/source/clock/budget freeze, actual GPU optimization/three arms,28 original sections/all14 final category acceptances/root750/R133459/R134delta or supersession/final330exact saved-successful raw/freeze/API/full-live SQLitebackup/normal activation/re-audit remain. Keep heartbeat.

Next: {status['next_work']}

## Historical checkpoint before round012 source-scope re-audit

'''
p=R/'CURRENT_HANDOFF_TH.md';old=p.read_text('utf8');marker='## Historical checkpoint before round012 source-scope re-audit\n\n';old=old.split(marker,1)[1] if marker in old else old;p.write_text(header+old,'utf8')
print(json.dumps({'source_reaudit':audit.name,'individual_requirement_reviews':48,'bounded_criteria':count,'unique_original_label_reviews':225,'remaining_labels':64,'gaps':len(gapdoc['gaps']),'installed':'R134','candidate_installed':False,'complete':False}))
