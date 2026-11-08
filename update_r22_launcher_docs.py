from pathlib import Path

root = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")

def change(relative, old, new):
    path = root / relative
    text = path.read_text(encoding="utf-8-sig")
    if text.count(old) != 1:
        raise RuntimeError(f"Expected one matching section: {relative}")
    path.write_text(text.replace(old, new), encoding="utf-8")

path = root / "deployment_templates/Start-PSU-Esports-Chatbot.ps1"
text = path.read_text(encoding="utf-8-sig")
start = text.index('$bookingDashboardPort = if ($ownerDashboardAt8080)')
end = text.index('$url = "http://127.0.0.1:$Port/"', start)
text = text[:start] + '''# The standalone Chatbot fetches the WordPress exports on demand. An
# already-running owner Dashboard remains authoritative for its own calendar.
$env:PSU_LIVE_BOOKING_FETCH_MODE = if ($ownerDashboardAt8080) { "dashboard" } else { "wordpress" }
$env:PSU_LIVE_BOOKING_ENABLED = "1"
$env:PSU_LIVE_BOOKING_STATUS_URL = if ($ownerDashboardAt8080) { "http://127.0.0.1:8080/api/chatbot-status" } else { "http://127.0.0.1:8091/api/chatbot-status" }
$env:PSU_LIVE_BOOKING_TIMEOUT_SEC = "5"
$env:PSU_LIVE_BOOKING_CACHE_SEC = "0"

''' + text[end:]
old = 'Write-Host $(if ($env:PSU_LIVE_BOOKING_ENABLED -eq "1") { "Dashboard connection: $($dashboardProbe.Kind) on port $bookingDashboardPort; live CSV data is checked for each question" } else { "Dashboard connection: unavailable on port $bookingDashboardPort; live availability cannot be confirmed" })'
assert text.count(old) == 1
text = text.replace(old, 'Write-Host $(if ($ownerDashboardAt8080) { "Booking: read owner Dashboard at port 8080 on each status question" } else { "Booking: fetch WordPress directly on each status question; no separate Dashboard process required" })')
path.write_text(text, encoding="utf-8")

