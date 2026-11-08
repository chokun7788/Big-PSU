"""Finalize same-key development evidence after the last HTTP run completes."""
import hashlib,json,statistics
from pathlib import Path
from datetime import datetime
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
done=read(R/'http03/TEST_COMPLETE.json');assert done['complete'] and done['unique_request_keys']==48 and done['grades']==164
for k in ['source_code_inputs_unchanged','original_sources_and_results_unchanged','model_identity_verified','all_selected_keys_recorded']:assert done[k]
latest_done=read(R/'http04/TEST_COMPLETE.json');assert latest_done['complete'] and latest_done['unique_request_keys']==8 and latest_done['grades']==26
for k in ['source_code_inputs_unchanged','original_sources_and_results_unchanged','model_identity_verified','all_selected_keys_recorded']:assert latest_done[k]
checks=read(R/'CONTRACT_CHECKS.json');assert checks['passed']==checks['total']==22
runs={name:read(R/name/'analysis/COMPARISON.json') for name in ['full01','http02','http03']}
rows={x['key']:x for x in map(json.loads,(R/'http03/RESULTS.jsonl').open(encoding='utf8'))}
old={x['key']:x for x in map(json.loads,(R/'SAVED_R115_RESULTS.jsonl').open(encoding='utf8'))}
assert set(rows)==set(old) and len(rows)==48
new=runs['http03'];c=new['counts']
point_rows={x['key']:x for x in map(json.loads,(R/'http04/RESULTS.jsonl').open(encoding='utf8'))}
assert len(point_rows)==8 and set(point_rows)<=set(rows)
point={'requests':8,'positive_grades':0,'old_positive':0,'new_positive':0}
for key,v in point_rows.items():
    for a,b in zip(v['grades'],old[key]['grades']):
        assert all(a[k]==b[k] for k in ['file','row','variant','positive_literal'])
        if a['positive_literal']:
            point['positive_grades']+=1;point['old_positive']+=b['literal_passed'];point['new_positive']+=a['literal_passed']
def ratio(n,d):return f'{n}/{d} ({100*n/d:.2f}%)' if d else 'N/A'
summary={'phase':'complete','complete':True,'candidate':'R117 revision04','production_installed':False,
    'unique_existing_questions':48,'development_http_attempts':152,'new_questions':0,'contract_checks':22,
    'latest_run':'http04','full_test_run':False,'source_unchanged':True,'model_verified':True,
    'report':'REPORT_TH.md','flow':'FLOW_TH.md','completed_at':datetime.now().astimezone().isoformat(),
    'same_key_positive_literal':{'baseline_r115':c['old_positive'],'candidate_r117':c['new_positive'],'denominator':c['positive_grades']},
    'comparison_applies_to':'revision03 before final explicit-duration and clarification patch','revision04_targeted_checks':point,
    'semantic_accuracy_claimed':False}
