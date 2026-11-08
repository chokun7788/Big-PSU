# วิเคราะห์เคสอังกฤษ r46

ก่อนแก้ 22/33; หลังแก้ 33/33 ในชุดอังกฤษใหม่; ชุดรวมผ่าน 181/181

## การอ่านคะแนน

confidence 0.99 ของ route เช่าเหมาเป็นค่าที่กำหนดในโค้ด ไม่ใช่ความแม่นยำจากการประเมิน ตัว builder ตอบตาม plan: ถ้า parser ขยาย target/period ผิด คำตอบจากเซลล์จริงก็ยังผิดความต้องการได้ เกณฑ์ทดสอบจึงตรวจ ID ราคา + ค่า + source hash + missing fields + คำตอบที่แสดง แยกจาก HTTP 200 และ validation_ok

## แต่ละเคส

### en-polite-hire

คำถาม/ลำดับ: Could you quote the full-day hire cost for PC for external organizations?

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"pc:external:full_day": 4000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "Could you quote the full-day hire cost for PC for external organizations?", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: pc; organizations external; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "pc:external:full_day", "value": 4000, "cell": "B8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-polite-rent

คำถาม/ลำดับ: I would like to rent PC for a full day. What is the cost for external organizations?

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"pc:external:full_day": 4000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "I would like to rent PC for a full day. What is the cost for external organizations?", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: pc; organizations external; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "pc:external:full_day", "value": 4000, "cell": "B8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-whole-day

คำถาม/ลำดับ: PC whole-day rental price for external organizations

ผลก่อนแก้: ไม่ผ่าน; เกณฑ์ที่พลาด: original_cell_oracle

FULL regex รองรับ whole day แต่ไม่รองรับ whole-day จึงคงค่าเริ่มต้นสองช่วง แก้ให้เป็นเต็มวันเท่านั้น

Expected rates: `{"pc:external:full_day": 4000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["half_day", "full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "PC whole-day rental price for external organizations", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: pc; organizations external; periods half_day, full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: half day 2,000 THB / full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "pc:external:full_day", "value": 4000, "cell": "B8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-halfday

คำถาม/ลำดับ: PC halfday hire fees for external organizations

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"pc:external:half_day": 2000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["half_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "PC halfday hire fees for external organizations", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: pc; organizations external; periods half_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: half day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "pc:external:half_day", "value": 2000, "cell": "C8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: half day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-polite-selection

คำถาม/ลำดับ: PC rental price for external organizations full day → Only the half day please

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"pc:external:half_day": 2000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["half_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "Only the half day please", "context_used": true, "act": "fill_rental_scope", "resolved_query": "Zone rental request: pc; organizations external; periods half_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: half day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "pc:external:half_day", "value": 2000, "cell": "C8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: half day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-different-zone

คำถาม/ลำดับ: PC rental price for external organizations full day → What about VR?

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"vr:external:full_day": 6000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["vr"], "groups": ["external"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "What about VR?", "context_used": true, "act": "fill_rental_scope", "resolved_query": "Zone rental request: vr; organizations external; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**VR Zone**
• External organizations: full day 6,000 THB
• Seating capacity: 34 seats; equipment: 1 VR unit

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "vr:external:full_day", "value": 6000, "cell": "B5"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**VR Zone**
• External organizations: full day 6,000 THB
• Seating capacity: 34 seats; equipment: 1 VR unit

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-different-group

คำถาม/ลำดับ: PC rental price for external organizations full day → internal instead

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"pc:internal:full_day": 2000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["internal"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "internal instead", "context_used": true, "act": "fill_rental_scope", "resolved_query": "Zone rental request: pc; organizations internal; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• Internal organizations: full day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "pc:internal:full_day", "value": 2000, "cell": "D8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• Internal organizations: full day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-equipment

คำถาม/ลำดับ: PC rental price for external organizations full day → What equipment comes with it?

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["full_day"], "asks": ["equipment"], "unresolved_targets": [], "original_query": "What equipment comes with it?", "context_used": true, "act": "fill_rental_scope", "resolved_query": "Zone rental request: pc; organizations external; periods full_day; facts equipment"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• Seating capacity: 43 seats; equipment: 10 PC units

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• Seating capacity: 43 seats; equipment: 10 PC units

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-seats

คำถาม/ลำดับ: PC rental price for external organizations full day → How many seats does it have?

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["full_day"], "asks": ["capacity"], "unresolved_targets": [], "original_query": "How many seats does it have?", "context_used": true, "act": "fill_rental_scope", "resolved_query": "Zone rental request: pc; organizations external; periods full_day; facts capacity"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• Seating capacity: 43 seats; equipment: 10 PC units

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• Seating capacity: 43 seats; equipment: 10 PC units

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-people

คำถาม/ลำดับ: PC rental price for external organizations full day → How many people can it accommodate?

ผลก่อนแก้: ไม่ผ่าน; เกณฑ์ที่พลาด: operation, source_sha256, required_content

ตัวตรวจ follow-up ไม่รวม how many people แม้ตัวแยก field รู้จัก capacity ทำให้หลุดไปถามยืนยัน แก้ให้ใช้ผลแยก field ร่วมกัน

Expected rates: `{}`

Plan ก่อนแก้: `{}`

คำตอบก่อนแก้:

I am still answering your price question. Which service do you mean: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can choose all services.

ผลหลังแก้: True; rates: `[]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• Seating capacity: 43 seats; equipment: 10 PC units

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-duration

