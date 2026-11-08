import json, re, shutil, hashlib, uuid
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT = BASE / ('r40_targeted_flow_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '_' + uuid.uuid4().hex[:6])
OUT.mkdir()
with (BASE / 'r40_current_path.txt').open('x', encoding='utf-8') as f:
    f.write(str(OUT))
before = OUT / 'before'
manifest = {}
for folder in ('app', 'web_chat', 'deployment_templates', 'tests'):
    for p in (ROOT / folder).rglob('*'):
        if not p.is_file() or '__pycache__' in p.parts:
            continue
        rel = p.relative_to(ROOT)
        dst = before / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dst)
        manifest[rel.as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
for rel in ('booking_dashboard/center_schedule.json', 'data/curated/service_policy_answers.json',
            'data/competition_rules/competition_rule_chunks.jsonl', 'data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl',
            'app/calculator/service_fee.py'):
    p = ROOT / rel
    if p.exists():
        manifest[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
with (OUT / 'before_manifest.json').open('x', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

inventory = (BASE / 'PSU_ESPORTS_REMAINING_WORK_R39_3_20261006.md').read_text(encoding='utf-8')
items = re.findall(r'^### (B\d{3}) — (.*?)\n(.*?)(?=^### B\d{3} —|^## )', inventory, re.M | re.S)
assert len(items) == 66
streams = [
 ('R', [1,2,3,4,5,45,50,52,59,66], 'รุ่น/แพ็กเกจ/หลักฐาน',
  'ตรวจ health/version/root/config และก่อนแก้ → สร้าง release ใหม่แยก → ตรวจ hash/CRC/launcher → เปิดเฉพาะ process ของรอบนี้ → ตรวจ URL ที่ผู้ใช้เข้า',
  'deployment_templates, tools/build_owner_local_package.ps1, web_chat/app.js, ตัวเก็บหลักฐานใน workspace',
  'พอร์ตชน; เปิดซ้ำ; path ไทย/ช่องว่าง; wrong instance; Git return code; data/index คนละรุ่น; cache 0/10; โมเดลหาย',
  'ใช้แพ็กเกจที่ตรวจจริง ไม่คัดลอก owner data/log เก่ามารวมชุดแจก'),
 ('L', [6,64], 'เวลาและการเรียกโมเดล',
  'แยก stage timings → ตรวจว่าขาด slot เดียวจริง → ใช้ deterministic clarification ที่แคบ → ตรวจ negative requests → วัด cold/warm และ model-call count',
  'app/pipeline/engine.py, ambiguity_gate.py, bilingual_english.py, โมดูล shared control request',
  'คำขอปุ่มหลายสำนวน TH/EN; unknown title; ชื่อภาคผิด; ปุ่มจอง; keyboard damage; คำถามใหม่ที่มี negation',
  'ไม่มี universal_intent/semantic model call ในเส้นทางที่ชัด ไม่รับรอง latency เป็น SLA'),
 ('D', [7,8,9,10,11,12,13,18,54,55], 'สถานะบทสนทนาและขอบเขต',
  'อ่าน state ที่อนุญาต → จำแนก new/selection/correction/continuation → merge ค่าที่ผู้ใช้เลือก → สร้างงานราย target → execute/contract → commit revision และ delivery',
  'app/session/context_resolver.py, conversation_store.py, conversation_plan.py, app/pipeline/engine.py',
  'เลือกหนึ่ง/สองเกม; เลือกสองโซน; เปลี่ยนหัวข้อ; all ไม่มีบริบท; all สองมิติ; partial failure; session ใหม่/TTL; source เปลี่ยน; retry',
  'คง operation/filter ของผู้ใช้ ไม่อ่าน offered list เป็น selected และ explicit new request ชนะบริบท'),
 ('N', [14,15,16,17,19,56], 'ภาษาพูด/คำผิด/ภาษา/ภาคเกม',
  'เก็บข้อความเดิม → เสนอ candidate ที่มีขอบเขต → กันตัวเลข/negation/ชื่อภาค → ประเมิน context+margin → รับ/ถามยืนยัน → trace recovery',
  'app/pipeline/input_recovery.py, entity_resolver.py, game_edition_guard.py, context_resolver.py, bilingual_english.py',
  'คำเบิ้ล/ขาด/สลับ/แป้นข้างเคียง; price/rice; pay/play; unknown title; เลขโรมัน; mixed language; general ที่มี PC',
  'clean input ไม่ถอยหลัง การแก้ไม่ลบความหมายที่ผู้ใช้ตั้งใจ และไม่มี alias ต่อประโยคเพื่อดันคะแนน'),
 ('O', [20,21,22,23,24,25,26,27,28,29,30,31,32], 'ข้อเท็จจริงและเจ้าของ',
  'จำแนก missing/conflict/stale → รวบรวม clause/วันที่/ID → ทำคำถามผู้มีอำนาจ → เมื่อได้คำตอบตรวจ source/hash → แปล/build release → paired regression',
  'data/competition_rules, data/curated, data/locales/en, source registry; รักษาต้นฉบับเดิม',
  'ราคา recorded vs current; pause conflicts; RoV ขาด; roster vs format; carry vs consume; source ที่ไม่มีห้ามอนุมาน',
  'ระหว่างรอให้ตอบข้อจำกัดตามจริง ห้ามเดาราคา/โทษ/สิทธิ์ และห้ามเปิด draft เป็น approved'),
 ('B', [33,34,35,36,37,57,58], 'Booking/calendar/เวลา',
  'ตีความ target+date+window → โหลด source/calendar identity → snapshot เดียว → คำนวณ blocked interval → free/booked/closed/unknown → timestamp/privacy contract',
  'app/booking/live_status.py, app/calendar/service_calendar.py, booking_dashboard/server.py; ตารางเจ้าของไม่แก้โดยเดา',
  '12:00/12:30/13:00; maintenance/special close; exact end/start; VR30 full-hour occupancy; cancellation; partial booking; midnight; live down',
  'fixture truth แยก live oracle; งานจริงยังพัก ไม่สร้าง/ยกเลิก/ถือสิทธิ์การจอง'),
 ('E', [38,39,40,41,42,62,63], 'Ground Truth/trace/semantic evidence',
  'freeze input/source/oracle → ตรวจ expected task/facts+forbidden facts → run targeted → จัด failure layers → adjudicate code/gold/source → replay+holdout',
  'tests เฉพาะเรื่อง, workspace runners, trace/decision artifacts, retrieval/evidence pack/answer contracts',
  'ชื่อมีแต่ operation ผิด; clause หลักขาด exception; false no-answer; unnecessary clarification; grade เดิมผิด; wrong source/year',
  'ไม่ใช้ HTTP 200/confidence/validation.ok แทนตอบถูก ไม่เปลี่ยน gold โดยไม่เก็บเหตุผล'),
 ('F', [43,44,46], 'Fault/load/log',
  'สร้าง process/adapter ที่แยก → ฉีด fault จุดเดียว → ตรวจ state/delivery/log หลัง fault → เพิ่มโหลดตามความจำเป็น → report ทุก error/timeout',
  'app/web_api/pipeline_supervisor.py, server.py, session store/chat_logger และ runner ที่แยก',
  'worker crash/hang; stale revision; network cut; logger fail; restore; 5/10/20/30 users เมื่อถึงระยะนั้น',
  'ไม่ฆ่า process ผู้ใช้เดิม ไม่ลบ log และไม่อนุมาน concurrency จาก serial tests'),
 ('P', [47,48,49,65], 'การใช้งานต่อเนื่อง/ภายนอก/เจ้าของเพิ่มข้อมูล',
  'กำหนด deployment/roles/retention → เลือกสิ่งจำเป็น → implementation แบบแยก → ตรวจ access/startup/review/publish → รับรองตามสภาพแวดล้อมจริง',
  'deployment configuration, admin workflow, data publishing tools; Local default เดิมยังคงใช้ได้',
  'เปิดเครื่อง; role access; no-log-in-sharing-package; draft ไม่เข้ารัน; owner UI approval; rollback',
  'เป็นระยะตามการใช้งาน ไม่เปลี่ยนระบบภายนอก/นโยบายแทนผู้ใช้'),
 ('K', [51,53,60,61], 'อัปเดตข้อมูล/คำแปล/จำนวน/แหล่งอ้างอิง',
  'snapshot ต้นทาง → classify change/effective date → invalidate locale → build projections/index → ตรวจ facts/counts/citations → publish release ที่ตรวจแล้ว',
  'data/content, data/locales/en, knowledge inbox, catalog/formatters และ viewer หากเลือกทำ',
  'Thai field เปลี่ยนแล้ว English stale; unique games vs zone sum; คน vs เครื่อง; local citation; publish ไม่ครบ',
  'แสดง source date/release ไม่เรียก static source ว่าเพิ่งอ่านเว็บ และไม่เปิดไฟล์ส่วนตัวผ่าน viewer'),
]
mapping = {}
for s in streams:
    for n in s[1]:
        assert n not in mapping, n
        mapping[n] = s
assert set(mapping) == set(range(1,67))

intro = '''# Flow พัฒนาและตรวจเฉพาะปัญหา 66 รายการ — r40

วันที่ 6 ตุลาคม 2026 / Asia Bangkok; เริ่มจาก r39.3

## 0. สถานะและข้อกำหนด

เอกสารนี้กำหนดวิธีแก้/ตรวจครบ B001–B066 ไม่ได้ประกาศว่าทุกงานเสร็จแล้ว สถานะการลงมือจริงอยู่ในรายงานผลคู่กัน ใช้ baseline และ targeted tests ไม่รัน full corpus สองหมื่นกว่าข้อ ไม่แก้ข้อมูลเจ้าของ/นโยบายที่ยังไม่ยืนยัน ไม่เก็บ booking truth จริงที่ผู้ใช้พักไว้ และไม่เปิดบริการสาธารณะหรือธุรกรรมจองเพิ่มเอง

ได้รับสิทธิ์เขียนต้นทางผ่านระบบในรอบนี้ สำรอง app/web/templates/tests ที่มีอยู่ก่อนแก้และ hash ข้อมูลที่ต้องรักษา ใช้ผล Git จาก workdir ตรง ไม่อนุมาน success จากไฟล์ stdout ที่เป็น error สร้าง release/process/log ใหม่ ไม่ทับ r39.3 และไม่หยุดชุดเดิมของผู้ใช้

## 1. หลักจากงานวิจัยและวิธีนำมาใช้

- [CheckList — Ribeiro et al., ACL 2020](https://aclanthology.org/2020.acl-main.442/): ใช้เมทริกซ์ความสามารถกับการทดสอบพฤติกรรม แยกเคสพื้นฐาน การเปลี่ยนที่ควรคงผล และการเปลี่ยนที่ต้องเปลี่ยนผล ใช้คู่คำสะกดผิด/คำสะอาด กับตัวเลข/negation ที่ต้องรักษา
- [RADDLE — Peng et al., ACL 2021](https://aclanthology.org/2021.acl-long.341/): ทดสอบบทสนทนาต่อเนื่อง ภาษาแปรผัน entity ใหม่และนอกหมวด จึงต้องตรวจทุก turn และ unknown targets แยกจาก typo ที่ควรกู้ได้
- [CheckDST — Cho et al., Findings EMNLP 2022](https://aclanthology.org/2022.findings-emnlp.391/): วินิจฉัยจุดแข็ง/จุดอ่อนและ failure modes แยก แทนรวม accuracy เดียว ใช้แยก context/target/entity/scope errors
- [Misspelling Semantics in Thai — Nakwijit & Purver, LREC 2022](https://aclanthology.org/2022.lrec-1.24/): งานศึกษา misspelling ในไทยพบว่ารูปสะกดอาจมีความหมายและการ normalize แบบไม่แยกแยะให้ผลเสียในงานที่ศึกษา จึงเก็บ original input ไม่บังคับแก้ทุกตัวและไม่อ้างผล sentiment ว่ารับรอง Chatbot นี้
- [Schema-Guided Dialogue Dataset — Rastogi et al.](https://arxiv.org/abs/1909.05855): ใช้ schema/slots เพื่ออธิบายบริการและสถานะ นำหลักการมาทำ request plan ไม่ได้ฝึกโมเดลใหม่หรือรับรองผล zero-shot ของระบบนี้

การใช้ paper เป็นเหตุผลออกแบบ การพิสูจน์ว่าช่วย PSU Chatbot ต้องใช้ผลก่อน/หลังจริงของเรา ไม่ถ่ายเปอร์เซ็นต์จาก paper มาเป็นผลโครงการ

## 2. Flow ร่วม

```mermaid
flowchart TD
 A[ข้อความ เวลา ภาษา session turn] --> B[อ่าน state ที่ยังใช้ได้และ recovery ที่มีขอบเขต]
 B --> C[จำแนก new request selection correction continuation]
 C --> D[รวม operation targets filters scope พร้อม provenance]
 D --> E{ขาดข้อมูลจำเป็นจริงหรือไม่}
 E -->|ขาดชัดหนึ่งส่วน| F[ถามเฉพาะช่องที่ขาดก่อนโมเดล]
 E -->|พอ| G[สร้าง expected IDs ต่อ task]
 E -->|กำกวมหลายความหมาย| H[bounded semantic review หรือถามยืนยัน]
 H --> D
 G --> I{ข้อมูล static source หรือ live}
 I -->|structured| J[คำนวณและกรองจาก facts]
 I -->|document| K[กรอง target facet version แล้ว evidence]
 I -->|live| L[read-only snapshot ที่มี date time freshness]
 J --> M[ตรวจ task facts scope locale temporal coverage]
 K --> M
 L --> M
 M --> N[complete partial missing conflict unavailable]
 N --> O[ส่งและ commit state พร้อม delivery status]
 F --> O
 O --> P[trace และ failure taxonomy]
```

ข้อแก้ไขสำคัญ: ไม่วน H→D ไม่จำกัดเวลา ใช้ semantic review เฉพาะหนึ่งครั้งภายใน deadline เดิม ถ้าไม่ได้ valid output ให้ถามเฉพาะที่ยังไม่ชัด ไม่เดาข้อเท็จจริง การแก้คำไม่เปลี่ยนเลข/รุ่น/คำปฏิเสธที่ชัด

## 3. แผนรอบนี้และเกณฑ์หยุดวน

1. ตรวจ inventory/state จริงและสำรอง → baseline targeted บน r39.3
2. Round A: ปุ่มที่ไม่มีชื่อเกม TH/EN — early deterministic clarification ก่อน semantic/model; negative controls ไม่ถูกดัก
3. Round B: เลือกหลายเกม/โซนจาก pending — คง operation และ explicit topic shift; ไม่เปลี่ยน unknown/เลขภาคเป็น known title
4. Round C: แก้จาก failure ที่พบจริง เพิ่ม holdout สำนวนใหม่และ regression ราคา/กติกา/session/fault ที่เกี่ยวข้อง จัดคู่มือ/runtime identity/config ให้ตรง
5. ส่งมอบ candidate ใหม่เมื่อ critical targeted gates ผ่าน บันทึกข้อที่เหลือว่า source gap/owner decision/coverage gap จริง

ทำรอบถัดไปเมื่อยังมี failure ที่เกี่ยวกับการแก้และมีหลักฐานสาเหตุ หยุด optional tests เมื่อ gate ที่เกี่ยวข้องเพียงพอแล้ว ไม่วนเพื่อเพิ่มตัวเลข ไม่กล่าวว่าทุก 66 ข้อเสร็จ การจบงานรอบนี้ต้องมีผลจริงและรายงาน residual ที่แก้ไม่ได้ด้วยข้อมูลที่มี

## 4. Test contract

- Freeze questions/source/oracle ก่อนแก้ เก็บ actual answer และ full debug trace แบบ JSONL แยก run ID
- ตรวจ operation/targets/required facts/forbidden facts และ first-turn clarification ไม่ใช้แค่ mode หรือชื่อปรากฏ
- Multi-select ต้องมีทุก selected target ไม่มี unselected zone; explicit new question ต้องออกจาก pending
- สำหรับ recorded prices ตรวจกับ fixture ที่บันทึกและคำเตือน validity ไม่รับรองอัตราปัจจุบัน
- เกมไม่รู้จัก/ภาคผิดต้องแจ้งข้อมูลไม่ยืนยัน ไม่ใช้ title อื่นเป็น substitute
- แยก direct source tests ที่ปิด LLM ออกจาก HTTP ที่เปิด LLM จริง และแยก fixtures จาก live booking
- แยก parse error/grader error/runtime error/source gap จึงแก้ทั้งระบบหรือ oracle ตามสาเหตุพร้อมหลักฐาน
- เก็บ clean/noisy และ invariance/directional negatives; ชุดที่ใช้พัฒนาแล้วเรียก regression ไม่เรียก holdout อีก
- ทุก run สรุป planned/executed/pass/fail/error/timeout และ latency; ไม่มีคำตอบหายจาก denominator

## 5. กลุ่มงานและ dependency

'''
for s in streams:
    intro += f'### {s[0]} — {s[2]}\n\n- รายการ: '+', '.join(f'B{n:03}' for n in s[1])+f'\n- ลำดับ: {s[3]}\n- จุดโค้ด/ข้อมูล: {s[4]}\n- เคส: {s[5]}\n- Gate: {s[6]}\n\n'
intro += '## 6. Flow เฉพาะแต่ละรายการ\n\nรายละเอียดสาเหตุและเกณฑ์จาก inventory เดิมถูกคงไว้เป็นข้อกำหนด แล้วเพิ่มขั้นลงมือและชุดตรวจต่อรายการ สถานะในหัวข้อนี้เป็นสถานะตั้งต้น ต้องใช้ execution report เพื่อทราบงานที่ทำแล้ว\n\n'
statuses = []
for ident, title, body in items:
    n = int(ident[1:]); s = mapping[n]
    status = re.search(r'\*\*สถานะ/ลำดับ:\*\* (.+)', body).group(1)
    owner = 20 <= n <= 32 or n == 33
    optional = n in (12,13,47,48,49,61,65)
    disposition = 'รอข้อมูลเฉพาะข้อเท็จจริง; ทำ guard/fixture ได้' if owner else 'ทำเมื่อเลือกการใช้งาน; ตรวจข้อจำกัดปัจจุบันได้' if optional else 'ทำเองจากหลักฐานและ targeted checks'
    intro += f'### F-{ident} — {title}\n\n- Workstream: {s[0]} / {s[2]}\n- สถานะตั้งต้น: {status}\n- วิธีจัดการ: {disposition}\n\n'+body.strip()+f'\n\n**ขั้นลงมือเฉพาะรายการ**\n\n1. อ่านหลักฐานของ {ident} และระบุ expected behavior ตามเกณฑ์เสร็จข้างบน เก็บ input/runtime/source ที่สร้างอาการ\n2. ใช้ลำดับกลุ่ม {s[0]}: {s[3]}\n3. สร้างเคสยืนยันอาการเดิม เคสสำนวนใหม่ และ negative control จากชุดต่อไปนี้: {s[5]}\n4. เชื่อมข้อของ {ident} กับเกณฑ์เนื้อหา/สถานะที่เฉพาะมัน ตรวจจุดโค้ด: {s[4]}\n5. '+('เก็บคำถามเจ้าของที่ระบุไว้พร้อม clause/วันที่ ยังไม่แก้ fact ระหว่างรอ และตรวจ safe missing/conflict/recorded answer' if owner else 'สำรองก่อนแก้และเปลี่ยนเฉพาะจุดที่ baseline/trace สนับสนุน หากไม่พบผิดให้เก็บเป็น coverage result ไม่เพิ่มเงื่อนไขโดยเดา')+f'\n6. ตรวจหลังแก้พร้อม regression ของ workstream นี้ Gate: {s[6]}\n7. เก็บผล/สาเหตุ/remaining limitations และเปลี่ยนสถานะ {ident} เฉพาะตามหลักฐาน ไม่ปิดรายการทั้งกลุ่มจากเคสเดียว\n\n'
    statuses.append(dict(id=ident,title=title,workstream=s[0],initial_status=status,execution_status='planned',disposition=disposition))
intro += '''## 7. ทบทวน Flow ก่อนลงมือ

| รอบ | สิ่งที่ตรวจ | สิ่งที่ปรับ |
|---|---|---|
| Review 1 | 66 IDs และการจัด dependency | ทุก ID อยู่ใน workstream เดียวครบ ไม่มีรายการ owner ถูกสั่งแก้ fact อัตโนมัติ |
| Review 2 | clarification/model/coverage | เพิ่ม original-vs-recovered negatives และ first-turn assertions; semantic review จำกัดหนึ่งครั้งใน deadline |
| Review 3 | release/live/fault/ภาษา | ค่า cache ตาม health ไม่ตาม README; read-only fixture แยก live oracle; source hash/locale/owner states แยก; stop gates ไม่บังคับรัน full corpus |

## 8. อะไรไม่ทำโดยเดา

- ไม่เปลี่ยนช่วงราคา/กติกา pause/RoV ขาด/สิทธิ์ภายนอก/อาหาร/อุปกรณ์จริง
- ไม่เปิดบริการภายนอก ไม่ตั้ง auto-start ถาวร และไม่เพิ่มการเก็บแชทถาวรตามใจ
- ไม่สลับไปใช้ Dashboard D: หรือเขียน calendar เจ้าของอัตโนมัติโดยไม่ตรวจ identity/diff
- ไม่อ้างผล unit/model-offline แทนผลเว็บที่เปิดโมเดล หรือ fixture แทนสถานะจองจริง

## 9. หลักฐานประกอบ

Inventory ฉบับ 66 รายการ, r39.3 report, r38.5 implemented C01–C32 และ source files เป็นฐาน ไม่ถือ research paper เป็นหลักฐานการผ่านของระบบนี้ รายงานรอบนี้ต้องเชื่อม raw JSONL, trace, before hashes, diff, test summary และ release identity ที่ตรวจจริง
'''
for name in ('FLOW_R40_v1.md','FLOW_R40_REVIEWED.md'):
    with (OUT/name).open('x',encoding='utf-8') as f:
        f.write(intro)
with (OUT/'BACKLOG_EXECUTION_STATUS_INITIAL.json').open('x',encoding='utf-8') as f:
    json.dump(statuses,f,ensure_ascii=False,indent=2)
print(json.dumps(dict(output=str(OUT),backups=len(manifest),flow_items=len(items),streams=len(streams)),ensure_ascii=False))
