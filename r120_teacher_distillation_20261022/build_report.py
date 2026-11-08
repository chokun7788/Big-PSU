"""Build the final review from complete saved runs only."""
import collections,hashlib,json,statistics
from pathlib import Path
R=Path(__file__).resolve().parent
read=lambda p:json.loads(p.read_text('utf8'))
rows=lambda p:list(map(json.loads,p.open(encoding='utf8')))
def link(name,label=None):return f'[{label or name}]({(R/name).resolve().as_posix()})'
def ratio(d):
 n=d['positive_pass'];total=d['positive_grades'];return f'{n}/{total} ({100*n/total:.1f}%)' if total else 'ไม่มี positive checks'
def modelstats(folder):
 es=rows(R/folder/'MODEL_EVENTS.jsonl');ts=rows(R/folder/'MODEL_TRANSPORT.jsonl')
 return {'events':len(es),'schema_rejected_events':sum(e.get('transport_ok') is True and e.get('schema_ok') is False for e in es),
  'transport_failed_events':sum(e.get('transport_ok') is False for e in es),'wire_attempts':len(ts),'wire_failed_attempts':sum(t.get('transport_ok') is False for t in ts),
  'wire_failure_types':dict(collections.Counter(t.get('error_type','unknown') for t in ts if t.get('transport_ok') is False)),
  'affected_request_keys':sorted({e['key'] for e in es if e.get('transport_ok') is False})}