คำถาม/ลำดับ: PC rental price for external organizations full day → How long is a full day?

ผลก่อนแก้: ไม่ผ่าน; เกณฑ์ที่พลาด: original_cell_oracle, missing_fields

ตัวตรวจ follow-up ไม่รวม how long แม้ตัวแยก field รู้จัก duration จึงเห็นแค่ full day และตอบราคา ต้องตอบว่าไฟล์ไม่ระบุจำนวนชั่วโมง

Expected rates: `{}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "How long is a full day?", "context_used": true, "act": "fill_rental_scope", "resolved_query": "Zone rental request: pc; organizations external; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[]`; missing fields: `["duration_definition"]`

คำตอบหลังแก้:

Zone rental fees for organizations

The workbook does not define the number of hours or clock windows for half-day/full-day rental. Please confirm the rental hours with the studio.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-staff

คำถาม/ลำดับ: PC rental price for external organizations full day → Is staff overtime included?

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["full_day"], "asks": ["overtime"], "unresolved_targets": [], "original_query": "Is staff overtime included?", "context_used": true, "act": "fill_rental_scope", "resolved_query": "Zone rental request: pc; organizations external; periods full_day; facts overtime"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

The note in the All Zones row says staff overtime compensation is reimbursed under university regulations. It does not state the amount, who pays, or whether it is included in rent.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[]`; missing fields: `["overtime"]`

คำตอบหลังแก้:

Zone rental fees for organizations

The note in the All Zones row says staff overtime compensation is reimbursed under university regulations. It does not state the amount, who pays, or whether it is included in rent.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-reserve

คำถาม/ลำดับ: PC rental price for external organizations full day → How can I reserve it?

ผลก่อนแก้: ไม่ผ่าน; เกณฑ์ที่พลาด: operation, source_sha256, missing_fields

รู้จัก reserve ในตัวแยก field แต่ตัวตรวจบริบทรับเฉพาะ how do I book it ต้องรักษาบริบทเช่าเหมาและแจ้งว่าไฟล์ไม่ระบุขั้นตอน

Expected rates: `{}`

Plan ก่อนแก้: `{}`

คำตอบก่อนแก้:

I am still answering your price question. Which service do you mean: PC, PlayStation 5, Nintendo Switch, Cockpit or VR? You can choose all services.

ผลหลังแก้: True; rates: `[]`; missing fields: `["booking"]`

คำตอบหลังแก้:

Zone rental fees for organizations

The workbook lists rental fees but does not specify the rental booking procedure. Please confirm it with the studio.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-booking-procedure

คำถาม/ลำดับ: PC rental price for external organizations full day → What is the booking procedure?

ผลก่อนแก้: ไม่ผ่าน; เกณฑ์ที่พลาด: operation, source_sha256, missing_fields

booking เป็นคำถามข้อมูลที่ไม่มีชื่อโซน ตัวตรวจ follow-up เดิมพลาด จึงหลุด retrieval ต้องใช้ rental context ที่ client รับแล้ว

Expected rates: `{}`

Plan ก่อนแก้: `{}`

คำตอบก่อนแก้:

I could not find verified PSU Esports Studio - Phuket information for reservation.

ผลหลังแก้: True; rates: `[]`; missing fields: `["booking"]`

คำตอบหลังแก้:

Zone rental fees for organizations

The workbook lists rental fees but does not specify the rental booking procedure. Please confirm it with the studio.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-effective

คำถาม/ลำดับ: PC rental price for external organizations full day → When do these prices take effect?

ผลก่อนแก้: ไม่ผ่าน; เกณฑ์ที่พลาด: original_cell_oracle, missing_fields

prices ทำให้เป็น generic_price แต่ take effect ไม่อยู่ใน effective_date จึงส่งราคาเดิม ต้องตอบว่าไม่ระบุวันที่มีผล

Expected rates: `{}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "When do these prices take effect?", "context_used": true, "act": "fill_rental_scope", "resolved_query": "Zone rental request: pc; organizations external; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[]`; missing fields: `["effective_date"]`

