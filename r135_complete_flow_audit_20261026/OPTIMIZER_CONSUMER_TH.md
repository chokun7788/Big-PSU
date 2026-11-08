# ตัวเริ่มฝึก R135 ที่ตรวจ admission ก่อนโหลดโมเดล

`system/tools/train_reviewed_planner.py` เรียก consumer ใน
`domain_flow/training_optimizer.py` โดยยังไม่ import torch/transformers/peft
จนกว่าจะตรวจข้อมูลจริงผ่าน `load_admitted_dataset` และตรวจ protocol เพิ่มแล้ว
โค้ดนี้อยู่เฉพาะ candidate R135 ที่ยังไม่ freeze/ติดตั้ง

สถานะจริง: review_round_008 ตรวจรายข้อ155/289; อีก134ยัง unreviewed
ชุดจริงไม่มี READY_FOR_OPTIMIZATION และ CLI ต้องออกด้วย admission_blocked
ก่อนอ่าน model assets/โหลด framework ตัวอย่างควบคุมใน training_optimizer_* เป็น
synthetic source-schema/adjudication/model-byte fixtures ไม่ใช่โมเดลที่ฝึกสำเร็จ
ไม่ใช่ผล semantic benchmark และห้ามนำ protocol ของ fixture ไปใช้กับ corpus จริง

Consumer ต้องได้รับ dataset, runtime-contract, base, base-manifest-ref,
protocol-ref, artifact-root และ output ใหม่ที่ไม่ทับ dataset/model
`--check-only` ตรวจ admission ครบโดยไม่โหลด tokenizer/model/optimizer
ทุก ref เป็น JSON `{path,sha256}` ที่ผูกกับไฟล์จริงใน artifact roots
ห้ามเขียน READY เองเพื่อข้ามส่วนที่ยังตรวจไม่ครบ

Base manifest ต้องมี model_profile เดียวกับ runtime และ `files` ครบทุกไฟล์ใต้
base directory รวม config/tokenizer/chat template และน้ำหนัก safetensors
revision string เพียงอย่างเดียวไม่ใช่ proof ของน้ำหนัก

Protocol version `r135-optimization-protocol-v1` ต้องผูก SHA ของ dataset freeze,
runtime, base manifest, CONFIG และ source identity พร้อม refs ต่อไปนี้:

- family_review_ref: การตัดสิน semantic family จริงครบ inventory พร้อมเหตุผล
  แต่ละ family ต้องอยู่ split เดียวกับข้อมูลที่ admit แล้ว
- coverage_review_ref: ทั้ง8 strata ตาม PHASE-08; กลุ่มที่ข้อมูลน้อยต้องเป็น
  insufficient พร้อม interpretation_limit ห้ามยก empty group เป็น assessed
- evaluation_plan_ref: สามแขน base/R121/candidate บน runtime/source เดียวกัน
  แยก planner/executor_verifier/end_to_end_answer พร้อมนิยาม เกณฑ์ promotion
  และวิธี review ที่ตรึงก่อนฝึก; unknown semantic ต้องเป็น review_required
  และ structural validity ต้องไม่ถูกนับเป็น semantic accuracy

Evaluation plan ต้องผูก question inventory/locale/reference clock ที่มีtimezone/
frozen live fixture/stage budgets/น้ำหนัก R121 จริง/exposure review ผ่าน refs
คำถามที่เปิดดูแล้วต้องคง retained_development ห้ามเรียก fresh holdout
การตรวจ ref/hash/รูปแบบเหล่านี้ไม่ตัดสิน semantic truth ของเนื้อหา protocol
ยังต้องอ่านและตัดสิน protocol ของ corpus จริงให้ครบก่อนใช้ฝึก

ค่าฝึกตั้งต้นคง base family/revision/NF4 doublequant BF16 และ LoRA ที่ R129
เคยรันได้: rank8/alpha16/dropout.05, q/k/v/o projections,3epochs,
batch1/accumulation8/lr.00015,sequence2048/generation850
แพ็กจาก exact current messages/template/options; ห้าม truncate prompt/target
ที่ไม่ครบหรือเกิน cap คัด checkpoint จาก development completion loss เท่านั้น
ไม่ใช้ holdout/test loss เลือก epoch และไม่ generate คำตอบระหว่าง consumer นี้

เมื่อรันจริงจะเก็บ full dataset/code/base/protocol freeze,environment,
actual model preflight,token stats,losses/gradients/steps,base/adapter parameter
hash ก่อนและหลัง,selected adapter hashes และ optimization proof
ความล้มเหลวหลัง admission ต้องรายงาน completed/attempted steps และสถานะ
weight updates ที่อาจยังตัดสินไม่ได้ ไม่ปลอมเป็นข้อมูลถูกบล็อกก่อนโหลด
telemetry ใช้ append-only journal และทนกรณี Windows reader lock

สิ่งที่ยังค้าง: corpus/context/transformation review ทุกข้อ,semantic family
regroup/eight-strata source adjudication และ metric thresholds จริง,
validation semantic metrics แยกชนิด,การทดสอบ optimizer บน GPU/optimization
จริงและ proof ทั้งหมด,สามแขนบน engine เดียวกัน,final source/model/raw/API
acceptance ไม่ promote adapter จาก completion loss หรือชุดควบคุมนี้
R121 retained context/base selector ยังเป็นตัวใช้งาน; adapter เดิมที่ critical
ถอยยังไม่ promote; constrained decoder ยังไม่ active ห้ามหยุด/kill PID42136
ซึ่งเคยถูก automatic review ปฏิเสธด้วย blocked by policy
