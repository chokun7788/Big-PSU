# ตัวอย่างหมวด policy — 10 รายการ

**DEMO ONLY: ข้อมูลแยก ไม่เกี่ยวกับข้อมูล Product จริง ห้ามใช้ยืนยันบริการ ราคา กฎ หรือสถานะจริงของ PSU**

คำแปลจัดทำโดยระบบ ยังไม่ได้ตรวจโดยเจ้าของ ข้อมูลเกมอ้างอิงผู้พัฒนา แต่การติดตั้ง เครื่อง ราคา กฎ และปุ่มจำลองไม่ใช่ข้อเท็จจริงของศูนย์

## ตัวอย่าง นโยบายและกฎศูนย์ 01

รหัส: `demo_policy_01`

### conditions_all

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### consequence

สถานะ: known

**ไทย:** ผลสมมุติ: ส่งต่อผู้ดูแลตัวอย่าง C01

**English:** Fictional consequence: refer to demo operator C01

### decision

สถานะ: known

`"prohibited"`

### details

สถานะ: known

**ไทย:** กฎสมมุติเรื่อง เช็กอิน ไม่ใช่นโยบาย PSU ให้ทำตามขั้นตอนตัวอย่าง C01

**English:** Fictional rule for Check-in, not PSU policy; follow sample procedure C01

### exceptions

สถานะ: known

**ไทย:** ข้อยกเว้นสมมุติ: ใช้เฉพาะกิจกรรมทดสอบที่ระบุ

**English:** Fictional exception: only the specified test activity

### procedure_id

สถานะ: known

`"demo_procedure_01"`

### subject

สถานะ: known

**ไทย:** ตัวอย่าง นโยบาย เช็กอิน 01

**English:** Demo Check-in policy 01

### topic

สถานะ: known

`"DEMO policy Check-in"`

## ตัวอย่าง นโยบายและกฎศูนย์ 02

รหัส: `demo_policy_02`

### conditions_all

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### consequence

สถานะ: known

**ไทย:** ผลสมมุติ: ส่งต่อผู้ดูแลตัวอย่าง C02

**English:** Fictional consequence: refer to demo operator C02

### decision

สถานะ: known

`"required"`

### details

สถานะ: known

**ไทย:** กฎสมมุติเรื่อง บัญชีเกม ไม่ใช่นโยบาย PSU ให้ทำตามขั้นตอนตัวอย่าง C02

**English:** Fictional rule for Game accounts, not PSU policy; follow sample procedure C02

### exceptions

สถานะ: known

**ไทย:** ข้อยกเว้นสมมุติ: ใช้เฉพาะกิจกรรมทดสอบที่ระบุ

**English:** Fictional exception: only the specified test activity

### procedure_id

สถานะ: known

`"demo_procedure_02"`

### subject

สถานะ: known

**ไทย:** ตัวอย่าง นโยบาย บัญชีเกม 02

**English:** Demo Game accounts policy 02

### topic

สถานะ: known

`"DEMO policy Game accounts"`

## ตัวอย่าง นโยบายและกฎศูนย์ 03

รหัส: `demo_policy_03`

### conditions_all

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### consequence

สถานะ: known

**ไทย:** ผลสมมุติ: ส่งต่อผู้ดูแลตัวอย่าง C03

**English:** Fictional consequence: refer to demo operator C03

### decision

สถานะ: known

`"conditional"`

### details

สถานะ: known

**ไทย:** กฎสมมุติเรื่อง ต่อเวลา ไม่ใช่นโยบาย PSU ให้ทำตามขั้นตอนตัวอย่าง C03

**English:** Fictional rule for Time extensions, not PSU policy; follow sample procedure C03

### exceptions

สถานะ: known

**ไทย:** ข้อยกเว้นสมมุติ: ใช้เฉพาะกิจกรรมทดสอบที่ระบุ

**English:** Fictional exception: only the specified test activity

### procedure_id

สถานะ: known

`"demo_procedure_03"`

### subject

สถานะ: known

**ไทย:** ตัวอย่าง นโยบาย ต่อเวลา 03

**English:** Demo Time extensions policy 03

### topic

สถานะ: known

`"DEMO policy Time extensions"`

## ตัวอย่าง นโยบายและกฎศูนย์ 04

