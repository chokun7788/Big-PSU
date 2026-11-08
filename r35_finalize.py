import json,hashlib,statistics,sys
from pathlib import Path
W=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
R=Path((W/'r35_report_path.txt').read_text().strip())
package=P/'owner_local_delivery_20261003_conversation_context_r35_finalE/PSU_Esports_Chatbot_Local'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
before=json.loads((R/'before_manifest.json').read_text());protected=json.loads((R/'protected_manifest.json').read_text())
old_tests={k:v for k,v in before.items() if k.startswith('tests/')}
changed=[k for k,v in before.items() if sha(P/k)!=v]
protected_changed=[k for k,v in protected.items() if sha(P/k)!=v]
test_changed=[k for k,v in old_tests.items() if sha(P/k)!=v]
runtime={}
for root in ('app','web_chat'):
 for f in (P/root).rglob('*'):
  if f.is_file() and '__pycache__' not in f.parts and f.suffix!='.pyc':runtime[f.relative_to(P).as_posix()]=sha(f)
package_mismatch=[k for k,v in runtime.items() if sha(package/k)!=v]
assert not protected_changed and not test_changed and not package_mismatch
with (R/'FINAL_RUNTIME_AND_PRESERVATION_AUDIT.json').open('x',encoding='utf-8') as f:json.dump(dict(changed=changed,owner_gold_preserved=len(protected),old_tests_preserved=len(old_tests),runtime_files=len(runtime),package_mismatch=package_mismatch,runtime_sha256=runtime,package=str(package)),f,indent=2)
unit=json.loads((R/'final_E_unit_all.json').read_text())
http=json.loads((R/'final_E_assist_HTTP_SUMMARY.json').read_text())
content=json.loads((R/'final_E_assist_CONTENT_AUDIT.json').read_text())
production=json.loads((R/'final_production_assist_HTTP_SUMMARY.json').read_text())
prod_content=json.loads((R/'final_production_assist_CONTENT_AUDIT.json').read_text())
assert unit['success'] and not http['failed'] and not content['failed'] and not production['failed'] and not prod_content['failed']
rows=[json.loads(line) for line in (R/'final_production_assist_HTTP.jsonl').read_text(encoding='utf-8').split('\n') if line.strip()]
times=[row['wall_sec'] for row in rows]
evidence=json.loads((R/'USER_HISTORY_LOG_EVIDENCE_UTC.json').read_text())
legacy=json.loads((R/'R35_LEGACY_SESSION_SUMMARY.json').read_text())
flow=f'''# Flow r35 ฉบับตรวจสอบแล้ว — เชื่อมคำถามต่อเนื่องกับเอกสารการแข่งขัน

## หลักฐานจากบทสนทนาจริง
วันที่ 3 ตุลาคม 2026 เวลาไทย 15:43 ผู้ใช้ถามรายการแข่งขัน → valorant → ขอกฏการแข่ง → valorant
log รับ history จำนวน {[x['recent_history_count'] for x in evidence]} ข้อความตามลำดับ แต่ context.used_context เป็น false
เมื่อพบชื่อเกม ฟังก์ชัน context_resolver คืนคำถามเดิมทันที ส่วน competition clarification ยังไม่มีตัวรับคำตอบชื่อเกม ทำให้ target lock เลือก games/detail
ตัวเลือก semantic ในกรณีไม่มี facet ยังอาจเลือกข่าว/ความรู้ที่มีชื่อเกมเดียวกัน แม้คำถามขอกติกา
แถบ Version เดิมเป็น r33 เพราะหน้าโหลดก่อนเปลี่ยน server; health และโปรเซสจริงเป็น r34 ไม่ใช่หลักฐานว่า server ยังใช้ r33

## Flow ที่ใช้จริง
1. เว็บเก็บข้อความของหน้าที่กำลังคุย ส่ง user/assistant 10 ข้อความล่าสุดก่อนเพิ่มข้อความปัจจุบัน พร้อม route, universal_intent และ resolved_text
2. server ตรวจ input/ภาษา แล้วเชื่อมบริบทก่อนส่งคำถามเข้า pipeline ไม่ดึงเรื่องย้อนหลังจากทุก session มาปะปน
3. คำตอบชื่อเกมสั้นหลังบอทถามให้เลือกกติกา ใช้คำถามก่อนหน้าและเติมชื่อเกม รักษาหัวข้อ ปี และคำปฏิเสธ
4. หลังรายการเอกสารที่มี ผู้ใช้ตอบชื่อเกม → ขอภาพรวมกติกาของเกมนั้น โดยแยกจากคำถามกำหนดรายการที่จะเปิดรับสมัคร
5. หลังตอบกติกาแล้ว ผู้ใช้เปลี่ยนชื่อเกม → แทนชื่อเดิมครบทั้งชื่อเต็ม/วงเล็บ ไม่ทิ้ง RoV ไว้กับ CS2; เก็บหัวข้อ/ปีเดิม
6. คำถามกติกาที่ไม่ระบุชื่อเกมใช้เกมชัดเจนจากคู่บทสนทนาล่าสุดเท่านั้น ไม่เลือกจากรายการตัวอย่างของบอท ไม่ข้ามเรื่องอื่น ไม่เลือกเกมเดียวจากคำถามหลายเกม
7. คำถามที่ระบุงานใหม่ เช่น VALORANT คือเกมอะไร / What is VALORANT? ไม่รับงานกติกาเดิม กรณีไทยไม่ให้คะแนน เกมอะไร เป็นทั้ง list และ detail
8. ภาพรวมกติกาสั้นต้องเข้าสรุปหลายหมวดจาก source; คำถามเฉพาะต้องตอบข้อกฎตรงหัวข้อ; เอกสารคนละปีต้องตอบว่าไม่มีฉบับนั้น
9. ตรวจทั้ง route/context และเนื้อหา/แหล่ง/ปี ไม่ใช้ validation_ok หรือการเชื่อมต่อสำเร็จแทนคำตอบที่ถูกต้อง
10. สำรองโค้ด → baseline → แก้/ตรวจเนื้อหา → unit/HTTP/UI → package ใหม่ → ตรวจ hash → เปิด8090 โดยเก็บ package และ log เดิม

## รอบที่ทำจริงและผลที่ใช้แก้
- Baseline: HTTP 9/19 ตามสัญญา route/context; ปัญหาซ้ำลำดับผู้ใช้จริง
- A: เพิ่มบริบท; HTTP14/19 ยังมี semantic เลือกข่าวแทนกติกาและ catalogue ไม่เข้า handler
- B: ทดสอบ helper พบ normalize_text เพิ่ม รายการ ซ้ำใน รายการแข่ง; หยุดชุดทดลองก่อนปล่อย
- C: catalogue/short overview; unit504ผ่าน, HTTP18/19 แต่ content17/19 — ภาพรวมหนึ่งคำถามยังได้หัวข้อเดียวและ detailไทยถามกลับ
- D: unit505ผ่าน, HTTP35/35 แต่ content33/35 — ชื่อเต็ม Arena of Valor (RoV) ทำให้ broad overview ไม่ตรง
- E: จัดการชื่อเต็ม/aliasร่วมกัน ตรวจ RoV→CS2 ไม่เหลือชื่อเก่า ผ่าน gates ด้านล่าง

## ผลอัตโนมัติของ finalE
- Unit {unit['tests']}/{unit['tests']} ผ่าน รวม 18 test methods ใหม่พร้อมหลาย subcasesไทย/อังกฤษ
- HTTPโปรไฟล์เปิด Local LLM/semantic: 8091 {http['passed']}/{http['requests']}, เนื้อหา {content['passed']}/{content['requests']}
- HTTPตัวเปิดใช้งานจริง8090: {production['passed']}/{production['requests']}, เนื้อหา {prod_content['passed']}/{prod_content['requests']}
- ชุดบริบทเดิม {legacy['passed']}/{legacy['sessions']} session, {legacy['turns_passed']}/{legacy['turns']} turn ใน D; E เปลี่ยนเฉพาะการแทนชื่อการแข่งขันและตรวจภาพรวม
- HTTPเวลาเครื่องนี้ median {statistics.median(times):.3f}s, max {max(times):.3f}s สำหรับชุดคำถามนี้ มี cache/การอุ่นระบบ จึงไม่ใช่เวลารับประกันทุกคำถาม
- รักษา owner/Gold {len(protected)} ไฟล์ และ testsเดิม {len(old_tests)} ไฟล์; package ตรงกับ source runtime {len(runtime)} ไฟล์
- สำเนาบทสนทนาจริง USER_HISTORY_LOG_EVIDENCE_UTC.json; JSONL/SQLiteเดิมไม่ทับ ผลทุกรอบอยู่ใน reportนี้

## ขอบเขตที่ยังไม่ได้ยืนยัน
- เป็นการทดสอบอัตโนมัติและเทียบข้อความกับเอกสาร ไม่ใช่เจ้าของรับรองนโยบาย/คำแปล/ฉบับการแข่งขัน
- คำถามปลายเปิดที่ไม่มีหลักฐานระบุงานหรือเป้าหมายยังอาจต้องถามเพิ่ม การกู้ชื่อคำผิดใช้ resolverเดิม ไม่เดาคำที่ขาดจนกำกวม
- หน้าเว็บใช้ anonymous session ต่อ page visit; refresh เริ่มบทสนทนาใหม่ตาม profileเดิม แต่ logเดิมยังเก็บบนเครื่อง จึงรักษาแท็บเดิมและเปิดแท็บชุดใหม่แยกให้ทดลอง
- history ที่ส่งจำกัด10ข้อความล่าสุด ไม่ใช่ความจำไม่จำกัด หรือข้ามsession
- เก็บ occupancy WordPress จริงยังพัก งานนี้ไม่มีการจอง/แก้ข้อมูลเจ้าของ/ดึงสถานะจองจริงใหม่
- รายการเอกสาร 4 เกมไม่ใช่รายการกำลังเปิดรับสมัคร ต้องใช้ข้อมูลผู้จัดหากถามงานครั้งถัดไป
- ความขัดแย้ง/ช่องว่าง source ที่บันทึกใน r34 ยังต้องถามเจ้าของ เช่น Tekken pause, RoVข้อ6.1.5.1, อายุ/ค่าสมัคร/roster/edition

## ไฟล์ที่แก้
{chr(10).join('- '+k for k in changed)}
- เพิ่ม tests/test_competition_session_context_r35.py; ไม่มีการแก้ testsเดิมหรือ Gold เพื่อให้ผ่าน
'''
doc=P/'docs/136_conversation_context_r35_verified_flow_20261003.md'
for path in (doc,R/'FLOW_FINAL_TH.md'):
 with path.open('x',encoding='utf-8') as f:f.write(flow)
with (W/'PSU_ESPORTS_R35_HANDOFF_FINAL_20261003.md').open('x',encoding='utf-8') as f:f.write(f'# PSU Esports r35 finalE\n\nProject `{P}`\nReport `{R}`\nFlow `{doc}`\nPackage `{package}`\n\nUnit{unit["tests"]} pass; 8091/8090 HTTP+content35/35 each. Preserve584 owner/Gold and oldtests. 8090 ownership record in web_chat_runs/r35_ready_8090_*.json; 8091 stop ownership record in report. Existing usertab retained; refresh starts anonymousnew chat by existingprofile. New deliverabletab8090tested. Real occupancy remainspaused. No subagents unless authorized; requestprojectwrite permissionsnextturn. Read FLOW_FINAL_TH and raw HTTP/content rounds before work.\n')
print(json.dumps(dict(flow=str(doc),report=str(R),unit=unit['tests'],http=production['requests'],protected=len(protected),old_tests=len(old_tests),changed=changed),ensure_ascii=False))