คำตอบหลังแก้:

Zone rental fees for organizations

The workbook does not state an effective or expiry date for these rental rates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-cost-after-details

คำถาม/ลำดับ: PC rental price for external organizations full day → What equipment comes with it? → How much would that be?

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"pc:external:full_day": 4000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "How much would that be?", "context_used": true, "act": "fill_rental_scope", "resolved_query": "Zone rental request: pc; organizations external; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "pc:external:full_day", "value": 4000, "cell": "B8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-typo-cockpit

คำถาม/ลำดับ: cockpitt full-day rental cost for external organizations

ผลก่อนแก้: ไม่ผ่าน; เกณฑ์ที่พลาด: original_cell_oracle

service_mentions ปิด fuzzy เมื่อทั้งประโยคยาวเกิน 50 ตัว ขณะที่ตัวสกัด unknown ลบ token ที่ fuzzy รู้จักออก ทำให้ไม่มี target/unknown แล้วใช้ทุกโซน แก้ใช้ fuzzy token เดิมกับประโยคยาวในขอบเขตเช่าเหมา

Expected rates: `{"cockpit:external:full_day": 2000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["all_zones", "cockpit", "vr", "nintendo_switch", "ps5", "pc"], "groups": ["external"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "cockpitt full-day rental cost for external organizations", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: all_zones, cockpit, vr, nintendo_switch, ps5, pc; organizations external; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**All Zones**
• External organizations: full day 12,000 THB
• Seating capacity: 50 seats; equipment: All gaming equipment

**Cockpit Zone**
• External organizations: full day 2,000 THB
• Seating capacity: 35 seats; equipment: 2 Cockpit units

**VR Zone**
• External organizations: full day 6,000 THB
• Seating capacity: 34 seats; equipment: 1 VR unit

**Nintendo Switch Zone**
• External organizations: full day 2,000 THB
• Seating capacity: 37 seats; equipment: 1 Nintendo Switch unit

**PlayStation 5 Zone**
• External organizations: full day 2,000 THB
• Seating capacity: 37 seats; equipment: 2 PlayStation 5 units

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.
Staff overtime compensation is reimbursed according to university regulations.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "cockpit:external:full_day", "value": 2000, "cell": "B4"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**Cockpit Zone**
• External organizations: full day 2,000 THB
• Seating capacity: 35 seats; equipment: 2 Cockpit units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-typo-nintendo

คำถาม/ลำดับ: nintndo switch full-day rental cost for external organizations

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"nintendo_switch:external:full_day": 2000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["nintendo_switch"], "groups": ["external"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "nintndo switch full-day rental cost for external organizations", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: nintendo_switch; organizations external; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**Nintendo Switch Zone**
• External organizations: full day 2,000 THB
• Seating capacity: 37 seats; equipment: 1 Nintendo Switch unit

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "nintendo_switch:external:full_day", "value": 2000, "cell": "B6"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**Nintendo Switch Zone**
• External organizations: full day 2,000 THB
• Seating capacity: 37 seats; equipment: 1 Nintendo Switch unit

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-unknown-code

คำถาม/ลำดับ: PS55 full-day rental cost for external organizations

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": [], "groups": ["external"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": ["ps55"], "original_query": "PS55 full-day rental cost for external organizations", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: ; organizations external; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

No rental rate is recorded for these requested targets: ps55

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[]`; missing fields: `["unresolved_targets"]`

คำตอบหลังแก้:

Zone rental fees for organizations

No rental rate is recorded for these requested targets: ps55

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-unknown-product

คำถาม/ลำดับ: Xbox full-day rental cost for external organizations

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": [], "groups": ["external"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": ["xbox"], "original_query": "Xbox full-day rental cost for external organizations", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: ; organizations external; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

