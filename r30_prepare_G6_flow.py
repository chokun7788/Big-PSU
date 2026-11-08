from pathlib import Path
s=Path('r30_finish_flow_G5.py').read_text(encoding='utf-8')
s=s.replace('2026.10.02-full-improvement-r30-G5','2026.10.02-full-improvement-r30-G6').replace("assert (r/'final_G5_all_summary.json').exists()","assert (r/'final_G6_all_summary.json').exists()")
s=s.replace('flow_before_final_G5.md','flow_before_final_G6.md').replace('flow_final_G5.md','flow_final_G6.md').replace('ทุกโมดูล 424 ข้อ','ทุกโมดูล 425 ข้อ').replace('G5/G5b\'','G5/G5b/G6\'')
s=s.replace('79 + 43 + 8 + 39 + 280 + 320 + 128 = 897','79 + 43 + 8 + 45 + 280 + 320 + 128 = 903')
s=s.replace("['P1-A','P1-B','P1-C','424','897'","['P1-A','P1-B','P1-C','425','903'")
s=s.replace('FINAL_G5_DETAILED_CAUSE_ANALYSIS_TH.md','FINAL_G6_DETAILED_CAUSE_ANALYSIS_TH.md').replace('FINAL_G5_FULL_ANALYSIS_SUMMARY.json','FINAL_G6_FULL_ANALYSIS_SUMMARY.json').replace('release_preflight_G5.json','release_preflight_G6.json')
s=s.replace('Flow ต่อสำหรับประโยคที่ยังไม่ครอบคลุม:', '''G6: ตรวจเว็บจริงเพิ่มพบ `CS2 แข่งกี่วันและแข่งที่ไหน` ยังไม่มี duration/venue concept ทั้งที่ `competition_rules_cs2_psu_phuket_2026_s08_c01` ระบุทั้งสองเรื่องในข้อเดียว เพิ่ม proposition ที่ผูก CS2 พร้อม literal clause ทั้งไทย/อังกฤษและ qualifier ว่าตามเอกสารกติกาที่มี ไม่ใช้เป็นกำหนดการรายการใหม่ ขอบ `last round`, ตำแหน่งปุ่ม และเวลา pause ไม่เป็นระยะเวลารายการ เพิ่ม 6 ประโยคก่อน/หลังและหนึ่ง unit method

Flow ต่อสำหรับประโยคที่ยังไม่ครอบคลุม:''')
s=s.replace('Strong competition composition/content/new-question 728 cases', 'G6 เปลี่ยน production จาก G5b เฉพาะ competition_detail.py จึงตรวจซ้ำกลุ่มแข่งขัน/CS2 ทั้งหมดที่คัดจาก raw, normalized trace, source และ expected โดยอนุรักษ์ขอบกว้าง แล้วรวมกับผล G5 ของส่วนที่ bytecode/เส้นทางไม่ได้เปลี่ยน จำนวนตรวจซ้ำจริงดู final_G6_all_summary.json; ไม่อ้างว่าเป็น full sweep G6 ใหม่อีก 20,327 ข้อ\n+- Strong competition composition/content/new-question 728 cases')
s=s.replace('- คู่ clean/noisy 2,000', '- Runtime flags ตรงทั้งสองประเภท 471/500: layout TP240/FN0/FP0; repeat TP173/FN27/FP2 โดย action ยังตรง 500/500 เพราะ repeat เป็น warn/continue และบาง repeat miss มี layout block อยู่แล้ว อ่าน final_G5_runtime_guard500_interpretation.json แยกจากคำตอบ การจับซ้ำต่ำกว่า .55 และภาษาไทยหลายคำติดกันเป็นงานต่อ ไม่ลด threshold รวมเพื่อไล่คะแนน\n+- คู่ clean/noisy 2,000')
s=s.replace("f.write_text(s,encoding='utf-8',newline='\\n')", "replay=json.loads((r/'final_G6_all_summary.json').read_text(encoding='utf-8'))\ns += '\\nG6 ตรวจซ้ำกลุ่มที่อาจได้รับผล '+str(replay['reexecuted_requests'])+' requests แล้วเก็บผลรวมการครอบคลุมเดิม 20,327 requests พร้อม execution_provenance ต่อแถว ไม่ใช่การรัน 20,327 ข้อใหม่ใน G6\\n'\nf.write_text(s,encoding='utf-8',newline='\\n')")
with Path('r30_finish_flow_G6.py').open('x',encoding='utf-8') as out:out.write(s)
