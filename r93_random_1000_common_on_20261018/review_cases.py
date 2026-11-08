"""Evidence-linked review of selected observed failures. No answer reruns."""
from pathlib import Path
import json
R=Path(__file__).resolve().parent
rows=[json.loads(x) for x in (R/'PER_REQUEST_ANALYSIS.jsonl').read_text('utf8').splitlines()]
notes=[
 ('I am planning a visit and would like to know: What kind of game is Animal Crossing: New Horizons',
  'คำเกริ่นทำให้ game task ที่มีชื่อชัดยังถูกปฏิเสธ',
  'ผู้ใช้ถามแนวเกม/ภาพรวม Animal Crossing ไม่ได้ขอเปลี่ยนหัวข้อ การจับชื่อเกมได้แต่ไม่ตอบสาระเป็น regression เชิงงานที่ต้องแก้ถ้า source summary/genre พร้อม',
  'task_interpretation._framing รับเฉพาะ framing บางรูป ขณะที่ entity_search.query_variants มีการตัด planning-a-visit อยู่ในอีกเส้นทางหนึ่ง การ normalize ที่ใช้เฉพาะ selector ไม่ได้ช่วยทุก named-target path; คำ and ในคำเกริ่นยังชนตัวตรวจ multi-task ได้',
  'ทำ normalization ของ discourse ร่วมก่อน task selection โดยเก็บ spans/raw input ไม่ลบ qualifiers/negation/ตัวเลข และแยก conversational and จาก substantive task coordination'),
 ('Could you please help me with this: Who operates PSU Esports Studio? Please use verified information',
  'คำถามผู้ดำเนินการศูนย์เลือกข้อมูลไม่สำเร็จ',
  'ควรเลือก operator/FAQ ผู้ดำเนินการที่ตรงกับศูนย์จากข้อมูลกลาง การขอ verified information เป็นข้อกำหนดหลักฐาน ไม่ใช่เหตุให้ถามชื่อเกมแทน',
  'ผลนี้ไม่มี usable final query plan และตอบว่า match ข้อมูลไม่ได้ ต้องไล่ named_scope และ candidate/guard ของคำถาม who/operator; ไม่สรุปว่าไม่มีข้อเท็จจริงเพียงเพราะตัวเลือกสุดท้ายว่าง',
  'เพิ่ม task profile ของ center/operator/directory ที่อ่าน fields/relations จาก snapshot ร่วมกับ wrapper normalization ไม่เพิ่ม alias เต็มประโยคต่อ record'),
 ('Can I bring my own food into the studio?',
  'กฎพื้นที่รับประทานกับสิทธิ์นำอาหารมาเป็นคนละขอบเขต',
  'คำตอบที่ให้บอก designated consumption areas ส่วนตัวตรวจคาดถ้อยคำ you may bring จึงไม่ผ่าน แต่คำตอบและ oracle ต้องตรวจว่าต้นฉบับยืนยันการนำอาหารส่วนตัวเข้ามาจริงหรือไม่',
  'มี source-backed answer เรื่อง food/drinks consumption แต่คำว่า own/bring เพิ่ม action/ownership ที่อาจไม่ครอบคลุม การมีหลักฐานเรื่องพื้นที่ไม่ยืนยัน permission ทุกกรณี',
  'รักษา action/object/ownership ใน TaskPlan; ถ้ามี policy ตรงให้อ้าง ถ้าไม่มีให้บอกเฉพาะส่วนที่ยืนยันไม่ได้ ไม่เพิ่ม you may bring เพื่อคะแนน'),
 ('Can visitors enter just to look around for free?',
  'คำถามเข้าชมฟรียังเลือก unsupported-policy outcome ไม่ตรง',
  'ถ้าไม่มีนโยบายยืนยันค่าเข้าชม ควรบอกว่า free visit ยังยืนยันไม่ได้พร้อมช่องทางถามเจ้าหน้าที่ ไม่ควรเอาค่าเล่นหรือสิทธิ์ผู้ใช้มาอนุมาน',
  'final no-match message กว้างกว่าประเด็นค่าเข้าชมฟรีที่ผู้ใช้ถาม ตัวตรวจคาด specific unconfirmed statement; เป็นทั้ง gap ด้าน task coverage และความเฉพาะเจาะจงของคำตอบ',
  'เพิ่ม need visit_only_fee ที่แยกจาก service price และไม่สร้างค่า 0 จากการไม่มี rate'),
 ('Under RoV tournamment rules, contrast restart requests before and after First Blood.',
  'RoV restart ก่อน/หลัง First Blood: ตรวจ proposition และคำแปล',
  'ต้องครอบคลุมสองเงื่อนไขครบ ได้แก่ช่วงก่อน First Blood/ไม่เกินเวลาที่กฎกำหนด และช่วงหลัง First Blood/เกินเวลา รวมข้อยกเว้นและสิ่งที่ต้องคงเดิมก่อน restart',
  'เลือก rule text ได้ แต่ complete-clause checker ระบุ missing clauses จากถ้อยคำที่คาด การไม่ตรงประโยคทั้งข้ออาจเป็น translation mismatch หรือขาด proposition จริง ต้องเทียบ source clauses/answer เต็ม ไม่สรุปว่าผิดทุกสาระจาก marker นี้อย่างเดียว',
  'ทำ per-proposition coverage: condition/time/actor/permission/exception; รักษา literal result เดิม และเพิ่ม equivalence review แยก ไม่ตัดข้อยกเว้นหรือใช้เล่มคนละรายการ'),
 ('API คืออะไร ตอบแบบเด็กปีหนึ่งเข้าใจได้',
  'โจทย์ general LLM เดิมอยู่นอกขอบเขตบริการที่ผู้ใช้กำหนด',
  'ผู้ใช้กำหนดให้บอตเน้นร้านเกม/ข้อมูลศูนย์ ไม่ต้องตอบความรู้ทั่วไปทุกเรื่อง คำถาม API ที่ไม่โยงบริการเป็นข้อที่ควรตรวจ scope ของ oracle ก่อนใช้เป็น production content failure',
  'corpus เก็บคำถามจาก benchmark ความรู้ทั่วไปเดิมไว้ด้วย จึงคงคะแนนดิบที่ไม่ผ่าน แต่ไม่ตีความว่าระบบต้องเปิด general generation กลับมาเพื่อให้ผ่าน',
  'แยก studio-service evaluation กับ retained legacy-general cohort ในรายงานรอบต่อไป โดยเก็บผลเดิม ไม่แก้ scope เพื่อไล่คะแนน'),
 ('จอสอบถามหน่อยครับ Sofa 2 seats คืออุปกรณ์อะไร',
  'การอธิบายอุปกรณ์ยังไม่ทั่วไปเท่าภาพรวมเกม',
  'ต้องหาว่าหมายถึง Sofa รายการใด แล้วอธิบาย device type/usage/specifications ที่มีหลักฐาน ส่วนคำเกริ่นพิมพ์ผิดไม่ควรเปลี่ยน subject เป็นจอโดยไม่มีหลักฐาน',
  'คืน safe clarification แทนสาระที่ถาม แสดงว่าการมี equipment-list contract ยังไม่ครอบคลุม equipment-explanation; ต้องอ่าน rejected plan เพื่อยืนยันว่าเสียที่ names, task หรือ coverage ไม่เดาจากคำตอบล้วน',
  'เพิ่ม reusable explain-entity task ต่อ schema kind และตรวจ mixed-target ambiguity พร้อม recovery ที่ไม่จับคำในคำเกริ่นเป็นอุปกรณ์'),
 ('Who are the studio members? Could you check this for me?',
  'รายชื่อภาษาไทยในคำตอบอังกฤษกับเกณฑ์ English localization',
  'รายชื่อเฉพาะอาจคงอักษรไทยได้ตามข้อมูลต้นฉบับ ขณะที่ role/team ที่เป็น prose ควรเป็นอังกฤษ ต้องแยกชื่อเฉพาะออกจากการแปลสาระไม่ครบ',
  'มีรายชื่อและ roles ในคำตอบ แต่ตัวตรวจคาด marker English localization การขาด marker ไม่พิสูจน์ว่าคน/หน้าที่ผิด และไม่ควรแต่งชื่อโรมันใหม่โดยไม่มีต้นฉบับ',
  'ตรวจ actual localized values และ translation status แยกจาก proper-name flags; ประเมินสาระ/ขอบเขตสาธารณะของ directory และ wording caveat คนละเงื่อนไข'),
 ('มีอะไรบ้าง',
  'คำถามกว้างที่ตอบ clarification แล้วแต่ไม่ตรง wording oracle',
  'เมื่อไม่มีประวัติ/subject ควรถามเลือกหัวข้อของศูนย์พร้อมตัวอย่างที่เข้าใจง่าย การตอบ clarification จึงไม่ใช่ failure ด้าน facts โดยอัตโนมัติ',
  'ตัวตรวจต้องการข้อความตัวอย่างเฉพาะ เช่น คำถามนี้ยังกว้างเกินไป และ มีเกมอะไรบ้าง คำตอบปัจจุบันขอชื่อเกม/อุปกรณ์/หัวข้อด้วยอีกสำนวนจึง fail literal',
  'ปรับ clarification UX ให้เสนอ task options ตามขอบเขต และตรวจ semantic outcome แยกจาก required string โดยยังเก็บ literal score เดิม'),
 ('นักศึกษาต่างมหาลัย เล่น VR 1 ชั่วโมง 30 นาที เสียกี่บาท',
  'ราคา VR: แยก validity จากกลุ่มผู้ใช้และระยะเวลา',
  'ถ้าราคาใน source หมดอายุ ณ reference clock ต้องไม่ยืนยันยอดปัจจุบัน แต่ยังต้องระบุให้ถูกว่ากำลังตรวจกลุ่มและระยะเวลาใด',
  'ผลแสดงหลาย rate ที่หมดอายุก่อน 1 เม.ย. 2026 และไม่มี marker บาท/ฟรีที่ oracle ต้องการ เป็นเหตุด้าน temporal data/oracle ส่วนหนึ่ง แต่ไม่ได้รับรองว่า audience/duration bindings ถูกแล้ว ต้องตรวจแยก',
  'คง validity guard และขอ source ราคาปัจจุบันตามงานข้อมูล; ตรวจ typed audience/session/duration contracts ด้วย isolated current fixtures โดยไม่เอาราคาเก่ามาคูณให้ผ่าน')
]
lines=['# วิเคราะห์ตัวอย่างจากผลสุ่ม R93 — อ่านผลที่บันทึก ไม่ส่งคำถามซ้ำ','',
'ตัวอย่างต่อไปนี้แยกสิ่งที่ trace ยืนยันได้ออกจากข้อที่ต้องตรวจความหมาย/ต้นฉบับเพิ่ม ไม่จัดทุก literal failure เป็นคำตอบผิดทางธุรกิจ และไม่ยกเลิกผลคะแนนเดิม','']
for i,(question,title,intended,cause,fix) in enumerate(notes,1):
 row=next((r for r in rows if r['question']==question),None)
 if row is None:continue
 plan=row.get('query_plan') or (row.get('rejected_candidate') or {}).get('query_plan') or {}
 failures=[e for f in row['failures'] for e in f['text_failures']]
 lines += [f'## C{i:02} — {title}','',f"Request key: `{row['key']}`",'', '**คำถาม**','',question,'',
  '**คำตอบจริงที่เก็บไว้ (ตัดเฉพาะการแสดงตัวอย่าง; ฉบับเต็มอยู่ PER_REQUEST_ANALYSIS.jsonl)**','', '```text',row['answer'][:1400],'```','',
  '**สิ่งที่ควรพิจารณาว่าต้องตอบอะไร**','',intended,'','**เหตุที่พบ/ข้อจำกัดในการวินิจฉัย**','',cause,'',
  '**สัญญาณและแผนที่เลือกจริง**','', '```json',json.dumps({'signals':row['signals'],'mode':row['mode'],'method':plan.get('method'),'record_ids':plan.get('record_ids'),'fields':plan.get('requested_fields'),'unresolved':plan.get('unresolved_clauses'),'text_failures':failures[:3]},ensure_ascii=False,indent=2),'```','',
  '**แนวแก้ต่อไป**','',fix,'']
lines += ['## ลำดับที่ควรแก้ต่อจากหลักฐานชุดนี้','',
'1. Discourse/wrapper normalization ที่ใช้ร่วมทุก named/unnamed path โดยเก็บ protected constraints',
'2. ขยาย explain/overview/eligibility task contracts ไปอุปกรณ์ ศูนย์ และ policy พร้อม per-need outcomes',
'3. Semantic binding/guard ของ paraphrases และ qualifiers โดยไม่เปิดรับทุก JSON จาก LLM',
'4. Proposition coverage ของ rules และการแยก exact-clause mismatch จากการขาดเงื่อนไขจริง',
'5. จัด data readiness/validity/translation ตาม field ที่บล็อกงานจริง และทบทวน oracle scopes/markers อย่างโปร่งใส','',
'รอบนี้เป็นการทดสอบและวิเคราะห์ ไม่เปลี่ยน production code/data ระหว่างวัดผล แผนแก้ข้างต้นยังไม่ใช่สิ่งที่แก้เสร็จแล้ว','']
with (R/'CASE_REVIEW_TH.md').open('x',encoding='utf8') as f:f.write('\n'.join(lines))
print('Evidence-linked case review saved')
