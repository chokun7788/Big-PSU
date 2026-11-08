"""Receipt-scope controls on the actual recorded source projection; no HTTP/model."""
import copy,json,time
from types import SimpleNamespace
from verification_support import R
from app.knowledge.common.domain_flow.projection import compile_snapshot
from app.knowledge.common.domain_flow.index import FactIndex
from app.knowledge.common.domain_flow.receipt_scope import check
O=R/('named_event_receipt_scope_'+str(time.time_ns()));O.mkdir();s=json.loads((R/'training_review_workbench_1793037663397671000/SOURCE_SNAPSHOT.json').read_text('utf8'));index=FactIndex(compile_snapshot(s));event='competition_competition_rules_rov_blueket_2025_men';rid=event+'_section_005';fact=next(f for f in index.byrecord[rid] if f['category']=='C13');q="Under Blueket Games 2025 Men's Team AOV tournament rules what is the competition format?";task=SimpleNamespace(category='C13',operation='detail',facet='rule_clause',target_span=None);proofs={};checks={}
def run(name,idx,f,question,t=task):proofs[name]=check(idx,t,f,question);return proofs[name]
p=run('named',index,fact,q);checks['exact_full_event_verified']=p['verified'] and p['target_binding_verified']
p=run('unnamed',index,fact,'What is the AOV competition format?');checks['unnamed_event_not_verified']=not p['verified'] and not p['target_binding_verified']
p=run('partial',index,fact,'What is the Blueket AOV competition format?');checks['partial_event_title_not_verified']=not p['verified'] and not p['target_binding_verified']
wrong=next(f for f in index.bycat['C13'] if f.get('event_id') and f.get('event_id')!=event);p=run('wrong_event',index,wrong,q);checks['different_event_rejected']=not p['verified'] and 'source_receipt_named_event_mismatch' in p['errors']
idx=copy.deepcopy(index);dup=copy.deepcopy(idx.records[event]);dup['record_id']='isolated_duplicate_competition';idx.records[dup['record_id']]=dup;p=run('duplicate_title',idx,fact,q);checks['duplicate_full_title_not_verified']=not p['verified'] and not p['target_binding_verified']
idx=copy.deepcopy(index);idx.records[event]['fields']['event_name']['value']['en']='Different event title';idx.records[event]['fields']['event_name']['value']['th']='Different event title';p=run('edited_title',idx,fact,q);checks['renamed_event_no_stale_binding']=not p['verified'] and not p['target_binding_verified']
result={'checks':checks,'all_passed':all(checks.values()),'proofs':proofs,'scope':'Direct actual source projection with isolated in-memory record/fact changes; not an end-to-end owner-edit or forgery test.','http_or_inference':False};(O/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'path':str(O),'checks':checks},ensure_ascii=False));assert result['all_passed']
