"""Read-only inventory of code/data/wiring gaps. No API or model requests."""
import ast,collections,hashlib,json,sqlite3,sys
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;S=ROOT/'r123_contract_execution_20261023/revision05_system'
LEGACY=Path('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(S))
from app.knowledge.common.registry import CATALOG,value
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write(n,v):(R/n).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
db=S/'data/knowledge/common.sqlite';before=sha(db)
with sqlite3.connect(db.resolve().as_uri()+'?mode=ro',uri=True) as c:
 records={rid:json.loads(payload) for rid,payload in c.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0')}
 sources={sid:json.loads(meta) for sid,meta in c.execute('SELECT source_id,payload FROM cc_sources')}
fields=[];stats=collections.defaultdict(collections.Counter)
for rid,r in records.items():
 for key,f in r['fields'].items():
  stats[r['kind']+' / '+key][f['status']]+=1
  fields.append({'record_id':rid,'kind':r['kind'],'field':key,'status':f['status'],'evidence_ref_count':len(f.get('evidence_refs',[])),
    'optional_unknown_is_not_automatically_missing_business_fact':True})
(R/'ALL_FIELD_STATUSES.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in fields),'utf8')
selected={
 'service':['resource_ids','platform','zone_ids','capacity_persons'],
 'game_service':['game_id','service_id','offered','installed_resource_ids'],
 'game':['players_min','players_max','supported_platforms','summary','official_description'],
 'schedule':['timezone','zone_ids','open_periods','bookable_periods','maintenance_periods','service_slots','service_closed'],
 'rate':['service_id','audience_id','amount_minor','unit','duration_minutes','calculation_rule'],
 'rental_package':['zone_ids','audience_id','period_label','amount_minor','duration_minutes','terms'],
 'closure':['local_date','zone_ids','state','resolution_policy_id'],
 'procedure':['preconditions','steps','required_documents','deadline_minutes'],
 'control_set':['game_id','platform','input_device','preset','bindings','limitations'],
 'competition':['coverage','rulebook_release'],'competition_rule':['completeness','depends_on_ids']}
critical=[]
for rid,r in records.items():
 for key in selected.get(r['kind'],[]):
  if key not in r['fields']:continue
  f=r['fields'][key]
  if f['status']!='known':critical.append({'record_id':rid,'kind':r['kind'],'field':key,'status':f['status'],'validity':r.get('validity'),
     'classification':'conflict_requires_scope_or_authority_review' if f['status']=='conflicted' else 'source_or_projection_gap_not_yet_adjudicated'})
write('PRIORITY_FIELD_GAPS.json',critical)
rate_rows=[{'record_id':rid,'service_id':value(r,'service_id'),'audience_id':value(r,'audience_id'),
 'duration_minutes':value(r,'duration_minutes'),'calculation_rule':value(r,'calculation_rule'),'rule_status':r['fields'].get('calculation_rule',{}).get('status'),
 'validity':r.get('validity')} for rid,r in records.items() if r['kind']=='rate']
write('RATE_RULE_INVENTORY.json',rate_rows)
summary={'scope':'R123 revision05; source/AST inspection only, not universal semantic completeness or live health verification',
 'candidate':str(S),'legacy_reference':str(LEGACY),'records':len(records),'sources':len(sources),
 'record_kinds':dict(collections.Counter(r['kind'] for r in records.values())),
 'schema_kinds_without_active_records':sorted(set(CATALOG)-{r['kind'] for r in records.values()}),
 'field_status_totals':dict(collections.Counter(x['status'] for x in fields)),
 'field_status_by_kind_field':{k:dict(v) for k,v in sorted(stats.items())},
 'validity_by_kind':{kind:dict(collections.Counter(r['validity']['state'] for r in records.values() if r['kind']==kind)) for kind in sorted({r['kind'] for r in records.values()})},
 'selected_non_known_field_count':len(critical),'live_binding_count':sum(r['kind']=='live_binding' for r in records.values()),
 'same_database_sha256_before_after':before==sha(db),'database_sha256':before,'new_api_calls':0,'new_model_calls':0,'new_tests':False}
write('DATA_INVENTORY.json',summary)
# Record code evidence without dumping environment, credentials or raw exports.
targets={
 'app/booking/live_status.py':['DEFAULT_STATUS_URL','BOOKING_SOURCE_URL','_RESOURCE_GROUPS','get_live_booking_status','resolve_live_target_date','requested_time_window'],
 'app/booking/wordpress_status.py':['fetch_wordpress_status'],
 'booking_dashboard/server.py':['chatbot_status_payload','build_status'],
 'app/calendar/service_calendar.py':['now_bangkok','resolve_date_from_text','resolve_month_from_text','resolve_year_from_text','regular_service_slots'],
 'app/calculator/service_fee.py':['calculate_service_fee'],
 'app/knowledge/common/live_reader.py':['answer'],
 'app/knowledge/common/domain_flow/financial.py':['unit_calculation','billing','rental_pool','resume_financial'],
 'app/knowledge/common/domain_flow/integration.py':['answer','_answer','package'],
 'app/knowledge/common/domain_flow/capabilities.py':['resolve'],
 'app/knowledge/common/domain_flow/task_execution.py':['execute','_execute'],
 'app/knowledge/common/domain_flow/plan_contract.py':['compile_request'],
 'app/knowledge/common/domain_flow/native_contract.py':['attach_native','guard_contract'],
 'app/pipeline/migrated_chat.py':['_answer']}
evidence=[]
for relative,names in targets.items():
 for basis,base in [('candidate',S),('legacy',LEGACY)]:
  p=base/relative
  if not p.is_file():continue
  tree=ast.parse(p.read_text('utf-8-sig'));found={}
  for node in tree.body:
   if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) and node.name in names:found[node.name]=node.lineno
   if isinstance(node,ast.Assign):
    for target in node.targets:
     if isinstance(target,ast.Name) and target.id in names:found[target.id]=node.lineno
  evidence.append({'basis':basis,'path':str(p.resolve()),'sha256':sha(p),'symbols':found})
write('CODE_EVIDENCE.json',evidence)
print(json.dumps({k:v for k,v in summary.items() if k not in {'field_status_by_kind_field','validity_by_kind'}},ensure_ascii=False,indent=2))