report=['# R117 — เพิ่มการเข้าใจบริบทและเจตนาก่อนอ่านข้อมูล','',
    '## สิ่งที่ปรับแล้ว','',
    '1. วิเคราะห์ทั้งคำถามเป็น operation + domain + facet + target + constraints ก่อนเลือก reader ไม่เริ่มจากชื่อเกมหรือคำสำคัญอย่างเดียว',
    '2. เก็บบริบท current turn ก่อน explicit_request_focus ตัดประโยคเกริ่น เพื่อรักษาชื่อเกม รายการแข่ง และกลุ่มผู้ใช้ที่เกี่ยวข้อง',
    '3. ใช้ QueryPlanTask/operations และตัวตรวจแผนจาก Flow เดิม ร่วมกับ heuristic และ control/competition frames เดิมเป็นตัวตรวจอิสระ ไม่ยกคำตอบจากฐานเก่ามาใช้',
    '4. ตรวจ quote/target/เงื่อนไขกับข้อความจริง ผูกกลุ่มผู้ใช้กับ audience directory ปัจจุบัน และแปลงหน่วยภาษาที่ระบุ เช่น one hour เป็นหน่วยที่ตัวอ่านใช้ได้',
    '5. ให้แผนใช้กับตัวอ่านจริง: list-all ปุ่มครบชุด, เกมไปโซนตาม graph, confirmed subset สำหรับหลายโซน, partial unit rates เมื่อกฎคำนวณยังขาด',
    '6. แผนที่มีเจตนาชัดแต่ source/target ไม่รองรับจะไม่เปลี่ยนไปตอบข้อมูลคนละเรื่องผ่าน compatibility fallback พร้อมบันทึก diagnostic เมื่อ fallback มีผลลัพธ์',
    '7. รักษา source/validity/permission guards และเพิ่ม public_scope guard ให้ domain reader สอดคล้องกับ complete_flow โดยไม่แก้ approvals', '',
    '```text','คำถามและบริบทเต็ม → แผนความหมาย → ตรวจแผนกับกฎเดิม/ข้อความจริง',
    '→ เลือกงานและหมวด → อ่าน field / set / relation → ตรวจหลักฐานและเงื่อนไข',
    '→ ตอบตรงจุด หรือระบุส่วนที่ยังยืนยันไม่ได้','```','',
    '## ตรวจด้วยคำถามเดิมเท่านั้น','',
    '- ใช้ 48 unique keys จาก Full เดิม: 40 seeded regressions จาก 10 หมวดหลักและ 8 known failures ไม่เพิ่มคำถามใหม่',
    '- ตรวจ 48 keys เดิมใน 3 revisions แรก รวม 144 HTTP attempts จากนั้น revision04 แก้การรับระยะเวลาที่โมเดลลืมส่งและข้อความถามเพิ่ม ตรวจซ้ำเฉพาะ 8 keys ที่เกี่ยวข้อง รวมงานนี้ 152 HTTP attempts แต่มีคำถามไม่ซ้ำ 48 ข้อ ไม่ใช่ Full Test หรือ blind holdout',
    '- ใช้ saved R115 ของ keys เดียวกัน ไม่รัน R115 หรือ Legacy ใหม่ Source/clock/locale/grade entries ตรงกับ saved R115 cohort นี้',
    '- Contract checks 22/22 รวม malformed model output, source-bound slots, การอ่านครบทั้ง set, context frames, ระยะเวลาที่โมเดลลืมส่ง และการไม่ข้ามกฎคำนวณราคา', '',
    '## ผลตรวจคำ/ข้อความที่คาดหวังในชุดพัฒนานี้','',
    '| รุ่น | Positive literal/clause grades | Requests ที่ผ่าน positive ทุกแถว |','|---|---:|---:|',
    f"| Saved R115 | {ratio(c['old_positive'],c['positive_grades'])} | {ratio(c['old_positive_all'],c['positive_requests'])} |"]
for name,label in [('full01','R117 revision01'),('http02','R117 revision02'),('http03','R117 revision03')]:
    t=runs[name]['counts'];report.append(f"| {label} | {ratio(t['new_positive'],t['positive_grades'])} | {ratio(t['new_positive_all'],t['positive_requests'])} |")
report+=['',
    '**รุ่นโค้ดสุดท้ายคือ revision04:** ตาราง 48 ข้อด้านบนเป็น revision03 ที่เก็บ code snapshot ไว้ครบ หลังแก้สุดท้ายตรวจเฉพาะ 8 ข้อที่กระทบ ไม่อ้างว่ามีผล 48 ข้อใหม่ของ revision04', '',
    f"ผล 8 ข้อที่ตรวจซ้ำด้วยเกณฑ์เดิม: saved R115 {ratio(point['old_positive'],point['positive_grades'])}; revision04 {ratio(point['new_positive'],point['positive_grades'])} — ไม่ใช่คะแนน Full หรือ semantic accuracy", '',
    '**ห้ามใช้ตารางนี้เป็นเปอร์เซ็นต์ความเข้าใจทุกคำถาม:** มีเพียง 18/48 requests ที่มี positive contracts รวม 62 grades; ชุดนี้เลือกบางข้อจาก failures ที่รู้แล้ว และเป็น development corpus ตัวตรวจ literal ยังอาจผ่านข้อความ unit rate แม้คำถาม total price ตอบได้เพียง partial จึงไม่ถือว่าทั้งคำถามตอบสมบูรณ์เพียงเพราะผ่าน keyword', '',
    'ผลนี้ใช้เทียบกับ R115 บน 48 keys เท่านั้น ไม่เทียบเปอร์เซ็นต์ตรง ๆ กับ 67.90% ของ R116 ทั้ง 2,108 keys หรือ 96.46% ของชุด template ก่อนหน้า เพราะเป็นคนละ cohort/metric และไม่อ้างว่ารุ่นนี้เท่า Legacy แล้ว', '',
    '## ตัวอย่างก่อน–หลัง พร้อมข้อจำกัด','']
