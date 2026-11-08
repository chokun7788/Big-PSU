"""Agent-authored source/causal review, before any 10% inference execution."""
import collections,gzip,hashlib,json,re,sqlite3,time,zlib
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r130_owner_context_completion_20261025';O=P/'full_analysis'
def load(p):return json.loads(p.read_text('utf-8-sig'))
def write(n,x):(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
def lines(p):
 with gzip.open(p,'rt',encoding='utf8') as f:
  for s in f:yield json.loads(s)
source=load(O/'REVIEW_SOURCE_INDEX.json');records=source['records'];prior=load(O/'AGENT_SOURCE_CASE_REVIEW.json')['cases']
deep={x['key']:x for x in lines(R/'DEEP_REVIEW_CASES.jsonl.gz')}
comparison=load(R/'SAVED_DEEP_COMPARISON.json');members=load(R/'CATEGORY_MEMBERSHIP.json')['members'];counts=load(R/'ISSUE_COUNTS.json')
# Existing saved cases inspected against responses, traces and source fields.
# A probable attribution is intentionally not promoted to confirmed content wrong.
extra=[
 ('5070c43c','needs_decomposition','probable','multi_target_collapse','ถามcontrolsของสองเกม แต่แผนเหลือtaskเดียวไม่มีtargetและถามแพลตฟอร์มของเกมนี้แบบเอกพจน์ ข้อมูลมีหลายแพลตฟอร์มจึงอาจต้องถามกลับจริง แต่ยังควรรักษาทั้งสองเกมและตอบส่วนที่ยืนยันได้ ต้องแยกความกำกวมแพลตฟอร์มจากการทำtargetหาย',False,[]),
 ('6efd2228','understanding_and_model_admission','probable','control_typo_then_model_fallback','uttonในคำถามRingFitไม่ถูกกู้เป็นbuttonในnativeframe จึงไปC04แล้วโมเดลไม่พร้อม ข้อมูลcontrolมีอยู่ ต้องตรวจการกู้surfaceคำและสาเหตุadmissionแยกกัน คำตอบคือยังไม่ได้ตอบ ไม่ใช่factเกี่ยวกับปุ่มผิด',False,[]),
 ('adabcf3a','needs_decomposition','probable','booking_typo_and_billing_presentation','คำถามท้ายhow do I booมีแนวโน้มถามbook แต่ไม่ได้เกิดbookingtask ส่วนราคาที่แสดง30นาทีต้องระบุว่าคิดminimumหนึ่งsession60นาทีตามกฎ ไม่สรุปว่าตัวเลขผิดก่อนตรวจbillingrule และคำว่าgeneral visirorยังต้องตรวจaudience',False,[]),
 ('a0092e36','understanding_and_model_admission','probable','person_role_typo_unanswered','ชื่อบุคคลมีในsource แต่rokeไม่ใช่roleตามsurface ระบบไปmodel/admissionแล้วไม่ตอบ ต้องแยกnamebindingจากroleintentและtransport ไม่สรุปว่าไม่มีperson record',False,[]),
 ('ed920c59','model_admission_or_transport','confirmed_event','known_rule_unanswered','ถามconductTekkenที่มีruleclauses แต่terminalmodel_transport_failureและไม่ส่งfactsให้ผู้ใช้ ในsavedlegacycaseนี้ไม่มีคำตอบเช่นกัน จึงไม่ใช้Flowเดิมเป็นครูที่ถูกโดยอัตโนมัติ',False,[]),
 ('94acbf68','evaluation_contract','source_supported','transfer_rule_supported','ข้อห้ามโอนสิทธิ์ตรงFAQและsavedlegacy ภายใต้scopeผู้รับสิทธิ์ภายนอกรายการจอง ไม่ขยายไปห้ามผู้เล่นร่วมที่ลงชื่อถูกต้องอยู่แล้ว คงvalidity/publicationreviewแยก',False,[]),
 ('a36b9e88','understanding','review_required','damage_cause_unspecified','คำถามคอมพิวเตอร์พังกว้าง แต่เลือกpolicyความเสียหายร้ายแรงและชดเชยเต็ม บทความsourceมีจริงและFlowเดิมตอบแบบเดียวกัน ยังต้องแยกสาเหตุผู้ใช้ทำเสียกับเครื่องเสียเองก่อนยืนยันความเหมาะสมของpolicyที่ใช้',False,['migrated_faq_rule_damage_responsibility']),
 ('e19a83ad','rule_reader','probable','rulebook_identity_to_penalty_clause','ถามscopeและidentityเอกสาร แต่ได้sectionบทลงโทษยาว แม้ชื่อรายการถูก ยังไม่เห็นว่าคำถามscopeได้รับคำตอบครบ traceแสดงevent_clause_dependency_readจึงต้องตรวจการเลือกtopic ไม่ใช่ถือsupportedว่าsemanticครบ',False,[]),
 ('dc5e988d','model_admission_or_transport','confirmed_event','rule_procedure_unanswered','ถามขั้นตอนระหว่างแข่งCS2 แต่โมเดลไม่พร้อมและไม่ตอบ ไม่ยืนยันว่าข้อมูลขั้นตอนหายจากterminalนี้',False,[]),
 ('27adcc11','evaluation_contract','source_supported','regular_calendar_no_24h_supported','แม้stdio/openสะกดผิด คำตอบไม่เปิด24ชั่วโมงและตารางบริการตรงsourceFAQ เป็นตัวอย่างข้อที่มีสาระถูกแม้routeต่าง ไม่ยืนยันoccupancyหรืออาคารเปิดจริง',False,[]),
 ('45854a28','constraint_extraction','confirmed','requested_word_number_subset_lost','ถามseven buttons แต่ตอบ14entriesโดยไม่ระบุว่าชุด7ปุ่มยังไม่ยืนยัน ตัวเลข7ในชื่อเกมไม่ใช่จำนวนที่ถาม และคำว่าsevenไม่ถูกเก็บในconstraints การเป็นcomplete_source_binding_setจึงไม่พิสูจน์ว่าครบตามrequest Flowเดิมก็ลิสต์14เช่นกัน ต้องวิจารณ์ทั้งสองฝั่ง',True,['controls_ps5_gran_turismo_7']),
 ('b59d525c','understanding_and_model_admission','probable','price_surface_typo_unanswered','ราคสะกดขาดา ทำให้การอ่านราคาเกมที่สัมพันธ์บริการไม่ทำงานจนไปmodel/admission แม้savedlegacyจับเจตนาและอธิบายgame→serviceได้ ต้องแก้surface/intentโดยไม่ฝังราคาในโมเดล',False,[]),
 ('aaab5190','controlled_live_dependency','confirmed_fixture','live_unavailable_expected','ถามVRเวลาชัดและfixtureถูกควบคุมunavailable การไม่ยืนยันว่างตรงscope Savedlegacyตอบunavailableเหมือนกันแต่clockเก่า จึงไม่ใช่providerจริงล่มหรือFlowใหม่ไม่เชื่อมlive',False,[]),
 ('302d49fb','controlled_live_dependency','confirmed_fixture','live_unavailable_expected','ถามNintendoช่วง14–15จริง เป็นlivefixtureเหมือนold ต่างวันอ้างอิง ต้องรักษาresourceและwindowโดยไม่อ้างผลmockเป็นสถานะจริง',False,[]),
 ('19e27fae','model_admission','confirmed_event','visitor_eligibility_unanswered','มีsourceการใช้บริการทั่วไปของคนนอก แต่requestนี้จบretryจากr101_model_unavailable ไม่ใช่sourceยืนยันว่าคนนอกใช้ไม่ได้ ยังต้องตรวจreadereligibilityก่อนfallback',False,['r114_q037_owner_policy']),
 ('21cdc3f6','controlled_live_dependency','confirmed_fixture','live_unavailable_expected','ถามCockpitตอนนี้ตรงlivepathและไม่ยืนยันslotจากfixtureoffline เหมาะกับเงื่อนไขทดสอบ ไม่ใช่คะแนนความพร้อมproviderจริง',False,[]),
 ('f83e7aa6','controlled_live_dependency','confirmed_fixture','live_unavailable_expected','วันที่พรุ่งนี้คำนวณจากfixedclock2026-10-16เป็น10-17 ไม่เท่ากับวันนี้ที่ตรวจ และไม่ถือsavedlegacyที่clock10-14เป็นคำตอบวันที่ที่ต้องเลียนแบบ',False,[]),
 ('6b55634a','model_admission_or_transport','confirmed_event','organizer_equipment_unanswered','sourceCS2section043ระบุPC/จอ/หูฟังไมค์/โต๊ะ/เก้าอี้ครบ แต่readerจบmodel_transport_failure savedlegacyเลือกclauseนี้ตรงคำถาม ตรวจแล้วเป็นsourceมีแต่การอ่านไม่สำเร็จ ไม่ใช่metadatawronggameทุกแถว',False,['competition_competition_rules_cs2_psu_phuket_2026_section_043']),
 ('f3055a6d','evaluation_contract','source_supported','refund_source_supported','ข้อความrefundและข้อยกเว้นcenterfaultตรงsourceกับsavedlegacyในคำถามทั่วไปนี้ แต่ไม่ถือว่าครอบทุกscenarioเครดิต/โอนเกิน/เลื่อนวัน',False,[]),
 ('439fa27a','evaluation_contract','source_supported','exact_control_source_supported','L3ของModernWarfareIIIตรงbindingในsourceและsavedlegacy พร้อมคำเตือนsecondarysource/installedpreset ข้อroutefailไม่ใช่ข้อผิดด้านปุ่ม',False,[]),
 ('9749c57f','predicate_selection','confirmed','damage_question_replaced_with_inventory','ถามชดเชยความเสียหายgamingmouse แต่fallbackเลือกequipmentinventoryPCzone ไม่ตอบความรับผิดชอบ แม้factsรายการอุปกรณ์ถูกต้อง มีกฎdamage_responsibilityในsourceและsavedlegacyตอบตรง predicate ต้องตรวจactionก่อนหยิบชื่ออุปกรณ์',True,['migrated_faq_rule_damage_responsibility']),
 ('000520a4','evaluation_contract','source_supported','person_role_source_supported','ชื่อและroleตรงrecord/sourceและsavedlegacy ไม่อ้างสถานะดำรงตำแหน่งปัจจุบันนอกvalidityที่ยืนยัน',False,[]),
 ('b72e8ca2','entity_binding','review_required','unverified_person_transliteration','ชื่ออังกฤษNattaponTongthesไม่ตรงชื่อที่ยืนยัน การถามชื่อที่แน่นอนมีเหตุผล Savedlegacyก็ไม่รับรองคนนี้ จึงไม่ควรบังคับจับชื่อใกล้เพื่อให้ผ่านgold ข้อความถามเกม/เครื่องเป็นUXไม่ตรงdomain',False,[]),
 ('934b6162','entity_binding_then_intent_override','confirmed','thai_substring_booking_to_monitor','จอในจองจับaliasจอภาพ ทำให้native_inventory_presence_recordเลือกequipmentusage แล้วตอบGamingMonitorแทนสิทธิ์คนนอกจอง มีกฎr114_q037_owner_policyยืนยันบริการทั่วไป และsavedlegacyตอบeligibilityตรงเรื่อง เป็นsource/predicatefailureที่ทำงานก่อนเรียกโมเดล',True,['r114_q037_owner_policy','equipment_gaming_monitor']),
 ('22b8cace','no_confirmed_failing_stage','review_required','operator_or_manager_ambiguity','Who manages the studioอาจถามหน่วยงานหรือบุคคล ระบบกับsavedlegacyตอบCollegeofComputingเหมือนกันและsourceรองรับoperator จึงยังไม่ตัดสินผิดคนโดยไม่มีบริบทเพิ่ม',False,[]),
 ('5f7c8623','service_scope_selection','confirmed','offsite_rental_wrong_clarification','ผู้ใช้ระบุnotebookกลับบ้าน แต่ถามต่อว่าจะเหมาโซนใด แสดงว่าoffsiteequipmentถูกเปลี่ยนเป็นonsitevenueแม้ยังไม่ให้ราคา ไม่มีsourceให้สรุปบริการเช่ากลับบ้าน ควรบอกส่วนที่ไม่ยืนยันตรงitem',True,[]),
 ('3f00783c','model_admission_or_transport','confirmed_event','zone_game_recommendation_unanswered','คำว่าเหมาะเป็นrecommendationไม่ใช่เหมา sourceยังต้องแยกรายการ/genreจากคำแนะนำที่ยืนยัน การไม่ตอบในrequestนี้เป็นmodel_transport_failure ไม่ใช้เป็นหลักฐานว่าrentalreaderขาด',False,[]),
 ('94170c02','evaluation_contract','source_supported','wrong_slip_owner_source_supported','คำตอบส่งสลิปทางเพจตรงownerclaimและsavedlegacy ใช้URLตามsource ไม่ได้ตรวจavailabilityของFacebookสด',False,[]),
]
# A previous deterministic category-card scan selected only 28 additional cases.
# Explicit statements above remain the human review record, not inferred labels.
needed={}
for prefix,*rest in extra:
 key=next(k for k in deep if k.startswith(prefix));needed[key]=(prefix,*rest)
guard=[]
for row in lines(R/'CASE_DIAGNOSTICS.jsonl.gz'):
 if any(i['code']=='substantive_clause_guard_rejected_claim' for i in row['observed_issues']):guard.append(row)
extra_keys=set(needed)|{x['key'] for x in guard}
for p in sorted((P/'full01').glob('RESULTS_*.jsonl.gz')):
 for row in lines(p):
  if row['key'] in extra_keys:deep[row['key']]=row
legacy=sqlite3.connect((R.parent/'r65_detailed_failure_analysis_20261014/evidence.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
for k in extra_keys-set(comparison['legacy']):
 row=json.loads(zlib.decompress(legacy.execute("select raw from results where arm='legacy_llm' and key=?",(k,)).fetchone()[0]));res=row.get('result') or {}
 comparison['legacy'][k]={'answer':res.get('answer'),'hits':res.get('hits'),'trace':res.get('trace'),'mode':res.get('mode'),'exception':row.get('exception')}
first_stage={'db84ae34':'meaning_to_resource_scope','0c25d981':'native_policy_precedence','eede3e9b':'substantive_verifier','41bef879':'needs_decomposition_then_verifier','cc40820b':'rule_clause_selection','f6a75fef':'entity_binding','7e3ed641':'static_vs_live_intent_gate','b9fa6734':'binding_to_ambiguity_reconciliation','21fe7ed0':'shared_event_scope','bf6817cf':'team_vs_game_mode_predicate','4dc69c73':'cancellation_actor_and_polarity','f44d6445':'public_phrase_vs_person_entity','4a52eaf2':'offsite_vs_onsite_scope','864bd598':'competition_predicate_to_procedure','06563f1a':'substantive_verifier','ed0be633':'billing_labels_and_compiled_scope'}
adjudicated={}
for old in prior:
 x=dict(old);prefix=x['key'][:8];x.update(first_failing_stage=first_stage.get(prefix,'no_confirmed_failing_stage_or_separate_evaluation_issue'),root_cause_confidence='confirmed_source_case' if x['confirmed_actual_content_failure'] else 'see_individual_decision',root_cause_code=first_stage.get(prefix,x['decision']),review_origin='R130_source_review_reused')
 adjudicated[x['key']]=x
for key,(_,stage,confidence,code,diag,actual,additional) in needed.items():
 row=deep[key];res=row['result'];a=res['decision_artifact'];ids=list(dict.fromkeys([*(a.get('query_plan') or {}).get('record_ids',[]),*additional]))
 adjudicated[key]={'key':key,'question':row['question'],'answer':res['answer'],'decision':'confirmed_actual_content_failure' if actual else confidence,'confirmed_actual_content_failure':actual,'first_failing_stage':stage,'root_cause_confidence':confidence,'root_cause_code':code,'diagnosis_th':diag,'source_record_ids':ids,'review_origin':'R131_additional_source_case_review','repair_and_acceptance':'แก้ต้นเหตุที่ระบุ แล้วตรวจpredicate/target/conditions/sourceด้วยเคสเดิม ไม่ปิดจากrouteหรือJSONเพียงอย่างเดียว'}
for item in guard:
 key=item['key']
 if key in adjudicated:continue
 proof=next(i['proof'] for i in item['observed_issues'] if i['code']=='substantive_clause_guard_rejected_claim');ids=sorted({x['record_id'] for x in proof['receipts']})
 adjudicated[key]={'key':key,'question':item['question'],'answer':item['delivered_answer'],'decision':'confirmed_actual_content_failure','confirmed_actual_content_failure':True,'first_failing_stage':'substantive_verifier','root_cause_confidence':'confirmed_source_and_trace','root_cause_code':'full_rule_text_equals_heading_false_rejection','diagnosis_th':'ตรวจsourceและtraceแล้ว clause033/045/046/058มีสาระตอบtechnicalpause/settings/macro/protestตรงคำถาม แต่substantive guardปฏิเสธเพราะvalueเท่ากับlabel ทำให้ตัดคำตอบทิ้ง ทุกkeyนี้อ่านคำถามและข้อความsourceแยกแล้ว ไม่อนุมานจากreasoncodeเพียงอย่างเดียว','source_record_ids':ids,'review_origin':'R131_all_13_guard_cases_source_review','repair_and_acceptance':'สาระประโยคกติกาเต็มต้องผ่านแม้เป็นheadingด้วย และต้องตอบconditions/time/actorครบตามแต่ละคำถาม'}
proof=load(R/'DETERMINISTIC_CAUSAL_PROBES.json');assert proof['model_http_calls']==0 and proof['source_before_matches']
source_bundle={};source_ids=set()
for key,x in adjudicated.items():
 row=deep[key];res=row['result'];a=res.get('decision_artifact') or {}
 x['question_needs_evidence']={'question':row['question'],'frozen_plan_tasks':(a.get('understanding') or {}).get('tasks',[]),'plan_is_not_independent_semantic_gold':True,'human_need_and_scope_review_th':x['diagnosis_th']}
 x['observed_answer_trace']={'response_type':a.get('response_type'),'query_plan':a.get('query_plan'),'tasks':(a.get('execution_contract') or {}).get('tasks',[]),'understanding':a.get('understanding')}
 old=comparison['legacy'].get(key) or {};x['saved_legacy']={'answer':old.get('answer'),'exception':old.get('exception'),'mode':old.get('mode'),'source_hits':old.get('hits'),'meaningful_trace':[t for t in old.get('trace') or [] if t.get('stage')!='timing'][:14],'baseline_new_inference':False,'not_automatic_current_truth':True}
 x['saved_r95_answer']=(comparison['r95'].get(key) or {}).get('answer')
 x['sampling_categories']=members[key]['categories'];x['severity']='high' if x['confirmed_actual_content_failure'] else 'review_or_mechanism'
 x['source_evidence']=[]
 for rid in x.get('source_record_ids',[]):
  if rid not in records:continue
  rec=records[rid];selected={f:v for f,v in rec['fields'].items() if v.get('status')=='known' and f!='legacy_context'};source_bundle[rid]={'record_id':rid,'revision':rec['revision'],'kind':rec['kind'],'validity':rec.get('validity'),'lifecycle':rec.get('lifecycle'),'fields':selected}
  for f,v in selected.items():
   source_ids.update(e['source_id'] for e in v.get('evidence_refs',[]))
   if f in ['answer','text','specifications','role','installed_resource_ids','source_coverage','limitations','bindings']:
    x['source_evidence'].append({'record_id':rid,'revision':rec['revision'],'field':f,'value':v['value'],'refs':v.get('evidence_refs',[])})
write('INDIVIDUAL_SOURCE_REVIEW.json',{'cases':list(adjudicated.values()),'unique_requests':len(adjudicated),'confirmed_actual_content_failure_examples':sum(x['confirmed_actual_content_failure'] for x in adjudicated.values()),'exhaustive_semantic_adjudication':False,'unreviewed_requests':20554-len(adjudicated),'semantic_accuracy':None,'no_baseline_rerun_or_regrading':True})
con=sqlite3.connect((P/'system/data/knowledge/common.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
snapshots={}
for sid in source_ids:
 row=con.execute('select payload,snapshot from cc_sources where source_id=?',(sid,)).fetchone()
 assert row,sid;snapshots[sid]={'metadata':json.loads(row[0]),'snapshot':json.loads(row[1]),'raw_snapshot_sha256':hashlib.sha256(row[1].encode()).hexdigest()}
write('SOURCE_CAUSAL_EVIDENCE.json',{'records':source_bundle,'sources':snapshots,'read_only_source':True,'logical_snapshot_digest':proof['source_logical_digest']})
with gzip.open(R/'CASE_DIAGNOSTICS_REVIEWED.jsonl.gz','xt',encoding='utf8') as out:
 for row in lines(R/'CASE_DIAGNOSTICS.jsonl.gz'):
  key=row['key'];case=adjudicated.get(key)
  if case:
   row.update(first_failing_stage=case['first_failing_stage'],semantic_adjudication=case['decision'],confirmed_actual_content_failure=case['confirmed_actual_content_failure'],root_cause_code=case['root_cause_code'],root_cause_confidence=case['root_cause_confidence'],diagnosis_th=case['diagnosis_th'],severity=case['severity'])
   row['expected_and_delivered_sources']['agent_confirmed_source_records']=case['source_record_ids']
  # Preserve unreviewed semantics; observed transport/contract evidence is separate.
  row['earliest_observed_mechanism_stages']=sorted({x['stage'] for x in row['observed_issues'] if x['stage']!='evaluation_contract'})
  out.write(json.dumps(row,ensure_ascii=False)+'\n')
roots=collections.defaultdict(list)
for x in adjudicated.values():roots[x['root_cause_code']].append(x['key'])
write('ROOT_CAUSE_REGISTER.json',{'root_groups':{k:{'individually_reviewed_unique_keys':v,'confirmed_content_failure_count':sum(adjudicated[key]['confirmed_actual_content_failure'] for key in v)} for k,v in roots.items()},'observed_mechanism_cohorts_reference':'ISSUE_COUNTS.json','do_not_treat_entire_cohort_as_same_confirmed_semantic_cause':True})
allocation=load(R/'SAMPLE_ALLOCATION.json')
doc=['# ข้อ2 — วินิจฉัยต้นเหตุจากผลเดิมก่อนทดสอบ10%','',
 'เอกสารนี้ทำก่อนsample01เริ่ม ไม่มีการแก้runtime/data/weights/prompt และยังไม่อ้างว่าปัญหาถูกแก้หรือคุณภาพดีขึ้น ขอบเขต76หัวข้อ/14หมวดเดิมคงไว้','',
 f"อ่านผลเดิมครบ20,554requests/55,811grades และทำcase ledgerทุกkey เพิ่มการตรวจsource/traceรายกรณีจาก34เป็น{len(adjudicated)}คำถาม ยืนยันตัวอย่างcontent/scope/omissionfailureได้{sum(x['confirmed_actual_content_failure'] for x in adjudicated.values())}คำถาม ส่วนที่ยังไม่ตัดสินคงreview_required ไม่คิดsemanticaccuracyจากตัวอย่าง",'',
 '## แยกความมั่นใจของหลักฐาน','',
 '- confirmed mechanism: มีtraceหรือcode-pathยืนยันเหตุที่เกิด เช่นHTTPtimeout/schema reject/verifierตัดclaim แต่ไม่รับรองว่าทุกคำตอบผิด','- confirmed content/scope/omission: agentตรวจคำถาม คำตอบ และsourceรายkeyแล้ว','- probable: มีหลักฐานเข้าทางสาเหตุ แต่ยังขาดcounterfactualหรือรายละเอียดbindingบางส่วน','- review_required: คงความไม่แน่ชัด เช่นpolicyequivalence, billing, ชื่อทับศัพท์ และข้อที่sourceยังไม่ยืนยัน','',
 '## สิ่งที่ทราบลึกกว่ารายงานเดิม','',
 '1. GPUไม่ได้หาย: จอในคำว่าการ์ดจอจับmonitor; เครื่องPCซึ่งยาวกว่าpcเลือกservicecapacityและกีดกันequipmentPC; poolไม่ว่างจึงไม่เข้าfallback device_type สองจุดร่วมกันทำให้ไม่เห็นGPUที่มีจริง','2. จอในคำว่าจองยังทำให้คำถามสิทธิ์คนนอกถูกตีเป็นinventorypresenceแล้วตอบวิธีใช้monitor เป็นข้อผิดก่อนโมเดล ไม่ใช่โมเดล4Bตอบไม่ได้เพียงเหตุเดียว','3. CS2streamคำถามแข่งไม่matchsourceclauseชัดก่อน แล้วnativepolicyfallbackเลือกstudio streamingก่อนmeaningreviewที่ควรคงcompetition scope','4. splitคำถามVALORANTแยกอาหารออกจากevent จึงส่งไปC10และทิ้งกฎเฉพาะการแข่งขัน','5. ตรวจsubstantive guardครบ13keys: source033/045/046/058มีสาระครบแต่textซ้ำheading จึงตัดทิ้ง รวมข้อหยุดเทคนิคและประท้วง ไม่ใช่แค่settingsตัวอย่างเดียว','6. seven buttonsของGranTurismoถูกทิ้งconstraint แล้วตอบ14entriesโดยledgerบอกsupported Savedlegacyก็มีปัญหาเดียวกัน จึงต้องตรวจครูกับsource ไม่เลียนแบบทั้งหมด','7. คำถามชดเชยmouseกลับตอบinventoryPCzone แสดงการจับentityแล้วละpredicate แม้ไม่มีmodelreplyที่ผ่าน','8. ผลsavedlegacyยืนยันแนวทางบางข้อ เช่นPC10/game→resource, GPU+ข้อจำกัดsource, CS2clauseเต็ม และoffsite rentalปฏิเสธตรงitem แต่บางkeysเดิมมีexception/ไม่มีคำตอบ จึงไม่ถือlegacyถูกทุกข้อ','',
 '## จำนวนอาการจากtraceทั้งชุด — กลุ่มซ้อนทับและไม่ใช่จำนวนตอบผิดทั้งหมด','',
 '| กลุ่มหลักฐาน | unique requests | ข้อจำกัดคำตัดสิน |','|---|---:|---|']
for code,group in sorted(counts['groups'].items(),key=lambda kv:-kv[1]['unique_requests']):doc.append(f"| {code} | {group['unique_requests']} | confirmed event/terminalตามชนิด; semanticต้องดูรายkey |")
doc+=['','ค่าจำนวนอาจต่างจากR130auto reportเพราะรอบนี้ตรวจunderstanding.eventบนcompatibility pathด้วย และนับunique requestsแยกจากevent/grade occurrences: schema rejectionพบ237requests เทียบ162ที่รายงานเดิมนับเฉพาะdomain_flow.model_events ทั้งสองนิยามเก็บไว้ ไม่เขียนทับผลเดิม ส่วนlatencyในledgerนี้ตรวจคำว่าlatencyตรงassertionจึง376ไม่ใช่performance388ที่รวมtimeoutด้วย','',
 '## ตารางสาเหตุและหลักฐานรายกรณี','']
for i,x in enumerate(adjudicated.values(),1):
 old=x['saved_legacy'];doc += [f"### {i}. {x['question']}",'',f"Key `{x['key']}` — first stage `{x['first_failing_stage']}`; confidence `{x['root_cause_confidence']}`; decision `{x['decision']}`",'', 'คำตอบR130:\n\n'+x['answer'][:1400],'','สาเหตุ: '+x['diagnosis_th'],'','คำตอบsavedlegacy (excerpt; ไม่ใช่คำตัดสินว่าถูกปัจจุบัน):\n\n'+str(old.get('answer'))[:1100],'',f"Legacy exception: `{old.get('exception')}`; mode: `{old.get('mode')}`",'']
 for ev in x['source_evidence'][:5]:doc.append(f"- `{ev['record_id']}` rev{ev['revision']}.{ev['field']}: "+json.dumps(ev['value'],ensure_ascii=False)[:1000]+' — '+json.dumps(ev['refs'],ensure_ascii=False))
 doc.append('')
doc+=['## ลำดับแก้ที่ได้จากการวินิจฉัย','',
 'เริ่มbindingและpredicate gateที่ให้sourceผิดเรื่อง, แก้C13scope/clause/verifier, reconcileanaphorและconstraints, แล้วแก้protocol/admission/latencyควบคู่กับsourceauthorityที่ยังreview แต่ละงานต้องมีcaseและacceptance ไม่แก้จากชื่อterminalเพียงอย่างเดียว งานรอบนี้ยังเป็นวินิจฉัยจึงไม่เปลี่ยนfrozenR130','',
 '## แผน10%ที่ตรึงก่อนยิงคำถาม','',f"เลือก{allocation['sample_requests']}unique requests/{allocation['sample_grades']}gradesจากFULL_JOBSเดิม 10%ปัดขึ้นทุกoriginalstratumและเติมหมวดตามinputให้ครบC01–C14 ไม่มีคำถามใหม่ ไม่เลือกตามคะแนน/ผลตอบ ได้มากกว่า10%บางหมวดเพราะการปัดขึ้น/คำถามหลายหมวด",'',
 '| หมวด | ประชากรตามinput | จำนวนที่เลือกในหมวด | หมายเหตุ |','|---|---:|---:|---|']
for a in allocation['categories']:doc.append(f"| {a['category']} {a['name_th']} | {a['population']} | {a['actual_selected']} | membershipsซ้อนทับได้ |")
doc+=['','ข้อจำกัดสำคัญ: C07มีเพียง6คำถามในfullinputเดิมและส่วนใหญ่ถามoffsite; เลือก1ตามceil10%ยังไม่ยืนยันคุณภาพราคาเหมาonsiteทั้งหมด C14ไม่มีrealnewsrecords การไม่ยืนยันข้อมูลล่าสุดต้องแยกจากreaderเสีย ไม่อ้างว่าทั้ง14หมวดผ่านเพราะมีsample','',
 'sample01จะใช้R130เดิม/retained/base/2workers/clock/budget/livefixtureเดิม เป็นการตรวจความเกิดซ้ำและความต่างของdiagnostic ไม่ใช่post-fix improvementหรือfreshholdout ไม่มีlegacy inference/regradingใหม่','',
 '## หลักฐาน','', '- CASE_DIAGNOSTICS_REVIEWED.jsonl.gz: ทุก20,554keysพร้อมobservedmechanismsและsemanticstatusที่ไม่เดา','- INDIVIDUAL_SOURCE_REVIEW.json: คำตัดสินรายกรณี/firststage/confidence/source/savedoldtrace','- SOURCE_CAUSAL_EVIDENCE.json: source77+recordsตามcaseและbody/locator/revision','- DETERMINISTIC_CAUSAL_PROBES.json:8localcodeprobes ไม่มีHTTP/model requests','- ROOT_CAUSE_REGISTER.json / ISSUE_COUNTS.json: สาเหตุที่reviewแล้วแยกจากcohortอาการทั้งหมด','- SELECTION_FREEZE.json / SAMPLE_ALLOCATION.json: วิธีเลือกและhashก่อนทดสอบ','', 'การทำข้อ2ระดับวินิจฉัยทุกกลุ่มและcase ledgerครบ ไม่เท่ากับsemanticjudgmentทุก20,554คำตอบ รายการที่ยังไม่ยืนยันคงreview_required และไม่ประกาศFlowครบ100%']
(R/'ITEM02_DETAILED_DIAGNOSIS_TH.md').write_text('\n'.join(doc)+'\n','utf8')
write('DIAGNOSIS_PRETEST_COMPLETE.json',{'complete':True,'scope':'full-case mechanism ledger + expanded individual source/causal review before retest','requests_streamed':20554,'grades_streamed':55811,'individual_source_cases':len(adjudicated),'confirmed_content_failure_examples':sum(x['confirmed_actual_content_failure'] for x in adjudicated.values()),'all_13_substantive_rejection_cases_source_reviewed':True,'deterministic_causal_probes':8,'source_unchanged':True,'runtime_fixes':0,'new_model_or_baseline_inferences':0,'exhaustive_semantic_adjudication':False,'semantic_accuracy':None,'report_sha256':hashlib.sha256((R/'ITEM02_DETAILED_DIAGNOSIS_TH.md').read_bytes()).hexdigest(),'completed_at_unix':time.time()})
write('STATUS.json',{'phase':'item02_detailed_diagnosis_complete_ready_for_authorized_10pct','diagnosis_before_retest':True,'source_cases':len(adjudicated),'sample_requests':allocation['sample_requests'],'sample_grades':allocation['sample_grades'],'complete':False,'production_installed':False,'updated_at':time.time()})
print(json.dumps({'source_cases':len(adjudicated),'actual_content_failure_examples':sum(x['confirmed_actual_content_failure'] for x in adjudicated.values()),'diagnosis_gate_complete':True,'report_bytes':(R/'ITEM02_DETAILED_DIAGNOSIS_TH.md').stat().st_size},ensure_ascii=False))
