import re
from pathlib import Path
R=Path(__file__).resolve().parent
original=(R.parent/'r123_parity_inventory_20261023/PARITY_COMPONENTS_TH.md').read_text('utf8')
items=[(m[1],m[2].strip()) for m in re.finditer(r'^\|\s*([A-F]\d\d)\s*\|([^|]+)\|',original,re.M)]
groups={
'A':[
'เชื่อมแล้ว: 18 draft bindings จาก catalogue จริง',
'เชื่อมแล้ว: internal service/resource → external ID พร้อม source snapshot',
'ใช้การเลือกผลิตภัณฑ์ตามรอบ/เวลาแบบเดิม; ไม่บวก binding เป็นจำนวนเครื่อง และไม่สร้าง physical equivalence ที่ source ไม่ยืนยัน',
'ใช้ status mapping พร้อม available count; unknown ไม่เป็น free',
'ตรวจ timezone, TTL และ effective mapping ด้วย observation wall clock แยก semantic booking date',
'เปิด profile WordPress จริงบน candidate API ไม่ใช่ unavailable fixture',
'ตรวจ catalogue/status จริงและ health แล้ว; เป็นหลักฐาน ณ เวลา probe ไม่ใช่ uptime guarantee',
'แยก recorded play slots จาก conflicted physical opening; ไม่แก้ raw conflicted fields',
'ใช้ renderer/contiguous-slot/count/list selectors เดิม และมี fault gates',
'แยก missing binding/configuration, payload/freshness และ transport; ไม่รวมเป็น model/content failure'],
'B':[
'อธิบายตัวเลขขัดแย้งครบ 5 วันและแยก predicate แล้ว',
'คง unknown scope; ใช้ตารางบริการเล่นที่บันทึกไว้ ไม่ขยายเป็นเวลาเข้าทุกพื้นที่',
'คงข้อจำกัด effective period ไม่ประกาศว่าเป็นตารางใหม่ทุกปี',
'ใช้ recorded closure/calendar semantics เดิม; ไม่อ้าง physical scope ที่ไม่มีหลักฐานเพิ่ม',
'ใช้ source-backed FAQ/policy ที่มี; ไม่สร้างนโยบายจัดการ booking จากการมี closure record',
'คง owner per-person confirmation ที่ผูก value hash; unit unknown ไม่ทำให้อัตราทั้งแถวหาย',
'แยก as-of confirmation กับ effective interval และตรวจปี/วันที่ใน calculator',
'คงราคาเหมา 24 แถว; terms ที่ไม่ยืนยันไม่ถูกเดาจากราคา',
'live ใช้ catalogue mapping จริง; physical members ที่ไม่ระบุไม่ถูกแต่งเพิ่ม',
'อ่าน offering/zone graph ได้; exact installed station ต้องมี edge ของมันเอง',
'ใช้ FAQ เจ้าของสำหรับคำถามที่ตรงครบข้อ; ไม่อนุมาน max players ของทุก mode จากจำนวนจอย',
'แยก studio offering platform จากทุก platform ที่ตัวเกมรองรับ',
'ตรวจทุก record ว่ามี projection หรือเป็น relation/stub/metadata; FAQ known-answer projection gap เป็น 0',
'คง edition/version/age uncertainty; ไม่ย้ายชื่อใกล้กันมาเป็นเกมเดียวโดยไม่มีหลักฐาน',
'เอกสาร check-in และ deadline อ่านจาก FAQ เดิม/เจ้าของได้ ไม่ต้องกรอกซ้ำเพราะ typed field บางช่อง unknown',
'ข่าวต้องมี source/date ที่ใช้ได้; exact FAQ ไม่รับคำถาม latest/upcoming เป็นข้อมูลคงที่',
'เก็บ variants/conflict และ source profile period; ไม่สร้าง approvals แทนเจ้าของ',
'รวม clause เฉพาะ full body/event ตรงกัน รักษา English และ dependencies'],
'C':[
'ใช้ whole-question context/validated task plan + exact FAQ ทั้งข้อ; ไม่อ้างว่ามี perfect semantic need detector',
'คง shared/local slot compiler และ source-span gates; ไม่คัดลอกปริมาณข้าม task เอง',
'ใช้ unique referent ที่ตรวจได้; หลาย antecedents ต้องถามกลับ',
'คง trusted delivered-state adapters; ตรวจ source edit/withdraw และ cache epoch ไม่ใช่รับประกันทุก dialogue scenario',
'ใช้ protected intents เดิมแยก bring/consume และ studio/tournament context',
'แก้ PS5 #01 normalization; ป้องกัน edition/จำนวนและ button substring; compound chord มาก่อน single key',
'คง duration/session/compare operator และ rounding ตาม current rate source',
'ใช้ source aliases/query profiles และ explicit event rules ก่อน equipment definition; ไม่สอน teacher error',
'คง R121 validated wire แล้ว compile เป็น IR; เปลี่ยน runtime/source wiring โดยไม่อ้างว่าฝึก graph-wire model ใหม่',
'คง provenance/quote/span gates และตรวจ 289 annotations compile; ไม่อ้าง Unicode equivalence ครบทุกการแปลง',
'แยก missing input/source, conflict, unsupported operation และ provider failure ใน ledger'],
'D':[
'registry ระบุ operation/facet ที่ทำได้จริง รวม recorded calendar-state; ไม่เปิดทุก operator ให้ผ่านโดยปริยาย',
'ตรวจ complete recorded control set และ partial_official แยกกัน; partial list ไม่เท่ากับ factual error',
'แก้ native calendar/live compounds ให้ typed reads ของทุก child มาก่อน deferred evidence selection',
'ทดสอบ budget 0 แล้วยังเก็บ calendar/booking ที่ตอบได้ ไม่ให้ task แรกทำผลอื่นหาย',
'ใช้ Decimal/current unit/duration/audience rules; ไม่ฝังราคาใน model/router',
'ใช้ event-specific clauses, section families, declared dependencies; ไม่หยิบ keyword hit เดียวตอบหมวดเต็ม',
'source refs/current snapshot/variants/conflict guards; ไม่ประกาศว่ามี global authority theorem solver',
'ตรวจค่า ตัวเลข identity และ planned obligations; ยังไม่ใช่ semantic entailment oracle ทุกประโยค',
'ตอบ fact ก่อน เก็บเงื่อนไขและ verification notes; ยังมี wording/variant repetition ที่ไม่ใช่ content failure',
'ต่อ shared native calendar adapter และ recorded play slots; การมี helper ไม่ใช่คะแนน parity เดือน/ปีทุกคำถาม',
'เก็บ reason codes/source/transport แยกถึง API logs และรายงานรายข้อ'],
'E':[
'review teacher contrasts ที่พบจริง; 289 compile gates ไม่ถูกเรียกว่า reviewed gold ทั้งหมด',
'เก็บ wrong-topic/task-omission/source-version teacher cases แยก ไม่คัดลอกเป็นคำตอบฝึก',
'ใช้ R121 adapter ที่มีอยู่กับ native compiler/legacy frames; ไม่มี training ใหม่ใน R124 และไม่อ้างว่าฝึกแล้ว',
'61 retained keys เป็น development set ใช้แก้ระบบแล้ว ไม่ถือเป็น fresh holdout',
'รัน legacy/common จริงและเปิดเผย model/data/clock/provider differences ไม่อ้าง causal Flow-only effect',
'แยก protocol/literal/source/content/transport; ไม่มีการเปลี่ยน gate count เป็น % accuracy ทั้งระบบ',
'เก็บ actual generation calls, profile/provenance, traced latency และ real API probe latencyแยกกัน'],
'F':[
'คง schema/editor/source references และ draft/approval boundaries เดิม',
'compile readiness และ capability registry ตรงตัว executor ที่เปิด; ขอบเขต semantic verification ระบุชัด',
'มี exact whole-question stable FAQ path และทดสอบ source change/epoch ให้ข้อมูลใหม่เปลี่ยนคำตอบได้',
'withdrawn known intent ไม่ย้อนตอบ legacy constant; test cache/source withdrawal เป็น memory fixture',
'เปิด candidate live API จริง แยกจาก R78; ไม่ติดตั้งทับ production หรือสร้าง approvals'],
}
actions={g+f'{i:02d}':text for g,values in groups.items() for i,text in enumerate(values,1)}
assert len(items)==62 and set(actions)=={i for i,_ in items}
lines=['# รายการติดตาม A01–F05 จาก inventory ก่อนหน้า','',
'ทุกแถวมีการจัดการหรือขอบเขตที่ชัดเจน ข้อจำกัดจาก source และข้อจำกัดของการพิสูจน์ semantic ไม่ได้ถูกแปลงเป็นข้อเท็จจริงเพื่อให้สถานะดูครบ และไม่ถือว่าต้องให้เจ้าของกรอกข้อมูลเดิมใหม่ทั้งหมด','',
'คำว่าใช้ได้ในตารางหมายถึง implementation/หลักฐานตามขอบเขตที่ระบุ ไม่ใช่ 100% accuracy ของทุก operator หรือทุกบทสนทนา การเปลี่ยนเป็น graph wire ใหม่/ฝึก weights ใหม่ไม่ได้เป็นเงื่อนไขจำเป็นของการซ่อม binding/projection/reader ในรอบนี้ และไม่มีการอ้างว่าได้ฝึกใหม่','',
'| ID | รายการเดิม | การจัดการใน R124 / ขอบเขตหลักฐาน |','|---|---|---|']
lines += [f'| {i} | {title} | {actions[i]} |' for i,title in items]
(R/'IMPLEMENTATION_CHECKLIST_TH.md').write_text('\n'.join(lines)+'\n','utf8')
print('Wrote 62-item implementation/source-boundary checklist')
