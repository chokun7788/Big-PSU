"""Generate separate as-built legacy/common flow documents with source links."""
import ast,json
from pathlib import Path
B=Path(__file__).resolve().parent;R=B/'r90_full_flow_analysis_20261018';L=B/'r64_full_comparison_20261013/system';C=B/'r88_full_common_llm_20261017/system'
M=json.loads((R/'DETAILED_METRICS.json').read_text('utf8'));D=json.loads((R/'DATA_INVENTORY.json').read_text('utf8'))
def link(root,rel,symbol=None,label=None,needle=None):
 p=root/rel;assert p.is_file(),p;src=p.read_text('utf-8-sig');line=1
 if symbol:
  matches=[n.lineno for n in ast.walk(ast.parse(src)) if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name==symbol];assert matches,(p,symbol);line=matches[0]
 if needle:
  matches=[i for i,s in enumerate(src.splitlines(),1) if needle in s];assert matches,(p,needle);line=matches[0]
 return '['+(label or rel+(' :: '+symbol if symbol else ''))+']('+p.as_posix()+':'+str(line)+')'
def local(name,label=None):return '['+(label or name)+']('+(R/name).as_posix()+')'
def write(name,body):
 with (R/name).open('x',encoding='utf8') as f:f.write(body.strip()+'\n')
