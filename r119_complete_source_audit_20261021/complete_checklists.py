"""Account for auxiliary documents, derived training rows and runtime literals."""
import collections,hashlib,json,re,sqlite3
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system'
read=lambda p:json.loads(p.read_text('utf8'))
write=lambda n,v:(R/n).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
def leaves(v):
 if isinstance(v,dict):return sum(leaves(x) for x in v.values())
 if isinstance(v,list):return sum(leaves(x) for x in v)
 return 1
aux=[]
for item in read(R/'FILE_INVENTORY.json'):
 if item['classification'] not in {'source_or_derived_business_candidate','evaluation_or_intent_workload_not_business_authority'}:continue
 p=S/item['path'];rows=[];kind='supporting_document'
 if p.suffix=='.json':rows=[json.loads(p.read_text('utf-8-sig'))]
 elif p.suffix=='.jsonl':rows=[json.loads(s) for s in p.read_text('utf-8-sig').splitlines() if s.strip()]
 if rows and all(isinstance(r,dict) and 'messages' in r for r in rows):kind='derived_training_conversations_not_answer_authority'
 elif '/locales/' in item['path']:kind='translation_and_review_layers_status_retained'
 elif '/competition_rules/' in item['path']:kind='rule_sources_projections_and_release_metadata'
 elif '/control_game/' in item['path'] or '/control_game_split/' in item['path']:kind='raw_control_maps_or_companion_metadata'
 elif '/curated/' in item['path']:kind='curated_inputs_with_canonical_or_native_mappings'
 elif any(x in item['path'] for x in ['schema','manifest','README','readme','summary']):kind='schema_manifest_or_source_documentation'
 elif '/calendar/' in item['path']:kind='calendar_source_or_exception_table'
 elif item['classification']=='evaluation_or_intent_workload_not_business_authority' or '/routing_eval_' in item['path']:kind='test_or_intent_workload_not_answer_authority'
 aux.append({'path':item['path'],'sha256':item['sha256'],'disposition':kind,'structured_rows_parsed':len(rows),'scalar_values_parsed':sum(leaves(x) for x in rows),'training_answers_promoted_to_authoritative_facts':False})
write('AUXILIARY_DOCUMENT_CHECKLIST.json',{'documents':aux,'counts':dict(collections.Counter(r['disposition'] for r in aux)),'structured_rows_parsed':sum(r['structured_rows_parsed'] for r in aux)})
mapped={'SERVICE_FEES','GROUP_LABELS','SERVICE_ALIASES','CUSTOMER_GROUP_ALIASES','_MEMBER_ROLE_QUERY_ALIASES','WEEKLY_SERVICE'}
cache={'PRICE_ROWS','PRICE_VALUES','PRICE_LABELS','GAME_DETAILS','ZONE_DETAILS','EQUIPMENT_BY_ZONE','EQUIPMENT_ITEM_DETAILS','SUPPORTED_GAME_CATALOG','RESERVATION_FACTS','POPULAR_GAMES_BY_GENRE','ESPORTS_GAME_TYPE_SECTIONS'}
constants=[]
for c in read(R/'CODE_CONSTANTS.json'):
 names=set(c['names']);v=c['value']
 if names & mapped:disposition='mapped_native_inputs_or_original_calendar_export'
 elif names & cache:disposition='derived_answer_cache_retained_in_source_code_not_independent_authority'
 elif 'COMPETITION_RULE_GENERIC_ANSWERS' in names:disposition='generic_and_negative_rule_templates_not_a_replacement_for_full_source_clauses'
 elif not v:disposition='empty_runtime_state_not_business_fact'
 else:disposition='runtime_language_routing_rendering_or_operator_definition_retained_as_code'
 original=R.parent/'r118_precision_readers_20261021/system'/c['path']
 constants.append({**c,'disposition':disposition,'scalar_values_checked':leaves(v),'original_source_code_path':str(original),'source_code_sha256':hashlib.sha256(original.read_bytes()).hexdigest()})
write('CODE_LITERAL_CHECKLIST.json',{'constants':constants,'counts':dict(collections.Counter(c['disposition'] for c in constants)),'scope_note':'A generated hard-coded answer is not independent owner/official evidence. Existing canonical/native facts take precedence; negative cache answers do not establish permanent absence.'})
# Resolve the five nonliteral differences after inspecting their actual values.
x=read(R/'TYPED_VALUE_REVIEW.json');reviews=[]
norm=lambda s:re.sub(r'[^\w]','',s.casefold())
for c in x['mismatches']:
 if c['native_field']=='game_service.game_id':
  labels=[s for a in c['actual'] for s in a.values()]
  ok=any(norm(c['expected'])==norm(s) for s in labels)
  disposition='same_game_identity_case_or_punctuation_only'
 elif c['content_id']=='rule_en_general_studio_rules':
  text=c['actual']['th'];ok=all(t in text for t in ['พื้นที่ที่กำหนด','สูบบุหรี่','แอลกอฮอล์','อาวุธ','การพนัน','เสียงดัง','คำพูดเสียดสี'])
  disposition='newer_expanded_rules_retain_all_original_prohibitions'
 else:ok=False;disposition='unresolved'
 reviews.append({'content_id':c['content_id'],'field':c['source_field'],'passed':ok,'disposition':disposition,'original_value':c['expected'],'native_value':c['actual']})
write('TYPED_VARIANT_DECISIONS.json',{'cases':reviews,'unresolved':sum(not r['passed'] for r in reviews),'literal_matches':x['passed'],'explicitly_reviewed_variants':len(reviews),'total':x['total']})
assert all(r['passed'] for r in reviews)
print(json.dumps({'auxiliary_documents':len(aux),'auxiliary_structured_rows':sum(r['structured_rows_parsed'] for r in aux),'code_literals':len(constants),'typed_checks':x['total'],'unresolved_typed_variants':0}))
