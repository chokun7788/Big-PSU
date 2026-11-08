import json,hashlib,urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path
r=Path(Path('r31_report_path.txt').read_text().strip());p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');root=Path(__file__).parent
def load(name):return json.loads((r/name).read_text(encoding='utf-8'))
full=load('R31_C_FULL_ANALYSIS_SUMMARY.json');common=load('R31_COMMON_SCORING_COMPARISON.json');remaining=load('R31_REMAINING_PAIRED_SUMMARY.json');extra=load('R31_C_EXTRA_CORPUS_ANALYSIS.json');api=load('API_FINAL_B_C_SUMMARY.json');post=load('postrelease8090_C_http_summary.json');paths=load('postrelease_C_path_guard_summary.json');idle=load('idle8090_C_concurrency.json');units=load('final_C_unit_all.json');preflight=load('release_preflight_C.json')
assert preflight['changed_behavior_release_gates_passed'] and idle['passed']==10 and paths['passed']==44 and sum(x['passed'] for x in post['by_suite'].values())==46 and not extra['new_failed_grades']
health=json.load(urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=8));assert health['ok'] and health['warmup']['ok'] and health['runtime']['version']=='2026.10.02-question-target-content-r31'
with (r/'final_health_8090_C.json').open('x',encoding='utf-8') as out:json.dump(health,out,ensure_ascii=False,indent=2)
def link(name):return f'[{name}](<{(r/name).as_posix()}>)'
flow_path=p/'docs/131_question_target_content_r31_flow_20261002.md';assert flow_path.read_text(encoding='utf-8')==(r/'flow_initial.md').read_text(encoding='utf-8')
flow='''# Flow r31 ฉบับตรวจหลังลงมือ — เป้าหมายเกม สิ่งที่ถาม และข้อ source

ปรับ 3 ระยะ A → B → C จากผลจริง วันที่ 2 ตุลาคม 2026 เวลาไทย รุ่นเว็บ `2026.10.02-question-target-content-r31` แพ็กเกจ C

## 1. ขอบเขตที่ทำสำเร็จในรอบนี้

กู้ชื่อเกมยาวที่พิมพ์ผิดในบริบทกฎ แยกสถานที่/ระยะเวลารายการ CS2 กับคำถามตำแหน่งปุ่ม และแยก tactical timeout/technical pause/เงื่อนไข Freeze time ทั้งไทยและอังกฤษ ข้อมูลมาจากเอกสารที่มีอยู่ ไม่สร้างนโยบายใหม่

ตัวตรวจสิ่งที่ถามกับข้อ source อิสระมี **3 กลุ่มของ CS2**: technical pause, tactical timeout และ venue/duration ยังไม่ได้ครอบคลุมทุก proposition ทุกเกม คำว่า “source ถูก” หรือ “confidence สูง” ไม่รับรองว่าตอบครบทั้งคำถาม

## 2. Flow ที่ลงมือแล้ว

1. เก็บ Git status, snapshot app/tests 258 ไฟล์ และตรวจ hash ข้อมูลเจ้าของ/Gold 584 ไฟล์ ก่อนแก้ → ผ่านตรวจหลังทำ ไม่มี original test หรือข้อมูลเจ้าของเปลี่ยน
2. สร้างข้อทดสอบจาก source พร้อม raw answer/trace และ baseline → fixture20 เดิมผ่าน6 จากนั้น A19 และปรับก่อน full sweepเป็น20; แต่6เคสชื่อเกมตรวจ target/source ไม่รับรองเนื้อหาทุกหัวข้อ
3. กู้ชื่อเกมทั้งช่วงก่อน generic normalization → bounded optimal string alignment edit distance รองรับเพิ่ม/ขาด/สลับ/ผิด, แยก script/ขอบคำ/เลขภาค/รุ่น, รับเฉพาะชื่อยาวที่เลือกได้ชัด และเก็บ original span/alias/edits ใน trace ไม่แก้ CS3 ให้เป็น CS2
4. อ่าน proposition ที่ถามโดยผูกกับเกม → Freeze time ที่ต่อหลัง timeout เป็นเงื่อนไขของ timeout; การถาม round time แยกยังคงตอบ; technical qualifier ไม่กลายเป็น tactical quota
5. อ่านข้อ source และ English localization ที่ hashตรง → ตอบข้อเต็มพร้อมจำนวนครั้ง เวลา และเงื่อนไข ปีรายการไม่ตรงต้องไม่เอารายการ2026ไปยืนยัน2027
6. Validator เทียบข้อที่ถามจากโจทย์กับ source/คำตอบ → ตัด quota/time/condition ออกในการทดสอบแล้วต้องไม่ผ่าน; correct source ID อย่างเดียวไม่พอ
7. รัน full sweep A 20,327 inputs /55,583 grades → processหยุดหลัง18,894; รักษาไฟล์เดิมและรันเฉพาะ1,433ที่เหลือ ไม่อ้างผลที่ยังไม่ครบ
8. ทบทวนผล/คำตอบจริง → พบคำถาม “pause และ timeout” ตก pause แม้ old gateผ่าน จึงเพิ่ม contractทั้งสองเรื่องและ18เคสพร้อม negative controlsใน B
9. ทบทวน API B → พบภาษาไทย “เวลานอกทางเทคนิค” ยังเข้าหัวข้อรวม เพราะ rule gateไม่รู้วลีไทยและ tactical matcherจับคำว่าเวลานอกซ้ำ จึงแก้ gateที่ผูกCS2และ suppress tactical matchเฉพาะ technical qualifierใน C
10. ตรวจคะแนนคู่ clean/noisy → เพิ่มการจำแนก mode `competition_rule_detail_source` เป็น answer โดยยังตรวจ no_answer/clarificationก่อน และยังต้องตรวจ contentต่างหาก เทียบ G6/Cด้วย classifierและoverlayเดียวกัน ไม่เอาคะแนนที่เพิ่มเพราะ grader มาอ้างว่าโมเดลดีขึ้น
11. รัน unit441, full/extra affected replay, API gates, preservation/package hashes → สร้างแพ็กเกจ C เปิด8090 แล้วตรวจ post-release46, live-path/guard44 และ idle concurrent10; ปิดเฉพาะเว็บทดสอบ8091โดยเก็บlog
12. เก็บ failure inventory/paired remainingพร้อม trace/expected/คำตอบclean/noisy; แยกข้อผิดจริง ข้อคาดหวังเก่า source gap และ live dependency

## 3. หลักฐานและ gate สุดท้าย

| ชุด | ผล | การตีความ |
|---|---:|---|
| Fixtureเฉพาะจุด | 20/20 จาก6/20 | venue/timeout และtarget checksตามชนิดเคส |
| Compound + technical/tactical controls | 18/18 | ข้อ sourceเต็มทั้งไทย/อังกฤษ และเรื่องที่ไม่ถามต้องไม่ปน |
| Unitล่าสุด | 440/441 | เหลือGold English builder driftเดิม1ข้อ ไม่แก้frozenGoldให้เขียว |
| APIรวม | 941/941 | B941ครบ → Cรันซ้ำ482ที่ได้รับผล และเก็บB459ที่ไม่เปลี่ยน; ไม่ใช่Cรัน941ใหม่ |
| Strong competition clauses | 728/728 | รวม composition280/content320/new128 ใน APIรวม; ไม่ใช่เจ้าของรับรอง |
| หลังเปิดเว็บหลัก | 46/46 | 20new +18compound +8locale |
| Live-path/guard | 44/44 | live8เป็นทางดึงข้อมูล; guard36เป็นการบล็อก; ไม่มี occupancy oracle |
| 10พร้อมกัน รอบidle | 10/10 | locale/catalog count oracle; ไม่ใช่SLAของWordPressช้า |

Full Aครบ20327; Bรันซ้ำ4370กลุ่มcompetition/CS2/pause; Cรันซ้ำ355กลุ่มpause/timeout ข้อมูล inputและgradeยังครบเดิม ไม่อ้างว่าทุกรอบรัน20327ใหม่ ชุดเสริม A970inputs/981grades → Cรันซ้ำ321ที่เกี่ยวข้องและเก็บ649เดิม

เกณฑ์ rootเดิมมี inputsที่อย่างน้อย1gradeไม่ผ่านลด1905 →1898; newly failed grades=0 จำนวนนี้ไม่ได้แปลว่าคำตอบผิดจริง1898ข้อ เพราะมี historical/metadata/weak/no-content oracle

เมื่อใช้ **เกณฑ์เดียวกันทั้ง G6/C** คู่2000: clean1772ทั้งคู่, noisy1665 →1672, cleanผ่าน/noisyตก118 →111 (ไทย57/อังกฤษ54); ดีขึ้น7 ไม่มีคู่ผ่านเดิมตกใหม่ ใน111มีpositive content contract43 และไม่มี68 จึงไม่เรียก111คำตอบผิดเชิงเนื้อหาทั้งหมด

Smoke85ชุดแรกผ่าน71/85 ข้อที่failเหมือนG6เดิม; Bตรวจ16competitionที่เกี่ยวข้องผ่าน11/16โดยไม่มีข้อผ่านเดิมตก ทั้งชุดแรกและBมีขอบการเปลี่ยนไฟล์ระหว่างช่วงเวลา จึงอ้างfreeze Cได้จากunit/API/content gatesล่าสุด ไม่อ้างว่า85smokeรันบนCทั้งหมด

## 4. สิ่งที่ยังต้องแก้ — Flow ลำดับถัดไป

### P0 — ความหมายเรื่องสถานะสดต้องไม่หลุดไปตารางบริการ

ตัวอย่างจริง “พรุ่งนี้13:00 Nintendo Switch ... วางหรือเปล่า” หลุดจากliveไปcalendar ในcontrolled-offlineคู่ทดสอบ → เก็บคู่เป็นfixture, ตรวจavailable-intentจากบริบทอุปกรณ์+วันเวลา+คำกริยา, ตรวจfreshness requirementอีกชั้นก่อนrender ห้ามใช้ตารางเปิดบริการรับรองว่าง/ถูกจอง ควรเข้าlive fetchหรือบอกว่ายืนยันสดไม่ได้ การตรวจเลขเวลา/เครื่องต้องไม่แก้เอง Real occupancy oracleยังพักตามผู้ใช้

### P1 — ชื่อถูกแต่หัวข้อ/หลายข้อยังไม่ครบ

ตัวอย่าง “อารีน่สออฟเวเลอร์ ... จำนวผู้เล่นต่อทีม” รู้RoVแล้วแต่ตอบข้อชื่อตัวละคร; “การตั้งค่าในเกม” ตอบแค่หัวข้อ; “คุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน” ตอบเพียง late-registration → เพิ่ม source-derived positive oracleของแต่ละหัวข้อและรายข้อที่ผู้ใช้ขอ; กู้ facet spanด้วยขอบ/บริบท; แยก overview/ค่ารายละเอียด; ไม่ให้ headerหรือข้อข้างเคียงผ่านเพราะsourcegameตรง; หากเจาะข้อไม่ได้ให้ถามตรงประเด็น การกู้ชื่อ7ข้อที่ผ่านV2ยังไม่รับรองsemantic answerทั้งหมด

### P1 — คำผิดที่เป็นอีกคำจริง/คำถามทั่วไป

ตัวอย่าง “Where can you play...” → “Wherw can you pay...” ไปตอบราคา; Pokémon ... “โซซนไหน” ไปno_answer → ใช้บริบทquestionframeและservice/game entitiesแยก play/pay; ambiguityต้องถามเมื่อหลักฐานไม่พอ, ไม่บังคับแก้payเป็นplayหรือriceเป็นPriceเสมอ เติม real-word errorsและThai deletion/repeat fixturesพร้อม content oracleเดียวกับclean

### P2 — Evaluation และแหล่งข้อมูล

อย่าแก้frozen Gold/old logs: เพิ่มเวอร์ชันoracleแยกและบันทึกreview reason Mode/source keywordไม่ใช่semantic correctness; English shadow1600ที่ไม่มีคำแปลมนุษย์ไม่เรียกapproved เก็บsource gaps/conflictsและรายการถามเจ้าของชัดเจน

### P2 — Queue/503 เมื่อเครื่องหรือ upstreamช้า

Smoke10พร้อมกันยังมี503ขณะรันงานอื่น ส่วนidleผ่าน10/10 → เก็บHTTP body/queuewait/deadlineและแยกsource latency; วัดสถานการณ์หลายคำถามWordPressช้าก่อนปรับworker/RAM แสดงสถานะรอ/ลองใหม่เป็นงานเสริม ไม่ลดcorrectness gate

## 5. คำถามที่ต้องให้เจ้าของตัดสินใจ

1. ให้ใช้CS2/VALORANT2026, RoV Blueket2025ประเภททีมชาย และTekkenฉบับที่มีเป็นกติกาปัจจุบันของรายการใดบ้าง? แต่ละฉบับยังมีผลถึงวันใด และมีฉบับใหม่หรือไม่?
2. Tekken การpauseมีข้อยกเว้นใด และโทษกรณีpauseแต่ละกรณีให้ใช้ข้อความจากแหล่งใดเมื่อเอกสารขัดกัน?
3. RoVข้อ6.1.5.1ที่ถูกตัด ข้อความเต็มคืออะไรและเอกสารฉบับใดเป็นauthoritative?
4. มีนโยบายภาพ/วิดีโอ อายุผู้สมัคร ค่าสมัคร และcontrollerที่ต้องตอบหรือไม่? ขอข้อความ/แหล่งต้นฉบับ ไม่ให้ระบบสร้างเอง
5. เมื่อกลับมาทดสอบจองจริง ให้提供สถานะที่เจ้าของรู้แน่ของเครื่อง+วันที่+ช่วงเวลา และเวลาที่ตรวจ เพื่อเทียบว่าง/ถูกจอง การเข้าถึงWordPressสำเร็จอย่างเดียวไม่พอ

## 6. เกณฑ์สำหรับรอบต่อไป

สร้างsource oracle → เก็บbaseline/trace → แก้เฉพาะlogicมีหลักฐาน → positive/negative/mutation tests → clean/noisyเดียวกัน → root/APIaffected replay → เปรียบเทียบเนื้อหาผ่านเดิมตกใหม่ → แพ็กเกจ/hash → ผลหลังเปิดเว็บ และปรับFlowจากความผิดจริง ไม่เพิ่มaliasทุกประโยคหรือเปลี่ยนนโยบายโดยเดา
'''.replace('ให้提供','ให้ส่ง')
with flow_path.open('w',encoding='utf-8') as out:out.write(flow)
with (r/'FLOW_FINAL_C.md').open('x',encoding='utf-8') as out:out.write(flow)
lines=['# ผลและวิเคราะห์ PSU Esports Chatbot r31','', 'วันที่ 2 ตุลาคม 2026 เวลาไทย — Revision C','', 'เว็บหลัก: [เปิดแชท](http://127.0.0.1:8090/) | รุ่น `2026.10.02-question-target-content-r31`','',f'Flowฉบับตรวจหลังลงมือ: [Flow r31](<{flow_path.as_posix()}>)','',
'## แก้แล้วและทำไมเดิมจึงผิด','',
'### 1. ชื่อเกมผิดถูกแบ่งแก้ทีละส่วน','',
'ชื่อเคาน์เตอร์สไตรก์ที่เบิ้ล/ขาดบางตำแหน่งผ่านgeneric normalizationก่อนระบุtarget จึงได้ชื่อครึ่งไทยครึ่งอังกฤษหรือไม่มีtargetแม้คล้ายชื่อsourceมาก ระบบเลยถามเกมใหม่ แก้ให้เทียบชื่อยาวทั้งspanจากregistryก่อนการแทนทั่วไป ใช้optimal string alignment รองรับinsert/delete/substitute/transposition จำกัดedit budget2เมื่อยาว≥10อักษร/1เมื่อสั้นกว่า และfraction≤0.18 ต้องไม่มีคู่แข่งต่างเกมใกล้กันเกินmargin0.08; ชื่อสั้น<6ตัวเลขและภาคไม่ทำfuzzy recovery ตัวเลขเหล่านี้คือกติกาเลือกcandidate ไม่ใช่เปอร์เซ็นต์คำตอบถูก','',
'Traceเก็บinput_text/offset/original/canonical/registered_alias/edit count; ไม่เพิ่มwhole-questionalias การทดสอบชื่อถูกต้อง/หลายเกม/CS3/Tekken7/unsupported/no-ruleยังอยู่ครบ แต่targetถูกอาจยังตอบfacetผิด ดูข้อที่เหลือด้านล่าง','',
'### 2. Freeze time ถูกเลือกเป็นคำถามเวลารอบ','',
'คำถาม “CS2 timeout ตอน freeze time ได้กี่วิกี่ครั้ง” เดิมเลือกround_timeจากคำว่าfreeze timeก่อนquotaของtimeout จึงตอบ1:55/15วินาทีซึ่งเป็นคนละข้อแม้sourceCS2ถูก ตอนนี้ timeoutเป็นpropositionหลักและFreeze timeเป็นlimiting condition; คำตอบsourceคือทีมละ4ครั้ง ครั้งละ30วินาที ใช้ในช่วงFreeze time การถามround timeแยกยังตอบข้อนั้นได้','',
'### 3. Venueมีข้อมูลแต่รูปประโยคไม่เข้าgate','',
'คำถาม “สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน” มีtargetแต่ไม่เข้าpatternเดิมจึงตอบยังไม่พบด้วยconfidence0.92 เพิ่มtarget-boundvenue/location/แข่งที่ใด; อ่านs08_c01เดิมที่ระบุ1วัน ณ PSU Esports Studio - Phuket ไม่เอาตำแหน่งปุ่มหรือเวลาหยุดเกมไปเป็นสถานที่ และปี2027ไม่เอากติกา2026ไปยืนยัน','',
'### 4. ทดสอบผ่านแต่ยังตกคำถามที่ขอหลายเรื่อง','',
'Aตอบเฉพาะtimeoutใน “pause และ timeout” เกณฑ์เดิมหลายแถวตรวจroute/outcomeแต่ไม่มีpositivecontent จึงยังผ่าน ขยายrequest contractให้ทั้งtechnicalและtacticalครบ: technicalทีมละ2ครั้ง ครั้งละไม่เกิน10นาที พบปัญหาต้องแจ้งกรรมการทันที; tacticalทีมละ4ครั้ง ครั้งละ30วินาทีในFreeze time เพิ่ม18เคสและmutationที่ลบquota/เวลา/เงื่อนไขแล้วต้องfail','',
'### 5. ภาษาไทยไม่มีคำว่าrulesและgenericเวลานอกชนqualifier','',
'Bคำถาม “CS2 เวลานอกทางเทคนิคขอได้กี่ครั้ง” ไม่ผ่านlooks_like_competition_rule_query แม้routerจัดcompetition_rules เพราะrule signalsมีEnglishtimeoutแต่ไม่มีThaiequivalentที่ผูกtarget แล้วfallbackเลือกfacetpause_timeoutรวมทั้งสองข้อ `retrieval.competition_fact_cards` score0.939สูงกว่าhybrid0.506; sourcegroundingผ่านเพราะgame/sectionถูก แต่ตอบtacticalก่อนtechnicalผิดประเด็น นี่เป็นตัวอย่างว่าscoreสูงไม่ได้รับรองครบ','',
'CเปิดCS2rulegateจากtechnical/tacticalrequestและให้technicalqualifierระงับtacticalmatchเฉพาะวลีนั้น APIเคสเดียวกันเหลือtechnical2ครั้ง/10นาที/แจ้งกรรมการครบ ไม่มี4ครั้ง/30วินาที; Bใช้15.042วินาที Cเคสนี้0.268วินาที เป็นผลรายเคส ไม่ใช่latencyทุกคำถาม','',
'## ผลทดสอบและขอบของหลักฐาน','',
'| ชุด | ผล | ขอบ |','|---|---:|---|',
'| Fixtureใหม่20 | 6→20ผ่าน | ชื่อ6ข้อเป็นtarget/source checks; venue/timeoutตรวจข้อความsource |',
'| Compound/control18 | 18/18 | ทั้งสองกฎ/กฎเดียว/เงื่อนไขที่ไม่ควรปน |',
'| Unitสุดท้าย | 440/441 | 1preexistingEnglishGoldbuilder drift; errors/skips0 |',
'| APIรวมจากB+C | 941/941 | B941ครบ/C482replayed; อีก459retainจากB |',
'| Strongcompetition | 728/728 | sourceclauses/firstline/conditionsตามfixture; รวมอยู่ใน941 |',
'| หลังเปิด8090 | 46/46 | 20new+18compound+8locale |',
'| Livepath/guard | 44/44 | ทางดึง8/guard36; ไม่มีoracle occupancy |',
'| Idle10พร้อมกัน | 10/10 | locale+42games; ไม่ใช่SLAWordPress |',
'| Smoke85 | 71/85 | fail14เหมือนG6เดิม; ไม่อ้างทั้งหมดCfreeze |',
'| Baffectedsmoke16 | 11/16 | ไม่มีข้อผ่านเดิมตก |','',
'Rootinputsครบ20,327/55,583grades จากAเต็ม (preserved18,894 + resumed1,433), Baffectedreplay4,370 และClocalreplay355 ตัวเลขinput/gradeเท่าเดิม ข้อมูลที่retainมีprovenance ไม่อ้างทุกรอบรันใหม่หมด ส่วนextra970inputs/981gradesมีobservations120ที่ยังไม่มีhumanoracle; Crun321affected/retain649','',
'Rootมีอย่างน้อย1gradefailลด1,905→1,898 และnewfailedgrades0 แต่ไม่นับเป็นansweraccuracyเดียวเพราะเกณฑ์ต่างรุ่นและข้อมูลซ้ำ/historical/route-only การเปรียบเทียบV2ด้วยclassifierและoverlayเดียวกัน: clean1,772→1,772; noisy1,665→1,672; cleanผ่าน/noisyตก118→111 ไม่เอาG6เดิม1740/1640มาเทียบตรงกับCเพราะเพิ่มrecognizedmodeในgrader','',
'111คู่ที่เหลือ: ไทย57 อังกฤษ54; มีpositivecontent43 ไม่มี68; ทั้ง2000คู่มีpositivecontent894. Triageเป็นคำใบ้ไม่ใช่ยืนยันสาเหตุเดียวทุกข้อ:','']
for name,count in remaining['triage_hints'].items():lines.append(f'- {name}: {count}')
lines+=['','## ข้อที่ยังผิด/ไม่ครบที่ยืนยันจากคำตอบได้ และลำดับต่อไป','',
'1. **P0 live-intentหายเมื่อคำผิด**: “วางหรือเปล่า” ของNintendoพร้อมวันเวลาไปcalendarแทนlive การดึงข้อมูลที่ถูกต้องต้องมีfreshness gateตั้งแต่intentจนrender; รายงานofflineนี้ไม่พิสูจน์bookingจริง','',
'2. **P1 targetถูกแต่propositionผิด**: “อารีน่สออฟเวเลอร์ ... จำนวผู้เล่นต่อทีม” ตอบห้ามชื่อตัวละครหยาบคายแทนcount (confidence0.84). SourceRoVs06_c01ระบุโหมดการแข่งขัน5v5ใน4.2.1; การตอบจำนวนผู้เล่นในเกมต้องอ้าง5v5และแยกจากสมาชิกลงทะเบียน/สำรองที่ไม่ควรเดา ต้องกู้facetพร้อมบริบทและใส่source-derivedcontentoracle','',
'3. **P1 หลายข้อขาดบางข้อ/หัวข้ออย่างเดียว**: “คุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน” ตอบเพียงlate-registration และ “การตั้งค่าในเกม” ได้แค่ชื่อหัวข้อ กู้ชื่อสำเร็จไม่ได้แก้สองอย่างนี้ อิสระrequestcontractในr31มี3กลุ่มCS2เท่านั้น งานต่อไปต้องทำrequested-ledgerให้ครบfacetsเหล่านี้พร้อมoverviewvsdetails/negativecontrols','',
'4. **P1 real-word errorsและภาษาทั่วไป**: “Wherw can you pay VALORANT” ไปservice_feeจากpay; ห้ามแก้pay→playเสมอ ต้องใช้location/zonecontextหรือถามเมื่อกำกวม ส่วน“โซซนไหน”ทำPokémon Championsได้no_answerทั้งที่cleanมีSwitch ให้ทดสอบboundedfacetrecoveryพร้อมcontent','',
'5. **P2 eval/source/English**: FrozenEnglishbuilder1unitfailยังอยู่; extrahistorical228ยัง0/228เพราะmodeเก่า เป็นต้น ห้ามเติมoracleด้วยคำตอบที่ระบบสร้างเอง คำแปลเครื่อง/shadow1600ไม่ใช่humanapproved ดูFlowคำถามเจ้าของเรื่องฉบับกฎและส่วนที่ขาด','',
'6. **P2 queue503**: concurrentwebsmokefailภายใต้โหลดเดิม ส่วนidle10ผ่าน การแก้UIรอ/ retryและวัดslowupstreamก่อนเพิ่มworkerเป็นงานแยกจากsemanticcorrectness','',
'## Extra corpus — rawและdiagnosticแยก','', '| Corpus | ผ่านเกณฑ์เดิม | ไม่บังคับmodeเก่าเพื่อวิเคราะห์ |','|---|---:|---:|']
for name,c in extra['counts'].items():lines.append(f"| {name} | {c['legacy_passed']}/{c['total']} | {c['diagnostic_without_mode_passed']}/{c['total']} |")
lines+=['','การตัดmodegateในcolumnขวาเป็นdiagnostic ไม่ใช่ผลผ่านใหม่หรือsemanticvalidation; rawยังอยู่ครบ ไม่มีnewfailedgradeจากextraC','', '## คะแนนที่เลือกคำตอบหมายถึงอะไร','',
'Route confidenceเช่น0.97, retrieval0.84 หรือcandidate0.939เป็นscoreจากกฎ/หลักฐานที่matcherมองเห็น ไม่ใช่โอกาส99%ว่าประโยคถูกครบ เมื่อmatcherไม่เห็นfacetที่หายไปก็ไม่มีcandidateนั้นให้เทียบ Validatorจึงต้องเริ่มจากโจทย์และมีpositiveoracleสำหรับสิ่งที่ต้องปรากฏ เช่นจำนวนครั้ง+เวลา+เงื่อนไข ทั้งหมดต้องตรงsource ห้ามรับคำตอบเพราะsourceIDถูกอย่างเดียว','',
'## การรักษางานเดิม','',
'ตรวจhash584owner/data/Goldไม่เปลี่ยน Snapshot258ไม่เปลี่ยน Originaltestsไม่เปลี่ยน Runtimeappในprojectตรงแพ็กเกจCทุกไฟล์ Oldlogs/rawresults/แพ็กเกจA,Bยังอยู่ ไม่มีGitreset/stash/commitหรือการลบไฟล์ เก็บflow_initialก่อนแก้Flowฉบับสุดท้าย','',
'## ไฟล์หลักฐาน','']
for name in ['release_preflight_C.json','preservation_package_C.json','API_FINAL_B_C_SUMMARY.json','R31_C_FULL_ANALYSIS_SUMMARY.json','R31_COMMON_SCORING_COMPARISON.json','R31_C_FAILURE_INVENTORY.jsonl','R31_REMAINING_PAIRED_DETAILS.jsonl','R31_C_CHANGED_ANSWERS.jsonl','R31_C_EXTRA_CORPUS_ANALYSIS.json','B_THAI_TECHNICAL_FAILURE.json','REMAINING_ROV_5V5_SOURCE.json']:
    lines.append('- '+link(name))
