"""Append evidence-backed revisions in the isolated candidate only.

Preserve every original document, retain newer known values, and explicitly
restore omitted typed relationships/search rules. Never edit approvals.
"""
import ast,base64,collections,copy,gzip,hashlib,json,re,sqlite3,sys
from datetime import date,timedelta
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S))
from app.knowledge.common.registry import CATALOG,template,value,now,validate
from app.knowledge.common.store import CommonStore
from app.knowledge.records import canonical_json
store=CommonStore(S/'data/knowledge/common.sqlite')
with store.connect() as connection:registered={sid:json.loads(meta)['sha256'] for sid,meta in connection.execute('SELECT source_id,payload FROM cc_sources')}
before=json.loads((R/'NATIVE_BEFORE.json').read_text('utf8'));records=copy.deepcopy(before['records']);old=copy.deepcopy(records)
canonical=json.loads((R/'LEGACY_RECORDS.json').read_text('utf8'));inventory=json.loads((R/'FILE_INVENTORY.json').read_text('utf8'))
constants=json.loads((R/'CODE_CONSTANTS.json').read_text('utf8'));withdrawn=set(before['withdrawn'])
changes=[];mapping=[];preserved=[];deferred=[];aliases=[];file_checks=[]
def norm(x):return re.sub(r'[^\w]','',str(x).casefold())
def stable(x):return re.sub('[^a-z0-9_:-]','_',x.lower())
def dump(n,x):(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
def const(name):return next(x['value'] for x in constants if name in x['names'])
def native_target(cid):
 options=[cid,stable(cid),'migrated_faq_'+stable(cid),'competition_'+stable(cid)]
 return next((x for x in options if x in records or x in withdrawn),None)
def source(path,data,mapped,kind,transform,public_url=None):
 snapshot=canonical_json({'original_path':path,'original':data,'mapped_fields':mapped,'transform':transform})
 sid='r119_'+hashlib.sha256((path+'\0'+snapshot).encode()).hexdigest()[:28]
 meta={'source_id':sid,'kind':'derived_curated','path':path,'sha256':hashlib.sha256(snapshot.encode()).hexdigest(),
       'authority_for':[kind] if kind else [],'observed_at':now(),'trust':'legacy_unreviewed','public_url':public_url if isinstance(public_url,str) and public_url.startswith('https://') and not re.search(r'[\s<>\[\]()]',public_url) else None}
 if sid in registered:assert registered[sid]==meta['sha256']
 else:store.add_source(meta,snapshot,actor='r119_complete_source_migration');registered[sid]=meta['sha256']
 return sid
def put(r,key,v,path,data,transform,*,replace=False):
 if v is None or v=='':return
 existing=r['fields'].get(key,{'status':'unknown','value':None})
 if existing['status']=='known' and existing['value']==v:return
 if existing['status']=='known' and not replace:
  deferred.append({'record_id':r['record_id'],'field':key,'reason':'newer_known_value_retained','incoming':v,'retained':existing['value'],'path':path});return
 if existing['status']=='conflicted' and not replace:
  deferred.append({'record_id':r['record_id'],'field':key,'reason':'conflict_not_silently_resolved','incoming':v,'path':path});return
 sid=source(path,data,{key:v},r['kind'],transform)
 r['fields'][key]={'status':'known','value':v,'evidence_refs':[{'source_id':sid,'locator':'/mapped_fields/'+key}],'note':'R119: '+transform}
 changes.append({'record_id':r['record_id'],'field':key,'before_status':existing['status'],'source_id':sid,'source_path':path,'transform':transform})
def add_alias(r,lang,values,path):
 for text in values:
  if not isinstance(text,str) or not text.strip() or text in r['aliases'][lang] or len(text)>200:continue
  r['aliases'][lang].append(text);aliases.append({'record_id':r['record_id'],'locale':lang,'alias':text,'source_path':path})
def bi(th,en=None):return {'th':th or None,'en':en or None}
zone_by_name={norm(label):rid for rid,r in records.items() if r['kind']=='zone' for label in (value(r,'name') or {}).values() if label}
game_by_name={norm(label):rid for rid,r in records.items() if r['kind']=='game' for label in (value(r,'title') or {}).values() if label}
def zone_ids(labels):
 out=[]
 for label in labels:
  rid=zone_by_name.get(norm(label))
  if not rid:raise AssertionError(('Unmapped explicit zone',label))
  if rid not in out:out.append(rid)
 return out
# Store complete inputs compressed in the source registry, never as competing
# active answers. Source references for typed fields use separate JSON mappings.
for item in inventory:
 p=S/item['path'];status=item['classification']
 if status=='native_database_or_runtime_state':
  file_checks.append({**item,'disposition':'native_state_audited_separately_not_business_source'});continue
 if status=='evaluation_or_intent_workload_not_business_authority' or '/routing_eval_' in item['path']:
  file_checks.append({**item,'disposition':'test_or_intent_workload_excluded_from_answer_authority'});continue
 raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==item['sha256']
 payload={'original_sha256':item['sha256'],'original_bytes':len(raw),'encoding':'gzip-base64','bytes':base64.b64encode(gzip.compress(raw,mtime=0)).decode()}
 sid=source(item['path'],payload,{},None,'lossless source archive; not active answer authority')
 file_checks.append({**item,'disposition':'source_preserved_losslessly','archive_source_id':sid})
# Attach the canonical source object to its current native root. Existing
# withdrawals remain withdrawn; their originals stay in the source archive.
for item in canonical:
 row=item['record'];cid=row['content_id'];rid=native_target(cid);path=item['path']
 if not rid and row.get('facts',{}).get('route_category')=='no_answer':
  mapping.append({'content_id':cid,'path':path,'native_record_id':None,'status':'nonassertive_legacy_guard_template_preserved_as_source','reason':'old absence/provider-unavailable wording is not a permanent business fact; current native source/provider guards remain authoritative'});continue
 if not rid:raise AssertionError(('Canonical source not mapped or explicitly retired',cid))
 if rid in withdrawn:
  mapping.append({'content_id':cid,'path':path,'native_record_id':rid,'status':'retired_source_preserved_not_reactivated'});continue
 r=records[rid];f=row.get('facts',{});th=row.get('locales',{}).get('th',{}).get('fields',{});en=row.get('locales',{}).get('en',{}).get('fields',{})
 put(r,'legacy_context',row,path,row,'lossless canonical record, including original locale status and provenance')
 for lang in ['th','en']:add_alias(r,lang,row.get('aliases',{}).get(lang,[]),path)
 kind=row['kind'];semantic=[]
 if kind=='game_profile':
  put(r,'studio_zone_ids',zone_ids(f.get('zones') or []),path,row,'explicit facts.zones -> native zone IDs; no resource inference')
  semantic+=['facts.zones']
 if kind=='service_availability':
  put(r,'studio_zone_ids',zone_ids([f['zone']]),path,row,'explicit facts.zone -> native zone ID; no machine IDs invented')
  semantic+=['facts.zone']
 if kind=='member':
  if row.get('lifecycle',{}).get('status')=='published' and str(f.get('source_url','')).startswith('https://esports.'):
   put(r,'public_scope',bi('ชื่อ ตำแหน่ง ทีม และสังกัดที่เผยแพร่ในโปรไฟล์ต้นทาง','Published profile fields: display name, role, team and affiliation'),path,row,
       'carry recorded published public-profile scope only; not new owner approval, current-tenure verification, or private-contact authorization')
  for key,raw in [('affiliation',th.get('affiliation')),('period',f.get('period'))]:
   if raw:put(r,key,bi(raw,en.get(key)),path,row,'copy explicit original profile field')
  semantic+=['lifecycle.status','facts.group','facts.period','locales.th.name','locales.th.role','locales.th.affiliation']
 if kind=='policy_rule':
  put(r,'legacy_search',{'intent':f.get('intent'),'route_category':f.get('route_category'),'patterns':f.get('patterns',[]),'priority':f.get('priority',0)},path,row,
      'original query patterns and priority are retrieval metadata, not business answers')
  semantic+=['facts.patterns','facts.intent','facts.route_category','facts.priority']
 if kind=='equipment':
  specs=value(r,'specifications') or [];quant=f.get('quantity');z=f.get('zone')
  new=copy.deepcopy(specs)
  for key,v in [('quantity',quant),('zone',z)]:
   if v is not None and v!='' and not any(x.get('key')==key for x in new):new.append({'key':key,'value':str(v),'unit':None})
  if new!=specs:put(r,'specifications',new,path,{'legacy':row,'prior_field':r['fields'].get('specifications')},'retain existing specifications; add missing explicit original inventory attributes',replace=True)
 mapping.append({'content_id':cid,'path':path,'native_record_id':rid,'status':'current_native_root_linked','typed_restored_paths':semantic})
# Direct game/service/zone edges cover titles without a standalone profile too.
for item in canonical:
 row=item['record'];f=row.get('facts',{})
 if row['kind']!='service_availability':continue
 for title in f.get('games',[]):
  gid=game_by_name.get(norm(title))
  if not gid:raise AssertionError(('Unmapped offered game',title))
  refs=zone_ids([f['zone']]);existing=value(records[gid],'studio_zone_ids') or []
  if not set(refs)<=set(existing):put(records[gid],'studio_zone_ids',sorted(set(existing+refs)),item['path'],{'availability':row,'prior_zone_ids':existing},'union explicit service-game membership and explicit service zone',replace=True)
# Carry linguistic aliases from the old resolver as editable native aliases.
group_map={'psu_student_staff':'audience_psu_student_staff','general_student':'audience_psu_alumni_general_student','general_adult':'audience_general_adult'}
for key,labels in const('CUSTOMER_GROUP_ALIASES').items():
 if key not in group_map:raise AssertionError(('Unmapped audience code',key))
 r=records[group_map[key]]
 for text in labels:add_alias(r,'th' if re.search('[\u0e00-\u0e7f]',text) else 'en',[text],'app/core/normalization.py#CUSTOMER_GROUP_ALIASES')
for key,label in const('GROUP_LABELS').items():
 if key in group_map:add_alias(records[group_map[key]],'th',[label],'app/calculator/service_fee.py#GROUP_LABELS')
service_aliases=const('SERVICE_ALIASES')
platform_map={'pc':'pc','ps5':'playstation5','nintendo_switch':'nintendoswitch','cockpit':'cockpit','vr':'vr'}
for rid,r in records.items():
 if r['kind']!='service':continue
 platform=norm(value(r,'platform') or '')
 for key,pf in platform_map.items():
  if pf==platform or key=='ps5' and platform in {'ps5','playstationps5'}:
   for text in service_aliases[key]:add_alias(r,'th' if re.search('[\u0e00-\u0e7f]',text) else 'en',[text],'app/core/normalization.py#SERVICE_ALIASES')
# Reuse old period rounding only when native rate duration and price still
# match its exact service/group row; keep owner-confirmed billing unit intact.
fees=const('SERVICE_FEES');fee_path='app/calculator/service_fee.py';fee_code=(S/fee_path).read_text('utf8')
assert re.search(r'math\.ceil\(',fee_code),'Original session rounding must be evidenced in executable source'
for rid,r in records.items():
 if r['kind']!='rate':continue
 service=records.get(value(r,'service_id'),{});name=' '.join((value(service,'name') or {}).values());platform=norm(value(service,'platform') or '')
 key='pc' if platform=='pc' else 'ps5' if platform in {'playstation5','ps5','playstationps5'} else 'cockpit' if platform=='cockpit' else None
 if platform=='nintendoswitch':key='nintendo_switch_3_4' if value(service,'capacity_max')==4 else 'nintendo_switch_1_2'
 if platform in {'vr','playstationvr2'} or 'vr' in name.casefold():key='vr_30' if value(r,'duration_minutes')==30 else 'vr_60'
 group=next((g for g,a in group_map.items() if a==value(r,'audience_id')),None)
 fee=fees.get(key or '')
 if not fee or not group or value(r,'duration_minutes')!=fee['minutes_per_session'] or value(r,'amount_minor')!=fee['prices'][group]*100:
  deferred.append({'record_id':rid,'reason':'legacy_rounding_not_transferred_without_exact_service_duration_price_match','candidate_service':key});continue
 put(r,'calculation_rule','session_ceil',fee_path,{'SERVICE_FEES':fees,'code':fee_code,'selected_service':key,'selected_group':group,'retained_unit':value(r,'unit')},
     'original ceil(duration/session_minutes) period rule; current amount and billing unit retained')
# Published/draft translations can be search aliases, never new reviewed names.
for p in sorted((S/'data/locales/en').rglob('*.jsonl')):
 for line in p.read_text('utf-8-sig').splitlines():
  if not line.strip():continue
  row=json.loads(line);cid=row.get('content_id');field=row.get('field');text=row.get('text')
  if cid in records and records[cid]['kind']=='person' and field=='name' and isinstance(text,str) and text.strip():
   add_alias(records[cid],'en',[text.strip()],str(p.relative_to(S)).replace('\\','/'))
# Role search vocabulary is independent of the fact's actual role value.
role_aliases=const('_MEMBER_ROLE_QUERY_ALIASES')
for r in records.values():
 if r['kind']!='person':continue
 role=value(r,'role') or {};values=set(role.values());found=[key for key,labels in role_aliases.items() if any(x in values for x in labels)]
 if found:put(r,'role_aliases',sorted(found),'app/pipeline/bilingual_english.py#_MEMBER_ROLE_QUERY_ALIASES',role_aliases,'search synonyms only; recorded role and exact longest-match scope retained')
# Export all seven weekdays from the pure legacy calendar function, then read
# only native fields at runtime. Keep physical open_periods conflicts intact.
from app.calendar.service_calendar import regular_service_slots
calendar_path='app/calendar/service_calendar.py';calendar_code=(S/calendar_path).read_text('utf8')
for weekday in range(7):
 rid='migrated_schedule_'+str(weekday);r=records[rid];slots=regular_service_slots(date(2026,10,19)+timedelta(days=weekday))
 put(r,'service_slots',slots,calendar_path,{'code':calendar_code,'weekday':weekday,'service_slots':slots},'export original regular_service_slots without changing physical opening fields')
 put(r,'service_closed',not any(s.get('state')=='open' for s in slots),calendar_path,{'code':calendar_code,'weekday':weekday,'service_slots':slots},'record regular play-service closure; maintenance does not imply building closure')
# Save append-only revisions after every referenced target and source exists.
saved=[]
for rid,r in records.items():
 if r==old[rid]:continue
 receipt=store.save(r,actor='r119_complete_source_migration',expected_version=old[rid]['revision'],change_note='Full legacy parity audit: preserve original context and restore evidenced omitted fields/search/period rules; no approval or production publication')
 saved.append(receipt)
dump('RECORD_MAPPING.json',mapping);dump('MIGRATED_FIELDS.json',changes);dump('MIGRATED_ALIASES.json',aliases);dump('RETAINED_VARIANTS_AND_LIMITS.json',deferred)
dump('FILE_DISPOSITIONS.json',file_checks);dump('SAVE_RECEIPTS.json',saved)
summary={'phase':'migration_written_awaiting_full_audit','canonical_records_checked':len(canonical),'canonical_active_mapped':sum(x['status']=='current_native_root_linked' for x in mapping),
 'retired_not_reactivated':sum(x['status'].startswith('retired') for x in mapping),'files_accounted':len(file_checks),'saved_native_revisions':len(saved),'changed_fields':len(changes),'added_aliases':len(aliases),
 'native_approvals_changed':False,'production_installed':False,'baseline_answers_run':False,'retained_variant_cases':len(deferred)}
dump('MIGRATION_STATUS.json',summary);print(json.dumps(summary))
