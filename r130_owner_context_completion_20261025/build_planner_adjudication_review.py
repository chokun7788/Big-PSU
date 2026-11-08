"""Archive the agent's review of all saved replay differences, with sources.

This does not infer answers, regrade R64/R95, change gold labels or select from
schema alone. The actual agent decision is written separately after review.
"""
import collections,hashlib,json,os,sys
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r129_full_plan_completion_20261024'
sys.path.insert(0,str(R/'system'));os.environ['PSU_COMMON_CHAT_PROFILE']='r69-migration-preview'
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.registry import pointer
snapshot=MigratedView(R/'system/data/knowledge/common.sqlite').snapshot()
rows=[json.loads(s) for s in (R/'paired_replay03/RESULTS.jsonl').read_text('utf8').splitlines()]
assert len(rows)==len({(x['arm'],x['key']) for x in rows})==330
by={a:{x['key']:x for x in rows if x['arm']==a} for a in ['base','retained','new']}
assert all(len(v)==110 for v in by.values())
gold={x['key']:x for x in map(json.loads,(P/'training_v2/test.jsonl').read_text('utf8').splitlines())}
diffs=json.loads((R/'ADJUDICATION_DIFFS.json').read_text('utf8'))
notes=[
 ('predicate_incomplete_gain','อ่านmaintenance periodsได้เพิ่ม แต่ไม่ตอบcan-book predicate จึงไม่ให้เครดิตว่าfulfilledทั้งคำถาม'),
 ('shared_failure_wording_only','ทั้งคู่ไม่ตอบเวลารอบบ่าย ไม่ใช่ข้อมูลขาดที่พิสูจน์แล้ว'),
 ('shared_failure_wording_only','คำสะกดผู้จัดกาถูกตีความไม่สำเร็จทั้งคู่'),
 ('source_backed_gain','newอ่านroleที่ถามจากmember_832e24bbcd11737eได้ โดยมีsource profile qualifier'),
 ('known_source_refusal_regression','retainedอธิบายศูนย์จากFAQที่มีอยู่ได้ แต่newเสียentity binding'),
 ('source_backed_gain_with_rendering_gap','newแสดงGPUตามspecificationsได้ แต่ปะปนtechnical keys/ข้อมูลไม่จำเป็น ต้องแยกformattingจากvalue'),
 ('old_heading_not_complete_answer','retainedแสดงชื่อ/หัวข้อrulebook ไม่ใช่เนื้อหาcompetition formatครบ จึงไม่ใช้answer statusเป็นหลักฐานว่าตอบถูกครบ; newunsupportedก็ตอบไม่ได้'),
 ('shared_failure_different_layer','Tekkenเลือกด่าน: unavailableเทียบunsupported_operation ยังไม่มีเนื้อหาคำตอบทั้งคู่'),
 ('known_source_refusal_regression','package_2มีroom_seats50และretainedตอบได้ newกลับentity_not_bound; ไม่ใช่live capacity'),
 ('known_source_refusal_regression','contact_studio_facebookมีURLตรงคำถาม แต่newไม่ส่งfieldที่ขอ'),
 ('source_backed_multi_need_gain','newเก็บทั้งขั้นตอนจองCockpitและตารางบริการ ในขณะที่retainedตกbooking need; ยังpartialและไม่เท่ากับlive slot'),
 ('shared_failure_wording_only','ข้อมูลที่ต้องใช้จองไม่สำเร็จทั้งคู่ แม้newเข้าwireได้ ไม่ถือเป็นsemantic gain'),
 ('critical_reservation_regression','walk-inต้องจองผ่านระบบมีsourceชัด retainedตอบได้ newกลับmissing_source'),
 ('critical_reservation_regression_with_scope_limit','retainedอ่านกฎแก้ข้อมูลทั่วไปได้ newไม่ตอบ; ยังต้องแยกข้อยกเว้นเบอร์โทรผิด ไม่ถือข้อความทั่วไปว่าครบทุกscenario'),
 ('wrong_domain_clarification','ทำจอยพังเป็นนโยบายบริการทั่วไป แต่newขอรายการแข่งขัน ไม่ใช่missing eventที่ผู้ใช้ต้องใส่'),
 ('shared_failure_different_layer','ความรับผิดชอบเก้าอี้พังไม่ตอบทั้งคู่ ต้องแยกการไม่รองรับoperationจากไม่มีข้อมูล'),
 ('shared_failure_wording_only','สิทธิ์เข้าใช้บริการไม่ตอบทั้งคู่ ไม่อ้างว่าข้อมูลeligibilityไม่มี'),
 ('shared_failure_different_layer','Switchตก/ค่าปรับไม่สำเร็จทั้งคู่ ไม่สร้างค่าปรับเป็นตัวเลข'),
 ('source_backed_payment_gain','newอ่านpayment deadline10นาทีจากFAQที่มีอยู่ได้ ไม่ใช่ผลยืนยันรายการจ่ายเงินจริง'),
 ('critical_payment_regression','r114_q018ยืนยันใบเสร็จ/ใบเสนอราคา/ใบกำกับภาษีออกไม่ได้ retainedตอบครบชนิด แต่newทิ้งคำตอบหลังfield verifier'),
 ('critical_payment_regression','คำถามเดียวกับข้อก่อนเพิ่มstyle request; newยังทิ้งsourceที่ตอบได้ ต้องนับเป็นregressionแต่รายงานfamily exposureด้วย'),
 ('shared_general_failure','คำถามตัวตนassistantไม่ตอบทั้งคู่ ไม่ใช่ขาดข้อมูลธุรกิจ'),
 ('shared_general_failure','คำถามassistantมีtypoไม่ตอบทั้งคู่'),
 ('shared_general_failure','คำขอเขียนประชาสัมพันธ์ไม่มีevent context ทั้งคู่ไม่ตอบ แต่newข้อความunsupportedต่างจากmissing entity'),
 ('shared_general_failure','คำขอประชาสัมพันธ์ภาษาอังกฤษไม่สำเร็จทั้งคู่'),
 ('shared_general_failure','greetingถูกตอบเป็นunsupported/missing_sourceทั้งคู่ ไม่ถือเป็นcontent accuracyที่ดี'),
 ('known_source_refusal_regression','equipment_gaming_chair.locationคือPC Zone แต่newจัดเป็นgame relationและไม่ตอบ'),
 ('actual_requested_predicate_failure','ถามรูปแบบการแข่งขันCS2 แต่newตอบแนวเกมTacticalFPS เป็นคนละpredicate/source kindแม้genre valueมีsourceจริง; ไม่ให้เครดิตanswer status'),
 ('shared_rule_retrieval_failure','CS2eligibility/roster/registrationไม่ตอบทั้งคู่ ต้องอ่านsource clausesเพื่อแก้ ไม่เรียกว่าno-dataจากstatus'),
 ('shared_rule_retrieval_failure','ข้อกำหนดก่อนแข่ง/หน้างานไม่ตอบทั้งคู่ ต่างfailure layer'),
 ('model_timeout_plus_domain_error','newมีTimeoutError60วินาทีที่evidence_selectionจริง และcompiledเป็นC05controlsแทนC13rule settings จึงแยกtransportจากwrong-domain ไม่เหมารวมเป็นcontent hallucination')
]
assert len(diffs)==len(notes)==31
review=[];source_bundle={}
for i,(d,(group,note)) in enumerate(zip(diffs,notes)):
 item={**d,'review_group':group,'agent_review':note,'human_semantic_accuracy_percent':None}
 for arm in ['retained','new']:
  for rid,facet,claim_value in d[arm+'_claims']:
   if rid in source_bundle:continue
   record=snapshot['release']['records'][rid];fields={}
   for key,f in record['fields'].items():
    if f.get('status')!='known':continue
    evidence=[]
    for ref in f.get('evidence_refs',[]):
     pair=snapshot.get('source_pairs',{}).get(ref['source_id'])
     if not pair:continue
     src,body=pair
     try:actual=pointer(json.loads(body),ref['locator']);resolved=True
     except (KeyError,ValueError,TypeError,IndexError):actual=None;resolved=False
     evidence.append({'source_id':ref['source_id'],'locator':ref['locator'],'snapshot_sha256':src['sha256'],'pointer_resolved':resolved,'source_value':actual})
    fields[key]={'value':f['value'],'evidence':evidence}
   source_bundle[rid]={'kind':record['kind'],'revision':record['revision'],'validity':record['validity'],'fields':fields}
 item['source_record_ids']=sorted({r[0] for arm in ['retained','new'] for r in d[arm+'_claims']});review.append(item)
