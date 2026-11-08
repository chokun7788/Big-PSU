"""Source-bound additive drafts. Existing revisions and production stay intact."""
import collections,copy,hashlib,json,re,sys,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent;H=B/'system/app/knowledge/common'
def dump(path,x):path.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
def read(rel):
 p=B/'source_snapshot'/rel
 return [json.loads(s) for s in p.read_text('utf-8-sig').splitlines() if s.strip()] if p.suffix=='.jsonl' else json.loads(p.read_text('utf-8-sig'))
cat=json.loads((H/'catalog.json').read_text('utf8'));by={x['kind']:x for x in cat}
local=copy.deepcopy(next(f['value_schema'] for f in by['game']['fields'] if f['key']=='summary'))
additions={
 'game':[('venue_zone_ids','โซนที่ระบุในข้อมูลเกมของศูนย์ (ไม่ใช่ทุกแพลตฟอร์มที่เกมรองรับ)',{'type':'array','items':{'type':'string','minLength':1},'uniqueItems':True},'zone'),('description_captured_at','เวลาที่เก็บคำบรรยายต้นฉบับ ไม่ใช่วันอัปเดตเกม',{'type':'string','format':'date-time'},None),('description_scope_note','ขอบเขตคำบรรยายจากต้นฉบับ',local,None)],
 'service':[('inventory_verified_on','วันที่รายการเกมและเครื่องถูกตรวจตามต้นฉบับ ไม่ใช่สถานะจองสด',{'type':'string','format':'date'},None),('inventory_basis','หลักฐานของรายการเกมและเครื่องตามต้นฉบับ',local,None)]
}
for kind,items in additions.items():
 schema=json.loads((H/'schemas'/f'{kind}.schema.json').read_text('utf8'));t=json.loads((H/'templates'/f'{kind}.draft.json').read_text('utf8'))
 for key,meaning,vs,ref in items:
  if any(f['key']==key for f in by[kind]['fields']):continue
  by[kind]['fields'].append({'key':key,'meaning_th':meaning,'publish_core':False,'reference_kind':ref,'value_schema':vs})
  slot=copy.deepcopy(next(iter(schema['properties']['fields']['properties'].values())));slot['description']=meaning;slot['oneOf'][0]['properties']['value']=vs
  schema['properties']['fields']['properties'][key]=slot;t['fields'][key]={'status':'unknown','value':None,'evidence_refs':[],'note':'ต้นฉบับยังไม่ยืนยัน'}
 dump(H/'schemas'/f'{kind}.schema.json',schema);dump(H/'templates'/f'{kind}.draft.json',t)
dump(H/'catalog.json',cat)
profiles=json.loads((H/'answer_profiles.json').read_text('utf8'))
labels={'venue_zone_ids':('โซนตามข้อมูลเกมของศูนย์','Venue zones in the source inventory'),'description_captured_at':('เก็บคำบรรยายเมื่อ','Description captured at'),'description_scope_note':('ขอบเขตคำบรรยาย','Description scope'),'inventory_verified_on':('วันที่ตรวจรายการตามต้นฉบับ','Inventory verified on'),'inventory_basis':('หลักฐานของรายการ','Inventory evidence')}
for kind,items in additions.items():
 for key,*_ in items:profiles.setdefault('labels',{}).setdefault(kind,{})[key]=dict(zip(('th','en'),labels[key]))
for kind,rule in [('game',{'when':['official_description'],'include':['description_captured_at','description_scope_note']}),('service',{'when':['inventory_verified_on','inventory_basis'],'include':['inventory_verified_on','inventory_basis']})]:
 context=profiles.setdefault('kinds',{}).setdefault(kind,{}).setdefault('context',[])
 if rule not in context:context.append(rule)
