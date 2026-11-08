"""Record explicit source judgements for the related cases read by the agent.
Does not bulk-label the separate 36-case tournament-policy candidate cohort.
"""
import hashlib,json,sqlite3,time,zlib
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r130_owner_context_completion_20261025'
def load(p):return json.loads(p.read_text('utf-8-sig'))
cohorts=load(R/'RELATED_TRACE_COHORTS.json')['cohorts'];records=load(P/'full_analysis/REVIEW_SOURCE_INDEX.json')['records']
assign={
 'tekken_format_to_document_title':('rule_clause_selection','ถามรูปแบบการแข่งขันแต่ได้ชื่อเอกสารอย่างเดียว ไม่ส่งOffline/PS5/1v1/FT2/R3/60Sในsection002 แม้sourceมีครบ อ่านคำถามทุกwrapper/typoใน29keysแล้วว่าขอformatจริง',['competition_competition_rules_tekken8_psu_esports_section_001','competition_competition_rules_tekken8_psu_esports_section_002']),
 'thai_substring_monitor_leak':('entity_binding_then_intent_override','คำว่าจองทำให้aliasจอภาพรั่วเข้าrequest แล้วตอบmonitorusage/locationแทนeligibility/วันจอง/ระบบออนไลน์ อ่านทั้ง10คำถามแล้วไม่มีการขอข้อมูลจอจริง; กรณีURLยังต้องตรวจnativeURLsourceเพิ่ม แต่PCZoneไม่ตอบสถานที่ของระบบออนไลน์',['equipment_gaming_monitor','r114_q037_owner_policy','migrated_schedule_0']),
 'damage_to_inventory':('predicate_selection_in_compatibility_fallback','ทั้ง10คำถามถามความรับผิดชอบเมื่อผู้ใช้ทำmouse/chairเสีย แต่ได้รายการอุปกรณ์PCzone ไม่มีคำตอบcompensation แม้sourcepolicyมีเงื่อนไขการชดเชย ไม่อนุมานค่าปรับตายตัวก่อนรู้ระดับความเสียหาย',['migrated_faq_rule_equipment_pc_zone','migrated_faq_rule_damage_responsibility']),
 'static_catalog_to_live':('static_vs_live_intent_gate','ทั้ง2คำถามขอรายการเกมในCockpitไม่มีวันที่หรือslot แต่ได้liveunavailable Sourcegame_serviceยืนยันGranTurismo7 ไม่ต้องรอprovideroccupancy',['migrated_link_availability_cockpit_01_02_game_detail_gran_turismo_7']),
 'resolved_binding_still_ambiguous':('binding_to_ambiguity_reconciliation','ทั้ง2คำถามitมีantecedentTekken8และcompilerผูกcontrolrecordแล้ว แต่ยังถามWhichgameซ้ำ คงplatformambiguityได้ถ้าจำเป็น แต่ไม่ควรทำidentityที่ผูกแล้วหาย',['controls_ps5_tekken_8'])}
legacy=sqlite3.connect((R.parent/'r65_detailed_failure_analysis_20261014/evidence.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
cases=[]
for name,(stage,diagnosis,ids) in assign.items():
 for x in cohorts[name]['cases']:
  raw=legacy.execute("select raw from results where arm='legacy_llm' and key=?",(x['key'],)).fetchone();assert raw
  old=json.loads(zlib.decompress(raw[0]));res=old.get('result') or {}
  cases.append({**x,'semantic_status':'agent_source_confirmed_scope_or_omission_failure','confirmed_actual_content_failure':True,'first_failing_stage':stage,'root_cause_group':name,'diagnosis_th':diagnosis,'source_records':[{'record_id':rid,'revision':records[rid]['revision'],'fields':{k:v for k,v in records[rid]['fields'].items() if k in ['text','answer','installed_resource_ids','game_id','service_id','usage','location','service_periods','bindings'] and v.get('status')=='known'}} for rid in ids],
   'saved_legacy_answer':res.get('answer'),'saved_legacy_exception':old.get('exception'),'saved_legacy_mode':res.get('mode'),'saved_legacy_trace_excerpt':[t for t in res.get('trace') or [] if t.get('stage')!='timing'][:10],'source_hash_context':'R130 frozen logical snapshot 6db199b4251f1805b2698d359efcf290254072665fafa394dceab32dec760480','reviewed_after_initial_diagnosis_gate':True,'new_assistant_or_model_requests':0})
prior=load(R/'INDIVIDUAL_SOURCE_REVIEW.json')['cases'];gpu=load(R/'POST_GATE_GPU_CAUSAL_REFINEMENT.json')['cases']
all_keys={x['key'] for x in prior}|{x['key'] for x in gpu}|{x['key'] for x in cases}
bad={x['key'] for x in prior if x['confirmed_actual_content_failure']}|{x['key'] for x in gpu}|{x['key'] for x in cases}
out={'created_at':time.time(),'cases':cases,'related_source_cases_reviewed':len(cases),'total_unique_keys_source_reviewed_or_causally_probed':len(all_keys),'confirmed_scope_content_omission_examples_total':len(bad),'confirmed_bad_keys':sorted(bad),'remaining_semantic_unadjudicated':20554-len(all_keys),'semantic_accuracy':None,'tournament_policy_36_cohort_not_bulk_adjudicated':True,'all_counts_unique_request_keys_not_grades':True,'new_model_requests':0}
(R/'POST_GATE_RELATED_SOURCE_REVIEW.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
doc=['# รายกรณีที่ตรวจเพิ่มจากcohortหลักฐาน','',f"อ่านsource/คำถาม/คำตอบของ53relatedcasesแล้ว รวมกับ72เคสก่อนgateและGPU13keysเป็น{len(all_keys)}unique reviewed/probed keys ในนี้ยืนยันตัวอย่างscope/content/omissionfailure{len(bad)}keys ไม่ใช่จำนวนผิดทั้งหมด ยังเหลือ{20554-len(all_keys)}keysที่ไม่ตัดสินsemanticรายข้อ",'',
 'การตรวจนี้ทำระหว่างsample01หลังgateเสร็จแล้ว ไม่แก้candidate ไม่เปลี่ยนชุดที่เลือก และไม่ยิงคำถามเพิ่ม กลุ่มtournament→generalpolicy36keysยังคงcandidate review_requiredนอกเหนือเคสที่มีคำตัดสินเฉพาะแล้ว ไม่เหมาว่าทุกkeyผิดเหมือนกัน','']
for x in cases:doc += [f"## {x['question']}",'',f"`{x['key']}` — first stage `{x['first_failing_stage']}`",'',x['answer'],'','สาเหตุ: '+x['diagnosis_th'],'','Source: '+', '.join(f"{s['record_id']} rev{s['revision']}" for s in x['source_records']),'','Savedlegacy: '+str(x['saved_legacy_answer'])[:900],'','Savedlegacy exception: '+str(x['saved_legacy_exception']),'']
(R/'ITEM02_RELATED_CASES_REVIEW_TH.md').write_text('\n'.join(doc),'utf8')
print(json.dumps({k:v for k,v in out.items() if k not in ['cases','confirmed_bad_keys']},ensure_ascii=False))
