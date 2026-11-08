from pathlib import Path
import json, re
HERE=Path(__file__).resolve().parent
archive=json.loads((HERE/'archive_verification_r38_5.json').read_text(encoding='utf-8'))
latest=max(HERE.glob('flow_results_20261005_*.json'),key=lambda p:p.stat().st_mtime)
records=json.loads(latest.read_text(encoding='utf-8'))
print('Latest functional recorded outputs:',len(records),latest.name)

flow=(HERE/'FLOW_IMPLEMENTED_R38.md').read_text(encoding='utf-8')
flow=flow.replace('r38.3','r38.5').replace('IMPLEMENTATION_AND_TEST_REPORT_TH.md','IMPLEMENTATION_AND_TEST_REPORT_R38_5_TH.md')
flow=flow.replace('Functional suite ใหม่ 21 methods ผ่าน','Functional suite ใหม่ฉบับสุดท้าย 23 methods ผ่าน')
flow=flow.replace('ชุดสุดท้าย r38.5 8/8 จาก 12 requests ผ่าน','ชุดสุดท้าย r38.5 10/10 จาก 15 requests ผ่าน; ไฟล์แตก ZIP ตรวจ 10/10 เคสผ่านทั้ง pipeline')
flow=flow.replace('r38.5 ที่ 8096','r38.5 ที่ 8093')
flow=flow.replace('explicit user และ metadata', 'explicit user และ metadata')
flow=flow.replace('## 4. สถานะตรวจตาม C01–C32', '''พบเพิ่มจากการแตก ZIP และเว็บรอบท้าย:

- ประโยคราคาใหม่ที่ยังอยู่ในบริบทราคาเดิม เช่น “I'd like the cockpit rate instead” ต้องคงกลุ่มผู้ใช้ที่ไม่ได้เปลี่ยน แม้ไม่มีคำว่า and/what about; คำสั่ง reset/new question ออกจากการสืบทอดกลุ่มได้ และค่าที่ผู้ใช้ระบุใหม่มีสิทธิ์แทนค่าเดิม
- `every/each section/clause/rule` เป็น full scope โดยผูกกับคำขอกติกา ไม่ตีความ “Every PC is available” เป็นกติกาฉบับเต็ม
- คำว่า rulebook/tournament/competition ต้องส่งให้ตัวจัดหมวดกติกาเดิมก่อน all-scope clarification ของราคา
- การตรวจตัวตอบแยกส่วนยังไม่พอ: เพิ่ม assertion ผ่าน pipeline และเว็บสำหรับเคสที่เคยถูกดักก่อนถึงตัวตอบ

## 4. สถานะตรวจตาม C01–C32''')
with (HERE/'FLOW_IMPLEMENTED_R38_5.md').open('x',encoding='utf-8') as f:f.write(flow)