dump(H/'answer_profiles.json',profiles)
q=H/'query_contract.py';s=q.read_text('utf8').replace("CUES={'source_listing_sections':","CUES={'venue_zone_ids':['โซนของศูนย์','โซนตามรายการ','venue zones','venue inventory zones'], 'description_captured_at':['เก็บคำบรรยายเมื่อ','description captured at'], 'inventory_verified_on':['ตรวจรายการเมื่อ','วันที่ตรวจรายการ','inventory verified on'], 'inventory_basis':['หลักฐานรายการ','inventory evidence'], 'source_listing_sections':")
q.write_text(s,encoding='utf8')
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.registry import value,template,validate,now,pointer
from app.knowledge.common.store import CommonStore
from app.knowledge.records import canonical_json
db=B/(sys.argv[1] if len(sys.argv)>1 else 'candidate03.sqlite')
if db.exists():raise SystemExit('Preserve existing candidate; choose a new candidate for another attempt')
with sqlite3.connect((B/'before.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(db) as dst:src.backup(dst)
store=CommonStore(db)
with store.connect() as c:before=store.heads(c);sources_before=store.sources(c);old_rows=[tuple(r) for r in c.execute('select * from cc_revisions')];old_meta=dict(c.execute('select key,value from cc_meta'));old_approvals=[tuple(r) for r in c.execute('select * from cc_approvals')]
rs=copy.deepcopy(before);changes=collections.defaultdict(dict);lineage=[];skipped=[];aliases_added=[]
def norm(s):return re.sub(r'[^\w]','',str(s).casefold())
def game(name):
 ids=[rid for rid,r in rs.items() if r['kind']=='game' and norm(name) in [norm(v) for v in (value(r,'title') or {}).values() if v]]
 assert len(ids)==1,(name,ids)
 return ids[0]
def rec(kind,rid):
 if rid not in rs:rs[rid]=template(kind);rs[rid]['record_id']=rid
 return rs[rid]
def put(rid,key,v,rel,loc,rule='exact source copy',replace=False):
 r=rs[rid];old=value(r,key)
 if old==v:return
 if old is not None and not replace:raise ValueError(('Unexpected overwrite',rid,key))
 p=B/'source_snapshot'/rel
 # Validate the source locator before committing any migration.
 raw=read(rel) if p.suffix in {'.json','.jsonl'} else {'text':p.read_text('utf-8-sig')}
 origin=pointer(raw,loc)
 r['fields'][key]={'status':'known','value':v,'evidence_refs':[{'source_id':'r68_pending_evidence','locator':'/mapped_fields/'+key}],'note':'R68 source-bound draft; '+rule}
 changes[rid][key]=v;lineage.append({'record_id':rid,'field':key,'source_path':rel,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'locator':loc,'source_value':origin,'mapped_value':v,'transform':rule})
loc=lambda th,en:{'th':th,'en':en}
# Full raw descriptions supersede only exact abridgements or their translation.
translations=json.loads((B/'full_description_translations.json').read_text('utf8'))
rel='data/sources/our_games_raw.jsonl';full=[]
for i,x in enumerate(read(rel)):
 rid=game(x['game']);old=value(rs[rid],'official_description');lang='th' if re.search('[\u0e00-\u0e7f]',x['description']) else 'en'
 assert old and old[lang],(rid,lang)
 if old[lang]!=x['description']:
  assert x['description'].startswith(old[lang].removesuffix('...')),(rid,'not a source prefix')
  assert str(i) in translations,(i,lang,x['game'])
  v=loc(x['description'],translations[str(i)]) if lang=='th' else loc(translations[str(i)],x['description'])
  put(rid,'official_description',v,rel,f'/{i}/description','expand exact source prefix from full raw capture; agent counterpart translation, not owner approval',replace=True);full.append(rid)
 put(rid,'description_captured_at',x['scraped_at_utc'],rel,f'/{i}/scraped_at_utc')
 th='ข้อความคำบรรยายที่เก็บจากหน้า Our Games ตามวันที่ระบุ ไม่ยืนยันเวอร์ชันปัจจุบัน จำนวนผู้เล่นหรืออุปกรณ์ที่ศูนย์จัดให้ และสิทธิ์บริการออนไลน์/DLC'
 en='Description captured from the Our Games page on the stated date. It does not confirm the current game version, the venue’s player/equipment capacity, or access to online services or DLC.'
 if i==8:th+=' ต้นฉบับระบุสูงสุด 3 คน* ซึ่งยังต้องตรวจความหมาย/เชิงอรรถ';en+=' The source states up to 3 players*, whose meaning/footnote still needs verification.'
 if i==25:th+=' ต้นฉบับระบุเหตุการณ์ห่างจาก RE2 สองปี ซึ่งยังไม่ได้ยืนยันความถูกต้องของลำดับเรื่อง';en+=' The source says two years after RE2; the accuracy of this story chronology is unverified.'
 put(rid,'description_scope_note',loc(th,en),rel,f'/{i}','source scope and unresolved source-quality caveat; not a new gameplay or venue claim')
# Game-profile zones are venue inventory facts, not a global compatibility list.
zone_by_name={norm(v):rid for rid,r in rs.items() if r['kind']=='zone' for v in (value(r,'name') or {}).values() if v}
rel='data/curated/game_item_details.jsonl'
for i,x in enumerate(read(rel)):
 ids=[zone_by_name[norm(z)] for z in x['zones']]
 put(x['id'],'venue_zone_ids',ids,rel,f'/{i}/zones','exact source zone labels -> existing zone IDs; no additional compatibility/installation claim')
# Search aliases: use the existing dictionary only when target identity is unique.
rel='data/curated/game_title_aliases.jsonl';raw_aliases=read(rel);owners=collections.defaultdict(set)
for rid,r in rs.items():
 if r['kind']=='game':
  for a in r['aliases']['th']+r['aliases']['en']+list((value(r,'title') or {}).values()):
   if a:owners[norm(a)].add(rid)
for x in raw_aliases:
 for a in x['aliases']:owners[norm(a)].add(game(x['game']))
for i,x in enumerate(raw_aliases):
 rid=game(x['game']);existing=set(rs[rid]['aliases']['th']+rs[rid]['aliases']['en'])
 for j,a in enumerate(x['aliases']):
  if a in existing:continue
  n=norm(a);reason=None
  if len(owners[n])!=1:reason='ambiguous_across_game_profiles'
  elif len(n)<3:reason='too_short_for_safe_identity'
  elif n in {'csgo','csgo2','csgoไทย','ซีเอสโก้'}:reason='historical_title_or_different_release_requires_review'
  if reason:skipped.append({'source':rel,'row':i,'alias':a,'record_id':rid,'reason':reason});continue
  lang='th' if re.search('[\u0e00-\u0e7f]',a) else 'en';rs[rid]['aliases'][lang].append(a);existing.add(a)
  item={'record_id':rid,'language':lang,'alias':a,'source_path':rel,'locator':f'/{i}/aliases/{j}'};aliases_added.append(item)
  changes[rid]['_aliases']=rs[rid]['aliases']
# Preserve the original inventory verification boundary separately from live booking.
rel='data/curated/service_game_availability.jsonl'
for i,x in enumerate(read(rel)):
 put(x['id'],'inventory_verified_on',x['last_verified_at'],rel,f'/{i}/last_verified_at')
 put(x['id'],'inventory_basis',loc('หน้าจองทางการและภาพหน้าจอที่ผู้ใช้ให้ตามต้นฉบับ',x['verified_by']),rel,f'/{i}/verified_by','source wording; no new verification performed')
# Explicit hardware descriptions permit a device category without assigning serial units.
types=['pc','display','peripheral','peripheral','peripheral','furniture','wheel','peripheral','furniture','peripheral','console','console','vr','display','display','furniture']
rel='data/curated/equipment_item_details.jsonl'
for i,(x,t) in enumerate(zip(read(rel),types,strict=True)):put(x['id'],'device_type',t,rel,f'/{i}/what_th','classify explicit device description; no physical-unit or model-spec inference')
# The canonical rule classifier already contains draft topic metadata. Copy only
# exact same document + text matches. Completeness and dependencies remain unknown.
rel='data/competition_rules/canonical/competition_rule_records.jsonl'
for i,x in enumerate(read(rel)):
 cid='competition_'+x['rulebook_id'];targets=[r for r in rs.values() if r['kind']=='competition_rule' and value(r,'competition_id')==cid and (value(r,'text') or {}).get('th')==x['content_th']]
 if len(targets)!=1:skipped.append({'source':rel,'row':i,'reason':'nonunique_clause_identity','matches':[r['record_id'] for r in targets]});continue
 facet_map={'rulebook_identity':'identity','registration':'eligibility_registration','team_size':'roster_composition','map_pool':'match_configuration','match_settings':'match_configuration','equipment':'pre_match_on_site','schedule':'pre_match_on_site','disconnect':'in_match_operations','pause_timeout':'in_match_operations','conduct':'fair_play_conduct','penalty':'penalty_matrix','dispute':'protest_dispute'}
 put(targets[0]['record_id'],'facet',facet_map.get(x['facet'],x['facet']),rel,f'/{i}/facet','legacy draft classifier -> common topic taxonomy for exact same clause; metadata only, not a completeness approval')
rel='data/competition_rules/competition_rule_documents.jsonl'
for i,x in enumerate(read(rel)):
 rid='competition_'+x['id'];old=value(rs[rid],'source_title')
 # R67 accidentally used the overview chunk title in this document-title slot.
 en={'Counter-Strike 2':'Competition Rules and Format for Counter-Strike 2','VALORANT':'Competition Rules and Format for VALORANT','Arena of Valor (RoV)':'Blueket Games 2025 Competition Rules','Tekken 8':'Tekken 8 Competition Rules and Format — PSU Esports ปะทะมันส์ สนั่นจอ'}[x['game']]
 put(rid,'source_title',loc(x['title'],en),rel,f'/{i}/title','actual document title replaces overview chunk heading; original revision retained',replace=True)
 if 'ประเภททีมชาย' in x['tournament']:put(rid,'division',loc('ประเภททีมชาย','Men’s team division'),rel,f'/{i}/tournament','explicit division in source tournament title')
# Existing FAQ facts also belong in owner-editable typed facility/contact fields.
rel='data/curated/user_service_facts_20261008.json';claims=read(rel)['claims']
put('center_psu_phuket','description',claims['university']['answers'],rel,'/claims/university/answers')
put('center_psu_phuket','timezone','Asia/Bangkok','app/calendar/service_calendar.py','/text','literal configured BANGKOK_TZ; not inferred from schema enum')
for key,name,location in [('parking',loc('ที่จอดรถ','Parking'),loc('หน้าตึก 5','In front of Building 5')),('rest_seating',loc('ที่นั่งพัก','Rest seating'),loc('โซนกลางห้อง','Central area of the room'))]:
 rid='facility_'+key;rec('facility',rid);rs[rid]['aliases']={l:[name[l]] for l in ('th','en')}
 put(rid,'name',name,rel,'/claims/'+key+'/answers','name derived directly from source statement')
 put(rid,'location',location,rel,'/claims/'+key+'/answers','explicit location, no accessible-parking or seating count claim')
 put(rid,'usage_conditions',claims[key]['answers'],rel,'/claims/'+key+'/answers')
rid='contact_studio_facebook';rec('contact',rid);rs[rid]['aliases']={'th':['เพจศูนย์อีสปอร์ต'],'en':['Studio Facebook page']}
put(rid,'channel','facebook',rel,'/claims/contact/answers','explicit Facebook page channel')
put(rid,'value','https://www.facebook.com/psuesportsphuket',rel,'/claims/contact/answers','extract exact URL')
put(rid,'purpose',claims['contact']['answers'],rel,'/claims/contact/answers','retain actual supported contact purpose; no response-time promise')
for key,name,steps in [('change_machine',loc('เปลี่ยนเครื่องที่จองผิด','Change a wrongly booked machine'),[loc('กดยกเลิกผ่านอีเมล','Cancel through the email.'),loc('จองเข้ามาใหม่','Make a new booking.')]),('change_time',loc('เปลี่ยนเวลาจอง','Change the booking time'),[loc('กดยกเลิกผ่านอีเมล','Cancel through the email.'),loc('จองเข้ามาใหม่','Make a new booking.')]),('wrong_slip',loc('แก้การแนบสลิปผิดรูป','Correct an incorrect payment-slip image'),[claims['wrong_slip']['answers']])]:
 rid='procedure_'+key;rec('procedure',rid);rs[rid]['aliases']={l:[name[l]] for l in ('th','en')}
 put(rid,'topic',key,rel,'/claims/'+key,'stable procedure topic from source claim key')
 put(rid,'preconditions',[{'field':'issue','operator':'eq','value':key}],rel,'/claims/'+key,'source claim scope; no universal refund/cancellation permission')
 put(rid,'steps',[{'order':j+1,'instruction':s,'contact_id':'contact_studio_facebook' if key=='wrong_slip' else None} for j,s in enumerate(steps)],rel,'/claims/'+key+'/answers','split only explicitly ordered instructions; preserve complete original FAQ too')
# New records link back from the original FAQ while leaving original answers intact.
for rid,r in list(rs.items()):
 if r['kind']!='faq':continue
 for key,target in [('parking','facility_parking'),('rest_seating','facility_rest_seating'),('contact','contact_studio_facebook'),('change_machine','procedure_change_machine'),('change_time','procedure_change_time'),('wrong_slip','procedure_wrong_slip')]:
  if value(r,'answer')==claims[key]['answers']:
   if value(r,'related_ids') is None:put(rid,'related_ids',[target],rel,'/claims/'+key,'typed relation to the same exact source claim')
# Validate the complete in-memory graph before saving, then save FK targets first.
from app.knowledge.common.registry import schema_errors
pre_errors={rid:schema_errors(r) for rid,r in rs.items() if schema_errors(r)}
if pre_errors:
 dump(B/(db.stem+'_PREVALIDATION_ERRORS.json'),pre_errors)
 raise ValueError('Prevalidation failed; see '+db.stem+'_PREVALIDATION_ERRORS.json')
for rid,fields in sorted(changes.items(),key=lambda item:({'zone':0,'contact':1,'facility':2,'procedure':3,'faq':9}.get(rs[item[0]]['kind'],5),item[0])):
 rows=[x for x in lineage if x['record_id']==rid];alias_rows=[x for x in aliases_added if x['record_id']==rid]
 payload={'mapped_fields':{k:v for k,v in fields.items() if k!='_aliases'},'field_lineage':rows,'alias_lineage':alias_rows,'aliases':rs[rid]['aliases'],'status':'draft_only_not_owner_approved'}
 raw=canonical_json(payload);sid='r68_'+hashlib.sha256((rid+raw).encode()).hexdigest()[:28]
 store.add_source({'source_id':sid,'kind':'derived_curated','path':'migration://r68/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':[rs[rid]['kind']],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None},raw,actor='r68-source-completion')
 for k in fields:
  if k!='_aliases':rs[rid]['fields'][k]['evidence_refs']=[{'source_id':sid,'locator':'/mapped_fields/'+k}]
 rs[rid]['localization']['en_status']='agent_translated'
 store.save(rs[rid],expected_version=before[rid]['revision'] if rid in before else 0,actor='r68-source-completion',change_note='Source-bound format completion; no publication/approval; evidence '+sid)
with store.connect() as c:
 after=store.heads(c);src=store.sources(c);errors={rid:validate(r,after,src) for rid,r in after.items() if validate(r,after,src)}
 assert not errors,errors
 for row in old_rows:assert tuple(c.execute('select * from cc_revisions where record_id=? and version=?',row[:2]).fetchone())==row
 assert all(src[k]==v for k,v in sources_before.items())
 assert [tuple(r) for r in c.execute('select * from cc_approvals')]==old_approvals
 assert dict(c.execute('select key,value from cc_meta')).get('active')==old_meta.get('active')
dump(B/'MIGRATION_LINEAGE.json',lineage);dump(B/'ALIAS_LINEAGE.json',aliases_added);dump(B/'EXCLUDED_REVIEW_ITEMS.json',skipped)
result={'before_heads':len(before),'after_heads':len(after),'changed_records':len(changes),'fields_by_kind':dict(collections.Counter(rs[x['record_id']]['kind']+'.'+x['field'] for x in lineage)),'expanded_full_descriptions':len(full),'added_aliases':len(aliases_added),'excluded_review_items':len(skipped),'schema_errors':errors,'old_revisions_preserved':len(old_rows),'old_sources_preserved':len(sources_before),'new_approvals':0,'active_release_unchanged':True}
dump(B/'MIGRATION_RESULT.json',result);print(json.dumps(result,ensure_ascii=False,indent=2))