def main():
 c=read(R/'SAVED_COMPARISON.json');assert not c['partial'] and c['revision']=='03'
 initial=read(R/'INITIAL_SAVED_COMPARISON.json');ss=c['summaries'];pairs=c['pairs']
 runs={n:read(R/n/'TEST_COMPLETE.json') for n in ['baseline01','student01','regression01','student02','student03','regression03']}
 retry_done=read(R/'transport_retry01/TEST_COMPLETE.json');assert retry_done['complete'] and retry_done['source_code_inputs_unchanged'] and retry_done['original_sources_and_results_unchanged'] and retry_done['model_identity_verified']
 retry_rows=rows(R/'transport_retry01/RESULTS.jsonl');assert len(retry_rows)==1
 assert all(d['complete'] and d['source_code_inputs_unchanged'] and d['original_sources_and_results_unchanged'] and d['model_identity_verified'] for d in runs.values())
 assert runs['student03']['unique_request_keys']==27 and runs['regression03']['unique_request_keys']==48
 teacher=read(R/'teacher01/COMPLETE.json');assert teacher['complete'] and teacher['requests']==64
 diagnostics={n:modelstats(n) for n in [*runs,'transport_retry01']}
 api_failures={n:[{'key':r['key'],'question':r['question'],'http_status':r.get('http_status'),'error':r.get('error'),'elapsed_sec':r.get('elapsed_sec')} for r in rows(R/n/'RESULTS.jsonl') if r.get('error') or not r['result']['answer']] for n in runs}
 review=read(R/'TEACHER_MAPPING_REVIEW.json')
 records=rows(R/'PER_REQUEST_COMPARISON.jsonl');keymap={r['key'][:8]:r for r in records}
 assert len(records)==len({r['key'] for r in records})==75
 assert all(x['passed'] for x in read(R/'HISTORICAL_SNAPSHOT_VERIFICATION.json'))
 assert read(R/'REVISION03_CONTRACTS.json')['passed']==8
 detailed=[]
 notes={
 '42582c1e':('definition_vs_name','คำถามนิยามอุปกรณ์ต้องใช้ usage/description การคืนชื่อเดิมอย่างเดียวไม่อธิบายอุปกรณ์; แยกผล cold request/model transport ออกจากการเลือก facet'),
 'eca9a681':('reader_binding_gap','รู้ว่าเป็น bookable/maintenance แต่ยังไม่ผูก source สำหรับคำถามที่ไม่ระบุวัน ควรตอบจากกฎ maintenance เมื่อมีขอบเขตยืนยัน หรือถามวันที่'),
 '5d18afc2':('completeness_review','คำถามการใช้ controller กว้าง reader เลือกเพียงบาง bindings ไม่ควรเรียกว่ารายการปุ่มครบ ต้องตรวจ scope/การสรุปกับ source ทั้งชุด'),
 '8711c0d5':('style_modifier_as_multiple_needs','คำขอให้ตอบสั้นถูกแยกเป็น factual task และตอบซ้ำสามช่วง การมี schema ถูกต้องไม่ได้รับรองว่าจำนวน needs ถูกต้อง'),
 'd01ecd03':('intent_failure','ไม่มี PSU ID เป็นเรื่องสิทธิ์เข้าใช้ แต่ได้จำนวนจอย PS5 ไม่ตอบคำถาม แม้ข้อมูลอุปกรณ์ที่ส่งจะเป็นจริง'),
 '4930d252':('intent_rule_vs_gameplay','ถามข้ออนุญาตตามกติกา แต่ไหลไปวิธีเล่นเกม เป็น confirmed wrong requested operation ไม่ใช่ขาด keyword อย่างเดียว'),
 '50d3e66b':('duration_ambiguity','คำถามมีทั้ง 30 นาทีและ 1 ชั่วโมง ไม่มีตัวเชื่อมที่ชัด การเลือกเพียง 60 นาทีไม่พิสูจน์ว่าครบ ควรถามว่าจะเทียบสองอัตราหรือคำนวณระยะใด'),
 '9c658222':('procedure_reader_gap','รู้หมวด reservation แล้วแต่ยังหาเงื่อนไขข้อมูลที่ต้องกรอกไม่ได้ การสอนหมวดไม่ทดแทน procedure facet/aliases'),
 '0234e46d':('capacity_and_transport','ต้องแยกจำนวนคนเล่นพร้อมกันต่อเครื่องจาก participant range ของบริการ รอบแรกมี model transport failure; revision03 ยังตีเป็น games/players_max และเลือกไม่เจอ source แทนที่จะอ่าน equipment/service capacity จึงยังเป็นปัญหา intent/reader คนละส่วนกับ transport'),
 '7551e61a':('broad_rulebook_incomplete','ถามกฎการแข่งขันกว้าง แต่ได้เฉพาะบทลงโทษบางข้อ ไม่ใช่ full rulebook; ตัวแก้ penalty family ไม่ครอบคลุม generic rules request นี้'),
 'd7158a36':('source_action_scope','แหล่งที่เลือกยืนยันการรับประทานในพื้นที่กำหนด ไม่ได้ยืนยันสิทธิ์นำเข้าแยกต่างหาก ต้องแสดง scope limit แม้ผ่าน literal food/designated keywords'),
 '18fc2648':('inverse_role_operator','initial student ส่งทั้ง directory แทนตำแหน่งที่ถาม ต้องจับ role suffix จาก source และใช้ public-scope gate ต่อไป'),
 '1806def7':('set_operator_regression','initial student เปลี่ยน list predicate เป็น detail ทำให้ lost source set; revision02 เพิ่ม explicit multi-zone set frame จาก native relations'),
 '00301c15':('native_projection_repaired','FAQ temporary suspension มีอยู่ใน native ก่อนเริ่ม แต่ intent/topic ไม่เข้า compiler; เพิ่ม declared topic mapping แล้ว source เดิมตอบได้'),
 '104194c2':('rule_family_repaired','facet เดิมของ Round Rollback/Map Forfeit ต่างกลุ่ม ทำให้เลือก penalty facet แล้วตก; อ่าน parent + numbered source siblings เพื่อรวม 5 types ตาม source'),
 '0d05eaf6':('duration_language_repaired','one hour ต้องกลายเป็น 60 นาที ไม่ควรออกทั้งอัตรา 30 และ 60 นาที; ใช้ current owner rates ไม่คัดลอกเงินเก่าของ teacher'),
 '4b0fb4a4':('event_context_and_heading_repaired','รักษา AOV จากทั้งประโยคแล้วจับ heading competition equipment ใน RoV Blueket 2025 source; ยังคงขอบเขตรายการ/ปี ไม่ยืนยันทุกการแข่งขันปัจจุบัน'),
 '546c4490':('game_price_operation_repaired','จากตอบรายการเกมเป็นข้อมูลค่าบริการที่ให้เล่นเกมนั้นได้ ผ่าน native game→service→rate; คำถามไม่ระบุกลุ่ม/ระยะเวลา จึงแสดงแยกอัตรา ไม่ใช่ราคาเดียว'),
 '9efbf2ac':('source_scope_gap','คำตอบเจ้าของเรื่อง capture ภายในเกมไม่ครอบคลุมการถ่ายวิดีโอพื้นที่จริง การไม่ยืนยันจึงไม่ใช่ความผิดเพราะ teacher ตอบได้'),
 '2c110689':('controlled_live_unavailable','workload ควบคุมให้ live provider unavailable ไม่ใช่การยืนยันว่าสถานะจริงของเครื่องเป็นอย่างไร'),
 'a1c90b6e':('edition_scope_gap','Part II กับ Part II Remastered ต้องมีความสัมพันธ์ source ยืนยันก่อน การตอบ Part I และบอกส่วน Part II ยังไม่ทราบเป็น partial ที่รักษาขอบเขต'),
 '3020765f':('response_detail_regression','profile FAQ สั้นอาจให้ที่อยู่ถูกแต่ขาดอาคาร 5 ชั้น 1 ที่ baseline structured address มี ต้องจัดลำดับ source ที่ตอบ location ครบกว่า'),
 'eafe23b9':('binding_source_limit','source Nintendo ที่มีเป็นคำอธิบายการควบคุมกว้าง ไม่มี mapping ปุ่มละเอียดทั้งหมด จึงยังห้ามเรียกว่าปุ่มรายปุ่มครบ'),
 '96ef8f71':('unresolved_reader_or_source','Hades II ยังได้ unconfirmed ต้องตรวจ source record/edition/reader เพิ่ม ไม่สรุปจาก missing_source เพียงอย่างเดียวว่าข้อมูลยังไม่ย้าย'),
 '981fa8d4':('unclear_request','คำถามสั้นและสะกดไม่ครบ ต้องตรวจ normalization และขอ clarification เมื่อไม่ชัด ไม่ควรสร้าง location ที่ไม่ได้ถามชัด'),
 'aefe9911':('unclear_action','คำถามเครื่องดื่ม/พื้นที่ขาด action ว่าจะนำเข้า บริโภค หรือจัดวาง ต้องรักษาขอบเขตความหมาย'),
 'e7a3582e':('multiple_unclear_scenarios','ของหาย/อุปกรณ์/เปียกเป็นหลายสถานการณ์ที่ไม่ชัด ไม่ควรรวมเป็นสิทธิ์ชดเชยหรือข้ออนุญาตเดียว'),
 'f683a42c':('http_transport_retry','regression03 เดิมเกิด HTTP client TimeoutError จึงไม่มีคำตอบ; retry HTTP 200 แต่ evidence selector ยัง TimeoutError และคืน unavailable จึงยังไม่ยืนยันคำตอบ เก็บผล retry แยกและไม่แก้คะแนน/ผลเดิม'),
 }
 for r in records:
  tag,note=notes.get(r['key'][:8],('main_intent_review_only','อ่านคำตอบก่อน/หลังและ claim receipts ในรายงานรายข้อแล้ว ไม่ได้ให้เปอร์เซ็นต์ semantic accuracy และไม่รับรองว่าทุกถ้อยคำครบทุกเงื่อนไข'))
  detailed.append({'key':r['key'],'cohort':r['cohort'],'question':r['question'],'review_group':tag,'note':note,'final_status':r['after_artifact'].get('status'),'after_claim_ids':[f['fact_id'] for f in r['after_artifact'].get('claims',[])]})
 (R/'SEMANTIC_REVIEW_NOTES.json').write_text(json.dumps(detailed,ensure_ascii=False,indent=2),'utf8')
 out={'complete':True,'candidate':'R120 revision03','teacher_requests':64,'reviewed_examples':60,'quarantined_examples':4,'parameter_training':False,
  'evaluation_requests':27,'development_requests':48,'new_questions':0,'full_test':False,'production_installed':False,
  'evaluation_reused_for_development_after_initial_pilot':True,'initial':initial['summaries'],'final':ss,'paired_changes':pairs,'model_diagnostics':diagnostics,'api_failures':api_failures,
  'transport_retry':{'completion':retry_done,'results':retry_rows},'all_original_final_http_successful':False,'all_questions_answered_correctly':False,
  'protected_original_files':len(read(R/'PROTECTED_INPUTS.json')),'originals_unchanged':True,'native_data_unchanged':read(R/'REVISION02_CONTRACTS.json')['checks'][3]['passed']}
 (R/'ANALYSIS_FINAL.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
 md=['# R120 ผลทดลองให้ Flow เดิมสอน Flow กลาง','',
 '## สรุป','',
 '**วิธีนี้ช่วยได้บางส่วน แต่ตัวอย่างสอนอย่างเดียวไม่แก้ข้อผิดพลาดทุกชั้น** รอบนี้ถ่ายทอดวิธีตีความ แผนเลือกเครื่องมือ และโครงสร้างคำตอบ โดยแก้ compiler/reader/operator ที่พบปัญหาร่วมด้วย ไม่มีการ train/fine-tune น้ำหนัก Typhoon และยังไม่ได้ติดตั้งทับ R78/production','',
 'ครูคือ Legacy R64 และนักเรียนเริ่มจาก Common R119 ใช้คำถามเดิมทั้งหมด: teacher 64 ข้อ → ตัวอย่างแผนที่ตรวจแล้ว 60 ข้อ, คัดออก 4 ข้อ; ชุดเปรียบเทียบ 27 ข้อและ development 48 ข้อ ไม่ใช่ Full Test','',
 '## ผลก่อนและหลัง','',
 '**ตารางนี้เป็น positive literal-content checks ไม่ใช่เปอร์เซ็นต์ความถูกต้องของคำตอบทั้งระบบ** คำถามเดียวมีหลาย grades จากหลาย corpus; 27 คำถามมีเพียง 17 คำถามที่มี positive checks รวม 51 grades และ 48 คำถามมีเพียง 18 คำถามที่มี positive checks รวม 62 grades ข้อที่ไม่มี positive checks ยังตรวจคำตอบประกอบในรายงานรายข้อ','',
 '| ชุด | ก่อน R119 | R120 รอบแรก | R120 revision03 |','|---|---:|---:|---:|',
 f'| ชุดแยกไว้ 27 ข้อ | {ratio(ss["baseline"]["counts"])} | {ratio(initial["summaries"]["student"]["counts"])} | {ratio(ss["student"]["counts"])} |',
 f'| Development 48 ข้อ | {ratio(ss["development_before"]["counts"])} | {ratio(initial["summaries"]["development_after"]["counts"])} | {ratio(ss["development_after"]["counts"])} |','',
 'ทั้ง teaching และชุด 27 ข้อคัดจาก saved Legacy ที่ validation/confidence ผ่านและไม่มี positive literal fail จึงมี selection bias ไปยังกรณีที่ Legacy เคยผ่านเกณฑ์ ไม่ใช่ตัวแทนสุ่มของ Full ทั้งหมด การผ่านเกณฑ์นี้ยังไม่รับรอง semantic correctness ของครู','',
 'รอบแรกแยกครอบครัว case IDs/origin IDs ไม่ให้ข้าม teaching/evaluation/development และตรึง code ก่อนอ่านคำตอบรายข้อของ evaluation หลังพบปัญหา ได้นำ 27 ข้อนั้นมาวิเคราะห์และแก้ revision02/03 ดังนั้น **คะแนน revision03 เป็นผลพัฒนาบนคำถามที่เคยดูแล้ว ไม่ใช่ holdout ใหม่** แม้ก่อนแก้ก็อาจมี semantic near-duplicates ที่คนละ IDs; ไม่ใช้ตัวเลขนี้ทำนาย Full accuracy','',
 '### แยกภาษา — ชุดเปรียบเทียบ 27 ข้อ','',
 '| ภาษา | คำถาม | R119 | R120 revision03 |','|---|---:|---:|---:|']
 for locale in ['th','en','auto']:
  a=ss['baseline']['locales'][locale];b=ss['student']['locales'][locale];md.append(f'| {locale} | {a["requests"]} | {ratio(a)} | {ratio(b)} |')
 md+=['','### แยกภาษา — Development 48 ข้อ','','| ภาษา | คำถาม | R119 | R120 revision03 |','|---|---:|---:|---:|']
 for locale in ['th','en','auto']:
  a=ss['development_before']['locales'][locale];b=ss['development_after']['locales'][locale];md.append(f'| {locale} | {a["requests"]} | {ratio(a)} | {ratio(b)} |')
 md+=['','## ครูสอนอะไรจริง','','1. แยก requested operation จากบริบท: ถามราคา Beat Saber ให้ใช้ game→service→rate ไม่ตอบรายการเกม','2. ใช้ structured tools สำหรับคำนวณ ปุ่มเกม ตาราง และนโยบาย ไม่บังคับให้ LLM เขียนข้อเท็จจริงจากความจำ','3. เก็บชื่อเกม/รายการและเงื่อนไขทั้งประโยคก่อนอ่าน clause','4. คำถามกว้างต้องอ่าน source family/รายการครบตาม scope หรือบอก partial','5. ตอบ fact ที่ถามก่อน ลดชื่อ field ภายในและข้อความ heading ซ้ำ โดยคงเงื่อนไขและ source citations','','ข้อมูลใน prompt มีเพียงคำถามกับ task plan ที่ผ่านการตรวจ ไม่มีราคา โทษ หรือข้ออนุญาตจากคำตอบ teacher teacher รันแบบอนุญาต LLM แต่หลายข้อจบใน structured fast paths จึงไม่อ้างว่าเป็นการกลั่นคำตอบโมเดล 64 ครั้ง และใช้เฉพาะ trace ที่ระบบเปิดเผย ไม่อ้างความคิดภายในของโมเดล','',
 '## ทำไมไม่คัดลอกทุกคำตอบครู','','ครูยังมีกรณี route ผิดและคำถามหลายงานที่แปลงเป็น task เดียวไม่ได้ อีกทั้ง Legacy และ native มีข้อมูลคนละรุ่น เช่น หน่วยราคา/owner reaffirmation ปัจจุบัน การสอนตัวเลขเก่าจะสร้างความผิดพลาดใหม่ จึงคัดออก/แก้ mapping ตาม '+link('TEACHER_MAPPING_REVIEW.json')+' และอ่าน native ปัจจุบันเมื่อจะตอบทุกครั้ง','',
 '## สาเหตุที่ยืนยันและสิ่งที่แก้','','| ชั้นที่ผิด | หลักฐาน | สิ่งที่เปลี่ยน |','|---|---|---|',
 '| Projection | temporary_suspension มีอยู่ใน native แต่ไม่ได้เป็น C10 fact | ใช้ declared topic/route category เชื่อม FAQ เข้าตัวอ่าน |',
 '| Requested operation | Beat Saber cost ไป catalogue; multi-zone ไป detail | source-backed price frame และ set predicate ก่อนอ่านข้อมูล |',
 '| Context | AOV อยู่ในประโยคเตรียมแข่งแต่ quote เหลือคำถาม equipment | รักษาบริบททั้ง single need และเชื่อม heading ใน event เดียว |',
 '| Clause coverage | Rollback/Map Forfeit ถูกจัด facet ต่างกลุ่ม | อ่าน parent และ numbered siblings ตาม source_order |',
 '| Language slots | one hour ทำให้แสดงทั้ง 30/60 นาที | แปลงหน่วยภาษาเป็น 60 นาทีโดยไม่แก้ business rate |',
 '| Inverse lookup | role อยู่หลังคำอธิบายยาวจึงไม่ตรงทั้ง string | จับ source role suffix และยังตรวจ public scope |',
 '| Source action | กฎรับประทานถูกใช้ตอบนำอาหารเข้า | คืนข้อความ scope limit และสถานะ partial |',
 '| Presentation | internal policy identifiers, session_ceil, label/value ซ้ำ | ตอบ fact ก่อนพร้อม citations; calculation rules ยังอยู่ใน audit |','',
 'รายละเอียด Flow และจุดจำกัด: '+link('FLOW_DISTILLATION_TH.md')+'; หลักฐาน source: '+link('REGRESSION_SOURCE_EVIDENCE.json')+' และ '+link('STUDENT_CONTRACT_CASES.json'),'']
 md+=['## ตัวอย่างก่อนและหลังจาก API จริง','']
 for prefix in ['546c4490','00301c15','0d05eaf6','104194c2','4b0fb4a4','1806def7','18fc2648','d7158a36','42582c1e']:
  r=keymap[prefix];md += [f'### `{prefix}` — {r["question"]}','','**ก่อน:**',r['before_answer'],'','**หลัง revision03:**',r['after_answer'],'',notes[prefix][1],'']
 md+=['## ข้อที่ยังไม่ควรเรียกว่าถูกครบ','']
 for prefix in ['eca9a681','5d18afc2','8711c0d5','d01ecd03','4930d252','50d3e66b','9c658222','0234e46d','7551e61a','3020765f','9efbf2ac','a1c90b6e','eafe23b9','96ef8f71']:
  r=keymap[prefix];md += [f'- `{prefix}` {r["question"]}: {notes[prefix][1]}']
 md+=['','มีบันทึกผลครบ 75 keys รวม 1 key ที่ HTTP ไม่กลับและแยกผล retry ไว้ อ่านคำตอบที่กลับและ receipt/fact IDs ได้ที่ '+link('PER_REQUEST_COMPARISON_TH.md')+'; ข้อสังเกตรายข้ออยู่ใน '+link('SEMANTIC_REVIEW_NOTES.json')+' รายงานนี้ไม่แปลง “ไม่พบ defect ในการอ่านรอบนี้” เป็นคำรับรอง semantic correctness ทั้งประโยค','',
 '## Strict/protocol, content, validity และ model transport','',
 '- Strict checker เดิมผ่าน 0/81 และ 0/164 ทั้งก่อนและหลัง เพราะยังคาด legacy mode/route/protocol หลายข้อ ไม่ใช่หลักฐานว่าคำตอบทุกข้อผิดเนื้อหา ต้องแยก expected outcome/performance/evidence IDs และ content/format ต่อไป',
 '- Positive literal checks ยังพลาดการประเมินคำตอบครบ/ตรงเจตนา เช่น food bring vs consumption และ directory ที่ยาวแต่ไม่กรองตำแหน่ง จึงตรวจคำตอบและ source ประกอบ',
 '- Validity/scope: owner rates reaffirmed ณ 2026-10-20 ไม่ได้สร้าง effective interval ใหม่, กติกา AOV ที่อ่านเป็น Blueket 2025, ตารางให้บริการไม่ใช่ live occupancy และไม่ยืนยันอาคารเปิดทุกส่วน',
 '- Live provider ใน workload ถูกควบคุม unavailable; ผลนั้นไม่บอกสถานะจริงของเครื่อง',
 '- HTTP 200, validation_ok หรือ model identity verified ไม่รับรอง intent/content accuracy; model call ล้มอาจทำให้คำตอบ unavailable แม้ API ตอบสำเร็จ','',
 '| รอบ | Model events | Events transport failed | Wire attempts failed | Schema rejected events |','|---|---:|---:|---:|---:|']
 for n,d in diagnostics.items():md.append(f'| {n} | {d["events"]} | {d["transport_failed_events"]} | {d["wire_failed_attempts"]}/{d["wire_attempts"]} | {d["schema_rejected_events"]} |')
 md+=['','### HTTP timeout ที่ต้องอ่านแยกจากคะแนน','','regression03 รันครบ 48 keys / 164 grades แต่ HTTP สำเร็จ 47/48 และมีคำตอบว่าง 1 ข้อ คือ `f683a42c` Animal Crossing เกิด `TimeoutError:timed out` ที่ client ใช้เวลาที่บันทึก 79.188 วินาที ค่า API timed_out เป็น 0 เพราะไม่มี response body กลับมา ไม่ได้หมายความว่าไม่มี timeout สาเหตุชั้นในยังไม่ยืนยัน จึงไม่เหมารวมว่าเป็น model transport หรือ content failure','',
 'ข้อนี้ไม่มี positive literal check จึงทำให้ 62/62 ยังผ่านได้แม้คำขอล้ม เก็บผลเดิมไว้แล้ว retry เฉพาะ key นี้หนึ่งครั้ง ใช้ candidate/frozen data เดียวกันแยก folder ไม่แทนที่คะแนนเดิม','',
 f'ผล retry: HTTP {retry_rows[0]["http_status"]}; error={retry_rows[0].get("error")}; คำตอบจริง:','',retry_rows[0]['result']['answer'] or '(ไม่มีคำตอบกลับ)', '',
 'แม้ retry จะได้ HTTP 200 แต่ trace ระบุ evidence selector `model_transport_failure` และ wire TimeoutError 3.781 วินาที จึงยังไม่ได้คำตอบเนื้อหาที่ยืนยันได้ ไม่ถือว่า retry แก้ข้อนี้สำเร็จ และแยกจาก live-provider fixture ที่ใช้กับคำถามสถานะสด','',
 link('transport_retry01/RESULTS.jsonl')+' / '+link('transport_retry01/TEST_COMPLETE.json'),'',
 'ดู error types/affected request keys ใน '+link('ANALYSIS_FINAL.json')+' และ MODEL_TRANSPORT/MODEL_EVENTS ของแต่ละรอบ request แรกมี cold initialization ร่วมกับ deadline จึงไม่สรุปว่า latency ต่างกันเกิดจาก distillation เพียงอย่างเดียว','',
 '## ขอบเขตการทดลองและการตรวจความคงเดิม','',
 f'- ต้นฉบับ {out["protected_original_files"]:,} ไฟล์ตรวจ hashes ไม่เปลี่ยน รวม source และผลเดิม; native database ทุกตารางเท่ากับ R119 ก่อนแก้ รวม approvals/withdrawals ตาม source contracts และ final run freeze',
 '- ใช้ model scb10x/typhoon2.5-qwen3-4b:latest digest b1f251ef835962b270ba48266d4e32e6f90b29f10930d0712ef5eaabec773a05 ตรวจ identity ก่อน/หลัง และ response identity ใน events',
 '- Source/code/input freeze ของทุก completed run ผ่าน ไม่แก้ log เก่า; เก็บ revision01_system/revision02_system ก่อนแก้ และตรวจ snapshots ย้อนหลังตรงกับ freeze ใน '+link('HISTORICAL_SNAPSHOT_VERIFICATION.json'),
 '- 77 source/code contracts ก่อน initial pilot, 5 regression contracts revision02 และ 8 final contracts revision03 เป็นการตรวจโครงสร้างข้อมูล/โค้ด ไม่ใช่จำนวนคำถามถูก; ดู '+link('STUDENT_CONTRACTS.json')+', '+link('REVISION02_CONTRACTS.json')+' และ '+link('REVISION03_CONTRACTS.json'),
 '- ตัวอย่าง teaching ครอบคลุม 9 กลุ่ม ไม่ได้ครอบคลุมทุกหมวดของระบบ ไม่มี Full Test หรือการติดตั้ง production',
 '- คำถาม API ใช้ session แยกตาม key และ runtime conversation database แยกแต่ละรอบ ไม่ได้ประเมินบทสนทนาต่อเนื่องหลาย turn',
 '- ผลเป็นการรวม demonstrations + parser/reader/compiler/presentation changes ยังไม่ได้ ablation ว่าตัวอย่าง prompt เพียงอย่างเดียวเพิ่มได้เท่าไร','',
 '- Candidate ยังพยายามเรียก LLM ตีความก่อนเป็นส่วนใหญ่ ไม่ได้ย้าย gated structured fast paths ของ Legacy มาครบ จึงยังมีความเสี่ยงเรื่อง transport/deadline แม้งานที่มี exact source reader จะไม่ต้องให้โมเดลสร้างคำตอบธุรกิจ','',
 '## ข้อสรุปและแนวพัฒนาต่อ','',
 'ควรใช้แนวนี้ต่อเพื่อสอน operation/slots/เครื่องมือ/ขอบเขตคำตอบ โดยให้ current source เป็นผู้ตัดสิน facts ข้อมูลครบอย่างเดียวไม่พอ ถ้า compiler ไม่ส่ง fact เข้า reader หรือ operator เลือกคนละงาน ข้อผิดพลาดยังเกิดได้','',
 'ลำดับที่ควรทำต่อ: (1) จัดการสิทธิ์ใช้บริการและกติกาที่หลุดเป็น gameplay (2) แยก style modifier กับ factual needs (3) ทำ procedure fields และ capacity semantics ให้ตรงคำถาม (4) เพิ่ม completeness contract สำหรับ broad rulebook และ broad controls (5) จัด source precedence ของที่อยู่/FAQ และประเมินบนกลุ่มคำถามเดิมที่ยังไม่เคยใช้ปรับรอบนี้ ก่อนอ้างคะแนนทั่วไป',
 '',
 'ถ้าจะทำ parameter distillation จริงในรอบถัดไป ควรฝึกเฉพาะแผน operation/slots และการเลือกหลักฐานจากชุดที่ตรวจแล้ว รักษาราคา/สิทธิ์/กฎที่เปลี่ยนได้ไว้ใน native ไม่สอนให้จดจำเป็นคำตอบคงที่ แนวคิดการฝึกใน [Hinton et al. 2015](https://arxiv.org/abs/1503.02531) และ [Hsieh et al. 2023](https://aclanthology.org/2023.findings-acl.507/) เป็นแรงอ้างอิง แต่การทดลองนี้ไม่ได้ทำซ้ำวิธีฝึกหรืออ้างผล benchmark จากงานเหล่านั้น','',
 '## ไฟล์สำคัญ','',
 '- '+link('PLAN_TH.md'),'- '+link('FLOW_DISTILLATION_TH.md'),'- '+link('TEACHER_MAPPING_REVIEW.json'),'- '+link('PER_REQUEST_COMPARISON_TH.md'),'- '+link('ANALYSIS_FINAL.json'),'- '+link('student03/TEST_COMPLETE.json'),'- '+link('regression03/TEST_COMPLETE.json')]
 (R/'FINAL_REPORT_TH.md').write_text('\n'.join(md)+'\n','utf8')
 (R/'STATUS.json').write_text(json.dumps({'complete':True,'phase':'pilot_review_complete','candidate':'R120 revision03','full_test':False,'production_installed':False,'report':str(R/'FINAL_REPORT_TH.md')},ensure_ascii=False,indent=2),'utf8')
 print(json.dumps({'complete':True,'evaluation':ratio(ss['student']['counts']),'development':ratio(ss['development_after']['counts']),'report':str(R/'FINAL_REPORT_TH.md')},ensure_ascii=False))
if __name__=='__main__':main()