lines+=['','## สิ่งที่ไม่ได้รับรอง','',
'ไม่ได้รับรองทุกประโยคพิมพ์ผิด ไม่ได้ยืนยันsourceconflictsจากเจ้าของใหม่ และไม่ได้พิสูจน์ว่าง/ถูกจองของข้อมูลจริง การพักเก็บbookingoracleของผู้ใช้ยังมีผล การผ่านWordPress/HTTPเป็นหลักฐานการเชื่อมต่อเท่านั้น','']
with (r/'FINAL_RESULTS_TH.md').open('x',encoding='utf-8') as out:out.write('\n'.join(lines))
# Include a readable review of every changed answer without collapsing raw traces.
review=['# คำตอบที่เปลี่ยนจาก G6 — 57 inputs','', 'รายการนี้เก็บคำถาม/คำตอบเดิม/คำตอบใหม่/เกณฑ์เพื่อreview ไม่รับรองsemanticcorrectnessทั้งหมด ชื่อเกมที่กู้ได้มีคำตอบหัวข้อผิดหรือขาดรายละเอียดอยู่ ดูFINAL_RESULTS_TH','']
for index,line in enumerate((r/'R31_C_CHANGED_ANSWERS.jsonl').open(encoding='utf-8'),1):
    x=json.loads(line);review += [f'## {index}. {x["question"]}','',f'ภาษา: {x["locale"]}; modeเดิม `{x["previous_signature"][1]}` → ใหม่ `{x["new_result"]["mode"]}`','', '### เดิม','',x['previous_signature'][0], '', '### ใหม่','', x['new_result']['answer'],'',f'Route: {json.dumps(x["new_result"].get("route"),ensure_ascii=False)}; confidence: {x["new_result"].get("confidence")}','', 'Expectedและtraceเต็ม: R31_C_CHANGED_ANSWERS.jsonl key '+x['key'],'']