รหัส: `demo_policy_04`

### conditions_all

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### consequence

สถานะ: known

**ไทย:** ผลสมมุติ: ส่งต่อผู้ดูแลตัวอย่าง C04

**English:** Fictional consequence: refer to demo operator C04

### decision

สถานะ: known

`"allowed"`

### details

สถานะ: known

**ไทย:** กฎสมมุติเรื่อง อุปกรณ์ส่วนตัว ไม่ใช่นโยบาย PSU ให้ทำตามขั้นตอนตัวอย่าง C04

**English:** Fictional rule for Personal equipment, not PSU policy; follow sample procedure C04

### exceptions

สถานะ: known

**ไทย:** ข้อยกเว้นสมมุติ: ใช้เฉพาะกิจกรรมทดสอบที่ระบุ

**English:** Fictional exception: only the specified test activity

### procedure_id

สถานะ: known

`"demo_procedure_04"`

### subject

สถานะ: known

**ไทย:** ตัวอย่าง นโยบาย อุปกรณ์ส่วนตัว 04

**English:** Demo Personal equipment policy 04

### topic

สถานะ: known

`"DEMO policy Personal equipment"`

## ตัวอย่าง นโยบายและกฎศูนย์ 05

รหัส: `demo_policy_05`

### conditions_all

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### consequence

สถานะ: known

**ไทย:** ผลสมมุติ: ส่งต่อผู้ดูแลตัวอย่าง C05

**English:** Fictional consequence: refer to demo operator C05

### decision

สถานะ: known

`"prohibited"`

### details

สถานะ: known

**ไทย:** กฎสมมุติเรื่อง ถ่ายภาพ ไม่ใช่นโยบาย PSU ให้ทำตามขั้นตอนตัวอย่าง C05

**English:** Fictional rule for Photography, not PSU policy; follow sample procedure C05

### exceptions

สถานะ: known

**ไทย:** ข้อยกเว้นสมมุติ: ใช้เฉพาะกิจกรรมทดสอบที่ระบุ

**English:** Fictional exception: only the specified test activity

### procedure_id

สถานะ: known

`"demo_procedure_05"`

### subject

สถานะ: known

**ไทย:** ตัวอย่าง นโยบาย ถ่ายภาพ 05

**English:** Demo Photography policy 05

### topic

สถานะ: known

`"DEMO policy Photography"`

## ตัวอย่าง นโยบายและกฎศูนย์ 06

รหัส: `demo_policy_06`

### conditions_all

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### consequence

สถานะ: known

**ไทย:** ผลสมมุติ: ส่งต่อผู้ดูแลตัวอย่าง C06

**English:** Fictional consequence: refer to demo operator C06

### decision

สถานะ: known

`"required"`

### details

สถานะ: known

**ไทย:** กฎสมมุติเรื่อง ติดตั้งโปรแกรม ไม่ใช่นโยบาย PSU ให้ทำตามขั้นตอนตัวอย่าง C06

**English:** Fictional rule for Software installation, not PSU policy; follow sample procedure C06

### exceptions

สถานะ: known

**ไทย:** ข้อยกเว้นสมมุติ: ใช้เฉพาะกิจกรรมทดสอบที่ระบุ

**English:** Fictional exception: only the specified test activity

### procedure_id

สถานะ: known

`"demo_procedure_06"`

### subject

สถานะ: known

**ไทย:** ตัวอย่าง นโยบาย ติดตั้งโปรแกรม 06

**English:** Demo Software installation policy 06

### topic

สถานะ: known

`"DEMO policy Software installation"`

## ตัวอย่าง นโยบายและกฎศูนย์ 07

รหัส: `demo_policy_07`

### conditions_all

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### consequence

สถานะ: known

**ไทย:** ผลสมมุติ: ส่งต่อผู้ดูแลตัวอย่าง C07

**English:** Fictional consequence: refer to demo operator C07

### decision

สถานะ: known

`"conditional"`

### details

สถานะ: known

**ไทย:** กฎสมมุติเรื่อง เด็กและผู้ปกครอง ไม่ใช่นโยบาย PSU ให้ทำตามขั้นตอนตัวอย่าง C07

**English:** Fictional rule for Children and guardians, not PSU policy; follow sample procedure C07

