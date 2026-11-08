# ผล Full Test R130 — Flow กลาง / LLM ON

ครบ 20,554 unique request keys และ 55,811 grades; ไม่มี key/grade ขาดหรือซ้ำ ตรวจ source/input และ model identity แล้ว

## คะแนนตามเกณฑ์เดิม

| ภาษา request | Strict ผ่าน/ทั้งหมด | Strict % | Positive literal ผ่าน/มีเกณฑ์ | Literal % | Saved R95 strict % |
|---|---:|---:|---:|---:|---:|
| auto | 445/3392 | 13.1191 | 1615/2301 | 70.1869 | 13.7087 |
| en | 802/27319 | 2.9357 | 7176/9466 | 75.8082 | 9.0523 |
| th | 231/25100 | 0.9203 | 10259/13142 | 78.0627 | 8.3347 |

Strict เป็นผล grader เดิม ส่วน positive literal ตรวจเฉพาะสัญญาข้อความด้านบวก ไม่ใช่ semantic accuracy ทั้งสองค่าไม่ยืนยันว่าตอบถูกครบทุกข้อ

## กลุ่มที่ต้องวิเคราะห์

| กลุ่ม | Requests (ซ้อนทับได้) |
|---|---:|
| protocol_mismatch | 19221 |
| controlled_provider_unavailable | 4132 |
| source_id_or_evidence_requirement_review_required | 2781 |
| literal_or_reference_contract_review_required | 2431 |
| outcome_mismatch_review_required | 1883 |
| keyword_firstline_clause_mismatch_review_required | 702 |
| source_gap_validity_or_conflict_review_required | 575 |
| performance | 388 |
| model_protocol_failure | 162 |

## ขอบเขตการเปรียบเทียบ

- เทียบ saved R95 ด้วย keys และ grade identities เดียวกัน ไม่รัน baseline ใหม่
- ข้อมูลของ R130 กับ R95 ต่างรุ่น และ deadline ต่างกัน จึงไม่ใช่ causal effect ของ Flow หรือน้ำหนักโมเดลเพียงอย่างเดียว
- workload ควบคุม live provider เป็น unavailable; ไม่ใช่ผลยืนยันสถานะจริง WordPress
- candidate ยังไม่ติดตั้งทับ R78
- API readiness และการตรวจ source lifecycle เป็น implementation gates แยกจากผลความแม่นยำ

## การตรวจ semantic

ROOT_CAUSE_REVIEW_TH.md ตรวจรากปัญหาครบทุกกลุ่มจากraw20,554requests/55,811gradesและ921reasonstringsแล้ว มี34case adjudicationsพร้อมsource77records/209snapshots ยืนยันตัวอย่างcontent/scope/omissionfailure15requests ไม่ใช่จำนวนผิดทั้งหมดและไม่ใช้คิดsemanticaccuracy คงreview_requiredสำหรับข้อที่ยังไม่ตัดสิน Flowยังไม่ผ่านคุณภาพครบ76ข้อ

## หลักฐาน

- COVERAGE.json
- SCORES.json
- ALL_FAILURES.jsonl.gz
- PER_REQUEST_ANALYSIS.jsonl.gz
- FAILURE_GROUPS.json
- REGRESSIONS_VS_R95.json
- MODEL_TRANSPORT_AND_LATENCY.json

## ข้อพบสำคัญหลังตรวจsourceจริง

- ข้อมูลGPUและกติกาCS2มีแล้ว แต่binding/verifierทำให้ไม่ตอบ; CS2textเท่ากับheadingถูกตัดทิ้ง ขณะที่ชื่อเอกสารTekkenformatกลับผ่านledger
- คำถามPC#10เสียresource scope; คำถามดูสตรีมระหว่างแข่งกลับตอบนโยบายสตรีมในศูนย์; tournamentfoodscopeหายระหว่างหลายneed
- availableในคำถามcatalogถูกส่งlive; explicititผูกเกมแล้วแต่ยังถามชื่อเกมซ้ำ; offsite notebookถูกแทนด้วยราคาเหมาโซน
- ชื่อกลุ่มcontrolled_provider_unavailable4,132กว้างเกินไป:3,160taskเป็นmodel-coded และ972ไม่มีreasoncode ต้องแยกจากliveartifacts1,082requests ห้ามอ้างทุกกลุ่มเป็นproviderจริงล่ม
- actualHTTP425/สำเร็จ263/timeouts162; successfulgatewayทุก263ตรวจprofile/adapter/messages/schema/stageได้ (retained199/base64) แต่HTTP/JSONไม่ใช่semanticcorrect
- median0.663s/p953.575s/p9947.175s/max151.130s ยังมี340requestsเกิน20s

คะแนนstrictตกหนักจากroute/intent/modecontract แต่literalก็ยังตามsavedR64 จึงยังไม่มีหลักฐานว่าคุณภาพใกล้Flowเดิมแล้ว รายละเอียดfixeddenominator/unknownและbaselineconfoundsในSAVED_FLOW_COMPARISON_TH.md และ FIXED_DENOMINATOR_SCORES.json

ตรวจhash2,361filesและlogicalsource/modelprovenanceซ้ำแบบread-onlyแล้วไม่เปลี่ยน ไม่มีbaselineinferenceใหม่ Candidateไม่ติดตั้งทับR78 งานวัดและรายงานเสร็จ; งานแก้คุณภาพยังเปิดอยู่
