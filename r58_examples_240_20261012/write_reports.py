"""Generate new readable reports from retained evidence, never edit production."""
import sys,json,collections
from pathlib import Path
B=Path(__file__).resolve().parent
S=B.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
sys.path.insert(0,str(S))
from app.knowledge.common.registry import CATALOG
def read(p):return json.loads((B/p).read_text(encoding='utf-8'))
def lines(p):return [json.loads(x) for x in (B/p).read_text(encoding='utf-8').splitlines() if x.strip()]
def link(label,p):return f'[{label}]({(B/p).as_posix()})'
def save(p,text):
    with (B/p).open('x',encoding='utf-8') as f:f.write(text+'\n')
def block(x):return '\n```json\n'+json.dumps(x,ensure_ascii=False,indent=2)+'\n```\n'
M=read('MANIFEST.json');SUM=read('content_final/SUMMARY.json');FAIL=read('content_final/FAILURES.json')
ROWS=lines('content_final/ANSWERS_AND_DECISIONS.jsonl');LLM=lines('LLM_SAMPLE_RESULTS.jsonl')
REJ=read('LLM_REJECTION_DIAGNOSIS.json');sources=read('RESEARCH_SOURCES.json')
pres=read('FINAL_PRESERVATION_RECEIPT_V2.json');edit=read('EDIT_AND_GUARD_SUMMARY.json')
assert len(ROWS)==5020 and sum(x['passed'] for x in ROWS)==4250 and len(FAIL)==770
assert edit['pass']==40 and pres['all_checks_pass']
order=list(M['per_kind'])
intro='''# ชุดทดลอง format กลาง — 240 รายการ / 24 หมวด

**ข้อมูลแยกสำหรับสาธิตเท่านั้น ไม่เกี่ยวกับ Product จริงของ PSU**

วันที่อ้างอิง 12 ตุลาคม 2026 เวลาไทย ชุดนี้ตั้งใจใช้ทดลองเพิ่มข้อมูล ถามคำถาม และแก้ข้อมูลเดิม ไม่ใช่การยืนยันบริการของศูนย์

## เปิดลองใช้

1. เปิด `Open-DEMO-ONLY.cmd` ในโฟลเดอร์นี้
2. จะเปิดหน้าเว็บที่มีแถบ “DEMO ONLY — NOT PRODUCTION” ด้านบน ใช้ฐาน `DEMO_ONLY.sqlite` เท่านั้น
3. เลือกหมวดทางซ้าย จะพบข้อมูลตัวอย่าง 10 รายการต่อหมวด กดรายการเพื่อดูช่องที่กรอกแล้ว
4. ส่วน “ทดลองคำตอบจากข้อมูลที่เผยแพร่” ด้านล่าง ใช้ถามข้อมูลชุดนี้ เลือกไทยหรือ English ได้
5. ถ้าจะแก้ตัวอย่าง: แก้ช่อง → บันทึกร่าง → ตรวจทานและอนุมัติ → เผยแพร่ ฉบับร่างและฉบับอนุมัติยังไม่เปลี่ยนคำตอบจนกว่าจะเผยแพร่

ใช้ Python ที่มีอยู่ใน `../r58_common_content_20261010/system/PSU_Esports_Chatbot_Local/runtime/python` จึงต้องวางชุด r58 เดิมข้างโฟลเดอร์นี้ ยังไม่ใช่แพ็กเกจพกพาที่มี runtime ของตัวเอง

ตัวเปิดใช้งานเลือกพอร์ตว่างเอง เปิดซ้ำจะเปิดหน้าเดิม ไม่ต้องกำหนด URL หรือคัดลอก token หน้า preview อ่านฐานกลางโดยตรงและไม่เรียก WordPress สด

## คำถามเริ่มต้น

```text
ตัวอย่าง Minecraft เล่นยังไง
ตัวอย่าง ข้อมูลศูนย์ 01 ขอข้อมูลทั้งหมดทุกส่วน
ตัวอย่าง ราคาต่อบริการ 01 ขอข้อมูลทั้งหมดทุกส่วน
ตัวอย่าง ราคาเหมาโซน/ห้อง 01 ขอข้อมูลทั้งหมดทุกส่วน
Demo game 05 What is this game about?
Demo rate 01 Show all information
```

สำหรับหมวดอื่น ใช้ชื่อหรือ alias ในไฟล์คำถามที่เก็บไว้ แล้วเติม “ขอข้อมูลทั้งหมดทุกส่วน” ตัวอย่างใช้ `01` ถึง `10` เพื่อแยกรายการที่ชื่อคล้ายกัน

**คำถามทั่วไปยังมีส่วนตอบผิด:** อย่าใช้การเปิดหน้าได้หรือการนำเข้าผ่านเป็นหลักฐานว่าคำถามทุกแบบตอบถูก ผลจริง 5,020 คำถามผ่าน 4,250 ผิด 770 เคส เก็บไว้โดยไม่ลบ

## ข้อมูลมาจากไหน

คำอธิบายเกม 10 เกมค้นจากหน้าผู้พัฒนา/ผู้จัดจำหน่าย ใช้ชื่อ ประเภท เนื้อหา และวิธีเล่นเบื้องต้น แปลและเรียบเรียงสั้น ๆ ส่วนชื่อศูนย์ เครื่อง การติดตั้ง จำนวนคน ราคา ข้อกำหนด ตาราง ปุ่มควบคุม รายการแข่ง ข่าว ทีมงาน และการจับคู่สถานะ API เป็นข้อมูลสมมุติที่เขียนเพื่อทดสอบ

ตัวอย่างปุ่ม `DEMO_KEY_01` ไม่ใช่ปุ่มเล่นเกมจริง URL `example.invalid` และอีเมลตัวอย่างไม่ใช่ช่องทางติดต่อจริง ไม่ได้ตรวจเวอร์ชันล่าสุดหรือเรตอายุ จึงคงเรตอายุเป็น “ไม่ทราบ” คำแปลยังไม่ได้ตรวจโดยมนุษย์

ทุก record มีรหัสขึ้นต้น `demo_` ทุก source ใช้ `fixture/synthetic` และมีคำเตือน ระบบ production ปฏิเสธ source ชนิดนี้ ฐานทดลองต้องเปิดใช้ DEMO อย่างชัดเจนก่อนอ่าน

## เลือกดูตัวอย่างแต่ละหมวด

| หมวด | จำนวน | ตัวอย่างที่กรอกครบ |
|---|---:|---|
'''
for kind in order:intro+=f'| {CATALOG[kind]["owner_form"]} (`{kind}`) | 10 | {link("เปิดตัวอย่าง",f"EXAMPLES_{kind}.md")} |\n'
intro+='\n## ผลและหลักฐาน\n\n'
for label,p in [('รายงานผลและวิเคราะห์ปัญหา','REPORT_TH.md'),('รายการคำถามพร้อมสิ่งที่ควรตอบ','content_final/QUESTIONS_EXPECTED.json'),('คำตอบและเหตุผลที่เลือกครบ 5,020 เคส','content_final/ANSWERS_AND_DECISIONS.jsonl'),('770 เคสที่ยังผิด','content_final/FAILURES.json'),('แหล่งข้อมูลเกม 10 เกม','RESEARCH_SOURCES.json'),('หลักฐานข้อมูลจริงไม่เปลี่ยน','FINAL_PRESERVATION_RECEIPT_V2.json')]:intro+='- '+link(label,p)+'\n'
intro+='\nการแก้ตัวอย่างบนเว็บหลังวันนี้อาจทำให้ผลต่างจากรายงานเดิม ผลทดสอบนี้อ้างอิง release ใน MANIFEST และ record JSON ที่ส่งออกก่อนแก้ไข\n'
save('README_TH.md',intro)
report='''# รายงานเพิ่มข้อมูลตัวอย่างทุกหมวดและทดลองถาม

**DEMO ONLY — NOT PSU PRODUCTION DATA**

วันที่อ้างอิง: 2026-10-12 เวลาไทย ข้อมูลที่ใช้ตอบเป็นชุดตัวอย่างแยกทั้งหมด ไม่ได้เอาตัวอย่างไปเผยแพร่ในแชทของศูนย์

## 1. สิ่งที่ทำจริง

- ตรวจ catalog ที่ใช้งานจริง: 24 หมวด สร้างหมวดละ 10 รายการ รวม 240 รายการ มีความสัมพันธ์ศูนย์ → โซน → เครื่อง → บริการ → เกม และราคา/กฎ/ขั้นตอน/การแข่งขัน
- 1,550 ช่องข้อมูล: known 1,530 ช่อง, unknown 10 ช่องเรตอายุเกม, not_applicable 10 ช่องรายการแข่งขันก่อนหน้า
- ค้นคำอธิบายเกม 10 เกมจากแหล่งทางการ ข้อมูลร้านและสถานะที่เหลือสมมุติ ไม่สร้างราคาหรือนโยบายจริงเพิ่มเอง
- ผ่าน CommonStore จริง: ตรวจ source/record/reference → บันทึกร่าง → อนุมัติ → เผยแพร่ atomic release ในฐาน DEMO
- เปิดหน้า editor DEMO แยก ใช้ handler/UI ของ r58 พร้อมคำเตือนและ actor ที่ระบุว่าไม่ใช่เจ้าของจริง
- ทดลองแก้เกม ราคา กฎศูนย์ กติกาแข่งอย่างละ 10 รายการในสำเนา DEMO อีกฐาน เก็บ revision เดิมไว้
- เก็บคำถาม คำตอบ สิ่งที่ต้องตอบ เหตุผลการเลือก evidence และเคสผิด ไม่มีการลบ log เดิม

## 2. ผลแยกตามชั้นที่ตรวจ

| ชั้นที่ตรวจ | ผ่าน | ผิด | สิ่งที่พิสูจน์ / ข้อจำกัด |
|---|---:|---:|---|
| นำเข้าและเผยแพร่ | 240 | 0 | รูปแบบและข้อมูลอ้างอิงผ่านในฐาน DEMO |
| CommonAnswerer รวมไทย/อังกฤษ | 4,250 | 770 | 5,020 คำถาม ไม่เรียก LLM/WordPress |
| ขอทุกข้อมูล (subset ข้างบน) | 480 | 0 | ทั้ง 240 รายการ × 2 ภาษา ตอบค่าและ evidence ครบ |
| ถามตามชื่อช่องข้อมูล | 2,970 | 130 | รวม 3,100 เป็น contract test ไม่ใช่ทุกคำถามที่ลูกค้าจะใช้ |
| ถามภาษาทั่วไป | 210 | 270 | 480 เคส: เจตนาหลักหนึ่งแบบต่อหมวด × 10 × 2 ภาษา |
| ถามต่อจากประวัติ | 220 | 260 | 480 เคส ประวัติระบุรายการก่อนแล้วถามหัวข้อต่อ |
| พิมพ์เบิ้ลชื่อรายการ | 370 | 110 | 480 เคส ดัดชื่อด้วยตัวซ้ำหนึ่งตำแหน่ง ไม่ครอบคลุม typo ทุกชนิด |
| HTTP preview ของ editor จริง | 480 | 0 | ทวนคำถามขอทั้งหมดผ่าน API; อ่าน record กลับตรง JSON ครบ 240 |
| AnswerQualityPipeline จริง | 480 | 0 | เข้า entry ของแชทในสภาพแวดล้อม DEMO; all-fields ไม่มี LLM/RAG/WordPress |
| ตัวอย่างภาษาทั่วไปพร้อม LLM | 23 | 25 | 48 เคส 1 รายการต่อหมวดต่อภาษา ใช้ Typhoon2.5-Qwen3-4B จริง |
| แก้ข้อมูลเดิม | 40 | 0 | 4 หมวด × 10: ร่าง/อนุมัติยังไม่เปลี่ยน live, เผยแพร่แล้วเปลี่ยน, v1 คงเดิม |
| หน้ารายการบน browser | 24 หมวด | 0 หมวด | เห็นหมวดละ 10 และลองคำถาม Minecraft/ศูนย์ ไม่ใช่ส่ง 5,020 ผ่าน browser |

แถวบางส่วนใช้คำถามซ้ำกับชุดหลัก **ห้ามบวกทุกแถวเป็นจำนวนเคสไม่ซ้ำ** ตัวอย่างคล้ายกันตามโครงสร้าง 10 รายการ ผลไม่ได้ประมาณความแม่นยำของลูกค้าจริงทั้งหมด

ไทยผ่าน 1,980/2,510 (78.88%) อังกฤษผ่าน 2,270/2,510 (90.44%) รวม 84.66% คำถามขอทั้งหมดผ่าน 100% ในชุดนี้ แต่คำถามทั่วไปผ่าน 43.75% เท่านั้น จึงยังไม่พอจะรับรองว่าใส่ format แล้วตอบได้ทุกสำนวน

## 3. วิธีตัดสินว่าตอบถูก

ตรวจ target record/field ที่กำหนดไว้ล่วงหน้า, ค่า known ที่ควรปรากฏครบ, unknown/not_applicable, และ source/locator ของ evidence ที่ใช้ตอบ ไม่ใช้แค่ HTTP 200 หรือข้อความที่อ่านดูคล้ายถูก ไม่ส่ง expected_fields ให้ LLM เพื่อช่วยตอบ

ค่าข้อมูลอ้างอิงที่ UI แสดงเป็นชื่อรายการต้องตรงกับชื่อใน fixture; ค่าซ้อน เช่นขั้นตอน/contact ต้องตรวจ leaf value ตาม field ที่อ้างอิง รายงานรอบแรกพบ scorer ที่เทียบรหัส contact กับชื่อแสดงผล จึงแก้ scorer แล้วสร้างผลรอบใหม่ เก็บรอบแรกไว้ไม่ปะปนกับผลสรุป

ชุดหลักใช้ snapshot ของ release ที่ผ่าน validation และไม่เปลี่ยนระหว่างรัน พร้อมตรวจ epoch ต่อคำตอบ ใช้ 4 process เพื่อทำงานให้ครบ จึง **ไม่ใช่ benchmark latency/concurrency ของเว็บ** การทดสอบ HTTP และ pipeline แยกต่างหาก ไม่ได้ยืนยันสถานะจองจริง

## 4. ผลทุกหมวด

จำนวนคำถามต่างกันตามจำนวน field ในหมวด ทุกหมวดมีข้อมูล 10 รายการเท่ากัน

| หมวด | ตัวอย่าง | คำถาม | ผ่าน | ผิด | ผ่าน % |
|---|---:|---:|---:|---:|---:|
'''
for k in order:
    x=SUM['kind/'+k];p=x.get('pass',0);f=x.get('fail',0)
    report+=f'| {CATALOG[k]["owner_form"]} (`{k}`) | 10 | {p+f} | {p} | {f} | {100*p/(p+f):.2f} |\n'
