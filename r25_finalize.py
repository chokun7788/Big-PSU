import hashlib,json,subprocess
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path(Path(__file__).with_name('r25_report_path.txt').read_text(encoding='utf-8').strip())
http=json.loads((report/'http_ready_8090.json').read_text(encoding='utf-8'))
review=json.loads((report/'full_r25_B_source_presence_review.json').read_text(encoding='utf-8'))
units=json.loads((report/'round_C_unit.json').read_text(encoding='utf-8'))
assert http['passed']==http['total']==30
assert http['health']['runtime']['version']=='2026.10.01-competition-format-r25'
assert review['source_presence_passed_after_review']==review['total']==2000
for relative,digest in json.loads((report/'final_code_manifest.json').read_text(encoding='utf-8')).items():
    assert hashlib.sha256((project/relative).read_bytes()).hexdigest()==digest,relative
protected=json.loads((report/'protected_data_verification.json').read_text(encoding='utf-8'))
for relative,entry in protected.items():
    assert hashlib.sha256((project/relative).read_bytes()).hexdigest()==entry['before'],relative
latencies=[row['elapsed_sec'] for row in http['cases']]
summary={'runtime':http['health']['runtime']['version'],'web':'http://127.0.0.1:8090/','unit_tests':units['tests'],'unit_success':units['success'],'http_passed':http['passed'],'http_total':http['total'],'http_latency_min_sec':min(latencies),'http_latency_max_sec':max(latencies),'large_corpus_total':review['total'],'legacy_passed':review['legacy_passed'],'legacy_failed':review['legacy_failed'],'source_presence_resolved':review['source_presence_resolved'],'source_presence_passed_after_review':review['source_presence_passed_after_review'],'protected_files_unchanged':len(protected),'owner_confirmation':'pending; especially Tekken pause scope/penalty and V2 review'}
with (report/'final_verification.json').open('x',encoding='utf-8') as handle:json.dump(summary,handle,ensure_ascii=False,indent=2)
git=subprocess.run(['git','status','--short'],cwd=project,text=True,encoding='utf-8',capture_output=True)
with (report/'git_status_after.txt').open('x',encoding='utf-8') as handle:handle.write(git.stdout)
doc=f'''# ผลส่งมอบ r25: รูปแบบคำตอบกติกาการแข่งขัน

วันที่ 1 ตุลาคม 2026 — เว็บใช้งาน: http://127.0.0.1:8090/

## สิ่งที่แก้แล้ว

- เลือกข้อย่อยที่ตรงคำถามก่อนชื่อหัวเอกสาร ไทย/อังกฤษ
- แยก Technical/Tactical/Emergency และคำถามการสื่อสาร/โควตา ไม่ยืมค่าจากคนละประเภท
- CS2 penalty table ครบ 9 คู่ โดยรวม continuation s54/s55 พร้อมอ้างอิง
- Tekken การตั้งค่าเกม เข้าเส้นทางกติกาและตอบ 3 rounds / 60 seconds
- English RoV tablet/iPad ตอบข้อห้ามและผลตัดสิทธิ์ในบรรทัดแรก
- VALORANT penalties ครบ 5 ประเภทพร้อมเงื่อนไข ไม่ซ้ำ
- Overview ตรวจแต่ละ clause ก่อนจัดหมวด; เว็บแสดง heading/list/table จริง

## ผลทดสอบ

| รายการ | ผล |
| --- | --- |
| Unit + regression | {units['tests']}/{units['tests']} ผ่าน |
| HTTP บนเว็บ 8090 หลังสลับแพ็กเกจ | {http['passed']}/{http['total']} ผ่าน เปิด LLM/semantic แบบเว็บ |
| Ground Truth เดิม 1000 ไทย + 1000 อังกฤษ ตัวตรวจ r24 | {review['legacy_passed']}/2000 ผ่าน, {review['legacy_failed']} ข้อตก source-content matcher |
| ตรวจ {review['legacy_failed']} ข้อที่ตกกลับจาก literal complete source clause | {review['source_presence_resolved']}/{review['legacy_failed']} มีข้อความต้นฉบับรองรับ |
| เกณฑ์มีข้อความ source รองรับหลัง review | 2000/2000; ไม่ใช่การตรวจความหมายครบทุก proposition โดยคน |
| DOM และภาพเว็บ | หัวข้อ/list จริง; ตารางไทย/อังกฤษ 9 แถว 2 คอลัมน์; user HTML เป็น text |
| Protected source/Gold/owner/release pointer hashes | {len(protected)}/{len(protected)} ตรงเดิม |

HTTP 8090 ใช้เวลาประมาณ {min(latencies):.3f}–{max(latencies):.3f} วินาทีในรอบนี้ ตัวอย่างคำถามพร้อมคำเกริ่นบางแบบยังใช้ LLM routing และปรับความเร็วได้อีก

## ทำไมตัวตรวจเดิมยังตก

30 ข้อเป็น exact short fact “PlayStation 5 console used” ภายในบรรทัด English ที่รวมหลาย bullet; ตัวตรวจเลือก fragment 7 tokens จึงตรวจข้อสั้นนี้ไม่พบ อีก 17 ข้อเป็นกฎโทษ VALORANT ซึ่งตัวกรองเลือกเฉพาะเลข/คำ modal บางคำและกรองบรรทัดโทษออกก่อนเทียบ ผลดิบและ Gold เดิมยังอยู่ครบ

## ผู้จัดยังต้องยืนยัน

1. Tekken s07 ให้หยุดได้เมื่อทุกคนเห็นพ้องและมีเหตุเหมาะสม เป็นข้อยกเว้นของ s03 ที่ห้ามหยุดหลังเริ่มเกมหรือไม่ ต้องให้กรรมการอนุญาตหรือไม่?
2. หยุดโดยเจตนา/ไม่จำเป็น เสีย Round, Game หรือ Match FT2 ในแต่ละกรณี? ข้อความ “1 รอบ” กับ “ปรับแพ้ทันที” ยังต้องให้ผู้จัดกำหนดขอบเขต

V2 review queue 104 records ยังรอตรวจและยังไม่ได้ activate canonical policy จากการแก้ format รอบนี้ คำตอบอังกฤษใช้ release ที่ระบบตรวจ hash แล้ว ไม่ถือเป็นหลักฐานการอนุมัติจากเจ้าของ

## เอกสารและหลักฐาน

- Flow ฉบับละเอียด: `docs/125_competition_format_r25_flow_20261001.md`
- Final verification: `final_verification.json`
- ตัวตรวจเดิม: `full_r25_B_summary.json`, `full_r25_B_details.jsonl`
- วิเคราะห์ข้อที่ตก: `full_r25_B_failure_groups.json`, `full_r25_B_source_presence_review.json`
- เว็บจริง: `http_ready_8090.json`; Browser evidence: `ui_verification.json`
- สำเนาโค้ดก่อน/หลัง: `before/`, `after/`; protected hashes: `protected_data_verification.json`

Package ใหม่อยู่ที่ `owner_local_delivery_20261001_competition_format_r25_final/PSU_Esports_Chatbot_Local`; package และ log เก่าคงอยู่ หยุดเฉพาะ launcher เว็บที่ตรวจว่า Codex เปิดเอง ไม่สั่งหยุด Dashboard ของเจ้าของหรือ Ollama
'''
with (report/'FINAL_RESULTS_TH.md').open('x',encoding='utf-8') as handle:handle.write(doc)
with (report/'flow_final.md').open('x',encoding='utf-8') as handle:handle.write((project/'docs/125_competition_format_r25_flow_20261001.md').read_text(encoding='utf-8'))
print(json.dumps(summary,ensure_ascii=False),flush=True)
