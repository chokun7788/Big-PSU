"""Expand design alternatives and explicitly map ideas to the implemented adapters."""
import json
from pathlib import Path
R=Path(__file__).resolve().parent
designs=json.loads((R/'DESIGNS_140.json').read_text('utf8'))
cats=json.loads((R.parent/'r112_category_design_20261021/CATEGORY_AND_METHOD_SPEC.json').read_text('utf8'))['categories']
domains={
'C01':('สถานที่/อาคาร/ชั้น/แผนที่/ช่องทาง/สิ่งอำนวยความสะดวก','center → facility/zone/contact','แยกที่อยู่จากเวลาติดต่อ และคืนเฉพาะช่องที่ถาม','ยังไม่ได้เดินกราฟอาคารจริงระหว่างรัน; อ่าน facts ที่ projection เตรียมไว้'),
'C02':('ชื่อบุคคล/ทีม/ตำแหน่ง/ฟิลด์สาธารณะ','person → team/role/public display name','ไม่ขยายชื่อสาธารณะเป็นสิทธิ์เปิดเผยข้อมูลส่วนตัว','ตัว typed จับชื่อ subject และ facet ตามข้อความ ยังไม่มี name disambiguation ข้ามหลาย alias เต็มรูปแบบ'),
'C03':('รุ่น/เครื่อง/โซน/จำนวนเครื่อง/จำนวนคน/สเปก','equipment_model → resource → zone','แยก physical units, simultaneous players และ room seats','relations ถูก compile บางส่วนเป็น facts; ยังไม่มี runtime graph query/aggregation ทุกรูปแบบ'),
'C04':('ชื่อเกม/บริการ/แพลตฟอร์ม/รายการเกม/วิธีเล่น','game_service.offered → game/service','catalog อ่านรายชื่อครบจาก offering; supported platform ไม่ยืนยันว่าศูนย์มีเกม','compile offering lists และ game details แล้ว แต่ตัวเลือกยังมี lexical top1/subject–facet เป็นหลัก'),
'C05':('เกม/แพลตฟอร์ม/preset/action/context','control_set → binding[action]','คืนเฉพาะ action ตรงบริบท และขอ platform ถ้าขัดกัน','ใช้ subject เกมรวม platform และ binding facts; ยังไม่ได้ทดสอบ preset conflicts และอุปกรณ์ที่ผู้ใช้ตั้งเองครบ'),
'C06':('บริการ/กลุ่มผู้ใช้/จำนวนรอบ/จำนวนคน/วันที่','rate(service,audience,validity,unit) → amount','คิดเลข deterministic; อย่าใช้ราคาปัจจุบันตอบปีที่ยังไม่ยืนยัน','รองรับ integer sessions ต่อคน; ยังไม่มี mixed-audience cart/proration และชื่อ duration บางส่วนเป็น ID ภายใน'),
'C07':('โซน/แพ็กเกจ/กลุ่ม/ครึ่งวันหรือเต็มวัน/อุปกรณ์/วันเวลา','package → price/duration/equipment/terms','แยกครึ่งวัน 3 ชั่วโมง กับเต็มวัน 7 ชั่วโมงตาม owner overlay','typed ยังจับชื่อแพ็กเกจแบบ literal; terms/หลายเงื่อนไขยังไม่เป็น solver เต็มรูปแบบ'),
'C08':('action/สถานะจอง/จ่ายแล้วหรือยัง/ผู้เล่น/เวลา/ช่องทาง','owner procedure + conditions → action steps','อย่าใช้กฎเปลี่ยนเครื่องแทนเปลี่ยนวันที่จ่ายแล้ว หรือทำธุรกรรมจริงเอง','มี policy text facts 9 ชุด แต่ยังไม่มี state machine ที่ bind เงื่อนไขจากสำนวนทั้งหมด'),
'C09':('ยอดเงิน/ผู้โอน/สลิป/สถานะจ่าย/ขอเอกสาร/คืนเงิน','payment policy → required evidence/contact/next step','แยกโอนเกิน โอนขาด สลิปผิด และคำขอเอกสาร','policy facts 7 ชุด; ตัว typed ยังไม่ผูกสถานการณ์ภาษาธรรมชาติเข้า subject ของนโยบาย'),
'C10':('การกระทำ/บุคคล/อุปกรณ์/เหตุขัดข้อง/เงื่อนไข/ข้อยกเว้น','permission policy → condition/exception/remedy','allowed/forbidden/conditional/unknown ต้องไม่รวมเป็น yes/no เดียว','ไม่มี condition graph traversal จริง; lexical ใช้ชื่อ/ข้อความ ส่วน typed ใช้ subject–facet'),
'C11':('วันที่อ้างอิง/เขตเวลา/วันในสัปดาห์/เปิด/จอง/maintenance/closure','dated closure → regular schedule → requested interval','ตอบวันนี้เป็นวันที่และสถานะที่ยืนยันได้; อย่าสรุปช่วงจองเป็นช่วงเปิดทั้งหมด','ชุดนี้ทดสอบ fact reads มากกว่าปฏิทินเต็ม; ยังไม่มี calendar interval resolver รวมทุก exception'),
'C12':('resource/วันที่/ช่วงเวลา/freshness/provider state','resource binding → controlled provider snapshot','unavailable/stale คือยืนยันไม่ได้ ไม่แปลว่าว่างหรือถูกจอง','ใช้ fixture snapshots เท่านั้น ไม่มีการเรียก provider ลูกค้าจริง และยังไม่มี production binding/freshness pipeline ครบ'),
'C13':('เกม/ชื่อรายการ/ปี/หัวข้อ/ข้อกติกา/dependencies','event-specific rule clauses + owner clarifications','อย่าข้ามรายการ/ปีหรือสรุปบทลงโทษโดยตัดเงื่อนไข; งดหน่วยโทษที่เจ้าของสั่ง','clause facts ยังไม่เดิน dependency graph ระหว่างข้อ; ภาษาอังกฤษบางข้อยังเป็นต้นฉบับไทย'),
'C14':('งาน/วันที่/เปิดรับสมัคร/ช่องทาง/ประกาศที่มา','dated event → registration/status/source','แยกไม่มีประกาศยืนยันกับข่าวเก่า และติดป้ายข้อมูลจำลอง','ไม่มี news records จริงใน source projection จึงใช้ synthetic fixtures; ยังวัด real announcement lifecycle ไม่ได้'),
}
def mechanism(d):
 n=d['name']
 if any(k in n for k in ['LLM สรุป','สรุปเอกสาร','อ่านข้อความ','อ่านข้อทั้งหมด','สรุป terms']):
  return ('สรุปเอกสารในหมวด','รวบรวมเอกสารเฉพาะ entity/event ที่ตรง → แบ่ง clauses และส่งให้ตัวสรุป → เก็บ source span ต่อ claim','เสี่ยงตอบเกินคำถาม/ตัดเงื่อนไข ต้องตรวจ claim coverage และขอบเขตหลังสรุป')
 if 'LLM คำนวณ' in n:return ('โมเดลตีความและคำนวณ','อ่านข้อความราคา/หน่วย → ให้โมเดลสร้างรายการคำนวณ → ตรวจซ้ำด้วยเครื่องคิดเลขก่อนตอบ','โมเดลคำนวณเองตรวจสอบยาก ต้องส่ง arithmetic ให้ code จึงจะเหมาะใช้งานจริง')
 if any(k in n for k in ['semantic','contract พร้อม','contract หลาย','semantic fallback']):
  return ('typed ก่อนแล้วโมเดลช่วยตีความ','bind subject/field แบบ deterministic → ถ้าไม่ลงตัวให้โมเดลเลือก existing evidence IDs → ตรวจ schema/subject/field → render จาก source','ถ้า candidates ไม่ครบ โมเดลแก้ไม่ได้; ต้องแยก unknown จาก parser failure และตรวจผลเป็นรายข้อ')
 if 'LLM' in n:return ('โมเดลเลือกข้อมูลในขอบเขต','ดึง evidence ตามหมวดและ entity → ให้โมเดลคืน IDs/field เท่านั้น → validate IDs และเงื่อนไขก่อน render','ต้องมี abstention และ schema; ห้ามถือ HTTP success ว่าเลือกหลักฐานถูกแล้ว')
 if any(k in n for k in ['กราฟ','เดินทีม','dependency','tuple']):
  return ('ค้นตามความสัมพันธ์และเงื่อนไข','bind entities/relations → วาง query path → กรองขอบเขต/เงื่อนไข → อ่านครบทุก node ที่ต้องใช้ → ตรวจ dependency','ต้องมี relation/typing ที่สมบูรณ์; flat text similarity แทน graph execution ทั้งหมดไม่ได้')
 if any(k in n for k in ['ต้นไม้','สถานะ','action-first','สถานการณ์','permission matcher']):
  return ('ตัดสินใจจากสถานการณ์','จำแนก action → ดึงสถานะและเงื่อนไขที่เปลี่ยนผล → เดิน decision table → เลือกนโยบาย/ขั้นตอนเฉพาะกรณี','หากไม่มีเงื่อนไขสำคัญต้องถามเฉพาะจุด; อย่าเลือกกฎจากคำเดียว')
 if any(k in n for k in ['enumerate','แสดง','ทั้งชุด','ครบชุด','ทุกกลุ่ม','นับ physical','all']):
  return ('อ่านเป็นชุดและกรอง','กำหนดขอบเขต entity/filter → enumerate ทุก record ที่มีสิทธิ์และใช้ได้ → รวม/นับด้วย typed values → คืนรายการครบ','top-K อาจทำรายการขาด; ต้องแยก total set จากบางรายการที่ยกตัวอย่าง')
 if any(k in n for k in ['FAQ','keyword','ค้นข้อความ','ค้นข่าว','ค้นเกม','retrieval','ค้นคำ','ค้นฟิลด์']):
  return ('ค้นข้อความ/FAQ ในหมวด','normalize คำถาม → จำกัดหมวด/entity → rank source passages → เลือก clause → ตรวจว่าตรง field และเงื่อนไข','คล้ายคำไม่ได้แปลว่าตอบเรื่องเดียวกัน; ต้องมี threshold/unknown และไม่ยืมข้อมูลใกล้เคียงมาตอบ')
 return ('อ่านข้อมูลแบบ typed','แยก subject/action/field → ผูกกับ schema → อ่านค่าตรง/คำนวณที่รองรับ → ตรวจวัน/หน่วย/สถานะก่อนตอบ','parser ต้องรองรับสำนวนจริงและ missing slots; literal subject matching อาจตอบไม่ได้ทั้งที่มี source')
