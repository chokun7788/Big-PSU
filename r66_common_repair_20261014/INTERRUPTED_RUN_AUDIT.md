# รอบที่ไม่ใช้เป็นผลสำเร็จ

`MATRIX_offline_03.jsonl` หยุดที่ 184/223 requests ไม่มีผลครบหรือ completion artifact ของรอบนั้น สถานะ running ในไฟล์เดิมจึงเป็น checkpoint ที่ค้าง ไม่ใช้เป็นหลักฐานว่ายังรันอยู่หรือว่าผ่านครบ

ใน session นี้ตรวจพบว่า shell session เดิมใช้ต่อไม่ได้และไม่พบ Python process ของรอบดังกล่าวจากการตรวจ process ที่มีสิทธิ์เพียงพอ สาเหตุที่ process สิ้นสุดไม่ได้รับการยืนยัน จึงไม่สรุปว่าเครื่อง/โมเดล/ข้อมูลเป็นต้นเหตุ

เก็บ partial rows/status/log เดิมไว้ และเริ่ม tag ใหม่จาก snapshot ใหม่ ไม่ต่อผลต่างเวอร์ชันโค้ดให้ดูเหมือนเป็นรอบเดียว

`final06` หยุดตาม gate เพราะการตาม control_set→game กว้างเกินไป ทำให้ canonical all-details ของข้อมูลใหม่ผิด 40/480 ข้อ แก้ role/intent scope แล้วรอบถัดไปกลับมาผ่าน 480/480

`final08` หยุดตาม gate เพราะ role search อ่าน withdrawn ID แล้วเกิด KeyError แก้ให้กรอง active records และทดสอบ native withdrawal behavior ต่อ โดยไม่ลบข้อสอบที่จับ regression ได้

รอบที่ชื่อ final ไม่ได้แปลว่า assertions ทุกข้อผ่าน ต้องอ่าน STATUS.json, stage logs, native raw failures และ final report ประกอบกัน