with (r/'CHANGED_ANSWERS_REVIEW_TH.md').open('x',encoding='utf-8') as out:out.write('\n'.join(review))
stamp=dict(runtime=health['runtime']['version'],revision='C',final=True,web='http://127.0.0.1:8090/',production_launcher_pid=19624,test8091_stopped=True,postrelease46=True,pathguard44=True,idle10=True,real_occupancy_verified=False,owner_approved=False,scope='r31 three source-clause groups + game-name recovery completed. Remaining P0/P1/P2 listed; not every semantic error solved.')
with (r/'SESSION_FINAL_STATE.json').open('x',encoding='utf-8') as out:json.dump(stamp,out,ensure_ascii=False,indent=2)
handoff=f'''# r31 handoff — 2 Oct 2026 (Bangkok)

- Project: `{p}`
- Report: `{r}`
- Flow: `{flow_path}`
- Web8090 runs C package, launcherPID19624 (verify commandline before stopping); record `web_chat_runs/r31_ready_8090_03beef33c7.json`.
- Package: `{p/'owner_local_delivery_20261002_question_target_content_r31_C/PSU_Esports_Chatbot_Local'}`
- Test8091 stopped; every raw A/B/C/package retained.
- Source/data584 unchanged; snapshots258/originaltests unchanged. No commits/reset/stash/delete.
- New production modules competition_name_recovery and competition_request_contract. Existing six app files changed. tests/test_competition_reliability_r31.py has16methods. eval_contract_v2 recognizes stable source-detail answer mode; compare both generations with same classifier, not historical scores directly.
- API941 assembled B941+C482affected, passes941. postrelease46/pathguard44/idle10pass. Unit440/441 known Gold English builder failure; smoke71/85 unchangedfailures, Baffected11/16. Owner/source approval and actual booking oracle still not completed; user paused real collection.
- A full20327/55583 includes preserved18894+resume1433 after process interruption. B4370replayed, C355replayed; final_C_all_results contains provenance, not a new fullC execution.
- Common scoring2000pairs: G6clean1772/noisy1665/regression118; Cclean1772/noisy1672/regression111. Improved7, newlyfailed0. Remaining111 TH57/EN54 with43positivecontentand68none. Fullrootfailedunique1898 (not semantic wrong count), triage/fulltrace preserved.
- Next priorities: P0 lost live intent วาง vsว่าง; P1 target-only recovery still wrong facet/heading-only or partialmulti-facet (RoVจำนว, CS2eligibility/roster/registration/settings); P1 real-word play/pay + zone typos; P2 oracle/source gaps and queue503loaded.
- Read FINAL_RESULTS_TH.md/Flow and CHANGED_ANSWERS_REVIEW_TH.md before more edits. Don't call all7meaning-correct; some onlytarget/outcomeevidence.
- Permissions for project writes/network must be obtained if absent in nextturn. No agents/goal/automation requested.
'''
with (root/'R31_SESSION_HANDOFF_20261002_C.md').open('x',encoding='utf-8') as out:out.write(handoff)
print(json.dumps(dict(report=str(r/'FINAL_RESULTS_TH.md'),flow=str(flow_path),handoff=str(root/'R31_SESSION_HANDOFF_20261002_C.md'),web=stamp['web']),ensure_ascii=False),flush=True)
