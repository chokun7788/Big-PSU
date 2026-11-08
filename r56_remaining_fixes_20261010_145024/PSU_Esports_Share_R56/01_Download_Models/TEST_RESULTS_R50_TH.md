

- โค้ด/dataตรงcandidateที่ทดสอบ HTTP 640ไฟล์; bundledPython/sqlite3/sslผ่าน ; ชุดนี้ไม่มีน้ำหนักโมเดลเต็ม
- candidateHTTP focused22/22, regression110/110และ136/136, unitหลัก52/52
- restart10sessionตามลำดับ+freshsession1ผ่าน11/11; followups4sessionพร้อมกันผ่าน4/4ตามเนื้อหา/session/resolvedquestion
- บนเครื่องผู้จัดทำ Fast16คำขอพร้อมกันผ่านครบp95~3.77s; Mixed6ผ่านครบp95~3.2–3.7s; เกินระดับนั้นพบ503 ไม่รับรองจำนวนเดียวกันบนเครื่องอื่น
- ยังไม่ได้coldbootทั้งสองvariantsบนเครื่องใหม่ ห้ามตีความfilechecksเป็นการทดสอบนั้น
- stateอยู่data/logs/dialogue_state_v1.sqlite3เมื่อเริ่มใช้; TTL30นาทีและsessionIDเดิม; ไม่ใช่ความจำทุกบทสนทนาถาวร
- ไม่แนบlog/stateส่วนตัวของผู้จัดทำ ข้อมูล/นโยบายเจ้าของไม่ได้เปลี่ยนในr50
- VALORANTจำนวนตัวจริง/สำรองยังไม่มีsourceรองรับในชุดข้อมูลที่นำเข้า; ค่าจอดรถ/จอยส่วนตัวยังไม่ยืนยัน

## เครื่องและไฟล์

ใช้ Windows10/11 x64; แนะนำRAM16GBขึ้นไป ผลความเร็วขึ้นอยู่กับCPU/GPU/driver/งานอื่นบนเครื่อง ไม่ได้benchmarkทุกเครื่อง
ต้องมีพื้นที่ทั้งโฟลเดอร์และเพิ่มสำหรับlog/โมเดล เก็บทั้งruntimeและsystemไว้ด้วยกัน
Logอยู่system/PSU_Esports_Chatbot_Local/data/logs/ ตรวจlauncherlogหากเปิดไม่ได้

TEST_RESULTS_R50_TH.mdคือผลรุ่นล่าสุด; README_HISTORICAL_PRE_R50.mdและTEST_RESULTS_TH.mdเป็นหลักฐานเก่าที่เก็บไว้ ไม่ใช่สถานะรุ่นล่าสุด
