import hashlib,json,subprocess,uuid
from datetime import datetime
from pathlib import Path

project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=project/'reports'/('r28_competition_composition_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6])
report.mkdir()
Path(__file__).with_name('r28_report_path.txt').write_text(str(report),encoding='utf-8')
files=['app/pipeline/engine.py','app/pipeline/competition_detail.py','app/pipeline/competition_presentation.py','app/core/intent_cue_recovery.py','app/web_api/pipeline_supervisor.py','tools/competition_content_grader_r27.py']
protected=['data/competition_rules/competition_rule_chunks.jsonl','data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl','data/eval/competition_user_r24_2000_20261001.jsonl','data/eval/competition_content_contract_r27_320_20261001.json','data/eval/competition_new_questions_r27_128_20261001.json','data/locales/en/CURRENT','data/curated/service_policy_answers.json','booking_dashboard/center_schedule.json','docs/127_competition_contract_r27_flow_20261001.md']
manifest={}
for relative in files+protected:
    src=project/relative;dst=report/'before'/relative;dst.parent.mkdir(parents=True,exist_ok=True)
    with dst.open('xb') as f:f.write(src.read_bytes())
    manifest[relative]=hashlib.sha256(src.read_bytes()).hexdigest()
for name,data in [('before_manifest.json',manifest),('protected_manifest.json',{r:manifest[r] for r in protected})]:
    with (report/name).open('x',encoding='utf-8') as f:json.dump(data,f,indent=2)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=project,capture_output=True,text=True,encoding='utf-8',check=True).stdout
with (report/'git_status_before.txt').open('x',encoding='utf-8') as f:f.write(status)
flow='''# Flow r28 — ความครบของคำถามกติกาหลายประเด็น

## ขอบเขต

ใช้ source และคำแปลที่ hash ตรง เพิ่มคำถามและคำตอบที่คาดหวังจาก clause ต้นฉบับก่อนแก้ selector. เก็บ owner pending, Gold, นโยบายศูนย์ และ logs เดิม. การตรวจคำแปลทำเองต่อได้ ส่วนกฎที่ขัดหรือ source ขาดต้องรอผู้จัด

## ขั้นตอน

1. ตรึงชุดประเด็นที่ยังไม่ครอบคลุมใน r27 รวมคำถามหลายเรื่องเกมเดียวและ controls: ไม่ระบุเกม, เกมไม่รองรับ, อายุ/ราคาไม่พบ, pause ที่ขัดกัน
2. แต่ละ expected clause มาจาก source ID/hash + approved English overlay; runtime ไม่อ่าน fixture และผล runtime ไม่ใช้สร้าง Gold
3. รัน baseline แยก clean/polite/typo, single/composite/controls. วิเคราะห์ทุก failure ตาม trace พร้อมเนื้อหาที่ควรปรากฏ
4. แก้การตรวจคำถามและการเลือก clause แบบแยกความหมาย ใช้แนวคิดทั่วไป ไม่ใช้ whole-question aliases. ตรวจว่า concept ที่จับหลายเรื่องไม่ตัดเรื่องอื่นและไม่มี head-only answer
5. ตรวจ local scope: ข้อห้าม macro/การติดตั้ง/เงื่อนไขการปรับค่า กับหัวข้ออื่นต้องไม่ถูก exclude ด้วยคำจากคำถามทั้งประโยค
6. เพิ่ม tests เฉพาะ failure จริง รวมคำที่ถูก, negation, game/number preservation และความกำกวม
7. รันชุดใหม่ซ้ำ, ชุดเดิม 320/128/80 และ unit; เมื่อเลือกคำตอบเปลี่ยนให้รัน Gold 2,000 อีกครั้ง เก็บ raw กับ source presence grade แยก
8. สร้าง package รุ่นใหม่ ไม่ทับแพ็กเกจเดิม ตรวจเว็บจริงก่อนนำขึ้น 8090. ใช้ผล r27 worker recycle เป็นหลักฐานเดิม; repeat เฉพาะ gate ที่ implementation ใหม่มีผล
9. สรุปสิ่งที่แก้ได้ ผลจริง ขอบเขต synthetic cases และคำถามเจ้าของที่ยังขาด. อัปเดต Flow ตามความผิดที่พบ

## การรับผล

Positive: game/source ถูก, complete expected clauses ทุกข้อ, first line ตรงหนึ่งประเด็นที่ถาม, validation ผ่าน. Safe controls: clarification/no-answer/conflict ตามหลักฐาน ไม่มีการแต่งข้อมูลอายุ/ค่าธรรมเนียม/คำที่ source ขาด. ไม่ใช้ source-presence pass แทน completeness

## ยังรอข้อมูล

Tekken s03/s07, RoV 6.1.5–6.1.5.1 ฉบับเต็ม, ขอบเขต/ฉบับที่มีผลและ V2 104. รุ่นจอย/นโยบายภาพ/ชื่ออังกฤษทางการเติมได้เมื่อมีข้อมูล. Booking oracle ยังเก็บภายหลัง
'''
with (project/'docs/128_competition_composition_r28_flow_20261001.md').open('x',encoding='utf-8') as f:f.write(flow)
with (report/'flow_initial.md').open('x',encoding='utf-8') as f:f.write(flow)
print(report)
