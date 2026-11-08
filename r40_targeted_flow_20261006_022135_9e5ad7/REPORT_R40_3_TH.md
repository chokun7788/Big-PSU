# รายงาน Flow → แก้ → ทดสอบ → วิเคราะห์ r40.3

วันที่ 2026-10-06T03:10:17 / เครื่องเจ้าของ / เริ่มจาก r39.3

## 1. ผลและขอบเขตที่ยืนยันได้

- เว็บจริง `2026.10.06-targeted-flow-r40.3` / installation `1559f5265e120f87` ที่ [เปิด Chatbot](http://127.0.0.1:8097/)
- เปิด Local LLM และ semantic RAG จริงตาม health; candidate ใช้ WordPress read-only/cache 0 วินาที
- รอบสุดท้าย **91/91 บทสนทนา**, **153 HTTP requests**; 105/105 test methods ของชุดที่เกี่ยวข้อง ผ่านตามหลักฐานรายไฟล์
- baseline 31 เคสเดิม: เกณฑ์แรก 20/31; เมื่อเพิ่มเงื่อนไขว่าปุ่มจองต้องเป็นการจองและราคา PC ต้องเลือก PC จริง ได้ **18/31**; r40.3 ได้ **31/31 ด้วย oracle เดียวกัน** เก็บ regrade เป็นไฟล์ใหม่
- ไม่รัน full corpus สองหมื่นกว่าข้อ ไม่เก็บ live booking truth ที่พักไว้ และไม่ใช้ผล fixture แทนสถานะจริง
- มี Flow ครบ B001–B066 แต่ผลชุดนี้ไม่พิสูจน์ว่าปิดทั้ง 66 รายการ; สถานะรายข้อแยก owner/deferred/partial/remaining
- สำรอง app/web/templates/tests ก่อนแก้ 306 ไฟล์และตรวจ hash ข้อมูลต้องรักษา 5 จุด; แก้ 12 ไฟล์เฉพาะรอบนี้ตามรายการ diff ไม่รวมเครดิตงานที่ Git ยังไม่บันทึกก่อนหน้า

## 2. ทำไมคำตอบยังผิดทั้งที่มีข้อมูล

มีหลายชั้นที่ทำงานต่อกัน การมี source ถูกต้องแก้ไม่ได้ถ้า operation/target/scope ถูกเปลี่ยนก่อน lookup คะแนน route สูงก็ไม่รับรองว่าตอบคำขอครบ

| กลุ่มสาเหตุ | พฤติกรรมก่อน | จุดที่เสีย | ควรตอบ/การแก้ที่ลงมือ |
|---|---|---|---|
| Missing slot กับ domain confusion | `Tell me the keyboard controls please` กลายเป็นรายการอุปกรณ์; `List all game buttons` บอกไม่ยืนยันเกม | keyword keyboard/buttons ชนะ operation และเรียก model ก่อนรู้ว่าขาดชื่อเกม | ถามชื่อเกมอย่างเดียว; detector ยอมรับเฉพาะ generic words และกันชื่อจริง/เลข/negation/hardware |
| Pending selection หาย | ขอปุ่มแล้วตอบ `VALORANT กับ Mario Kart 8 Deluxe` → no_answer/availability หรือเกมเดียว | การต่อข้อความกับ semicolon ไม่เท่ากับส่งรายการงาน; heuristic splitter ทำหล่น | สร้าง `dialogue_selection_v1` จากการเลือกจริง คง operation แล้ว execute ทุก child |
| Scope หลายโซนหาย | `PC and PS5` ถูกอ่านเป็นอุปกรณ์หรือแสดงแค่โซนเดียว | resolver รับเป้าหมายเดียว/ใช้ assistant catalog เป็นบริบทไม่พอ | ทำ requests ต่อโซน ตรวจ selected headers และ forbidden unselected zones |
| Edition normalization ไม่ครบ | `TEKKEN IX` ตอบ TEKKEN 8 | guard กัน Arabic แต่ Roman ไม่ผ่าน; fuzzy alias ทำชื่อใกล้สุดแทนภาค | ตรวจ Roman ที่ถูกไวยากรณ์เทียบ recorded editions, กันทั้ง single และ child; VIII รับเป็น 8; IX ไม่แทนเป็น 8 |
| Unknown Thai title หลุด operation | `มายคราฟต์` หลังถามชื่อเกม กลับถามหมวดเกม/ราคา/จอง | unknown bare Thai ไม่มี entity ที่ยืนยันจึงไม่ถูก merge เป็น game slot | เก็บชื่อที่ผู้ใช้ส่งและ control operation แต่ไม่ยืนยัน title ว่ามี source |
| Unknown ใน scope หลายรายการถูกทิ้ง | `PC and washing machine` ตอบ PC อย่างเดียว | service scan หา PC ได้แล้วใช้ผลบางส่วน | เก็บ selection_errors และขอระบุโซนทั้งหมดใหม่ |
| Negation กินคำขอใหม่ | `ไม่เอาปุ่ม ขอราคาของ PC` ตอบว่าไม่มี service | ตัวอ่านไม่เอาอ่านเลยถึง PC จึง exclude PC ด้วย | หยุด span ตรง `ขอ/ต้องการ/show/want…`; มีคู่ negative ที่ต้องตัด PC จริง |
| Guard เฉพาะ parent | VALORANT + Minecraft/TEKKEN IX เสี่ยง child ไป lookup เกมอื่น | compound เรียก `_answer_single` ตรงโดยข้าม guard ของ entry | guard ชื่อและภาคใน child ด้วย ตอบ known + explicit unconfirmed แยกส่วน |
| Fast answer กลืนอีก task | ปุ่มจองพร้อมราคา ตอบแค่ลิงก์ | booking navigation shortcut ตรวจทั้งประโยคแล้ว return ก่อน split | จำกัด shortcut ให้ navigation เดียวและใช้ใน child ของคำถามผสม |
| Parent adapter ทิ้ง task ก่อน worker | source test ถูก แต่ HTTP r40.2 ยังตอบราคาล้วน | STORE/resolve_request_plan ย่อ original เป็น `Service prices PC` ก่อนเข้า engine | parent ไม่ canonicalize คำถามผสมเป็น fee task เดียว; source harness ต้องจำลองการ rewrite เหมือนเว็บ |
| ภาษาอังกฤษ singular/plural | price ผ่าน แต่ prices ไม่แยก compound | `_english_compound_intent` รู้จัก price/fee/cost แบบ singular | รองรับ plural ใน operation signal เดิมและทดสอบทั้งภาษา |
| Shared tail ตีประโยคเต็มเป็นชื่อ | `PC ราคาเท่าไหร่ และ VALORANT มีปุ่มอะไรบ้าง` → `PC ราคาเท่าไหร่ มีปุ่มอะไรบ้าง` | parser กระจาย tail ปุ่มให้ operand ที่เป็น price question อยู่แล้ว | ถ้า operand มี operation ครบ ห้ามแชร์ tail; ให้ generic split รักษาสอง operation |
| เกิน batch limit หลุดเส้นทาง | เลือก 5 รายการ → availability/detail ผิดหมวด | parser reject >4 แล้ว fallback ไป general path | explicit clarification ครั้งละไม่เกิน 4 รายการ ไม่ execute subset; เป็น technical bound ไม่ใช่ policy ศูนย์ |
| Trace domain ผิด | selection plan ถูก log เป็น service_fee/price_lookup | response finalizer ใช้ price schema กับ plan ใหม่ | รักษา context ของ dialogue_selection_v1 เดิม |

## 3. ทำไมคะแนนสูงยังเลือกคำตอบผิด

ตัวอย่าง HTTP r40.2 ของคำถามปุ่มจองพร้อมราคา: `conversation_request` แสดง confidence 1.0 และ `universal_intent` 0.98 (`method=conversation_plan`) แต่ input ที่ worker ได้เหลือ `Service prices PC` แล้ว คะแนนนี้ยืนยันการจัดประเภทของข้อความที่ถูกย่อ ไม่ตรวจว่าคำขอปุ่มจองเดิมยังอยู่ จึงเกิด outcome `answered_complete` กับคำตอบที่ครบเพียงงานราคา

เกณฑ์ใหม่ตรวจ original requests → child domains → content → scope ไม่ใช้ confidence เป็นเฉลย สำหรับ multi-controls ต้องมีทุก title/operation และ unknown/edition ต้องไม่ถูกแทนเกมอื่น สำหรับ catalog ต้องมีโซนที่เลือกและไม่มีโซนที่ไม่ได้เลือก

พบ false positive ของ grader ด้วย: เคสไทยราคา+ปุ่มมีคำ PC อยู่ในหัวคำถาม แต่ไม่มีคำตอบราคา ค่า string-presence ผ่านได้ จึงเพิ่ม child operation assertions และ unit test ที่ตรวจทั้ง games กับ service_fee เก็บผลเกณฑ์อ่อนและผลเข้มแยกไว้ ไม่ย้อนแก้ raw

## 4. ผลสุดท้ายแยกชุด

| ชุด | ผ่าน/ทั้งหมด | HTTP requests | หลักฐาน |
|---|---:|---:|---|
| ปัญหาเดิม TH/EN | 31/31 | 43 | [final_r40_3_targeted_20261006_025941_cb5379_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/final_r40_3_targeted_20261006_025941_cb5379_summary.json) |
| สำนวนใหม่/unknown/3 turn | 12/12 | 19 | [final_r40_3_transfer_20261006_025957_a201c2_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/final_r40_3_transfer_20261006_025957_a201c2_summary.json) |
| boundary/limit/family/partial | 8/8 | 15 | [final_r40_3_boundary_20261006_030002_31bf27_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/final_r40_3_boundary_20261006_030002_31bf27_summary.json) |
| controls+price สองลำดับ TH/EN | 4/4 | 4 | [final_r40_3_mixed_20261006_030005_1025fb_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/final_r40_3_mixed_20261006_030005_1025fb_summary.json) |
| regression สอง turn ราคา/กฎ/หัวข้อ | 36/36 | 72 | [adjacent_http_20261006_030007_2f12e6_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/adjacent_http_20261006_030007_2f12e6_summary.json) |

### Unit / fixture gates

| ไฟล์ชุดทดสอบ | methods | exit | ผลดิบ |
|---|---:|---:|---|
| test_targeted_dialogue_r40.py | 15 | 0 | [test_targeted_dialogue_r40_30120c.txt](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/test_targeted_dialogue_r40_30120c.txt) |
| test_conversation_flow_r38.py | 23 | 0 | [test_conversation_flow_r38_a72268.txt](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/test_conversation_flow_r38_a72268.txt) |
| test_two_turn_choices_r39.py | 16 | 0 | [test_two_turn_choices_r39_cd53a0.txt](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/test_two_turn_choices_r39_cd53a0.txt) |
| test_competition_session_context_r35.py | 18 | 0 | [test_competition_session_context_r35_abe208.txt](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/test_competition_session_context_r35_abe208.txt) |
| test_p0_calendar_booking_reconciliation_20260925.py | 11 | 0 | [test_p0_calendar_booking_reconciliation_20260925_2eb2a9.txt](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/test_p0_calendar_booking_reconciliation_20260925_2eb2a9.txt) |
| test_saved_booking_oracle_r32.py | 5 | 0 | [test_saved_booking_oracle_r32_a4e724.txt](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/test_saved_booking_oracle_r32_a4e724.txt) |
| test_booking_on_demand_20261001.py | 17 | 0 | [test_booking_on_demand_20261001_9be70b.txt](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/test_booking_on_demand_20261001_9be70b.txt) |

fixture ตรวจ lunch/maintenance/closed/VR-hour-blocking/read-only/ผิดวัน/ข้อมูลว่าง/transport-success-but-wrong-count ไม่ใช่การเทียบ WordPress กับรายการจองจริง

### เวลาเส้นทางถามชื่อเกม

13 สำนวนในรอบเรียงลำดับบนเครื่องนี้: median ก่อน 0.4663s, หลัง 0.0185s; ช่วงหลัง 0.0166–0.1760s; trace มี `closed_control_request` และไม่มี `universal_intent` ใน 13 เคสนี้ ไม่ได้สรุป latency ทุกหมวดหรือวัด concurrency SLA

## 5. รอบวิเคราะห์และแก้ — เก็บทั้งผลที่ผิดและที่ผ่าน

| รอบ/ผลที่เก็บ | ประเภท | ผ่าน | เอกสารผล |
|---|---|---:|---|
| baseline_r39_3 | HTTP/model on | 20/31 | [baseline_r39_3_20261006_022303_49deab_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/baseline_r39_3_20261006_022303_49deab_summary.json) |
| round_A_B_source | source/model off | 25/31 | [round_A_B_source_20261006_022812_5df43a_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_A_B_source_20261006_022812_5df43a_summary.json) |
| round_B_structured_selection | source/model off | 31/31 | [round_B_structured_selection_20261006_023000_0829b4_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_B_structured_selection_20261006_023000_0829b4_summary.json) |
| round_C_stronger_oracle | source/model off | 30/31 | [round_C_stronger_oracle_20261006_023216_ddf268_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_C_stronger_oracle_20261006_023216_ddf268_summary.json) |
| round_C_negation_scope_fixed | source/model off | 31/31 | [round_C_negation_scope_fixed_20261006_023312_275f91_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_C_negation_scope_fixed_20261006_023312_275f91_summary.json) |
| round_D_fresh_holdout | source/model off | 11/12 | [round_D_fresh_holdout_20261006_023539_6d436c_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_D_fresh_holdout_20261006_023539_6d436c_summary.json) |
| round_E_unresolved_scope_fixed | source/model off | 12/12 | [round_E_unresolved_scope_fixed_20261006_023700_f9d886_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_E_unresolved_scope_fixed_20261006_023700_f9d886_summary.json) |
| round_F_http_r40_1 | HTTP/model on | 31/31 | [round_F_http_r40_1_20261006_024407_26d5d6_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_F_http_r40_1_20261006_024407_26d5d6_summary.json) |
| round_G_http_holdout_r40_1 | HTTP/model on | 12/12 | [round_G_http_holdout_r40_1_20261006_024505_a00686_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_G_http_holdout_r40_1_20261006_024505_a00686_summary.json) |
| adjacent_http_20261006_024523_725e5b_summary | HTTP/model on | 36/36 | [adjacent_http_20261006_024523_725e5b_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/adjacent_http_20261006_024523_725e5b_summary.json) |
| round_H_boundary_before_fix | source/model off | 4/8 | [round_H_boundary_before_fix_20261006_024636_29d7ff_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_H_boundary_before_fix_20261006_024636_29d7ff_summary.json) |
| round_I_boundary_after_fix | source/model off | 7/8 | [round_I_boundary_after_fix_20261006_024904_dbc905_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_I_boundary_after_fix_20261006_024904_dbc905_summary.json) |
| round_J_bilingual_boundary_fixed | source/model off | 7/8 | [round_J_bilingual_boundary_fixed_20261006_024938_ec1d68_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_J_bilingual_boundary_fixed_20261006_024938_ec1d68_summary.json) |
| round_K_plural_price_boundary_fixed | source/model off | 8/8 | [round_K_plural_price_boundary_fixed_20261006_025037_e3802f_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_K_plural_price_boundary_fixed_20261006_025037_e3802f_summary.json) |
| final_r40_2_targeted | HTTP/model on | 31/31 | [final_r40_2_targeted_20261006_025306_5b4c84_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/final_r40_2_targeted_20261006_025306_5b4c84_summary.json) |
| final_r40_2_transfer | HTTP/model on | 12/12 | [final_r40_2_transfer_20261006_025321_a4d833_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/final_r40_2_transfer_20261006_025321_a4d833_summary.json) |
| final_r40_2_boundary | HTTP/model on | 6/8 | [final_r40_2_boundary_20261006_025326_ab8066_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/final_r40_2_boundary_20261006_025326_ab8066_summary.json) |
| adjacent_http_20261006_025330_02e936_summary | HTTP/model on | 36/36 | [adjacent_http_20261006_025330_02e936_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/adjacent_http_20261006_025330_02e936_summary.json) |
| round_L_parent_adapter_fixed | source/model off | 8/8 | [round_L_parent_adapter_fixed_20261006_025450_2fff5a_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_L_parent_adapter_fixed_20261006_025450_2fff5a_summary.json) |
| round_M_compound_price_before | source/model off | 0/4 | [round_M_compound_price_before_20261006_025545_9da8fa_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_M_compound_price_before_20261006_025545_9da8fa_summary.json) |
| round_N_compound_price_after | source/model off | 4/4 | [round_N_compound_price_after_20261006_025607_4e5ab4_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_N_compound_price_after_20261006_025607_4e5ab4_summary.json) |
| round_O_shared_tail_corrected | source/model off | 4/4 | [round_O_shared_tail_corrected_20261006_025806_67df20_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/round_O_shared_tail_corrected_20261006_025806_67df20_summary.json) |
| final_r40_3_targeted | HTTP/model on | 31/31 | [final_r40_3_targeted_20261006_025941_cb5379_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/final_r40_3_targeted_20261006_025941_cb5379_summary.json) |
| final_r40_3_transfer | HTTP/model on | 12/12 | [final_r40_3_transfer_20261006_025957_a201c2_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/final_r40_3_transfer_20261006_025957_a201c2_summary.json) |
| final_r40_3_boundary | HTTP/model on | 8/8 | [final_r40_3_boundary_20261006_030002_31bf27_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/final_r40_3_boundary_20261006_030002_31bf27_summary.json) |
| final_r40_3_mixed | HTTP/model on | 4/4 | [final_r40_3_mixed_20261006_030005_1025fb_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/final_r40_3_mixed_20261006_030005_1025fb_summary.json) |
| adjacent_http_20261006_030007_2f12e6_summary | HTTP/model on | 36/36 | [adjacent_http_20261006_030007_2f12e6_summary.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/adjacent_http_20261006_030007_2f12e6_summary.json) |

12 transfer cases พบใหม่ครั้งแรกหลังแก้ชุดแรก: 11/12; หลังนำ failure มาแก้ไม่ถือเป็น independent holdout อีก ส่วน boundary พบ 4/8 ใน first pass, แก้ผ่าน source แต่ HTTP r40.2 ยังเหลือ 6/8 จึงกลับไปแก้ parent adapter ไม่จบที่ source pass ส่วน controls+price first pass 0/4 และ unit พบ weak oracle จึงปรับ parser/เกณฑ์จนผ่านเว็บจริง ชุดเหล่านี้เป็น regression หลังใช้พัฒนาแล้ว คะแนน 91/91 ไม่ใช่ accuracy โลกจริง

## 6. ตรวจทาน Flow หลังทำจริง

1. เพิ่ม state schema selection, selection_errors, target limit และ parent preservation ก่อน worker; ตรวจ original-vs-resolved ในทุกชั้น
2. เพิ่ม per-child edition/unknown/navigation guard; fast path ต้องไม่ข้ามคำขออื่น
3. เพิ่ม operation assertions ไม่ใช้เฉพาะชื่อในคำตอบ; แยก unit/source/HTTP/owner truth
4. ขอบเขตที่ไม่มี source ต้อง missing/conflict/unavailable ไม่แต่ง fact หรือบังคับ approximate entity
5. จำกัด parser selection 2–4 รายการ, fast mixed navigation 2–3 clauses; ใส่ข้อจำกัดจริงในแผนแทนวาดว่าทุกชนิดใช้ state เดียวแล้ว
6. แยก old/new release พร้อม hash; manifest เป็นที่มาของ version และ UI แสดง URL จริง
7. Stop เมื่อ targeted failures ที่ยืนยันได้หมดและ regressions ผ่าน; งาน owner/live/production/holdout ที่ยังขาดหลักฐานไม่ถูกปิดโดยคะแนนรวม

## 7. ยังเหลืออะไร และควรทำลำดับใด

### P0 ข้อมูลที่ต้องตัดสินใจ/ยืนยัน

- ราคาใน source พ้นช่วงประกาศแล้ว: ขอฉบับอัตราที่ใช้จริง ณ ปัจจุบัน วันที่เริ่ม/สิ้นสุด กลุ่มผู้ใช้และแพ็กเกจ; รอบนี้ทดสอบกับ recorded rates ไม่ยืนยันราคาใช้จริงวันนี้
- Tekken pause: ขอ clause ฉบับรับรองว่าข้อจำกัด pause ใช้ Round/Game/Match และให้เลือกข้อความ authoritative ที่ขัดกัน
- RoV ข้อ 6.1.5/6.1.5.1: ขอส่วนต่อจากข้อความที่ถูกตัดและฉบับเต็ม
- ข้อมูล roster/check-in, VALORANT 6 source gaps, อายุ/ค่าสมัคร, คนนอก/อาหาร/ถ่ายภาพ: คำถามและ source IDs แยกใน F-B024–F-B029
- รายการอุปกรณ์จริง ปุ่มที่ปรับบนเครื่องจริง และชื่ออังกฤษทางการ: ใช้รายการ review ให้เจ้าของยืนยัน ไม่เปลี่ยนให้ดู complete โดยแต่ง
- V2 canonical queue 104 pending และ active claim IDs ว่าง: ไม่ใช่แปลว่า legacy/English runtime ไม่มีคำตอบ; activation ต้องผ่าน source/human workflow

### P1 ทำเองต่อได้

1. ขยาย typed task state ให้ครอบคลุมหมวดอื่นและการกลับไปงานเก่า/partial outcome ทุก child; ตอนนี้ parent active task ยังเป็นราคา และ selection plan ใหม่ไม่ใช่ persistent multidomain state
2. เสริม task coverage contract ทุก compound combination และ all หลายมิติ; 91 เคสนี้รองรับเฉพาะแบบที่ตรวจ ห้ามอนุมาน universal robustness
3. ทำ independent holdout ที่ไม่เคยใช้แก้ และ adjudicate historical corpus ด้วย content/target/scope oracle ก่อนรันใหญ่ตามคำสั่งใหม่
4. จัดชุดแจก WithModels/DownloadModels จาก source เดียวกับ r40.3 พร้อม checksum/launcher; fresh Windows/ไทยใน path/offline-first installation ยังไม่ตรวจ
5. รวม trace schema, source hash/English invalidation, local-source viewer และขั้น refresh canonical/index ตาม Flow

### P2 งานเมื่อเลือกใช้งานจริง

- Live per-slot truth ยังพักตามผู้ใช้; load/worker-crash/network-soak/retention/public deployment ต้องเก็บหลักฐานตาม Flow ก่อนรับรอง
- พบเครื่องมืออ่านไฟล์ของ PowerShell ล้มเหลวหนึ่งครั้งพร้อม OutOfMemory ระหว่างมีเว็บหลายรุ่นเปิดอยู่; HTTP รอบนั้นยังผ่าน ไม่สรุปว่าเป็น chatbot answer error
- ปิดเฉพาะ process tree r40.1/r40.2 ที่เปิดรอบนี้หลังตรวจ command line แล้ว เก็บ r40.3 และเว็บเดิมของผู้ใช้; หลักฐาน cleanup แยก เก็บ log ทั้งหมดไม่ลบ
- เครื่อง local ต้องเปิดอยู่ขณะตอบสด; background launcher ไม่ทำให้เครื่องที่ปิดอยู่ตอบได้ และไม่ตั้ง auto-start/public server โดยเดา

## 8. ไฟล์ส่งมอบ/การเปิดใช้

- [Flow ฉบับตรวจทานครบ 66 รายการ](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/FLOW_R40_FINAL.md)
- [สถานะลงมือรายข้อ 66 รายการ](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/BACKLOG_EXECUTION_STATUS_FINAL.json)
- [คำตอบก่อน/หลังและคะแนน trace รายเคส](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/CASE_ANALYSIS_R40_3_TH.md)
- [ผล gates พร้อมการแยก owner truth](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/FINAL_AUTOMATED_GATES.json)
- [hash ข้อมูลที่รักษาไว้](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/PROTECTED_FACT_HASH_CHECK.json)
- [ไฟล์ที่แก้เฉพาะรอบนี้](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/SOURCE_CHANGES_THIS_TURN.json)
- [เปิดชุด r40.3 เบื้องหลัง](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r40_targeted_flow_20261006_022135_9e5ad7/release_r40_3/PSU_Esports_Chatbot_Local/Open-PSU-Esports-Background.cmd) หรือ [เว็บที่เปิดอยู่](http://127.0.0.1:8097/)

ชุดใหม่เป็น candidate สำหรับเครื่องนี้ ใช้โมเดลที่ติดตั้งอยู่แล้ว ไม่ใช่ชุด WithModels ใหม่ที่รับรองการแจกไปเครื่องอื่นได้ทันที
