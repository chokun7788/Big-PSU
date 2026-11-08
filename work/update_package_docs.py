from pathlib import Path


project = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")


def replace_once(relative: str, old: str, new: str) -> None:
    path = project / relative
    content = path.read_text(encoding="utf-8")
    if content.count(old) != 1:
        raise RuntimeError(f"Expected one match in {path}, got {content.count(old)}")
    path.write_text(content.replace(old, new), encoding="utf-8")


replace_once(
    "tools/build_owner_local_package.ps1",
    '$outputRootPath = Join-Path $projectRoot $OutputRoot',
    '$outputRootPath = if ([System.IO.Path]::IsPathRooted($OutputRoot)) { $OutputRoot } else { Join-Path $projectRoot $OutputRoot }',
)
replace_once(
    "deployment_templates/README_TH.md",
    'เวอร์ชัน `2026.09.25-owner-review-candidate`',
    'เวอร์ชัน `2026.09.26-owner-review-candidate`',
)
replace_once(
    "deployment_templates/README_TH.md",
    '''4. ระบบจะเปิด Booking Dashboard ภายในเครื่องที่ `http://127.0.0.1:8091/` ให้อัตโนมัติ เพื่อให้คำถาม `ตอนนี้เปิดไหม` และ `Slot ไหนว่าง` อ่านสถานะสดได้
''',
    '''4. ระบบจะเปิด Booking Dashboard ภายในเครื่องที่ `http://127.0.0.1:8091/` ให้อัตโนมัติ เพื่อให้คำถาม `ตอนนี้เปิดไหม` และ `Slot ไหนว่าง` อ่านสถานะสดได้

หากต้องการปิดหน้าต่างคำสั่งหลังเปิดระบบ ให้ใช้ `Open-PSU-Esports-Background.cmd` แทน ระบบจะรันเบื้องหลังและเก็บ log การเริ่มครั้งใหม่ไว้ใน `data\\logs\\launcher\\` เปิด Chatbot ที่ `http://127.0.0.1:8080/` และ Dashboard ที่ `http://127.0.0.1:8091/` ได้ตลอดที่เครื่องยังเปิดอยู่ วิธีนี้ยังไม่เริ่มเองหลังเข้าสู่ Windows; หากต้องการแบบนั้นให้ตั้ง Windows Task Scheduler กับไฟล์นี้บนเครื่องเจ้าของ

Dashboard ต้นฉบับที่เปิดด้วย `start-dashboard.bat` ใช้พอร์ต 8080 เช่นเดียวกับ Chatbot และเป็นคนละชุดข้อมูลกับ Dashboard ในแพ็กเกจ หากต้องใช้ Chatbot กับสถานะเดียวกัน ให้เปิด Dashboard ในแพ็กเกจที่พอร์ต 8091; ปิด Dashboard ต้นฉบับก่อนเปิด Chatbot เพื่อไม่ให้พอร์ตชนกัน การแก้เวลาหรือวันปิดใน Dashboard ต้นฉบับจะไม่ย้ายมาแพ็กเกจโดยอัตโนมัติ
''',
)
replace_once(
    "deployment_templates/README_TH.md",
    '''- `PC2 ว่างไหม` หรือ `PC #02 ว่างไหม` (หากไม่ระบุวันและเวลา ระบบตรวจเวลาปัจจุบัน)
''',
    '''- `PC2 ว่างไหม` หรือ `PC #02 ว่างไหม` (หากไม่ระบุวันและเวลา ระบบตรวจเวลาปัจจุบัน)
- `วันนี้ตอน10โมง PC1 ว่างไหม` (ตรวจ PC #01 เฉพาะช่วง 10:00-11:00)
''',
)
replace_once(
    "deployment_templates/README_TH.md",
    'การตอบช่วงเวลา เช่น `13:00-14:00` จะนับว่าเครื่องว่างก็ต่อเมื่อว่างตลอดทั้งช่วงเท่านั้น',
    'ช่วง 12:00-13:00 ไม่เปิดให้จอง และ VR ที่จอง 30 นาทีจะกันสิทธิ์เต็ม Slot ชั่วโมงนั้น เช่น 09:00-09:30 กัน 09:00-10:00\nการตอบช่วงเวลา เช่น `13:00-14:00` จะนับว่าเครื่องว่างก็ต่อเมื่อว่างตลอดทั้งช่วงเท่านั้น',
)
print("Updated package guide, version, and absolute output support.")
