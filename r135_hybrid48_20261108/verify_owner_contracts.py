"""Isolated owner workflow, never the user's database or approvals."""
import copy,json,os,time
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.store import CommonStore,Conflict
from app.knowledge.common.registry import template,CATALOG,schema_errors,validate,content_hash
from app.knowledge.common.owner_server import save_owner_record,preview_answer
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
out=R/('owner_contract_verification_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'controlled_owner.sqlite');store.initialize(allow_demo=False)
checks={};checks['all_registered_form_templates_schema_valid']=all(not schema_errors(template(k)) for k in CATALOG)
def record():
 r=template('faq');r['record_id']='controlled_owner_faq';r['localization']['en_status']='agent_translated'
 for k,v in {'question':{'th':'ข้อมูลอัลฟาคืออะไร','en':'What is controlled alpha?'},'answer':{'th':'ข้อมูลทดสอบร่างเท่านั้น','en':'Controlled draft source only'},'topic':'controlled_alpha'}.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return r
r=record();saved=save_owner_record(store,r,0,'controlled-test')
checks['save_is_draft_not_approval']=store.get(r['record_id'])['record']['lifecycle']=='draft' and not store.get(r['record_id'])['approved_hash']
checks['draft_not_silently_published']=store.snapshot()['release'] is None
try:store.publish([r['record_id']],actor='controlled-test',expected_active='',request_key='unapproved');checks['unapproved_publish_rejected']=False
except Conflict:checks['unapproved_publish_rejected']=True
head=store.get(r['record_id']);item=head['record']
with store.connect() as c:sources=store.sources(c);records=store.heads(c)
bad=copy.deepcopy(item);bad['fields']['answer']['value']['en']='not in the attested source'
checks['value_source_pointer_mismatch_rejected']=any('value does not match source' in e for e in validate(bad,records,sources))
bad=copy.deepcopy(item);bad['record_id']='controlled_missing_reference';bad['fields']['related_ids']={'status':'known','value':['missing_target'],'evidence_refs':[],'note':''}
try:save_owner_record(store,bad,0,'controlled-test');checks['foreign_key_missing_reported']=False
except ValueError as exc:checks['foreign_key_missing_reported']='missing reference' in str(exc)
bad=copy.deepcopy(item);bad['fields']['answer']['status']='conflicted';bad['fields']['answer']['value']=None
checks['conflicted_cannot_publish']=bool(validate(bad,records,sources,publish=True))
bad=copy.deepcopy(item);bad['fields']['topic'].update(status='unknown',value='assertion while unknown')
checks['unknown_cannot_assert_value']=bool(schema_errors(bad))
checks['unknown_distinct_from_not_applicable']=template('policy')['fields']['exceptions']['status']=='unknown'
try:save_owner_record(store,copy.deepcopy(item),0,'controlled-test');checks['stale_edit_rejected']=False
except Conflict:checks['stale_edit_rejected']=True
store.approve(r['record_id'],saved['version'],saved['hash'],actor='controlled-reviewer')
release=store.publish([r['record_id']],actor='controlled-test',expected_active='',request_key='controlled-publish')
checks['reviewed_fixture_publish_requires_explicit_revision_hash']=store.snapshot()['active']==release
checks['publish_idempotent']=store.publish([r['record_id']],actor='controlled-test',expected_active='',request_key='controlled-publish')==release
published_before=store.snapshot()
item=store.get(r['record_id'])['record'];item['fields']['answer']['value']={'th':'แก้เฉพาะร่างรอบใหม่','en':'Edited draft only'}
edit=save_owner_record(store,item,1,'controlled-test')
checks['new_revision_does_not_inherit_old_approval']=store.get(r['record_id'])['approved_hash'] is None
checks['published_snapshot_keeps_prior_revision']=store.snapshot()['release']['records'][r['record_id']]['fields']['answer']['value']['en']=='Controlled draft source only'
checks['draft_view_explicitly_separate']=DraftSnapshotView(store).snapshot()['release']['records'][r['record_id']]['fields']['answer']['value']['en']=='Edited draft only'
checks['epoch_invalidates_inflight_snapshot']=not store.still_current(published_before)
reviewed=store.get(r['record_id'])['record'];reviewed['localization'].update(en_status='reviewed',source_revision_hash=content_hash(reviewed));reviewed['fields']['answer']['value']['en']='unreviewed new wording'
stale=save_owner_record(store,reviewed,2,'controlled-test')['record']
checks['content_edit_invalidates_translation_review']=stale['localization']['en_status']=='stale'
store.withdraw(r['record_id'],actor='controlled-test')
snap=store.snapshot();compiled=Engine.from_snapshot(snap)
checks['withdrawn_published_content_not_in_next_index']=not any(f['record_id']==r['record_id'] for f in compiled.index.facts)
try:store.rollback(release,actor='controlled-test',expected_active=release);checks['rollback_does_not_resurrect_withdrawn']=False
except Conflict:checks['rollback_does_not_resurrect_withdrawn']=True
with store.connect() as c:
 events=[x[0] for x in c.execute('SELECT event FROM cc_audit ORDER BY id')]
 checks['save_review_publish_edit_withdraw_audited']=all(e in events for e in ['source','save','approve','publish','withdraw'])
report={'all_passed':all(checks.values()),'checks':checks,'database':str(store.path),'actual_model_inferences':0,'user_data_or_approvals_modified':False};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');print(json.dumps(report));assert report['all_passed']
