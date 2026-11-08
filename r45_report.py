import json,re,statistics,urllib.request,hashlib
from pathlib import Path
import r45_probe as probe
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r45_current_path.txt').read_text());RELEASE=Path((OUT/'release_r45_2_path.txt').read_text())
sp=next(OUT.glob('R45_FINAL_WEB_V2*_summary.json'));s=json.loads(sp.read_text(encoding='utf-8'))
assert s['passed']==s['executed_cases']==148 and s['health']['runtime']['version']=='2026.10.07-rental-scope-r45.2'
initial=json.loads(next(OUT.glob('R45_INITIAL*_summary.json')).read_text(encoding='utf-8'))
after={r['id']:r for r in s['results']};definitions={c['id']:c for c in probe.cases()}
units={}
for p in sorted(OUT.glob('source_regression_*.json')):
    for row in json.loads(p.read_text(encoding='utf-8')):
        text=(OUT/row['evidence']).read_text(encoding='utf-8');n=re.search(r'Ran (\d+) tests',text);assert n and row['returncode']==0
        units[row['file']]=dict(methods=int(n[1]),evidence=row['evidence'])
assert sum(r['methods'] for r in units.values())==128
with urllib.request.urlopen('http://127.0.0.1:8091/health',timeout=5) as r:health=json.load(r)
assert health['runtime']['version']=='2026.10.07-rental-scope-r45.2' and health['warmup']['ok']
with (OUT/'FINAL_HEALTH_R45_2.json').open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
records=[r for case in s['results'] for r in case['records']]
rentals=[r for r in records if r['response']['mode']=='pipeline:zone_rental_fee']
assert all(r['status']==200 and r['response']['ok'] and not r['response'].get('timed_out') for r in records)
assert all(r['response'].get('validation_ok') is True for r in rentals)
audit=json.loads((OUT/'SOURCE_AUDIT_R45_2_FINAL.json').read_text())
frozen=json.loads((OUT/'release_r45_2_hashes.json').read_text());assert all(hashlib.sha256((RELEASE/r).read_bytes()).hexdigest()==v for r,v in frozen.items())
lat=dict(count=len(rentals),median_sec=round(statistics.median(r['elapsed_sec'] for r in rentals),4),max_sec=max(r['elapsed_sec'] for r in rentals))
gates=dict(version=health['runtime']['version'],http_cases=148,http_requests=s['requests'],http_passed=s['passed'],http_evidence=sp.name,unit_total=128,unit_files=units,rental_latency=lat,protected_unchanged=all(audit['protected_unchanged'].values()),workbook_unchanged=all(audit['workbooks_unchanged'].values()),source_release_parity=sum(audit['source_release_parity'].values()),live_wordpress_state_correctness_verified=False,owner_policy_newly_confirmed=False)
with (OUT/'FINAL_AUTOMATED_GATES_R45_2.json').open('x',encoding='utf-8') as f:json.dump(gates,f,ensure_ascii=False,indent=2)
analysis=['# วิเคราะห์เคสใหม่ทั้ง 40 เคส — r45','',f'ก่อนแก้ผ่าน {initial["passed"]}/40; ผิด 25 เคส เก็บผลเดิมครบ หลังแก้ทั้ง 40 อยู่ใน HTTP final ที่ผ่าน 148/148 เคส','',
'ตรวจ rate ID/value กับ original cell extraction ของ workbook r44 ไม่ใช้ HTTP 200 เป็นตัวตัดสินคำตอบ; missing field เป็นคำตอบที่ถูกต้องเมื่อ source ไม่มี policy','']
for row in initial['results']:
    c=definitions[row['id']];old=row['records'][-1]['response'];meta=next((t.get('metadata',{}) for t in old.get('trace',[]) if t.get('stage')=='zone_rental_contract'),{})
    chosen={r['id']:r['value'] for r in meta.get('returned_rates',[])}
    analysis += [f'## {row["id"]}','',f'- คำถาม/ลำดับ: {json.dumps(c["turns"],ensure_ascii=False)}',f'- ควรคืน rate IDs/values: `{json.dumps(c["expected"],ensure_ascii=False)}`',f'- ควรแจ้งข้อมูลขาด: `{c.get("missing",[])}`',f'- ก่อนแก้: {"ผ่าน" if row["passed"] else "ไม่ผ่าน"}; mode `{old.get("mode")}`; checks ที่ตก `{[k for k,v in row["checks"].items() if not v]}`',f'- เลือก rates ก่อนแก้: `{json.dumps(chosen,ensure_ascii=False)}`',f'- แผนก่อนแก้: `{json.dumps(meta.get("request_plan"),ensure_ascii=False)}`',f'- ผลเว็บหลังแก้: {"ผ่าน" if after[row["id"]]["passed"] else "ไม่ผ่าน"}', '', '**คำตอบก่อนแก้**','',old.get('answer',''),'', '**คำตอบหลังแก้**','',after[row['id']]['answer'],'']