### exceptions

สถานะ: known

**ไทย:** ข้อยกเว้นสมมุติ: ใช้เฉพาะกิจกรรมทดสอบที่ระบุ

**English:** Fictional exception: only the specified test activity

### procedure_id

สถานะ: known

`"demo_procedure_07"`

### subject

สถานะ: known

**ไทย:** ตัวอย่าง นโยบาย เด็กและผู้ปกครอง 07

**English:** Demo Children and guardians policy 07

### topic

สถานะ: known

`"DEMO policy Children and guardians"`

## ตัวอย่าง นโยบายและกฎศูนย์ 08

รหัส: `demo_policy_08`

### conditions_all

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### consequence

สถานะ: known

**ไทย:** ผลสมมุติ: ส่งต่อผู้ดูแลตัวอย่าง C08

**English:** Fictional consequence: refer to demo operator C08

### decision

สถานะ: known

`"allowed"`

### details

สถานะ: known

**ไทย:** กฎสมมุติเรื่อง อาหารและเครื่องดื่ม ไม่ใช่นโยบาย PSU ให้ทำตามขั้นตอนตัวอย่าง C08

**English:** Fictional rule for Food and drinks, not PSU policy; follow sample procedure C08

### exceptions

สถานะ: known

**ไทย:** ข้อยกเว้นสมมุติ: ใช้เฉพาะกิจกรรมทดสอบที่ระบุ

**English:** Fictional exception: only the specified test activity

### procedure_id

สถานะ: known

`"demo_procedure_08"`

### subject

สถานะ: known

**ไทย:** ตัวอย่าง นโยบาย อาหารและเครื่องดื่ม 08

**English:** Demo Food and drinks policy 08

### topic

สถานะ: known

`"DEMO policy Food and drinks"`

## ตัวอย่าง นโยบายและกฎศูนย์ 09

รหัส: `demo_policy_09`

### conditions_all

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### consequence

สถานะ: known

**ไทย:** ผลสมมุติ: ส่งต่อผู้ดูแลตัวอย่าง C09

**English:** Fictional consequence: refer to demo operator C09

### decision

สถานะ: known

`"prohibited"`

### details

สถานะ: known

**ไทย:** กฎสมมุติเรื่อง ของหาย ไม่ใช่นโยบาย PSU ให้ทำตามขั้นตอนตัวอย่าง C09

**English:** Fictional rule for Lost property, not PSU policy; follow sample procedure C09

### exceptions

สถานะ: known

**ไทย:** ข้อยกเว้นสมมุติ: ใช้เฉพาะกิจกรรมทดสอบที่ระบุ

**English:** Fictional exception: only the specified test activity

### procedure_id

สถานะ: known

`"demo_procedure_09"`

### subject

สถานะ: known

**ไทย:** ตัวอย่าง นโยบาย ของหาย 09

**English:** Demo Lost property policy 09

### topic

สถานะ: known

`"DEMO policy Lost property"`

## ตัวอย่าง นโยบายและกฎศูนย์ 10

รหัส: `demo_policy_10`

### conditions_all

สถานะ: known

`[{"field": "demo_environment", "operator": "eq", "value": true}]`

### consequence

สถานะ: known

**ไทย:** ผลสมมุติ: ส่งต่อผู้ดูแลตัวอย่าง C10

**English:** Fictional consequence: refer to demo operator C10

### decision

สถานะ: known

`"required"`

### details

สถานะ: known

**ไทย:** กฎสมมุติเรื่อง เลื่อนการจอง ไม่ใช่นโยบาย PSU ให้ทำตามขั้นตอนตัวอย่าง C10

**English:** Fictional rule for Rescheduling, not PSU policy; follow sample procedure C10

### exceptions

สถานะ: known

**ไทย:** ข้อยกเว้นสมมุติ: ใช้เฉพาะกิจกรรมทดสอบที่ระบุ

**English:** Fictional exception: only the specified test activity

### procedure_id

สถานะ: known

`"demo_procedure_10"`

### subject

สถานะ: known

**ไทย:** ตัวอย่าง นโยบาย เลื่อนการจอง 10

**English:** Demo Rescheduling policy 10

### topic

สถานะ: known

`"DEMO policy Rescheduling"`