legacy=r'''
# Full Flow ระบบเดิม — as built ใน snapshot ที่เคยทดสอบ R64

## 0. เอกสารนี้อธิบายอะไร

อธิบายเส้นทางจริงของโค้ด `r64_full_comparison_20261013/system` ซึ่งใช้เป็นฐาน legacy ON ที่นำมาเทียบ R88 ไม่ใช่การอ้างว่าโครงการ Downloads ปัจจุบันยังเหมือน snapshot ทุกบรรทัด ไม่รันระบบเดิมใหม่และไม่คัดลอกคำตอบเก่ามาแทน facts ของข้อมูลกลาง

Flow เป็นต้นไม้ของทางออกที่มีลำดับความสำคัญ ไม่ใช่รายการที่ทุกคำถามต้องผ่านครบ หาก typed handler ตอบได้ก่อน จะไม่เดินถึง retrieval/LLM ส่วนขั้นเว็บต้องแยกจาก batch evaluator ที่เรียก engine ตรง

## 1. แผนภาพรวมตั้งแต่ input ถึง output

```mermaid
flowchart TD
 A["ผู้ใช้พิมพ์ในเว็บ"] --> B["API: ตรวจ payload, locale, input guard"]
 B --> X{"ต้องหยุดที่ guard หรือ replay เดิม?"}
 X -- "ใช่" --> O["ส่งผลที่ถูกต้องตามชนิด พร้อม log/state"]
 X -- "ไม่" --> S["ล็อก session, รับ acknowledge, begin turn/idempotency"]
 S --> T["Typed request plan หรือ context resolver เดิม"]
 T --> W["Admission / worker / request deadline"]
 W --> E["Engine: studio scope / creation-translation boundary"]
 E --> F{"Typed fast exit: ราคาเหมา, navigation, resume, missing slot"}
 F -- "ตอบได้" --> V["Final answer/source/language/task contract validation"]
 F -- "ยังไม่ได้" --> Q["Intent-cue recovery, typed fee, budget, compound plan"]
 Q --> Z{"หลายคำถาม?"}
 Z -- "ใช่" --> K["รักษา subject/dependency แล้วตอบแต่ละ task"]
 Z -- "ไม่" --> P["Single: owner facts / game guard / preprocess recovery"]
 K --> P
 P --> I["Entities + route variants + routing priority"]
 I --> H{"Protected/bilingual/competition/live handler ตอบได้?"}
 H -- "ได้" --> V
 H -- "ไม่ได้" --> J["Freshness, boundary, universal intent, target locks"]
 J --> U["Tool routing + ambiguity + question frame"]
 U --> N["Capability candidates: score, margin, preconditions"]
 N --> R{"Structured หรือ deterministic tool?"}
 R -- "มีคำตอบ" --> V
 R -- "ไม่มี" --> G["Competition fact cards / curated / hybrid retrieval"]
 G --> Y{"มีหลักฐานพอ?"}
 Y -- "พอ" --> V
 Y -- "ไม่พอ" --> LL["Scoped LLM / vector / RAG fallback ตาม flag และ deadline"]
 LL --> V
 V --> VV{"ผ่าน contract?"}
 VV -- "ไม่ผ่าน" --> NO["Safe no-answer + rejected draft diagnostics"]
 VV -- "ผ่าน" --> O
 NO --> O
 O --> END["Commit state, JSON sources/trace, async log, frontend แสดงผล"]
```

หมายเหตุ: engine เดิมมี optional common/canonical checkpoints ด้วย แต่แขน legacy ที่เก็บผลไม่ได้หมายถึง current migrated dispatcher; การมีโค้ด checkpoint ไม่ใช่หลักฐานว่ามีการใช้ common facts ในทุกคำถาม

## 2. ชั้นข้อมูลที่ระบบเดิมใช้อยู่

| ประเภท | แหล่ง/ตัวอ่านหลัก | สิ่งที่ระบบต้องเลือกให้ถูก |
|---|---|---|
| กฎศูนย์/FAQ/ช่องทางติดต่อ | rules, owner service facts, static-domain และ curated sources | intent, เงื่อนไข, สิทธิ์/ขอบเขต ไม่ใช่แค่คำที่เหมือนกัน |
| ราคาใช้บริการ | service fee calculator + structured price facts | บริการ, กลุ่มผู้ใช้, หน่วยราคา, ระยะเวลา, เงื่อนไขต้นฉบับ |
| ราคาเหมา | zone_rental parser + package source | โซน, ภายใน/ภายนอก, ครึ่งวัน/เต็มวัน แบบ tuple ต่อ clause |
| เกม/อุปกรณ์/บุคลากร | structured resolver, fact composer, curated/canonical information | entity/edition, field, จำนวน/ความหมายของที่นั่ง, ความสัมพันธ์ |
| วิธีเล่น/ปุ่ม | game-control parser + source mappings + partial-control caveats | เกม/แพลตฟอร์ม/โหมด/action และข้อจำกัดการตรวจปุ่ม |
| กติกาแข่ง | locked rulebook registry + source sections/fact cards/detail predicates | เกม/รายการ/ปี, facet, proposition และเงื่อนไขเต็ม |
| ตารางบริการ | service calendar + source schedule/closures | วัน/เขตเวลา, เปิด, จองได้, Maintenance, วันปิดพิเศษ |
| สถานะจองสด | live booking adapter: dashboard หรือ WordPress ตาม config | วันที่, ช่วงเวลา, หมวด/หมายเลขเครื่อง, occupancy snapshot |
| ความรู้ที่ค้นไม่ตรง | curated lexical/hybrid/vector หรือ scoped LLM ตาม gate | มี studio anchor, ownership/source authority และ validation |

ข้อมูลเดิมจึงไม่ได้อยู่ในไฟล์เดียว และ parser/renderer หลายหมวดรู้โครง source ของตัวเอง การย้ายเฉพาะค่าข้อมูลไม่เท่ากับย้ายความสามารถอ่านข้อมูลเหล่านี้

## 3. Web/API/session layer

1. Frontend ส่ง question, locale, client_session_id, client_turn_id และการ acknowledge คำตอบก่อนหน้าเมื่อมี
2. API ตรวจขนาด/รูป payload, input quality, ภาษา และ admission ก่อนทำงานหนัก
3. ต่อ session มี lock; turn เดิมกับ fingerprint เดิม replay ได้โดยไม่เรียกตอบซ้ำ ส่วน turn ID ชนกันแต่ payload ต่างกันเป็น conflict
4. ประวัติที่เชื่อถือได้มาจาก conversation store และ delivery/acknowledge ไม่ถือทุกข้อความจาก client เป็น server state โดยอัตโนมัติ
5. typed task memory แยกราคา/เหมา/การเลือกตัวเลือก/การกลับไป task เดิม หากไม่มี typed plan จึงใช้ context resolver
6. worker supervisor/job queue เป็นชั้นตาม config: busy, pending, restarting และ timeout เป็น response type แยกจากคำตอบข้อมูล
7. หลังตอบ เก็บ actual task contract และ state เฉพาะสิ่งที่ส่งจริง ไม่ใช่ทุกสิ่งที่ assistant เคยเสนอเป็นตัวเลือก
8. API แสดง answer, source list, mode/trace/debug ตามการตั้งค่า และบันทึก log แบบ async

**ห้ามตีความ** API200 = เนื้อหาถูก; replay สำเร็จ = อัปเดต facts แล้ว; มี history = ทุก task จะสืบต่อถูก

## 4. Engine entry: ลำดับที่มีสิทธิ์จบก่อน

| ลำดับ | ขั้น | เงื่อนไข/สัญญาที่รักษา | ทางออก |
|---|---|---|---|
| L01 | locale + deadline + booking snapshot context | ภาษาและกรอบเวลาคำขอเดียวกัน | context สำหรับขั้นถัดไป |
| L02 | studio scope / creation / translation boundary | ไม่ขยายบอตเป็นผู้ตอบทุกเรื่อง | scoped refusal |
| L03 | optional knowledge checkpoint | ต้องตรง profile/ฐานที่อนุญาต | answer หรือส่งต่อ |
| L04 | affirmative request focus | ทิ้งเฉพาะ task ที่ผู้ใช้ปฏิเสธอย่างชัดเจน | active question |
| L05 | zone rental plan | รักษา zone/audience/period และ tuple ของคำถามผสม | source-backed package answer/clarification |
| L06 | dialogue state clarification/navigation/resume/selection | “ทั้งหมด”, “อันแรก”, “กลับไป” ต้องมีแกนที่ยืนยันได้ | typed clarification หรือ resume |
| L07 | unsupported numbered game/edition/control target | ไม่เดารุ่น/เกมที่ไม่มีหลักฐาน | explicit unsupported/no-answer |
| L08 | generic control missing game | “ปุ่มยิงกดอะไร” ยังขาดชื่อเกม | ขอชื่อเกม ไม่ดึงปุ่มเกมอื่น |
| L09 | intent-cue recovery + source operation splitter | แก้ cue และรักษาหลาย operation ของ subject เดียว | clauses/tasks |
| L10 | budget + typed fee conversation | จำนวนเงิน/กลุ่ม/เวลาไม่สลับ slot | calculator/targeted clarification |
| L11 | optional canonical knowledge | เปิดตาม flag และช่วงภาษาที่รองรับ | source answer หรือส่งต่อ |
| L12 | compound complexity/query planner | กติกาเกมเดียวไม่แตก “conduct and etiquette” เป็นคนละเกม | single หรือ multi task |

## 5. การแก้คำผิดและ routing ของ single-question path

คำถามบางชนิดตอบจาก fast facts/guard ก่อน preprocessing ได้ หากยังไม่ได้ จึงเข้า preprocessing ดังนี้

1. ตัด conversational preface ที่ไม่เปลี่ยนสาระ โดยเก็บ raw input ไว้
2. ฟื้นชื่อเกมแข่งขันที่มี registry และรูปอักษร `เเ` → `แ`
3. keyboard-neighbor recovery
4. Thai transposition recovery
5. multi-error phrase recovery
6. intent-cue recovery
7. game-title variants เฉพาะบริบทที่เข้าเงื่อนไข พร้อมป้องกันการเปลี่ยน verified service label เป็นชื่อเกม
8. เก็บ variants ไม่เกิน 8 รูป; รักษา explicit competition target และตัวเลข/edition ไม่ให้ recovery เปลี่ยนเกมที่ผู้ใช้ระบุ
9. extract_entities → route_intent → routing_priority_policy
10. ประเมิน variant เมื่อ route ยังอ่อน; เทียบ route candidate ตาม threshold/margin ของโค้ด ไม่ใช่เลือกคำตอบที่คะแนน factual สูงกว่า

**จุดเด่น:** recovery มีหลาย error channel และเป็นระดับ task cue ไม่ได้มีแค่ alias ชื่อเกม

**ความเสี่ยง:** recovery อาจแปลงเจตนาหรือเกมถ้าขาด anchor protection; การเพิ่ม alias อย่างเดียวไม่แก้การรักษา negation, จำนวน, subject หรือหลาย task

## 6. ชั้นเลือกตัวตอบ: rule, intent, frame และ capability ไม่ใช่ชั้นเดียวกัน

### 6.1 RuleMatcher

โหลด trusted rules, compile pattern แล้วเรียง priority สูงก่อน Pattern ที่ match ระบุ category/intent และ source/answer ของ rules เดิม English ไม่ fallback ไป Thai prose โดยเงียบ หากไม่มี English ที่ใช้ได้จะเข้าทางปลอดภัยของ bilingual path

คะแนน priority เป็นลำดับกฎ ไม่ใช่ probability ว่าข้อมูลถูก การมี regex ตรงก็ยังต้องผ่าน source/answer contract

### 6.2 Protected handlers และ target locking

มีการตอบ owner facts, social/identity, protected intents, bilingual English, competition catalog/overview/detail และ live booking ก่อนตัวเลือกทั่วไปบางชั้น แต่ละ branch อาจ return ได้ทันที

ชื่อเกม/รายการที่ระบุชัดถูก lock เพื่อไม่ให้ universal intent หรือ tool router เปลี่ยนเป็นเกมที่คำคล้ายกว่า หาก target ไม่อยู่ในข้อมูลต้องแจ้งไม่ยืนยัน ไม่ดึงกติกา VALORANT มาตอบแทนเกมอื่น

### 6.3 Universal intent → tool routing → ambiguity → question frame

ใช้ domain/operation/target/เงื่อนไขเพื่อ refine route; semantic lock และ game lock ต้องคงอยู่ ต่อด้วย freshness/boundary/ambiguity checks ก่อนเรียก tool ตัวใด ไม่ใช่ให้ LLM เลือกแล้วเชื่อทันที

### 6.4 Capability scoring

ความสามารถ candidate มี base score, bonus/penalty ตาม route, intent, tool decision และ question frame จากนั้น normalize score ด้วย `/1.80` และ clamp ไม่เกิน `.999`

- ไม่มี candidate ที่รับได้ → ไม่อนุญาต execution
- score ต่ำกว่า `.45` → abstain
- margin ต่ำกว่า `.035`, action ต่างกันและ operation ยัง unknown → review_required
- margin ต่ำแต่ action เหมือนกัน/รู้ operation อาจยังอนุญาต execution

ตัวเลขนี้เป็น **ranking heuristic** ไม่ใช่การวัดว่าคำตอบมีโอกาสถูกกี่เปอร์เซ็นต์ ต้องอ่าน reasons, preconditions และ source ต่อ

## 7. Domain subflows

### 7.1 ราคาใช้บริการและราคาเหมา

```mermaid
flowchart LR
 A["คำถาม + task state"] --> B["แยก service/zone, audience, duration/period"]
 B --> C{"ขาด slot ที่มีผลต่อราคา?"}
 C -- "ขาด" --> D["ถามเฉพาะ slot ที่ขาด"]
 C -- "ครบ" --> E["อ่าน fee/package source ตาม billing basis"]
 E --> F["คำนวณเฉพาะสูตรที่ source อนุญาต"]
 F --> G["แสดงราคา + หน่วย + กลุ่ม + เงื่อนไข + citation"]
```

half-day/full-day ไม่เท่ากับจำนวนชั่วโมงจนกว่าจะมี source; จำนวนที่นั่งไม่ใช่จำนวนผู้เล่นพร้อมกันโดยอัตโนมัติ; ราคา VR30 นาทีไม่ใช่สิทธิ์ให้ slot อีกครึ่งชั่วโมงว่างให้คนอื่นจอง การกันชั่วโมงเต็มเป็น occupancy policy อีกชั้น

**ข้อจำกัดเดิมที่ต้องคงไว้ในการเทียบ:** บาง renderer อ่านตารางราคาเดิมได้ตรงตาม oracle แต่ไม่ได้มี validity behavior เท่ากับข้อมูลกลางปัจจุบัน การตอบตัวเลขได้จึงไม่ยืนยันว่าเป็นราคาปัจจุบัน

### 7.2 เกม/อุปกรณ์/ปุ่ม

entity resolver → exact/ambiguous/unknown target → structured game/equipment fact → requested operation (overview/list/how-to/controls) → source control/action rows → partial-data warning → citations

หากไม่มีชื่อเกมใน control request ต้องขอชื่อเกม; ถ้าเป็นรายชื่อเกมในโซนต้องไม่ตีความ “เล่นได้ไหม” เป็น live vacancy โดยอัตโนมัติ; ถ้า source ปุ่มยังไม่ตรวจจริงต้องบอกสถานะนั้น

### 7.3 กติกาแข่งขัน

```mermaid
flowchart TD
 A["ชื่อเกม/รายการ/ปี + คำถามกติกา"] --> B["ล็อก rulebook target"]
 B --> C{"ขอบเขตคำถาม"}
 C -- "ภาพรวม" --> D["เลือก substantive clauses หลาย facet พร้อมระบุว่าเป็นบางข้อ"]
 C -- "ทั้งหมด" --> E["อ่าน source sections ตามลำดับพร้อม coverage"]
 C -- "เฉพาะประเด็น" --> F["detail concepts / requirements / exact clauses"]
 F --> G["รักษา conditions, exceptions, penalties, dependencies"]
 D --> H["ตอบพร้อม source และ edition"]
 E --> H
 G --> H
```

“ประท้วง” ต่างจาก “ใช้ภาษาอะไรในการประท้วง”; “จำนวนผู้เล่นในเกม” ต่างจาก roster/substitute; “เวลานอก” ต่างจาก technical pause ต้องไม่ใช้ clause ของอีก proposition มาแทน

### 7.4 ตารางและสถานะจอง

คำถามเปิด/ปิดรายวันใช้ calendar/closures และเขตเวลาไทย ส่วนเครื่องว่างตามเวลาใช้ live adapter

- `dashboard` mode: อ่าน local status service ที่ต้องพร้อมทำงาน
- `wordpress` mode: ดึง source ผ่าน WordPress adapter ตาม config ไม่ใช่กดเปิด batch ใหม่ทุกคำถาม
- อุปกรณ์ทั้งหมวด: เลือก family แล้วสรุปว่างกี่เครื่องจากทั้งหมด พร้อมรายเครื่องตามคำถาม
- ถาม “มีอะไร **ว่าง** ให้เล่น”: ไม่แสดงเครื่องที่ไม่ว่างปนเป็นรายการว่าง
- ยืนยัน transport/schema ≠ ยืนยัน occupancy; ต้องมี known-result fixture หรือ ground truth แยก
- VR30 นาทีอาจกัน occupancy เต็มชั่วโมงตามนโยบายที่ผู้ใช้ยืนยัน ห้ามนำกฎนี้ไปเปลี่ยนราคาเอง

### 7.5 FAQ/นโยบาย/ขั้นตอน

ตรวจ source ownership และ qualification ก่อนตอบ เช่น สลิปผิด/หลักฐานตัวตนผิด/ยอดชำระผิด เป็นคนละ task แม้มีคำว่า “หลักฐาน/ผิด/แก้” ร่วมกัน หาก source ครอบคลุมเพียงพื้นที่รับประทานอาหาร ต้องไม่ขยายเป็นทุกเงื่อนไขการนำอาหารจากภายนอก

## 8. Retrieval และ LLM fallback

เมื่อ structured/deterministic ไม่ตอบ จะพิจารณา fact cards/curated/hybrid ตาม route และ target; ใช้ vector/RAG/scoped general LLM เมื่อ flags, studio anchor, evidence และ deadline อนุญาต

LLM ON จึงไม่ได้บังคับทุกคำถามให้ generate คำตอบ และไม่ใช่เหตุผลให้ปิด safety/ownership checks หากหาข้อมูลไม่ได้ ทางสุดท้ายยังเป็น no-answer/clarification พร้อมร่องรอยเหตุที่เลือก

## 9. Validation และ output contract

`_build_result` รวม validation จากตัวตอบ กับ source/language checks เพิ่ม หากไม่ผ่าน hard veto จะเปลี่ยนเป็น safe no-answer, ล้าง hits และบันทึก rejected mode/route/errors

**จุดที่อ่านผลผิดได้:** final `validation.ok=True` อาจหมายถึง “คำตอบปฏิเสธที่ปลอดภัยผ่านแล้ว” หลัง veto ไม่ได้หมายถึง draft ก่อนหน้าถูกต้อง ต้องอ่าน warnings, rejected errors และ task_answer_contract ด้วย

decision_artifact และ trace เก็บ route, intent, selected capability, source/evidence, coverage, timing และ fallback; server commit เฉพาะผลที่ส่งจริงแล้วจึงส่งให้ frontend

## 10. การเพิ่ม/แก้ข้อมูลในระบบเดิม

1. ระบุ authoritative source และหมวดที่เกี่ยวข้อง
2. แก้ rules/structured facts/curated/canonical data ตาม provider นั้น ไม่มีกติกากลางเดียวครอบคลุมทุก provider
3. หากมีตารางหรือ index/cache ให้ rebuild/invalidate ตามตัวอ่าน
4. ตรวจ parser/renderer ว่ารองรับ field, new entity, edition และ relationship ใหม่หรือไม่
5. ทดสอบโจทย์เดิมและโจทย์ของข้อมูลใหม่ พร้อม provenance และ validity

ข้อดีคือ interpreter/renderer เฉพาะหมวดพัฒนาสะสมมามาก แต่การดูแลข้อมูลหลายโครงและ vocab/source-specific code มีต้นทุนสูง ไม่ควรนำไฟล์คำตอบเดิมมาทับข้อมูลกลางเพื่อให้คะแนนกลับมา

## 11. ปัญหาที่พิสูจน์แล้วใน snapshot เดิม

- legacy ON มี 2,694 execution exceptions: **2,692 เป็น NameError `ownership_blocked`**, อีก 2 เป็น harness timeout30s; ชื่อแปรถูกใช้ใน retrieve_curated แต่ assignment ที่พบอยู่ใน function อื่น จึงไม่ควรคัดลอก retrieval เก่าทั้งชุดมาใช้
- คะแนน strict อิง schema/route เดิม จึงได้เปรียบด้าน protocol โดยธรรมชาติ
- ตัวตรวจข้อความอาจให้ผ่านเพียงคำจำเป็นบางคำ แม้คำตอบไม่ครอบคลุมทุกข้อจริง
- การอ่านตารางเดิมได้ไม่รับรอง current validity, ขอบเขตนโยบายใหม่ หรือการตรวจแปลโดยเจ้าของ
- fallback หลายชั้นและ source หลายแบบทำให้รักษา task/ownership/ภาษาให้สม่ำเสมอยาก

ข้อมูลคะแนนและความผิดพลาดทั้งหมดดูเอกสารวิเคราะห์คู่กัน ไม่สรุปว่าเดิมถูกทุกข้อจากคะแนน94.41%
'''
legacy+='\n## 12. จุดอ้างอิงโค้ดที่ตรวจ\n\n'+'\n'.join('- '+x for x in [link(L,'app/web_api/server.py','do_POST'),link(L,'app/pipeline/engine.py','answer'),link(L,'app/pipeline/engine.py','_answer_single'),link(L,'app/pipeline/engine.py','_answer_multi'),link(L,'app/pipeline/preprocess.py','preprocess_input'),link(L,'app/rules/matcher.py','RuleMatcher'),link(L,'app/pipeline/capability_registry.py','build_candidate_decisions'),link(L,'app/pipeline/engine.py','_handlers_for_route'),link(L,'app/pipeline/engine.py','_build_result'),link(L,'app/pipeline/retrieval.py','retrieve_curated'),link(L,'app/session/context_resolver.py','resolve_question_with_context')])
write('01_FULL_FLOW_LEGACY_TH.md',legacy)

