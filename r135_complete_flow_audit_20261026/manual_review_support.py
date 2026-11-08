"""Write explicit per-question adjudications; never generate semantic decisions."""
import copy,json
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import *
W=R/'training_review_workbench_1793037663397671000'
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(x) for x in p.read_text('utf8').splitlines() if x.strip()]
def record_round(name,parent,notes,source_ids,edits,source_issues,*,quarantines=None):
    quarantines=quarantines or {};assert set(quarantines)<=set(notes) and all(isinstance(reason,str) and reason.strip() for reason in quarantines.values())
    assert set(notes)==set(source_ids) and set(edits)<=set(notes) and set(source_issues)<=set(notes)
    O=W/name;O.mkdir(exist_ok=False);S=W/parent
    def write(n,v):
        p=O/n;p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in v) if n.endswith('.jsonl') else json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf8');return p
    source=read(W/'SOURCE_SNAPSHOT.json');source_ref=read(W/'SOURCE_REF.json');source_sha=digest(source_identity(source));examples=rows(S/'EXAMPLES.jsonl');reviews=rows(S/'REVIEWS.jsonl');prior_reviews=copy.deepcopy(reviews);review_index=read(S/'REVIEW_INDEX.json');done={v['row'] for v in review_index};assert not done&set(notes)
    lookup={x['annotation_provenance']['historical_review_ref']['line']-1:x for x in examples};tokenizer=Path('D:/CodexTraining/psu-r121-20261022/model/tokenizer_config.json');runtime=runtime_contract(read(tokenizer),chat_template=tokenizer.with_name('chat_template.jinja').read_text('utf8'),model_profile=read(W/'DECLARED_MODEL_PROFILE.json'));write('RUNTIME_CONTRACT.json',runtime)
    for i,reasons in notes.items():
        assert len(reasons)==len(CRITERIA) and all(reasons);x=lookup[i];prior=copy.deepcopy(x['plan_label'])
        if i in edits:edits[i](x['plan_label'])
        x['annotation_provenance'].update(method='manual_review_of_saved_question',runtime_contract_sha256=digest(runtime));decision='quarantined' if i in quarantines else 'accepted' if prior==x['plan_label'] else 'corrected';who={'id':'Codex-primary-agent-R135-source-adjudication','kind':'agent'};ids=source_ids[i];assert all(k in source['release']['records'] for k in ids)
        issues=[{'scope':'answer_source','reason':reason,'handling':handling} for reason,handling in source_issues.get(i,[])]
        evidence={'question_key':x['question_key'],'example_sha256':example_sha(x),'adjudication_status':decision,'reviewer':who,'source_identity_sha256':source_sha,'criteria':{n:{'status':'passed','reason':reason,'raw_quotes':[x['raw_question']],'source_record_ids':ids if n=='source_version_alignment' else []} for n,reason in zip(CRITERIA,reasons)},'unresolved_issues':issues,'historical_review_row':i,'prior_label':prior,'reviewed_label':x['plan_label'],'review_scope':'language plan only; no answer accuracy certificate','source_field_evidence':{rid:{'revision':source['release']['records'][rid]['revision'],'record_sha256':digest(source['release']['records'][rid])} for rid in ids}}
        if decision=='quarantined':
            issues.append({'scope':'label_protocol','reason':quarantines[i],'handling':'Do not optimize the retained proposal; separately review a correct versioned representation before readmission.'});evidence['quarantine_reason']=quarantines[i];evidence['criteria']['intent_operation_facet']['status']='unresolved'
        p=write('ADJUDICATION_'+str(i).zfill(3)+'.json',evidence);review={'version':VERSION,'question_key':x['question_key'],'example_sha256':example_sha(x),'adjudication_status':decision,'reviewer':who,'review_method':'individual_source_adjudication','source_version':source_ref,'adjudication_ref':{'path':str(p.resolve()),'sha256':file_sha(p)},'teacher_status':'not_applicable','teacher_trace_refs':[],'unresolved_issues':issues}
        if decision=='quarantined':review['quarantine_reason']=quarantines[i]
        reviews.append(review);review_index.append({'row':i,'question_key':x['question_key'],'decision':decision,'changed_label':prior!=x['plan_label'],'source_record_ids':ids})
    bykey={r['question_key']:r for r in reviews};artifacts=Artifacts(R.parent);artifacts._cache={}
    for x in examples:
        if x['question_key'] not in bykey:continue
        effective=planner_question(x,artifacts.read(x['annotation_provenance']['origin_ref']),artifacts,source_ref);before=example_sha(x);x['annotation_provenance']['runtime_contract_sha256']=digest(runtime);x['messages']=messages(effective)+[{'role':'assistant','content':json.dumps(x['plan_label'],ensure_ascii=False,separators=(',',':'))}];assert before==example_sha(x)==bykey[x['question_key']]['example_sha256']
    artifacts.verify_pinned_files();write('EXAMPLES.jsonl',examples);write('REVIEWS.jsonl',reviews);write('REVIEW_INDEX.json',review_index);inventory=read(W/'INVENTORY.json');report=prepare_dataset(O/'admission_bundle',examples,reviews,Artifacts(R.parent),source_ref,runtime,expected_keys=inventory['question_keys'],known_exposed=inventory['known_exposed_question_keys'])
    assert sum(x['eligible'] for x in report['rows'])==sum(r['adjudication_status'] in {'accepted','corrected'} for r in reviews) and sum(x['inventory_adjudicated'] for x in report['rows'])==len(reviews),[x for x in report['rows'] if x.get('adjudication_status') and not x['inventory_adjudicated']]
    summary={'individually_adjudicated':len(reviews),'new_adjudications':len(notes),'accepted':sum(x['decision']=='accepted' for x in review_index),'corrected_or_enriched':sum(x['decision']=='corrected' for x in review_index),'quarantined':sum(x['decision']=='quarantined' for x in review_index),'eligible_reviewed_rows':sum(x['eligible'] for x in report['rows']),'unreviewed':len(examples)-len(reviews),'total_original_inventory':len(examples),'prior_adjudications_unchanged':reviews[:len(prior_reviews)]==prior_reviews,'training_ready':report['ready_for_optimization'],'source_answer_issues_remain':sum(any(i.get('scope')=='answer_source' for i in r['unresolved_issues']) for r in reviews),'new_model_inferences':0,'optimizer_started':False,'historical_files_modified':False,'complete':False};write('SUMMARY.json',summary);print(json.dumps({'output':str(O),**summary}))