for key,label in [
    ('9813e160d170afb1642c7a117bdc3ab5253f5372ad62a7eb27ecdba7a283c1cb','ปุ่มทั้งหมด: Warzone'),
    ('b2ff4f05d34e5b2a82ae5cb5ede86f5a05bb022cf13531c682a39d936e4de5b7','ปุ่มทั้งหมด: God of War Ragnarök'),
    ('8570a28b567efb150998f4e15cebed739de8dcc6c72b66747d9f66b10022607a','ถามโซนของเกม'),
    ('1806def707336a05166ef9b2589b66cb0450c840866d7ea5f6b920dccd0823f8','ถามเกมที่เล่นได้หลายโซน'),
    ('044f667114ab611667f0d97496b6ba029d49dfd88337fc90123cd7a189623458','ทราบระยะเวลาแล้ว แต่กฎคำนวณยังไม่ประกาศ'),
    ('4b0fb4a4344134b1f575032bdf52be169e19f555edfefbda347310760b6c859d','รักษาบริบทการแข่งขัน')]:
    measured=point_rows.get(key,rows[key]);revision='revision04' if key in point_rows else 'revision03'
    a=measured['response'];b=old[key]['response'];u=(a.get('decision_artifact') or {}).get('understanding') or {}
    report += [f'### {label}','',rows[key]['question'],'','**R115**','','```text',b.get('answer',''),'```','',
       '**R117 '+revision+'**','','```text',a.get('answer',''),'```','',
       '**แผนที่ใช้**','','```json',json.dumps({'reason':u.get('reason'),'tasks':u.get('tasks'),'model_schema_ok':u.get('event',{}).get('schema_ok'),'independent_review':u.get('event',{}).get('meaning_review')},ensure_ascii=False,indent=2),'```','']
report+=['## สิ่งที่ยังต้องพัฒนา','',
    '- การตีความของโมเดลและกฎอิสระยังผิดได้ ไม่ใช่ semantic proof; เงื่อนไขที่ซับซ้อนและการผูกเงื่อนไขให้ถูกคำถามย่อยยังต้องตรวจเพิ่ม',
    '- ตัวคำนวณ count/group/compare/recommendation บางกรณียังไม่ครบ การเข้าใจเจตนาถูกไม่ได้ทำให้ reader ที่ยังไม่รองรับทำงานนั้นได้ทันที',
    '- บางชื่อ/ความสัมพันธ์/metadata และ source validity ยังขาดหรือขัดแย้ง บุคลากร public_scope unknown ยังถูกกันไว้ ต้องให้เจ้าของยืนยันผ่านขั้นตอนข้อมูลจริง',
    '- Billing arithmetic ที่ไม่ประกาศยังไม่คำนวณยอดรวมใหม่ การให้ recorded unit rates แบบ partial มีประโยชน์กว่าเดิม แต่ยังไม่ใช่คำตอบยอดรวมที่สมบูรณ์',
    '- ยังมี compatibility paths สำหรับการตีความไม่สำเร็จหรือหมวด general จึงไม่อ้างว่ากำจัด unrelated retrieval/metadata presentation ได้ทุกแบบ',
    '- การใช้โมเดลวิเคราะห์เพิ่มมีต้นทุนเวลา และ cold start อาจทำให้ model call timeout แม้ HTTP chat จะคืนคำตอบได้ ต้องอ่าน transport แยกจาก correctness',
    '- Booking รอบนี้ยัง controlled unavailable ไม่มีการพิสูจน์สถานะเครื่องว่างจริง และ candidate ไม่ติดตั้งทับ R78', '',
    '## เวลาและ transport ของรอบล่าสุด','',
    '```json',json.dumps({'revision03_48_keys':new['latency'],'saved_r115_same_48_keys_median_sec':statistics.median(x['elapsed_sec'] for x in old.values()),'revision03_model_transport':new['model_transport'],'revision03_integrity':done,'revision04_final_integrity':latest_done},ensure_ascii=False,indent=2),'```','',
    '## เอกสารและหลักฐาน','',
    '- [Flow และรายละเอียด implementation](FLOW_TH.md)',
    '- [คำตอบและแผนทุกข้อของ revision03](http03/analysis/REPORT_TH.md)',
    '- [คะแนน JSON](http03/analysis/COMPARISON.json)',
    '- [Raw HTTP / PipelineAnswer / grades](http03/RESULTS.jsonl)',
    '- [Contract checks 22 จุด](CONTRACT_CHECKS.json)',
    '- [Raw ของ 8 ข้อหลังแก้สุดท้าย](http04/RESULTS.jsonl)',
    '- [ยืนยันรอบสุดท้าย source/model unchanged](http04/TEST_COMPLETE.json)',
    '- [revision01](full01/analysis/REPORT_TH.md), [revision02](http02/analysis/REPORT_TH.md) และ revision03 เก็บครบ พร้อม FROZEN_SYSTEM ที่ตรวจ hash ก่อนแก้รอบถัดไป','']
(R/'REPORT_TH.md').write_text('\n'.join(report),'utf8')
(R/'STATUS.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(summary,ensure_ascii=False))
