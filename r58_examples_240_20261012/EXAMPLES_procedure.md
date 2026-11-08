# ตัวอย่างหมวด procedure — 10 รายการ

**DEMO ONLY: ข้อมูลแยก ไม่เกี่ยวกับข้อมูล Product จริง ห้ามใช้ยืนยันบริการ ราคา กฎ หรือสถานะจริงของ PSU**

คำแปลจัดทำโดยระบบ ยังไม่ได้ตรวจโดยเจ้าของ ข้อมูลเกมอ้างอิงผู้พัฒนา แต่การติดตั้ง เครื่อง ราคา กฎ และปุ่มจำลองไม่ใช่ข้อเท็จจริงของศูนย์

## ตัวอย่าง ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา 01

รหัส: `demo_procedure_01`

### deadline_minutes

สถานะ: known

`6`

### outcome

สถานะ: known

**ไทย:** ได้รับผลการดำเนินการสมมุติ เช็กอิน

**English:** Receive a fictional outcome for Check-in

### preconditions

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### required_documents

สถานะ: known

`["DEMO voucher C01"]`

### steps

สถานะ: known

`[{"contact_id": null, "instruction": {"en": "Select Check-in on the demo page", "th": "เลือกหัวข้อ เช็กอิน ในหน้าตัวอย่าง"}, "order": 1}, {"contact_id": "demo_contact_01", "instruction": {"en": "Provide sample code C01 to the fictional operator", "th": "แจ้งรหัสตัวอย่าง C01 กับเจ้าหน้าที่สมมุติ"}, "order": 2}]`

### topic

สถานะ: known

`"DEMO Check-in"`

## ตัวอย่าง ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา 02

รหัส: `demo_procedure_02`

### deadline_minutes

สถานะ: known

`7`

### outcome

สถานะ: known

**ไทย:** ได้รับผลการดำเนินการสมมุติ บัญชีเกม

**English:** Receive a fictional outcome for Game accounts

### preconditions

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### required_documents

สถานะ: known

`["DEMO voucher C02"]`

### steps

สถานะ: known

`[{"contact_id": null, "instruction": {"en": "Select Game accounts on the demo page", "th": "เลือกหัวข้อ บัญชีเกม ในหน้าตัวอย่าง"}, "order": 1}, {"contact_id": "demo_contact_02", "instruction": {"en": "Provide sample code C02 to the fictional operator", "th": "แจ้งรหัสตัวอย่าง C02 กับเจ้าหน้าที่สมมุติ"}, "order": 2}]`

### topic

สถานะ: known

`"DEMO Game accounts"`

## ตัวอย่าง ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา 03

รหัส: `demo_procedure_03`

### deadline_minutes

สถานะ: known

`8`

### outcome

สถานะ: known

**ไทย:** ได้รับผลการดำเนินการสมมุติ ต่อเวลา

**English:** Receive a fictional outcome for Time extensions

### preconditions

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### required_documents

สถานะ: known

`["DEMO voucher C03"]`

### steps

สถานะ: known

`[{"contact_id": null, "instruction": {"en": "Select Time extensions on the demo page", "th": "เลือกหัวข้อ ต่อเวลา ในหน้าตัวอย่าง"}, "order": 1}, {"contact_id": "demo_contact_03", "instruction": {"en": "Provide sample code C03 to the fictional operator", "th": "แจ้งรหัสตัวอย่าง C03 กับเจ้าหน้าที่สมมุติ"}, "order": 2}]`

### topic

สถานะ: known

`"DEMO Time extensions"`

## ตัวอย่าง ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา 04

รหัส: `demo_procedure_04`

### deadline_minutes

สถานะ: known

`9`

### outcome

สถานะ: known

**ไทย:** ได้รับผลการดำเนินการสมมุติ อุปกรณ์ส่วนตัว

**English:** Receive a fictional outcome for Personal equipment

### preconditions

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### required_documents

สถานะ: known

`["DEMO voucher C04"]`

### steps

สถานะ: known

`[{"contact_id": null, "instruction": {"en": "Select Personal equipment on the demo page", "th": "เลือกหัวข้อ อุปกรณ์ส่วนตัว ในหน้าตัวอย่าง"}, "order": 1}, {"contact_id": "demo_contact_04", "instruction": {"en": "Provide sample code C04 to the fictional operator", "th": "แจ้งรหัสตัวอย่าง C04 กับเจ้าหน้าที่สมมุติ"}, "order": 2}]`

### topic

สถานะ: known

`"DEMO Personal equipment"`

## ตัวอย่าง ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา 05

รหัส: `demo_procedure_05`

### deadline_minutes

สถานะ: known

`10`

### outcome

สถานะ: known

**ไทย:** ได้รับผลการดำเนินการสมมุติ ถ่ายภาพ

**English:** Receive a fictional outcome for Photography

### preconditions

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### required_documents

สถานะ: known

`["DEMO voucher C05"]`

### steps

สถานะ: known

`[{"contact_id": null, "instruction": {"en": "Select Photography on the demo page", "th": "เลือกหัวข้อ ถ่ายภาพ ในหน้าตัวอย่าง"}, "order": 1}, {"contact_id": "demo_contact_05", "instruction": {"en": "Provide sample code C05 to the fictional operator", "th": "แจ้งรหัสตัวอย่าง C05 กับเจ้าหน้าที่สมมุติ"}, "order": 2}]`