report+='''
## 5. สาเหตุที่มีข้อมูลครบแต่ยังตอบผิด

### 5.1 ชื่อช่องไทยมีคำอังกฤษ แต่การ normalize ไม่ตรงกัน

`field_requests` ทำ NFC/casefold กับคำถาม แต่เทียบ `meaning_th` ใน catalog โดยไม่ casefold ทั้งสองฝั่ง ชื่อช่องมี ISO/API/PC/VR/WordPress/FAQ/TTL จึงหลุดการจับคู่ตรง ขณะที่ EN canonical key มีตัวเล็กอยู่แล้ว

130 เคส contract ที่ผิดเกิดใน 13 กลุ่ม กลุ่มละ 10: closure.local_date; control_set.platform; faq.scope_note; game.age_rating; live_binding.external_resource_key/freshness_policy/status_mapping; resource.name/physical_pool_key; service.booking_product_key/name/occupancy_minutes; zone.name กลุ่มนี้รวมปัญหา keyword และ routing ข้างล่างด้วย ไม่ใช่ทั้ง 130 เคสเกิดจาก casefold อย่างเดียว

### 5.2 จับจำนวนคนเป็น field ผิดหมวด

คำ “กี่คน / players / together” จับเป็น `players_min` แต่ resource ใช้ `capacity_persons`, service ใช้ `capacity_min/capacity_max`, zone ใช้ `capacity`, rental ใช้ `room_seats` และ game_mode ที่ถามได้สูงสุดต้องตอบ `players_max` ระบบค้นเจอรายการถูกแต่ requested_fields ไม่ตรง จึงไม่พิมพ์ข้อมูลที่ควรตอบ

### 5.3 คำในชื่อรายการถูกนับเป็นหัวข้อคำถาม

alias เช่น “วิธีเล่นและปุ่ม” ของ control_set มี keyword จึงดึง how_to_play/bindings/steps แม้ผู้ถามอยากรู้แพลตฟอร์ม ต้องแยกข้อความชื่อรายการออกก่อนตีความส่วนที่ถาม มิฉะนั้นเพิ่ม alias อาจทำให้หัวข้อแทรกเพิ่ม

### 5.4 keyword ข้ามหมวด และไม่แยกคำปฏิเสธ

ชื่อ field เรตอายุมีข้อความ “ไม่ใช่นโยบายรับเด็กของศูนย์” แต่คำ “นโยบาย” กระตุ้น details และทางแยกกฎแข่งขัน จากนั้นเปลี่ยน target จาก game เป็น competition ทำให้ age_rating ของเกมหาย ปัญหาเป็น routing จากคำประกอบ ไม่มีหลักฐานว่า DB ไม่มีเกม

### 5.5 ถามต่อแล้วยังไม่รู้ว่าจะเอา field ไหน

บาง log มี method `history_exact:pending_fields`: ประวัติช่วยระบุ record ได้แล้ว แต่ “ต้องใช้หลักฐานอะไร” ยังไม่ได้ mapped ไป required_proofs จึงถามซ้ำกว้าง ๆ ไม่ได้แปลว่าประวัติสูญหายทั้งหมด ต้องดู record_ids และ requested_fields แยกกัน

### 5.6 พิมพ์เบิ้ลยังพลาดได้หลายสาเหตุ

110 เคสไม่ใช่ทั้งหมดจับชื่อไม่เจอ บางเคสจับ record ถูกแต่หัวข้อยังผิดเหมือนคำปกติ จึงต้องเทียบคู่ clean/typo ก่อนสรุปว่า fuzzy ไม่ดี Threshold และ margin ป้องกันชื่อคล้ายกัน 01–10; ห้ามลด threshold เพื่อให้ตอบเร็วโดยเสี่ยงเลือกอีกเครื่องหรืออีกราคา

### 5.7 เปิด LLM แล้ว schema ยังปฏิเสธ และบางเคสไม่เรียก LLM

48 เคส sample: planner ถูกเรียก 22 ครั้ง ยอมรับ plan 2 ครั้ง ตอบถูก 23/48 บางเคสที่จับ field ได้แล้วแต่ผิดหมวดไม่เข้าประตูเรียก planner จึงเพิ่ม LLM อย่างเดียวไม่แก้ทั้งหมด

health รายงาน 22 successes / 0 failures คือเรียกโมเดลและ decode ได้ ไม่ได้หมายความว่า accepted plan หรือคำตอบถูก 22 ครั้ง `checked_plan` ตรวจ field กับ platform อีกชั้น แต่ schema ที่ส่งโมเดลยอมให้ platform เป็น string ใดก็ได้

ตรวจ raw ใหม่ 6 เคสที่ครั้งแรก plan ถูกปฏิเสธ พบทั้ง 6 ครั้งใส่ platform ผิด: `unknown` หรือ `demo_audience_01`/`demo_closure_01`/`demo_competition_01`/`demo_competition_rule_01` แทน null/ชื่อแพลตฟอร์ม หลายกรณี requested_fields ถูกแล้วแต่ platform ทำให้ทั้ง plan ถูกปฏิเสธ นี่เป็นเหตุผลที่ยืนยันได้จาก raw สำหรับ 6 probe ไม่ใช่หลักฐานว่าอีก 14 เคสแรกผิดด้วยเหตุเดียวกันทั้งหมด เพราะเป็นการเรียกใหม่

'''
base={r['id']:r for r in ROWS};before=sum(base[r['id']]['passed'] for r in LLM)
report+=f'เคส 48 เดียวกันเมื่อปิด LLM ผ่าน {before}/48 เทียบเปิด LLM ผ่าน 23/48; ไม่ใช่การวัดประสิทธิภาพโมเดลแบบกว้าง และไม่ได้รัน LLM ทั้ง 5,020\n\n'
reasons=collections.Counter(reason for r in FAIL for reason in r['reasons'])
report+='### ป้ายกำกับผิดที่พบ\n\nหนึ่งเคสมีได้หลายป้าย จึงห้ามรวมจำนวนป้ายเป็นจำนวนคำถามผิด\n\n| ป้ายจาก log | จำนวนเคส |\n|---|---:|\n'
for reason,count in reasons.most_common():report+=f'| `{reason}` | {count} |\n'
report+='\n## 6. ตัวอย่างคำตอบผิดพร้อมค่าที่ควรตอบ ทุกหมวดที่ยังผิด\n\nค่าด้านล่างเป็น fixture ไม่ใช่คำตอบจริงของ PSU ชื่อไทย/อังกฤษใน JSON ให้เลือกตามภาษา; การแสดงผลตามปกติควรแนบ evidence\n'
for kind in order:
    match=next((r for r in FAIL if r['kind']==kind and r['style']=='natural'),next((r for r in FAIL if r['kind']==kind),None))
    if not match:report+=f'\n### {kind}\n\nชุดนี้ผ่านทั้งหมด ไม่มีเคสผิดให้ยกจากผลรอบนี้ ยังไม่ใช่รับรองทุกคำถามใหม่\n';continue
    r=read(f'records/{kind}/{match["rid"]}.json')
    expected={k:r['fields'].get(k) for k in match['expected_fields']}
    report+=f'\n### {kind} — เคส {match["id"]}\n\n**ถาม ({match["lang"]}/{match["style"]}):** {match["question"]}\n\n**ตอบจริง:** {match["answer"]}\n\n**ผิดตรง:** {", ".join(match["reasons"])}\n\n**plan ที่เลือก:**'+block(match['decision'].get('query_plan'))+'\n**ข้อมูลที่ควรนำมาตอบ:**'+block(expected)