No rental rate is recorded for these requested targets: xbox

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[]`; missing fields: `["unresolved_targets"]`

คำตอบหลังแก้:

Zone rental fees for organizations

No rental rate is recorded for these requested targets: xbox

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-exclude-period

คำถาม/ลำดับ: PC rental price for external organizations, not half-day

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"pc:external:full_day": 4000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "PC rental price for external organizations, not half-day", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: pc; organizations external; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "pc:external:full_day", "value": 4000, "cell": "B8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-exclude-group

คำถาม/ลำดับ: PC full-day rental cost, not internal organizations

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"pc:external:full_day": 4000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external"], "periods": ["full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "PC full-day rental cost, not internal organizations", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: pc; organizations external; periods full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "pc:external:full_day", "value": 4000, "cell": "B8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-exclude-target

คำถาม/ลำดับ: All rental rates except VR

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"all_zones:external:half_day": 6000, "all_zones:external:full_day": 12000, "all_zones:internal:half_day": 3000, "all_zones:internal:full_day": 6000, "cockpit:external:half_day": 1000, "cockpit:external:full_day": 2000, "cockpit:internal:half_day": 500, "cockpit:internal:full_day": 1000, "nintendo_switch:external:half_day": 1000, "nintendo_switch:external:full_day": 2000, "nintendo_switch:internal:half_day": 500, "nintendo_switch:internal:full_day": 1000, "ps5:external:half_day": 1000, "ps5:external:full_day": 2000, "ps5:internal:half_day": 500, "ps5:internal:full_day": 1000, "pc:external:half_day": 2000, "pc:external:full_day": 4000, "pc:internal:half_day": 1000, "pc:internal:full_day": 2000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["all_zones", "cockpit", "nintendo_switch", "ps5", "pc"], "groups": ["external", "internal"], "periods": ["half_day", "full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "All rental rates except VR", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: all_zones, cockpit, nintendo_switch, ps5, pc; organizations external, internal; periods half_day, full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**All Zones**
• External organizations: half day 6,000 THB / full day 12,000 THB
• Internal organizations: half day 3,000 THB / full day 6,000 THB
• Seating capacity: 50 seats; equipment: All gaming equipment

**Cockpit Zone**
• External organizations: half day 1,000 THB / full day 2,000 THB
• Internal organizations: half day 500 THB / full day 1,000 THB
• Seating capacity: 35 seats; equipment: 2 Cockpit units

**Nintendo Switch Zone**
• External organizations: half day 1,000 THB / full day 2,000 THB
• Internal organizations: half day 500 THB / full day 1,000 THB
• Seating capacity: 37 seats; equipment: 1 Nintendo Switch unit

**PlayStation 5 Zone**
• External organizations: half day 1,000 THB / full day 2,000 THB
• Internal organizations: half day 500 THB / full day 1,000 THB
• Seating capacity: 37 seats; equipment: 2 PlayStation 5 units

**PC Zone**
• External organizations: half day 2,000 THB / full day 4,000 THB
• Internal organizations: half day 1,000 THB / full day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.
Staff overtime compensation is reimbursed according to university regulations.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "all_zones:external:half_day", "value": 6000, "cell": "C3"}, {"id": "all_zones:external:full_day", "value": 12000, "cell": "B3"}, {"id": "all_zones:internal:half_day", "value": 3000, "cell": "E3"}, {"id": "all_zones:internal:full_day", "value": 6000, "cell": "D3"}, {"id": "cockpit:external:half_day", "value": 1000, "cell": "C4"}, {"id": "cockpit:external:full_day", "value": 2000, "cell": "B4"}, {"id": "cockpit:internal:half_day", "value": 500, "cell": "E4"}, {"id": "cockpit:internal:full_day", "value": 1000, "cell": "D4"}, {"id": "nintendo_switch:external:half_day", "value": 1000, "cell": "C6"}, {"id": "nintendo_switch:external:full_day", "value": 2000, "cell": "B6"}, {"id": "nintendo_switch:internal:half_day", "value": 500, "cell": "E6"}, {"id": "nintendo_switch:internal:full_day", "value": 1000, "cell": "D6"}, {"id": "ps5:external:half_day", "value": 1000, "cell": "C7"}, {"id": "ps5:external:full_day", "value": 2000, "cell": "B7"}, {"id": "ps5:internal:half_day", "value": 500, "cell": "E7"}, {"id": "ps5:internal:full_day", "value": 1000, "cell": "D7"}, {"id": "pc:external:half_day", "value": 2000, "cell": "C8"}, {"id": "pc:external:full_day", "value": 4000, "cell": "B8"}, {"id": "pc:internal:half_day", "value": 1000, "cell": "E8"}, {"id": "pc:internal:full_day", "value": 2000, "cell": "D8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**All Zones**
• External organizations: half day 6,000 THB / full day 12,000 THB
• Internal organizations: half day 3,000 THB / full day 6,000 THB
• Seating capacity: 50 seats; equipment: All gaming equipment

**Cockpit Zone**
• External organizations: half day 1,000 THB / full day 2,000 THB
• Internal organizations: half day 500 THB / full day 1,000 THB
• Seating capacity: 35 seats; equipment: 2 Cockpit units

**Nintendo Switch Zone**
• External organizations: half day 1,000 THB / full day 2,000 THB
• Internal organizations: half day 500 THB / full day 1,000 THB
• Seating capacity: 37 seats; equipment: 1 Nintendo Switch unit

**PlayStation 5 Zone**
• External organizations: half day 1,000 THB / full day 2,000 THB
• Internal organizations: half day 500 THB / full day 1,000 THB
• Seating capacity: 37 seats; equipment: 2 PlayStation 5 units

**PC Zone**
• External organizations: half day 2,000 THB / full day 4,000 THB
• Internal organizations: half day 1,000 THB / full day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.
Staff overtime compensation is reimbursed according to university regulations.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-generic-exclusion

คำถาม/ลำดับ: Rental prices except VR

ผลก่อนแก้: ไม่ผ่าน; เกณฑ์ที่พลาด: original_cell_oracle

พบ VR แล้วตัดออกจน targets ว่าง ตัวสร้าง plan ใช้ทุกโซนค่าเริ่มต้นทำให้ VR กลับมา แก้ให้ค่าเริ่มต้นถูกกรองตั้งแต่ต้น

Expected rates: `{"all_zones:external:half_day": 6000, "all_zones:external:full_day": 12000, "all_zones:internal:half_day": 3000, "all_zones:internal:full_day": 6000, "cockpit:external:half_day": 1000, "cockpit:external:full_day": 2000, "cockpit:internal:half_day": 500, "cockpit:internal:full_day": 1000, "nintendo_switch:external:half_day": 1000, "nintendo_switch:external:full_day": 2000, "nintendo_switch:internal:half_day": 500, "nintendo_switch:internal:full_day": 1000, "ps5:external:half_day": 1000, "ps5:external:full_day": 2000, "ps5:internal:half_day": 500, "ps5:internal:full_day": 1000, "pc:external:half_day": 2000, "pc:external:full_day": 4000, "pc:internal:half_day": 1000, "pc:internal:full_day": 2000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["all_zones", "cockpit", "vr", "nintendo_switch", "ps5", "pc"], "groups": ["external", "internal"], "periods": ["half_day", "full_day"], "asks": ["rates"], "unresolved_targets": [], "original_query": "Rental prices except VR", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: all_zones, cockpit, vr, nintendo_switch, ps5, pc; organizations external, internal; periods half_day, full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**All Zones**
• External organizations: half day 6,000 THB / full day 12,000 THB
• Internal organizations: half day 3,000 THB / full day 6,000 THB
• Seating capacity: 50 seats; equipment: All gaming equipment

**Cockpit Zone**
• External organizations: half day 1,000 THB / full day 2,000 THB
• Internal organizations: half day 500 THB / full day 1,000 THB
• Seating capacity: 35 seats; equipment: 2 Cockpit units

**VR Zone**
• External organizations: half day 3,000 THB / full day 6,000 THB
• Internal organizations: half day 1,500 THB / full day 3,000 THB
• Seating capacity: 34 seats; equipment: 1 VR unit

**Nintendo Switch Zone**
• External organizations: half day 1,000 THB / full day 2,000 THB
• Internal organizations: half day 500 THB / full day 1,000 THB
• Seating capacity: 37 seats; equipment: 1 Nintendo Switch unit

**PlayStation 5 Zone**
• External organizations: half day 1,000 THB / full day 2,000 THB
• Internal organizations: half day 500 THB / full day 1,000 THB
• Seating capacity: 37 seats; equipment: 2 PlayStation 5 units

**PC Zone**
• External organizations: half day 2,000 THB / full day 4,000 THB
• Internal organizations: half day 1,000 THB / full day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.
Staff overtime compensation is reimbursed according to university regulations.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "all_zones:external:half_day", "value": 6000, "cell": "C3"}, {"id": "all_zones:external:full_day", "value": 12000, "cell": "B3"}, {"id": "all_zones:internal:half_day", "value": 3000, "cell": "E3"}, {"id": "all_zones:internal:full_day", "value": 6000, "cell": "D3"}, {"id": "cockpit:external:half_day", "value": 1000, "cell": "C4"}, {"id": "cockpit:external:full_day", "value": 2000, "cell": "B4"}, {"id": "cockpit:internal:half_day", "value": 500, "cell": "E4"}, {"id": "cockpit:internal:full_day", "value": 1000, "cell": "D4"}, {"id": "nintendo_switch:external:half_day", "value": 1000, "cell": "C6"}, {"id": "nintendo_switch:external:full_day", "value": 2000, "cell": "B6"}, {"id": "nintendo_switch:internal:half_day", "value": 500, "cell": "E6"}, {"id": "nintendo_switch:internal:full_day", "value": 1000, "cell": "D6"}, {"id": "ps5:external:half_day", "value": 1000, "cell": "C7"}, {"id": "ps5:external:full_day", "value": 2000, "cell": "B7"}, {"id": "ps5:internal:half_day", "value": 500, "cell": "E7"}, {"id": "ps5:internal:full_day", "value": 1000, "cell": "D7"}, {"id": "pc:external:half_day", "value": 2000, "cell": "C8"}, {"id": "pc:external:full_day", "value": 4000, "cell": "B8"}, {"id": "pc:internal:half_day", "value": 1000, "cell": "E8"}, {"id": "pc:internal:full_day", "value": 2000, "cell": "D8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**All Zones**
• External organizations: half day 6,000 THB / full day 12,000 THB
• Internal organizations: half day 3,000 THB / full day 6,000 THB
• Seating capacity: 50 seats; equipment: All gaming equipment

**Cockpit Zone**
• External organizations: half day 1,000 THB / full day 2,000 THB
• Internal organizations: half day 500 THB / full day 1,000 THB
• Seating capacity: 35 seats; equipment: 2 Cockpit units

**Nintendo Switch Zone**
• External organizations: half day 1,000 THB / full day 2,000 THB
• Internal organizations: half day 500 THB / full day 1,000 THB
• Seating capacity: 37 seats; equipment: 1 Nintendo Switch unit

**PlayStation 5 Zone**
• External organizations: half day 1,000 THB / full day 2,000 THB
• Internal organizations: half day 500 THB / full day 1,000 THB
• Seating capacity: 37 seats; equipment: 2 PlayStation 5 units

**PC Zone**
• External organizations: half day 2,000 THB / full day 4,000 THB
• Internal organizations: half day 1,000 THB / full day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.
Staff overtime compensation is reimbursed according to university regulations.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-custom-bundle

คำถาม/ลำดับ: Entire studio rental excluding PC

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": [], "groups": ["external", "internal"], "periods": ["half_day", "full_day"], "asks": ["custom_package"], "unresolved_targets": [], "original_query": "Entire studio rental excluding PC", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: ; organizations external, internal; periods half_day, full_day; facts custom_package"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

The workbook gives the complete All Zones package rate, not a rate for a modified package excluding a zone. Please confirm the custom package price with the studio.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[]`; missing fields: `["custom_package"]`

คำตอบหลังแก้:

Zone rental fees for organizations

The workbook gives the complete All Zones package rate, not a rate for a modified package excluding a zone. Please confirm the custom package price with the studio.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-individual

คำถาม/ลำดับ: Full-day PC rental price for an individual

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"pc:external:full_day": 4000, "pc:internal:full_day": 2000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external", "internal"], "periods": ["full_day"], "asks": ["rates", "eligibility"], "unresolved_targets": [], "original_query": "Full-day PC rental price for an individual", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: pc; organizations external, internal; periods full_day; facts rates, eligibility"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Internal organizations: full day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Rates are grouped by internal/external organizations. The workbook does not assign an individual or student to either organization rate.

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "pc:external:full_day", "value": 4000, "cell": "B8"}, {"id": "pc:internal:full_day", "value": 2000, "cell": "D8"}]`; missing fields: `["eligibility"]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Internal organizations: full day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Rates are grouped by internal/external organizations. The workbook does not assign an individual or student to either organization rate.

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-hourly

คำถาม/ลำดับ: PC hourly rental price

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external", "internal"], "periods": ["half_day", "full_day"], "asks": ["hourly_rental"], "unresolved_targets": [], "original_query": "PC hourly rental price", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: pc; organizations external, internal; periods half_day, full_day; facts hourly_rental"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

This workbook provides half-day/full-day zone rental fees, not an hourly zone rental rate.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[]`; missing fields: `["hourly_rental"]`

คำตอบหลังแก้:

Zone rental fees for organizations

This workbook provides half-day/full-day zone rental fees, not an hourly zone rental rate.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-per-machine

คำถาม/ลำดับ: PC full-day rental price per machine

ผลก่อนแก้: ไม่ผ่าน; เกณฑ์ที่พลาด: missing_fields

per machine ถูกจับเป็น field และ noun ที่ไม่รู้จักพร้อมกัน ต้องเป็นคำขอราคาต่อเครื่องที่ไฟล์ไม่มี ไม่ใช่สินค้าใหม่

Expected rates: `{"pc:external:full_day": 4000, "pc:internal:full_day": 2000}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["pc"], "groups": ["external", "internal"], "periods": ["full_day"], "asks": ["rates", "per_unit"], "unresolved_targets": ["per machine"], "original_query": "PC full-day rental price per machine", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: pc; organizations external, internal; periods full_day; facts rates, per_unit"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Internal organizations: full day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

These are zone rental rates with the listed equipment. The workbook does not provide a rental price per individual machine.

No rental rate is recorded for these requested targets: per machine

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "pc:external:full_day", "value": 4000, "cell": "B8"}, {"id": "pc:internal:full_day", "value": 2000, "cell": "D8"}]`; missing fields: `["per_unit"]`

คำตอบหลังแก้:

Zone rental fees for organizations

**PC Zone**
• External organizations: full day 4,000 THB
• Internal organizations: full day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

These are zone rental rates with the listed equipment. The workbook does not provide a rental price per individual machine.

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-compound-and

คำถาม/ลำดับ: PC full-day rental external organizations and VR half-day rental internal organizations

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{"pc:external:full_day": 4000, "vr:internal:half_day": 1500}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["vr", "pc"], "groups": ["external", "internal"], "periods": ["half_day", "full_day"], "asks": ["rates"], "unresolved_targets": [], "scoped_requests": [{"targets": ["pc"], "groups": ["external"], "periods": ["full_day"]}, {"targets": ["vr"], "groups": ["internal"], "periods": ["half_day"]}], "original_query": "PC full-day rental external organizations and VR half-day rental internal organizations", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: vr, pc; organizations external, internal; periods half_day, full_day; facts rates; scoped requests [{\"targets\": [\"pc\"], \"groups\": [\"external\"], \"periods\": [\"full_day\"]}, {\"targets\": [\"vr\"], \"groups\": [\"internal\"], \"periods\": [\"half_day\"]}]"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**VR Zone**
• Internal organizations: half day 1,500 THB
• Seating capacity: 34 seats; equipment: 1 VR unit

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "vr:internal:half_day", "value": 1500, "cell": "E5"}, {"id": "pc:external:full_day", "value": 4000, "cell": "B8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**VR Zone**
• Internal organizations: half day 1,500 THB
• Seating capacity: 34 seats; equipment: 1 VR unit

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-compound-versus

คำถาม/ลำดับ: PC full-day rental external organizations versus VR half-day rental internal organizations

ผลก่อนแก้: ไม่ผ่าน; เกณฑ์ที่พลาด: original_cell_oracle, missing_fields

แยก clause เฉพาะ and/และ/semicolon ทำให้ versus ตกเป็น unknown และ union เงื่อนไขกลายเป็น Cartesian product แก้แยกตาม versus

Expected rates: `{"pc:external:full_day": 4000, "vr:internal:half_day": 1500}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["vr", "pc"], "groups": ["external", "internal"], "periods": ["half_day", "full_day"], "asks": ["rates"], "unresolved_targets": ["versus"], "original_query": "PC full-day rental external organizations versus VR half-day rental internal organizations", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: vr, pc; organizations external, internal; periods half_day, full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**VR Zone**
• External organizations: half day 3,000 THB / full day 6,000 THB
• Internal organizations: half day 1,500 THB / full day 3,000 THB
• Seating capacity: 34 seats; equipment: 1 VR unit

**PC Zone**
• External organizations: half day 2,000 THB / full day 4,000 THB
• Internal organizations: half day 1,000 THB / full day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

No rental rate is recorded for these requested targets: versus

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "vr:internal:half_day", "value": 1500, "cell": "E5"}, {"id": "pc:external:full_day", "value": 4000, "cell": "B8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**VR Zone**
• Internal organizations: half day 1,500 THB
• Seating capacity: 34 seats; equipment: 1 VR unit

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-compound-with

คำถาม/ลำดับ: Compare PC full-day rental for external organizations with VR half-day rental for internal organizations

ผลก่อนแก้: ไม่ผ่าน; เกณฑ์ที่พลาด: original_cell_oracle, missing_fields

compare...with ไม่แยก clause และ compare/with กลายเป็น unknown แก้แยก with เฉพาะประโยค compare แล้วเก็บเงื่อนไขราย clause

Expected rates: `{"pc:external:full_day": 4000, "vr:internal:half_day": 1500}`

Plan ก่อนแก้: `{"schema_type": "zone_rental_v1", "schema_version": 1, "targets": ["vr", "pc"], "groups": ["external", "internal"], "periods": ["half_day", "full_day"], "asks": ["rates"], "unresolved_targets": ["with", "compare"], "original_query": "Compare PC full-day rental for external organizations with VR half-day rental for internal organizations", "context_used": false, "act": "new_rental_request", "resolved_query": "Zone rental request: vr, pc; organizations external, internal; periods half_day, full_day; facts rates"}`

คำตอบก่อนแก้:

Zone rental fees for organizations

**VR Zone**
• External organizations: half day 3,000 THB / full day 6,000 THB
• Internal organizations: half day 1,500 THB / full day 3,000 THB
• Seating capacity: 34 seats; equipment: 1 VR unit

**PC Zone**
• External organizations: half day 2,000 THB / full day 4,000 THB
• Internal organizations: half day 1,000 THB / full day 2,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

No rental rate is recorded for these requested targets: with, compare

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

ผลหลังแก้: True; rates: `[{"id": "vr:internal:half_day", "value": 1500, "cell": "E5"}, {"id": "pc:external:full_day", "value": 4000, "cell": "B8"}]`; missing fields: `[]`

คำตอบหลังแก้:

Zone rental fees for organizations

**VR Zone**
• Internal organizations: half day 1,500 THB
• Seating capacity: 34 seats; equipment: 1 VR unit

**PC Zone**
• External organizations: full day 4,000 THB
• Seating capacity: 43 seats; equipment: 10 PC units

Prices are per zone for organizations, not per player or machine. The workbook does not define the rental hours or effective dates.

Source: user-provided half/full-day rental workbook
local://service_fee/zone_rental_fees_20261006

### en-topic-games

คำถาม/ลำดับ: PC rental price for external organizations full day → What games are available on PC?

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{}`

Plan ก่อนแก้: `{}`

คำตอบก่อนแก้:

There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

ผลหลังแก้: True; rates: `[]`; missing fields: `[]`

คำตอบหลังแก้:

There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### en-topic-rules

คำถาม/ลำดับ: PC rental price for external organizations full day → Competition rules for CS2

ผลก่อนแก้: ผ่าน; เกณฑ์ที่พลาด: 

เคสนี้ผ่านอยู่แล้ว เก็บไว้ตรวจว่าแก้เคสอื่นแล้วไม่กระทบเงื่อนไขเดิม

Expected rates: `{}`

Plan ก่อนแก้: `{}`

คำตอบก่อนแก้:

Selected Counter-Strike 2 competition rules from the recorded rulebook:
Tournament: Counter-Strike 2 / 2026


**Competition format**
•    Tournament format: Single Elimination

**Players and team composition**
•    Team composition Each team consists of 5 players

**Eligibility and registration**
•    Registration of players is not permitted after the registration period has closed.

**Competition equipment**
•    Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

**Match settings**
•    The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

**Before the match**
•    Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

**Pauses and timeouts**
•    Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
•    Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

ผลหลังแก้: True; rates: `[]`; missing fields: `[]`

คำตอบหลังแก้:

Selected Counter-Strike 2 competition rules from the recorded rulebook:
Tournament: Counter-Strike 2 / 2026


**Competition format**
•    Tournament format: Single Elimination

**Players and team composition**
•    Team composition Each team consists of 5 players

**Eligibility and registration**
•    Registration of players is not permitted after the registration period has closed.

**Competition equipment**
•    Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

**Match settings**
•    The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

**Before the match**
•    Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

**Pauses and timeouts**
•    Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
•    Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026