critical={'service_fee','reservation','payment','rules','competition_rules','schedule','live'}
all_cases=[];domain_changes=collections.defaultdict(collections.Counter)
for key,n in by['new'].items():
 old=by['retained'][key]['execution'];new=n['execution'];domains={t['domain'] for t in gold[key]['label']['tasks']}
 same=old['answer']==new['answer'] and old['status']==new['status']
 for domain in domains:domain_changes[domain]['same' if same else 'changed']+=1
 all_cases.append({'key':key,'question':n['question'],'gold_tasks':gold[key]['label']['tasks'],'critical':bool(domains&critical),'same_answer_and_status':same,'retained_status':old['status'],'new_status':new['status'],'retained_answer':old['answer'],'new_answer':new['answer'],'retained_record_ids':[c['record_id'] for c in old['claims']],'new_record_ids':[c['record_id'] for c in new['claims']],'same_does_not_mean_semantically_correct':True})
with (R/'ADJUDICATION_ALL_110_CASES.jsonl').open('x',encoding='utf8') as f:
 for item in all_cases:f.write(json.dumps(item,ensure_ascii=False)+'\n')
(R/'ADJUDICATION_SOURCE_EVIDENCE.json').write_text(json.dumps({'snapshot':{'active':snapshot['active'],'epoch':snapshot['epoch']},'records':source_bundle,'new_model_inferences':0,'source_pointer_not_semantic_accuracy_proof':True},ensure_ascii=False,indent=2),'utf8')
(R/'ADJUDICATION_REVIEW.json').write_text(json.dumps({'saved_rows_reviewed':330,'paired_questions':110,'same_answer_status':79,'changed_cases_reviewed':review,'critical_domain_changes':dict(domain_changes),'critical_source_noninferiority_passed':False,'new_weight_promotion_rejected':True,'selection_recommendation':'retained','wire_metrics_not_semantic_accuracy':True,'all_scope_limitations_still_reported':True},ensure_ascii=False,indent=2),'utf8')
md=['# การตรวจเลือกน้ำหนักหลัง R130 replayครบ330','','ข้อสรุป: **ไม่รับน้ำหนักnewสำหรับFull Testรอบนี้ ใช้retainedตามfallbackที่กำหนดไว้** เพราะพบcritical reservation/payment regressionและตอบgenreแทนcompetition format แม้raw wire/obligation ratioดีขึ้น','',
 '## ขอบเขตหลักฐาน','','- 110keysเหมือนกันทั้ง3แขน รวม330แถว ตรวจactual profile/messages/schema/adapter/precision provenance ไม่มีcontext inferenceใหม่','- source/inputของR130คงเดิม; แตกต่างจากข้อมูลR95/R64 จึงไม่ใช่causal Flow comparisonกับlegacy','- newผ่านwire90/110, operation+field56/110, mean slotF1ประมาณ0.131 แต่base/retainedwire0เกิดserialization/version mismatch ไม่ใช่คำตอบถูก0% อ่าน RAW_PROTOCOL_REVIEW_TH.md','- mean typed obligation ratioเพิ่ม0.2409→0.3955 แต่denominatorมาจากproposal อาจตกgold needs จึงใช้ratioอย่างเดียวเลือกไม่ได้','- เปรียบคำตอบ/statusครบ110pairs:79เหมือนกัน และ31เปลี่ยน อ่าน31กรณีเปลี่ยนด้านล่างพร้อมsource bundle; sameไม่เท่ากับcorrect','- retainedเป็นR121plannerweightsบนengine/dataใหม่ ไม่ใช่FlowlegacyR64 การเลือกนี้ไม่รับรองคุณภาพretainedหรือบอกว่าแก้ทุกหมวดครบ','',
 '## กรณีเปลี่ยนทั้งหมด31กรณี','']
