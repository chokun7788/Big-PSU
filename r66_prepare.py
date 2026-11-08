from pathlib import Path
import hashlib,json,shutil,sqlite3,subprocess

B=Path(__file__).resolve().parent
O=B/'r66_common_repair_20261014'
R=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
if O.exists():raise SystemExit('Preserve existing R66; do not recreate')
O.mkdir();S=O/'system';S.mkdir();manifest=[]
for folder in ('app','tools','tests','web_chat','booking_dashboard','data'):
 for p in (R/folder).rglob('*'):
  if not p.is_file():continue
  rel=p.relative_to(R)
  if any(x in rel.parts for x in ('__pycache__','logs','common_test_tmp','knowledge_inbox','human_review','migration_r63_20261013')):continue
  if rel.parts[:2]==('data','knowledge') or p.suffix in ('.pyc','.sqlite','.sqlite-wal','.sqlite-shm','.db'):continue
  target=S/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,target)
  manifest.append({'path':rel.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
for name in ('common','legacy_sources'):
 source=R/('data/knowledge/migration_r63_20261013/approved.sqlite' if name=='common' else 'data/knowledge/approved.sqlite')
 with sqlite3.connect(source.as_uri()+'?mode=ro',uri=True) as c,sqlite3.connect(O/(name+'.sqlite')) as d:c.backup(d)
original=S/'data/knowledge';original.mkdir(parents=True);shutil.copy2(O/'legacy_sources.sqlite',original/'approved.sqlite')
(O/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
catalog=json.loads((S/'app/knowledge/common/catalog.json').read_text(encoding='utf-8'))
flow='''# R66 — Flow แก้ Format กลางครบหมวด

## เป้าหมายและข้อจำกัด

ตอบเฉพาะบริการศูนย์/ร้านเกมจากข้อมูลที่ให้ ทั้งไทย/อังกฤษ ข้อมูลเก่าใน Format กลางและข้อมูลเพิ่มใหม่ใช้ตัวอ่านเดียวกัน ทดสอบเฉพาะ common ปิด/เปิด LLM ไม่รัน legacy arm ไม่แก้นโยบายที่ไม่ยืนยัน ไม่ publish draft ไม่ upgrade การแปลเป็น owner-reviewed ไม่ทับ log หรือไฟล์ต้นฉบับ

## หลักฐานและงานวิจัยที่ใช้

- [RAT-SQL](https://aclanthology.org/2020.acl-main.677/): alignment คำถามกับช่องและความสัมพันธ์ schema; ประยุกต์ใช้ graph ที่ประกาศ ไม่เดา FK จากชื่อเหมือนกัน ไม่ได้อ้างว่าใช้โมเดล RAT-SQL
- [CANARD](https://aclanthology.org/D19-1605/): คำถามต่อเนื่องต้อง resolve บริบทก่อนค้น; ใช้ typed state ที่เก็บ target/scope/needs ไม่เก็บคำตอบเป็นข้อเท็จจริง
- [Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/): บริบทยาวไม่ได้รับรองอ่านข้อมูลสำคัญได้; เลือกกฎเฉพาะหัวข้อพร้อม dependencies และลำดับ ห้ามส่งทั้งเล่มเพียงเพื่อผ่าน keyword
- [RAGAs](https://aclanthology.org/2024.eacl-demo.16/): แยก retrieval/context/answer quality; ในระบบนี้ใช้ oracle จาก source และ clause contracts ไม่ให้ LLM judge ของตัวเองเป็น gold

เครื่องมือ agent_search ของ paper-search-pro ใช้ไม่ได้ใน runtime นี้เพราะขาด pyalex จึงตรวจเอกสารต้นทางผ่าน web search แทน เป็น targeted engineering research ไม่อ้างเป็น systematic literature review

## Flow รับและตอบคำถาม

```mermaid
flowchart TD
 A[ข้อความดิบ + locale + ACK/history + clock] --> B[Normalize แบบรักษาตัวเลข/คำปฏิเสธ]
 B --> C[ตรวจ scope ร้านเกมและ live intent]
 C --> D[Resolve target จาก schema names + typed context]
 D --> E[เลือก operation/fields/facet + service/audience/platform/date]
 E --> F[ตรวจ authority, withdrawal, revision, validity]
 F --> G[ตาม declared relations หรือ migration provenance ที่ตรวจได้]
 G --> H[อ่าน known fields และ partial legacy representation]
 H --> I[เลือก clauses/controls + dependencies ตาม source]
 I --> J[ตรวจ coverage ต่อ clause และความสัมพันธ์]
 J --> K[จัดภาษาและแสดงเฉพาะเนื้อหาที่ถาม + necessary conditions]
 K --> L[ตอบ/partial/clarify/unavailable + trace + typed state]
 C --> M[Live adapter: transport/parse/freshness/availability oracle แยก]
 M --> L
 E --> N[LLM เสนอ fields ได้ในขอบเขต schema]
 N --> J
```

## วิธีแก้และ acceptance gate แยกหมวด

| หมวดปัญหา | วิธีแก้ | Gate ที่ต้องเห็น |
|---|---|---|
| Execution / ownership | guard_hits ใน retrieval branch ที่ใช้งานจริง; audit จำนวน blocked; ห้ามกลืน NameErrorหรือถอน filter | no-hit/withdrawn/owned-field ไม่ล้มและไม่คืน stale facts |
| Target collision | operation-first: game identity → controls/rules/rates; audience เป็น filter; หลาย record ชื่อเดียวไม่ใช่ primary ทุกตัว | ราคา CS2 ไม่ใช้ competition/control เป็นราคา |
| Field / intent | typed strong needs มาก่อน schema-only proposal; metadata ไม่แทน user need; proposal ที่ไม่ตรวจ relevance ต้อง clarify | disputes ไม่ตอบ dates; compound ครบ known clauses |
| Competition | facet derived จาก headings/text และ source tags; local relevance selection+dependency; numeric section ordering | เฉพาะเรื่องไม่ทั้งเล่ม; all ครบ; ไม่ข้ามเกม |
| Controls | เพิ่ม representation rows ที่เก็บ button/action/description/section พร้อม gesture unknown เฉพาะช่อง; ไม่เดา press; adapter อ่าน limitations ที่มี provenance | ปุ่ม known ยังตอบได้; platformผิดไม่ยืมชุดPC |
| Games/catalog | offered game_service เป็นฐานรายการ; filter service/platform; แยก family/edition/competitive-only | PS5 list ไม่รวม PC-only หรือ RoV เพราะมีrulebook |
| Equipment/resources | specifications/usage จาก equipment_model, resource identity/live แยก; exact source zone metadata สำหรับ migration only | ขอ PC specs ไม่คืนเครื่องทุกโซน |
| Rate | service+audience เป็น intersect filters; explicit billing relation; expired rates เป็น historical ไม่current; calculation unknown ห้ามคูณ | PC+General Adult ไม่แสดงทุกservice; ชี้expiredจริง |
| Rental/budget | half/full period, included equipment, audience, persons, notes; งบใช้ formula knownเท่านั้น; แยกavailable | budgetไม่อ้างเครื่องว่าง; ไม่รวมทุกgroupราคาเดียว |
| Calendar | timezoneจากหลักฐาน; bookable/area hoursแยก; special closure override; query dateไม่ใช้nowกรองอนาคต | 12–13no booking, maintenance, boundaries TH/EN |
| Booking | defer commonเฉพาะ live; declared physical resource/pool; unknown transportไม่อ้างfree | fixture oracle overlap/VR round/status counts |
| Localization | existing ENก่อน; proper Latin titleไม่ติด Thai marker; missing translationเป็นexplicit pending; offline review artifacts; numeric/negation/units invariant | ENไม่อ้าง reviewedเอง; no inventedpolicy |
| Dialogue | typed state พร้อม scopesและrequested fields; bare device/audience/ทั้งหมดสืบ pendingtask; new topic clear | price→PC, PS5→games, controls→button, group→members |
| Compound/all | coverageต่อ clause; partialตอบส่วนknown+clarifyเฉพาะส่วนขาด; allขยายcontentไม่internalmetadata | missing field ไม่ผ่านเป็นcomplete |
| Typo/layout | bounded unique candidates, numeric protection, repeat recovery; namescacheตามrelease; ไม่globalstripduplicates | cockpik/typosไม่เปลี่ยนPC1เป็นPC2 |
| Rendering/long | natural labels; allmetadataเฉพาะผู้ใช้ขอ; unknownที่ไม่ถามไม่spam; ruleorderจากsource occurrence | answer scopeครบ, ไม่truncateexceptions |
| Validation/confidence | separate execution/schema/coverage/source/time/locale; response unknownไม่เรียกanswered; uncalibratedไม่แปลเป็นprobability | malformed/unsupported/missingไม่ผ่านschemaเป็นcorrect |
| Evaluator | new semantic adapter version; preservelegacyGT; protocol mismatchแยกcontent; exceptionในdenominator; fixedclock+configs | coverageต่อarmและผลLLMtransportแยก |
| Runtime/performance | memoized normalized alias by names/release + upper boundpruning; boundedmodel queue/deadline; fallbackไม่stale | no overlappingtestarm; timeoutรายงานจริง |
| Owner/provenance/release | migrationใหม่versionแยก, sourcepointersตรง, no guessedprice/date/policy; publishgateคงไว้ | draftไม่ตอบproductionก่อนอนุมัติ |

## ตรวจทานและปรับ Flow รอบ 1 — อธิบายข้อมูลครบกับอ่านไม่ได้

พบข้อบกพร่องในร่าง: การเติม bindings ด้วย press จะสร้างข้อเท็จจริง; เปลี่ยน unknown เป็น knownทั้งชุดไม่ปลอดภัย; กฎทั้งหมดกับกฎเรื่องเดียวต้องแยก

ปรับ: partial representation แยก gesture unknown, preserve raw source; topic selection derived ไม่ใช่นโยบาย; unstructured text fallback เฉพาะ mappingที่มีsource และไม่ใช้เก่าทับwithdrawn

## ตรวจทานและปรับ Flow รอบ 2 — ขอบเขตและบทสนทนา

พบข้อบกพร่องในร่าง: การเลือก audienceแล้วลืม service; all games นับcompetition-only; whole-record validity ทำให้ fieldอื่นหายเพราะ optionalFKเก่า; closureอนาคตถูกnowfilter; historyสืบราคาไปถามเกม

ปรับ: intersectscopes; offeredcatalogเท่านั้น; validityตามfieldที่อ่านและrequiredpath; date-specificclosure; explicitoperationreplace และ shortselectorinherit แยก newtopic

## ตรวจทานและปรับ Flow รอบ 3 — การพิสูจน์และส่งใช้จริง

พบข้อบกพร่องในร่าง: keyword passไม่พิสูจน์semantics; fixturesไม่ใช่live; draftmigrationไม่ใช่release; modelenabledไม่แปลว่าทุกข้อcalled; logเก่าห้ามoverwrite

ปรับ: regression/source-oracleต่อหมวด พร้อม negativecounterexamplesและnew-record fixtures; fixedclock, serializedcommonoff/on; reportexecution+content+protocol+time+locale+transport; optimisticcompareก่อนdeployโค้ด; productiondataไม่activate; ownerquestionsเฉพาะfactsunknownจริง

## ลำดับลงมือและการทดสอบ

1. สำรอง live code+manifest+DB แบบ read-only backup ลง R66 ใหม่ ตรวจ Git และ source parity ก่อนแก้
2. แก้ execution/ownership, partial controls, relations/selection, rules/fields, dialogue, language/rendering, validator/performance ตามลำดับ
3. migration enrichment เป็น candidateใหม่พร้อม lineage; schema validate ทุกrecordและauditoriginalpreservation
4. tests common off/on: focused actual failuresหลายคำถาม+counterexamples, allcatalognewrecordfixtures, conversationprotocol, booking controlledoracle, modelproposalnegative/success/timeout
5. อ่านfailedcasesและปรับflow/codeเฉพาะcauseที่พิสูจน์ แล้วrerunaffectedtests; ไม่ rerun armเดิม
6. commonใหญ่ทั้ง20,554requestsหากsmallgatesยังมีcriticalfailureไม่เริ่มfull; fixedclock/reference_date; resultsappend-onlyและcheckpoint resume; ดึงR64 baselineจากlogsไม่เรียกlegacyใหม่
7. deploy code ที่ตรวจแล้วด้วยbeforehash compareและbackup เก็บcandidatedataเป็นdraft; สรุปสิ่งที่ทำ/ผล/ยังไม่verified/คำถามownerและrollbackpath

## คำถามเจ้าของที่แก้ด้วยโค้ดไม่ได้

- hourlyratesที่หมดอายุ31มีนาคม2026: ฉบับใหม่/วันเริ่มมีผลและกลุ่มที่อนุมัติคืออะไร (ไม่ยืดอายุเอง)
- หากarea opening09–12,13–18กับsourceอื่นไม่ตรง: sourceใดเป็นเวลาเปิดพื้นที่จริง และsourceใดเป็นเวลาเปิดจอง (12–13ไม่จองยืนยันแล้ว)
- account lending, compensation, mods, minors และrefundexceptionsที่ไม่มีคำตอบ: แต่ละpolicyอนุญาต/ห้าม/เงื่อนไขอะไร ไม่ใช้ร้านอื่นเป็นgold
- ambiguitybillingที่ไม่พิสูจน์จากsource: machinegroupsกับpricingserviceใดเป็นกลุ่มเดียวกัน; mappingที่มีหลักฐานทำเองก่อนถาม

## สถานะงาน

เอกสารนี้เป็น Flow ที่ผ่านการตรวจแบบ reasoning3รอบก่อนimplementation การทดสอบต้องบันทึกผลจริงหลังลงมือ ไม่ถือว่าทบทวนเอกสารคือระบบผ่านแล้ว

## Inventory ทุกหมวด schema (รวมหมวดที่ R63 ไม่มีrecords)

'''
for k in catalog:
 flow+=f"### {k['kind']}\n\nแบบฟอร์ม: {k['owner_form']}\n\n"
 flow+=' | '.join(f['key'] for f in k['fields'])+'\n\n'
 flow+='Gate: validate field/source/FK/unknown/withdrawal/locale/validity ตามชนิดข้อมูล; new-record fixture มี target ที่ไม่อยู่ในข้อมูลศูนย์จริง; ห้ามเติม facts เพื่อให้ผ่าน\n\n'
(O/'FLOW_R66_COMMON_REPAIR_TH.md').write_text(flow,encoding='utf-8')
print(json.dumps({'stage_files':len(manifest),'stage_bytes':sum(x['bytes'] for x in manifest),'schema_kinds':len(catalog),'output':str(O)}))
