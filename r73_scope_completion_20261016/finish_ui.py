from pathlib import Path
import json
B=Path(__file__).resolve().parent;H=B/'system/app/knowledge/common';p=H/'ui/owner.js'
text=p.read_text('utf8')
addition="""
// Routing metadata is optional and never supplies an answer or approval.
SIMPLE_FIELD_LABELS.query_profile='ช่วยแชทเลือกหัวข้อคำตอบ (กรอกเพิ่มได้)';
Object.assign(SUB_LABELS,{task:'ผู้ใช้ถามเรื่องลักษณะไหน',subjects:'เรื่องหรือสิ่งของที่คำตอบนี้ครอบคลุม',ownership:'เป็นของส่วนตัวหรือไม่',context:'ใช้กับบริการทั่วไปหรือการแข่งขัน'});
Object.assign(OPTION_LABELS,{permission:'ถามว่าใช้/นำมาได้ไหม',correction:'ถามวิธีแก้สิ่งที่ทำผิด',any:'ไม่จำกัดเจ้าของสิ่งของ',personal:'ของส่วนตัวของผู้ใช้',studio:'บริการทั่วไปของศูนย์',competition:'เฉพาะการแข่งขัน'});
for (const kind of ['faq','policy','procedure']) {
 FIELD_HELP[kind].query_profile={hint:'ไม่ต้องเขียนคำถามทุกแบบ เลือกชนิดคำถาม ใส่ชื่อเรื่องไทย/อังกฤษ เช่น คีย์บอร์ด / keyboard แล้วเลือกขอบเขตให้ตรง คำตอบจริงยังอ่านจากเนื้อหาด้านบน ถ้ายังไม่แน่ใจให้คงสถานะยังไม่ทราบ',example:{task:'permission',subjects:[{th:'อุปกรณ์ตัวอย่าง',en:'example equipment'}],ownership:'personal',context:'studio'}};
}
"""
idx=text.index('function valueEditor(')
text=text[:idx]+addition+'\n'+text[idx:];p.write_text(text,encoding='utf8')
p=H/'build_info.py';p.write_text(p.read_text('utf8').replace('common-r72-flow-repair','common-r73-question-scope'),encoding='utf8')
p=B/'system/web_chat/index.html';p.write_text(p.read_text('utf8').replace('R72','R73'),encoding='utf8')
for name in ['Start-New-Chat.ps1','Open-Data-Editor.ps1']:
 p=B/name;text=p.read_text('utf-8-sig').replace('8103','8105').replace('8104','8106').replace('new-common-chat-r72','new-common-chat-r73').replace("PSU_RUNTIME_VERSION = 'R72'","PSU_RUNTIME_VERSION = 'R73'")
 p.write_text(text,encoding='utf-8-sig')
for folder in ['runtime/logs','runtime/state']:(B/folder).mkdir(parents=True,exist_ok=True)
print('Added owner-friendly profile labels/examples and separate R73 launchers.')