for i,item in enumerate(review,1):
 md += [f"### {i}. {item['key']}",'',item['q'],'',f"**กลุ่ม:** {item['review_group']}",'',item['agent_review'],'', '**Retained:** `'+item['retained_status']+'`','',item['retained_answer'],'','**New:** `'+item['new_status']+'`','',item['new_answer'],'','**Source records:** '+', '.join('`'+rid+'`' for rid in item['source_record_ids']),'']
md+=['## ปัญหาร่วมที่ห้ามปิดบัง','','ทั้งสองแขนยังมีrule retrieval failures, timetable/eligibility/contact/paraphrase misses, duplicated policy conflictsจากข้อความต่างรูป, missing needsในคำถามหลายส่วน, greeting/general handling และselector timeout/contract failures Source-verifier fatal0ยืนยันเพียงกลไกหลักฐาน ไม่ยืนยันว่าเลือกpredicateหรือคำตอบถูกครบ','',
 'Engine replayไม่ครอบคลุมnative API pathทุกเส้นทาง จึงต้องตรวจfinal APIและFull Testจริงต่อ ไม่ใช้ข้อสันนิษฐานว่าAPIอาจตอบถูกเพื่อลบregressionในชุดนี้ ไม่ใช้Full Testเป็นproduction approval','',
 '## หลักฐาน','','- ADJUDICATION_ALL_110_CASES.jsonl: gold needsและคำตอบทั้งสองแขนครบ110คู่','- ADJUDICATION_REVIEW.json:31กรณีและเหตุผลแยกกลุ่ม','- ADJUDICATION_SOURCE_EVIDENCE.json: record revision/fields/pointer values/source SHA256','- paired_replay03/RESULTS.jsonl และ RUN_FREEZE.json','- RAW_PROTOCOL_REVIEW_TH.md และ RAW_PROTOCOL_REVIEW.json','']
(R/'PLANNER_ADJUDICATION_REVIEW_TH.md').write_text('\n'.join(md)+'\n','utf8')
print(json.dumps({'paired_questions':110,'all_changed_cases_reviewed':31,'source_records_archived':len(source_bundle),'new_promotion_rejected':True,'recommended_profile':'retained'}))