with (OUT/'CASE_ANALYSIS_R45_ALL_TH.md').open('x',encoding='utf-8') as f:f.write('\n'.join(analysis))
report=f'''# ผลทดสอบเคสเพิ่มเติม r45.2 — 7 ตุลาคม 2026

## ผลสุดท้าย

- ชุดใหม่ 40 เคสก่อนแก้ผ่าน 15/40; พบ 25 เคสผิดหรือข้อมูลเกิน scope ที่ขอ
- หลังแก้ ชุดใหม่ 40 เคสผ่านทั้งหมด ร่วมกับเคสเดิม 103 และเคสต่อเนื่อง/ขอบเขตเพิ่ม 5 รวม **148/148 เคส HTTP, {s['requests']} requests**
- Unit ที่เกี่ยวข้อง **128/128 methods**: r45 scope 17, r44 workbook 19, dialogue/resume/schedule/booking fixtures เดิม 92
- Code/data parity source ↔ release **155/155 ไฟล์**; workbook ต้นฉบับและสำเนา unchanged; ราคาทั้งหมดและเครื่องคิดค่าบริการรายชั่วโมงเดิม unchanged
- แก้ production code เพียง `app/pipeline/zone_rental.py`; เพิ่ม `tests/test_rental_scope_r45.py`; ไม่ reset/stash/commit งานเดิมและไม่ลบ log
- เว็บที่ใช้: http://127.0.0.1:8091/ รุ่น `{health['runtime']['version']}`
- ชุด local ล่าสุด: `{RELEASE}` เปิด `Open-PSU-Esports-Background.cmd`; ไม่ได้ rebuild ชุดแจกพร้อม/ไม่มีโมเดลในรอบนี้

## เคสที่ครอบคลุม

ภาษาไทย/อังกฤษ, ประโยคยาว/สั้น, ชื่ออุปกรณ์พิมพ์เบิ้ล/ขาด เช่น cockpitt/cockpik/nintndo/playstaton, คำลงท้าย, ชื่อสินค้าเลขผิด PS55, Xbox ที่ไม่มีราคา, ครึ่งวัน/เต็มวัน, หน่วยงานภายใน/ภายนอก, ไม่เอา/ยกเว้น/not/excluding, เปลี่ยนกลุ่มหรือช่วงในคำถามต่อ, รวมอะไรบ้างแล้วกลับมาถามราคา, จองยังไง, เปลี่ยนเรื่องเกม/กฎ/เวลาเปิด, กลับไปเรื่องราคาเหมา, compound ต่างกลุ่ม/ต่างช่วง/โซนเดียวคนละเงื่อนไข, เลือก child ต่อจาก compound, ขยายทั้งหมด, ยกเลิกถามราคา

## สาเหตุและวิธีแก้

| หมวดที่ผิดในชุดใหม่ | จำนวน | สาเหตุ | การแก้ |
|---|---:|---|---|
| Grammar/คำขยาย | 1 | สำหรับ/แบบถูกมองเป็นชื่อสินค้า unknown | แยกคำโครงสร้างออกจาก noun ที่ขอ |
| ปฏิเสธกลุ่ม | 2 | เจอ internal แล้วเลือก internal แม้มี excluding/ไม่เอา | อ่าน polarity ก่อนเลือกค่า ไม่ใช้ positive substring อย่างเดียว |
| ปฏิเสธช่วง | 2 | half/full รวมกันแม้ขอ not half | ตัดช่วงที่ถูกปฏิเสธ หากปฏิเสธทุกช่วงให้ clarification |
| ทั้งหมดพร้อมยกเว้นใน followup | 2 | หลุดไป hourly หรือ reset groups/periods | ขยาย targets และคงตัวกรองที่รับแล้ว |
| Unknown menu/PS55 | 4 | ไม่รับคำตอบชื่ออย่างเดียว หรือ match PS5 เป็น prefix ของ PS55 | แยก noun choice จาก new topic; รักษาเลขสินค้า ไม่ fuzzy แก้เลข |
| Field แล้วกลับถามราคา | 2 | Generic price ไม่มี target จึงออกจาก rental | คง typed scope และเปลี่ยน requested field กลับเป็น rates |
| All Zones ตัดโซน | 2 | ยังคงใช้ราคา full package ทั้งที่ขอ modified bundle | แจ้ง custom_package missing ไม่คำนวณหรือใช้ 12,000 แทนแพ็กเกจที่ตัดโซน |
| Explicit followup | 2 | แล้ว/And rental price ถูกถือเป็นคำถามใหม่ reset scope | ยอม inherit เฉพาะ contextual link ที่ชัดเจน |
| Booking followup | 2 | จองยังไง/How do I book it ไม่คง rental domain | ตอบตรงว่าขั้นตอน rental ไม่มีใน workbook ไม่ยก play booking cap 3 sessions มาแทน |
| Compound conditions | 6 | เก็บ targets/groups/periods เป็นรายการรวม ทำ Cartesian product จนตอบเงื่อนไขที่ไม่ได้ถาม | เพิ่ม scoped_requests ต่อ clause และ render เฉพาะ target/group/period triples ที่สังกัด child นั้น |

ตัวอย่างก่อนแก้ PC เต็มวันภายนอก + VR ครึ่งวันภายใน ถูกตอบทั้งสองกลุ่ม/ทั้งสองช่วงของทั้งสองโซน หลังแก้คืนเฉพาะ `pc:external:full_day=4000` และ `vr:internal:half_day=1500`

## Regression ที่พบระหว่างแก้

1. รวม source cases 143 รอบแรกผ่าน 142/143: “both groups” ถูกจัดเป็น unknown noun หลังเพิ่มเมนูสินค้าไม่รู้จัก แก้ gating ให้คำสั่ง scope/selection ที่รู้จักมาก่อน unknown selection และเพิ่ม unit
2. เว็บ candidate .1 ผ่าน 147/148: “Competition rules for CS2” หลังคำถามราคาแบบหลายเงื่อนไขถูกคิดเป็น menu selection และเขียนทับ memory เรื่องราคา ทำให้ resume พก unknown ผิดกลับมา แก้ใช้ domain guard เดิมสำหรับ rules/games/controls/schedule ก่อน noun selection เพิ่ม unit และเพิ่ม check ว่า intermediate turn ไป competition_rules จริง
3. เว็บ candidate .2 ผ่าน 148/148 เก็บ candidate .1 พร้อม raw/failed logs ไว้ ไม่แก้ frozen release เดิม

## คะแนนและการตรวจคำตอบ

เส้นทาง rental ใช้คะแนนคงที่ .99 แปลว่า direct source route ไม่ใช่ความน่าจะเป็นว่าเข้าใจ intent ถูก 99% บั๊กก่อนแก้เกิดก่อน render จากการตี scope ผิด แม้ข้อมูลและ source hit ถูก จึงต้องตรวจ expected rate IDs/values, missing fields, intermediate topic, rendered values และ validation แยกจากคะแนน/HTTP success

ตัวเลข oracle อิง XML cells B3:E8 ของ workbook เดิมที่อ่านใน r44; unit r44 เปิด archived workbook โดยตรงและเทียบ 24 cells; ทดสอบยังแยก seating capacity จากจำนวนเครื่อง ไม่กำหนด seats เป็นผู้เล่นพร้อมกัน

เวลาคำตอบ rental ที่วัดในเว็บรอบสุดท้าย {lat['count']} requests: median {lat['median_sec']} s, max {lat['max_sec']} s; เป็น HTTP timing ไม่รวมวาดหน้าเว็บ ไม่ใช่เวลา WordPress fetch และไม่รับรองเวลาคำถาม LLM/general

## สิ่งที่ยังไม่ได้ยืนยัน

- จำนวนชั่วโมง/ช่วงเวลาของ half/full day, effective dates, ช่องทาง/มัดจำ/ยกเลิกการเช่าเหมา, ค่าเจ้าหน้าที่รวมไหม/ใครจ่าย, สิทธิ์บุคคลที่ไม่ได้จองนามหน่วยงาน, ราคา modified bundles/ส่วนลด/ต่อเครื่อง/รายชั่วโมง ยังต้องข้อมูลจากศูนย์
- รอบนี้ไม่ใช้ตารางราคาไปยืนยัน live availability ของ WordPress; booking fixture methods ผ่านไม่ได้เท่ากับตรวจสถานะจองจริงกับเจ้าของ
- “Where is the venue?” ยังเป็น english_no_answer; ในชุดเดิมเป็น negative test ไม่ให้ตอบราคา จึงไม่ถือว่าตอบคำถามสถานที่ถูกแล้ว
- 148 เคสเป็น focused regression ไม่ใช่ full 20k suite หรือการรับรองคำพิมพ์ผิดและ compound ทุกรูปแบบ; schema scoped requests จำกัด 6 children
- การยกเลิกถามราคาไป `ambiguity_clarification` ในเคสที่ลอง เป็น negative gate ว่าไม่ resend ราคา ไม่ถือว่าทดสอบข้อความยืนยันยกเลิกที่สวยงามครบแล้ว

## หลักฐาน

- `{sp.name}` และ JSONL raw ที่อ้างใน summary
- `CASE_ANALYSIS_R45_ALL_TH.md` มีคำถาม/expected/chosen plan/คำตอบก่อนและหลังทั้ง 40 เคส
- `FINAL_AUTOMATED_GATES_R45_2.json`, `FINAL_HEALTH_R45_2.json`, `SOURCE_AUDIT_R45_2_FINAL.json`, `SOURCE_CHANGE_R45_2_FINAL.diff`
- source/unit logs ทุก attempt; backup `before/`; `FLOW_R45_FINAL.md`
'''
with (OUT/'REPORT_R45_FINAL_TH.md').open('x',encoding='utf-8') as f:f.write(report)
flow='''# Flow r45 หลังทดสอบและแก้ scope ราคาเหมา

1. เก็บก่อนแก้และ expected rate IDs จาก original workbook cell extraction → new 40 cases ครอบคลุมคำปฏิเสธ/บริบท/compound → รันจริง เก็บ trace/output ตก 25 เคส
2. อ่านฟิลเตอร์ด้วย polarity ก่อน positive matching; ไม่ fuzzy เลขสินค้า; unknown product ไม่ default เป็นทุกโซน
3. หลัง ACK ใน session เดียว: แยก short selection, generic price followup, requested field, contextual explicit link, new domain; OTHER_TASK/SCHEDULE_TASK guard มาก่อน unknown noun selection
4. เก็บ scope ต่อ child ใน scoped_requests: target/group/period ไม่ผสมข้าม child; unspecified field แสดง source options ตามแผน ไม่ map individual เป็น internal/free
5. Validate child schema/ขอบเขต/subset/type → สร้าง allowed triples → อ่าน rates จาก source table → render เฉพาะ triples พร้อม source provenance
6. Modified All Zones package ไม่มี source tariff → custom_package missing; ปฏิเสธช่วงทุกแบบ → scope clarification; booking method ไม่มี → missing ไม่เอา play policy มาตัดสิน rental
7. Field followup คง child scopes; เลือก PC จาก compound คง PC's groups/periods; all rental rates ขยาย catalog; explicit resume ใช้ acknowledged archive ไม่เอา facts ตัวอย่างคำตอบมาสร้าง target
8. Source regression 142/143 พบ both groups false unknown → แก้ + unit; actual HTTP .1 147/148 พบ noun-style rules topic ถูกกินเป็น choice → แก้ domain guard + intermediate operation oracle
9. Freeze .2 ใหม่และยืนยันรุ่น/Python/warmup/readiness → HTTP final 148/148, unit methods 128/128, source-release parity 155/155, ราคากับ workbook hash เดิม
10. วิเคราะห์เป็น .md ทุกเคสใหม่; เก็บผลผิด/ก่อนแก้/release .1/logs ทั้งหมด; ไม่รัน full 20k; owner missing policies และ negative tests ไม่ถูกนับเป็น human approval หรือการยืนยัน live booking
'''
with (OUT/'FLOW_R45_FINAL.md').open('x',encoding='utf-8') as f:f.write(flow)
print('FINAL',s['passed'],s['executed_cases'],'requests',s['requests'],'unit',128,'latency',lat,'REPORT',OUT/'REPORT_R45_FINAL_TH.md')