report+='''
## 7. ลำดับการแก้ที่หลักฐานรองรับ

| ลำดับ | สิ่งที่แก้ | วิธีตรวจว่าแก้จริง |
|---|---|---|
| P0 | normalize ทั้งคำถามและ label catalog ให้เหมือนกัน; แยก entity span ออกจากข้อความถาม | 13 กลุ่ม contract และคำถาม clean/typo เดิม ต้องไม่เสีย exact record/evidence |
| P0 | เลือกจำนวนคน/ความจุ/หลักฐานตาม kind; ให้ schema descriptions ช่วยจับ semantic field | natural/followup ของ audience, resource, service, zone, game_mode; ตรวจ min/max ตามสิ่งที่ถาม |
| P0 | กัน keyword details/นโยบายเปลี่ยน game เป็น competition โดยไม่มีเจตนาการแข่ง; คำปฏิเสธต้องไม่สลับหมวด | age_rating ต้องตอบ unknown ของเกม และคำถามกฎแข่งจริงยังไป competition |
| P1 | schema ของ planner ต้อง enum field ที่รองรับและ platform ที่มีจริง หรือ null; เก็บ rejection_reason/raw แบบเหมาะสม | API success, parsed, checked accepted, answer correct เป็นสี่ตัวชี้วัดแยก |
| P1 | ให้ planner ช่วยเมื่อ detected_fields ไม่มีใน kind ด้วย ไม่ใช่เฉพาะไม่มี field | natural ที่เคยจับ players_min ผิดหมวด ต้องตอบ capacity โดยไม่แต่งค่า |
| P1 | ผูกประวัติ record/field/context ให้ชัด แล้วถามเจาะจงเมื่อยังคลุมเครือ | สองรอบและเปลี่ยนเรื่องใหม่ ไม่ดึง record/ราคาจากเรื่องเก่า |
| P2 | วิเคราะห์ typo เทียบ clean เป็นคู่ รักษาตัวเลขเครื่องและราคา | ไม่เพิ่มการเลือกผิดเครื่อง 01→10 และไม่เพิ่ม alias เฉพาะเคสทุกประโยค |

รอบนี้เพิ่มชุดข้อมูลและทดสอบตามคำขอ ไม่ได้เอา patch routing หรือข้อมูลสมมุติเหล่านี้ไปเปลี่ยนระบบ production เก็บหลักฐานเพียงพอสำหรับแก้ชั้นตีความต่อโดยไม่แก้นโยบายของเจ้าของ

## 8. การแก้ข้อมูลเดิมและการแยกฐาน

40 เคสแก้: game.how_to_play 10, rate.amount_minor 10, policy.details 10, competition_rule.text 10 ใช้สำเนา `edit_demo/DEMO_EDITS_ONLY.sqlite` เท่านั้น ตรวจค่า live ไม่เปลี่ยนตอน save/approve, เปลี่ยนหลัง publish และ v1 ไม่ถูกเขียนทับ ฐาน DEMO หลักคง 240 records/240 revisions/1 release

ลองใส่ fixture เข้า empty production guard store: ถูกปฏิเสธ `Fixture source cannot enter production database`; store นั้นยังว่าง ลองอ่าน DEMO โดยไม่เปิด opt-in: ไม่คืนคำตอบ DEMO

production ของ ROOT และ ready_package ยังมี cc_heads 41 / cc_revisions 41 / cc_releases 0 hash เชิงตรรกะเหมือนใบตรวจ owner-edit เดิม; ready_package เทียบ baseline ที่เก็บก่อน import รอบนี้ด้วย SOURCE ห้าไฟล์ที่เกี่ยวข้องเหมือนกันทั้ง ROOT/CAND/PACK ไม่มีการเขียนแก้โค้ด production รอบนี้

ใบตรวจ V1 เคยนับเฉพาะตาราง legacy `records/releases` ซึ่งเป็นศูนย์ จึงออก V2 เพิ่ม `cc_heads/cc_revisions/cc_releases` ให้ตรง format กลาง เก็บ V1 ไว้และระบุการแก้ใน V2; hash ในทั้งสองใบตรงกัน

## 9. สิ่งที่ยังไม่มีการยืนยันจากมนุษย์

- ความเหมาะสมของคำแปลและคำอธิบายสำหรับเจ้าของจริง: agent_translated เท่านั้น
- อุปกรณ์ที่ติดตั้งจริง ราคา ตาราง กฎ การแข่งขัน แพ็กเกจ จำนวนคน และช่องทางติดต่อ: เป็นข้อมูลสมมุติทั้งหมด ไม่มีการขอหรืออ้าง owner sign-off
- เรตอายุเกม: unknown เพราะไม่ได้ตรวจ rating source ไม่ใช้เป็นเกณฑ์รับเด็กของศูนย์
- ปุ่มจริง เวอร์ชันจริง รายการเกมจริง และสถานะจองจริง: ไม่ได้ตรวจในรอบนี้; live_binding เป็นตัวอย่าง mapping ไม่ได้ต่อ WordPress

ไม่รัน full GT สองหมื่นเคส ไม่ติดตั้งโมเดลใหม่ ไม่ใช้ผล fixture เป็นข้อสรุปว่า API WordPress หรือสถานะสดถูกต้อง

## 10. แหล่งข้อมูลที่ค้นเอง

ใช้เฉพาะคำอธิบายเกมที่เรียบเรียงสั้น ๆ ส่วนข้อมูลร้านสมมุติ ไม่ถือว่าหน้าผู้พัฒนายืนยันเกมที่มีใน PSU

| เกม | แหล่งผู้พัฒนา/ผู้จัดจำหน่าย |
|---|---|
'''
for s in sources:report+=f'| {s["game"]} | [หน้าอ้างอิงทางการ]({s["url"]}) |\n'
report+='\n## 11. ไฟล์หลักฐาน\n\n'
for p in ['MANIFEST.json','RESEARCH_SOURCES.json','content_final/SUMMARY.json','content_final/SUMMARY_BY_CATEGORY.csv','content_final/QUESTIONS_EXPECTED.json','content_final/ANSWERS_AND_DECISIONS.jsonl','content_final/FAILURES.json','content_final/EVALUATION_SCOPE.json','HTTP_SUMMARY.json','HTTP_PREVIEW_RESULTS.jsonl','ACTUAL_CHAT_PIPELINE_SUMMARY.json','ACTUAL_CHAT_PIPELINE_RESULTS.jsonl','LLM_PREFLIGHT.json','LLM_SAMPLE_SUMMARY.json','LLM_SAMPLE_RESULTS.jsonl','LLM_REJECTION_DIAGNOSIS.json','EDIT_AND_GUARD_SUMMARY.json','EDIT_40_RESULTS.json','BROWSER_LIST_CHECKS.json','FINAL_PRESERVATION_RECEIPT_V2.json','DEMO_SCREENSHOT.png']:report+='- '+link(p,p)+'\n'
report+='\nผลส่วนที่รันก่อนปรับ scorer/เร่งการรันอยู่ใน log และ content_round2 เดิม เก็บครบ ส่วน `content_final` เท่านั้นเป็นผลหลัก 5,020 เคส\n'
save('REPORT_TH.md',report)
print(json.dumps({'report_chars':len(report),'readme_chars':len(intro),'llm_baseline_same_48_pass':before,'data_files':len(list((B/'records').glob('*/*.json')))},ensure_ascii=False))