readme = "deployment_templates/README_TH.md"
change(readme, "เวอร์ชัน `2026.09.28-owner-review-candidate-r8`", "เวอร์ชันที่ระบุใน `package_manifest.json`")
change(readme, "4. ถ้า Dashboard ต้นฉบับบน D: ทำงานที่พอร์ต 8080 ระบบจะใช้ข้อมูลจากตัวนั้นเมื่อยืนยันช่วงพักและข้อมูล CSV สดได้; มิฉะนั้นจะเปิด Dashboard ที่มากับแพ็กเกจบนพอร์ต 8091 เพื่อให้คำถามสถานะอ่านข้อมูลสด", "4. เมื่อถามสถานะว่าง/ถูกจองหรือรอบที่จองได้ Chatbot จะดึง WordPress CSV สดให้เอง โดยใช้ตัวคำนวณ Slot และปฏิทินที่บันทึกไว้ของ Dashboard ไม่ต้องเปิด `start-dashboard.bat` สำหรับชุด Chatbot อย่างเดียว ถ้าเปิด Dashboard เจ้าของบน D: ที่พอร์ต 8080 ก่อน Chatbot จะอ่านจากตัวนั้นเพื่อคงปฏิทินที่เจ้าของแก้ไว้")
change(readme, "Chatbot ใช้ 8090 ส่วน Dashboard ใช้ 8080 เมื่อเปิด D: ก่อน หรือ 8091 เมื่อใช้ชุดในแพ็กเกจ", "Chatbot ใช้ 8090 และดึง Booking เมื่อมีคำถามสถานะ หากเปิด Dashboard บน D: ก่อนจะอ่านจากพอร์ต 8080")
change(readme, "Dashboard ต้นฉบับที่เปิดด้วย `start-dashboard.bat` ใช้พอร์ต 8080 ถ้าเปิด **ก่อน Chatbot** ตัวเปิดจะตรวจสถานะจาก D: โดยตรง ถ้าดึง CSV หรือยืนยันช่วงพักเที่ยงไม่ได้ Chatbot ยังเปิดได้แต่จะไม่อ้างว่ารู้สถานะจองสด หากไม่ได้เปิด D: ก่อน แพ็กเกจจะใช้ Dashboard ของตัวเองบน 8091; ถ้าเปิด D: ภายหลัง ให้ปิดแล้วเปิด Chatbot ใหม่เพื่อสลับแหล่งสถานะ การแก้ตารางใน D: ไม่ถูกคัดลอกไปอีกชุดโดยอัตโนมัติ", "Dashboard ต้นฉบับที่เปิดด้วย `start-dashboard.bat` ใช้พอร์ต 8080 ถ้าเปิด **ก่อน Chatbot** ตัวเปิดจะเลือกข้อมูลจาก D: และลองอ่านข้อมูลใหม่เมื่อมีคำถามสถานะทุกครั้ง ไม่ปิดความสามารถนี้ถาวรเพราะอินเทอร์เน็ตล่มตอนเปิดระบบ หากไม่ได้เปิด D: ก่อน Chatbot จะดึง WordPress เองพร้อมใช้ปฏิทินของแพ็กเกจ ถ้าเปิด D: ภายหลัง ให้ปิดแล้วเปิด Chatbot ใหม่เพื่อสลับแหล่งสถานะ การแก้ตารางใน D: ไม่ถูกคัดลอกไปอีกชุดโดยอัตโนมัติ")
change(readme, "ระบบอ่านข้อมูลสดจาก WordPress CSV ผ่าน Booking Dashboard ในเครื่อง", "ระบบอ่าน WordPress CSV สดเมื่อมีคำถาม โดยใช้ตัวคำนวณเดิมของ Booking Dashboard หรืออ่านจาก Dashboard เจ้าของที่เลือกไว้")
change(readme, "ตรวจ Dashboard ที่ใช้จริงบนพอร์ต 8080 หรือ 8091 และดูข้อความสถานะตอนเริ่มระบบ", "ตรวจอินเทอร์เน็ตและข้อความสาเหตุที่ตอบกลับ; ถ้าเปิด D: ก่อน Chatbot ให้ตรวจ Dashboard บนพอร์ต 8080 ด้วย")
change(readme, "คำถามโซน เช่น `PC Zone ว่างไหม`, `VR ว่างไหม` หรือ `Nintendo ว่างไหม` จะสรุปจำนวนว่างของโซนนั้น และจะแสดงรายชื่อเมื่อถามว่า `มีอะไรว่างบ้าง` หรือ `Which stations are free?`", "คำถามโซน เช่น `PC Zone ว่างไหม`, `VR ว่างไหม` หรือ `Nintendo ว่างไหม` จะสรุปจำนวนว่างและสถานะรายเครื่องทั้งหมดในโซนนั้น")
change(readme, "Chatbot อ่านเฉพาะสถานะเปิด-ปิดและจำนวน Slot ว่าง/ถูกจองจาก Booking Dashboard ที่ดึง WordPress CSV สด โดยไม่รับชื่อผู้จอง รหัสนัดหมาย อีเมล หรือเบอร์โทรเข้า Chatbot", "ตัวเชื่อมต่อ Booking อ่าน WordPress CSV สดแล้วตัดชื่อผู้จอง รหัสนัดหมาย อีเมล เบอร์โทร และ token ก่อนคำนวณสถานะ ส่งเข้าระบบตอบเฉพาะสถานะเปิด-ปิดและจำนวน Slot ว่าง/ถูกจอง ไม่บันทึก CSV ดิบลง log")
policy = "deployment_templates/LOCAL_OPERATION_AND_DATA_POLICY_TH.md"
change(policy, "เมื่อเปิด Chatbot ระบบจะใช้ Dashboard ต้นฉบับที่ทำงานบน `http://127.0.0.1:8080/` หากตรวจสอบชนิดระบบ ข้อมูล CSV สด และช่วงพักเที่ยงได้ มิฉะนั้นจะเริ่ม Dashboard ที่มากับแพ็กเกจบน `http://127.0.0.1:8091/` เมื่อพอร์ตว่าง หากตรวจสอบข้อมูลสดไม่ได้ ระบบยังตอบข้อมูลคงที่ได้แต่จะไม่ยืนยันว่า Slot ว่าง", "เมื่อถามสถานะจอง Chatbot จะดึง WordPress CSV สดโดยใช้ตัวคำนวณ Slot เดิมและปฏิทินที่บันทึกไว้ในแพ็กเกจ ไม่ต้องเริ่ม Dashboard แยก หากมี Dashboard เจ้าของบน `http://127.0.0.1:8080/` ทำงานก่อนเปิด Chatbot จะอ่านจากตัวนั้นเพื่อคงปฏิทินของเจ้าของ หากดึงข้อมูลไม่สำเร็จจะตอบสาเหตุและลองใหม่เมื่อมีคำถามถัดไป ไม่อ้างว่า Slot ว่างจากข้อมูลตัวอย่าง ตัวเชื่อมต่อตัดข้อมูลผู้จองก่อนส่งสถานะเข้าสู่ระบบตอบและไม่บันทึก CSV ดิบ")
scope = "deployment_templates/OWNER_HANDOFF_AND_SCOPE_TH.md"
change(scope, "การอ่านสถานะ Slot จาก Booking Dashboard แบบ read-only เมื่อ WordPress CSV สดพร้อมใช้งาน โดยไม่ส่งข้อมูลผู้จองเข้า Chatbot", "การดึง WordPress CSV เมื่อถามสถานะ Slot โดยใช้ตัวคำนวณ Booking Dashboard แบบอ่านอย่างเดียว ไม่ต้องเปิด Dashboard เพิ่มสำหรับชุด Chatbot; ตัวเชื่อมต่อตัดข้อมูลผู้จองก่อนส่งสถานะเข้าระบบตอบ")
print("Launcher and operation documents updated; previous versions are backed up.")