common=r'''
# Full Flow Format กลาง — as built ใน R88 / โค้ด R87 stage 2

## 0. ขอบเขต: runtime ปัจจุบันเป็น migration preview

ใช้โค้ด/ฐานที่ตรึงจาก R78 หลังติดตั้ง R87 stage2 มี602 heads; profile=`r69-migration-preview` ไม่ใช่ published production profile แม้ชื่อบางช่องใน artifact ใช้ `common_published` ต้องอ่าน `content_view=evaluation_draft` และ `production_publication_verified=False` ประกอบ

ต้องแยก **owner editing/publication flow**, **published reader**, **migration-preview reader**, และ **web/engine execution flow** ไม่ใช้ผลผ่าน schema/preview แทน owner approval

## 1. Full flow ตั้งแต่เจ้าของกรอกถึงผู้ใช้ได้รับคำตอบ

```mermaid
flowchart TD
 A["เจ้าของเลือกหมวด / สร้างหรือแก้ record เดิม"] --> B["Template + typed fields + stable ID + relations"]
 B --> C["Source snapshot / hash / field evidence pointer / revision"]
 C --> D["Schema, references, validity, language and optimistic-version checks"]
 D --> EE["เก็บ draft revision และ audit"]
 EE --> PR["Owner preview เป็นเส้นทางตรวจอีกแบบหนึ่ง"]
 EE --> AP["Approve revision/hash แล้ว publish release เมื่อผ่านเงื่อนไข"]
 AP --> PUB["Normal CommonStore อ่าน active published release"]
 EE --> PRE["R78/R88 MigratedView อ่าน latest draft heads แบบ read-only"]
 U["ผู้ใช้ส่งคำถามจากเว็บ"] --> API["Guard, locale, session, idempotency, queue/deadline"]
 API --> HIST["ใช้ original input + trusted common_read_state; ไม่ใช้ request_plan เดิม"]
 HIST --> EN["Engine studio scope แล้ว return migrated dispatcher"]
 EN --> MD["Greeting / repair / qualified follow-up / common reader"]
 PRE --> MD
 PUB -. "เส้นทาง common ปกติ ไม่ใช่ profile ทดสอบนี้" .-> CR["Typed reader"]
 MD --> CR
 CR --> FAST{"Opening status / rental bridge ตอบได้?"}
 FAST -- "ได้" --> VALID["Current snapshot, evidence, scope, coverage validation"]
 FAST -- "ไม่ได้" --> ENT["Names / context / identity / profiles / operation"]
 ENT --> SEL{"มี record scope แล้ว?"}
 SEL -- "ไม่มี" --> ES["Bounded candidate retrieval + optional LLM entity/profile selector"]
 SEL -- "มี" --> FIELDS["Field needs, task roles, related records, typed plan"]
 ES --> FIELDS
 FIELDS --> FP{"ต้องตีความ field เพิ่ม?"}
 FP -- "ต้อง" --> LM["LLM JSON field plan ไม่สร้าง facts"]
 LM --> SG["Schema + semantic guard + clause coverage"]
 SG --> READ["อ่าน current source fields / joins / domain bridges"]
 FP -- "ไม่ต้อง" --> READ
 READ --> VALID
 VALID --> RET{"Reader คืนผลแบบใด?"}
 RET -- "ถูก schema/coverage" --> OUT["migrated finish: draft/source/status metadata"]
 RET -- "invalid candidate" --> CL["Topic confirmation หรือ safe clarification"]
 RET -- "ไม่มี result" --> LIVE{"เป็นคำถามสถานะจองสด?"}
 LIVE -- "ใช่" --> WP["Live read-only adapter ตาม transport config"]
 LIVE -- "ไม่ใช่" --> NO["ไม่พบข้อมูลที่ยืนยันได้ / ขอรายละเอียด"]
 WP --> OUT
 CL --> OUT
 NO --> OUT
 OUT --> UI["Server commit common state, sources, log แล้ว frontend แสดงผล"]
```

หมายเหตุ: diagram แสดง logical families ของ branch; ตารางลำดับในข้อ5เป็นลำดับจากโค้ดจริง ไม่มีการปล่อยให้ทุกคำถามเข้าทั้งสอง reader หรือเข้าทุก bridge

## 2. Record กลางหนึ่งรายการประกอบด้วยอะไร

- `record_id`: ตัวตนอ้างอิงคงที่สำหรับแก้ record เดิม/เชื่อม record อื่น ไม่ใช้ชื่อที่ผู้ใช้เห็นแทน primary key
- `kind`: หมวดที่เลือก schema/form/relationship rules
- `revision`, lifecycle และ review metadata: แยก draft revision จาก revision ที่ approve/publish แล้ว
- `aliases.th/en`: ชื่อ/คำเรียกสำหรับหา entity ไม่ใช่ regex หรือเนื้อหานโยบายใหม่โดยอัตโนมัติ
- `fields[key].status`: known / unknown / conflicted; unknown ไม่ใช่falseหรือไม่มีบริการ และ conflicted ไม่ให้เลือกฝ่ายใดเอง
- `fields[key].value`: ค่าตามชนิด รวม localized text, list, numbers, periods และ references
- `evidence_refs`: source_id + JSON pointer ที่ต้องตรวจย้อนว่าค่าตรงกับ snapshot
- `validity`: effective_from/effective_until แบบมี timezone; expiry เป็น exclusive endpoint
- `localization`: translation/review status ไม่เท่ากับการมี string en ในทุกช่อง

ระบบอ่านค่าผ่าน `value()` เฉพาะ field ที่ known การบันทึกครบช่องจึงต้องมีความหมาย/หน่วย/relations/source ถูกต้องด้วย ไม่ใช่เพียง JSON parse ได้

## 3. Owner create/edit/publish flow

1. เลือก template ตามหมวด ถ้าแก้ราคา/เกมเดิม ให้ใช้ record_id เดิมและ expected_version ล่าสุด
2. กรอกเฉพาะ facts ที่ยืนยันได้ ระบุ unknown/conflicted เมื่อยังไม่รู้ ห้ามใช้0/false/[] แทนความไม่ทราบ
3. save_owner_record สร้าง immutable attestation snapshot ของค่าที่เจ้าของกรอก พร้อม source hash/pointers และ actor/change note
4. optimistic version ป้องกันแก้ทับ revision ที่เปลี่ยนไปแล้ว
5. validate schema/refs/source pointer/authority/interval/capacity/periods; unknown optional field ไม่จำเป็นต้องเดาให้ครบ
6. preview ใช้ CommonAnswerer กับ planner ตาม flag จึงไม่ใช่ full web/migrated dispatcher เสมอไป ต้องตรวจ end-to-end เพิ่ม
7. approve ผูก record version+hash; ถ้าแก้เนื้อหาหลังจากนั้นต้องไม่ถือ approval เก่าเป็นการอนุมัติค่าฉบับใหม่
8. publish ตรวจ selected revisions, referenced records, factual trust, required fields, translation metadata และ validity ตามชนิดก่อนสร้าง release/สลับ active อย่างมีเงื่อนไข
9. withdraw ระเบียนที่ไม่ควรตอบต่อ; rollback เป็นการเปลี่ยน release/สถานะผ่าน store ไม่ย้อนเขียนทับประวัติ

**ความต่างที่สำคัญ:** MigratedView ของแชททดสอบอ่าน latest heads แบบ read-only ไม่รอ active published release ดังนั้น “แก้ draft แล้วเห็นในแชททดสอบ” ไม่ใช่หลักฐานว่า deployment ที่อ่าน published release จะเปลี่ยนตาม draft ทันที หรือว่า draft ถูกอนุมัติแล้ว

## 4. ชนิดข้อมูลและ task ที่ต้องเชื่อม

{{KIND_TABLE}}

หน่วยที่ต้องแยกตลอด flow: service กับเครื่องรายตัว, zone กับ resource, จำนวนที่นั่งกับผู้เล่นพร้อมกัน, นาทีเล่นกับนาทีกันช่องจอง, package rate กับ hourly rate, historical rulebook กับรายการที่จะจัดใหม่

## 5. Common reader: ลำดับจริงและทางออก

| ขั้น | งานหลัก | การตัดสิน/ผลลัพธ์ |
|---|---|---|
| C01 | snapshot + timezone/current records | อ่าน revision/source/withdrawn ใน snapshot เดียว; at ต้องมีtimezone |
| C02 | declined/confirmation/qualified reply | ตีความ yes/no/rephrase/เงื่อนไขเพิ่ม โดยไม่ถือ yes เป็น owner approval |
| C03 | compact opening status | เฉพาะคำถามรายวันที่ grammar ครอบคลุม; ไม่ใช้เปิดวันนี้เป็น occupancy |
| C04 | rental bridge | ใช้ grammar เดิม แต่ facts จาก current common snapshot พร้อม tuple/state |
| C05 | request roles + scoped names + derived names | แยกสิ่งที่ขอ สร้างชื่อจากข้อมูล ไม่ compile aliases ทั้งหมดเป็น regex |
| C06 | price-scope resume, named/context/identity links | exact/fuzzy entity ไม่ใช่หลักฐานว่า operation ถูกแล้ว |
| C07 | early intent/topic resolution ถ้ายังไม่มี scope | รักษา live query และ known-unconfirmed boundaries |
| C08 | compound operations / declared question profile | ไม่เลือก profile ที่ครอบคลุมเพียงส่วนเดียวแล้วตอบเหมือนครบ |
| C09 | primary_ids → operation | เลือก game/competition/service/zone และชนิดงาน |
| C10 | equipment / trusted legacy-intent bridges | รับเฉพาะขอบเขตที่ bridge ตรวจได้ ไม่ fallback facts เก่า |
| C11 | audience, budget, comparisons, live/calendar, people/rental | ห้ามเดากลุ่มราคา/ระยะเวลา/วันที่; live requestอาจ defer dispatcher |
| C12 | FAQ/procedure/policy/game-service discovery | เลือก subject/context/qualifier; บาง operation เปลี่ยน roots เป็น related records |
| C13 | optional bounded entity selector เมื่อ scope ยังไม่พอ | candidates จำกัด, task backstop, LLM index/profile binding, independent-topic guard |
| C14 | field requests / state defaults / requested focus | แยก broad overview จาก field ชัดเจน; named FAQ บางกรณีเลือก answer |
| C15 | competition parent/rule text และ authority/field ownership | ไม่อ่านกฎคนละเกม; explicit all ขอครบตาม source order |
| C16 | competition clause bridge | สรุปบางข้อ/ประท้วงเฉพาะ proposition; source facts ไม่มาจาก legacy loader |
| C17 | unresolved clauses / semantic review | ตรวจสิ่งที่ literal grammar ยังไม่รู้จัก ไม่ถือ field ที่ parseได้ว่าครอบคลุมเจตนาทั้งหมด |
| C18 | optional LLM field plan | เลือกได้เฉพาะ field/schema ของ scope ที่ล็อกแล้ว ไม่ย้าย entity/fabricate facts |
| C19 | checked_plan + semantic_guard | JSON/schema ผ่านอาจยัง reject ถ้า intent ยังไม่มี independent typed support |
| C20 | read contract + relation projection + render | อ่าน known fields, unknown/conflicted/expired, dependencies และ citations |
| C21 | billing/comparison/budget/source caveats | สูตรเฉพาะที่มี source, warning/partial ของขอบเขตที่ยังไม่ยืนยัน |
| C22 | finish validation + still_current | ตรวจ source pointer/needs/epoch แล้วเลือก answer/list/partial/clarification/not_current/retry |

แต่ละขั้นมี early return; field planner ไม่ได้ทำงานทุกครั้ง และไม่สามารถย้อนแก้ entity ที่ถูกเลือกผิดก่อนหน้าได้เอง

## 6. การเลือก entity และการให้คะแนน

### 6.1 Name matcher

`normalize` → exact observed spans → suppress เฉพาะ nested mention ที่พบจริง → one adjacent non-digit duplicate deletion หากได้ entity เดียว → bounded SequenceMatcher spans

- fuzzy ต้องยาวพอ, numeric edition/resource digits ต้องตรง
- threshold `.88`; กรณีหลาย candidate ต้องมี margin อย่างน้อย `.06`
- exact hit ที่มีอยู่ทำให้ matcher คืนทันที ส่วน task cue ที่สะกดผิดยังอาจไม่ฟื้น

ตัวเลข similarity เป็นความคล้ายชื่อ ไม่ใช่ความถูกต้องของเจตนา/คำตอบ เช่น Zelda ถูกชื่อแต่คำว่า “คือเกมอะไร” พิมพ์ผิดยังเลือก field ไม่ได้

### 6.2 Bounded semantic entity/profile selector

ค้น known textual fields และ names ด้วย weighted trigram overlap: generic grams มีน้ำหนักน้อยลง; scoreต้องผ่าน `.16`; ส่ง candidatesไม่เกิน8 โดยมี declared-task backstopไม่เกิน4

ก่อนเรียกโมเดลมี guard สำหรับ numbered targets, price ที่ไม่มี target, broad/live query และ independent topic anchor โมเดลเลือก index และส่ง quoted bindings ตาม schema ไม่เขียนข้อเท็จจริง

หลังตอบมี JSON/schema checks, subject/task/ownership/context/clauses binding และ independent support checks ความถูกต้องของ binding ไม่ใช่การตรวจความหมายโดยมนุษย์ และการกรองก่อน LLM อาจทำให้ source ที่มีคำตอบไม่ถูกส่งให้โมเดลตั้งแต่แรก

## 7. LLM field planner และคอขวดที่พบจริง

1. scope/record ถูกเลือกแล้ว จึงสร้าง schema ของ field ที่สัมพันธ์ได้ พร้อม meanings ภาษาไทยหรืออังกฤษ
2. คำถามถูกแบ่ง semantic clauses; ปกติ batchไม่เกิน6 clauses และจำนวนbatchจำกัด
3. deadline/model admission/queue/local model gate ต้องอนุญาตก่อน HTTP
4. ส่ง JSON schema, `think=False`, `temperature=0`; ไม่ขอข้อความคำตอบหรือ SQL/source facts
5. ตรวจขนาด/JSON/envelope/clause IDs/allowed field keys/platform/all_fields
6. `semantic_guard` เทียบ typed known needs, broad request, unresolved spans และ unverified intents
7. หากไม่พบ strong needs ที่ระบบรู้จัก อาจ reject ทั้งแผน แม้โมเดลตอบ schema ถูก

**ผล R88:** field-planner audit schemaผ่าน2,623 events แต่ finalรับ129 events; อีก2,494 eventsถูก `rejected_unverified_intent` ตัวเลขเป็น audit events ไม่ใช่คำถามไม่ซ้ำ ผลสุดท้ายมี method bounded_llm_schema_fields62 requests เพราะมีการเรียกซ้ำ/ย่อย/เปลี่ยนทางออก

จึงมีปัญหาสองฝั่งพร้อมกัน: โมเดลบางครั้งเสนอ fieldกว้าง/ผิดงาน และ semantic guard ยังพึ่ง cue ที่รู้จักจนปฏิเสธ paraphrase ที่ควรเข้าใจ ห้ามแก้โดยปิด guard ทั้งหมดหรือเชื่อทุก JSON ของโมเดล

## 8. R87 bridges: สิ่งที่นำกลับมาแล้วและขอบเขต

| Bridge | ส่วนเดิมที่ใช้ | แหล่ง facts | Final method requests ใน R88 |
|---|---|---|---:|
| legacy_intent_bridge | regex compiler, priority/category/intent | FAQ intent_key/answer ปัจจุบันที่ตรงรายการเดียว |16|
| rental_bridge | zone/audience/period/task grammar | current rental_package และ relations |5|
| equipment_bridge | operation/catalog projection | current equipment/source grouping |166|
| competition overview | pure substantive clause/facet helpers | current competition_ruleของ parentเดียว |13|
| competition proposition | pure protest query/source predicates | current rule text และ source pointers |2|

รวม202 requests ที่จบด้วย methodเหล่านี้ **ไม่ใช่**จำนวนทุกคำถามที่ระบบตอบได้ และไม่ใช่อัตราความครอบคลุมของ “คำถามที่ควรเข้า bridge” เพราะ corpus มีคำถามแต่ละหมวดไม่เท่ากัน เป็นหลักฐานว่าการเชื่อมบางส่วนไม่เท่ากับนำ interpreter เดิมกลับมาทั้งหมด

Legacy intent bridge ยังไม่รับ rules/rental/price/games/controls/equipment/people และ correction/profileบางกลุ่มโดยตั้งใจ ต้องครอบคลุมสาระทั้งคำถามหลังตัดคำสุภาพและ map current FAQ intent ได้รายการเดียว จึงไม่ใช่ generic legacy router

## 9. Domain read/render subflows

### เกม/อุปกรณ์

game → game_service/service/zone หรือ control_set ตาม operation; แยก source listing จาก installation/live availability ที่ยืนยันจริง คำถามระดับ zone ควร renderระดับzone หากมี relationที่ยืนยัน ไม่ตอบเฉพาะชื่อ service แล้วถือว่าครบทุกกรณี

### ปุ่ม

เลือก control_set ที่ตรงเกม/แพลตฟอร์ม/โหมด → action/binding projection → renderปุ่มและscope caveat; “ปุ่มทั้งหมด” กับปุ่มเฉพาะ action เป็นคนละcoverage partial sourceต้องบอกว่าข้อมูลมีเพียงบางส่วน

### ราคา/เหมา

service/zone/resource + audience + duration/period → related rate/package → billing basis/validity → calculationที่sourceอนุญาต → current value และevidence ไม่อ่านตัวเลขจากhistory

24 rental packages ยังมี validityunknownในsnapshot ส่วน18 ratesมีendก่อน1เม.ย.2026 และ6 rate validityunknown กรณีงดตอบราคาปัจจุบันต้องแยกจาก parser/กลุ่มราคาเลือกผิด

### กติกา

game → competition edition → children ordered by source_order/section → facet/proposition/explicit-all → depends_on_ids และ full clause text → citation

summarybridgeไม่เกิน6facetsพร้อมบอกว่าเป็นบางข้อ explicit-allไม่ถูกจำกัดด้วยsummary ข้อประท้วงต้องมีdeadlineหลังจบแมตช์และผู้ยื่นครบ ถ้าถามภาษา/authorityร่วมด้วยไม่ตัดเหลือข้อประท้วงอย่างเดียว

### ตาราง/วันปิด

open_day compact day request → schedule/closure/current date ไทย → day status พร้อมวันที่; วันกับ“ตอนนี้”/ช่วงเวลาย่อยและ live slot เป็นคนละคำถาม

มีschedule5fields open_periodsที่ยังเป็นconflictedจากบันทึกmigrationเดิม; 12:00–13:00จองไม่ได้และVR30นาทีกันชั่วโมงเต็มเป็นสิ่งที่ผู้ใช้ยืนยันแล้ว ไม่ย้อนถามเหมือนยังไม่เคยได้รับข้อมูล แต่ห้ามใช้การจองไม่ได้มายืนยันข้อเท็จจริงอื่น เช่น การเข้าพื้นที่ทางกายภาพ โดยไม่มีหลักฐาน

### สถานะจอง

common readerต้อง defer live requestที่เกี่ยวข้อง → migrated dispatcher → live_status → WordPress/dashboardตามruntimeconfig → normalized snapshot/cache → time/resource/family filtering → vacancy answer

R88 bulkจำลองunavailable จึงไม่ใช้ความล้มเหลวจากmockนี้สรุปว่าWordPressจริงล่ม ผู้ใช้เคยยืนยันสถานะจริงถูกต้องแล้ว รอบนี้ไม่ได้เปิดประเด็นตรวจสถานะจริงใหม่

## 10. การถามต่อ การยืนยัน และการเปลี่ยนหัวข้อ

- stateเก็บIDs, requested_fields, operation, scope_ids, constraints และrequest_contract ไม่เก็บราคาหรือfactsให้ใช้แทนrevisionใหม่
- pending profileใช้routing fingerprint/revision ตรวจyes/no/เลือกชื่อ ถ้าข้อมูลขอบเขตเปลี่ยนต้องถามใหม่
- qualified reply/rejection/replacementต้องทิ้งข้อเสนอที่ผู้ใช้ปฏิเสธและตรวจtaskใหม่ ไม่ยึดcandidateเก่าเพียงเพราะมีhistory
- รหัส “PC”/“ครึ่งวัน”/“ภายใน” ต้องผูกกับtaskที่ส่งจริง; คำว่า“ทั้งหมด”ต้องรู้ว่าทั้งหมดของรายการไหน
- serverจงใจไม่ส่งlegacyrequest_planให้common แต่ส่งoriginal input + trusted common state ประวัติจึงไม่ได้หายไปเองทุกกรณี
- SF-006 พิสูจน์ว่าstateมีPCและrelationอุปกรณ์ถูกพบแล้ว แต่reply“อุปกรณ์”ยังถูก unresolved_query_clause veto เป็นปัญหาtask→field/projection ไม่ใช่พิสูจน์ว่าserverไม่ส่งhistory

## 11. Validation และ fallback

`finish` ตรวจ snapshot epoch, requested-field obligations, evidence pointer, unknown/conflicted/validity, scope_limits แล้วคืนชนิดผลที่ตรง ไม่อ้างว่ามนุษย์รับรอง semantics

หาก invalid candidateถูกคืนมายัง migrated_chat จะถูกแทนด้วย profile confirmation หรือ safe clarification เก็บ rejected_candidateไว้ บางผลจึงไม่มีquery_planที่ระดับบน ต้องดูrejected_candidate.query_planด้วย

เมื่อcommonไม่พบคำตอบ จะมีเพียงlive adapterที่เข้าเงื่อนไข หรือข้อความไม่ยืนยัน/ขอรายละเอียด **ไม่มี factual fallbackไปFAQ/ราคา/RAGเก่า หรือให้LLMแต่งpolicyใหม่** ถ้าDBอ่านไม่ได้ก็แจ้งunavailableไม่สลับฐานเอง

`confidence=.8` ของanswer/list เป็นค่าคงที่ในcommon finish ไม่ใช่accuracy80%; migration trace confidence1ก็หมายถึงเลือกdispatchสำเร็จ ไม่ใช่factsถูก100%

## 12. Translation และ publication readiness

ในsnapshot602records มีfieldknown2,951 / unknown1,431 / conflicted5 unknownจำนวนมากเป็นoptionalหรือยังไม่ยืนยัน ไม่ใช่หลักฐานว่าmigrationหาย1,431facts

metadata en_status: agent_translated486 / missing116 แต่การscanค่าที่knownจริงพบlocalized objectsที่มีthและไม่มีen11จุด ทั้งหมดเป็นsectionในbindingsของMario Kart Live: Home Circuit จึงห้ามเอา116ไปพูดว่า116recordไม่มีภาษาอังกฤษทั้งหมด

มีlocalized en32objectsปนอักษรไทย และคำตอบEnglish512requestsที่ถูกThai-proseflag บางส่วนเป็นชื่อเฉพาะ/หน่วย/ชื่อรายการ ต้องแยกจากการแปลผิดความหมาย

581recordsมีvalidityunknown และ5conflicted schedulefields จึงยังไม่ใช่publication-readyโดยอาศัยผลทดสอบอัตโนมัติอย่างเดียว การย้ายเป็นdraftกับการreview/publishเป็นคนละงาน

## 13. การเพิ่มข้อมูลใหม่ให้ตอบได้ ต้องผ่านอะไรบ้าง

1. ชนิดข้อมูล/fieldรองรับในcatalog/schema
2. source/ภาษา/หน่วย/validityถูกต้องเท่าที่มีหลักฐาน
3. reference IDsและระดับzone/service/resource/เกมถูกต้อง
4. query semanticsเลือกtask/subject/qualifierได้ ไม่ใช่เพียงเจอalias
5. field contract/projectionรู้ว่าควรคืนอะไรตามคำถาม
6. renderer/citations/stateรักษาความหมายครบ
7. LLM proposalsผ่านschemaและbindingโดยไม่ถูกบล็อกจากข้อจำกัดที่ไม่จำเป็น
8. preview/full chat/packaged runtimeใช้revision/configเดียวกันตามที่ตั้งใจ

Fixture R87ผ่าน19checksและกติกา7checksยืนยันบางกลุ่มเพิ่ม/แก้/ถอนได้โดยไม่แก้router แต่ไม่ใช่หลักฐานว่าเพิ่มทุกหมวดด้วยคำถามทุกรูปแบบแล้วจะตอบถูกเสมอ หรือว่าเพิ่มโซนใหม่แล้วlive adapterจะรู้mappingใหม่นอกขอบเขตที่ตรวจแล้วอัตโนมัติ

## 14. ขอบเขต full test ที่ต้องอ่านประกอบ

- 20,554 unique questions,55,811grades; single-question bulkเริ่มhistoryว่าง
- เพิ่มengine session12ชุด/24เทิร์น ผ่านliteral23เทิร์น โดยมีpositivecontract12เทิร์น; ไม่ใช่HTTPsessionhead-to-headกับเดิม22/24
- guard500เคสเป็นdiagnosticsของlayout/repeat/blockpolicy ไม่ใช่proofว่าฟื้นtypoทุกชนิด
- modelHTTP4,412calls transportสำเร็จ4,376/timeout36; typed/model/schemaสำเร็จไม่ใช่หลักฐานว่าเลือกคำตอบถูก
- reference clock16ต.ค.2026เที่ยงไทย ไม่ใช่วันที่ปัจจุบันของคนที่เปิดรายงาน; per-job reference_dateมีสิทธิ์เหนือกว่า
- ไม่ได้rebuildportable packageหรือทดสอบproductionหลายuser/หลายเครื่องในรอบนี้
'''
uses={'game':'overview/genre/how_to_play/description','center':'ข้อมูลศูนย์/ที่ตั้ง/map','policy':'ขอบเขตการใช้บริการ/conditions','audience':'กลุ่มราคา/สิทธิ์','zone':'หมวดพื้นที่/ระดับการถาม','rental_package':'เหมาzone+audience+period','resource':'เครื่องรายตัว/booking mapping','service':'บริการ/เวลาเล่น/occupancy basis','game_service':'เกมสัมพันธ์กับบริการ/การให้บริการ','faq':'คำถาม/answer/query_profile','competition':'เกม/รายการ/edition','competition_rule':'clause/facet/dependency/text','control_set':'bindings/action/platform/mode','person':'directory/roles','equipment_model':'รุ่น/จำนวน/specifications','closure':'วันที่ปิดหรือเปลี่ยนเวลา','rate':'price+billing+audience+validity','schedule':'open/bookable/maintenance','contact':'ช่องทางติดต่อ','facility':'พื้นที่/สิ่งอำนวยความสะดวก','procedure':'ขั้นตอน/conditions/required docs'}
table='| kind | Records | ขอบเขตงาน |\n|---|---:|---|\n'+'\n'.join(f'| {k} | {n} | {uses.get(k,"ตาม schema")} |' for k,n in M['data_inventory']['by_kind'].items())
common=common.replace('{{KIND_TABLE}}',table)
common+='\n## 15. จุดอ้างอิงโค้ดที่ตรวจ\n\n'+'\n'.join('- '+x for x in [link(C,'app/web_api/server.py','do_POST'),link(C,'app/web_api/server.py',needle="request_plan = None",label='server: common profile ไม่ใช้ legacy request_plan'),link(C,'app/pipeline/engine.py',needle='if migrated_chat_enabled():',label='engine: migrated early return'),link(C,'app/pipeline/migrated_chat.py','answer'),link(C,'app/knowledge/common/migrated_view.py','snapshot'),link(C,'app/knowledge/common/owner_server.py','save_owner_record'),link(C,'app/knowledge/common/owner_server.py','preview_answer'),link(C,'app/knowledge/common/store.py','publish'),link(C,'app/knowledge/common/registry.py','validate'),link(C,'app/knowledge/common/answer.py','named'),link(C,'app/knowledge/common/answer.py','answer'),link(C,'app/knowledge/common/entity_search.py','candidates'),link(C,'app/knowledge/common/planner.py','semantic_guard'),link(C,'app/knowledge/common/legacy_intent_bridge.py','select'),link(C,'app/knowledge/common/answer.py','finish')])
write('02_FULL_FLOW_COMMON_TH.md',common)
print('Wrote separate full-flow documents')