### topic

สถานะ: known

`"DEMO Photography"`

## ตัวอย่าง ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา 06

รหัส: `demo_procedure_06`

### deadline_minutes

สถานะ: known

`11`

### outcome

สถานะ: known

**ไทย:** ได้รับผลการดำเนินการสมมุติ ติดตั้งโปรแกรม

**English:** Receive a fictional outcome for Software installation

### preconditions

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### required_documents

สถานะ: known

`["DEMO voucher C06"]`

### steps

สถานะ: known

`[{"contact_id": null, "instruction": {"en": "Select Software installation on the demo page", "th": "เลือกหัวข้อ ติดตั้งโปรแกรม ในหน้าตัวอย่าง"}, "order": 1}, {"contact_id": "demo_contact_06", "instruction": {"en": "Provide sample code C06 to the fictional operator", "th": "แจ้งรหัสตัวอย่าง C06 กับเจ้าหน้าที่สมมุติ"}, "order": 2}]`

### topic

สถานะ: known

`"DEMO Software installation"`

## ตัวอย่าง ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา 07

รหัส: `demo_procedure_07`

### deadline_minutes

สถานะ: known

`12`

### outcome

สถานะ: known

**ไทย:** ได้รับผลการดำเนินการสมมุติ เด็กและผู้ปกครอง

**English:** Receive a fictional outcome for Children and guardians

### preconditions

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### required_documents

สถานะ: known

`["DEMO voucher C07"]`

### steps

สถานะ: known

`[{"contact_id": null, "instruction": {"en": "Select Children and guardians on the demo page", "th": "เลือกหัวข้อ เด็กและผู้ปกครอง ในหน้าตัวอย่าง"}, "order": 1}, {"contact_id": "demo_contact_07", "instruction": {"en": "Provide sample code C07 to the fictional operator", "th": "แจ้งรหัสตัวอย่าง C07 กับเจ้าหน้าที่สมมุติ"}, "order": 2}]`

### topic

สถานะ: known

`"DEMO Children and guardians"`

## ตัวอย่าง ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา 08

รหัส: `demo_procedure_08`

### deadline_minutes

สถานะ: known

`13`

### outcome

สถานะ: known

**ไทย:** ได้รับผลการดำเนินการสมมุติ อาหารและเครื่องดื่ม

**English:** Receive a fictional outcome for Food and drinks

### preconditions

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### required_documents

สถานะ: known

`["DEMO voucher C08"]`

### steps

สถานะ: known

`[{"contact_id": null, "instruction": {"en": "Select Food and drinks on the demo page", "th": "เลือกหัวข้อ อาหารและเครื่องดื่ม ในหน้าตัวอย่าง"}, "order": 1}, {"contact_id": "demo_contact_08", "instruction": {"en": "Provide sample code C08 to the fictional operator", "th": "แจ้งรหัสตัวอย่าง C08 กับเจ้าหน้าที่สมมุติ"}, "order": 2}]`

### topic

สถานะ: known

`"DEMO Food and drinks"`

## ตัวอย่าง ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา 09

รหัส: `demo_procedure_09`

### deadline_minutes

สถานะ: known

`14`

### outcome

สถานะ: known

**ไทย:** ได้รับผลการดำเนินการสมมุติ ของหาย

**English:** Receive a fictional outcome for Lost property

### preconditions

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### required_documents

สถานะ: known

`["DEMO voucher C09"]`

### steps

สถานะ: known

`[{"contact_id": null, "instruction": {"en": "Select Lost property on the demo page", "th": "เลือกหัวข้อ ของหาย ในหน้าตัวอย่าง"}, "order": 1}, {"contact_id": "demo_contact_09", "instruction": {"en": "Provide sample code C09 to the fictional operator", "th": "แจ้งรหัสตัวอย่าง C09 กับเจ้าหน้าที่สมมุติ"}, "order": 2}]`

### topic

สถานะ: known

`"DEMO Lost property"`

## ตัวอย่าง ขั้นตอนจอง/จ่าย/เช็กอิน/แก้ปัญหา 10

รหัส: `demo_procedure_10`

### deadline_minutes

สถานะ: known

`15`

### outcome

สถานะ: known

**ไทย:** ได้รับผลการดำเนินการสมมุติ เลื่อนการจอง

**English:** Receive a fictional outcome for Rescheduling

### preconditions

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### required_documents

สถานะ: known

`["DEMO voucher C10"]`

### steps

สถานะ: known

`[{"contact_id": null, "instruction": {"en": "Select Rescheduling on the demo page", "th": "เลือกหัวข้อ เลื่อนการจอง ในหน้าตัวอย่าง"}, "order": 1}, {"contact_id": "demo_contact_10", "instruction": {"en": "Provide sample code C10 to the fictional operator", "th": "แจ้งรหัสตัวอย่าง C10 กับเจ้าหน้าที่สมมุติ"}, "order": 2}]`

### topic

สถานะ: known

`"DEMO Rescheduling"`
