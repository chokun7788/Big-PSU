"""Materialize GPT-read intent reviews of the 36 paired difference questions."""
import json,pathlib,collections
R=pathlib.Path(__file__).resolve().parent
notes='''
อุปกรณ์นี้คืออะไร|ตอบชื่อ/ชนิด/สเปก แต่ยังไม่อธิบายหน้าที่ด้วยภาษาธรรมดา|ตอบบางส่วน|field selection และ renderer เป็นสาเหตุที่เป็นไปได้ ต้องดู trace ก่อนแก้
เกมเล่นได้ที่ไหน|ระบบไม่พร้อม จึงไม่ตอบเป้าหมาย|ตรวจต่อใน log|ข้อความปลายทางไม่แยก verifier rejection กับ transport failure
ราคา VR ระยะเวลาซ้ำ|ถามกลับอย่างมีเหตุผล ไม่ควรเดาว่าหนึ่งหรือสองรอบ|การชี้แจงเหมาะสม|duration_scope.py/plan_contract.py มี guard ระยะเวลาซ้ำโดยตรง
ราคาและวิธีจอง|ตอบราคา แต่ขั้นตอนจองที่สะกดผิดยังหาย|คำตอบไม่ครบ|อาจสูญเสีย predicate จากคำสะกดผิดหรือ task scope; สถานะ duration ยังขัดกับราคาที่แสดง ต้องตรวจ receipt
วิธีใช้จอย Monster Hunter Rise|เลือก PS5 โดยผู้ถามไม่ระบุแพลตฟอร์ม; source มีบริการ Nintendo และ control PS5 ซึ่งไม่ใช่หลักฐานว่าศูนย์มีเกม PS5|scope ยังไม่ยืนยัน|ต้องแยก control source กับ offered-service relation
กินอาหารระหว่างเล่น PC ได้ไหม|ตอบนโยบายพื้นที่กินพร้อมข้อจำกัด แทนการไปตอบเครื่องว่างแบบรุ่นเก่า|ตรงหัวข้อมากขึ้น แต่สิทธิ์ปัจจุบันยังไม่ยืนยัน|แยก policy predicate ออกจาก live availability; ไม่ลบ validity caveat
วิธีใช้หูฟัง Pulse Elite|ตอบ zone/จำนวน แทน usage ที่มีอยู่ใน source|ตอบผิดส่วน|equipment_definition_card ใน meaning_reader.py มีเส้นทาง broad fields; ต้องยืนยันเส้นทางจริงจาก log ของข้อนี้
Cockpit สองเครื่องเล่นได้กี่คน|ไม่ตอบ capacity; รุ่นเก่าพูด single-player ซึ่งไม่เท่ากับจำนวนคนต่อเครื่อง/รวมสองเครื่อง|ยังตัดสินจำนวนไม่ได้|ต้องแยก resource capacity กับ game player count
ความหมาย mechanical แบบสั้น|ใหม่ระงับคำตอบ เก่าเป็นข้อมูลคีย์บอร์ดทั่วไป ไม่ใช่คำนิยาม mechanical|ข้อมูลไม่พอ ไม่ใช่พิสูจน์ว่าใหม่ผิด|meaning_reader.py ระงับ subtype definition โดยตรง
สรุปกติกา CS2|ตอบเพียงชื่อแผนที่ ไม่ครบใจความกติกา แม้แจ้งข้อจำกัด|ตอบบางส่วน|operation summary/overview และ rule dependency coverage ต้องตรวจร่วม
Nintendo มีอะไรบ้าง|เลือกตอบรายชื่อเกม อาจตรงหากหมายถึงเกม แต่คำถามอาจหมายถึงเครื่อง/อุปกรณ์|เจตนากำกวม|ไม่ควรให้คะแนน semantic ว่าถูกจากรายชื่อเกมอย่างเดียว
ความหมาย mechanical แบบสั้น|ใหม่ไม่ยืนยัน เก่าอธิบาย generic keyboard และยาวเกินคำขอ|ข้อมูลไม่พอ|ไม่ยก generic usage เป็น subtype definition
ปุ่ม Naruto ใช้ยังไง|แสดงตารางปุ่ม แต่แพลตฟอร์ม/เวอร์ชัน/ความตรงต้นทางยังต้องตรวจทุก binding|รูปคำตอบตรงงาน แต่ข้อเท็จจริงยังไม่รับรองครบ|controller platform/preset/version scope
ราคา PS5 สองชั่วโมง|ใหม่ไม่ตอบ เก่าให้ราคา 300 บาท; ยังใช้ราคาเก่าเป็นคำตอบถูกไม่ได้ก่อนเช็กช่วงมีผลและขอบเขตคน|ต้องตรวจ source/receipt|ราคาแยก service/audience/duration/person bounds/confirmation
PC Zone รอบละกี่นาที|ใหม่ระบบไม่พร้อม; เก่าแสดงรายชื่อเกมซึ่งไม่ตอบระยะเวลารอบ|ทั้งสองยังไม่ตอบโจทย์|ต้องอ่าน session duration จาก service ไม่ใช่ game catalog
ตารางจองรายสัปดาห์|ใหม่ตอบวันและช่วงจองพร้อม caveat; เก่าตอบขั้นตอนจอง|ตรงเจตนามากขึ้น|ยังไม่พิสูจน์ current applicability หรือ live availability
เวลา session บ่าย|ใหม่และเก่าระบุเวลาเดียวกัน แต่ใหม่แยกวัน/maintenance; literal อาจแพ้เครื่องหมายขีด|ความต่างรูปแบบไม่ใช่หลักฐานคำตอบผิด|ตรวจ play-service scope และ effective interval
วิธีใช้พวงมาลัย Logitech|ใหม่ระบบไม่พร้อม; ข้อมูลรุ่นเก่าที่เห็นเน้นชนิด/ที่ตั้ง/จำนวน ยังไม่พอเป็นวิธีใช้|ต้องตรวจ log และ usage|อย่าปิด failure ด้วยการแสดง card กว้าง
วันและเวลาจอง|ใหม่ตอบ recorded booking periods เก่าตีความไม่พร้อม|ตรงรูปงานมากขึ้น|แยก booking windows/building/play/live และระบุช่วงมีผล
ใครดำเนินงานศูนย์|ใหม่ unknown; FAQ เก่าระบุ College แต่ binding/authority ยังไม่ชัดและ typed center ระบุ PSU|ยังตัดสินข้อเท็จจริงไม่ได้|ห้ามผูก FAQ กับศูนย์ด้วย regex เพียงอย่างเดียว
ปุ่ม Right Stick ของเกมฉบับ Remastered|ใหม่ตอบมุมกล้องพร้อมเตือนแหล่งรอง แต่หัวเรื่องเป็น base game|ตรง action แต่ edition scope ยังต้องตรวจ|alias ของ edition ไม่ใช่หลักฐานว่า binding ใช้ร่วมกัน
ปุ่ม Tekken และราคา PC|ใหม่ยืนยันไม่ได้ซ้ำสองช่วง จึงไม่ตอบทั้งสอง need; เก่าตอบแต่ราคา|คำตอบไม่ครบทั้งสองรุ่น|task split/slot ownership และ guard คำสะกดผิดก่อน renderer
PUBG ใช้จอย|ใหม่ตอบปุ่มคีย์บอร์ด PC ซึ่งมี source จริงแต่ไม่ใช่จอย|อุปกรณ์ควบคุมผิดเจตนา|input device ต้องเป็น constraint ที่ reader/verifier ตรวจ ไม่ใช่เดาตาม control set ที่มี
Pulse Elite คืออะไร|ใหม่ระบบไม่พร้อม; เก่ามีแต่ชื่อก็ยังไม่ใช่คำอธิบายครบ|ต้องตรวจ log|type/name/usage คนละคำตอบตามคำถาม
ใครดำเนินงานศูนย์|FAQ กับ center ยังมี scope/authority ที่แก้ไม่ได้ด้วยคำตรง|ยังไม่ยืนยัน|คง unknown จนมี relation และ authority รองรับ
ราคา PS5 สองชั่วโมง|เช่นเดียวกับกลุ่มราคา PS5 ไม่สรุปว่า 300 บาทถูกสำหรับวันปัจจุบัน|ต้องตรวจ source/receipt|ตรวจ confirmation/effective interval และ raw person bounds
ราคา VR ระยะเวลาซ้ำ|ถามยืนยันว่าหนึ่งช่วงหรือหลายรอบเป็นพฤติกรรมมีเหตุผล|การชี้แจงเหมาะสม|ห้าม normalize จำนวน/เวลาโดยเงียบ
ใครดำเนินงานศูนย์|ยังไม่สามารถตัดสินจาก FAQ ตัวเดียว|ยังไม่ยืนยัน|ต้องมี center binding และ authority ที่แยก institution/operator
PUBG คือเกมอะไร|ใหม่ให้คำอธิบายแนวเอาชีวิตรอดซึ่งตอบชนิดคำถามมากกว่า error เก่า|ตรงเจตนาในระดับข้อความ|ยังต้องเทียบ claim กับ summary/source/edition ก่อนรับรอง factual correctness เต็ม
วิธีใช้ Racezone Cockpit|ใหม่มีคำอธิบายให้นั่งและใช้พวงมาลัย/คันเร่ง/เบรก ตรงการใช้งานมากกว่า error เก่า|ตรงเจตนาเบื้องต้น|ยังไม่พิสูจน์ขั้นตอนเปิดเครื่องหรือความปลอดภัยที่ไม่ได้มีใน source
TV 86 นิ้วคืออะไร|ใหม่ระบบไม่พร้อม เก่าเพียงชื่อก็ยังไม่อธิบายชนิดและหน้าที่|ต้องตรวจ log|ไม่ควรถือ name echo เป็นคำจำกัดความ
ปุ่ม Mario Odyssey บน Switch|ใหม่แสดงปุ่มตาม platform ที่ผู้ใช้ระบุ|ตรงงานเบื้องต้น|ต้องตรวจ binding/action ทั้งตารางและ source version ก่อนบอกถูกทุกปุ่ม
เวลา session บ่าย|ความต่าง hyphen/en-dash และรายละเอียดวันยังไม่ใช่ semantic regression|ตรวจ scope ต่อ|อย่าแก้ให้ผ่าน literal โดยลบ maintenance/validity
ROV มีปุ่มให้เล่นที่ศูนย์ไหม|อาจถามว่ามีเกมหรือขอผังปุ่ม; ทั้งสองควรถามให้ชัดโดยรักษาชื่อ ROV ที่ระบุแล้ว|การชี้แจงยังไม่เฉพาะจุด|แยก offered-game predicate ออกจาก control predicate
เวลา session บ่าย|ตอบเวลาและข้อจำกัดสอดคล้องชนิดคำถาม|ตรวจ scope ต่อ|แยกเวลาที่บันทึกกับสิทธิ์เข้าใช้จริง
Gaming Keyboard คืออะไร|ใหม่ระบบไม่พร้อม; เก่าตอบแค่ชื่อก็ไม่เพียงพอ|ต้องตรวจ log|trace first ไม่สรุปว่า source ไม่มีจากข้อความ unavailable
'''.strip().splitlines()
seen={}
for x in map(json.loads,(R/'SEMANTIC_REVIEW_INPUT.jsonl').open(encoding='utf8')):seen.setdefault(x['key'],x)
assert len(seen)==len(notes)==36
rows=[];md=['# วิเคราะห์ผลและแผนปรับ Flow รุ่นผสม','',
'ตรวจข้อความคำถาม/คำตอบของกลุ่มที่ literal ต่างกันครบ36คำถาม จาก115เกณฑ์ที่เปลี่ยน ไม่ใช่ตรวจ semantic ครบ1056คำถาม การอ้างสาเหตุแยกสิ่งที่เห็นจาก output กับสมมติฐานที่ต้องตรวจ trace ต่อ ไม่ใช้ R134 เป็นคำตอบถูกอัตโนมัติ','',
'## ภาพรวม1056คำขอ','',
'common_partial_answer 414, common_answer 279, common_unavailable 198, common_unconfirmed 98, common_clarification 45, greeting13, migrated clarification4, out-of-scope3, live unavailable1, common_list1. ทั้งหมดเป็นสถานะระบบ ไม่ใช่คะแนนถูก/ผิด; partial ไม่ได้แปลว่าผิด และ answer ไม่ได้แปลว่าถูก','',
'## ตรวจรายข้อ']
for i,(x,note) in enumerate(zip(seen.values(),notes),1):
 intent,problem,verdict,cause=note.split('|');row={**x,'intent':intent,'finding':problem,'assessment':verdict,'cause_or_hypothesis':cause,'semantic_score':None};rows.append(row)
 md.extend([f'### {i}. {x["question"]}',f'- Key: `{x["key"]}`',f'- เจตนา: {intent}',f'- ผลวินิจฉัย: {verdict}',f'- ปัญหา/ข้อจำกัด: {problem}',f'- สาเหตุหรือสมมติฐาน: {cause}','', '**คำตอบรุ่นผสมจริง**','',x['new'],'','**คำตอบ R134 ที่บันทึกไว้**','',x['old'],''])
