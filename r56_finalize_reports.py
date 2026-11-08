import json,statistics,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());READY=BASE.parents[1]/'PSU_Esports_Share_R56_20261010'
def read(name):return json.loads((OUT/name).read_text(encoding='utf-8-sig'))
web=read('web_final7.json');target=read('targeted_final7.json');units=read('units7.json');load=read('load_final7.json');rules=read('rulebooks_final5.json');audit=read('PRESERVATION_AND_PACKAGE_AUDIT_7.json');portable=read('package_smoke7c_answers.json')
summary=dict(runtime='2026.10.10-service-r56.7',url='http://127.0.0.1:8093/',web_cases=len(web),web_failed=sum(bool(r['errors']) for r in web),content_checked=sum(r['content_audit']['verdict']=='CONTENT_CONTRACT_CHECKED' for r in web),live_truth_unverified=sum(r['content_audit']['verdict']=='LIVE_FORMAT_CHECKED_TRUTH_UNVERIFIED' for r in web),targeted_cases=len(target),targeted_failed=sum(bool(r['errors']) for r in target),units=units,load_stages=[{k:s[k] for k in ('kind','simultaneous','median_sec','max_sec','failures')} for s in load['stages']],portable_answers=len(portable['rows']),portable_failures=sum(bool(r['errors']) for r in portable['rows']),source_audit=audit,meaning='Bounded content/source contracts and fixtures; not semantic accuracy for all questions or owner approval')
(OUT/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
flow='''# Flow ฉบับตรวจทานและลงมือทำ · r56.7

## เป้าหมายและขอบเขต

แก้ข้อผิดที่มีหลักฐานจาก inventory r55 และการทดลองคำถามบริการจริง โดยเก็บต้นฉบับ นโยบายเจ้าของ ประวัติ และผลที่ไม่ผ่านไว้ ไม่รัน full20k ไม่เรียก HTTP สำเร็จว่าข้อเท็จจริงถูกต้อง และไม่ตีความ owner policy ที่ยังไม่ได้ตอบเอง

## Flow ต่อคำถาม

1. รับข้อความ/locale/session/turn/last_seen_response_id; job ใช้ idempotency ของ session+turn ป้องกันการประมวลผลซ้ำ ข้อความเดิมคนละ turn ยังเป็นคำขอใหม่ได้
2. คืน job ID และสถานะคิว แยกเวลานับจากรับคำขอ เวลารอก่อน dispatch ล่าสุด และเวลาของ dispatch ล่าสุด ไม่เรียกช่วงนี้ว่า GPU inference ทั้งหมด
3. โหลดบริบทที่ผู้ใช้ได้รับคำตอบแล้ว; การรีเฟรช anonymous session เริ่มใหม่ตามพฤติกรรมเดิม
4. แยก translation data ออกจากคำสั่ง; งานเขียนชัดเจนเกี่ยวกับเกมไม่ใช่การขอ catalog แต่คำขอราคา/กฎ/ข้อมูลจริงของศูนย์ต้องใช้ source
5. ถ้าผู้ใช้ปฏิเสธงานเดิมแล้วขอเรื่องใหม่ ให้เน้นคำขอใหม่และเก็บข้อความเดิมใน trace; อย่าลบ negation ทั่วไปหรือข้อความที่ขอแปล
6. แยก clause ที่มีหัวข้อชัด 2–6 ส่วน เก็บทุกส่วน/target/outcome/source evidence ของ child; เกิน 6 หรือเงื่อนไขซ้อนยังไม่ถือว่ารองรับครบ
7. เลือก typed operation: ราคา/รายการเกม/นโยบายบริการ/กฎ/สถานะสด/unknown/clarification/general creation
8. ราคา: ผูก service+user_group+unit+duration+rate+total จาก source; คำสั้น PC/ทั้งหมด สืบทอดเฉพาะ context ที่เกี่ยวข้อง; การเปลี่ยน filter ต้องแทนค่าก่อนคำนวณ ไม่สะสมราคาเดิม
9. Catalog/กฎ: canonical target ต้องตรง; ทั้งหมดตีความตาม scope ที่ยืนยันในบริบท กฎยาวแบ่งหน้าพร้อม returned/remaining IDs; ถ้าต้นฉบับขาดให้ตอบ partial และระบุ gap
10. Booking: อ่าน WordPress ตามคำถาม ใช้ snapshot ของวัน/transport เดียวร่วมกันในคำตอบเดียว คำถามใหม่ fetch ใหม่; timeout/HTML/401/wrong date/missing structure ไม่ใช่ unavailable equipment และห้ามเปลี่ยนเป็นว่าง
11. Source ที่เจ้าของไม่ได้ยืนยัน: ใช้ unknown policy ที่ตรงหัวข้อ ไม่อนุมานจากร้านอื่นหรือกฎการแข่งขัน
12. LLM: shared admission 1, bounded deadline/token budget; งานเขียนต้องตามรูปแบบ/ความยาว ไม่เติมวันเวลา/สถานที่เอง หาก output contract ไม่ผ่านและมี budget ให้ repair ครั้งเดียว เก็บ rejected draft และเหตุผล ไม่แอบผ่อน validator ให้คะแนนผ่าน
13. รวมคำตอบโดยคงสถานะของแต่ละส่วน; source execution coverage ไม่รับรอง factual completeness ข้อความทุกประโยค
14. คืน final result และ client acknowledgement; ไม่มีการ replay หลัง network ambiguity โดยอัตโนมัติ เก็บผลเดิมสำหรับตรวจสอบ

## วงรอบที่ทำจริง

| รอบ | พบ/ตรวจ | การแก้ | หลักฐานและข้อจำกัด |
|---|---|---|---|
| 0 | snapshot + r55 contract audit | frozen source contract v2, mutation oracle | offline audit ไม่ใช่รัน pipeline ใหม่; v1 เก็บไว้ |
| 1 | คำถามหลายส่วน, negation, topic correction, location+parking | 2–6 clauses, scoped exclusions, request_focus, parking regex | targeted baseline/targeted1; มี oracle 3 จุดที่ต้องแก้ตาม source |
| 2 | คนเล่นไม่มีชื่อ word order | service fact cue | targeted2: 38 เคสผ่าน; ไม่รับประกันทุกคำเสีย |
| 3 | คิว elapsed, child source binding, booking atomicity | timing+trace+ContextVar request snapshot | targeted3, units3, web3 ผ่านเกณฑ์ |
| 4 | หน้าเว็บ ternary precedence | elapsed แสดง queued/running ตามที่ตั้งใจ | Node mock protocol checks 4 ผ่าน |
| 5 | RoV EN 11/12, source fragment | hash-bound labelled translation + partial/source gap | rulebooks 28 requests, 8 game/locale checks; RoV source policy ยังไม่ครบ |
| 6 | invitation EN ถูกเลือกเป็น catalog, 80 words ใช้ short_creation cap | explicit creation route + word profile ≥30 | units6/web_final6 ผ่าน; load6 ยัง output rejection 4 |
| 7 | ระหว่าง ถูกมองเป็น ว่าง, invented days และไม่มี repair สำหรับ long writing | scoped regex, prompt constraint, one bounded repair | ดูผล units7/web_final7/targeted_final7/load_final7; ไม่อ้างทุก LLM draft ถูกต้อง |
| แพ็กเกจหลังรอบ7 | worker2ถูกทับกลับ1 และ Stop อ่าน ISO ด้วยThai cultureเป็นปี1483 | ค่าworker2เพียงครั้งเดียว, ParseExact invariant helper | package_process_identity_tests4checks Thai/English, wrong/malformed time rejected; actualstop/restart/smoke7c |

## เกณฑ์ผ่านและการเก็บผล

- ตรวจ mandatory content + source binding + target/units/conditions ที่กำหนดต่อเคส ไม่ใช้เพียง mode หรือ HTTP 200
- ใช้ mutation ลบข้อเท็จจริง/เปลี่ยนราคา/target/เงื่อนไขเพื่อพิสูจน์ว่า validator จับผิดตามขอบเขตได้
- Fixtures มีผลจริงที่กำหนดล่วงหน้า: VR ครึ่งชั่วโมงกินชั่วโมงเต็ม, พัก 12–13, Maintenance/ปิดพิเศษ, parse/API faults ทั้ง TH/EN
- Live WordPress ผ่าน transport/format แยกจาก independent truth verification; ผู้ใช้ยืนยันของจริงเดิมแล้ว ไม่ขอซ้ำโดยไร้เหตุ
- ทดสอบคิวแบบจำกัด 1/2/4/6/8 งาน แยก fast/LLM/mixed; ไม่ใช้แทน sustained load, fairness, capacity หรือ clean Windows
- Source change ต้องส่งต่อไป candidate และแพ็กเกจใหม่ทั้งสอง ตรวจ hash; ไม่แก้ R50 เดิม ไม่ย้าย state/log ของผู้ใช้โดยเดา
- หน่วยทดสอบและ raw web/trace/error/draft เก็บในรอบใหม่ อ่านผลก่อนสรุปปัญหาคงเหลือ

## การทบทวน flow หลังทดสอบ

ผลที่ยังไม่ผ่านต้องแยก transport / routing / source gap / context / generation / validator / oracle ผิด ก่อนแก้ ถ้า source gap ให้ระบุคำถามเจ้าของและไม่สร้างนโยบาย ถ้า validator ผิดให้เก็บข้อผิดกับ oracle เดิม ไม่เปลี่ยนคะแนนย้อนกลับแบบเงียบ ถ้า source/route ถูกแต่ LLM เติมรายละเอียดให้แก้ prompt/repair ภายใต้ deadline ไม่ปล่อย draft ที่ไม่ผ่าน หากเพียง coverage ID ครบแต่ต้นฉบับขาด ให้คง answered_partial

สิ่งที่ยังต้องพัฒนาเป็นขั้นต่อไปอยู่ใน REMAINING_AFTER_R56.md; ไม่อ้างว่า flow นี้แก้ทุกสำนวนหรืออนุญาต deployment สาธารณะแล้ว
'''
(OUT/'FLOW_FINAL.md').write_text(flow,encoding='utf-8')
statuses={
'T01':'เพิ่ม frozen content contract 156 ข้อแล้ว: 145 ตรวจเนื้อหาตามเกณฑ์ +11 live truth unverified; ไม่ใช่ accuracy ทุก claim',
'T02':'เพิ่มตรวจ required facts/source units/fee child binding และ mutation 11/11; semantic completeness ทุกประโยคยังไม่ครอบคลุม',
'T03':'รัน 156 +38 บน r56.7 รุ่นเดียวแล้ว; source units 110 ผ่าน',
'T04':'แก้ oracle 3 จุดในชุดใหม่ตาม source และแยก v1/v2; legacy ทุกชุดยังไม่ได้ audit',
'T05':'เพิ่มสำนวน 38 เคส; หลังใช้แก้ code เป็น regression แล้ว ยังต้อง external untouched holdout',
'T06':'tests typo/service/calendar ที่เลือกผ่าน; ไม่รับรอง subject+action+ชื่อเกมเสียหนักทุกแบบ',
'T07':'ยังมี ambiguity จริง; ต้องถามยืนยันเมื่อขาด anchor ไม่บังคับ fuzzy เป็นคำใกล้สุด',
'T08':'แก้ scoped equipment negation และ explicit topic correction; nested not only/exception ยังจำกัด',
'T09':'registry รวมทุกเกม/ภาคยังไม่ได้ refactor; preserve known controls/resolver',
'T10':'ขยาย explicit clauses 2–6 พร้อม child source evidence; เกิน6/mixed translation+booking+rules ยังต้องพัฒนา',
'T11':'หลาย target/ทั้งหมดและราคา group/duration ในชุดที่เลือกผ่าน; scope ซ้อนทุกมิติยังไม่รับรอง',
'T12':'เพิ่ม price filter changes หลาย turn และ named selection; TTL/topic shift ทุกลำดับยังไม่ทดสอบ',
'T13':'8 game/locale source ID coverage ผ่าน CS2 56, RoV12, Tekken7, VALORANT25; RoV partial และ missing facets ยังอยู่',
'T14':'TH/EN regression และ hash-bound RoV fragment translation; ไม่มี human-approved EN ของ fragment และ Thai word count ยังไม่ตรวจเต็ม',
'T15':'แก้ snapshot ต่อ question/date/transport; parallel fixture fetch ครั้งเดียว; ไม่เปลี่ยน cache policy ของ owner',
'T16':'fault fixtures wrongdate/HTML/401/timeout/empty services ผ่าน; sustained upstream faults ยังไม่ตรวจครบ',
'T17':'shared LLM1 คงไว้; finite fast/LLM/mixed load มีผลเวลาจริง; ไม่ได้ GPU simultaneous all หรือ certified capacity',
'T18':'finite bursts ตรวจแล้ว; sustained fairness/starvation endurance ยังไม่ได้พิสูจน์',
'T19':'แสดง elapsed/admission/last dispatch/deadline แยกใน API/UI; running-job suspension เกินTTL ยังต้อง audit เพิ่ม',
'T20':'queue idempotency/ambiguous network no replay/admission retry fixtures ผ่าน; live hard-kill ทุกจังหวะยังไม่ทำ',
'T21':'bundled model hashes และ actual portable launch เครื่องนี้ตรวจแล้ว; clean Windows/RAM ต่ำยังไม่ได้พิสูจน์',
'T22':'compound source evidence และ job timing เพิ่มแล้ว; ไม่สรุป GPU cause จาก stage ล่าสุดอย่างเดียว',
'T23':'ยังไม่มี controlled ablation ทุก layer; รายงาน finite load มี sample/caveat',
'T24':'เพิ่ม readonly storage diagnostic; retention/cleanup ยังไม่เปิดเพราะต้องกำหนดอายุและbackupก่อน',
'T25':'anonymous refresh behavior เดิมตั้งใจ; ไม่ได้ restore session/history โดยเดา',
'T26':'สร้าง DownloadModels/WithModels รุ่น r56.7 ใหม่ source/data hashes ตรง; R50 เก็บเดิม',
'T27':'same-machine actual portable smoke ผ่าน; clean VM/path long/ZIP/download failure ยังรอตรวจ (long output copy เคย fail จึงใช้ short package root)',
'T28':'manifest/version/source/data hash sync ตรวจแล้ว; URL/โฟลเดอร์เก่ายังเป็นรุ่นเก่า ไม่ sync ข้อมูล owner ข้ามชุดเอง',
'T29':'snapshot/diffs/new candidates preserved; ยังไม่ใช่ state migration/rollback updater',
'T30':'Git metadata ยัง broken; ไม่ reset/clean/ซ่อม linkage เพราะต้องจัด provenance ก่อน',
'T31':'local source viewer ยังไม่ได้ทำ; source/fragment labels มีในคำตอบและ trace',
'T32':'owner admin UI publish ทุกหมวดยังไม่ทำ เป็น feature ต่อไป',
'T33':'on-demand WordPress ไม่ต้องเปิด Dashboard; chatbot/server/เครื่องต้องเปิด, service deployment mode ยังต้องเลือก',
'T34':'แก้ creative 80-word routing/repair ที่เกี่ยวร้านเกม; บทความ500คำ/Thai exact words ยังนอก priority',
'T35':'general translation/reasoning ซับซ้อนไม่รับรองครบ; guard ไม่ยอมคืน rejected draft'
}
remaining='# สถานะประเด็นค้างหลัง r56.7\n\nนี่ไม่ใช่รายการบั๊กที่ยังเกิดทั้งหมด: แยกแก้เฉพาะขอบเขตแล้ว, ตรวจจำกัด, source gap และ feature ที่ยังไม่ได้ทำ\n\n## สถานะ T01–T35 ทุกข้อจาก inventory เดิม\n\n| ID | สถานะและขอบเขต |\n|---|---|\n'+''.join(f'| {k} | {v} |\n' for k,v in statuses.items())
remaining+='''
## ลำดับที่ควรทำต่อเอง

1. หาก load_final7 ยังมี rejected outputs ให้เก็บ reason/draft/repair/provider timings แล้วแก้เฉพาะ generation หรือ validator ที่ผิดจริง ไม่รวมเป็น HTTP failure
2. ข้อความเกิน 6 งาน: ออกแบบ bounded task graph หรือ explicit clarification ที่แจ้งทุกส่วนไม่ให้คำตอบดูครบทั้งที่ตกส่วนใด; เพิ่ม oracle รายส่วนก่อนแก้
3. บริบท/negation/real-word typo: untouched holdout โดยไม่ใช้พัฒนาก่อน, ตรวจ false corrections และลำดับ 8–12 turns; ไม่ขยาย alias เป็นหลัก
4. คิวจริง: sustained fairness, process suspension/deadline, hard-kill mid-generation โดยทำใน runtime แยก; ห้าม replay ambiguous completion
5. แพ็กเกจ: clean Windows VM, RAM ต่ำ, download failure, path/ZIP และ migration rehearsal
6. Source viewer, registry รวม, owner publish UI เป็นงานเพิ่มที่มีขอบเขตใหญ่ ไม่ใช่ defect ที่ต้องเดานโยบายเพื่อปิด

## คำถามที่ต้องมี source หรือการตัดสินใจจากเจ้าของ

- **RoV**: ขอข้อความต้นฉบับเต็มของข้อ 6.1.5 และ 6.1.5.1 โดยเฉพาะท้ายที่หยุดคำว่า “ออกจาก…”; ผล/บทลงโทษที่ตามมาคืออะไร? ไฟล์ raw ที่ metadata อ้างอิงไม่พบ จึงขอไฟล์ใหม่ ไม่เติมเอง
- **ราคา non-PC**: ตารางปัจจุบันสิ้นสุด 31 มี.ค. 2026; หลังวันนั้นใช้ตารางเดิมหรือมีฉบับใหม่ พร้อมวันที่เริ่ม/สิ้นสุด? แสดงอัตราในไฟล์เดิมพร้อม caveat ไม่เปลี่ยนวันหมดอายุเอง
- **เปลี่ยนวันหลังจ่าย**: “จองผิดวันแต่จ่ายแล้วเปลี่ยนได้” กับ “เลื่อนแทนคืนเงินไม่ได้” ใช้ต่างกรณีอย่างไร ต้องติดต่อช่องทางใด/ก่อนกี่ชั่วโมง? ไม่รวมเป็นสิทธิ์เลื่อนได้ทุกกรณี
- **Tekken pause**: clause ที่มีค่าปรับ/เงื่อนไขไม่ตรงกันในเอกสาร ให้ระบุฉบับ/ข้อที่มีผลก่อนตอบยืนยันเดียว
- **เก็บข้อมูล**: job terminal results/log เก็บกี่วัน backup ที่ใด และใครมีสิทธิ์ดู? Diagnostic ทำแล้ว แต่ยังไม่ลบข้อมูลจริง
- **ใช้งานต่อเนื่อง**: ใช้คอมเครื่องนี้แบบเปิดเอง หรือเครื่องบริการที่เปิดตลอด/Windows service? ยังไม่ตั้ง auto-start โดยเดา

รายการนโยบายเจ้าของ 26 fields และ additional gaps/competition facets จาก inventory เดิมแนบข้างล่างโดยคงความหมายเดิม ไม่ถือว่าคำแปลอังกฤษหรือ API success ทำให้นโยบายเหล่านี้ยืนยันแล้ว
'''
old=(BASE/'REMAINING_ISSUES_R55_20261010.md').read_text(encoding='utf-8');start=old.find('## B.');end=old.find('## F.');remaining+='\n'+old[start:end] if start>=0 else '\nดู inventory r55 ต้นฉบับ\n'
(OUT/'REMAINING_AFTER_R56.md').write_text(remaining,encoding='utf-8')
table='| ชุด/พร้อมกัน | median วินาที | max วินาที | ผลไม่ผ่านเกณฑ์ |\n|---|---:|---:|---:|\n'+''.join(f"| {s['kind']}/{s['simultaneous']} | {s['median_sec']:.2f} | {s['max_sec']:.2f} | {s['failures']} |\n" for s in load['stages'])
failed=[]
for s in load['stages']:
 for r in s['rows']:
  if r['errors']:
   calls=[t['metadata']['llm_call'] for t in r.get('job',{}).get('result',{}).get('trace',[]) if t.get('metadata',{}).get('llm_call')]
   failed.append(dict(question=r['question'],errors=r['errors'],calls=calls))
(OUT/'load_final7_failures_extracted.json').write_text(json.dumps(failed,ensure_ascii=False,indent=2),encoding='utf-8')
report=f'''# ผลแก้และวิเคราะห์ r56.7 · 10 ต.ค. 2026

## ผลที่ยืนยันอัตโนมัติในขอบเขตทดสอบ

- Source unit/fixtures: {units['tests']} tests, failures {units['failed']}, errors {units['errors']} ใน10 modules รวม calendar/VR/maintenance/closure/API faults/queue/conversation
- เว็บบริการ: {len(web)} requests บน r56.7, fail {summary['web_failed']}; content contracts {summary['content_checked']} ข้อ + live transport/format {summary['live_truth_unverified']} ข้อที่ไม่ได้ตรวจ independent truth ในรอบนี้
- เว็บสำนวนใหม่/context: {len(target)} requests, fail {summary['targeted_failed']} ตาม mandatory text/negative checks; ไม่ใช่ทุกข้อความใหม่ในอนาคต
- Oracle wrong-answer mutations 11/11 rejected; frontend protocol mock checks4ผ่าน; ไม่ใช่ human/browser visual QA ทุกหน้าจอ
- Full rulebooks: 28 requests บน r56.5, 8 game/locale section-ID checks ผ่าน; codeกฎ/source hashesตรงรุ่น7 (รุ่น6–7แก้creativeเท่านั้น) CS2 56/56, RoV12/12, Tekken7/7, VALORANT25/25 ทุกภาษา
- RoV coverage12/12 เป็น recorded-section coverage; outcome answered_partial เพราะต้นฉบับข้อ6.1.5/6.1.5.1ยังขาด ไม่ใช่ครบกฎจริงทั้งหมด คำแปล fragment ของ agent มี label และ SHA match ก่อนใช้
- Portable WithModels: actual launch พร้อม bundled Python/Ollama บนพอร์ต8096 และคำถาม smoke {summary['portable_answers']} ข้อ, fail {summary['portable_failures']}; ไม่ใช่ clean machine certification

## ทำไมเคยตอบผิด และแก้ตรงไหน

1. **ข้อความหลายหัวข้อถูกดักตอบข้อเดียว**: typed plan/server adapter ตอบ policy ก่อน compound; แก้ delegation และแยก clauses2–6, source child binding ไม่ให้ราคาขาดเงื่อนไข
2. **คำปฏิเสธกิน target ข้างหลัง**: regexข้าม not a student ไปยังPC; ผูกคำปฏิเสธกับชื่อบริการทันที และแยกคำขอใหม่เมื่อปฏิเสธงานก่อนหน้าโดยชัดเจน
3. **ที่จอดรถถูกมองเป็นจอ**: keywordจอไม่มีขอบเขต; แก้จอ(?!ด) จึงตอบ address+parkingครบ
4. **รูปประโยคจริงไม่เข้าคิวบริการ**: “คนเล่นไม่มีชื่อในรายการ”/forgot logout word order; เพิ่ม cues ที่อธิบาย action+subject จริง ไม่เติม policy
5. **APIหลายlookupอาจเห็นคนละ snapshot**: ใช้ request-local snapshot/date/transport ร่วมกันในคำตอบเดียว แต่คำถามถัดไป refresh ไม่ใช่ cacheสถานะเก่า
6. **RoV ENขาด section**: validatorถูกที่ไม่เรียก untranslated fragmentว่า complete; เพิ่มเฉพาะแปลข้อความที่อ่านได้แบบ hashbound + sourcegap warning ต้นฉบับไม่ถูกแก้
7. **คิวทำให้เข้าใจผิดว่าโมเดลช้าเท่าทั้งjob**: ก่อนนี้ไม่แยก elapsed/dispatch; ตอนนี้มี timingfields/UI label และเก็บ trace, lastdispatchไม่ใช่ cumulative GPUtime
8. **เขียนคำเชิญENตอบเกม42เกม**: English inventoryguardมาก่อน creationintent; named taskเลือก general creation ก่อน incidentalgamewords แต่ actualstudiofactrequestยัง grounded
9. **80คำใช้ cap25คำ**: wordprofileจับขั้นต่ำ100; ลดเฉพาะ explicitwordrequestถึง30และปรับboundedtokenbudget
10. **ระหว่างถูกเป็นว่าง/เติมวันเวลาเอง**: factualregexไม่มีboundary, promptไม่ชัดและ longcreationrejectไม่ได้repair; จำกัดregex เพิ่มpromptและrepairครั้งเดียวภายใต้deadline เก็บrejectguardเดิม

## โหลดพร้อมกันบนเครื่องนี้

{table}
finite warm batches ไม่ใช่ sustained maximum capacity; nสูงสุดแต่ละชุดมีsampleเท่าจำนวนn จึงไม่ใช้ p95 เป็น production SLO งานLLMยังใช้sharedlimit1 ต้องรอคิว ส่วนfastใช้workersได้โดยไม่รอGPUทั้งหมด

Load7 เหลือ {len(failed)} คำตอบไม่ผ่านเกณฑ์; รายละเอียด/provider/draft/repair อยู่ load_final7_failures_extracted.json: EN invitation3ครั้งความยาวต่ำกว่า64คำหลังrepair1ครั้ง, THdialogue1ครั้งวนซ้ำจนtokenlimit. เป็นผลซ้ำของคำถามบางแบบ ไม่ใช่4uniquebugs. Modeเดิม general_rag_miss_llm_unavailable ยังเป็นชื่อlegacy; llm_failure_reason/rejected_reasonแสดงoutputquality. ไม่ใช่ automatic transport outage ผลLLMไม่รับรองความลื่นของภาษาไทยหรือwordcountภาษาไทยตรง80ทุกคำ

งานเขียนทั่วไปยังมีข้อจำกัด จึงไม่ปิดT34/T35ทั้งหมด; คำตอบที่rejectไม่ได้ถูกปล่อยให้ผู้ใช้เป็นข้อมูลศูนย์ที่ยืนยันแล้ว

## การตีความผลแต่ละรอบ

- baseline38มี15fail (รวมoracle3ข้อ); targeted1เหลือ4 (oracle3+namedplayer1); targeted2/3ผ่านหลังแก้ตามsource
- v1contractaudit8failส่วนใหญ่oracle; v2เหลือ2tracebindingcompoundที่คำตอบเดิมถูกอยู่แล้ว จึงแก้evidenceไม่แต่งราคาหรืออ้างผลเดิมผิด
- load6fail4: providerstopไม่ได้truncation/timeoutหลัก แต่inventedtoday/tonightและroutefalsepositive; loop7แก้prompt/repair/regex ไม่ลดvalidationเพื่อเพิ่มคะแนน
- HTTPconnectionrefusedครั้งแรกหลังrestartเกิดก่อนserverlisten; ไม่ใช่failedanswercontract การรันหลังhealthreadyมีไฟล์web_final7
- Portable startupแรกผ่านแต่พบworker override; StopแรกfailเพราะcurrentcultureThaiแปลISOyear2026เป็น1483. แก้helperInvariantCulture+RoundtripKindโดยไม่ผ่อนPID/path/timechecks. ตัวหยุดจริงผ่านหลังแก้ และเปิดซ้ำใช้worker2; เก็บlauncherก่อนแก้+hash+testผลไว้ ไม่แก้R50

## เก็บรักษาและแจกใช้งาน

Snapshot484ไฟล์, changedexisting{len(audit['changed_existing'])}, addedrelevant{len(audit['added_relevant'])}, originalsourceที่หาย0, owner38ไฟล์hashไม่เปลี่ยน; candidate/app/webและแต่ละแพ็กเกจruntimeData495ไฟล์ไม่มีhashmismatch
ไฟล์sourceเดิมที่แก้มีcopyก่อนแก้+diff; originallogsไม่ได้hashทั้งหมดแต่ไม่มีการตั้งใจdelete/truncate; ผลแต่ละรอบและpackagesR50ไม่ถูกแทนที่ Gitmetadataเดิมbrokenจึงใช้snapshotdiff ไม่claimgitclean

แพ็กเกจใหม่: {READY}
01_Download_Modelsประมาณ3.02GB โหลดweightsอีก3.65GBครั้งแรก;02_With_Modelsประมาณ6.68GBมีweights (decimalGB) ขนาดเทียบตอนbuildก่อนnewsmokelogs
ไฟล์modelcheck/hashpassของWithModelsแยกจากready=falsemissing2ของDownloadModelsที่ตั้งใจไม่มีweights; เว็บจองยังต้องinternet

เอกสารต่อ: FLOW_FINAL.md, REMAINING_AFTER_R56.md, PRESERVATION_AND_PACKAGE_AUDIT_7.json, source_changes_7.patch, SUMMARY.json
'''
(OUT/'RESULTS_ANALYSIS_TH.md').write_text(report,encoding='utf-8')
(OUT/'HANDOFF_R56.md').write_text(f'''# Handoff r56.7

Active candidate `{OUT / 'candidate_7/PSU_Esports_Chatbot_Local'}` URL http://127.0.0.1:8093/ version2026.10.10-service-r56.7. ROOTมีโค้ดแก้จริงแล้ว ไม่ใช้Gitreset/clean. BundledPythonของReady20261003. UserOllama11434/old8091ไม่ได้หยุด.

อ่าน RESULTS_ANALYSIS_TH.md, FLOW_FINAL.md, REMAINING_AFTER_R56.md และ SUMMARY.json ก่อนทำต่อ. Source snapshotก่อนงานอยู่before/;before_loop7สำหรับล่าสุด;source_changes_7.patch. Ownerhash38ไม่เปลี่ยน.

สองแพ็กเกจใหม่อยู่ `{READY}` เปิดStart-Chatbot.cmd;WithModelsพร้อมweights,DownloadModelsยังต้องโหลด. Actualportabletestเป็นsame-machine ไม่ใช่cleanWindows;port8096เป็นsmokeเท่านั้นและใช้StopChatbotของแพ็กเกจเองหลังจบ.

Raw failuresรอบเก่าและsourcegapRoVต้องรักษา. Runtimeversionในhealthต้องตรงก่อนเทส. อย่าเก็บliveAPIpassเป็นtruthpass;อย่าขยายpolicyunknown26/priceexpiry/Tekkenconflict/RoVmissingendingเอง. Full20kยังไม่รันตามคำสั่งผู้ใช้.
''',encoding='utf-8')
for variant in ('01_Download_Models','02_With_Models'):
 d=READY/variant;p=d/'README_R56_TH.md';t=p.read_text(encoding='utf-8').replace('R56_REVISION6_CHECKS','R56_REVISION7_CHECKS');p.write_text(t,encoding='utf-8');docs=d/'reports/R56';docs.mkdir(parents=True,exist_ok=True)
 for name in ('FLOW_FINAL.md','RESULTS_ANALYSIS_TH.md','REMAINING_AFTER_R56.md','SUMMARY.json','PRESERVATION_AND_PACKAGE_AUDIT_7.json'):
  shutil.copy2(OUT/name,docs/name)
print(json.dumps({k:v for k,v in summary.items() if k not in ('source_audit','units','load_stages')},ensure_ascii=False))