lines=['# R113 — รายละเอียด 140 แนวคิดและขอบเขตการพัฒนา','',
'เอกสารนี้ขยายแนวคิดทุกหมวด พร้อมแยกสิ่งที่แนวคิดตั้งใจให้ทำกับความสามารถของ prototype ที่ทดสอบจริง ใช้อ่านคู่กับ 01_DESIGNS_AND_SELECTION_TH.md และ 02_BENCHMARK_REPORT_TH.md','',
'## วิธีอ่านคะแนน','',
'คะแนนออกแบบเดิมใช้ rubric correctness 30 / scope 25 / data-only updates 20 / feasibility 15 / latency 10 เป็น heuristic ล่วงหน้า ค่าประเมินผูกตาม family และลำดับไอเดีย จึงไม่ใช่การประเมินเชิงประจักษ์แยกราย 140 แบบ และไม่ใช้เป็นเปอร์เซ็นต์ความถูกต้อง การตัดสินคุณภาพตัวรันให้ใช้ผล 100 คำถามร่วมกันต่อหมวดเท่านั้น คะแนนไม่ใช่หลักฐานว่าแนวคิดที่ไม่ถูกเลือกด้อยกว่าแน่นอน','',
'## โครงร่วมที่พัฒนาจริงก่อนทดสอบ','',
'1. อ่าน common.sqlite แบบ read-only และคำยืนยันเจ้าของ → compiled read model มี fact IDs, entity/field/value, evidence refs และ fixture flags',
'2. แยก 14 source scopes แล้วส่งหมวดที่ทราบแล้วให้ตัวอ่าน; ยังไม่วัด global router',
'3. ทาง A: lexical ranking → top1 ต่อ need; ทาง B: subject/field contract → matching claims; ทาง C: ทาง B แล้ว local model เลือก evidence เมื่อ ambiguous',
'4. แยก coordinated needs, คำนวณจำนวนรอบด้วย code และ renderer ภาษาไทย/อังกฤษตามค่า locale',
'5. ตรวจด้วย oracle ที่แยกจาก answer engine: claims ครบ/ไม่เกิน, ค่าและหน่วย, source refs, answer state',
'6. ตรึง implementation/ข้อมูล/เกณฑ์ระหว่างชุดหลัก; เก็บ raw results และ model event ทุกครั้งที่บันทึกสำเร็จ ไม่มีการคัดเฉพาะคำตอบที่ดี','']
for cat in cats:
 cid=cat['id'];slots,path,policy,gap=domains[cid]
 lines += [f"## {cid} {cat['name']}",'',f'**Input ที่ควรแยก:** {slots}',f'**เส้นทางข้อมูล:** {path}',f'**เงื่อนไขคำตอบ:** {policy}','']
 for d in [x for x in designs if x['category']==cid]:
  kind,route,risk=mechanism(d)
  state=f"คัดมาทดลองด้วย family `{d['family']}`" if d['selected'] else 'แนวคิดสำรอง ยังไม่ได้ implement/test แบบนี้แยกต่างหาก'
  lines += [f"### {d['id']} — {d['name']}",'',f"- คะแนน heuristic เดิม: {d['design_feasibility_score']}/100; {state}",f'- แนวทาง: {kind}',f'- Step 1: แยก {slots} จากคำถาม โดยรักษา entity และ qualifiers ของแต่ละ need',f'- Step 2: {route}',f'- Step 3: ใช้ข้อมูลผ่าน {path}; ถ้าไม่มี source/field ที่ถามให้คืน unknown พร้อมขอบเขตที่ขาด',f'- Step 4: {policy}; แนบแหล่งข้อมูลที่ใช้จริงและตรวจข้ามขอบเขตก่อนส่ง',f'- จุดบกพร่องที่ต้องคุม: {risk}','']
 lines += [f'**ขอบเขตของ 3 ตัวที่รันในหมวดนี้:** {gap}',
 'ชื่อแนวคิดที่มีคำว่า graph/contract เป็นเป้าหมายออกแบบ ส่วน prototype ใช้ reader ร่วมและ projection ที่ระบุข้างต้น จึงไม่ควรอ่านคะแนนว่าพิสูจน์ production graph/solver ครบทั้งระบบแล้ว','']
(R/'01B_ALL_FLOW_STEPS_AND_IMPLEMENTATION_SCOPE_TH.md').write_text('\n'.join(lines)+'\n','utf8')
print('Wrote detailed steps for 140 designs with explicit prototype scope.')