md.extend(['## ลำดับแผนแก้และเกณฑ์ผ่าน','',
'1. **P0 แกะ198 unavailable ก่อน:** join request/session กับ decision_artifact; แยก fatal source receipt, planner/model/protocol, timeout และ exception ตาม logจริง ตัวเลขอาจซ้อนกัน ต้องนับ requestไม่ใช่จำนวน reason. แก้สาเหตุร่วมที่กระทบหลายคำถามก่อน ไม่ลด verifier เพื่อให้ส่งคำตอบได้เฉยๆ. ผ่านเมื่อกรณีที่มี source เหมาะสมส่งคำตอบได้ และ wrong-target/forgery ยังคงถูกปฏิเสธ','',
'2. **P1 field และ operation:** how-to-use→usage/procedure; what-is→คำอธิบายที่มี source ไม่ใช่ name echo; session minutes→service duration; summary→หัวข้อกติกาที่แสดงความครบ/ส่วนขาด ไม่ใช่แผนที่หัวข้อเดียว. ตรวจทั้งไทย/อังกฤษและ owner edit/withdraw เฉพาะfieldsที่เปลี่ยน','',
'3. **P1 input device/platform/edition:** จอยต้องไม่ตอบ keyboard; unspecified platform มีหลายตัวเลือกให้ถามเพิ่ม; อย่าใช้ control set เป็น offered-service proof; Remastered ต้องรักษาedition. เพิ่ม direct forced-verifier wrong device/platform และ positive ที่ source รองรับจริง','',
'4. **P1 compound/typo:** เก็บราคา+วิธีจอง และปุ่ม+ราคาเป็นคนละneed; normalizeคำสะกดผิดเฉพาะpredicateพร้อมraw span ไม่แก้ชื่อเกม จำนวน หรือเวลา. ยอด/ระยะเวลาที่ใช้ในคำตอบต้องตรง receipts และ coverage notice; ไม่มีข้อความคำถาม/unknownซ้ำทั้งก้อน','',
'5. **P2 ราคา PS5:** ตรวจ source scopes/confirmation/effective dates/rawbounds จาก frozen snapshot และ traces ก่อนเลือก fix. ถ้าข้อมูลไม่พอให้บอกส่วนที่ขาด; ถ้าข้อมูลพอและguardผิด ให้แก้และตรวจ positive, alternative durations, same-platform-other-service, forged amount/person count. ไม่ hardcode300บาทหรือยก R134 เป็นgold','',
'6. **P2 authority/data gaps:** operator/definitions/current hours ต้องมี source ที่ผูกเป้าหมายตรง ข้อมูลไม่พอให้คง unknown และจัดรายการข้อมูลที่ต้องยืนยัน; ไม่แก้ข้อเท็จจริงเพื่อไล่คะแนน','',
'7. **การวัด:** ตรึง expected intent/required claims/prohibited claims/acceptable clarification/source IDs ก่อนรัน; ตรวจ focused positives/negatives+affected regressionหนึ่งรอบต่อกลุ่ม; ใช้เหมือนเดิมได้เฉพาะdependenciesตรง. สร้าง targeted review set จาก36ข้อพร้อมคำถามใหม่ที่ไม่ใช่คำแปรเดิมและหมวดเบาบาง; ไม่ปรับ gold ตามคำตอบที่เพิ่งเห็น. ก่อนกล่าวถึงคะแนนsemanticต้องระบุจำนวนที่ตรวจได้และunassessed หลีกเลี่ยงเอา36ข้อที่เลือกเพราะผลต่างไปแทน1056ทั้งหมด','',
'8. **รอบรวมถัดไป:** รัน1056เดิมอีกเมื่อรวมfixที่มีผลจริงและผ่านcritical controls เก็บ frozen code/source/model/time/config/manifestก่อนรัน แยก literal, intent coverage, claim support, correct clarification และ operational failures; ห้าม rerun/regrade R132 ห้ามแก้ผลเดิม','',
'## การป้องกันการวนและหลักฐาน','',
'ต่อหนึ่งกลุ่มต้องมีปัญหาที่พิสูจน์แล้ว → patch → before/after → positive+negative → regressionที่ได้รับผลกระทบ → disposition. แนวทางเดิมล้มสองรอบให้เปลี่ยนวิธีหรือถอน ไม่เพิ่มเพียงnegative case ไม่รัน5%ทุกครั้งที่แก้หนึ่งจุด. พัฒนาสำเนารอบใหม่ เก็บ evaluation/FROZEN_CODE และrawเดิมไว้ ไม่แก้ owner/live/frozen และไม่หยุด protected model','',
'รายงานนี้เป็นแผนหลังวิเคราะห์ ยังไม่ได้แก้runtimeตามแผนนี้ ยังไม่มีคะแนนsemanticทั้งหมด และยังไม่ยืนยันความถูกต้องปุ่มทุกแถว/ราคา/สิทธิ์ปัจจุบัน'])
(R/'DETAILED_INTENT_FAILURE_ANALYSIS_TH.md').write_text('\n'.join(md),encoding='utf8')
(R/'GPT_REVIEW_36.json').write_text(json.dumps({'scope':'36 changed questions, GPT textual intent review; partial source checks; not full semantic accuracy','rows':rows},ensure_ascii=False,indent=2),encoding='utf8')
print('wrote36 detailed reviews and grouped repair plan')
