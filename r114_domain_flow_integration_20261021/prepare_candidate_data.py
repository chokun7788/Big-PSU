"""Import supplied owner material into candidate drafts, never approvals.

The source snapshots retain original pointers. Rental values use the native
typed rental schema; scoped textual clarifications use source-backed FAQs.
"""
import hashlib,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;S=R/'system';sys.path.insert(0,str(S))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import template,now
from app.knowledge.records import canonical_json
from app.knowledge.common.domain_flow.projection import value,bilingual,title

def read(p):return json.loads(p.read_text('utf8'))
store=CommonStore(S/'data/knowledge/common.sqlite')
base=read(B/'r113_multi_flow_benchmark_20261021/COMMON_READ_MODEL.json')
with store.connect() as c:
    original=CommonStore.heads(c)
    before_approvals=c.execute('SELECT count(*) FROM cc_approvals').fetchone()[0]
    before_active=c.execute("SELECT value FROM cc_meta WHERE key='active'").fetchone()[0]
ledger=[]

def save_record(record,fields,origin,trust='owner_confirmed'):
    rid=record['record_id']
    try:existing=store.get(rid)
    except ValueError as exc:
        if str(exc)!='Unknown record':raise
        existing=None
    if existing:raise ValueError('Refusing to overwrite candidate record '+rid)
    snapshot={'fields':fields,'original_evidence':origin,'import_scope':'R114 candidate draft only; no publication approval'}
    raw=canonical_json(snapshot);sid='r114_import_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
    src={'source_id':sid,'kind':'owner_document','path':'candidate-import://'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),
      'authority_for':[record['kind']],'observed_at':now(),'trust':trust,'public_url':None}
    store.add_source(src,raw,actor='codex_candidate_import')
    for k,v in fields.items():record['fields'][k].update(status='known',value=v,evidence_refs=[{'source_id':sid,'locator':'/fields/'+k}],note='Imported source-backed candidate draft; not published')
    record['localization']['en_status']='agent_translated'
    result=store.save(record,actor='codex_candidate_import',expected_version=0,change_note='Import user-supplied source into isolated candidate draft; approvals unchanged')
    ledger.append({'record_id':rid,'kind':record['kind'],'source_id':sid,'original_evidence':origin,'version':result['version']})

rent=read(B/'r109_owner_answers_20261020/RENTAL_PACKAGES_RECONCILED.json')
for i,p in enumerate(rent['packages']):
    f=next(f for f in base['facts'] if f['category']=='C07' and f['record_id']=='package_'+str(i))
    record=template('rental_package');record['record_id']='package_'+str(i);record['aliases']={'th':[p['zone_name']],'en':[p['zone_name']]}
    fields={'name':f['subject'],'period_label':p['period_label'],'duration_minutes':p['duration_minutes'],'amount_minor':int(p['amount_thb']*100),
      'currency':'THB','equipment_included':bilingual(p['equipment_included']),'room_seats':p['room_seats']}
    zones=[rid for rid,r in original.items() if r['kind']=='zone' and any(x in p['zone_name'] for x in title(r).values() if len(x)>4)]
    if zones:fields['zone_ids']=zones
    audiences=[rid for rid,r in original.items() if r['kind']=='audience' and p['audience'] in rid]
    if len(audiences)==1:fields['audience_id']=audiences[0]
    save_record(record,fields,[{'path':str(B/'r109_owner_answers_20261020/RENTAL_PACKAGES_RECONCILED.json'),'locator':'/packages/'+str(i),'source':p}])

owner={x['source_question_id']:x for x in read(B/'r109_owner_answers_20261020/MERGED_SERVICE_STATEMENTS.json')['statements']}
for f in base['facts']:
    if f.get('fixture') or f['record_id'] in base['records'] or f['record_id'].startswith('package_'):continue
    # Native records preserve stable source-backed values. No test question,
    # expected answer or result file is used in this import.
    record=template('faq');rid='r114_'+re.sub('[^a-zA-Z0-9_]','_',f['record_id']+'_'+f['facet']).lower();record['record_id']=rid
    record['aliases']={'th':[s for s in f.get('aliases',[]) if re.search('[\u0e00-\u0e7f]',s)],'en':[s for s in f.get('aliases',[]) if not re.search('[\u0e00-\u0e7f]',s)]}
    descriptor={k:f[k] for k in ['category','facet','subject','label','numeric','section_number','english_translation_missing','owner_confirmed'] if k in f}
    descriptor['source_record_id']=f['record_id']
    statement=owner.get(f['record_id'])
    question={'th':statement['source_question'] if statement else f['subject']['th']+' — '+f['label']['th'],
      'en':f['subject']['en']+' — '+f['label']['en']}
    fields={'question':question,'answer':f['value'],'topic':f['category'],
      'scope_note':bilingual(json.dumps({'r114_fact':descriptor},ensure_ascii=False)),
      'intent_key':'r114.'+f['category']+'.'+f['facet']}
    # scope_note is bilingual in this registry; the compiler accepts the same
    # descriptor JSON in either language without treating it as answer text.
    save_record(record,fields,f['evidence_refs'],trust='official' if f['category']=='C13' else 'owner_confirmed')

with store.connect() as c:
    after_approvals=c.execute('SELECT count(*) FROM cc_approvals').fetchone()[0]
    after_active=c.execute("SELECT value FROM cc_meta WHERE key='active'").fetchone()[0]
assert before_approvals==after_approvals and before_active==after_active
result={'candidate_only':True,'records_imported':len(ledger),'approvals_before':before_approvals,'approvals_after':after_approvals,
 'active_release_unchanged':True,'native_rental_records':len(rent['packages']),'imports':ledger}
(R/'CANDIDATE_DATA_IMPORT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({k:v for k,v in result.items() if k!='imports'}))
