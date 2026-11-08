import json,re,sys,hashlib
from pathlib import Path
from collections import Counter
root=Path(__file__).parent
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path((root/'r28_report_path.txt').read_text(encoding='utf-8').strip())
def rows(name):return [json.loads(x) for x in (report/name).read_text(encoding='utf-8').splitlines() if x.strip()]
full=rows('full_r28_A_details.jsonl');retests=rows('failed59_D_details.jsonl');ret={r['id']:r for r in retests}
assert len(full)==2000 and len(ret)==59
merged=[]
for r in full:
    updated=dict(ret.get(r['id'],r));updated['evidence_run']='failed59_D' if r['id'] in ret else 'full_r28_A';merged.append(updated)
with (report/'full_r28_corrected_merged_details_v2.jsonl').open('x',encoding='utf-8') as f:
    for r in merged:f.write(json.dumps(r,ensure_ascii=False)+'\n')
gold=[json.loads(x) for x in (project/'data/eval/competition_user_r24_2000_20261001.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
affected=[c['id'] for c in gold if c.get('expected_game_id')=='cs2' and re.search(r'\b(?:dispute|conflict)\s+resolution\b',c['question'],re.I)]
true_wrong=[r for r in full if 'wrong_facet_evidence' in r['failures']]
assert set(affected)=={r['id'] for r in true_wrong}
assert all(ret[r['id']]['passed'] for r in true_wrong)
manifest={'full_run':'full_r28_A','full_total':2000,'full_legacy_passed':1941,'targeted_retest':'failed59_D','targeted_total':59,'true_wrong_facet_fixed':12,'unchanged_legacy_presence_failures':47,'merged_legacy_passed':sum(r['passed'] for r in merged),'evidence_run_counts':dict(Counter(r['evidence_run'] for r in merged)),'final_scope':'full first pass plus targeted retest; not a second full execution under final code','affected_question_ids':affected,'changes_after_full_run':'mask dispute/conflict resolution collocation only for custom_display; source/Gold unchanged; time freeze in tests only'}
with (report/'full_merge_audit.json').open('x',encoding='utf-8') as f:json.dump(manifest,f,ensure_ascii=False,indent=2)
graded=json.loads((report/'full_r28_A_source_grade.json').read_text(encoding='utf-8'));gradeby={r['id']:r for r in graded['records']}
lines=['# ชุดใหญ่ 2,000: ข้อผิดจริงและข้อจำกัดตัวตรวจ','', '## การตีความผล','',
'รอบแรก legacy 1,941/2,000; source-grade 1,988/2,000. ข้อผิดจริง 12 ข้อเป็น CS2 dispute resolution. อีก 47 ข้อเป็น source-presence false failures. หลังแก้เฉพาะบริบท resolution ทดสอบ 59 ข้อเดิมซ้ำ: ข้อผิดจริงทั้ง 12 ผ่าน legacy; 47 ข้อยังไม่ผ่าน legacy แต่ source-grade ตรวจพบ clause สมบูรณ์. ไม่มีการเขียน Gold ใหม่.',
'','## สาเหตุข้อผิดจริง','',
'`custom_display` เดิมจับคำ Resolution โดยไม่มีบริบท จึงได้ source s45 (brightness/resolution/crosshair) และ confidence ที่ตั้งไว้ 0.97. ผล source เกมเดียวกันและ validation ผ่าน ไม่พอจะบอกว่าตอบประเด็นถูก. แก้โดยตัด collocation dispute/conflict resolution เฉพาะตอนตรวจแนวคิดหน้าจอ แล้วให้เส้นทาง protest_dispute เดิมเลือก s06/s58. ถ้ายังมี screen resolution ในประโยคเดียวกัน จะเก็บ display intent นั้นไว้. ชุดนี้ไม่ได้พิสูจน์การรวมข้อพิพาท+หน้าจอในคำตอบเดียว.',
'','## ข้อผิดจริงทั้ง 12 และคำตอบที่แก้แล้ว','']
for r in true_wrong:
    a=ret[r['id']]
    lines += [f"### {r['id']}",'', 'คำถาม: '+r['question'],'','คำตอบผิด:','','```text',r['answer'],'```','', 'ควรตอบการยื่นประท้วง: ภาษาไทย และผู้ยื่นกัปตัน/โค้ชภายใน 15 นาทีหลังแมตช์ โดยอ้าง rulebook ของ CS2. ขอบเขตข้อที่ตอบต้องอิง source s06/s58 ไม่ใช่ข้อปรับจอ.','','คำตอบหลังแก้:','','```text',a['answer'],'```','', 'Source IDs หลังแก้: '+', '.join(a['source_ids']),'', 'Legacy failures หลังแก้: '+str(a['failures']),'']
lines+=['## 47 ข้อที่ตัวตรวจเดิมจับ source ไม่พบ','',
'ตัวตรวจเดิมแบ่งด้วย newline และใช้ fragment ยาว/keyword จำกัด บางคำตอบอังกฤษที่สั้นหรือหลายข้อในย่อหน้าเดียวจึงไม่ถูกนับ. ตัวตรวจ r27 แยก atomic clauses และเอาเลข outline ออกโดยไม่ลบค่าจำนวน จากนั้นตรวจ literal complete-clause presence. เก็บ route/status/target/facet/time/validation gate เดิมทั้งหมด. สิ่งนี้ยืนยันว่ามีข้อความต้นฉบับอยู่ในคำตอบ; ไม่ยืนยันว่าประเด็นที่ผู้ถามต้องการครบทั้งหมด.', '', '| ID | แหล่ง clause ที่ตรวจพบ | Clause ตัวอย่าง |','|---|---|---|']
for r in full:
    if r['failures']==['answer_without_substantive_source_content']:
        g=gradeby[r['id']];assert g['source_grade_passed'] and g['complete_clause_matches']
        match=g['complete_clause_matches'][0]
        lines.append('| '+r['id']+' | '+match['source_id']+' | '+match['complete_clause'].replace('|','\\|').replace('\n',' ')+' |')
lines+=['','## ข้ามวันกับ fixture การจอง','',
'ระหว่างงานวันที่จริงเปลี่ยนเป็น 2 ตุลาคม. CSV fixture ตั้งไว้ 1 ตุลาคม แต่คำถามใช้ “วันนี้” จึงเกิด date mismatch และระบบปฏิเสธยืนยันสถานะอย่างถูกต้อง. Unit Candidate D ล้ม 3 test methods ด้านการจองเพราะ fixture-clock ไม่สอดคล้อง; ไม่มีเหตุให้แก้ runtime ให้ยอมรับวันที่ผิด. Snapshot tests เก็บก่อนแก้ แล้ว freeze now_bangkok เฉพาะ test ให้ตรง 1 ตุลาคม. Candidate E ผ่าน 153/153. ข้อ dispute unit อีก 1 ข้อแก้เลข source assertion จากที่เดา s54/s57 เป็น s58 หลังอ่านต้นฉบับจริง พร้อมตรวจเนื้อหา 15 minutes/captain/coach.',
'','## ขอบเขตผลรวม','',
'ไฟล์ full_r28_corrected_merged_details_v2.jsonl เป็นผลรอบแรก 1,941 ข้อที่ผ่าน กับรอบ retest 59 ข้อ ไม่ได้รันครบ 2,000 รอบสอง. Audit ตรวจว่าทั้ง 12 query ของ CS2 ที่มี collocation ตรงการแก้ถูก retest แล้ว. เก็บผลรอบแรกครบเพื่อเห็นข้อผิดก่อนแก้. ชุดใหม่ 280 และเว็บจริงมีเกณฑ์ครบทุก expected clauses แยกจาก source presence.',
'','การเชื่อม API สำเร็จ/ตอบ HTTP 200 ไม่ใช่การยืนยัน booked/free ของ booking จริง; smoke ด้าน booking ตรวจการเข้าถึงเส้นทางเท่านั้น. Oracle booked/free เป็น fixture อัตโนมัติ ส่วนข้อมูลจริงกับเจ้าของเก็บภายหลังตามคำสั่งผู้ใช้.']
with (report/'FULL_GROUND_TRUTH_ANALYSIS_TH.md').open('x',encoding='utf-8') as f:f.write('\n'.join(lines)+'\n')
print(json.dumps(manifest,ensure_ascii=False))