report=(HERE/'IMPLEMENTATION_AND_TEST_REPORT_TH.md').read_text(encoding='utf-8')
report=report.replace('r38.3','r38.5').replace('release_r38_3','release_r38_5').replace('r38_3.zip','r38_5.zip')
report=report.replace('FLOW_IMPLEMENTED_R38.md','FLOW_IMPLEMENTED_R38_5.md').replace('WEB_R38_3_VERIFIED.png','WEB_R38_5_VERIFIED.png')
report=report.replace('http://127.0.0.1:8096/','http://127.0.0.1:8093/').replace('เว็บ 8096','เว็บ 8093').replace('เป็น 8096','เป็น 8093')
report=report.replace('archive_verification.json','archive_verification_r38_5.json').replace('after_manifest.json','after_manifest_r38_5.json').replace('launcher_verification_r38_3.json','launcher_verification_r38_5.json')
report=report.replace('7,298,673 bytes',f"{archive['bytes']:,} bytes").replace('ed570d35e9ee9cb1b301e420462f3a15e5bf9565e751cf75ca992de03c6c917d',archive['sha256'])
report=report.replace('21 test methods ผ่าน มีหลาย subcases และ recorded outputs 75 รายการในชุดที่เก็บ: 47 pipeline answers และ 28 หน้ากติกา นี่เป็นชุดตรวจแบบมี expected values ไม่ใช่ 75 คำถามสุ่มอิสระ',f"ฉบับสุดท้าย 23 test methods ผ่าน เพิ่มสอง methods หลังพบปัญหาจากคำถามเพิ่มเติม มี {len(records)} recorded outputs ในรอบล่าสุด ส่วนชุดแรก 21 methods เก็บ 75 outputs (47 pipeline answers และ 28 หน้ากติกา) จำนวน outputs ไม่ใช่จำนวนคำถามสุ่มอิสระ")
report=report.replace('### 4.2 Regression ที่เลือก','### 4.2 Regression ที่เลือก\n\nตรวจซ้ำครบชุด 70 tests ในรอบ r38.4 ก่อนแก้ keyword rulebook/tournament ขั้นท้าย; r38.5 ตรวจ functional 23 methods รวม pipeline ของรูปคำถามใหม่นี้และเว็บซ้ำ ไม่กล่าวว่าได้รันทุก regression ของโปรเจกต์หลังทุกการแก้')
start=report.index('| รอบ | พบ | แก้และตรวจซ้ำ |')
end=report.index('\nจำนวน checks กับ requests',start)
report=report[:start]+'''| รอบ | พบ | แก้และตรวจซ้ำ |
|---|---|---|
| Functional แรก | all phrase ผิดบริการ, group/negation, หลาย task และ format/หน่วย PC | จัดลำดับ all/filter, per-target duration/capacity และ task outcomes; 21 methods ผ่าน |
| เว็บ source 8093 | 25/28 checks; ต่อกติกา TH/EN ไม่ได้และ general EN rejected | แก้ rendered metadata/ack ordering และ complete sentence contract |
| เว็บ source 8094 | 28/28 จาก 32 requests | โมเดลจริง/negation/general/continuation ผ่าน |
| แพ็กเกจ r38.2 8095 | 30/30 จาก 36 requests | ตรวจ Auto/retry; พบตัวเปิดอาจใช้ชุดเก่า |
| แพ็กเกจ r38.3 8096 | 8/8 จาก 12 requests | identity/version และ reuse ผ่าน |
| แตก ZIP r38.3 | คำถามเพิ่มผ่าน 6/8: สำนวนราคาใหม่ทิ้งกลุ่ม external และ every section ไม่เปิด full scope | คงกลุ่มเมื่อไม่ได้เปลี่ยน และเพิ่ม each/every scope; เก็บผลพลาดเดิม |
| r38.4 แยกส่วน/เว็บ | ไฟล์แตก ZIP ผ่าน 10/10 แต่เว็บผ่าน 9/10: rulebook ถูก typed all-scope ดักก่อนถึงตัวตอบ | เพิ่ม domain cues rulebook/tournament/competition และ assertion ผ่าน pipeline |
| r38.5 สุดท้าย | functional 23/23, ไฟล์แตก ZIP 10/10 ผ่านทั้ง pipeline, เว็บ 10/10 จาก 15 requests | สองสาเหตุแก้ครบเส้นทางที่ตรวจ; hash/CRC/launcher/web ผ่าน |
''' +report[end:]
report=report.replace('- `final_package_summary_221253.json`: 8/8 checks, 12 requests บน r38.5','- `final_package_summary_224000.json`: 10/10 checks, 15 requests บน r38.5\n- `extracted_holdout_results.json`: ผลก่อนแก้ 6/8; `extracted_holdout_results_r38_5.json`: หลังแก้ 10/10 และตรวจ rule scope ผ่าน pipeline ด้วย ไม่เรียกชุดที่แก้แล้วว่าเป็น holdout อิสระอีกครั้ง')
report=report.replace('หยุดเว็บทดสอบที่ผมเปิดไว้ 8093–8095 แล้ว คง r38.5 สำหรับลองใช้และไม่หยุดชุดเดิมของผู้ใช้ 8090–8092','หยุดเว็บทดสอบ source 8093–8095 และแพ็กเกจรอบก่อน r38.3/r38.4 แล้ว ปัจจุบัน 8093 เป็น r38.5 สำหรับลองใช้ ชุดเดิมของผู้ใช้ 8090–8092 ไม่ถูกหยุด')
report=report.replace('SHA256:', '''การแตก ZIP ในโฟลเดอร์หลักฐานที่ซ้อนลึกครั้งแรกชนข้อจำกัดความยาว path ของ Windows จึงตรวจใหม่ใน path สั้น `C:\\Users\\Chokhun\\Documents\\Codex\\psu_r38_5_archive_check_20261005` และผ่าน ไม่ลบโฟลเดอร์แตกบางส่วนเดิม หากย้ายแพ็กเกจควรแตกในโฟลเดอร์ที่ path สั้นเพื่อหลีกเลี่ยงข้อจำกัดนี้

SHA256:''')
report=report.replace('### คะแนนไม่ได้แปลว่าคำตอบถูก 98%', '''### ปัญหาที่พบจากคำถามเพิ่มเติมและตรวจทั้งเส้นทาง

“I'd like the cockpit rate instead” มี target ถูกแล้ว แต่เดิมถูกสร้างเป็น new price task และไม่ได้รับ group จากคำถาม external เพราะระบบยอมสืบทอด filter เฉพาะประโยคที่มี and/what about ทำให้แสดง PSU ฟรีด้วย แก้ให้คง eligibility ที่ยังไม่ได้เปลี่ยนในบริบทราคาเดิม โดยคำระบุกลุ่มใหม่หรือ reset แทน/ล้างได้

“Please show every section of the CS2 tournament rulebook” มีสองสาเหตุ: full-scope reader ไม่รับ every section และ typed price resolver ไม่รู้ว่า rulebook/tournament เป็นอีกหมวด จึงดักไปถาม “All of which topic…” ก่อนถึงตัวตอบ แม้แก้สาเหตุแรกแล้ว component test ผ่าน แต่เว็บยังผิด จึงแก้สาเหตุที่สองและเพิ่ม pipeline assertion ก่อนออก r38.5

### คะแนนไม่ได้แปลว่าคำตอบถูก 98%''')
with (HERE/'IMPLEMENTATION_AND_TEST_REPORT_R38_5_TH.md').open('x',encoding='utf-8') as f:f.write(report)

# Resolve every linked local file in the final reports, without changing originals.
for path in [HERE/'FLOW_IMPLEMENTED_R38_5.md',HERE/'IMPLEMENTATION_AND_TEST_REPORT_R38_5_TH.md']:
    for target in re.findall(r'\]\((C:/[^)]+)\)',path.read_text(encoding='utf-8')):
        assert Path(target).exists(), target
print('Final reports written and local links verified.')
